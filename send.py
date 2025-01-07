# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
# 
# 
import os
import sys
#cURL指令的库包
import requests
from typing import List

from alibabacloud_dysmsapi20170525.client import Client as Dysmsapi20170525Client
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_dysmsapi20170525 import models as dysmsapi_20170525_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient

import json
with open('./user.json', 'r', encoding='utf-8') as user_info:
    user = json.load(user_info)

url_api_weather = 'https://devapi.qweather.com/v7/weather/3d?location='
city = user['user'][0]['location']
key = user['weather_key']
url = url_api_weather + city + '&&key=' +key 
weather_data = requests.get(url).json()

daily_weather1 = weather_data['daily'][0]
daily_weather2 = weather_data['daily'][1]
daily_weather3 = weather_data['daily'][2]

template_param = {
    "day1_text": daily_weather1["textDay"],
    "day1_max": daily_weather1["tempMax"],
    "day1_min": daily_weather1["tempMin"],
    "day2_text": daily_weather2["textDay"],
    "day2_max": daily_weather2["tempMax"],
    "day2_min": daily_weather2["tempMin"],
    "day3_text": daily_weather3["textDay"],
    "day3_max": daily_weather3["tempMax"],
    "day3_min": daily_weather3["tempMin"],
}
print(template_param)
class Sample:
    def __init__(self):
        pass

    @staticmethod
    def create_client() -> Dysmsapi20170525Client:
        """
        使用AK&SK初始化账号Client
        @return: Client
        @throws Exception
        """
        # 工程代码泄露可能会导致 AccessKey 泄露，并威胁账号下所有资源的安全性。以下代码示例仅供参考。
        # 建议使用更安全的 STS 方式，更多鉴权访问方式请参见：https://help.aliyun.com/document_detail/378659.html。
        config = open_api_models.Config(
            # 必填，请确保代码运行环境设置了环境变量 ALIBABA_CLOUD_ACCESS_KEY_ID。,
            access_key_id=os.environ['ALIBABA_CLOUD_ACCESS_KEY_ID'],
            # 必填，请确保代码运行环境设置了环境变量 ALIBABA_CLOUD_ACCESS_KEY_SECRET。,
            access_key_secret=os.environ['ALIBABA_CLOUD_ACCESS_KEY_SECRET']
        )
        # Endpoint 请参考 https://api.aliyun.com/product/Dysmsapi
        config.endpoint = f'dysmsapi.aliyuncs.com'
        return Dysmsapi20170525Client(config)

    @staticmethod
    def main(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        send_sms_request = dysmsapi_20170525_models.SendSmsRequest(
            phone_numbers=user["user"][0]["phone_number"],
            sign_name=user["sign_name"],
            template_code=user["template_code"],
            template_param=json.dumps(template_param)
            # template_param='{"day1_text":"1234","day1_min":"1234","day1_max":"1234","day2_text":"1234","day2_min":"1234","day2_max":"1234","day3_text":"1234","day3_min":"1234","day3_max":"1234","poetry":"1234"}'
        )
        runtime = util_models.RuntimeOptions()
        try:
            # 复制代码运行请自行打印 API 的返回值
            print(client.send_sms_with_options(send_sms_request, runtime))
        except Exception as error:
            # 此处仅做打印展示，请谨慎对待异常处理，在工程项目中切勿直接忽略异常。
            # 错误 message
            print(error.message)
            # 诊断地址
            print(error.data.get("Recommend"))
            UtilClient.assert_as_string(error.message)

    @staticmethod
    async def main_async(
        args: List[str],
    ) -> None:
        client = Sample.create_client()
        send_sms_request = dysmsapi_20170525_models.SendSmsRequest(
            phone_numbers=user["user"][0]["phone_number"],
            sign_name=user["sign_name"],
            template_code=user["template_code"],
            template_param=json.dumps(template_param)
            # template_param='{"day1_text":"1234","day1_min":"1234","day1_max":"1234","day2_text":"1234","day2_min":"1234","day2_max":"1234","day3_text":"1234","day3_min":"1234","day3_max":"1234","poetry":"1234"}'
        )
        runtime = util_models.RuntimeOptions()
        try:
            # 复制代码运行请自行打印 API 的返回值
            await client.send_sms_with_options_async(send_sms_request, runtime)
        except Exception as error:
            # 此处仅做打印展示，请谨慎对待异常处理，在工程项目中切勿直接忽略异常。
            # 错误 message
            print(error.message)
            # 诊断地址
            print(error.data.get("Recommend"))
            UtilClient.assert_as_string(error.message)


if __name__ == '__main__':
    Sample.main(sys.argv[1:])
