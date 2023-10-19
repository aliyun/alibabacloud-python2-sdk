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

    def add_chatapp_phone_number_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.cc):
            body['Cc'] = request.cc
        if not UtilClient.is_unset(request.cust_space_id):
            body['CustSpaceId'] = request.cust_space_id
        if not UtilClient.is_unset(request.phone_number):
            body['PhoneNumber'] = request.phone_number
        if not UtilClient.is_unset(request.pre_validate_id):
            body['PreValidateId'] = request.pre_validate_id
        if not UtilClient.is_unset(request.verified_name):
            body['VerifiedName'] = request.verified_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddChatappPhoneNumber',
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
            cams_20200606_models.AddChatappPhoneNumberResponse(),
            self.call_api(params, req, runtime)
        )

    def add_chatapp_phone_number(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_chatapp_phone_number_with_options(request, runtime)

    def bee_bot_associate_with_options(self, tmp_req, runtime):
        """
        You can call this operation up to 100 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        

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
        You can call this operation up to 100 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        

        @param request: BeeBotAssociateRequest

        @return: BeeBotAssociateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.bee_bot_associate_with_options(request, runtime)

    def bee_bot_chat_with_options(self, tmp_req, runtime):
        """
        You can call this operation up to 100 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        

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
        You can call this operation up to 100 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        

        @param request: BeeBotChatRequest

        @return: BeeBotChatResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.bee_bot_chat_with_options(request, runtime)

    def chatapp_bind_waba_with_options(self, request, runtime):
        """
        You can call this operation up to 10 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        

        @param request: ChatappBindWabaRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ChatappBindWabaResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.waba_id):
            body['WabaId'] = request.waba_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ChatappBindWaba',
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
            cams_20200606_models.ChatappBindWabaResponse(),
            self.call_api(params, req, runtime)
        )

    def chatapp_bind_waba(self, request):
        """
        You can call this operation up to 10 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        

        @param request: ChatappBindWabaRequest

        @return: ChatappBindWabaResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.chatapp_bind_waba_with_options(request, runtime)

    def chatapp_embed_sign_up_with_options(self, request, runtime):
        """
        You can call this operation up to 10 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        

        @param request: ChatappEmbedSignUpRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ChatappEmbedSignUpResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.input_token):
            body['InputToken'] = request.input_token
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ChatappEmbedSignUp',
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
            cams_20200606_models.ChatappEmbedSignUpResponse(),
            self.call_api(params, req, runtime)
        )

    def chatapp_embed_sign_up(self, request):
        """
        You can call this operation up to 10 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        

        @param request: ChatappEmbedSignUpRequest

        @return: ChatappEmbedSignUpResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.chatapp_embed_sign_up_with_options(request, runtime)

    def chatapp_migration_register_with_options(self, request, runtime):
        """
        You can call this operation up to 10 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        

        @param request: ChatappMigrationRegisterRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ChatappMigrationRegisterResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not UtilClient.is_unset(request.phone_number):
            query['PhoneNumber'] = request.phone_number
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ChatappMigrationRegister',
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
            cams_20200606_models.ChatappMigrationRegisterResponse(),
            self.call_api(params, req, runtime)
        )

    def chatapp_migration_register(self, request):
        """
        You can call this operation up to 10 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        

        @param request: ChatappMigrationRegisterRequest

        @return: ChatappMigrationRegisterResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.chatapp_migration_register_with_options(request, runtime)

    def chatapp_migration_verified_with_options(self, request, runtime):
        """
        You can call this operation up to 10 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        

        @param request: ChatappMigrationVerifiedRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ChatappMigrationVerifiedResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not UtilClient.is_unset(request.phone_number):
            query['PhoneNumber'] = request.phone_number
        if not UtilClient.is_unset(request.verify_code):
            query['VerifyCode'] = request.verify_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ChatappMigrationVerified',
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
            cams_20200606_models.ChatappMigrationVerifiedResponse(),
            self.call_api(params, req, runtime)
        )

    def chatapp_migration_verified(self, request):
        """
        You can call this operation up to 10 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        

        @param request: ChatappMigrationVerifiedRequest

        @return: ChatappMigrationVerifiedResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.chatapp_migration_verified_with_options(request, runtime)

    def chatapp_phone_number_deregister_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.cust_space_id):
            body['CustSpaceId'] = request.cust_space_id
        if not UtilClient.is_unset(request.phone_number):
            body['PhoneNumber'] = request.phone_number
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ChatappPhoneNumberDeregister',
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
            cams_20200606_models.ChatappPhoneNumberDeregisterResponse(),
            self.call_api(params, req, runtime)
        )

    def chatapp_phone_number_deregister(self, request):
        runtime = util_models.RuntimeOptions()
        return self.chatapp_phone_number_deregister_with_options(request, runtime)

    def chatapp_phone_number_register_with_options(self, request, runtime):
        """
        You can call this operation up to 10 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        

        @param request: ChatappPhoneNumberRegisterRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ChatappPhoneNumberRegisterResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.cust_space_id):
            body['CustSpaceId'] = request.cust_space_id
        if not UtilClient.is_unset(request.phone_number):
            body['PhoneNumber'] = request.phone_number
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ChatappPhoneNumberRegister',
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
            cams_20200606_models.ChatappPhoneNumberRegisterResponse(),
            self.call_api(params, req, runtime)
        )

    def chatapp_phone_number_register(self, request):
        """
        You can call this operation up to 10 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        

        @param request: ChatappPhoneNumberRegisterRequest

        @return: ChatappPhoneNumberRegisterResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.chatapp_phone_number_register_with_options(request, runtime)

    def chatapp_sync_phone_number_with_options(self, request, runtime):
        """
        You can call this operation up to 10 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        

        @param request: ChatappSyncPhoneNumberRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ChatappSyncPhoneNumberResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ChatappSyncPhoneNumber',
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
            cams_20200606_models.ChatappSyncPhoneNumberResponse(),
            self.call_api(params, req, runtime)
        )

    def chatapp_sync_phone_number(self, request):
        """
        You can call this operation up to 10 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        

        @param request: ChatappSyncPhoneNumberRequest

        @return: ChatappSyncPhoneNumberResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.chatapp_sync_phone_number_with_options(request, runtime)

    def chatapp_verify_and_register_with_options(self, request, runtime):
        """
        You can call this operation up to 10 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        

        @param request: ChatappVerifyAndRegisterRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ChatappVerifyAndRegisterResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.cust_space_id):
            body['CustSpaceId'] = request.cust_space_id
        if not UtilClient.is_unset(request.phone_number):
            body['PhoneNumber'] = request.phone_number
        if not UtilClient.is_unset(request.verify_code):
            body['VerifyCode'] = request.verify_code
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ChatappVerifyAndRegister',
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
            cams_20200606_models.ChatappVerifyAndRegisterResponse(),
            self.call_api(params, req, runtime)
        )

    def chatapp_verify_and_register(self, request):
        """
        You can call this operation up to 10 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        

        @param request: ChatappVerifyAndRegisterRequest

        @return: ChatappVerifyAndRegisterResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.chatapp_verify_and_register_with_options(request, runtime)

    def create_chatapp_migration_initiate_with_options(self, request, runtime):
        """
        The status of the phone number.
        

        @param request: CreateChatappMigrationInitiateRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateChatappMigrationInitiateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.country_code):
            query['CountryCode'] = request.country_code
        if not UtilClient.is_unset(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not UtilClient.is_unset(request.mobile_number):
            query['MobileNumber'] = request.mobile_number
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateChatappMigrationInitiate',
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
            cams_20200606_models.CreateChatappMigrationInitiateResponse(),
            self.call_api(params, req, runtime)
        )

    def create_chatapp_migration_initiate(self, request):
        """
        The status of the phone number.
        

        @param request: CreateChatappMigrationInitiateRequest

        @return: CreateChatappMigrationInitiateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_chatapp_migration_initiate_with_options(request, runtime)

    def create_chatapp_template_with_options(self, tmp_req, runtime):
        """
        The error message.
        

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
        body = {}
        if not UtilClient.is_unset(request.allow_category_change):
            body['AllowCategoryChange'] = request.allow_category_change
        if not UtilClient.is_unset(request.category):
            body['Category'] = request.category
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
        if not UtilClient.is_unset(request.message_send_ttl_seconds):
            body['MessageSendTtlSeconds'] = request.message_send_ttl_seconds
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
        """
        The error message.
        

        @param request: CreateChatappTemplateRequest

        @return: CreateChatappTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_chatapp_template_with_options(request, runtime)

    def delete_chatapp_template_with_options(self, request, runtime):
        """
        ### QPS limit
        You can call this operation up to five times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        

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
        You can call this operation up to five times per second per account. If the number of the calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        

        @param request: DeleteChatappTemplateRequest

        @return: DeleteChatappTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_chatapp_template_with_options(request, runtime)

    def enable_whatsapp_roimetric_with_options(self, request, runtime):
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
            action='EnableWhatsappROIMetric',
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
            cams_20200606_models.EnableWhatsappROIMetricResponse(),
            self.call_api(params, req, runtime)
        )

    def enable_whatsapp_roimetric(self, request):
        runtime = util_models.RuntimeOptions()
        return self.enable_whatsapp_roimetric_with_options(request, runtime)

    def get_chatapp_phone_number_metric_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not UtilClient.is_unset(request.end):
            query['End'] = request.end
        if not UtilClient.is_unset(request.granularity):
            query['Granularity'] = request.granularity
        if not UtilClient.is_unset(request.isv_code):
            query['IsvCode'] = request.isv_code
        if not UtilClient.is_unset(request.phone_number):
            query['PhoneNumber'] = request.phone_number
        if not UtilClient.is_unset(request.start):
            query['Start'] = request.start
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetChatappPhoneNumberMetric',
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
            cams_20200606_models.GetChatappPhoneNumberMetricResponse(),
            self.call_api(params, req, runtime)
        )

    def get_chatapp_phone_number_metric(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_chatapp_phone_number_metric_with_options(request, runtime)

    def get_chatapp_template_detail_with_options(self, request, runtime):
        """
        ### QPS limit
        You can call this API operation up to five times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        

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
        if not UtilClient.is_unset(request.template_type):
            query['TemplateType'] = request.template_type
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
        You can call this API operation up to five times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        

        @param request: GetChatappTemplateDetailRequest

        @return: GetChatappTemplateDetailResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_chatapp_template_detail_with_options(request, runtime)

    def get_chatapp_template_metric_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not UtilClient.is_unset(request.end):
            query['End'] = request.end
        if not UtilClient.is_unset(request.granularity):
            query['Granularity'] = request.granularity
        if not UtilClient.is_unset(request.isv_code):
            query['IsvCode'] = request.isv_code
        if not UtilClient.is_unset(request.language):
            query['Language'] = request.language
        if not UtilClient.is_unset(request.start):
            query['Start'] = request.start
        if not UtilClient.is_unset(request.template_code):
            query['TemplateCode'] = request.template_code
        if not UtilClient.is_unset(request.template_type):
            query['TemplateType'] = request.template_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetChatappTemplateMetric',
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
            cams_20200606_models.GetChatappTemplateMetricResponse(),
            self.call_api(params, req, runtime)
        )

    def get_chatapp_template_metric(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_chatapp_template_metric_with_options(request, runtime)

    def get_chatapp_upload_authorization_with_options(self, request, runtime):
        """
        You can call this operation up to five times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        

        @param request: GetChatappUploadAuthorizationRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: GetChatappUploadAuthorizationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetChatappUploadAuthorization',
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
            cams_20200606_models.GetChatappUploadAuthorizationResponse(),
            self.call_api(params, req, runtime)
        )

    def get_chatapp_upload_authorization(self, request):
        """
        You can call this operation up to five times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        

        @param request: GetChatappUploadAuthorizationRequest

        @return: GetChatappUploadAuthorizationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_chatapp_upload_authorization_with_options(request, runtime)

    def get_chatapp_verify_code_with_options(self, request, runtime):
        """
        You can call this operation up to 10 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        

        @param request: GetChatappVerifyCodeRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: GetChatappVerifyCodeResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.cust_space_id):
            body['CustSpaceId'] = request.cust_space_id
        if not UtilClient.is_unset(request.locale):
            body['Locale'] = request.locale
        if not UtilClient.is_unset(request.method):
            body['Method'] = request.method
        if not UtilClient.is_unset(request.phone_number):
            body['PhoneNumber'] = request.phone_number
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetChatappVerifyCode',
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
            cams_20200606_models.GetChatappVerifyCodeResponse(),
            self.call_api(params, req, runtime)
        )

    def get_chatapp_verify_code(self, request):
        """
        You can call this operation up to 10 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        

        @param request: GetChatappVerifyCodeRequest

        @return: GetChatappVerifyCodeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_chatapp_verify_code_with_options(request, runtime)

    def get_commerce_setting_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not UtilClient.is_unset(request.phone_number):
            query['PhoneNumber'] = request.phone_number
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetCommerceSetting',
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
            cams_20200606_models.GetCommerceSettingResponse(),
            self.call_api(params, req, runtime)
        )

    def get_commerce_setting(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_commerce_setting_with_options(request, runtime)

    def get_migration_verify_code_with_options(self, request, runtime):
        """
        The ID of the phone number.
        

        @param request: GetMigrationVerifyCodeRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: GetMigrationVerifyCodeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not UtilClient.is_unset(request.locale):
            query['Locale'] = request.locale
        if not UtilClient.is_unset(request.method):
            query['Method'] = request.method
        if not UtilClient.is_unset(request.phone_number):
            query['PhoneNumber'] = request.phone_number
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetMigrationVerifyCode',
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
            cams_20200606_models.GetMigrationVerifyCodeResponse(),
            self.call_api(params, req, runtime)
        )

    def get_migration_verify_code(self, request):
        """
        The ID of the phone number.
        

        @param request: GetMigrationVerifyCodeRequest

        @return: GetMigrationVerifyCodeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_migration_verify_code_with_options(request, runtime)

    def get_phone_number_verification_status_with_options(self, request, runtime):
        """
        You can call this operation up to 10 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        

        @param request: GetPhoneNumberVerificationStatusRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: GetPhoneNumberVerificationStatusResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.cust_space_id):
            body['CustSpaceId'] = request.cust_space_id
        if not UtilClient.is_unset(request.phone_number):
            body['PhoneNumber'] = request.phone_number
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetPhoneNumberVerificationStatus',
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
            cams_20200606_models.GetPhoneNumberVerificationStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def get_phone_number_verification_status(self, request):
        """
        You can call this operation up to 10 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        

        @param request: GetPhoneNumberVerificationStatusRequest

        @return: GetPhoneNumberVerificationStatusResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_phone_number_verification_status_with_options(request, runtime)

    def get_pre_validate_phone_id_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.phone_number):
            body['PhoneNumber'] = request.phone_number
        if not UtilClient.is_unset(request.verify_code):
            body['VerifyCode'] = request.verify_code
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetPreValidatePhoneId',
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
            cams_20200606_models.GetPreValidatePhoneIdResponse(),
            self.call_api(params, req, runtime)
        )

    def get_pre_validate_phone_id(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_pre_validate_phone_id_with_options(request, runtime)

    def get_whatsapp_connection_catalog_with_options(self, request, runtime):
        """
        You can call this operation up to 10 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        

        @param request: GetWhatsappConnectionCatalogRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: GetWhatsappConnectionCatalogResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.waba_id):
            query['WabaId'] = request.waba_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetWhatsappConnectionCatalog',
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
            cams_20200606_models.GetWhatsappConnectionCatalogResponse(),
            self.call_api(params, req, runtime)
        )

    def get_whatsapp_connection_catalog(self, request):
        """
        You can call this operation up to 10 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        

        @param request: GetWhatsappConnectionCatalogRequest

        @return: GetWhatsappConnectionCatalogResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_whatsapp_connection_catalog_with_options(request, runtime)

    def isv_get_app_id_with_options(self, request, runtime):
        """
        You can call this operation up to 10 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        

        @param request: IsvGetAppIdRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: IsvGetAppIdResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='IsvGetAppId',
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
            cams_20200606_models.IsvGetAppIdResponse(),
            self.call_api(params, req, runtime)
        )

    def isv_get_app_id(self, request):
        """
        You can call this operation up to 10 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        

        @param request: IsvGetAppIdRequest

        @return: IsvGetAppIdResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.isv_get_app_id_with_options(request, runtime)

    def list_chatapp_template_with_options(self, tmp_req, runtime):
        """
        ### QPS limit
        You can call this operation up to five times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        

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
        if not UtilClient.is_unset(request.template_type):
            query['TemplateType'] = request.template_type
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
        You can call this operation up to five times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        

        @param request: ListChatappTemplateRequest

        @return: ListChatappTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_chatapp_template_with_options(request, runtime)

    def list_product_with_options(self, request, runtime):
        """
        You can call this operation up to 10 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        

        @param request: ListProductRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListProductResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.after):
            query['After'] = request.after
        if not UtilClient.is_unset(request.before):
            query['Before'] = request.before
        if not UtilClient.is_unset(request.catalog_id):
            query['CatalogId'] = request.catalog_id
        if not UtilClient.is_unset(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not UtilClient.is_unset(request.fields):
            query['Fields'] = request.fields
        if not UtilClient.is_unset(request.limit):
            query['Limit'] = request.limit
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.waba_id):
            query['WabaId'] = request.waba_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListProduct',
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
            cams_20200606_models.ListProductResponse(),
            self.call_api(params, req, runtime)
        )

    def list_product(self, request):
        """
        You can call this operation up to 10 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        

        @param request: ListProductRequest

        @return: ListProductResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_product_with_options(request, runtime)

    def list_product_catalog_with_options(self, request, runtime):
        """
        You can call this operation up to 10 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        

        @param request: ListProductCatalogRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListProductCatalogResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.after):
            query['After'] = request.after
        if not UtilClient.is_unset(request.before):
            query['Before'] = request.before
        if not UtilClient.is_unset(request.business_id):
            query['BusinessId'] = request.business_id
        if not UtilClient.is_unset(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not UtilClient.is_unset(request.fields):
            query['Fields'] = request.fields
        if not UtilClient.is_unset(request.limit):
            query['Limit'] = request.limit
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListProductCatalog',
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
            cams_20200606_models.ListProductCatalogResponse(),
            self.call_api(params, req, runtime)
        )

    def list_product_catalog(self, request):
        """
        You can call this operation up to 10 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        

        @param request: ListProductCatalogRequest

        @return: ListProductCatalogResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_product_catalog_with_options(request, runtime)

    def modify_chatapp_template_with_options(self, tmp_req, runtime):
        """
        The name of the message template.
        

        @param tmp_req: ModifyChatappTemplateRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ModifyChatappTemplateResponse
        """
        UtilClient.validate_model(tmp_req)
        request = cams_20200606_models.ModifyChatappTemplateShrinkRequest()
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
        if not UtilClient.is_unset(request.message_send_ttl_seconds):
            body['MessageSendTtlSeconds'] = request.message_send_ttl_seconds
        if not UtilClient.is_unset(request.template_code):
            body['TemplateCode'] = request.template_code
        if not UtilClient.is_unset(request.template_type):
            body['TemplateType'] = request.template_type
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
        """
        The name of the message template.
        

        @param request: ModifyChatappTemplateRequest

        @return: ModifyChatappTemplateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_chatapp_template_with_options(request, runtime)

    def modify_phone_business_profile_with_options(self, tmp_req, runtime):
        """
        ModifyPhoneBusinessProfile
        

        @param tmp_req: ModifyPhoneBusinessProfileRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ModifyPhoneBusinessProfileResponse
        """
        UtilClient.validate_model(tmp_req)
        request = cams_20200606_models.ModifyPhoneBusinessProfileShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.websites):
            request.websites_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.websites, 'Websites', 'json')
        query = {}
        if not UtilClient.is_unset(request.address):
            query['Address'] = request.address
        if not UtilClient.is_unset(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.email):
            query['Email'] = request.email
        if not UtilClient.is_unset(request.phone_number):
            query['PhoneNumber'] = request.phone_number
        if not UtilClient.is_unset(request.profile_picture_url):
            query['ProfilePictureUrl'] = request.profile_picture_url
        if not UtilClient.is_unset(request.vertical):
            query['Vertical'] = request.vertical
        if not UtilClient.is_unset(request.websites_shrink):
            query['Websites'] = request.websites_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyPhoneBusinessProfile',
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
            cams_20200606_models.ModifyPhoneBusinessProfileResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_phone_business_profile(self, request):
        """
        ModifyPhoneBusinessProfile
        

        @param request: ModifyPhoneBusinessProfileRequest

        @return: ModifyPhoneBusinessProfileResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_phone_business_profile_with_options(request, runtime)

    def query_chatapp_bind_waba_with_options(self, request, runtime):
        """
        You can call this operation up to 10 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        

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
        You can call this operation up to 10 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        

        @param request: QueryChatappBindWabaRequest

        @return: QueryChatappBindWabaResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_chatapp_bind_waba_with_options(request, runtime)

    def query_chatapp_phone_numbers_with_options(self, request, runtime):
        """
        You can call this operation up to 10 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        

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
        You can call this operation up to 10 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        

        @param request: QueryChatappPhoneNumbersRequest

        @return: QueryChatappPhoneNumbersResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_chatapp_phone_numbers_with_options(request, runtime)

    def query_phone_business_profile_with_options(self, request, runtime):
        """
        You can call this operation up to 10 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        

        @param request: QueryPhoneBusinessProfileRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: QueryPhoneBusinessProfileResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not UtilClient.is_unset(request.phone_number):
            query['PhoneNumber'] = request.phone_number
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryPhoneBusinessProfile',
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
            cams_20200606_models.QueryPhoneBusinessProfileResponse(),
            self.call_api(params, req, runtime)
        )

    def query_phone_business_profile(self, request):
        """
        You can call this operation up to 10 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        

        @param request: QueryPhoneBusinessProfileRequest

        @return: QueryPhoneBusinessProfileResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_phone_business_profile_with_options(request, runtime)

    def query_waba_business_info_with_options(self, request, runtime):
        """
        You can call this operation up to 10 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        

        @param request: QueryWabaBusinessInfoRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: QueryWabaBusinessInfoResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not UtilClient.is_unset(request.waba_id):
            query['WabaId'] = request.waba_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryWabaBusinessInfo',
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
            cams_20200606_models.QueryWabaBusinessInfoResponse(),
            self.call_api(params, req, runtime)
        )

    def query_waba_business_info(self, request):
        """
        You can call this operation up to 10 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        

        @param request: QueryWabaBusinessInfoRequest

        @return: QueryWabaBusinessInfoResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.query_waba_business_info_with_options(request, runtime)

    def send_chatapp_mass_message_with_options(self, tmp_req, runtime):
        """
        You can call this operation up to 10 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        You can send messages to up to 1,000 phone numbers in a single request.
        

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
        if not UtilClient.is_unset(request.fall_back_duration):
            body['FallBackDuration'] = request.fall_back_duration
        if not UtilClient.is_unset(request.fall_back_id):
            body['FallBackId'] = request.fall_back_id
        if not UtilClient.is_unset(request.fall_back_rule):
            body['FallBackRule'] = request.fall_back_rule
        if not UtilClient.is_unset(request.from_):
            body['From'] = request.from_
        if not UtilClient.is_unset(request.isv_code):
            body['IsvCode'] = request.isv_code
        if not UtilClient.is_unset(request.label):
            body['Label'] = request.label
        if not UtilClient.is_unset(request.language):
            body['Language'] = request.language
        if not UtilClient.is_unset(request.sender_list_shrink):
            body['SenderList'] = request.sender_list_shrink
        if not UtilClient.is_unset(request.tag):
            body['Tag'] = request.tag
        if not UtilClient.is_unset(request.task_id):
            body['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.template_code):
            body['TemplateCode'] = request.template_code
        if not UtilClient.is_unset(request.ttl):
            body['Ttl'] = request.ttl
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
        You can call this operation up to 10 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        You can send messages to up to 1,000 phone numbers in a single request.
        

        @param request: SendChatappMassMessageRequest

        @return: SendChatappMassMessageResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.send_chatapp_mass_message_with_options(request, runtime)

    def send_chatapp_message_with_options(self, tmp_req, runtime):
        """
        You can call this operation up to 200 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        

        @param tmp_req: SendChatappMessageRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: SendChatappMessageResponse
        """
        UtilClient.validate_model(tmp_req)
        request = cams_20200606_models.SendChatappMessageShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.payload):
            request.payload_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.payload, 'Payload', 'json')
        if not UtilClient.is_unset(tmp_req.product_action):
            request.product_action_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.product_action, 'ProductAction', 'json')
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
        if not UtilClient.is_unset(request.fall_back_duration):
            body['FallBackDuration'] = request.fall_back_duration
        if not UtilClient.is_unset(request.fall_back_id):
            body['FallBackId'] = request.fall_back_id
        if not UtilClient.is_unset(request.fall_back_rule):
            body['FallBackRule'] = request.fall_back_rule
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
        if not UtilClient.is_unset(request.product_action_shrink):
            body['ProductAction'] = request.product_action_shrink
        if not UtilClient.is_unset(request.tag):
            body['Tag'] = request.tag
        if not UtilClient.is_unset(request.task_id):
            body['TaskId'] = request.task_id
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
        You can call this operation up to 200 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        

        @param request: SendChatappMessageRequest

        @return: SendChatappMessageResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.send_chatapp_message_with_options(request, runtime)

    def submit_isv_customer_terms_with_options(self, request, runtime):
        """
        You can call this operation up to five times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        

        @param request: SubmitIsvCustomerTermsRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: SubmitIsvCustomerTermsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.business_desc):
            query['BusinessDesc'] = request.business_desc
        if not UtilClient.is_unset(request.contact_mail):
            query['ContactMail'] = request.contact_mail
        if not UtilClient.is_unset(request.country_id):
            query['CountryId'] = request.country_id
        if not UtilClient.is_unset(request.cust_name):
            query['CustName'] = request.cust_name
        if not UtilClient.is_unset(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not UtilClient.is_unset(request.isv_terms):
            query['IsvTerms'] = request.isv_terms
        if not UtilClient.is_unset(request.office_address):
            query['OfficeAddress'] = request.office_address
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubmitIsvCustomerTerms',
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
            cams_20200606_models.SubmitIsvCustomerTermsResponse(),
            self.call_api(params, req, runtime)
        )

    def submit_isv_customer_terms(self, request):
        """
        You can call this operation up to five times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        

        @param request: SubmitIsvCustomerTermsRequest

        @return: SubmitIsvCustomerTermsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.submit_isv_customer_terms_with_options(request, runtime)

    def update_account_webhook_with_options(self, request, runtime):
        """
        You can call this operation up to 10 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        

        @param request: UpdateAccountWebhookRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: UpdateAccountWebhookResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not UtilClient.is_unset(request.http_flag):
            query['HttpFlag'] = request.http_flag
        if not UtilClient.is_unset(request.queue_flag):
            query['QueueFlag'] = request.queue_flag
        if not UtilClient.is_unset(request.status_callback_url):
            query['StatusCallbackUrl'] = request.status_callback_url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateAccountWebhook',
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
            cams_20200606_models.UpdateAccountWebhookResponse(),
            self.call_api(params, req, runtime)
        )

    def update_account_webhook(self, request):
        """
        You can call this operation up to 10 times per second per account. If the number of calls per second exceeds the limit, throttling is triggered. As a result, your business may be affected. We recommend that you take note of the limit when you call this operation.
        

        @param request: UpdateAccountWebhookRequest

        @return: UpdateAccountWebhookResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_account_webhook_with_options(request, runtime)

    def update_commerce_setting_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cart_enable):
            query['CartEnable'] = request.cart_enable
        if not UtilClient.is_unset(request.catalog_visible):
            query['CatalogVisible'] = request.catalog_visible
        if not UtilClient.is_unset(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not UtilClient.is_unset(request.phone_number):
            query['PhoneNumber'] = request.phone_number
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateCommerceSetting',
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
            cams_20200606_models.UpdateCommerceSettingResponse(),
            self.call_api(params, req, runtime)
        )

    def update_commerce_setting(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_commerce_setting_with_options(request, runtime)

    def update_phone_webhook_with_options(self, request, runtime):
        """
        The error message returned.
        

        @param request: UpdatePhoneWebhookRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: UpdatePhoneWebhookResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cust_space_id):
            query['CustSpaceId'] = request.cust_space_id
        if not UtilClient.is_unset(request.http_flag):
            query['HttpFlag'] = request.http_flag
        if not UtilClient.is_unset(request.phone_number):
            query['PhoneNumber'] = request.phone_number
        if not UtilClient.is_unset(request.queue_flag):
            query['QueueFlag'] = request.queue_flag
        if not UtilClient.is_unset(request.status_callback_url):
            query['StatusCallbackUrl'] = request.status_callback_url
        if not UtilClient.is_unset(request.up_callback_url):
            query['UpCallbackUrl'] = request.up_callback_url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdatePhoneWebhook',
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
            cams_20200606_models.UpdatePhoneWebhookResponse(),
            self.call_api(params, req, runtime)
        )

    def update_phone_webhook(self, request):
        """
        The error message returned.
        

        @param request: UpdatePhoneWebhookRequest

        @return: UpdatePhoneWebhookResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_phone_webhook_with_options(request, runtime)
