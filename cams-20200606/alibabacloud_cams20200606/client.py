# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_cams20200606 import models as cams_20200606_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_openapi_util.client import Client as OpenApiUtilClient


class Client(OpenApiClient):
    """
    *\
    """
    def __init__(self, config):
        super(Client, self).__init__(config)
        self._endpoint_rule = 'regional'
        self.check_config(config)
        self._endpoint = self.get_endpoint('cams', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def check_chatapp_contacts_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = cams_20200606_models.CheckChatappContactsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.contacts):
            request.contacts_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.contacts, 'Contacts', 'json')
        body = {}
        if not UtilClient.is_unset(request.channel_type):
            body['ChannelType'] = request.channel_type
        if not UtilClient.is_unset(request.contacts_shrink):
            body['Contacts'] = request.contacts_shrink
        if not UtilClient.is_unset(request.cust_waba_id):
            body['CustWabaId'] = request.cust_waba_id
        if not UtilClient.is_unset(request.from_):
            body['From'] = request.from_
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CheckChatappContacts',
            version='2020-06-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cams_20200606_models.CheckChatappContactsResponse(),
            self.call_api(params, req, runtime)
        )

    def check_chatapp_contacts(self, request):
        runtime = util_models.RuntimeOptions()
        return self.check_chatapp_contacts_with_options(request, runtime)

    def create_chatapp_template_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = cams_20200606_models.CreateChatappTemplateShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.components):
            request.components_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.components, 'Components', 'json')
        if not UtilClient.is_unset(tmp_req.example):
            request.example_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.example, 'Example', 'json')
        body = {}
        if not UtilClient.is_unset(request.category):
            body['Category'] = request.category
        if not UtilClient.is_unset(request.components_shrink):
            body['Components'] = request.components_shrink
        if not UtilClient.is_unset(request.cust_waba_id):
            body['CustWabaId'] = request.cust_waba_id
        if not UtilClient.is_unset(request.example_shrink):
            body['Example'] = request.example_shrink
        if not UtilClient.is_unset(request.language):
            body['Language'] = request.language
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.template_type):
            body['TemplateType'] = request.template_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateChatappTemplate',
            version='2020-06-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cams_20200606_models.CreateChatappTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    def create_chatapp_template(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_chatapp_template_with_options(request, runtime)

    def delete_chatapp_template_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cust_waba_id):
            query['CustWabaId'] = request.cust_waba_id
        if not UtilClient.is_unset(request.template_code):
            query['TemplateCode'] = request.template_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteChatappTemplate',
            version='2020-06-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cams_20200606_models.DeleteChatappTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_chatapp_template(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_chatapp_template_with_options(request, runtime)

    def get_chatapp_template_detail_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cust_waba_id):
            query['CustWabaId'] = request.cust_waba_id
        if not UtilClient.is_unset(request.language):
            query['Language'] = request.language
        if not UtilClient.is_unset(request.template_code):
            query['TemplateCode'] = request.template_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetChatappTemplateDetail',
            version='2020-06-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cams_20200606_models.GetChatappTemplateDetailResponse(),
            self.call_api(params, req, runtime)
        )

    def get_chatapp_template_detail(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_chatapp_template_detail_with_options(request, runtime)

    def list_chatapp_template_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = cams_20200606_models.ListChatappTemplateShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.page):
            request.page_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.page), 'Page', 'json')
        query = {}
        if not UtilClient.is_unset(request.audit_status):
            query['AuditStatus'] = request.audit_status
        if not UtilClient.is_unset(request.cust_waba_id):
            query['CustWabaId'] = request.cust_waba_id
        if not UtilClient.is_unset(request.language):
            query['Language'] = request.language
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.page_shrink):
            query['Page'] = request.page_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListChatappTemplate',
            version='2020-06-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cams_20200606_models.ListChatappTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    def list_chatapp_template(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_chatapp_template_with_options(request, runtime)

    def send_chatapp_message_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = cams_20200606_models.SendChatappMessageShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.payload):
            request.payload_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.payload, 'Payload', 'json')
        if not UtilClient.is_unset(tmp_req.template_params):
            request.template_params_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.template_params, 'TemplateParams', 'json')
        query = {}
        if not UtilClient.is_unset(request.content):
            query['Content'] = request.content
        if not UtilClient.is_unset(request.payload_shrink):
            query['Payload'] = request.payload_shrink
        body = {}
        if not UtilClient.is_unset(request.channel_type):
            body['ChannelType'] = request.channel_type
        if not UtilClient.is_unset(request.cust_waba_id):
            body['CustWabaId'] = request.cust_waba_id
        if not UtilClient.is_unset(request.fall_back_content):
            body['FallBackContent'] = request.fall_back_content
        if not UtilClient.is_unset(request.fall_back_id):
            body['FallBackId'] = request.fall_back_id
        if not UtilClient.is_unset(request.from_):
            body['From'] = request.from_
        if not UtilClient.is_unset(request.language):
            body['Language'] = request.language
        if not UtilClient.is_unset(request.message_type):
            body['MessageType'] = request.message_type
        if not UtilClient.is_unset(request.template_code):
            body['TemplateCode'] = request.template_code
        if not UtilClient.is_unset(request.template_params_shrink):
            body['TemplateParams'] = request.template_params_shrink
        if not UtilClient.is_unset(request.to):
            body['To'] = request.to
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SendChatappMessage',
            version='2020-06-06',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cams_20200606_models.SendChatappMessageResponse(),
            self.call_api(params, req, runtime)
        )

    def send_chatapp_message(self, request):
        runtime = util_models.RuntimeOptions()
        return self.send_chatapp_message_with_options(request, runtime)
