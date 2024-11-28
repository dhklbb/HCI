import os
import time

from utils.obs_create import file_upload, file_upload_mutilrole
from utils.recognition_commit import commit, commit_mutilrole
from utils.recognition_getres import getres, getres_mutilrole
from pydub import AudioSegment

def recognize_file(audio_path):
    filename = f"file_{int(time.time())}.wav"
    file_upload(filename,audio_path)
    data_url = f"https://dhklbb.obs.cn-north-4.myhuaweicloud.com/{filename}"
    job_id = commit(data_url)
    res = getres(job_id)
    print("录音识别中...........")
    while res.status != 'FINISHED':
        time.sleep(2)  # 每隔2秒暂停
        res = getres(job_id)
    combined_text = ""
    for segment in res.segments:
        combined_text += segment.result.text
    return combined_text

def recognize_file_mutilrole(audio_path):
    filename = f"mutilrole_file_{int(time.time())}.wav"
    parent_path = os.path.dirname(audio_path)
    new_path = os.path.join(parent_path, "8k_mutilrole_audio.wav")
    # 读取原始 WAV 文件
    audio = AudioSegment.from_wav(audio_path)
    # 将采样率更改为 8kHz
    audio_8k = audio.set_frame_rate(8000)
    # 保存为新的 WAV 文件
    audio_8k.export(new_path, format="wav")
    file_upload_mutilrole(filename,new_path)
    data_url = f"https://dhklbb.obs.cn-north-4.myhuaweicloud.com/{filename}"
    job_id = commit_mutilrole(data_url)
    res = getres_mutilrole(job_id)
    print("录音识别中...........")
    while res.status != 'FINISHED':
        time.sleep(2)  # 每隔2秒暂停
        res = getres_mutilrole(job_id)
    # 初始化两个空列表
    roles = []
    texts = []
    # 遍历 segments 提取 role 和 text
    for segment in res.segments:
        roles.append(segment.result.analysis_info.role)
        texts.append(segment.result.text)
    return roles,texts

# print(recognize_file_mutilrole('../mutilrole_course.wav'))