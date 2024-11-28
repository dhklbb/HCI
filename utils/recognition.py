# -*- coding: utf-8 -*-
from huaweicloud_sis.client.rasr_client import RasrClient
from huaweicloud_sis.bean.rasr_request import RasrRequest
from huaweicloud_sis.bean.callback import RasrCallBack
from huaweicloud_sis.bean.sis_config import SisConfig
import json
import itertools
import os

# 鉴权参数
ak = "2FPGQVWZZ8NVMLXVPX2E"  # 替换为实际的ak
assert ak is not None, "Please add ak in your develop environment"
sk = "pzBo87nj25InCLcTmR3tKG9N2PdqenANCXAO5J25"  # 替换为实际的sk
assert sk is not None, "Please add sk in your develop environment"
project_id = "00a19146b82d472aa54dd25d8416a650"  # 替换为实际的project id
region = 'cn-north-4'  # 替换为实际的region

audio_format = 'pcm16k16bit'  # 音频支持格式，如pcm16k16bit，详见api文档
property = 'chinese_16k_general'  # 属性字符串，language_sampleRate_domain

class MyCallback(RasrCallBack):
    """ 回调类，用户需要在对应方法中实现自己的逻辑，其中on_response必须重写 """

    def __init__(self):
        super(MyCallback, self).__init__()
        self.results = []  # 用于保存识别结果

    def on_open(self):
        """ websocket连接成功会回调此函数 """
        print('websocket connect success')

    def on_start(self, message):
        """ websocket 开始识别回调此函数 """
        print('websocket start to recognize, %s' % message)

    def on_response(self, message):
        """ websocket返回响应结果会回调此函数 """
        print(json.dumps(message, indent=2, ensure_ascii=False))
        texts = []
        if "segments" in message:
            for segment in message["segments"]:
                if "result" in segment and "text" in segment["result"]:
                    texts.append(segment["result"]["text"])
        # text = message["segments"]['result']['text']
        self.results.append(texts)

    def on_end(self, message):
        """ websocket 结束识别回调此函数 """
        print('websocket is ended, %s' % message)

    def on_close(self):
        """ websocket关闭会回调此函数 """
        print('websocket is closed')

    def on_error(self, error):
        """ websocket出错回调此函数 """
        print('websocket meets error, the error is %s' % error)

    def on_event(self, event):
        """ 出现事件的回调 """
        print('receive event %s' % event)


def rasr_example(path):
    """ 实时语音识别demo
    :param path: 输入音频文件路径
    """
    # step1 初始化RasrClient, 暂不支持使用代理
    my_callback = MyCallback()
    config = SisConfig()
    config.set_connect_timeout(10)  # 设置连接超时, 默认是10
    config.set_read_timeout(10)  # 设置读取超时, 默认是10
    config.set_connect_lost_timeout(10)  # 设置connect lost超时, 默认是10
    rasr_client = RasrClient(ak=ak, sk=sk, use_aksk=True, region=region, project_id=project_id, callback=my_callback,
                             config=config)

    try:
        # step2 构造请求
        request = RasrRequest(audio_format, property)
        request.set_add_punc('yes')
        request.set_vad_head(10000)
        request.set_vad_tail(500)
        request.set_max_seconds(60)
        request.set_interim_results('no')
        request.set_digit_norm('no')
        request.set_need_word_info('no')

        # step3 选择连接模式
        rasr_client.continue_stream_connect(request)

        # step4 发送音频
        rasr_client.send_start()
        with open(path, 'rb') as f:
            data = f.read()
            rasr_client.send_audio(data)
        # rasr_client.send_audio(path)
        rasr_client.send_end()
        # merged_list = list(itertools.chain(*message))
        merged_text = " ".join(itertools.chain(*my_callback.results))
        return merged_text
    except Exception as e:
        print('rasr error', e)
    finally:
        rasr_client.close()

if __name__ == "__main__":
    file_path = "../test.wav"
    message = rasr_example(file_path)

    print(message)
