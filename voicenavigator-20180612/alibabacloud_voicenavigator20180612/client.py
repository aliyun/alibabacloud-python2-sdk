# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_voicenavigator20180612 import models as voice_navigator_20180612_models
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
        self._endpoint = self.get_endpoint('voicenavigator', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def associate_chatbot_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.chatbot_instance_id):
            query['ChatbotInstanceId'] = request.chatbot_instance_id
        if not UtilClient.is_unset(request.chatbot_name):
            query['ChatbotName'] = request.chatbot_name
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AssociateChatbotInstance',
            version='2018-06-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            voice_navigator_20180612_models.AssociateChatbotInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    def associate_chatbot_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.associate_chatbot_instance_with_options(request, runtime)

    def audit_ttsvoice_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.speech_rate):
            query['SpeechRate'] = request.speech_rate
        if not UtilClient.is_unset(request.text):
            query['Text'] = request.text
        if not UtilClient.is_unset(request.voice):
            query['Voice'] = request.voice
        if not UtilClient.is_unset(request.volume):
            query['Volume'] = request.volume
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AuditTTSVoice',
            version='2018-06-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            voice_navigator_20180612_models.AuditTTSVoiceResponse(),
            self.call_api(params, req, runtime)
        )

    def audit_ttsvoice(self, request):
        runtime = util_models.RuntimeOptions()
        return self.audit_ttsvoice_with_options(request, runtime)

    def begin_dialogue_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.called_number):
            query['CalledNumber'] = request.called_number
        if not UtilClient.is_unset(request.calling_number):
            query['CallingNumber'] = request.calling_number
        if not UtilClient.is_unset(request.conversation_id):
            query['ConversationId'] = request.conversation_id
        if not UtilClient.is_unset(request.initial_context):
            query['InitialContext'] = request.initial_context
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_owner_id):
            query['InstanceOwnerId'] = request.instance_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BeginDialogue',
            version='2018-06-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            voice_navigator_20180612_models.BeginDialogueResponse(),
            self.call_api(params, req, runtime)
        )

    def begin_dialogue(self, request):
        runtime = util_models.RuntimeOptions()
        return self.begin_dialogue_with_options(request, runtime)

    def collected_number_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.conversation_id):
            query['ConversationId'] = request.conversation_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_owner_id):
            query['InstanceOwnerId'] = request.instance_owner_id
        if not UtilClient.is_unset(request.number):
            query['Number'] = request.number
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CollectedNumber',
            version='2018-06-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            voice_navigator_20180612_models.CollectedNumberResponse(),
            self.call_api(params, req, runtime)
        )

    def collected_number(self, request):
        runtime = util_models.RuntimeOptions()
        return self.collected_number_with_options(request, runtime)

    def create_download_url_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDownloadUrl',
            version='2018-06-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            voice_navigator_20180612_models.CreateDownloadUrlResponse(),
            self.call_api(params, req, runtime)
        )

    def create_download_url(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_download_url_with_options(request, runtime)

    def create_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.concurrency):
            query['Concurrency'] = request.concurrency
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateInstance',
            version='2018-06-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            voice_navigator_20180612_models.CreateInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    def create_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_instance_with_options(request, runtime)

    def debug_begin_dialogue_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.called_number):
            query['CalledNumber'] = request.called_number
        if not UtilClient.is_unset(request.calling_number):
            query['CallingNumber'] = request.calling_number
        if not UtilClient.is_unset(request.conversation_id):
            query['ConversationId'] = request.conversation_id
        if not UtilClient.is_unset(request.initial_context):
            query['InitialContext'] = request.initial_context
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DebugBeginDialogue',
            version='2018-06-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            voice_navigator_20180612_models.DebugBeginDialogueResponse(),
            self.call_api(params, req, runtime)
        )

    def debug_begin_dialogue(self, request):
        runtime = util_models.RuntimeOptions()
        return self.debug_begin_dialogue_with_options(request, runtime)

    def debug_collected_number_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.conversation_id):
            query['ConversationId'] = request.conversation_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.number):
            query['Number'] = request.number
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DebugCollectedNumber',
            version='2018-06-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            voice_navigator_20180612_models.DebugCollectedNumberResponse(),
            self.call_api(params, req, runtime)
        )

    def debug_collected_number(self, request):
        runtime = util_models.RuntimeOptions()
        return self.debug_collected_number_with_options(request, runtime)

    def debug_dialogue_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.additional_context):
            query['AdditionalContext'] = request.additional_context
        if not UtilClient.is_unset(request.conversation_id):
            query['ConversationId'] = request.conversation_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.utterance):
            query['Utterance'] = request.utterance
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DebugDialogue',
            version='2018-06-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            voice_navigator_20180612_models.DebugDialogueResponse(),
            self.call_api(params, req, runtime)
        )

    def debug_dialogue(self, request):
        runtime = util_models.RuntimeOptions()
        return self.debug_dialogue_with_options(request, runtime)

    def delete_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteInstance',
            version='2018-06-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            voice_navigator_20180612_models.DeleteInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_instance_with_options(request, runtime)

    def describe_conversation_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeConversation',
            version='2018-06-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            voice_navigator_20180612_models.DescribeConversationResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_conversation(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_conversation_with_options(request, runtime)

    def describe_conversation_context_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeConversationContext',
            version='2018-06-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            voice_navigator_20180612_models.DescribeConversationContextResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_conversation_context(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_conversation_context_with_options(request, runtime)

    def describe_export_progress_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeExportProgress',
            version='2018-06-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            voice_navigator_20180612_models.DescribeExportProgressResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_export_progress(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_export_progress_with_options(request, runtime)

    def describe_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeInstance',
            version='2018-06-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            voice_navigator_20180612_models.DescribeInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_with_options(request, runtime)

    def describe_navigation_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeNavigationConfig',
            version='2018-06-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            voice_navigator_20180612_models.DescribeNavigationConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_navigation_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_navigation_config_with_options(request, runtime)

    def describe_recording_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRecording',
            version='2018-06-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            voice_navigator_20180612_models.DescribeRecordingResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_recording(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_recording_with_options(request, runtime)

    def describe_statistical_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeStatisticalData',
            version='2018-06-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            voice_navigator_20180612_models.DescribeStatisticalDataResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_statistical_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_statistical_data_with_options(request, runtime)

    def describe_ttsconfig_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeTTSConfig',
            version='2018-06-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            voice_navigator_20180612_models.DescribeTTSConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_ttsconfig(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_ttsconfig_with_options(request, runtime)

    def dialogue_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.additional_context):
            query['AdditionalContext'] = request.additional_context
        if not UtilClient.is_unset(request.called_number):
            query['CalledNumber'] = request.called_number
        if not UtilClient.is_unset(request.calling_number):
            query['CallingNumber'] = request.calling_number
        if not UtilClient.is_unset(request.conversation_id):
            query['ConversationId'] = request.conversation_id
        if not UtilClient.is_unset(request.emotion):
            query['Emotion'] = request.emotion
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_owner_id):
            query['InstanceOwnerId'] = request.instance_owner_id
        if not UtilClient.is_unset(request.utterance):
            query['Utterance'] = request.utterance
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='Dialogue',
            version='2018-06-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            voice_navigator_20180612_models.DialogueResponse(),
            self.call_api(params, req, runtime)
        )

    def dialogue(self, request):
        runtime = util_models.RuntimeOptions()
        return self.dialogue_with_options(request, runtime)

    def disable_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DisableInstance',
            version='2018-06-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            voice_navigator_20180612_models.DisableInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    def disable_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.disable_instance_with_options(request, runtime)

    def enable_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnableInstance',
            version='2018-06-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            voice_navigator_20180612_models.EnableInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    def enable_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.enable_instance_with_options(request, runtime)

    def end_dialogue_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.conversation_id):
            query['ConversationId'] = request.conversation_id
        if not UtilClient.is_unset(request.hang_up_params):
            query['HangUpParams'] = request.hang_up_params
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_owner_id):
            query['InstanceOwnerId'] = request.instance_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EndDialogue',
            version='2018-06-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            voice_navigator_20180612_models.EndDialogueResponse(),
            self.call_api(params, req, runtime)
        )

    def end_dialogue(self, request):
        runtime = util_models.RuntimeOptions()
        return self.end_dialogue_with_options(request, runtime)

    def export_conversation_details_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.begin_time_left_range):
            query['BeginTimeLeftRange'] = request.begin_time_left_range
        if not UtilClient.is_unset(request.begin_time_right_range):
            query['BeginTimeRightRange'] = request.begin_time_right_range
        if not UtilClient.is_unset(request.calling_number):
            query['CallingNumber'] = request.calling_number
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.options):
            query['Options'] = request.options
        if not UtilClient.is_unset(request.rounds_left_range):
            query['RoundsLeftRange'] = request.rounds_left_range
        if not UtilClient.is_unset(request.rounds_right_range):
            query['RoundsRightRange'] = request.rounds_right_range
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ExportConversationDetails',
            version='2018-06-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            voice_navigator_20180612_models.ExportConversationDetailsResponse(),
            self.call_api(params, req, runtime)
        )

    def export_conversation_details(self, request):
        runtime = util_models.RuntimeOptions()
        return self.export_conversation_details_with_options(request, runtime)

    def export_statistical_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.begin_time_left_range):
            query['BeginTimeLeftRange'] = request.begin_time_left_range
        if not UtilClient.is_unset(request.begin_time_right_range):
            query['BeginTimeRightRange'] = request.begin_time_right_range
        if not UtilClient.is_unset(request.export_type):
            query['ExportType'] = request.export_type
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.time_unit):
            query['TimeUnit'] = request.time_unit
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ExportStatisticalData',
            version='2018-06-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            voice_navigator_20180612_models.ExportStatisticalDataResponse(),
            self.call_api(params, req, runtime)
        )

    def export_statistical_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.export_statistical_data_with_options(request, runtime)

    def generate_upload_url_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.caller_bid):
            body['CallerBid'] = request.caller_bid
        if not UtilClient.is_unset(request.caller_ip):
            body['CallerIp'] = request.caller_ip
        if not UtilClient.is_unset(request.caller_parent_id):
            body['CallerParentId'] = request.caller_parent_id
        if not UtilClient.is_unset(request.caller_type):
            body['CallerType'] = request.caller_type
        if not UtilClient.is_unset(request.caller_uid):
            body['CallerUid'] = request.caller_uid
        if not UtilClient.is_unset(request.client_ip):
            body['ClientIp'] = request.client_ip
        if not UtilClient.is_unset(request.environment):
            body['Environment'] = request.environment
        if not UtilClient.is_unset(request.file_name):
            body['FileName'] = request.file_name
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_owner_id):
            body['InstanceOwnerId'] = request.instance_owner_id
        if not UtilClient.is_unset(request.key):
            body['Key'] = request.key
        if not UtilClient.is_unset(request.mfa_present):
            body['MfaPresent'] = request.mfa_present
        if not UtilClient.is_unset(request.proxy_original_security_transport):
            body['ProxyOriginalSecurityTransport'] = request.proxy_original_security_transport
        if not UtilClient.is_unset(request.proxy_original_source_ip):
            body['ProxyOriginalSourceIp'] = request.proxy_original_source_ip
        if not UtilClient.is_unset(request.proxy_trust_transport_info):
            body['ProxyTrustTransportInfo'] = request.proxy_trust_transport_info
        if not UtilClient.is_unset(request.request_id):
            body['RequestId'] = request.request_id
        if not UtilClient.is_unset(request.security_token):
            body['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.security_transport):
            body['SecurityTransport'] = request.security_transport
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.tenant_name):
            body['TenantName'] = request.tenant_name
        if not UtilClient.is_unset(request.user_id):
            body['UserId'] = request.user_id
        if not UtilClient.is_unset(request.user_name):
            body['UserName'] = request.user_name
        if not UtilClient.is_unset(request.xspace_servicer_id):
            body['XspaceServicerId'] = request.xspace_servicer_id
        if not UtilClient.is_unset(request.xspace_tenant_bu_id):
            body['XspaceTenantBuId'] = request.xspace_tenant_bu_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GenerateUploadUrl',
            version='2018-06-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            voice_navigator_20180612_models.GenerateUploadUrlResponse(),
            self.call_api(params, req, runtime)
        )

    def generate_upload_url(self, request):
        runtime = util_models.RuntimeOptions()
        return self.generate_upload_url_with_options(request, runtime)

    def get_asr_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.config_level):
            query['ConfigLevel'] = request.config_level
        if not UtilClient.is_unset(request.entry_id):
            query['EntryId'] = request.entry_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAsrConfig',
            version='2018-06-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            voice_navigator_20180612_models.GetAsrConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def get_asr_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_asr_config_with_options(request, runtime)

    def get_real_time_concurrency_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetRealTimeConcurrency',
            version='2018-06-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            voice_navigator_20180612_models.GetRealTimeConcurrencyResponse(),
            self.call_api(params, req, runtime)
        )

    def get_real_time_concurrency(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_real_time_concurrency_with_options(request, runtime)

    def list_chatbot_instances_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListChatbotInstances',
            version='2018-06-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            voice_navigator_20180612_models.ListChatbotInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_chatbot_instances(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_chatbot_instances_with_options(request, runtime)

    def list_conversation_details_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListConversationDetails',
            version='2018-06-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            voice_navigator_20180612_models.ListConversationDetailsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_conversation_details(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_conversation_details_with_options(request, runtime)

    def list_conversations_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListConversations',
            version='2018-06-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            voice_navigator_20180612_models.ListConversationsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_conversations(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_conversations_with_options(request, runtime)

    def list_download_tasks_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDownloadTasks',
            version='2018-06-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            voice_navigator_20180612_models.ListDownloadTasksResponse(),
            self.call_api(params, req, runtime)
        )

    def list_download_tasks(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_download_tasks_with_options(request, runtime)

    def list_instances_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListInstances',
            version='2018-06-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            voice_navigator_20180612_models.ListInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_instances(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_instances_with_options(request, runtime)

    def modify_asr_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.asr_acoustic_model_id):
            query['AsrAcousticModelId'] = request.asr_acoustic_model_id
        if not UtilClient.is_unset(request.asr_class_vocabulary_id):
            query['AsrClassVocabularyId'] = request.asr_class_vocabulary_id
        if not UtilClient.is_unset(request.asr_customization_id):
            query['AsrCustomizationId'] = request.asr_customization_id
        if not UtilClient.is_unset(request.asr_vocabulary_id):
            query['AsrVocabularyId'] = request.asr_vocabulary_id
        if not UtilClient.is_unset(request.config_level):
            query['ConfigLevel'] = request.config_level
        if not UtilClient.is_unset(request.entry_id):
            query['EntryId'] = request.entry_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyAsrConfig',
            version='2018-06-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            voice_navigator_20180612_models.ModifyAsrConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_asr_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_asr_config_with_options(request, runtime)

    def modify_greeting_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.greeting_words):
            query['GreetingWords'] = request.greeting_words
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.intent_trigger):
            query['IntentTrigger'] = request.intent_trigger
        if not UtilClient.is_unset(request.source_type):
            query['SourceType'] = request.source_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyGreetingConfig',
            version='2018-06-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            voice_navigator_20180612_models.ModifyGreetingConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_greeting_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_greeting_config_with_options(request, runtime)

    def modify_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.concurrency):
            query['Concurrency'] = request.concurrency
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyInstance',
            version='2018-06-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            voice_navigator_20180612_models.ModifyInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_instance_with_options(request, runtime)

    def modify_silence_timeout_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.final_action):
            query['FinalAction'] = request.final_action
        if not UtilClient.is_unset(request.final_action_params):
            query['FinalActionParams'] = request.final_action_params
        if not UtilClient.is_unset(request.final_prompt):
            query['FinalPrompt'] = request.final_prompt
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.intent_trigger):
            query['IntentTrigger'] = request.intent_trigger
        if not UtilClient.is_unset(request.prompt):
            query['Prompt'] = request.prompt
        if not UtilClient.is_unset(request.source_type):
            query['SourceType'] = request.source_type
        if not UtilClient.is_unset(request.threshold):
            query['Threshold'] = request.threshold
        if not UtilClient.is_unset(request.timeout):
            query['Timeout'] = request.timeout
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifySilenceTimeoutConfig',
            version='2018-06-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            voice_navigator_20180612_models.ModifySilenceTimeoutConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_silence_timeout_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_silence_timeout_config_with_options(request, runtime)

    def modify_ttsconfig_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_key):
            query['AppKey'] = request.app_key
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.nls_service_type):
            query['NlsServiceType'] = request.nls_service_type
        if not UtilClient.is_unset(request.speech_rate):
            query['SpeechRate'] = request.speech_rate
        if not UtilClient.is_unset(request.voice):
            query['Voice'] = request.voice
        if not UtilClient.is_unset(request.volume):
            query['Volume'] = request.volume
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyTTSConfig',
            version='2018-06-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            voice_navigator_20180612_models.ModifyTTSConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_ttsconfig(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_ttsconfig_with_options(request, runtime)

    def modify_unrecognizing_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.final_action):
            query['FinalAction'] = request.final_action
        if not UtilClient.is_unset(request.final_action_params):
            query['FinalActionParams'] = request.final_action_params
        if not UtilClient.is_unset(request.final_prompt):
            query['FinalPrompt'] = request.final_prompt
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.prompt):
            query['Prompt'] = request.prompt
        if not UtilClient.is_unset(request.threshold):
            query['Threshold'] = request.threshold
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyUnrecognizingConfig',
            version='2018-06-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            voice_navigator_20180612_models.ModifyUnrecognizingConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_unrecognizing_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_unrecognizing_config_with_options(request, runtime)

    def query_conversations_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryConversations',
            version='2018-06-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            voice_navigator_20180612_models.QueryConversationsResponse(),
            self.call_api(params, req, runtime)
        )

    def query_conversations(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_conversations_with_options(request, runtime)

    def save_recording_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.conversation_id):
            query['ConversationId'] = request.conversation_id
        if not UtilClient.is_unset(request.duration):
            query['Duration'] = request.duration
        if not UtilClient.is_unset(request.file_name):
            query['FileName'] = request.file_name
        if not UtilClient.is_unset(request.file_path):
            query['FilePath'] = request.file_path
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_owner_id):
            query['InstanceOwnerId'] = request.instance_owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        if not UtilClient.is_unset(request.voice_slice_recording_list):
            query['VoiceSliceRecordingList'] = request.voice_slice_recording_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SaveRecording',
            version='2018-06-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            voice_navigator_20180612_models.SaveRecordingResponse(),
            self.call_api(params, req, runtime)
        )

    def save_recording(self, request):
        runtime = util_models.RuntimeOptions()
        return self.save_recording_with_options(request, runtime)

    def silence_timeout_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.conversation_id):
            query['ConversationId'] = request.conversation_id
        if not UtilClient.is_unset(request.initial_context):
            query['InitialContext'] = request.initial_context
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_owner_id):
            query['InstanceOwnerId'] = request.instance_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SilenceTimeout',
            version='2018-06-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            voice_navigator_20180612_models.SilenceTimeoutResponse(),
            self.call_api(params, req, runtime)
        )

    def silence_timeout(self, request):
        runtime = util_models.RuntimeOptions()
        return self.silence_timeout_with_options(request, runtime)
