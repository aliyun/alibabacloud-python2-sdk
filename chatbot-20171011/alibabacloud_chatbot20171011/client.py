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

    def create_entity_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = chatbot_20171011_models.CreateEntityShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.members):
            request.members_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.members, 'Members', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            chatbot_20171011_models.CreateEntityResponse(),
            self.do_rpcrequest('CreateEntity', '2017-10-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_entity(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_entity_with_options(request, runtime)

    def add_synonym_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            chatbot_20171011_models.AddSynonymResponse(),
            self.do_rpcrequest('AddSynonym', '2017-10-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def add_synonym(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_synonym_with_options(request, runtime)

    def delete_category_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            chatbot_20171011_models.DeleteCategoryResponse(),
            self.do_rpcrequest('DeleteCategory', '2017-10-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_category(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_category_with_options(request, runtime)

    def publish_knowledge_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            chatbot_20171011_models.PublishKnowledgeResponse(),
            self.do_rpcrequest('PublishKnowledge', '2017-10-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def publish_knowledge(self, request):
        runtime = util_models.RuntimeOptions()
        return self.publish_knowledge_with_options(request, runtime)

    def list_bot_knowledge_details_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            chatbot_20171011_models.ListBotKnowledgeDetailsResponse(),
            self.do_rpcrequest('ListBotKnowledgeDetails', '2017-10-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_bot_knowledge_details(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_bot_knowledge_details_with_options(request, runtime)

    def query_intents_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            chatbot_20171011_models.QueryIntentsResponse(),
            self.do_rpcrequest('QueryIntents', '2017-10-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_intents(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_intents_with_options(request, runtime)

    def describe_category_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            chatbot_20171011_models.DescribeCategoryResponse(),
            self.do_rpcrequest('DescribeCategory', '2017-10-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_category(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_category_with_options(request, runtime)

    def list_bot_reception_detail_datas_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            chatbot_20171011_models.ListBotReceptionDetailDatasResponse(),
            self.do_rpcrequest('ListBotReceptionDetailDatas', '2017-10-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_bot_reception_detail_datas(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_bot_reception_detail_datas_with_options(request, runtime)

    def append_entity_member_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = chatbot_20171011_models.AppendEntityMemberShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.member):
            request.member_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.member), 'Member', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            chatbot_20171011_models.AppendEntityMemberResponse(),
            self.do_rpcrequest('AppendEntityMember', '2017-10-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def append_entity_member(self, request):
        runtime = util_models.RuntimeOptions()
        return self.append_entity_member_with_options(request, runtime)

    def describe_bot_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            chatbot_20171011_models.DescribeBotResponse(),
            self.do_rpcrequest('DescribeBot', '2017-10-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_bot(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_bot_with_options(request, runtime)

    def list_bot_cold_ds_datas_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            chatbot_20171011_models.ListBotColdDsDatasResponse(),
            self.do_rpcrequest('ListBotColdDsDatas', '2017-10-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_bot_cold_ds_datas(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_bot_cold_ds_datas_with_options(request, runtime)

    def describe_perspective_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            chatbot_20171011_models.DescribePerspectiveResponse(),
            self.do_rpcrequest('DescribePerspective', '2017-10-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_perspective(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_perspective_with_options(request, runtime)

    def update_dialog_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            chatbot_20171011_models.UpdateDialogResponse(),
            self.do_rpcrequest('UpdateDialog', '2017-10-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_dialog(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_dialog_with_options(request, runtime)

    def create_bot_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            chatbot_20171011_models.CreateBotResponse(),
            self.do_rpcrequest('CreateBot', '2017-10-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_bot(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_bot_with_options(request, runtime)

    def describe_intent_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            chatbot_20171011_models.DescribeIntentResponse(),
            self.do_rpcrequest('DescribeIntent', '2017-10-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_intent(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_intent_with_options(request, runtime)

    def query_dialogs_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            chatbot_20171011_models.QueryDialogsResponse(),
            self.do_rpcrequest('QueryDialogs', '2017-10-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_dialogs(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_dialogs_with_options(request, runtime)

    def create_dialog_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            chatbot_20171011_models.CreateDialogResponse(),
            self.do_rpcrequest('CreateDialog', '2017-10-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_dialog(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_dialog_with_options(request, runtime)

    def query_core_words_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            chatbot_20171011_models.QueryCoreWordsResponse(),
            self.do_rpcrequest('QueryCoreWords', '2017-10-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_core_words(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_core_words_with_options(request, runtime)

    def update_core_word_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            chatbot_20171011_models.UpdateCoreWordResponse(),
            self.do_rpcrequest('UpdateCoreWord', '2017-10-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_core_word(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_core_word_with_options(request, runtime)

    def update_category_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            chatbot_20171011_models.UpdateCategoryResponse(),
            self.do_rpcrequest('UpdateCategory', '2017-10-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_category(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_category_with_options(request, runtime)

    def get_conversation_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            chatbot_20171011_models.GetConversationListResponse(),
            self.do_rpcrequest('GetConversationList', '2017-10-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_conversation_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_conversation_list_with_options(request, runtime)

    def update_entity_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = chatbot_20171011_models.UpdateEntityShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.members):
            request.members_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.members, 'Members', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            chatbot_20171011_models.UpdateEntityResponse(),
            self.do_rpcrequest('UpdateEntity', '2017-10-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_entity(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_entity_with_options(request, runtime)

    def delete_core_word_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            chatbot_20171011_models.DeleteCoreWordResponse(),
            self.do_rpcrequest('DeleteCoreWord', '2017-10-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_core_word(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_core_word_with_options(request, runtime)

    def move_knowledge_category_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            chatbot_20171011_models.MoveKnowledgeCategoryResponse(),
            self.do_rpcrequest('MoveKnowledgeCategory', '2017-10-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def move_knowledge_category(self, request):
        runtime = util_models.RuntimeOptions()
        return self.move_knowledge_category_with_options(request, runtime)

    def create_intent_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = chatbot_20171011_models.CreateIntentShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.intent_definition):
            request.intent_definition_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.intent_definition), 'IntentDefinition', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            chatbot_20171011_models.CreateIntentResponse(),
            self.do_rpcrequest('CreateIntent', '2017-10-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_intent(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_intent_with_options(request, runtime)

    def update_perspective_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            chatbot_20171011_models.UpdatePerspectiveResponse(),
            self.do_rpcrequest('UpdatePerspective', '2017-10-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_perspective(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_perspective_with_options(request, runtime)

    def query_categories_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            chatbot_20171011_models.QueryCategoriesResponse(),
            self.do_rpcrequest('QueryCategories', '2017-10-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_categories(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_categories_with_options(request, runtime)

    def delete_dialog_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            chatbot_20171011_models.DeleteDialogResponse(),
            self.do_rpcrequest('DeleteDialog', '2017-10-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_dialog(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_dialog_with_options(request, runtime)

    def query_knowledges_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            chatbot_20171011_models.QueryKnowledgesResponse(),
            self.do_rpcrequest('QueryKnowledges', '2017-10-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_knowledges(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_knowledges_with_options(request, runtime)

    def get_async_result_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            chatbot_20171011_models.GetAsyncResultResponse(),
            self.do_rpcrequest('GetAsyncResult', '2017-10-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_async_result(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_async_result_with_options(request, runtime)

    def describe_dialog_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            chatbot_20171011_models.DescribeDialogResponse(),
            self.do_rpcrequest('DescribeDialog', '2017-10-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dialog(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dialog_with_options(request, runtime)

    def update_intent_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = chatbot_20171011_models.UpdateIntentShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.intent_definition):
            request.intent_definition_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.intent_definition), 'IntentDefinition', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            chatbot_20171011_models.UpdateIntentResponse(),
            self.do_rpcrequest('UpdateIntent', '2017-10-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_intent(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_intent_with_options(request, runtime)

    def remove_synonym_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            chatbot_20171011_models.RemoveSynonymResponse(),
            self.do_rpcrequest('RemoveSynonym', '2017-10-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def remove_synonym(self, request):
        runtime = util_models.RuntimeOptions()
        return self.remove_synonym_with_options(request, runtime)

    def describe_dialog_flow_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            chatbot_20171011_models.DescribeDialogFlowResponse(),
            self.do_rpcrequest('DescribeDialogFlow', '2017-10-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_dialog_flow(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dialog_flow_with_options(request, runtime)

    def activate_perspective_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            chatbot_20171011_models.ActivatePerspectiveResponse(),
            self.do_rpcrequest('ActivatePerspective', '2017-10-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def activate_perspective(self, request):
        runtime = util_models.RuntimeOptions()
        return self.activate_perspective_with_options(request, runtime)

    def describe_knowledge_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            chatbot_20171011_models.DescribeKnowledgeResponse(),
            self.do_rpcrequest('DescribeKnowledge', '2017-10-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_knowledge(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_knowledge_with_options(request, runtime)

    def query_perspectives_with_options(self, runtime):
        req = open_api_models.OpenApiRequest()
        return TeaCore.from_map(
            chatbot_20171011_models.QueryPerspectivesResponse(),
            self.do_rpcrequest('QueryPerspectives', '2017-10-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_perspectives(self):
        runtime = util_models.RuntimeOptions()
        return self.query_perspectives_with_options(runtime)

    def create_perspective_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            chatbot_20171011_models.CreatePerspectiveResponse(),
            self.do_rpcrequest('CreatePerspective', '2017-10-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_perspective(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_perspective_with_options(request, runtime)

    def delete_entity_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            chatbot_20171011_models.DeleteEntityResponse(),
            self.do_rpcrequest('DeleteEntity', '2017-10-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_entity(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_entity_with_options(request, runtime)

    def remove_entity_member_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = chatbot_20171011_models.RemoveEntityMemberShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.member):
            request.member_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.member), 'Member', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            chatbot_20171011_models.RemoveEntityMemberResponse(),
            self.do_rpcrequest('RemoveEntityMember', '2017-10-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def remove_entity_member(self, request):
        runtime = util_models.RuntimeOptions()
        return self.remove_entity_member_with_options(request, runtime)

    def test_dialog_flow_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            chatbot_20171011_models.TestDialogFlowResponse(),
            self.do_rpcrequest('TestDialogFlow', '2017-10-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def test_dialog_flow(self, request):
        runtime = util_models.RuntimeOptions()
        return self.test_dialog_flow_with_options(request, runtime)

    def get_bot_ds_stat_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            chatbot_20171011_models.GetBotDsStatDataResponse(),
            self.do_rpcrequest('GetBotDsStatData', '2017-10-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_bot_ds_stat_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_bot_ds_stat_data_with_options(request, runtime)

    def feedback_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            chatbot_20171011_models.FeedbackResponse(),
            self.do_rpcrequest('Feedback', '2017-10-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def feedback(self, request):
        runtime = util_models.RuntimeOptions()
        return self.feedback_with_options(request, runtime)

    def chat_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            chatbot_20171011_models.ChatResponse(),
            self.do_rpcrequest('Chat', '2017-10-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def chat(self, request):
        runtime = util_models.RuntimeOptions()
        return self.chat_with_options(request, runtime)

    def disable_knowledge_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            chatbot_20171011_models.DisableKnowledgeResponse(),
            self.do_rpcrequest('DisableKnowledge', '2017-10-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def disable_knowledge(self, request):
        runtime = util_models.RuntimeOptions()
        return self.disable_knowledge_with_options(request, runtime)

    def list_bot_hot_ds_datas_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            chatbot_20171011_models.ListBotHotDsDatasResponse(),
            self.do_rpcrequest('ListBotHotDsDatas', '2017-10-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_bot_hot_ds_datas(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_bot_hot_ds_datas_with_options(request, runtime)

    def get_bot_knowledge_stat_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            chatbot_20171011_models.GetBotKnowledgeStatDataResponse(),
            self.do_rpcrequest('GetBotKnowledgeStatData', '2017-10-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_bot_knowledge_stat_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_bot_knowledge_stat_data_with_options(request, runtime)

    def update_knowledge_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = chatbot_20171011_models.UpdateKnowledgeShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.knowledge):
            request.knowledge_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.knowledge), 'Knowledge', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            chatbot_20171011_models.UpdateKnowledgeResponse(),
            self.do_rpcrequest('UpdateKnowledge', '2017-10-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_knowledge(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_knowledge_with_options(request, runtime)

    def create_knowledge_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = chatbot_20171011_models.CreateKnowledgeShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.knowledge):
            request.knowledge_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.knowledge), 'Knowledge', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            chatbot_20171011_models.CreateKnowledgeResponse(),
            self.do_rpcrequest('CreateKnowledge', '2017-10-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_knowledge(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_knowledge_with_options(request, runtime)

    def delete_intent_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            chatbot_20171011_models.DeleteIntentResponse(),
            self.do_rpcrequest('DeleteIntent', '2017-10-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_intent(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_intent_with_options(request, runtime)

    def delete_knowledge_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            chatbot_20171011_models.DeleteKnowledgeResponse(),
            self.do_rpcrequest('DeleteKnowledge', '2017-10-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_knowledge(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_knowledge_with_options(request, runtime)

    def list_bot_chat_historys_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            chatbot_20171011_models.ListBotChatHistorysResponse(),
            self.do_rpcrequest('ListBotChatHistorys', '2017-10-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_bot_chat_historys(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_bot_chat_historys_with_options(request, runtime)

    def disable_dialog_flow_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            chatbot_20171011_models.DisableDialogFlowResponse(),
            self.do_rpcrequest('DisableDialogFlow', '2017-10-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def disable_dialog_flow(self, request):
        runtime = util_models.RuntimeOptions()
        return self.disable_dialog_flow_with_options(request, runtime)

    def query_bots_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            chatbot_20171011_models.QueryBotsResponse(),
            self.do_rpcrequest('QueryBots', '2017-10-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_bots(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_bots_with_options(request, runtime)

    def publish_dialog_flow_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            chatbot_20171011_models.PublishDialogFlowResponse(),
            self.do_rpcrequest('PublishDialogFlow', '2017-10-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def publish_dialog_flow(self, request):
        runtime = util_models.RuntimeOptions()
        return self.publish_dialog_flow_with_options(request, runtime)

    def list_bot_cold_knowledges_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            chatbot_20171011_models.ListBotColdKnowledgesResponse(),
            self.do_rpcrequest('ListBotColdKnowledges', '2017-10-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_bot_cold_knowledges(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_bot_cold_knowledges_with_options(request, runtime)

    def create_core_word_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            chatbot_20171011_models.CreateCoreWordResponse(),
            self.do_rpcrequest('CreateCoreWord', '2017-10-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_core_word(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_core_word_with_options(request, runtime)

    def delete_bot_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            chatbot_20171011_models.DeleteBotResponse(),
            self.do_rpcrequest('DeleteBot', '2017-10-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_bot(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_bot_with_options(request, runtime)

    def query_system_entities_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            chatbot_20171011_models.QuerySystemEntitiesResponse(),
            self.do_rpcrequest('QuerySystemEntities', '2017-10-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_system_entities(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_system_entities_with_options(request, runtime)

    def list_conversation_logs_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            chatbot_20171011_models.ListConversationLogsResponse(),
            self.do_rpcrequest('ListConversationLogs', '2017-10-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_conversation_logs(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_conversation_logs_with_options(request, runtime)

    def get_bot_chat_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            chatbot_20171011_models.GetBotChatDataResponse(),
            self.do_rpcrequest('GetBotChatData', '2017-10-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_bot_chat_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_bot_chat_data_with_options(request, runtime)

    def describe_core_word_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            chatbot_20171011_models.DescribeCoreWordResponse(),
            self.do_rpcrequest('DescribeCoreWord', '2017-10-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_core_word(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_core_word_with_options(request, runtime)

    def get_bot_session_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            chatbot_20171011_models.GetBotSessionDataResponse(),
            self.do_rpcrequest('GetBotSessionData', '2017-10-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_bot_session_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_bot_session_data_with_options(request, runtime)

    def list_bot_hot_knowledges_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            chatbot_20171011_models.ListBotHotKnowledgesResponse(),
            self.do_rpcrequest('ListBotHotKnowledges', '2017-10-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_bot_hot_knowledges(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_bot_hot_knowledges_with_options(request, runtime)

    def query_entities_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            chatbot_20171011_models.QueryEntitiesResponse(),
            self.do_rpcrequest('QueryEntities', '2017-10-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_entities(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_entities_with_options(request, runtime)

    def update_dialog_flow_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = chatbot_20171011_models.UpdateDialogFlowShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.module_definition):
            request.module_definition_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.module_definition), 'ModuleDefinition', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            chatbot_20171011_models.UpdateDialogFlowResponse(),
            self.do_rpcrequest('UpdateDialogFlow', '2017-10-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_dialog_flow(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_dialog_flow_with_options(request, runtime)

    def list_bot_ds_details_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            chatbot_20171011_models.ListBotDsDetailsResponse(),
            self.do_rpcrequest('ListBotDsDetails', '2017-10-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_bot_ds_details(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_bot_ds_details_with_options(request, runtime)

    def associate_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            chatbot_20171011_models.AssociateResponse(),
            self.do_rpcrequest('Associate', '2017-10-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def associate(self, request):
        runtime = util_models.RuntimeOptions()
        return self.associate_with_options(request, runtime)

    def create_category_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            chatbot_20171011_models.CreateCategoryResponse(),
            self.do_rpcrequest('CreateCategory', '2017-10-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_category(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_category_with_options(request, runtime)

    def describe_entities_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            chatbot_20171011_models.DescribeEntitiesResponse(),
            self.do_rpcrequest('DescribeEntities', '2017-10-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_entities(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_entities_with_options(request, runtime)
