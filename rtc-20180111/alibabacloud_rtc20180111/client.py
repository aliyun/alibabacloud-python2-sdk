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
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.background_color):
            query['BackgroundColor'] = request.background_color
        if not UtilClient.is_unset(request.backgrounds):
            query['Backgrounds'] = request.backgrounds
        if not UtilClient.is_unset(request.clock_widgets):
            query['ClockWidgets'] = request.clock_widgets
        if not UtilClient.is_unset(request.delay_stop_time):
            query['DelayStopTime'] = request.delay_stop_time
        if not UtilClient.is_unset(request.enable_m3u_8date_time):
            query['EnableM3u8DateTime'] = request.enable_m3u_8date_time
        if not UtilClient.is_unset(request.file_split_interval):
            query['FileSplitInterval'] = request.file_split_interval
        if not UtilClient.is_unset(request.formats):
            query['Formats'] = request.formats
        if not UtilClient.is_unset(request.http_callback_url):
            query['HttpCallbackUrl'] = request.http_callback_url
        if not UtilClient.is_unset(request.layout_ids):
            query['LayoutIds'] = request.layout_ids
        if not UtilClient.is_unset(request.media_encode):
            query['MediaEncode'] = request.media_encode
        if not UtilClient.is_unset(request.mns_queue):
            query['MnsQueue'] = request.mns_queue
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.oss_bucket):
            query['OssBucket'] = request.oss_bucket
        if not UtilClient.is_unset(request.oss_endpoint):
            query['OssEndpoint'] = request.oss_endpoint
        if not UtilClient.is_unset(request.oss_file_prefix):
            query['OssFilePrefix'] = request.oss_file_prefix
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.task_profile):
            query['TaskProfile'] = request.task_profile
        if not UtilClient.is_unset(request.watermarks):
            query['Watermarks'] = request.watermarks
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddRecordTemplate',
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
            rtc_20180111_models.AddRecordTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    def add_record_template(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_record_template_with_options(request, runtime)

    def create_app_streaming_out_template_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = rtc_20180111_models.CreateAppStreamingOutTemplateShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.streaming_out_template):
            request.streaming_out_template_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.streaming_out_template, 'StreamingOutTemplate', 'json')
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.streaming_out_template_shrink):
            query['StreamingOutTemplate'] = request.streaming_out_template_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateAppStreamingOutTemplate',
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
            rtc_20180111_models.CreateAppStreamingOutTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    def create_app_streaming_out_template(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_app_streaming_out_template_with_options(request, runtime)

    def create_auto_live_stream_rule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.call_back):
            query['CallBack'] = request.call_back
        if not UtilClient.is_unset(request.channel_id_prefixes):
            query['ChannelIdPrefixes'] = request.channel_id_prefixes
        if not UtilClient.is_unset(request.channel_ids):
            query['ChannelIds'] = request.channel_ids
        if not UtilClient.is_unset(request.media_encode):
            query['MediaEncode'] = request.media_encode
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.play_domain):
            query['PlayDomain'] = request.play_domain
        if not UtilClient.is_unset(request.rule_name):
            query['RuleName'] = request.rule_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateAutoLiveStreamRule',
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
            rtc_20180111_models.CreateAutoLiveStreamRuleResponse(),
            self.call_api(params, req, runtime)
        )

    def create_auto_live_stream_rule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_auto_live_stream_rule_with_options(request, runtime)

    def create_event_subscribe_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.callback_url):
            query['CallbackUrl'] = request.callback_url
        if not UtilClient.is_unset(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.events):
            query['Events'] = request.events
        if not UtilClient.is_unset(request.need_callback_auth):
            query['NeedCallbackAuth'] = request.need_callback_auth
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.role):
            query['Role'] = request.role
        if not UtilClient.is_unset(request.users):
            query['Users'] = request.users
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateEventSubscribe',
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
            rtc_20180111_models.CreateEventSubscribeResponse(),
            self.call_api(params, req, runtime)
        )

    def create_event_subscribe(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_event_subscribe_with_options(request, runtime)

    def create_mpulayout_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.audio_mix_count):
            query['AudioMixCount'] = request.audio_mix_count
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.panes):
            query['Panes'] = request.panes
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateMPULayout',
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
            rtc_20180111_models.CreateMPULayoutResponse(),
            self.call_api(params, req, runtime)
        )

    def create_mpulayout(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_mpulayout_with_options(request, runtime)

    def delete_app_streaming_out_template_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = rtc_20180111_models.DeleteAppStreamingOutTemplateShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.streaming_out_template):
            request.streaming_out_template_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.streaming_out_template, 'StreamingOutTemplate', 'json')
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.streaming_out_template_shrink):
            query['StreamingOutTemplate'] = request.streaming_out_template_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteAppStreamingOutTemplate',
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
            rtc_20180111_models.DeleteAppStreamingOutTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_app_streaming_out_template(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_app_streaming_out_template_with_options(request, runtime)

    def delete_auto_live_stream_rule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.rule_id):
            query['RuleId'] = request.rule_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteAutoLiveStreamRule',
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
            rtc_20180111_models.DeleteAutoLiveStreamRuleResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_auto_live_stream_rule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_auto_live_stream_rule_with_options(request, runtime)

    def delete_channel_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteChannel',
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
            rtc_20180111_models.DeleteChannelResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_channel(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_channel_with_options(request, runtime)

    def delete_event_subscribe_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.subscribe_id):
            query['SubscribeId'] = request.subscribe_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteEventSubscribe',
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
            rtc_20180111_models.DeleteEventSubscribeResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_event_subscribe(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_event_subscribe_with_options(request, runtime)

    def delete_mpulayout_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.layout_id):
            query['LayoutId'] = request.layout_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteMPULayout',
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
            rtc_20180111_models.DeleteMPULayoutResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_mpulayout(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_mpulayout_with_options(request, runtime)

    def delete_record_template_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteRecordTemplate',
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
            rtc_20180111_models.DeleteRecordTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_record_template(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_record_template_with_options(request, runtime)

    def describe_app_key_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAppKey',
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
            rtc_20180111_models.DescribeAppKeyResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_app_key(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_app_key_with_options(request, runtime)

    def describe_app_streaming_out_templates_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = rtc_20180111_models.DescribeAppStreamingOutTemplatesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.condition):
            request.condition_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.condition, 'Condition', 'json')
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.condition_shrink):
            query['Condition'] = request.condition_shrink
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAppStreamingOutTemplates',
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
            rtc_20180111_models.DescribeAppStreamingOutTemplatesResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_app_streaming_out_templates(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_app_streaming_out_templates_with_options(request, runtime)

    def describe_apps_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeApps',
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
            rtc_20180111_models.DescribeAppsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_apps(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_apps_with_options(request, runtime)

    def describe_auto_live_stream_rule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAutoLiveStreamRule',
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
            rtc_20180111_models.DescribeAutoLiveStreamRuleResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_auto_live_stream_rule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_auto_live_stream_rule_with_options(request, runtime)

    def describe_call_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.created_ts):
            query['CreatedTs'] = request.created_ts
        if not UtilClient.is_unset(request.destroyed_ts):
            query['DestroyedTs'] = request.destroyed_ts
        if not UtilClient.is_unset(request.ext_data_type):
            query['ExtDataType'] = request.ext_data_type
        if not UtilClient.is_unset(request.query_exp_info):
            query['QueryExpInfo'] = request.query_exp_info
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCall',
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
            rtc_20180111_models.DescribeCallResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_call(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_call_with_options(request, runtime)

    def describe_call_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.call_status):
            query['CallStatus'] = request.call_status
        if not UtilClient.is_unset(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.end_ts):
            query['EndTs'] = request.end_ts
        if not UtilClient.is_unset(request.order_by):
            query['OrderBy'] = request.order_by
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.query_mode):
            query['QueryMode'] = request.query_mode
        if not UtilClient.is_unset(request.start_ts):
            query['StartTs'] = request.start_ts
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCallList',
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
            rtc_20180111_models.DescribeCallListResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_call_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_call_list_with_options(request, runtime)

    def describe_channel_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.channel_id):
            query['ChannelId'] = request.channel_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeChannel',
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
            rtc_20180111_models.DescribeChannelResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_channel(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_channel_with_options(request, runtime)

    def describe_channel_all_users_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.channel_id):
            query['ChannelId'] = request.channel_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeChannelAllUsers',
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
            rtc_20180111_models.DescribeChannelAllUsersResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_channel_all_users(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_channel_all_users_with_options(request, runtime)

    def describe_channel_area_distribution_stat_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.created_ts):
            query['CreatedTs'] = request.created_ts
        if not UtilClient.is_unset(request.destroyed_ts):
            query['DestroyedTs'] = request.destroyed_ts
        if not UtilClient.is_unset(request.parent_area):
            query['ParentArea'] = request.parent_area
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeChannelAreaDistributionStatData',
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
            rtc_20180111_models.DescribeChannelAreaDistributionStatDataResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_channel_area_distribution_stat_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_channel_area_distribution_stat_data_with_options(request, runtime)

    def describe_channel_distribution_stat_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.created_ts):
            query['CreatedTs'] = request.created_ts
        if not UtilClient.is_unset(request.destroyed_ts):
            query['DestroyedTs'] = request.destroyed_ts
        if not UtilClient.is_unset(request.stat_dim):
            query['StatDim'] = request.stat_dim
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeChannelDistributionStatData',
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
            rtc_20180111_models.DescribeChannelDistributionStatDataResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_channel_distribution_stat_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_channel_distribution_stat_data_with_options(request, runtime)

    def describe_channel_overall_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.created_ts):
            query['CreatedTs'] = request.created_ts
        if not UtilClient.is_unset(request.destroyed_ts):
            query['DestroyedTs'] = request.destroyed_ts
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeChannelOverallData',
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
            rtc_20180111_models.DescribeChannelOverallDataResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_channel_overall_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_channel_overall_data_with_options(request, runtime)

    def describe_channel_participants_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeChannelParticipants',
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
            rtc_20180111_models.DescribeChannelParticipantsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_channel_participants(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_channel_participants_with_options(request, runtime)

    def describe_channel_top_pub_user_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.created_ts):
            query['CreatedTs'] = request.created_ts
        if not UtilClient.is_unset(request.destroyed_ts):
            query['DestroyedTs'] = request.destroyed_ts
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeChannelTopPubUserList',
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
            rtc_20180111_models.DescribeChannelTopPubUserListResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_channel_top_pub_user_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_channel_top_pub_user_list_with_options(request, runtime)

    def describe_channel_user_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeChannelUser',
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
            rtc_20180111_models.DescribeChannelUserResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_channel_user(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_channel_user_with_options(request, runtime)

    def describe_channel_user_metrics_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.created_ts):
            query['CreatedTs'] = request.created_ts
        if not UtilClient.is_unset(request.destroyed_ts):
            query['DestroyedTs'] = request.destroyed_ts
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeChannelUserMetrics',
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
            rtc_20180111_models.DescribeChannelUserMetricsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_channel_user_metrics(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_channel_user_metrics_with_options(request, runtime)

    def describe_channel_users_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeChannelUsers',
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
            rtc_20180111_models.DescribeChannelUsersResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_channel_users(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_channel_users_with_options(request, runtime)

    def describe_end_point_event_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.created_ts):
            query['CreatedTs'] = request.created_ts
        if not UtilClient.is_unset(request.destroyed_ts):
            query['DestroyedTs'] = request.destroyed_ts
        if not UtilClient.is_unset(request.user_id_list):
            query['UserIdList'] = request.user_id_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeEndPointEventList',
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
            rtc_20180111_models.DescribeEndPointEventListResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_end_point_event_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_end_point_event_list_with_options(request, runtime)

    def describe_end_point_metric_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.created_ts):
            query['CreatedTs'] = request.created_ts
        if not UtilClient.is_unset(request.destroyed_ts):
            query['DestroyedTs'] = request.destroyed_ts
        if not UtilClient.is_unset(request.metrics):
            query['Metrics'] = request.metrics
        if not UtilClient.is_unset(request.pub_call_id_list):
            query['PubCallIdList'] = request.pub_call_id_list
        if not UtilClient.is_unset(request.pub_user_id):
            query['PubUserId'] = request.pub_user_id
        if not UtilClient.is_unset(request.sub_user_id):
            query['SubUserId'] = request.sub_user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeEndPointMetricData',
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
            rtc_20180111_models.DescribeEndPointMetricDataResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_end_point_metric_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_end_point_metric_data_with_options(request, runtime)

    def describe_fault_diagnosis_factor_distribution_stat_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.end_ts):
            query['EndTs'] = request.end_ts
        if not UtilClient.is_unset(request.start_ts):
            query['StartTs'] = request.start_ts
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeFaultDiagnosisFactorDistributionStat',
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
            rtc_20180111_models.DescribeFaultDiagnosisFactorDistributionStatResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_fault_diagnosis_factor_distribution_stat(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_fault_diagnosis_factor_distribution_stat_with_options(request, runtime)

    def describe_fault_diagnosis_overall_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.end_ts):
            query['EndTs'] = request.end_ts
        if not UtilClient.is_unset(request.start_ts):
            query['StartTs'] = request.start_ts
        if not UtilClient.is_unset(request.stat_dim):
            query['StatDim'] = request.stat_dim
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeFaultDiagnosisOverallData',
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
            rtc_20180111_models.DescribeFaultDiagnosisOverallDataResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_fault_diagnosis_overall_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_fault_diagnosis_overall_data_with_options(request, runtime)

    def describe_fault_diagnosis_user_detail_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.created_ts):
            query['CreatedTs'] = request.created_ts
        if not UtilClient.is_unset(request.fault_type):
            query['FaultType'] = request.fault_type
        if not UtilClient.is_unset(request.query_call_user_info):
            query['QueryCallUserInfo'] = request.query_call_user_info
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeFaultDiagnosisUserDetail',
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
            rtc_20180111_models.DescribeFaultDiagnosisUserDetailResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_fault_diagnosis_user_detail(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_fault_diagnosis_user_detail_with_options(request, runtime)

    def describe_fault_diagnosis_user_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.end_ts):
            query['EndTs'] = request.end_ts
        if not UtilClient.is_unset(request.fault_types):
            query['FaultTypes'] = request.fault_types
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.start_ts):
            query['StartTs'] = request.start_ts
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeFaultDiagnosisUserList',
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
            rtc_20180111_models.DescribeFaultDiagnosisUserListResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_fault_diagnosis_user_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_fault_diagnosis_user_list_with_options(request, runtime)

    def describe_mpulayout_info_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.layout_id):
            query['LayoutId'] = request.layout_id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeMPULayoutInfoList',
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
            rtc_20180111_models.DescribeMPULayoutInfoListResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_mpulayout_info_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_mpulayout_info_list_with_options(request, runtime)

    def describe_pub_user_list_by_sub_user_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.created_ts):
            query['CreatedTs'] = request.created_ts
        if not UtilClient.is_unset(request.destroyed_ts):
            query['DestroyedTs'] = request.destroyed_ts
        if not UtilClient.is_unset(request.sub_user_id):
            query['SubUserId'] = request.sub_user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePubUserListBySubUser',
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
            rtc_20180111_models.DescribePubUserListBySubUserResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_pub_user_list_by_sub_user(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_pub_user_list_by_sub_user_with_options(request, runtime)

    def describe_qoe_metric_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.created_ts):
            query['CreatedTs'] = request.created_ts
        if not UtilClient.is_unset(request.destroyed_ts):
            query['DestroyedTs'] = request.destroyed_ts
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeQoeMetricData',
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
            rtc_20180111_models.DescribeQoeMetricDataResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_qoe_metric_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_qoe_metric_data_with_options(request, runtime)

    def describe_quality_area_distribution_stat_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.end_date):
            query['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.parent_area):
            query['ParentArea'] = request.parent_area
        if not UtilClient.is_unset(request.start_date):
            query['StartDate'] = request.start_date
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeQualityAreaDistributionStatData',
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
            rtc_20180111_models.DescribeQualityAreaDistributionStatDataResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_quality_area_distribution_stat_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_quality_area_distribution_stat_data_with_options(request, runtime)

    def describe_quality_distribution_stat_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.end_date):
            query['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.start_date):
            query['StartDate'] = request.start_date
        if not UtilClient.is_unset(request.stat_dim):
            query['StatDim'] = request.stat_dim
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeQualityDistributionStatData',
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
            rtc_20180111_models.DescribeQualityDistributionStatDataResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_quality_distribution_stat_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_quality_distribution_stat_data_with_options(request, runtime)

    def describe_quality_os_sdk_version_distribution_stat_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.end_date):
            query['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.start_date):
            query['StartDate'] = request.start_date
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeQualityOsSdkVersionDistributionStatData',
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
            rtc_20180111_models.DescribeQualityOsSdkVersionDistributionStatDataResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_quality_os_sdk_version_distribution_stat_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_quality_os_sdk_version_distribution_stat_data_with_options(request, runtime)

    def describe_quality_overall_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.end_date):
            query['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.start_date):
            query['StartDate'] = request.start_date
        if not UtilClient.is_unset(request.types):
            query['Types'] = request.types
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeQualityOverallData',
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
            rtc_20180111_models.DescribeQualityOverallDataResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_quality_overall_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_quality_overall_data_with_options(request, runtime)

    def describe_record_files_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.task_ids):
            query['TaskIds'] = request.task_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRecordFiles',
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
            rtc_20180111_models.DescribeRecordFilesResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_record_files(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_record_files_with_options(request, runtime)

    def describe_record_templates_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.template_ids):
            query['TemplateIds'] = request.template_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRecordTemplates',
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
            rtc_20180111_models.DescribeRecordTemplatesResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_record_templates(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_record_templates_with_options(request, runtime)

    def describe_rtc_channel_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.service_area):
            query['ServiceArea'] = request.service_area
        if not UtilClient.is_unset(request.sort_type):
            query['SortType'] = request.sort_type
        if not UtilClient.is_unset(request.time_point):
            query['TimePoint'] = request.time_point
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRtcChannelList',
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
            rtc_20180111_models.DescribeRtcChannelListResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_rtc_channel_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_rtc_channel_list_with_options(request, runtime)

    def describe_rtc_channel_metric_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.time_point):
            query['TimePoint'] = request.time_point
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRtcChannelMetric',
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
            rtc_20180111_models.DescribeRtcChannelMetricResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_rtc_channel_metric(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_rtc_channel_metric_with_options(request, runtime)

    def describe_rtc_duration_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.service_area):
            query['ServiceArea'] = request.service_area
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRtcDurationData',
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
            rtc_20180111_models.DescribeRtcDurationDataResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_rtc_duration_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_rtc_duration_data_with_options(request, runtime)

    def describe_rtc_peak_channel_cnt_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.service_area):
            query['ServiceArea'] = request.service_area
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRtcPeakChannelCntData',
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
            rtc_20180111_models.DescribeRtcPeakChannelCntDataResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_rtc_peak_channel_cnt_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_rtc_peak_channel_cnt_data_with_options(request, runtime)

    def describe_rtc_user_cnt_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.service_area):
            query['ServiceArea'] = request.service_area
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRtcUserCntData',
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
            rtc_20180111_models.DescribeRtcUserCntDataResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_rtc_user_cnt_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_rtc_user_cnt_data_with_options(request, runtime)

    def describe_usage_area_distribution_stat_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.end_date):
            query['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.parent_area):
            query['ParentArea'] = request.parent_area
        if not UtilClient.is_unset(request.start_date):
            query['StartDate'] = request.start_date
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeUsageAreaDistributionStatData',
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
            rtc_20180111_models.DescribeUsageAreaDistributionStatDataResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_usage_area_distribution_stat_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_usage_area_distribution_stat_data_with_options(request, runtime)

    def describe_usage_distribution_stat_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.end_date):
            query['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.start_date):
            query['StartDate'] = request.start_date
        if not UtilClient.is_unset(request.stat_dim):
            query['StatDim'] = request.stat_dim
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeUsageDistributionStatData',
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
            rtc_20180111_models.DescribeUsageDistributionStatDataResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_usage_distribution_stat_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_usage_distribution_stat_data_with_options(request, runtime)

    def describe_usage_os_sdk_version_distribution_stat_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.end_date):
            query['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.start_date):
            query['StartDate'] = request.start_date
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeUsageOsSdkVersionDistributionStatData',
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
            rtc_20180111_models.DescribeUsageOsSdkVersionDistributionStatDataResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_usage_os_sdk_version_distribution_stat_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_usage_os_sdk_version_distribution_stat_data_with_options(request, runtime)

    def describe_usage_overall_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.end_date):
            query['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.start_date):
            query['StartDate'] = request.start_date
        if not UtilClient.is_unset(request.types):
            query['Types'] = request.types
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeUsageOverallData',
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
            rtc_20180111_models.DescribeUsageOverallDataResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_usage_overall_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_usage_overall_data_with_options(request, runtime)

    def describe_user_info_in_channel_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeUserInfoInChannel',
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
            rtc_20180111_models.DescribeUserInfoInChannelResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_user_info_in_channel(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_user_info_in_channel_with_options(request, runtime)

    def disable_auto_live_stream_rule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.rule_id):
            query['RuleId'] = request.rule_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DisableAutoLiveStreamRule',
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
            rtc_20180111_models.DisableAutoLiveStreamRuleResponse(),
            self.call_api(params, req, runtime)
        )

    def disable_auto_live_stream_rule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.disable_auto_live_stream_rule_with_options(request, runtime)

    def enable_auto_live_stream_rule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.rule_id):
            query['RuleId'] = request.rule_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnableAutoLiveStreamRule',
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
            rtc_20180111_models.EnableAutoLiveStreamRuleResponse(),
            self.call_api(params, req, runtime)
        )

    def enable_auto_live_stream_rule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.enable_auto_live_stream_rule_with_options(request, runtime)

    def get_mputask_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetMPUTaskStatus',
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
            rtc_20180111_models.GetMPUTaskStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def get_mputask_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_mputask_status_with_options(request, runtime)

    def modify_app_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyApp',
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
            rtc_20180111_models.ModifyAppResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_app(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_app_with_options(request, runtime)

    def modify_app_streaming_out_template_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = rtc_20180111_models.ModifyAppStreamingOutTemplateShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.streaming_out_template):
            request.streaming_out_template_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.streaming_out_template, 'StreamingOutTemplate', 'json')
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.streaming_out_template_shrink):
            query['StreamingOutTemplate'] = request.streaming_out_template_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyAppStreamingOutTemplate',
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
            rtc_20180111_models.ModifyAppStreamingOutTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_app_streaming_out_template(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_app_streaming_out_template_with_options(request, runtime)

    def modify_mpulayout_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.audio_mix_count):
            query['AudioMixCount'] = request.audio_mix_count
        if not UtilClient.is_unset(request.layout_id):
            query['LayoutId'] = request.layout_id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.panes):
            query['Panes'] = request.panes
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyMPULayout',
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
            rtc_20180111_models.ModifyMPULayoutResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_mpulayout(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_mpulayout_with_options(request, runtime)

    def remove_terminals_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.terminal_ids):
            query['TerminalIds'] = request.terminal_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemoveTerminals',
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
            rtc_20180111_models.RemoveTerminalsResponse(),
            self.call_api(params, req, runtime)
        )

    def remove_terminals(self, request):
        runtime = util_models.RuntimeOptions()
        return self.remove_terminals_with_options(request, runtime)

    def remove_users_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.users):
            query['Users'] = request.users
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemoveUsers',
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
            rtc_20180111_models.RemoveUsersResponse(),
            self.call_api(params, req, runtime)
        )

    def remove_users(self, request):
        runtime = util_models.RuntimeOptions()
        return self.remove_users_with_options(request, runtime)

    def start_cloud_record_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.panes):
            query['Panes'] = request.panes
        if not UtilClient.is_unset(request.storage_config):
            query['StorageConfig'] = request.storage_config
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartCloudRecord',
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
            rtc_20180111_models.StartCloudRecordResponse(),
            self.call_api(params, req, runtime)
        )

    def start_cloud_record(self, request):
        runtime = util_models.RuntimeOptions()
        return self.start_cloud_record_with_options(request, runtime)

    def start_mputask_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.background_color):
            query['BackgroundColor'] = request.background_color
        if not UtilClient.is_unset(request.backgrounds):
            query['Backgrounds'] = request.backgrounds
        if not UtilClient.is_unset(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.clock_widgets):
            query['ClockWidgets'] = request.clock_widgets
        if not UtilClient.is_unset(request.crop_mode):
            query['CropMode'] = request.crop_mode
        if not UtilClient.is_unset(request.layout_ids):
            query['LayoutIds'] = request.layout_ids
        if not UtilClient.is_unset(request.media_encode):
            query['MediaEncode'] = request.media_encode
        if not UtilClient.is_unset(request.mix_mode):
            query['MixMode'] = request.mix_mode
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.payload_type):
            query['PayloadType'] = request.payload_type
        if not UtilClient.is_unset(request.report_vad):
            query['ReportVad'] = request.report_vad
        if not UtilClient.is_unset(request.rtp_ext_info):
            query['RtpExtInfo'] = request.rtp_ext_info
        if not UtilClient.is_unset(request.source_type):
            query['SourceType'] = request.source_type
        if not UtilClient.is_unset(request.stream_type):
            query['StreamType'] = request.stream_type
        if not UtilClient.is_unset(request.stream_url):
            query['StreamURL'] = request.stream_url
        if not UtilClient.is_unset(request.sub_spec_audio_users):
            query['SubSpecAudioUsers'] = request.sub_spec_audio_users
        if not UtilClient.is_unset(request.sub_spec_camera_users):
            query['SubSpecCameraUsers'] = request.sub_spec_camera_users
        if not UtilClient.is_unset(request.sub_spec_share_screen_users):
            query['SubSpecShareScreenUsers'] = request.sub_spec_share_screen_users
        if not UtilClient.is_unset(request.sub_spec_users):
            query['SubSpecUsers'] = request.sub_spec_users
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.task_type):
            query['TaskType'] = request.task_type
        if not UtilClient.is_unset(request.time_stamp_ref):
            query['TimeStampRef'] = request.time_stamp_ref
        if not UtilClient.is_unset(request.unsub_spec_audio_users):
            query['UnsubSpecAudioUsers'] = request.unsub_spec_audio_users
        if not UtilClient.is_unset(request.unsub_spec_camera_users):
            query['UnsubSpecCameraUsers'] = request.unsub_spec_camera_users
        if not UtilClient.is_unset(request.unsub_spec_share_screen_users):
            query['UnsubSpecShareScreenUsers'] = request.unsub_spec_share_screen_users
        if not UtilClient.is_unset(request.user_panes):
            query['UserPanes'] = request.user_panes
        if not UtilClient.is_unset(request.vad_interval):
            query['VadInterval'] = request.vad_interval
        if not UtilClient.is_unset(request.watermarks):
            query['Watermarks'] = request.watermarks
        body = {}
        body_flat = {}
        if not UtilClient.is_unset(request.enhanced_param):
            body_flat['EnhancedParam'] = request.enhanced_param
        body = TeaCore.merge(body,
            OpenApiUtilClient.query(body_flat))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
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
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.crop_mode):
            query['CropMode'] = request.crop_mode
        if not UtilClient.is_unset(request.layout_ids):
            query['LayoutIds'] = request.layout_ids
        if not UtilClient.is_unset(request.media_encode):
            query['MediaEncode'] = request.media_encode
        if not UtilClient.is_unset(request.mix_mode):
            query['MixMode'] = request.mix_mode
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.source_type):
            query['SourceType'] = request.source_type
        if not UtilClient.is_unset(request.stream_type):
            query['StreamType'] = request.stream_type
        if not UtilClient.is_unset(request.sub_spec_audio_users):
            query['SubSpecAudioUsers'] = request.sub_spec_audio_users
        if not UtilClient.is_unset(request.sub_spec_camera_users):
            query['SubSpecCameraUsers'] = request.sub_spec_camera_users
        if not UtilClient.is_unset(request.sub_spec_share_screen_users):
            query['SubSpecShareScreenUsers'] = request.sub_spec_share_screen_users
        if not UtilClient.is_unset(request.sub_spec_users):
            query['SubSpecUsers'] = request.sub_spec_users
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.task_profile):
            query['TaskProfile'] = request.task_profile
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        if not UtilClient.is_unset(request.unsub_spec_audio_users):
            query['UnsubSpecAudioUsers'] = request.unsub_spec_audio_users
        if not UtilClient.is_unset(request.unsub_spec_camera_users):
            query['UnsubSpecCameraUsers'] = request.unsub_spec_camera_users
        if not UtilClient.is_unset(request.unsub_spec_share_screen_users):
            query['UnsubSpecShareScreenUsers'] = request.unsub_spec_share_screen_users
        if not UtilClient.is_unset(request.user_panes):
            query['UserPanes'] = request.user_panes
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartRecordTask',
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
            rtc_20180111_models.StartRecordTaskResponse(),
            self.call_api(params, req, runtime)
        )

    def start_record_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.start_record_task_with_options(request, runtime)

    def start_streaming_out_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.panes):
            query['Panes'] = request.panes
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartStreamingOut',
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
            rtc_20180111_models.StartStreamingOutResponse(),
            self.call_api(params, req, runtime)
        )

    def start_streaming_out(self, request):
        runtime = util_models.RuntimeOptions()
        return self.start_streaming_out_with_options(request, runtime)

    def stop_channel_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.channel_id):
            query['ChannelId'] = request.channel_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopChannel',
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
            rtc_20180111_models.StopChannelResponse(),
            self.call_api(params, req, runtime)
        )

    def stop_channel(self, request):
        runtime = util_models.RuntimeOptions()
        return self.stop_channel_with_options(request, runtime)

    def stop_cloud_record_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopCloudRecord',
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
            rtc_20180111_models.StopCloudRecordResponse(),
            self.call_api(params, req, runtime)
        )

    def stop_cloud_record(self, request):
        runtime = util_models.RuntimeOptions()
        return self.stop_cloud_record_with_options(request, runtime)

    def stop_mputask_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopMPUTask',
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
            rtc_20180111_models.StopMPUTaskResponse(),
            self.call_api(params, req, runtime)
        )

    def stop_mputask(self, request):
        runtime = util_models.RuntimeOptions()
        return self.stop_mputask_with_options(request, runtime)

    def stop_record_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopRecordTask',
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
            rtc_20180111_models.StopRecordTaskResponse(),
            self.call_api(params, req, runtime)
        )

    def stop_record_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.stop_record_task_with_options(request, runtime)

    def stop_streaming_out_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopStreamingOut',
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
            rtc_20180111_models.StopStreamingOutResponse(),
            self.call_api(params, req, runtime)
        )

    def stop_streaming_out(self, request):
        runtime = util_models.RuntimeOptions()
        return self.stop_streaming_out_with_options(request, runtime)

    def update_auto_live_stream_rule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.call_back):
            query['CallBack'] = request.call_back
        if not UtilClient.is_unset(request.channel_id_prefixes):
            query['ChannelIdPrefixes'] = request.channel_id_prefixes
        if not UtilClient.is_unset(request.channel_ids):
            query['ChannelIds'] = request.channel_ids
        if not UtilClient.is_unset(request.media_encode):
            query['MediaEncode'] = request.media_encode
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.play_domain):
            query['PlayDomain'] = request.play_domain
        if not UtilClient.is_unset(request.rule_id):
            query['RuleId'] = request.rule_id
        if not UtilClient.is_unset(request.rule_name):
            query['RuleName'] = request.rule_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateAutoLiveStreamRule',
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
            rtc_20180111_models.UpdateAutoLiveStreamRuleResponse(),
            self.call_api(params, req, runtime)
        )

    def update_auto_live_stream_rule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_auto_live_stream_rule_with_options(request, runtime)

    def update_mputask_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.background_color):
            query['BackgroundColor'] = request.background_color
        if not UtilClient.is_unset(request.backgrounds):
            query['Backgrounds'] = request.backgrounds
        if not UtilClient.is_unset(request.clock_widgets):
            query['ClockWidgets'] = request.clock_widgets
        if not UtilClient.is_unset(request.crop_mode):
            query['CropMode'] = request.crop_mode
        if not UtilClient.is_unset(request.layout_ids):
            query['LayoutIds'] = request.layout_ids
        if not UtilClient.is_unset(request.media_encode):
            query['MediaEncode'] = request.media_encode
        if not UtilClient.is_unset(request.mix_mode):
            query['MixMode'] = request.mix_mode
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.source_type):
            query['SourceType'] = request.source_type
        if not UtilClient.is_unset(request.stream_type):
            query['StreamType'] = request.stream_type
        if not UtilClient.is_unset(request.sub_spec_audio_users):
            query['SubSpecAudioUsers'] = request.sub_spec_audio_users
        if not UtilClient.is_unset(request.sub_spec_camera_users):
            query['SubSpecCameraUsers'] = request.sub_spec_camera_users
        if not UtilClient.is_unset(request.sub_spec_share_screen_users):
            query['SubSpecShareScreenUsers'] = request.sub_spec_share_screen_users
        if not UtilClient.is_unset(request.sub_spec_users):
            query['SubSpecUsers'] = request.sub_spec_users
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.unsub_spec_audio_users):
            query['UnsubSpecAudioUsers'] = request.unsub_spec_audio_users
        if not UtilClient.is_unset(request.unsub_spec_camera_users):
            query['UnsubSpecCameraUsers'] = request.unsub_spec_camera_users
        if not UtilClient.is_unset(request.unsub_spec_share_screen_users):
            query['UnsubSpecShareScreenUsers'] = request.unsub_spec_share_screen_users
        if not UtilClient.is_unset(request.user_panes):
            query['UserPanes'] = request.user_panes
        if not UtilClient.is_unset(request.watermarks):
            query['Watermarks'] = request.watermarks
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateMPUTask',
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
            rtc_20180111_models.UpdateMPUTaskResponse(),
            self.call_api(params, req, runtime)
        )

    def update_mputask(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_mputask_with_options(request, runtime)

    def update_record_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.crop_mode):
            query['CropMode'] = request.crop_mode
        if not UtilClient.is_unset(request.layout_ids):
            query['LayoutIds'] = request.layout_ids
        if not UtilClient.is_unset(request.media_encode):
            query['MediaEncode'] = request.media_encode
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.sub_spec_audio_users):
            query['SubSpecAudioUsers'] = request.sub_spec_audio_users
        if not UtilClient.is_unset(request.sub_spec_camera_users):
            query['SubSpecCameraUsers'] = request.sub_spec_camera_users
        if not UtilClient.is_unset(request.sub_spec_share_screen_users):
            query['SubSpecShareScreenUsers'] = request.sub_spec_share_screen_users
        if not UtilClient.is_unset(request.sub_spec_users):
            query['SubSpecUsers'] = request.sub_spec_users
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.task_profile):
            query['TaskProfile'] = request.task_profile
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        if not UtilClient.is_unset(request.unsub_spec_audio_users):
            query['UnsubSpecAudioUsers'] = request.unsub_spec_audio_users
        if not UtilClient.is_unset(request.unsub_spec_camera_users):
            query['UnsubSpecCameraUsers'] = request.unsub_spec_camera_users
        if not UtilClient.is_unset(request.unsub_spec_share_screen_users):
            query['UnsubSpecShareScreenUsers'] = request.unsub_spec_share_screen_users
        if not UtilClient.is_unset(request.user_panes):
            query['UserPanes'] = request.user_panes
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateRecordTask',
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
            rtc_20180111_models.UpdateRecordTaskResponse(),
            self.call_api(params, req, runtime)
        )

    def update_record_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_record_task_with_options(request, runtime)

    def update_record_template_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.background_color):
            query['BackgroundColor'] = request.background_color
        if not UtilClient.is_unset(request.backgrounds):
            query['Backgrounds'] = request.backgrounds
        if not UtilClient.is_unset(request.clock_widgets):
            query['ClockWidgets'] = request.clock_widgets
        if not UtilClient.is_unset(request.delay_stop_time):
            query['DelayStopTime'] = request.delay_stop_time
        if not UtilClient.is_unset(request.enable_m3u_8date_time):
            query['EnableM3u8DateTime'] = request.enable_m3u_8date_time
        if not UtilClient.is_unset(request.file_split_interval):
            query['FileSplitInterval'] = request.file_split_interval
        if not UtilClient.is_unset(request.formats):
            query['Formats'] = request.formats
        if not UtilClient.is_unset(request.http_callback_url):
            query['HttpCallbackUrl'] = request.http_callback_url
        if not UtilClient.is_unset(request.layout_ids):
            query['LayoutIds'] = request.layout_ids
        if not UtilClient.is_unset(request.media_encode):
            query['MediaEncode'] = request.media_encode
        if not UtilClient.is_unset(request.mns_queue):
            query['MnsQueue'] = request.mns_queue
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.oss_bucket):
            query['OssBucket'] = request.oss_bucket
        if not UtilClient.is_unset(request.oss_endpoint):
            query['OssEndpoint'] = request.oss_endpoint
        if not UtilClient.is_unset(request.oss_file_prefix):
            query['OssFilePrefix'] = request.oss_file_prefix
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.task_profile):
            query['TaskProfile'] = request.task_profile
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        if not UtilClient.is_unset(request.watermarks):
            query['Watermarks'] = request.watermarks
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateRecordTemplate',
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
            rtc_20180111_models.UpdateRecordTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    def update_record_template(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_record_template_with_options(request, runtime)
