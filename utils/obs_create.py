from obs import ObsClient
from obs import PutObjectHeader
import os
import traceback

def file_upload(file_name,file_path):
    # 推荐通过环境变量获取AKSK，这里也可以使用其他外部引入方式传入，如果使用硬编码可能会存在泄露风险
    # 您可以登录访问管理控制台获取访问密钥AK/SK，获取方式请参见https://support.huaweicloud.com/usermanual-ca/ca_01_0003.html。
    # 运行本代码示例之前，请确保已设置环境变量AccessKeyID和SecretAccessKey
    ak = "2FPGQVWZZ8NVMLXVPX2E"
    sk = "pzBo87nj25InCLcTmR3tKG9N2PdqenANCXAO5J25"
    # 【可选】如果使用临时AKSK和SecurityToken访问OBS，则同样推荐通过环境变量获取
    # security_token = os.getenv("SecurityToken")#  server填写Bucket对应的Endpoint, 这里以华北-北京四为例，其他地区请按实际情况填写
    server = "https://obs.cn-north-4.myhuaweicloud.com"
    # 创建obsClient实例
    # 如果使用临时AKSK和SecurityToken访问OBS，需要在创建实例时通过security_token参数指定securityToken值
    obsClient = ObsClient(access_key_id=ak, secret_access_key=sk, server=server)
    try:
        # 上传对象的附加头域
        # headers = PutObjectHeader()
        # 【可选】待上传对象的MIME类型
        # headers.contentType = 'text/plain'
        bucketName = "dhklbb"
        # 对象名，即上传后的文件名
        objectKey = file_name
        # 待上传文件的完整路径，如aa/bb.txt
        file_path = file_path
        # 上传文件的自定义元数据
        # metadata = {'meta1': 'value1', 'meta2': 'value2'}
        # 文件上传
        resp = obsClient.putFile(bucketName, objectKey, file_path)
        # 返回码为2xx时，接口调用成功，否则接口调用失败
        if resp.status < 300:
            print('Put File Succeeded')
            print('requestId:', resp.requestId)
            print('etag:', resp.body.etag)
            print('versionId:', resp.body.versionId)
            print('storageClass:', resp.body.storageClass)
        else:
            print('Put File Failed')
            print('requestId:', resp.requestId)
            print('errorCode:', resp.errorCode)
            print('errorMessage:', resp.errorMessage)
    except:
        print('Put File Failed')
        print(traceback.format_exc())


def file_upload_mutilrole(file_name,file_path):
    # 推荐通过环境变量获取AKSK，这里也可以使用其他外部引入方式传入，如果使用硬编码可能会存在泄露风险
    # 您可以登录访问管理控制台获取访问密钥AK/SK，获取方式请参见https://support.huaweicloud.com/usermanual-ca/ca_01_0003.html。
    # 运行本代码示例之前，请确保已设置环境变量AccessKeyID和SecretAccessKey
    ak = "2FPGQVWZZ8NVMLXVPX2E"
    sk = "pzBo87nj25InCLcTmR3tKG9N2PdqenANCXAO5J25"
    # 【可选】如果使用临时AKSK和SecurityToken访问OBS，则同样推荐通过环境变量获取
    # security_token = os.getenv("SecurityToken")#  server填写Bucket对应的Endpoint, 这里以华北-北京四为例，其他地区请按实际情况填写
    server = "https://obs.cn-north-4.myhuaweicloud.com"
    # 创建obsClient实例
    # 如果使用临时AKSK和SecurityToken访问OBS，需要在创建实例时通过security_token参数指定securityToken值
    obsClient = ObsClient(access_key_id=ak, secret_access_key=sk, server=server)
    try:
        # 上传对象的附加头域
        # headers = PutObjectHeader()
        # 【可选】待上传对象的MIME类型
        # headers.contentType = 'text/plain'
        bucketName = "dhklbb"
        # 对象名，即上传后的文件名
        objectKey = file_name
        # 待上传文件的完整路径，如aa/bb.txt
        file_path = file_path
        # 上传文件的自定义元数据
        # metadata = {'meta1': 'value1', 'meta2': 'value2'}
        # 文件上传
        resp = obsClient.putFile(bucketName, objectKey, file_path)
        # 返回码为2xx时，接口调用成功，否则接口调用失败
        if resp.status < 300:
            print('Put File Succeeded')
            print('requestId:', resp.requestId)
            print('etag:', resp.body.etag)
            print('versionId:', resp.body.versionId)
            print('storageClass:', resp.body.storageClass)
        else:
            print('Put File Failed')
            print('requestId:', resp.requestId)
            print('errorCode:', resp.errorCode)
            print('errorMessage:', resp.errorMessage)
    except:
        print('Put File Failed')
        print(traceback.format_exc())