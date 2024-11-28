# coding: utf-8

import os
from huaweicloudsdkcore.auth.credentials import BasicCredentials
from huaweicloudsdksis.v1.region.sis_region import SisRegion
from huaweicloudsdkcore.exceptions import exceptions
from huaweicloudsdksis.v1 import *


def getres(job_id):
    ak = "2FPGQVWZZ8NVMLXVPX2E"
    sk = "pzBo87nj25InCLcTmR3tKG9N2PdqenANCXAO5J25"

    credentials = BasicCredentials(ak, sk)

    client = SisClient.new_builder() \
        .with_credentials(credentials) \
        .with_region(SisRegion.value_of("cn-north-4")) \
        .build()

    try:
        request = CollectTranscriberJobRequest()
        request.job_id = job_id
        response = client.collect_transcriber_job(request)
        print(response)
        return response
    except exceptions.ClientRequestException as e:
        print(e.status_code)
        print(e.request_id)
        print(e.error_code)
        print(e.error_msg)

def getres_mutilrole(job_id):
    ak = "2FPGQVWZZ8NVMLXVPX2E"
    sk = "pzBo87nj25InCLcTmR3tKG9N2PdqenANCXAO5J25"

    credentials = BasicCredentials(ak, sk)

    client = SisClient.new_builder() \
        .with_credentials(credentials) \
        .with_region(SisRegion.value_of("cn-north-4")) \
        .build()

    try:
        request = CollectTranscriberJobRequest()
        request.job_id = job_id
        response = client.collect_transcriber_job(request)
        print(response)
        return response
    except exceptions.ClientRequestException as e:
        print(e.status_code)
        print(e.request_id)
        print(e.error_code)
        print(e.error_msg)

if __name__ == "__main__":
    # The AK and SK used for authentication are hard-coded or stored in plaintext, which has great security risks. It is recommended that the AK and SK be stored in ciphertext in configuration files or environment variables and decrypted during use to ensure security.
    # In this example, AK and SK are stored in environment variables for authentication. Before running this example, set environment variables CLOUD_SDK_AK and CLOUD_SDK_SK in the local environment
    ak = "2FPGQVWZZ8NVMLXVPX2E"
    sk = "pzBo87nj25InCLcTmR3tKG9N2PdqenANCXAO5J25"

    credentials = BasicCredentials(ak, sk)

    client = SisClient.new_builder() \
        .with_credentials(credentials) \
        .with_region(SisRegion.value_of("cn-north-4")) \
        .build()

    try:
        request = CollectTranscriberJobRequest()
        request.job_id = "bd62bd6908ae47959f7f854348d85e80"
        response = client.collect_transcriber_job(request)
        print(response)
    except exceptions.ClientRequestException as e:
        print(e.status_code)
        print(e.request_id)
        print(e.error_code)
        print(e.error_msg)