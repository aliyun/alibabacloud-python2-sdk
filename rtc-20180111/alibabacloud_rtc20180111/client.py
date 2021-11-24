# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_rtc20180111 import models as rtc_20180111_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_openapi_util.client import Client as OpenApiUtilClient


class Client(OpenApiClient):
    """
    *\
    """
    def __init__(self, config):
        super(Client, self).__init__(config)
        self._endpoint_rule = 'central'
        self.check_config(config)
        self._endpoint = self.get_endpoint('rtc', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def add_record_template_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['AppId'] = request.app_id
        query['BackgroundColor'] = request.background_color
        query['Backgrounds'] = request.backgrounds
        query['ClockWidgets'] = request.clock_widgets
        query['DelayStopTime'] = request.delay_stop_time
        query['EnableM3u8DateTime'] = request.enable_m3u_8date_time
        query['FileSplitInterval'] = request.file_split_interval
        query['Formats'] = request.formats
        query['HttpCallbackUrl'] = request.http_callback_url
        query['LayoutIds'] = request.layout_ids
        query['MediaEncode'] = request.media_encode
        query['MnsQueue'] = request.mns_queue
        query['Name'] = request.name
        query['OssBucket'] = request.oss_bucket
        query['OssFilePrefix'] = request.oss_file_prefix
        query['OwnerId'] = request.owner_id
        query['TaskProfile'] = request.task_profile
        query['Watermarks'] = request.watermarks
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='AddRecordTemplate',
            version='2018-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rtc_20180111_models.AddRecordTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    def add_record_template(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_record_template_with_options(request, runtime)

    def create_auto_live_stream_rule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['AppId'] = request.app_id
        query['CallBack'] = request.call_back
        query['ChannelIdPrefixes'] = request.channel_id_prefixes
        query['ChannelIds'] = request.channel_ids
        query['MediaEncode'] = request.media_encode
        query['OwnerId'] = request.owner_id
        query['PlayDomain'] = request.play_domain
        query['RuleName'] = request.rule_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateAutoLiveStreamRule',
            version='2018-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rtc_20180111_models.CreateAutoLiveStreamRuleResponse(),
            self.call_api(params, req, runtime)
        )

    def create_auto_live_stream_rule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_auto_live_stream_rule_with_options(request, runtime)

    def create_event_subscribe_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['AppId'] = request.app_id
        query['CallbackUrl'] = request.callback_url
        query['ChannelId'] = request.channel_id
        query['ClientToken'] = request.client_token
        query['Events'] = request.events
        query['OwnerId'] = request.owner_id
        query['Users'] = request.users
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateEventSubscribe',
            version='2018-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rtc_20180111_models.CreateEventSubscribeResponse(),
            self.call_api(params, req, runtime)
        )

    def create_event_subscribe(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_event_subscribe_with_options(request, runtime)

    def create_mpulayout_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['AppId'] = request.app_id
        query['AudioMixCount'] = request.audio_mix_count
        query['Name'] = request.name
        query['OwnerId'] = request.owner_id
        query['Panes'] = request.panes
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='CreateMPULayout',
            version='2018-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rtc_20180111_models.CreateMPULayoutResponse(),
            self.call_api(params, req, runtime)
        )

    def create_mpulayout(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_mpulayout_with_options(request, runtime)

    def delete_auto_live_stream_rule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['AppId'] = request.app_id
        query['OwnerId'] = request.owner_id
        query['RuleId'] = request.rule_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteAutoLiveStreamRule',
            version='2018-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rtc_20180111_models.DeleteAutoLiveStreamRuleResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_auto_live_stream_rule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_auto_live_stream_rule_with_options(request, runtime)

    def delete_event_subscribe_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['AppId'] = request.app_id
        query['OwnerId'] = request.owner_id
        query['SubscribeId'] = request.subscribe_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteEventSubscribe',
            version='2018-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rtc_20180111_models.DeleteEventSubscribeResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_event_subscribe(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_event_subscribe_with_options(request, runtime)

    def delete_mpulayout_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['AppId'] = request.app_id
        query['LayoutId'] = request.layout_id
        query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteMPULayout',
            version='2018-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rtc_20180111_models.DeleteMPULayoutResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_mpulayout(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_mpulayout_with_options(request, runtime)

    def delete_record_template_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['AppId'] = request.app_id
        query['OwnerId'] = request.owner_id
        query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DeleteRecordTemplate',
            version='2018-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rtc_20180111_models.DeleteRecordTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_record_template(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_record_template_with_options(request, runtime)

    def describe_auto_live_stream_rule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['AppId'] = request.app_id
        query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeAutoLiveStreamRule',
            version='2018-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rtc_20180111_models.DescribeAutoLiveStreamRuleResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_auto_live_stream_rule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_auto_live_stream_rule_with_options(request, runtime)

    def describe_channel_participants_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['AppId'] = request.app_id
        query['ChannelId'] = request.channel_id
        query['Order'] = request.order
        query['OwnerId'] = request.owner_id
        query['PageNum'] = request.page_num
        query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeChannelParticipants',
            version='2018-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rtc_20180111_models.DescribeChannelParticipantsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_channel_participants(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_channel_participants_with_options(request, runtime)

    def describe_channel_users_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['AppId'] = request.app_id
        query['ChannelId'] = request.channel_id
        query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeChannelUsers',
            version='2018-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rtc_20180111_models.DescribeChannelUsersResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_channel_users(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_channel_users_with_options(request, runtime)

    def describe_mpulayout_info_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['AppId'] = request.app_id
        query['LayoutId'] = request.layout_id
        query['Name'] = request.name
        query['OwnerId'] = request.owner_id
        query['PageNum'] = request.page_num
        query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeMPULayoutInfoList',
            version='2018-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rtc_20180111_models.DescribeMPULayoutInfoListResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_mpulayout_info_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_mpulayout_info_list_with_options(request, runtime)

    def describe_record_files_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['AppId'] = request.app_id
        query['ChannelId'] = request.channel_id
        query['EndTime'] = request.end_time
        query['OwnerId'] = request.owner_id
        query['PageNum'] = request.page_num
        query['PageSize'] = request.page_size
        query['StartTime'] = request.start_time
        query['TaskIds'] = request.task_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeRecordFiles',
            version='2018-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rtc_20180111_models.DescribeRecordFilesResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_record_files(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_record_files_with_options(request, runtime)

    def describe_record_templates_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['AppId'] = request.app_id
        query['OwnerId'] = request.owner_id
        query['PageNum'] = request.page_num
        query['PageSize'] = request.page_size
        query['TemplateIds'] = request.template_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeRecordTemplates',
            version='2018-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rtc_20180111_models.DescribeRecordTemplatesResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_record_templates(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_record_templates_with_options(request, runtime)

    def describe_user_info_in_channel_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['AppId'] = request.app_id
        query['ChannelId'] = request.channel_id
        query['OwnerId'] = request.owner_id
        query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DescribeUserInfoInChannel',
            version='2018-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rtc_20180111_models.DescribeUserInfoInChannelResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_user_info_in_channel(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_user_info_in_channel_with_options(request, runtime)

    def disable_auto_live_stream_rule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['AppId'] = request.app_id
        query['OwnerId'] = request.owner_id
        query['RuleId'] = request.rule_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='DisableAutoLiveStreamRule',
            version='2018-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rtc_20180111_models.DisableAutoLiveStreamRuleResponse(),
            self.call_api(params, req, runtime)
        )

    def disable_auto_live_stream_rule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.disable_auto_live_stream_rule_with_options(request, runtime)

    def enable_auto_live_stream_rule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['AppId'] = request.app_id
        query['OwnerId'] = request.owner_id
        query['RuleId'] = request.rule_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='EnableAutoLiveStreamRule',
            version='2018-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rtc_20180111_models.EnableAutoLiveStreamRuleResponse(),
            self.call_api(params, req, runtime)
        )

    def enable_auto_live_stream_rule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.enable_auto_live_stream_rule_with_options(request, runtime)

    def get_mputask_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['AppId'] = request.app_id
        query['OwnerId'] = request.owner_id
        query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='GetMPUTaskStatus',
            version='2018-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rtc_20180111_models.GetMPUTaskStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def get_mputask_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_mputask_status_with_options(request, runtime)

    def modify_mpulayout_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['AppId'] = request.app_id
        query['AudioMixCount'] = request.audio_mix_count
        query['LayoutId'] = request.layout_id
        query['Name'] = request.name
        query['OwnerId'] = request.owner_id
        query['Panes'] = request.panes
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='ModifyMPULayout',
            version='2018-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rtc_20180111_models.ModifyMPULayoutResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_mpulayout(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_mpulayout_with_options(request, runtime)

    def remove_terminals_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['AppId'] = request.app_id
        query['ChannelId'] = request.channel_id
        query['OwnerId'] = request.owner_id
        query['TerminalIds'] = request.terminal_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='RemoveTerminals',
            version='2018-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rtc_20180111_models.RemoveTerminalsResponse(),
            self.call_api(params, req, runtime)
        )

    def remove_terminals(self, request):
        runtime = util_models.RuntimeOptions()
        return self.remove_terminals_with_options(request, runtime)

    def start_mputask_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['AppId'] = request.app_id
        query['BackgroundColor'] = request.background_color
        query['Backgrounds'] = request.backgrounds
        query['ChannelId'] = request.channel_id
        query['ClockWidgets'] = request.clock_widgets
        query['CropMode'] = request.crop_mode
        query['LayoutIds'] = request.layout_ids
        query['MediaEncode'] = request.media_encode
        query['MixMode'] = request.mix_mode
        query['OwnerId'] = request.owner_id
        query['PayloadType'] = request.payload_type
        query['ReportVad'] = request.report_vad
        query['RtpExtInfo'] = request.rtp_ext_info
        query['SourceType'] = request.source_type
        query['StreamType'] = request.stream_type
        query['StreamURL'] = request.stream_url
        query['SubSpecAudioUsers'] = request.sub_spec_audio_users
        query['SubSpecCameraUsers'] = request.sub_spec_camera_users
        query['SubSpecShareScreenUsers'] = request.sub_spec_share_screen_users
        query['SubSpecUsers'] = request.sub_spec_users
        query['TaskId'] = request.task_id
        query['TaskType'] = request.task_type
        query['TimeStampRef'] = request.time_stamp_ref
        query['UnsubSpecAudioUsers'] = request.unsub_spec_audio_users
        query['UnsubSpecCameraUsers'] = request.unsub_spec_camera_users
        query['UnsubSpecShareScreenUsers'] = request.unsub_spec_share_screen_users
        query['UserPanes'] = request.user_panes
        query['VadInterval'] = request.vad_interval
        query['Watermarks'] = request.watermarks
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='StartMPUTask',
            version='2018-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            rtc_20180111_models.StartMPUTaskResponse(),
            self.call_api(params, req, runtime)
        )

    def start_mputask(self, request):
        runtime = util_models.RuntimeOptions()
        return self.start_mputask_with_options(request, runtime)

    def start_record_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['AppId'] = request.app_id
        query['ChannelId'] = request.channel_id
        query['CropMode'] = request.crop_mode
        query['LayoutIds'] = request.layout_ids
        query['MediaEncode'] = request.media_encode
        query['MixMode'] = request.mix_mode
        query['OwnerId'] = request.owner_id
        query['SourceType'] = request.source_type
        query['StreamType'] = request.stream_type
        query['SubSpecAudioUsers'] = request.sub_spec_audio_users
        query['SubSpecCameraUsers'] = request.sub_spec_camera_users
        query['SubSpecShareScreenUsers'] = request.sub_spec_share_screen_users
        query['SubSpecUsers'] = request.sub_spec_users
        query['TaskId'] = request.task_id
        query['TaskProfile'] = request.task_profile
        query['TemplateId'] = request.template_id
        query['UnsubSpecAudioUsers'] = request.unsub_spec_audio_users
        query['UnsubSpecCameraUsers'] = request.unsub_spec_camera_users
        query['UnsubSpecShareScreenUsers'] = request.unsub_spec_share_screen_users
        query['UserPanes'] = request.user_panes
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='StartRecordTask',
            version='2018-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rtc_20180111_models.StartRecordTaskResponse(),
            self.call_api(params, req, runtime)
        )

    def start_record_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.start_record_task_with_options(request, runtime)

    def stop_channel_user_publish_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['AppId'] = request.app_id
        query['ChannelId'] = request.channel_id
        query['OwnerId'] = request.owner_id
        query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='StopChannelUserPublish',
            version='2018-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rtc_20180111_models.StopChannelUserPublishResponse(),
            self.call_api(params, req, runtime)
        )

    def stop_channel_user_publish(self, request):
        runtime = util_models.RuntimeOptions()
        return self.stop_channel_user_publish_with_options(request, runtime)

    def stop_mputask_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['AppId'] = request.app_id
        query['OwnerId'] = request.owner_id
        query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='StopMPUTask',
            version='2018-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rtc_20180111_models.StopMPUTaskResponse(),
            self.call_api(params, req, runtime)
        )

    def stop_mputask(self, request):
        runtime = util_models.RuntimeOptions()
        return self.stop_mputask_with_options(request, runtime)

    def stop_record_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['AppId'] = request.app_id
        query['OwnerId'] = request.owner_id
        query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='StopRecordTask',
            version='2018-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rtc_20180111_models.StopRecordTaskResponse(),
            self.call_api(params, req, runtime)
        )

    def stop_record_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.stop_record_task_with_options(request, runtime)

    def update_auto_live_stream_rule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['AppId'] = request.app_id
        query['CallBack'] = request.call_back
        query['ChannelIdPrefixes'] = request.channel_id_prefixes
        query['ChannelIds'] = request.channel_ids
        query['MediaEncode'] = request.media_encode
        query['OwnerId'] = request.owner_id
        query['PlayDomain'] = request.play_domain
        query['RuleId'] = request.rule_id
        query['RuleName'] = request.rule_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UpdateAutoLiveStreamRule',
            version='2018-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rtc_20180111_models.UpdateAutoLiveStreamRuleResponse(),
            self.call_api(params, req, runtime)
        )

    def update_auto_live_stream_rule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_auto_live_stream_rule_with_options(request, runtime)

    def update_mputask_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['AppId'] = request.app_id
        query['BackgroundColor'] = request.background_color
        query['Backgrounds'] = request.backgrounds
        query['ClockWidgets'] = request.clock_widgets
        query['CropMode'] = request.crop_mode
        query['LayoutIds'] = request.layout_ids
        query['MediaEncode'] = request.media_encode
        query['MixMode'] = request.mix_mode
        query['OwnerId'] = request.owner_id
        query['SourceType'] = request.source_type
        query['StreamType'] = request.stream_type
        query['SubSpecAudioUsers'] = request.sub_spec_audio_users
        query['SubSpecCameraUsers'] = request.sub_spec_camera_users
        query['SubSpecShareScreenUsers'] = request.sub_spec_share_screen_users
        query['SubSpecUsers'] = request.sub_spec_users
        query['TaskId'] = request.task_id
        query['UnsubSpecAudioUsers'] = request.unsub_spec_audio_users
        query['UnsubSpecCameraUsers'] = request.unsub_spec_camera_users
        query['UnsubSpecShareScreenUsers'] = request.unsub_spec_share_screen_users
        query['UserPanes'] = request.user_panes
        query['Watermarks'] = request.watermarks
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UpdateMPUTask',
            version='2018-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rtc_20180111_models.UpdateMPUTaskResponse(),
            self.call_api(params, req, runtime)
        )

    def update_mputask(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_mputask_with_options(request, runtime)

    def update_record_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['AppId'] = request.app_id
        query['ChannelId'] = request.channel_id
        query['LayoutIds'] = request.layout_ids
        query['OwnerId'] = request.owner_id
        query['SubSpecAudioUsers'] = request.sub_spec_audio_users
        query['SubSpecCameraUsers'] = request.sub_spec_camera_users
        query['SubSpecShareScreenUsers'] = request.sub_spec_share_screen_users
        query['SubSpecUsers'] = request.sub_spec_users
        query['TaskId'] = request.task_id
        query['TemplateId'] = request.template_id
        query['UnsubSpecAudioUsers'] = request.unsub_spec_audio_users
        query['UnsubSpecCameraUsers'] = request.unsub_spec_camera_users
        query['UnsubSpecShareScreenUsers'] = request.unsub_spec_share_screen_users
        query['UserPanes'] = request.user_panes
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UpdateRecordTask',
            version='2018-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rtc_20180111_models.UpdateRecordTaskResponse(),
            self.call_api(params, req, runtime)
        )

    def update_record_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_record_task_with_options(request, runtime)

    def update_record_template_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        query['AppId'] = request.app_id
        query['BackgroundColor'] = request.background_color
        query['Backgrounds'] = request.backgrounds
        query['ClockWidgets'] = request.clock_widgets
        query['DelayStopTime'] = request.delay_stop_time
        query['EnableM3u8DateTime'] = request.enable_m3u_8date_time
        query['FileSplitInterval'] = request.file_split_interval
        query['Formats'] = request.formats
        query['HttpCallbackUrl'] = request.http_callback_url
        query['LayoutIds'] = request.layout_ids
        query['MediaEncode'] = request.media_encode
        query['MnsQueue'] = request.mns_queue
        query['Name'] = request.name
        query['OssBucket'] = request.oss_bucket
        query['OssFilePrefix'] = request.oss_file_prefix
        query['OwnerId'] = request.owner_id
        query['TaskProfile'] = request.task_profile
        query['TemplateId'] = request.template_id
        query['Watermarks'] = request.watermarks
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=UtilClient.to_map(request)
        )
        params = open_api_models.Params(
            action='UpdateRecordTemplate',
            version='2018-01-11',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='json',
            body_type='json'
        )
        return TeaCore.from_map(
            rtc_20180111_models.UpdateRecordTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    def update_record_template(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_record_template_with_options(request, runtime)
