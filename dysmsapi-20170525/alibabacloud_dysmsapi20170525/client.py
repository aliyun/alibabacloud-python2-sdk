# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_dysmsapi20170525 import models as dysmsapi_20170525_models
from alibabacloud_tea_util import models as util_models


class Client(OpenApiClient):
    """
    *\
    """
    def __init__(self, config):
        super(Client, self).__init__(config)
        self._endpoint_rule = 'central'
        self._endpoint_map = {
            'ap-southeast-1': 'dysmsapi.ap-southeast-1.aliyuncs.com',
            'ap-southeast-5': 'dysmsapi-xman.ap-southeast-5.aliyuncs.com',
            'cn-beijing': 'dysmsapi-proxy.cn-beijing.aliyuncs.com',
            'cn-hongkong': 'dysmsapi-xman.cn-hongkong.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('dysmsapi', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def add_sms_sign_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dysmsapi_20170525_models.AddSmsSignResponse(),
            self.do_rpcrequest('AddSmsSign', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def add_sms_sign(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_sms_sign_with_options(request, runtime)

    def add_sms_template_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dysmsapi_20170525_models.AddSmsTemplateResponse(),
            self.do_rpcrequest('AddSmsTemplate', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def add_sms_template(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_sms_template_with_options(request, runtime)

    def delete_sms_sign_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dysmsapi_20170525_models.DeleteSmsSignResponse(),
            self.do_rpcrequest('DeleteSmsSign', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_sms_sign(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_sms_sign_with_options(request, runtime)

    def delete_sms_template_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dysmsapi_20170525_models.DeleteSmsTemplateResponse(),
            self.do_rpcrequest('DeleteSmsTemplate', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_sms_template(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_sms_template_with_options(request, runtime)

    def modify_sms_sign_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dysmsapi_20170525_models.ModifySmsSignResponse(),
            self.do_rpcrequest('ModifySmsSign', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_sms_sign(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_sms_sign_with_options(request, runtime)

    def modify_sms_template_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dysmsapi_20170525_models.ModifySmsTemplateResponse(),
            self.do_rpcrequest('ModifySmsTemplate', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_sms_template(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_sms_template_with_options(request, runtime)

    def query_send_details_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dysmsapi_20170525_models.QuerySendDetailsResponse(),
            self.do_rpcrequest('QuerySendDetails', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_send_details(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_send_details_with_options(request, runtime)

    def query_sms_sign_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dysmsapi_20170525_models.QuerySmsSignResponse(),
            self.do_rpcrequest('QuerySmsSign', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_sms_sign(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_sms_sign_with_options(request, runtime)

    def query_sms_template_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dysmsapi_20170525_models.QuerySmsTemplateResponse(),
            self.do_rpcrequest('QuerySmsTemplate', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_sms_template(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_sms_template_with_options(request, runtime)

    def send_batch_sms_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dysmsapi_20170525_models.SendBatchSmsResponse(),
            self.do_rpcrequest('SendBatchSms', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def send_batch_sms(self, request):
        runtime = util_models.RuntimeOptions()
        return self.send_batch_sms_with_options(request, runtime)

    def send_message_to_globe_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dysmsapi_20170525_models.SendMessageToGlobeResponse(),
            self.do_rpcrequest('SendMessageToGlobe', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def send_message_to_globe(self, request):
        runtime = util_models.RuntimeOptions()
        return self.send_message_to_globe_with_options(request, runtime)

    def send_sms_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            dysmsapi_20170525_models.SendSmsResponse(),
            self.do_rpcrequest('SendSms', '2017-05-25', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def send_sms(self, request):
        runtime = util_models.RuntimeOptions()
        return self.send_sms_with_options(request, runtime)
