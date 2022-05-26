# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_chatbot20171011 import models as chatbot_20171011_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_openapi_util.client import Client as OpenApiUtilClient


class Client(OpenApiClient):
    """
    *\
    """
    def __init__(self, config):
        super(Client, self).__init__(config)
        self._endpoint_rule = ''
        self.check_config(config)
        self._endpoint = self.get_endpoint('chatbot', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def activate_perspective_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.perspective_id):
            query['PerspectiveId'] = request.perspective_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ActivatePerspective',
            version='2017-10-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20171011_models.ActivatePerspectiveResponse(),
            self.call_api(params, req, runtime)
        )

    def activate_perspective(self, request):
        runtime = util_models.RuntimeOptions()
        return self.activate_perspective_with_options(request, runtime)

    def add_synonym_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.core_word_name):
            query['CoreWordName'] = request.core_word_name
        if not UtilClient.is_unset(request.synonym):
            query['Synonym'] = request.synonym
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddSynonym',
            version='2017-10-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20171011_models.AddSynonymResponse(),
            self.call_api(params, req, runtime)
        )

    def add_synonym(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_synonym_with_options(request, runtime)

    def append_entity_member_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = chatbot_20171011_models.AppendEntityMemberShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.member):
            request.member_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.member), 'Member', 'json')
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.apply_type):
            query['ApplyType'] = request.apply_type
        if not UtilClient.is_unset(request.entity_id):
            query['EntityId'] = request.entity_id
        if not UtilClient.is_unset(request.member_shrink):
            query['Member'] = request.member_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AppendEntityMember',
            version='2017-10-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20171011_models.AppendEntityMemberResponse(),
            self.call_api(params, req, runtime)
        )

    def append_entity_member(self, request):
        runtime = util_models.RuntimeOptions()
        return self.append_entity_member_with_options(request, runtime)

    def associate_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.perspective):
            query['Perspective'] = request.perspective
        if not UtilClient.is_unset(request.recommend_num):
            query['RecommendNum'] = request.recommend_num
        if not UtilClient.is_unset(request.session_id):
            query['SessionId'] = request.session_id
        if not UtilClient.is_unset(request.utterance):
            query['Utterance'] = request.utterance
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='Associate',
            version='2017-10-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20171011_models.AssociateResponse(),
            self.call_api(params, req, runtime)
        )

    def associate(self, request):
        runtime = util_models.RuntimeOptions()
        return self.associate_with_options(request, runtime)

    def chat_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.intent_name):
            query['IntentName'] = request.intent_name
        if not UtilClient.is_unset(request.knowledge_id):
            query['KnowledgeId'] = request.knowledge_id
        if not UtilClient.is_unset(request.perspective):
            query['Perspective'] = request.perspective
        if not UtilClient.is_unset(request.sender_id):
            query['SenderId'] = request.sender_id
        if not UtilClient.is_unset(request.sender_nick):
            query['SenderNick'] = request.sender_nick
        if not UtilClient.is_unset(request.session_id):
            query['SessionId'] = request.session_id
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.utterance):
            query['Utterance'] = request.utterance
        if not UtilClient.is_unset(request.vendor_param):
            query['VendorParam'] = request.vendor_param
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='Chat',
            version='2017-10-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20171011_models.ChatResponse(),
            self.call_api(params, req, runtime)
        )

    def chat(self, request):
        runtime = util_models.RuntimeOptions()
        return self.chat_with_options(request, runtime)

    def create_bot_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.avatar):
            query['Avatar'] = request.avatar
        if not UtilClient.is_unset(request.introduction):
            query['Introduction'] = request.introduction
        if not UtilClient.is_unset(request.language_code):
            query['LanguageCode'] = request.language_code
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.robot_type):
            query['RobotType'] = request.robot_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateBot',
            version='2017-10-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20171011_models.CreateBotResponse(),
            self.call_api(params, req, runtime)
        )

    def create_bot(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_bot_with_options(request, runtime)

    def create_category_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.biz_code):
            query['BizCode'] = request.biz_code
        if not UtilClient.is_unset(request.knowledge_type):
            query['KnowledgeType'] = request.knowledge_type
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.parent_category_id):
            query['ParentCategoryId'] = request.parent_category_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateCategory',
            version='2017-10-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20171011_models.CreateCategoryResponse(),
            self.call_api(params, req, runtime)
        )

    def create_category(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_category_with_options(request, runtime)

    def create_core_word_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.core_word_name):
            query['CoreWordName'] = request.core_word_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateCoreWord',
            version='2017-10-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20171011_models.CreateCoreWordResponse(),
            self.call_api(params, req, runtime)
        )

    def create_core_word(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_core_word_with_options(request, runtime)

    def create_dialog_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.dialog_name):
            query['DialogName'] = request.dialog_name
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDialog',
            version='2017-10-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20171011_models.CreateDialogResponse(),
            self.call_api(params, req, runtime)
        )

    def create_dialog(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_dialog_with_options(request, runtime)

    def create_entity_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = chatbot_20171011_models.CreateEntityShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.members):
            request.members_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.members, 'Members', 'json')
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.dialog_id):
            query['DialogId'] = request.dialog_id
        if not UtilClient.is_unset(request.entity_name):
            query['EntityName'] = request.entity_name
        if not UtilClient.is_unset(request.entity_type):
            query['EntityType'] = request.entity_type
        if not UtilClient.is_unset(request.members_shrink):
            query['Members'] = request.members_shrink
        if not UtilClient.is_unset(request.regex):
            query['Regex'] = request.regex
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateEntity',
            version='2017-10-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20171011_models.CreateEntityResponse(),
            self.call_api(params, req, runtime)
        )

    def create_entity(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_entity_with_options(request, runtime)

    def create_intent_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = chatbot_20171011_models.CreateIntentShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.intent_definition):
            request.intent_definition_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.intent_definition), 'IntentDefinition', 'json')
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.dialog_id):
            query['DialogId'] = request.dialog_id
        if not UtilClient.is_unset(request.intent_definition_shrink):
            query['IntentDefinition'] = request.intent_definition_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateIntent',
            version='2017-10-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20171011_models.CreateIntentResponse(),
            self.call_api(params, req, runtime)
        )

    def create_intent(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_intent_with_options(request, runtime)

    def create_knowledge_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = chatbot_20171011_models.CreateKnowledgeShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.knowledge):
            request.knowledge_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.knowledge), 'Knowledge', 'json')
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.knowledge_shrink):
            body['Knowledge'] = request.knowledge_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateKnowledge',
            version='2017-10-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20171011_models.CreateKnowledgeResponse(),
            self.call_api(params, req, runtime)
        )

    def create_knowledge(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_knowledge_with_options(request, runtime)

    def create_perspective_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreatePerspective',
            version='2017-10-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20171011_models.CreatePerspectiveResponse(),
            self.call_api(params, req, runtime)
        )

    def create_perspective(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_perspective_with_options(request, runtime)

    def delete_bot_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteBot',
            version='2017-10-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20171011_models.DeleteBotResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_bot(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_bot_with_options(request, runtime)

    def delete_category_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.category_id):
            query['CategoryId'] = request.category_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteCategory',
            version='2017-10-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20171011_models.DeleteCategoryResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_category(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_category_with_options(request, runtime)

    def delete_core_word_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.core_word_name):
            query['CoreWordName'] = request.core_word_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteCoreWord',
            version='2017-10-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20171011_models.DeleteCoreWordResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_core_word(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_core_word_with_options(request, runtime)

    def delete_dialog_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.dialog_id):
            query['DialogId'] = request.dialog_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDialog',
            version='2017-10-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20171011_models.DeleteDialogResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_dialog(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_dialog_with_options(request, runtime)

    def delete_entity_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.entity_id):
            query['EntityId'] = request.entity_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteEntity',
            version='2017-10-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20171011_models.DeleteEntityResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_entity(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_entity_with_options(request, runtime)

    def delete_intent_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.intent_id):
            query['IntentId'] = request.intent_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteIntent',
            version='2017-10-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20171011_models.DeleteIntentResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_intent(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_intent_with_options(request, runtime)

    def delete_knowledge_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.knowledge_id):
            query['KnowledgeId'] = request.knowledge_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteKnowledge',
            version='2017-10-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20171011_models.DeleteKnowledgeResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_knowledge(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_knowledge_with_options(request, runtime)

    def delete_perspective_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.perspective_id):
            query['PerspectiveId'] = request.perspective_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeletePerspective',
            version='2017-10-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20171011_models.DeletePerspectiveResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_perspective(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_perspective_with_options(request, runtime)

    def describe_bot_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeBot',
            version='2017-10-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20171011_models.DescribeBotResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_bot(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_bot_with_options(request, runtime)

    def describe_category_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.category_id):
            query['CategoryId'] = request.category_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCategory',
            version='2017-10-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20171011_models.DescribeCategoryResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_category(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_category_with_options(request, runtime)

    def describe_core_word_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.core_word_name):
            query['CoreWordName'] = request.core_word_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCoreWord',
            version='2017-10-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20171011_models.DescribeCoreWordResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_core_word(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_core_word_with_options(request, runtime)

    def describe_dialog_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.dialog_id):
            query['DialogId'] = request.dialog_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDialog',
            version='2017-10-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20171011_models.DescribeDialogResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_dialog(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dialog_with_options(request, runtime)

    def describe_dialog_flow_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.dialog_id):
            query['DialogId'] = request.dialog_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDialogFlow',
            version='2017-10-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20171011_models.DescribeDialogFlowResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_dialog_flow(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dialog_flow_with_options(request, runtime)

    def describe_entities_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.entity_id):
            query['EntityId'] = request.entity_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeEntities',
            version='2017-10-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20171011_models.DescribeEntitiesResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_entities(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_entities_with_options(request, runtime)

    def describe_intent_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.intent_id):
            query['IntentId'] = request.intent_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeIntent',
            version='2017-10-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20171011_models.DescribeIntentResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_intent(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_intent_with_options(request, runtime)

    def describe_knowledge_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.knowledge_id):
            query['KnowledgeId'] = request.knowledge_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeKnowledge',
            version='2017-10-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20171011_models.DescribeKnowledgeResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_knowledge(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_knowledge_with_options(request, runtime)

    def describe_perspective_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.perspective_id):
            query['PerspectiveId'] = request.perspective_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePerspective',
            version='2017-10-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20171011_models.DescribePerspectiveResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_perspective(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_perspective_with_options(request, runtime)

    def disable_dialog_flow_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.dialog_id):
            query['DialogId'] = request.dialog_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DisableDialogFlow',
            version='2017-10-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20171011_models.DisableDialogFlowResponse(),
            self.call_api(params, req, runtime)
        )

    def disable_dialog_flow(self, request):
        runtime = util_models.RuntimeOptions()
        return self.disable_dialog_flow_with_options(request, runtime)

    def disable_knowledge_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.knowledge_id):
            query['KnowledgeId'] = request.knowledge_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DisableKnowledge',
            version='2017-10-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20171011_models.DisableKnowledgeResponse(),
            self.call_api(params, req, runtime)
        )

    def disable_knowledge(self, request):
        runtime = util_models.RuntimeOptions()
        return self.disable_knowledge_with_options(request, runtime)

    def feedback_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.feedback):
            query['Feedback'] = request.feedback
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.message_id):
            query['MessageId'] = request.message_id
        if not UtilClient.is_unset(request.session_id):
            query['SessionId'] = request.session_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='Feedback',
            version='2017-10-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20171011_models.FeedbackResponse(),
            self.call_api(params, req, runtime)
        )

    def feedback(self, request):
        runtime = util_models.RuntimeOptions()
        return self.feedback_with_options(request, runtime)

    def get_async_result_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAsyncResult',
            version='2017-10-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20171011_models.GetAsyncResultResponse(),
            self.call_api(params, req, runtime)
        )

    def get_async_result(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_async_result_with_options(request, runtime)

    def get_bot_chat_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.robot_instance_id):
            query['RobotInstanceId'] = request.robot_instance_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetBotChatData',
            version='2017-10-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20171011_models.GetBotChatDataResponse(),
            self.call_api(params, req, runtime)
        )

    def get_bot_chat_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_bot_chat_data_with_options(request, runtime)

    def get_bot_ds_stat_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.robot_instance_id):
            query['RobotInstanceId'] = request.robot_instance_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetBotDsStatData',
            version='2017-10-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20171011_models.GetBotDsStatDataResponse(),
            self.call_api(params, req, runtime)
        )

    def get_bot_ds_stat_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_bot_ds_stat_data_with_options(request, runtime)

    def get_bot_knowledge_stat_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.robot_instance_id):
            query['RobotInstanceId'] = request.robot_instance_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetBotKnowledgeStatData',
            version='2017-10-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20171011_models.GetBotKnowledgeStatDataResponse(),
            self.call_api(params, req, runtime)
        )

    def get_bot_knowledge_stat_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_bot_knowledge_stat_data_with_options(request, runtime)

    def get_bot_session_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.robot_instance_id):
            query['RobotInstanceId'] = request.robot_instance_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetBotSessionData',
            version='2017-10-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20171011_models.GetBotSessionDataResponse(),
            self.call_api(params, req, runtime)
        )

    def get_bot_session_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_bot_session_data_with_options(request, runtime)

    def get_conversation_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.end_date):
            query['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.sender_id):
            query['SenderId'] = request.sender_id
        if not UtilClient.is_unset(request.session_id):
            query['SessionId'] = request.session_id
        if not UtilClient.is_unset(request.start_date):
            query['StartDate'] = request.start_date
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetConversationList',
            version='2017-10-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20171011_models.GetConversationListResponse(),
            self.call_api(params, req, runtime)
        )

    def get_conversation_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_conversation_list_with_options(request, runtime)

    def list_bot_chat_historys_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.limit):
            query['Limit'] = request.limit
        if not UtilClient.is_unset(request.robot_instance_id):
            query['RobotInstanceId'] = request.robot_instance_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListBotChatHistorys',
            version='2017-10-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20171011_models.ListBotChatHistorysResponse(),
            self.call_api(params, req, runtime)
        )

    def list_bot_chat_historys(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_bot_chat_historys_with_options(request, runtime)

    def list_bot_cold_ds_datas_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.limit):
            query['Limit'] = request.limit
        if not UtilClient.is_unset(request.robot_instance_id):
            query['RobotInstanceId'] = request.robot_instance_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListBotColdDsDatas',
            version='2017-10-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20171011_models.ListBotColdDsDatasResponse(),
            self.call_api(params, req, runtime)
        )

    def list_bot_cold_ds_datas(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_bot_cold_ds_datas_with_options(request, runtime)

    def list_bot_cold_knowledges_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.limit):
            query['Limit'] = request.limit
        if not UtilClient.is_unset(request.robot_instance_id):
            query['RobotInstanceId'] = request.robot_instance_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListBotColdKnowledges',
            version='2017-10-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20171011_models.ListBotColdKnowledgesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_bot_cold_knowledges(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_bot_cold_knowledges_with_options(request, runtime)

    def list_bot_ds_details_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.limit):
            query['Limit'] = request.limit
        if not UtilClient.is_unset(request.robot_instance_id):
            query['RobotInstanceId'] = request.robot_instance_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListBotDsDetails',
            version='2017-10-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20171011_models.ListBotDsDetailsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_bot_ds_details(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_bot_ds_details_with_options(request, runtime)

    def list_bot_hot_ds_datas_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.limit):
            query['Limit'] = request.limit
        if not UtilClient.is_unset(request.robot_instance_id):
            query['RobotInstanceId'] = request.robot_instance_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListBotHotDsDatas',
            version='2017-10-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20171011_models.ListBotHotDsDatasResponse(),
            self.call_api(params, req, runtime)
        )

    def list_bot_hot_ds_datas(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_bot_hot_ds_datas_with_options(request, runtime)

    def list_bot_hot_knowledges_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.limit):
            query['Limit'] = request.limit
        if not UtilClient.is_unset(request.robot_instance_id):
            query['RobotInstanceId'] = request.robot_instance_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListBotHotKnowledges',
            version='2017-10-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20171011_models.ListBotHotKnowledgesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_bot_hot_knowledges(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_bot_hot_knowledges_with_options(request, runtime)

    def list_bot_knowledge_details_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.limit):
            query['Limit'] = request.limit
        if not UtilClient.is_unset(request.robot_instance_id):
            query['RobotInstanceId'] = request.robot_instance_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListBotKnowledgeDetails',
            version='2017-10-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20171011_models.ListBotKnowledgeDetailsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_bot_knowledge_details(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_bot_knowledge_details_with_options(request, runtime)

    def list_bot_reception_detail_datas_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.robot_instance_id):
            query['RobotInstanceId'] = request.robot_instance_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListBotReceptionDetailDatas',
            version='2017-10-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20171011_models.ListBotReceptionDetailDatasResponse(),
            self.call_api(params, req, runtime)
        )

    def list_bot_reception_detail_datas(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_bot_reception_detail_datas_with_options(request, runtime)

    def list_conversation_logs_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.session_id):
            query['SessionId'] = request.session_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListConversationLogs',
            version='2017-10-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20171011_models.ListConversationLogsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_conversation_logs(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_conversation_logs_with_options(request, runtime)

    def move_knowledge_category_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.category_id):
            query['CategoryId'] = request.category_id
        if not UtilClient.is_unset(request.knowledge_id):
            query['KnowledgeId'] = request.knowledge_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='MoveKnowledgeCategory',
            version='2017-10-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20171011_models.MoveKnowledgeCategoryResponse(),
            self.call_api(params, req, runtime)
        )

    def move_knowledge_category(self, request):
        runtime = util_models.RuntimeOptions()
        return self.move_knowledge_category_with_options(request, runtime)

    def publish_dialog_flow_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.dialog_id):
            query['DialogId'] = request.dialog_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PublishDialogFlow',
            version='2017-10-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20171011_models.PublishDialogFlowResponse(),
            self.call_api(params, req, runtime)
        )

    def publish_dialog_flow(self, request):
        runtime = util_models.RuntimeOptions()
        return self.publish_dialog_flow_with_options(request, runtime)

    def publish_knowledge_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.async):
            query['Async'] = request.async
        if not UtilClient.is_unset(request.knowledge_id):
            query['KnowledgeId'] = request.knowledge_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PublishKnowledge',
            version='2017-10-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20171011_models.PublishKnowledgeResponse(),
            self.call_api(params, req, runtime)
        )

    def publish_knowledge(self, request):
        runtime = util_models.RuntimeOptions()
        return self.publish_knowledge_with_options(request, runtime)

    def query_bots_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryBots',
            version='2017-10-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20171011_models.QueryBotsResponse(),
            self.call_api(params, req, runtime)
        )

    def query_bots(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_bots_with_options(request, runtime)

    def query_categories_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.knowledge_type):
            query['KnowledgeType'] = request.knowledge_type
        if not UtilClient.is_unset(request.parent_category_id):
            query['ParentCategoryId'] = request.parent_category_id
        if not UtilClient.is_unset(request.show_childrens):
            query['ShowChildrens'] = request.show_childrens
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryCategories',
            version='2017-10-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20171011_models.QueryCategoriesResponse(),
            self.call_api(params, req, runtime)
        )

    def query_categories(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_categories_with_options(request, runtime)

    def query_core_words_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.core_word_name):
            query['CoreWordName'] = request.core_word_name
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.synonym):
            query['Synonym'] = request.synonym
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryCoreWords',
            version='2017-10-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20171011_models.QueryCoreWordsResponse(),
            self.call_api(params, req, runtime)
        )

    def query_core_words(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_core_words_with_options(request, runtime)

    def query_dialogs_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.dialog_name):
            query['DialogName'] = request.dialog_name
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryDialogs',
            version='2017-10-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20171011_models.QueryDialogsResponse(),
            self.call_api(params, req, runtime)
        )

    def query_dialogs(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_dialogs_with_options(request, runtime)

    def query_entities_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.dialog_id):
            query['DialogId'] = request.dialog_id
        if not UtilClient.is_unset(request.entity_name):
            query['EntityName'] = request.entity_name
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryEntities',
            version='2017-10-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20171011_models.QueryEntitiesResponse(),
            self.call_api(params, req, runtime)
        )

    def query_entities(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_entities_with_options(request, runtime)

    def query_intents_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.dialog_id):
            query['DialogId'] = request.dialog_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.intent_name):
            query['IntentName'] = request.intent_name
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryIntents',
            version='2017-10-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20171011_models.QueryIntentsResponse(),
            self.call_api(params, req, runtime)
        )

    def query_intents(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_intents_with_options(request, runtime)

    def query_knowledges_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.category_id):
            query['CategoryId'] = request.category_id
        if not UtilClient.is_unset(request.core_word_name):
            query['CoreWordName'] = request.core_word_name
        if not UtilClient.is_unset(request.knowledge_title):
            query['KnowledgeTitle'] = request.knowledge_title
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryKnowledges',
            version='2017-10-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20171011_models.QueryKnowledgesResponse(),
            self.call_api(params, req, runtime)
        )

    def query_knowledges(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_knowledges_with_options(request, runtime)

    def query_perspectives_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryPerspectives',
            version='2017-10-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20171011_models.QueryPerspectivesResponse(),
            self.call_api(params, req, runtime)
        )

    def query_perspectives(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_perspectives_with_options(request, runtime)

    def query_system_entities_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.entity_name):
            query['EntityName'] = request.entity_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QuerySystemEntities',
            version='2017-10-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20171011_models.QuerySystemEntitiesResponse(),
            self.call_api(params, req, runtime)
        )

    def query_system_entities(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_system_entities_with_options(request, runtime)

    def remove_entity_member_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = chatbot_20171011_models.RemoveEntityMemberShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.member):
            request.member_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.member), 'Member', 'json')
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.entity_id):
            query['EntityId'] = request.entity_id
        if not UtilClient.is_unset(request.member_shrink):
            query['Member'] = request.member_shrink
        if not UtilClient.is_unset(request.remove_type):
            query['RemoveType'] = request.remove_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemoveEntityMember',
            version='2017-10-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20171011_models.RemoveEntityMemberResponse(),
            self.call_api(params, req, runtime)
        )

    def remove_entity_member(self, request):
        runtime = util_models.RuntimeOptions()
        return self.remove_entity_member_with_options(request, runtime)

    def remove_synonym_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.core_word_name):
            query['CoreWordName'] = request.core_word_name
        if not UtilClient.is_unset(request.synonym):
            query['Synonym'] = request.synonym
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemoveSynonym',
            version='2017-10-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20171011_models.RemoveSynonymResponse(),
            self.call_api(params, req, runtime)
        )

    def remove_synonym(self, request):
        runtime = util_models.RuntimeOptions()
        return self.remove_synonym_with_options(request, runtime)

    def test_dialog_flow_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.dialog_id):
            query['DialogId'] = request.dialog_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TestDialogFlow',
            version='2017-10-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20171011_models.TestDialogFlowResponse(),
            self.call_api(params, req, runtime)
        )

    def test_dialog_flow(self, request):
        runtime = util_models.RuntimeOptions()
        return self.test_dialog_flow_with_options(request, runtime)

    def update_category_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.category_id):
            query['CategoryId'] = request.category_id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateCategory',
            version='2017-10-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20171011_models.UpdateCategoryResponse(),
            self.call_api(params, req, runtime)
        )

    def update_category(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_category_with_options(request, runtime)

    def update_core_word_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.core_word_code):
            query['CoreWordCode'] = request.core_word_code
        if not UtilClient.is_unset(request.core_word_name):
            query['CoreWordName'] = request.core_word_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateCoreWord',
            version='2017-10-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20171011_models.UpdateCoreWordResponse(),
            self.call_api(params, req, runtime)
        )

    def update_core_word(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_core_word_with_options(request, runtime)

    def update_dialog_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.dialog_id):
            query['DialogId'] = request.dialog_id
        if not UtilClient.is_unset(request.dialog_name):
            query['DialogName'] = request.dialog_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateDialog',
            version='2017-10-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20171011_models.UpdateDialogResponse(),
            self.call_api(params, req, runtime)
        )

    def update_dialog(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_dialog_with_options(request, runtime)

    def update_dialog_flow_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = chatbot_20171011_models.UpdateDialogFlowShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.module_definition):
            request.module_definition_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.module_definition), 'ModuleDefinition', 'json')
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.dialog_id):
            query['DialogId'] = request.dialog_id
        body = {}
        if not UtilClient.is_unset(request.module_definition_shrink):
            body['ModuleDefinition'] = request.module_definition_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateDialogFlow',
            version='2017-10-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20171011_models.UpdateDialogFlowResponse(),
            self.call_api(params, req, runtime)
        )

    def update_dialog_flow(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_dialog_flow_with_options(request, runtime)

    def update_entity_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = chatbot_20171011_models.UpdateEntityShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.members):
            request.members_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.members, 'Members', 'json')
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.entity_id):
            query['EntityId'] = request.entity_id
        if not UtilClient.is_unset(request.entity_name):
            query['EntityName'] = request.entity_name
        if not UtilClient.is_unset(request.entity_type):
            query['EntityType'] = request.entity_type
        if not UtilClient.is_unset(request.regex):
            query['Regex'] = request.regex
        body = {}
        if not UtilClient.is_unset(request.members_shrink):
            body['Members'] = request.members_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateEntity',
            version='2017-10-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20171011_models.UpdateEntityResponse(),
            self.call_api(params, req, runtime)
        )

    def update_entity(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_entity_with_options(request, runtime)

    def update_intent_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = chatbot_20171011_models.UpdateIntentShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.intent_definition):
            request.intent_definition_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.intent_definition), 'IntentDefinition', 'json')
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.intent_definition_shrink):
            query['IntentDefinition'] = request.intent_definition_shrink
        if not UtilClient.is_unset(request.intent_id):
            query['IntentId'] = request.intent_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateIntent',
            version='2017-10-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20171011_models.UpdateIntentResponse(),
            self.call_api(params, req, runtime)
        )

    def update_intent(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_intent_with_options(request, runtime)

    def update_knowledge_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = chatbot_20171011_models.UpdateKnowledgeShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.knowledge):
            request.knowledge_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.knowledge), 'Knowledge', 'json')
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        body = {}
        if not UtilClient.is_unset(request.knowledge_shrink):
            body['Knowledge'] = request.knowledge_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateKnowledge',
            version='2017-10-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20171011_models.UpdateKnowledgeResponse(),
            self.call_api(params, req, runtime)
        )

    def update_knowledge(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_knowledge_with_options(request, runtime)

    def update_perspective_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.agent_key):
            query['AgentKey'] = request.agent_key
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.perspective_id):
            query['PerspectiveId'] = request.perspective_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdatePerspective',
            version='2017-10-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            chatbot_20171011_models.UpdatePerspectiveResponse(),
            self.call_api(params, req, runtime)
        )

    def update_perspective(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_perspective_with_options(request, runtime)
