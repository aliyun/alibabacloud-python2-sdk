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

    def bee_bot_associate_with_options(self, tmp_req, runtime):
        """
        You can call this operation up to 100 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        

        @param tmp_req: BeeBotAssociateRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: BeeBotAssociateResponse
        """
        UtilClient.validate_model(tmp_req)
        request = cams_20200606_models.BeeBotAssociateShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.perspective):
            request.perspective_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.perspective, 'Perspective', 'json')
        body = {}
        if not UtilClient.is_unset(request.chat_bot_instance_id):
            body['ChatBotInstanceId'] = request.chat_bot_instance_id
        if not UtilClient.is_unset(request.cust_space_id):
            body['CustSpaceId'] = request.cust_space_id
        if not UtilClient.is_unset(request.isv_code):
            body['IsvCode'] = request.isv_code
        if not UtilClient.is_unset(request.perspective_shrink):
            body['Perspective'] = request.perspective_shrink
        if not UtilClient.is_unset(request.recommend_num):
            body['RecommendNum'] = request.recommend_num
        if not UtilClient.is_unset(request.session_id):
            body['SessionId'] = request.session_id
        if not UtilClient.is_unset(request.utterance):
            body['Utterance'] = request.utterance
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='BeeBotAssociate',
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
            cams_20200606_models.BeeBotAssociateResponse(),
            self.call_api(params, req, runtime)
        )

    def bee_bot_associate(self, request):
        """
        You can call this operation up to 100 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        

        @param request: BeeBotAssociateRequest

        @return: BeeBotAssociateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.bee_bot_associate_with_options(request, runtime)

    def bee_bot_chat_with_options(self, tmp_req, runtime):
        """
        You can call this operation up to 100 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        

        @param tmp_req: BeeBotChatRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: BeeBotChatResponse
        """
        UtilClient.validate_model(tmp_req)
        request = cams_20200606_models.BeeBotChatShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.perspective):
            request.perspective_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.perspective, 'Perspective', 'json')
        if not UtilClient.is_unset(tmp_req.vendor_param):
            request.vendor_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.vendor_param, 'VendorParam', 'json')
        body = {}
        if not UtilClient.is_unset(request.chat_bot_instance_id):
            body['ChatBotInstanceId'] = request.chat_bot_instance_id
        if not UtilClient.is_unset(request.cust_space_id):
            body['CustSpaceId'] = request.cust_space_id
        if not UtilClient.is_unset(request.intent_name):
            body['IntentName'] = request.intent_name
        if not UtilClient.is_unset(request.isv_code):
            body['IsvCode'] = request.isv_code
        if not UtilClient.is_unset(request.knowledge_id):
            body['KnowledgeId'] = request.knowledge_id
        if not UtilClient.is_unset(request.perspective_shrink):
            body['Perspective'] = request.perspective_shrink
        if not UtilClient.is_unset(request.sender_id):
            body['SenderId'] = request.sender_id
        if not UtilClient.is_unset(request.sender_nick):
            body['SenderNick'] = request.sender_nick
        if not UtilClient.is_unset(request.session_id):
            body['SessionId'] = request.session_id
        if not UtilClient.is_unset(request.utterance):
            body['Utterance'] = request.utterance
        if not UtilClient.is_unset(request.vendor_param_shrink):
            body['VendorParam'] = request.vendor_param_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='BeeBotChat',
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
            cams_20200606_models.BeeBotChatResponse(),
            self.call_api(params, req, runtime)
        )

    def bee_bot_chat(self, request):
        """
        You can call this operation up to 100 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        

        @param request: BeeBotChatRequest

        @return: BeeBotChatResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.bee_bot_chat_with_options(request, runtime)

    def create_chatapp_template_with_options(self, tmp_req, runtime):
        """
        ### QPS limit
        You can call this operation up to 5 times per second per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation.
        

        @param tmp_req: CreateChatappTemplateRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateChatappTemplateResponse
        """
        UtilClient.validate_model(tmp_req)
        request = cams_20200606_models.CreateChatappTemplateShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.components):
            request.components_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.components, 'Components', 'json')
        if not UtilClient.is_unset(tmp_req.example):
            request.example_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.example, 'Example', 'json')
        query = {}
        if not UtilClient.is_unset(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        body = {}
        if not UtilClient.is_unset(request.category):
            body['Category'] = request.category
        if not UtilClient.is_unset(request.components_shrink):
            body['Components'] = request.components_shrink
        if not UtilClient.is_unset(request.cust_waba_id):
            body['CustWabaId'] = request.cust_waba_id
        if not UtilClient.is_unset(request.example_shrink):
            body['Example'] = request.example_shrink
        if not UtilClient.is_unset(request.isv_code):
            body['IsvCode'] = request.isv_code
        if not UtilClient.is_unset(request.language):
            body['Language'] = request.language
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.template_type):
            body['TemplateType'] = request.template_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
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
        """
        ### QPS limit
        You can call this operation up to 5 times per second per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation.
        

        @param request: CreateChatappTemplateRequest

        @return: CreateChatappTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_chatapp_template_with_options(request, runtime)

    def delete_chatapp_template_with_options(self, request, runtime):
        """
        ### QPS limit
        You can call this operation up to 5 times per second per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation.
        

        @param request: DeleteChatappTemplateRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteChatappTemplateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not UtilClient.is_unset(request.cust_waba_id):
            query['CustWabaId'] = request.cust_waba_id
        if not UtilClient.is_unset(request.isv_code):
            query['IsvCode'] = request.isv_code
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
        """
        ### QPS limit
        You can call this operation up to 5 times per second per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation.
        

        @param request: DeleteChatappTemplateRequest

        @return: DeleteChatappTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_chatapp_template_with_options(request, runtime)

    def get_chatapp_template_detail_with_options(self, request, runtime):
        """
        ### QPS limit
        You can call this operation up to 5 times per second per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation.
        

        @param request: GetChatappTemplateDetailRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: GetChatappTemplateDetailResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not UtilClient.is_unset(request.cust_waba_id):
            query['CustWabaId'] = request.cust_waba_id
        if not UtilClient.is_unset(request.isv_code):
            query['IsvCode'] = request.isv_code
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
        """
        ### QPS limit
        You can call this operation up to 5 times per second per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation.
        

        @param request: GetChatappTemplateDetailRequest

        @return: GetChatappTemplateDetailResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_chatapp_template_detail_with_options(request, runtime)

    def list_chatapp_template_with_options(self, tmp_req, runtime):
        """
        ### QPS limit
        You can call this operation up to 5 times per second per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation.
        

        @param tmp_req: ListChatappTemplateRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListChatappTemplateResponse
        """
        UtilClient.validate_model(tmp_req)
        request = cams_20200606_models.ListChatappTemplateShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.page):
            request.page_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.page, 'Page', 'json')
        query = {}
        if not UtilClient.is_unset(request.audit_status):
            query['AuditStatus'] = request.audit_status
        if not UtilClient.is_unset(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not UtilClient.is_unset(request.cust_waba_id):
            query['CustWabaId'] = request.cust_waba_id
        if not UtilClient.is_unset(request.isv_code):
            query['IsvCode'] = request.isv_code
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
        """
        ### QPS limit
        You can call this operation up to 5 times per second per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation.
        

        @param request: ListChatappTemplateRequest

        @return: ListChatappTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_chatapp_template_with_options(request, runtime)

    def modify_chatapp_template_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = cams_20200606_models.ModifyChatappTemplateShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.components):
            request.components_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.components, 'Components', 'json')
        if not UtilClient.is_unset(tmp_req.example):
            request.example_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.example, 'Example', 'json')
        body = {}
        if not UtilClient.is_unset(request.components_shrink):
            body['Components'] = request.components_shrink
        if not UtilClient.is_unset(request.cust_space_id):
            body['CustSpaceId'] = request.cust_space_id
        if not UtilClient.is_unset(request.cust_waba_id):
            body['CustWabaId'] = request.cust_waba_id
        if not UtilClient.is_unset(request.example_shrink):
            body['Example'] = request.example_shrink
        if not UtilClient.is_unset(request.isv_code):
            body['IsvCode'] = request.isv_code
        if not UtilClient.is_unset(request.language):
            body['Language'] = request.language
        if not UtilClient.is_unset(request.template_code):
            body['TemplateCode'] = request.template_code
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifyChatappTemplate',
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
            cams_20200606_models.ModifyChatappTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_chatapp_template(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_chatapp_template_with_options(request, runtime)

    def query_chatapp_bind_waba_with_options(self, request, runtime):
        """
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        

        @param request: QueryChatappBindWabaRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: QueryChatappBindWabaResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not UtilClient.is_unset(request.isv_code):
            query['IsvCode'] = request.isv_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryChatappBindWaba',
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
            cams_20200606_models.QueryChatappBindWabaResponse(),
            self.call_api(params, req, runtime)
        )

    def query_chatapp_bind_waba(self, request):
        """
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        

        @param request: QueryChatappBindWabaRequest

        @return: QueryChatappBindWabaResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_chatapp_bind_waba_with_options(request, runtime)

    def query_chatapp_phone_numbers_with_options(self, request, runtime):
        """
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        

        @param request: QueryChatappPhoneNumbersRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: QueryChatappPhoneNumbersResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not UtilClient.is_unset(request.isv_code):
            query['IsvCode'] = request.isv_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryChatappPhoneNumbers',
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
            cams_20200606_models.QueryChatappPhoneNumbersResponse(),
            self.call_api(params, req, runtime)
        )

    def query_chatapp_phone_numbers(self, request):
        """
        You can call this operation up to 10 times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        

        @param request: QueryChatappPhoneNumbersRequest

        @return: QueryChatappPhoneNumbersResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_chatapp_phone_numbers_with_options(request, runtime)

    def send_chatapp_mass_message_with_options(self, tmp_req, runtime):
        """
        You can call this operation up to 10 times per second per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation.
        Can support up to 1,000 numbers per request.
        

        @param tmp_req: SendChatappMassMessageRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: SendChatappMassMessageResponse
        """
        UtilClient.validate_model(tmp_req)
        request = cams_20200606_models.SendChatappMassMessageShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.sender_list):
            request.sender_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.sender_list, 'SenderList', 'json')
        body = {}
        if not UtilClient.is_unset(request.channel_type):
            body['ChannelType'] = request.channel_type
        if not UtilClient.is_unset(request.cust_space_id):
            body['CustSpaceId'] = request.cust_space_id
        if not UtilClient.is_unset(request.cust_waba_id):
            body['CustWabaId'] = request.cust_waba_id
        if not UtilClient.is_unset(request.fall_back_content):
            body['FallBackContent'] = request.fall_back_content
        if not UtilClient.is_unset(request.fall_back_id):
            body['FallBackId'] = request.fall_back_id
        if not UtilClient.is_unset(request.from_):
            body['From'] = request.from_
        if not UtilClient.is_unset(request.isv_code):
            body['IsvCode'] = request.isv_code
        if not UtilClient.is_unset(request.language):
            body['Language'] = request.language
        if not UtilClient.is_unset(request.sender_list_shrink):
            body['SenderList'] = request.sender_list_shrink
        if not UtilClient.is_unset(request.task_id):
            body['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.template_code):
            body['TemplateCode'] = request.template_code
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SendChatappMassMessage',
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
            cams_20200606_models.SendChatappMassMessageResponse(),
            self.call_api(params, req, runtime)
        )

    def send_chatapp_mass_message(self, request):
        """
        You can call this operation up to 10 times per second per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation.
        Can support up to 1,000 numbers per request.
        

        @param request: SendChatappMassMessageRequest

        @return: SendChatappMassMessageResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.send_chatapp_mass_message_with_options(request, runtime)

    def send_chatapp_message_with_options(self, tmp_req, runtime):
        """
        You can call this operation up to 200 times per second per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation.
        

        @param tmp_req: SendChatappMessageRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: SendChatappMessageResponse
        """
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
        if not UtilClient.is_unset(request.context_message_id):
            body['ContextMessageId'] = request.context_message_id
        if not UtilClient.is_unset(request.cust_space_id):
            body['CustSpaceId'] = request.cust_space_id
        if not UtilClient.is_unset(request.cust_waba_id):
            body['CustWabaId'] = request.cust_waba_id
        if not UtilClient.is_unset(request.fall_back_content):
            body['FallBackContent'] = request.fall_back_content
        if not UtilClient.is_unset(request.fall_back_id):
            body['FallBackId'] = request.fall_back_id
        if not UtilClient.is_unset(request.from_):
            body['From'] = request.from_
        if not UtilClient.is_unset(request.isv_code):
            body['IsvCode'] = request.isv_code
        if not UtilClient.is_unset(request.label):
            body['Label'] = request.label
        if not UtilClient.is_unset(request.language):
            body['Language'] = request.language
        if not UtilClient.is_unset(request.message_type):
            body['MessageType'] = request.message_type
        if not UtilClient.is_unset(request.tag):
            body['Tag'] = request.tag
        if not UtilClient.is_unset(request.template_code):
            body['TemplateCode'] = request.template_code
        if not UtilClient.is_unset(request.template_params_shrink):
            body['TemplateParams'] = request.template_params_shrink
        if not UtilClient.is_unset(request.to):
            body['To'] = request.to
        if not UtilClient.is_unset(request.tracking_data):
            body['TrackingData'] = request.tracking_data
        if not UtilClient.is_unset(request.ttl):
            body['Ttl'] = request.ttl
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
        """
        You can call this operation up to 200 times per second per account. Requests that exceed this limit are dropped and you will experience service interruptions. We recommend that you take note of this limit when you call this operation.
        

        @param request: SendChatappMessageRequest

        @return: SendChatappMessageResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.send_chatapp_message_with_options(request, runtime)
