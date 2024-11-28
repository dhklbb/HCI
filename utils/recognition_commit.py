# coding: utf-8

import os
from huaweicloudsdkcore.auth.credentials import BasicCredentials
from huaweicloudsdksis.v1.region.sis_region import SisRegion
from huaweicloudsdkcore.exceptions import exceptions
from huaweicloudsdksis.v1 import *


def commit(data_url):
    ak = "2FPGQVWZZ8NVMLXVPX2E"
    sk = "pzBo87nj25InCLcTmR3tKG9N2PdqenANCXAO5J25"

    credentials = BasicCredentials(ak, sk)

    client = SisClient.new_builder() \
        .with_credentials(credentials) \
        .with_region(SisRegion.value_of("cn-north-4")) \
        .build()

    try:
        request = PushTranscriberJobsRequest()
        configbody = TranscriberConfig(
            audio_format="auto",
            _property="chinese_16k_media",
            add_punc="yes",
            digit_norm="yes"
        )
        request.body = PostTranscriberJobs(
            data_url=data_url,
            config=configbody
        )
        response = client.push_transcriber_jobs(request)
        print(response)
        return response.job_id
    except exceptions.ClientRequestException as e:
        print(e.status_code)
        print(e.request_id)
        print(e.error_code)
        print(e.error_msg)

def commit_mutilrole(data_url):
    ak = "2FPGQVWZZ8NVMLXVPX2E"
    sk = "pzBo87nj25InCLcTmR3tKG9N2PdqenANCXAO5J25"

    credentials = BasicCredentials(ak, sk)

    client = SisClient.new_builder() \
        .with_credentials(credentials) \
        .with_region(SisRegion.value_of("cn-north-4")) \
        .build()

    try:
        request = PushTranscriberJobsRequest()
        needAnalysisInfoConfig = AnalysisInfo(
            diarization=True
        )
        configbody = TranscriberConfig(
            audio_format="auto",
            _property="chinese_8k_general",
            add_punc="yes",
            need_analysis_info=needAnalysisInfoConfig,
            digit_norm="yes"
        )
        request.body = PostTranscriberJobs(
            data_url=data_url,
            config=configbody
        )
        response = client.push_transcriber_jobs(request)
        print(response)
        return response.job_id
    except exceptions.ClientRequestException as e:
        print(e.status_code)
        print(e.request_id)
        print(e.error_code)
        print(e.error_msg)
# print(commit_mutilrole("https://dhklbb2.obs.cn-east-3.myhuaweicloud.com/file_1732679451.wav"))

# if __name__ == "__main__":
#     # The AK and SK used for authentication are hard-coded or stored in plaintext, which has great security risks. It is recommended that the AK and SK be stored in ciphertext in configuration files or environment variables and decrypted during use to ensure security.
#     # In this example, AK and SK are stored in environment variables for authentication. Before running this example, set environment variables CLOUD_SDK_AK and CLOUD_SDK_SK in the local environment
#     ak = "2FPGQVWZZ8NVMLXVPX2E"
#     sk = "pzBo87nj25InCLcTmR3tKG9N2PdqenANCXAO5J25"
#
#     credentials = BasicCredentials(ak, sk)
#
#     client = SisClient.new_builder() \
#         .with_credentials(credentials) \
#         .with_region(SisRegion.value_of("cn-north-4")) \
#         .build()
#
#     try:
#         request = PushTranscriberJobsRequest()
#         configbody = TranscriberConfig(
#             audio_format="auto",
#             _property="chinese_16k_media",
#             add_punc="yes",
#             digit_norm="yes"
#         )
#         request.body = PostTranscriberJobs(
#             data_url="https://dhklbb.obs.cn-north-4.myhuaweicloud.com/output_16khz.wav",
#             config=configbody
#         )
#         response = client.push_transcriber_jobs(request)
#         print(response)
#     except exceptions.ClientRequestException as e:
#         print(e.status_code)
#         print(e.request_id)
#         print(e.error_code)
#         print(e.error_msg)