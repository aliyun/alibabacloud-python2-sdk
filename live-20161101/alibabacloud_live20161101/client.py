# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_live20161101 import models as live_20161101_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_openapi_util.client import Client as OpenApiUtilClient


class Client(OpenApiClient):
    """
    *\
    """
    def __init__(self, config):
        super(Client, self).__init__(config)
        self._endpoint_rule = 'regional'
        self._endpoint_map = {
            'cn-qingdao': 'live.aliyuncs.com',
            'cn-beijing': 'live.aliyuncs.com',
            'cn-hangzhou': 'live.aliyuncs.com',
            'cn-shanghai': 'live.aliyuncs.com',
            'cn-shenzhen': 'live.aliyuncs.com',
            'ap-southeast-1': 'live.aliyuncs.com',
            'ap-southeast-5': 'live.aliyuncs.com',
            'ap-northeast-1': 'live.aliyuncs.com',
            'eu-central-1': 'live.aliyuncs.com',
            'ap-south-1': 'live.aliyuncs.com',
            'ap-northeast-2-pop': 'live.aliyuncs.com',
            'ap-southeast-2': 'live.aliyuncs.com',
            'ap-southeast-3': 'live.aliyuncs.com',
            'cn-beijing-finance-1': 'live.aliyuncs.com',
            'cn-beijing-finance-pop': 'live.aliyuncs.com',
            'cn-beijing-gov-1': 'live.aliyuncs.com',
            'cn-beijing-nu16-b01': 'live.aliyuncs.com',
            'cn-chengdu': 'live.aliyuncs.com',
            'cn-edge-1': 'live.aliyuncs.com',
            'cn-fujian': 'live.aliyuncs.com',
            'cn-haidian-cm12-c01': 'live.aliyuncs.com',
            'cn-hangzhou-bj-b01': 'live.aliyuncs.com',
            'cn-hangzhou-finance': 'live.aliyuncs.com',
            'cn-hangzhou-internal-prod-1': 'live.aliyuncs.com',
            'cn-hangzhou-internal-test-1': 'live.aliyuncs.com',
            'cn-hangzhou-internal-test-2': 'live.aliyuncs.com',
            'cn-hangzhou-internal-test-3': 'live.aliyuncs.com',
            'cn-hangzhou-test-306': 'live.aliyuncs.com',
            'cn-hongkong': 'live.aliyuncs.com',
            'cn-hongkong-finance-pop': 'live.aliyuncs.com',
            'cn-huhehaote': 'live.aliyuncs.com',
            'cn-huhehaote-nebula-1': 'live.aliyuncs.com',
            'cn-north-2-gov-1': 'live.aliyuncs.com',
            'cn-qingdao-nebula': 'live.aliyuncs.com',
            'cn-shanghai-et15-b01': 'live.aliyuncs.com',
            'cn-shanghai-et2-b01': 'live.aliyuncs.com',
            'cn-shanghai-finance-1': 'live.aliyuncs.com',
            'cn-shanghai-inner': 'live.aliyuncs.com',
            'cn-shanghai-internal-test-1': 'live.aliyuncs.com',
            'cn-shenzhen-finance-1': 'live.aliyuncs.com',
            'cn-shenzhen-inner': 'live.aliyuncs.com',
            'cn-shenzhen-st4-d01': 'live.aliyuncs.com',
            'cn-shenzhen-su18-b01': 'live.aliyuncs.com',
            'cn-wuhan': 'live.aliyuncs.com',
            'cn-wulanchabu': 'live.aliyuncs.com',
            'cn-yushanfang': 'live.aliyuncs.com',
            'cn-zhangbei': 'live.aliyuncs.com',
            'cn-zhangbei-na61-b01': 'live.aliyuncs.com',
            'cn-zhangjiakou': 'live.aliyuncs.com',
            'cn-zhangjiakou-na62-a01': 'live.aliyuncs.com',
            'cn-zhengzhou-nebula-1': 'live.aliyuncs.com',
            'eu-west-1': 'live.aliyuncs.com',
            'eu-west-1-oxs': 'live.aliyuncs.com',
            'me-east-1': 'live.aliyuncs.com',
            'rus-west-1-pop': 'live.aliyuncs.com',
            'us-east-1': 'live.aliyuncs.com',
            'us-west-1': 'live.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('live', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def add_caster_component_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.caption_layer_content):
            query['CaptionLayerContent'] = request.caption_layer_content
        if not UtilClient.is_unset(request.caster_id):
            query['CasterId'] = request.caster_id
        if not UtilClient.is_unset(request.component_layer):
            query['ComponentLayer'] = request.component_layer
        if not UtilClient.is_unset(request.component_name):
            query['ComponentName'] = request.component_name
        if not UtilClient.is_unset(request.component_type):
            query['ComponentType'] = request.component_type
        if not UtilClient.is_unset(request.effect):
            query['Effect'] = request.effect
        if not UtilClient.is_unset(request.html_layer_content):
            query['HtmlLayerContent'] = request.html_layer_content
        if not UtilClient.is_unset(request.image_layer_content):
            query['ImageLayerContent'] = request.image_layer_content
        if not UtilClient.is_unset(request.layer_order):
            query['LayerOrder'] = request.layer_order
        if not UtilClient.is_unset(request.location_id):
            query['LocationId'] = request.location_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.text_layer_content):
            query['TextLayerContent'] = request.text_layer_content
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddCasterComponent',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.AddCasterComponentResponse(),
            self.call_api(params, req, runtime)
        )

    def add_caster_component(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_caster_component_with_options(request, runtime)

    def add_caster_episode_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.caster_id):
            query['CasterId'] = request.caster_id
        if not UtilClient.is_unset(request.component_id):
            query['ComponentId'] = request.component_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.episode_name):
            query['EpisodeName'] = request.episode_name
        if not UtilClient.is_unset(request.episode_type):
            query['EpisodeType'] = request.episode_type
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.switch_type):
            query['SwitchType'] = request.switch_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddCasterEpisode',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.AddCasterEpisodeResponse(),
            self.call_api(params, req, runtime)
        )

    def add_caster_episode(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_caster_episode_with_options(request, runtime)

    def add_caster_episode_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.callback_url):
            query['CallbackUrl'] = request.callback_url
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.item):
            query['Item'] = request.item
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.repeat_num):
            query['RepeatNum'] = request.repeat_num
        if not UtilClient.is_unset(request.side_output_url):
            query['SideOutputUrl'] = request.side_output_url
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddCasterEpisodeGroup',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.AddCasterEpisodeGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def add_caster_episode_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_caster_episode_group_with_options(request, runtime)

    def add_caster_episode_group_content_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.content):
            query['Content'] = request.content
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddCasterEpisodeGroupContent',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.AddCasterEpisodeGroupContentResponse(),
            self.call_api(params, req, runtime)
        )

    def add_caster_episode_group_content(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_caster_episode_group_content_with_options(request, runtime)

    def add_caster_layout_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.audio_layer):
            query['AudioLayer'] = request.audio_layer
        if not UtilClient.is_unset(request.blend_list):
            query['BlendList'] = request.blend_list
        if not UtilClient.is_unset(request.caster_id):
            query['CasterId'] = request.caster_id
        if not UtilClient.is_unset(request.mix_list):
            query['MixList'] = request.mix_list
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.video_layer):
            query['VideoLayer'] = request.video_layer
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddCasterLayout',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.AddCasterLayoutResponse(),
            self.call_api(params, req, runtime)
        )

    def add_caster_layout(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_caster_layout_with_options(request, runtime)

    def add_caster_program_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.caster_id):
            query['CasterId'] = request.caster_id
        if not UtilClient.is_unset(request.episode):
            query['Episode'] = request.episode
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddCasterProgram',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.AddCasterProgramResponse(),
            self.call_api(params, req, runtime)
        )

    def add_caster_program(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_caster_program_with_options(request, runtime)

    def add_caster_video_resource_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.begin_offset):
            query['BeginOffset'] = request.begin_offset
        if not UtilClient.is_unset(request.caster_id):
            query['CasterId'] = request.caster_id
        if not UtilClient.is_unset(request.end_offset):
            query['EndOffset'] = request.end_offset
        if not UtilClient.is_unset(request.fixed_delay_duration):
            query['FixedDelayDuration'] = request.fixed_delay_duration
        if not UtilClient.is_unset(request.live_stream_url):
            query['LiveStreamUrl'] = request.live_stream_url
        if not UtilClient.is_unset(request.location_id):
            query['LocationId'] = request.location_id
        if not UtilClient.is_unset(request.material_id):
            query['MaterialId'] = request.material_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.pts_callback_interval):
            query['PtsCallbackInterval'] = request.pts_callback_interval
        if not UtilClient.is_unset(request.repeat_num):
            query['RepeatNum'] = request.repeat_num
        if not UtilClient.is_unset(request.resource_name):
            query['ResourceName'] = request.resource_name
        if not UtilClient.is_unset(request.stream_id):
            query['StreamId'] = request.stream_id
        if not UtilClient.is_unset(request.vod_url):
            query['VodUrl'] = request.vod_url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddCasterVideoResource',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.AddCasterVideoResourceResponse(),
            self.call_api(params, req, runtime)
        )

    def add_caster_video_resource(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_caster_video_resource_with_options(request, runtime)

    def add_custom_live_stream_transcode_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app):
            query['App'] = request.app
        if not UtilClient.is_unset(request.audio_bitrate):
            query['AudioBitrate'] = request.audio_bitrate
        if not UtilClient.is_unset(request.audio_channel_num):
            query['AudioChannelNum'] = request.audio_channel_num
        if not UtilClient.is_unset(request.audio_codec):
            query['AudioCodec'] = request.audio_codec
        if not UtilClient.is_unset(request.audio_profile):
            query['AudioProfile'] = request.audio_profile
        if not UtilClient.is_unset(request.audio_rate):
            query['AudioRate'] = request.audio_rate
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.encrypt_parameters):
            query['EncryptParameters'] = request.encrypt_parameters
        if not UtilClient.is_unset(request.fps):
            query['FPS'] = request.fps
        if not UtilClient.is_unset(request.gop):
            query['Gop'] = request.gop
        if not UtilClient.is_unset(request.height):
            query['Height'] = request.height
        if not UtilClient.is_unset(request.kms_key_expire_interval):
            query['KmsKeyExpireInterval'] = request.kms_key_expire_interval
        if not UtilClient.is_unset(request.kms_key_id):
            query['KmsKeyID'] = request.kms_key_id
        if not UtilClient.is_unset(request.kms_uid):
            query['KmsUID'] = request.kms_uid
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.profile):
            query['Profile'] = request.profile
        if not UtilClient.is_unset(request.template):
            query['Template'] = request.template
        if not UtilClient.is_unset(request.template_type):
            query['TemplateType'] = request.template_type
        if not UtilClient.is_unset(request.video_bitrate):
            query['VideoBitrate'] = request.video_bitrate
        if not UtilClient.is_unset(request.width):
            query['Width'] = request.width
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddCustomLiveStreamTranscode',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.AddCustomLiveStreamTranscodeResponse(),
            self.call_api(params, req, runtime)
        )

    def add_custom_live_stream_transcode(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_custom_live_stream_transcode_with_options(request, runtime)

    def add_live_app_record_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.on_demand):
            query['OnDemand'] = request.on_demand
        if not UtilClient.is_unset(request.oss_bucket):
            query['OssBucket'] = request.oss_bucket
        if not UtilClient.is_unset(request.oss_endpoint):
            query['OssEndpoint'] = request.oss_endpoint
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.record_format):
            query['RecordFormat'] = request.record_format
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.stream_name):
            query['StreamName'] = request.stream_name
        if not UtilClient.is_unset(request.transcode_record_format):
            query['TranscodeRecordFormat'] = request.transcode_record_format
        if not UtilClient.is_unset(request.transcode_templates):
            query['TranscodeTemplates'] = request.transcode_templates
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddLiveAppRecordConfig',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.AddLiveAppRecordConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def add_live_app_record_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_live_app_record_config_with_options(request, runtime)

    def add_live_app_snapshot_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.callback):
            query['Callback'] = request.callback
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.oss_bucket):
            query['OssBucket'] = request.oss_bucket
        if not UtilClient.is_unset(request.oss_endpoint):
            query['OssEndpoint'] = request.oss_endpoint
        if not UtilClient.is_unset(request.overwrite_oss_object):
            query['OverwriteOssObject'] = request.overwrite_oss_object
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.sequence_oss_object):
            query['SequenceOssObject'] = request.sequence_oss_object
        if not UtilClient.is_unset(request.time_interval):
            query['TimeInterval'] = request.time_interval
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddLiveAppSnapshotConfig',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.AddLiveAppSnapshotConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def add_live_app_snapshot_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_live_app_snapshot_config_with_options(request, runtime)

    def add_live_audio_audit_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.biz_type):
            query['BizType'] = request.biz_type
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.oss_bucket):
            query['OssBucket'] = request.oss_bucket
        if not UtilClient.is_unset(request.oss_endpoint):
            query['OssEndpoint'] = request.oss_endpoint
        if not UtilClient.is_unset(request.oss_object):
            query['OssObject'] = request.oss_object
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.stream_name):
            query['StreamName'] = request.stream_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddLiveAudioAuditConfig',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.AddLiveAudioAuditConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def add_live_audio_audit_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_live_audio_audit_config_with_options(request, runtime)

    def add_live_audio_audit_notify_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.callback):
            query['Callback'] = request.callback
        if not UtilClient.is_unset(request.callback_template):
            query['CallbackTemplate'] = request.callback_template
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddLiveAudioAuditNotifyConfig',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.AddLiveAudioAuditNotifyConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def add_live_audio_audit_notify_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_live_audio_audit_notify_config_with_options(request, runtime)

    def add_live_detect_notify_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.notify_url):
            query['NotifyUrl'] = request.notify_url
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddLiveDetectNotifyConfig',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.AddLiveDetectNotifyConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def add_live_detect_notify_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_live_detect_notify_config_with_options(request, runtime)

    def add_live_domain_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.check_url):
            query['CheckUrl'] = request.check_url
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.live_domain_type):
            query['LiveDomainType'] = request.live_domain_type
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        if not UtilClient.is_unset(request.scope):
            query['Scope'] = request.scope
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.top_level_domain):
            query['TopLevelDomain'] = request.top_level_domain
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddLiveDomain',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.AddLiveDomainResponse(),
            self.call_api(params, req, runtime)
        )

    def add_live_domain(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_live_domain_with_options(request, runtime)

    def add_live_domain_mapping_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.pull_domain):
            query['PullDomain'] = request.pull_domain
        if not UtilClient.is_unset(request.push_domain):
            query['PushDomain'] = request.push_domain
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddLiveDomainMapping',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.AddLiveDomainMappingResponse(),
            self.call_api(params, req, runtime)
        )

    def add_live_domain_mapping(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_live_domain_mapping_with_options(request, runtime)

    def add_live_domain_play_mapping_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.play_domain):
            query['PlayDomain'] = request.play_domain
        if not UtilClient.is_unset(request.pull_domain):
            query['PullDomain'] = request.pull_domain
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddLiveDomainPlayMapping',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.AddLiveDomainPlayMappingResponse(),
            self.call_api(params, req, runtime)
        )

    def add_live_domain_play_mapping(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_live_domain_play_mapping_with_options(request, runtime)

    def add_live_pull_stream_info_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.source_url):
            query['SourceUrl'] = request.source_url
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.stream_name):
            query['StreamName'] = request.stream_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddLivePullStreamInfoConfig',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.AddLivePullStreamInfoConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def add_live_pull_stream_info_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_live_pull_stream_info_config_with_options(request, runtime)

    def add_live_record_notify_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.need_status_notify):
            query['NeedStatusNotify'] = request.need_status_notify
        if not UtilClient.is_unset(request.notify_url):
            query['NotifyUrl'] = request.notify_url
        if not UtilClient.is_unset(request.on_demand_url):
            query['OnDemandUrl'] = request.on_demand_url
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddLiveRecordNotifyConfig',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.AddLiveRecordNotifyConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def add_live_record_notify_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_live_record_notify_config_with_options(request, runtime)

    def add_live_record_vod_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.auto_compose):
            query['AutoCompose'] = request.auto_compose
        if not UtilClient.is_unset(request.compose_vod_transcode_group_id):
            query['ComposeVodTranscodeGroupId'] = request.compose_vod_transcode_group_id
        if not UtilClient.is_unset(request.cycle_duration):
            query['CycleDuration'] = request.cycle_duration
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.storage_location):
            query['StorageLocation'] = request.storage_location
        if not UtilClient.is_unset(request.stream_name):
            query['StreamName'] = request.stream_name
        if not UtilClient.is_unset(request.vod_transcode_group_id):
            query['VodTranscodeGroupId'] = request.vod_transcode_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddLiveRecordVodConfig',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.AddLiveRecordVodConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def add_live_record_vod_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_live_record_vod_config_with_options(request, runtime)

    def add_live_snapshot_detect_porn_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.oss_bucket):
            query['OssBucket'] = request.oss_bucket
        if not UtilClient.is_unset(request.oss_endpoint):
            query['OssEndpoint'] = request.oss_endpoint
        if not UtilClient.is_unset(request.oss_object):
            query['OssObject'] = request.oss_object
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.scene):
            query['Scene'] = request.scene
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddLiveSnapshotDetectPornConfig',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.AddLiveSnapshotDetectPornConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def add_live_snapshot_detect_porn_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_live_snapshot_detect_porn_config_with_options(request, runtime)

    def add_live_stream_transcode_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app):
            query['App'] = request.app
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.encrypt_parameters):
            query['EncryptParameters'] = request.encrypt_parameters
        if not UtilClient.is_unset(request.lazy):
            query['Lazy'] = request.lazy
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.template):
            query['Template'] = request.template
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddLiveStreamTranscode',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.AddLiveStreamTranscodeResponse(),
            self.call_api(params, req, runtime)
        )

    def add_live_stream_transcode(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_live_stream_transcode_with_options(request, runtime)

    def add_live_stream_watermark_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.height):
            query['Height'] = request.height
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.offset_corner):
            query['OffsetCorner'] = request.offset_corner
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.picture_url):
            query['PictureUrl'] = request.picture_url
        if not UtilClient.is_unset(request.ref_height):
            query['RefHeight'] = request.ref_height
        if not UtilClient.is_unset(request.ref_width):
            query['RefWidth'] = request.ref_width
        if not UtilClient.is_unset(request.transparency):
            query['Transparency'] = request.transparency
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        if not UtilClient.is_unset(request.xoffset):
            query['XOffset'] = request.xoffset
        if not UtilClient.is_unset(request.yoffset):
            query['YOffset'] = request.yoffset
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddLiveStreamWatermark',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.AddLiveStreamWatermarkResponse(),
            self.call_api(params, req, runtime)
        )

    def add_live_stream_watermark(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_live_stream_watermark_with_options(request, runtime)

    def add_live_stream_watermark_rule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app):
            query['App'] = request.app
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.stream):
            query['Stream'] = request.stream
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddLiveStreamWatermarkRule',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.AddLiveStreamWatermarkRuleResponse(),
            self.call_api(params, req, runtime)
        )

    def add_live_stream_watermark_rule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_live_stream_watermark_rule_with_options(request, runtime)

    def add_multi_rate_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app):
            query['App'] = request.app
        if not UtilClient.is_unset(request.av_format):
            query['AvFormat'] = request.av_format
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.is_lazy):
            query['IsLazy'] = request.is_lazy
        if not UtilClient.is_unset(request.is_time_align):
            query['IsTimeAlign'] = request.is_time_align
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.templates):
            query['Templates'] = request.templates
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddMultiRateConfig',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.AddMultiRateConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def add_multi_rate_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_multi_rate_config_with_options(request, runtime)

    def add_playlist_items_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.caster_id):
            query['CasterId'] = request.caster_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.program_config):
            query['ProgramConfig'] = request.program_config
        if not UtilClient.is_unset(request.program_id):
            query['ProgramId'] = request.program_id
        if not UtilClient.is_unset(request.program_items):
            query['ProgramItems'] = request.program_items
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddPlaylistItems',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.AddPlaylistItemsResponse(),
            self.call_api(params, req, runtime)
        )

    def add_playlist_items(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_playlist_items_with_options(request, runtime)

    def add_rts_live_stream_transcode_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app):
            query['App'] = request.app
        if not UtilClient.is_unset(request.audio_bitrate):
            query['AudioBitrate'] = request.audio_bitrate
        if not UtilClient.is_unset(request.audio_channel_num):
            query['AudioChannelNum'] = request.audio_channel_num
        if not UtilClient.is_unset(request.audio_codec):
            query['AudioCodec'] = request.audio_codec
        if not UtilClient.is_unset(request.audio_profile):
            query['AudioProfile'] = request.audio_profile
        if not UtilClient.is_unset(request.audio_rate):
            query['AudioRate'] = request.audio_rate
        if not UtilClient.is_unset(request.delete_bframes):
            query['DeleteBframes'] = request.delete_bframes
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.fps):
            query['FPS'] = request.fps
        if not UtilClient.is_unset(request.gop):
            query['Gop'] = request.gop
        if not UtilClient.is_unset(request.height):
            query['Height'] = request.height
        if not UtilClient.is_unset(request.lazy):
            query['Lazy'] = request.lazy
        if not UtilClient.is_unset(request.opus):
            query['Opus'] = request.opus
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.profile):
            query['Profile'] = request.profile
        if not UtilClient.is_unset(request.template):
            query['Template'] = request.template
        if not UtilClient.is_unset(request.template_type):
            query['TemplateType'] = request.template_type
        if not UtilClient.is_unset(request.video_bitrate):
            query['VideoBitrate'] = request.video_bitrate
        if not UtilClient.is_unset(request.width):
            query['Width'] = request.width
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddRtsLiveStreamTranscode',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.AddRtsLiveStreamTranscodeResponse(),
            self.call_api(params, req, runtime)
        )

    def add_rts_live_stream_transcode(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_rts_live_stream_transcode_with_options(request, runtime)

    def add_show_into_show_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.caster_id):
            query['CasterId'] = request.caster_id
        if not UtilClient.is_unset(request.duration):
            query['Duration'] = request.duration
        if not UtilClient.is_unset(request.live_input_type):
            query['LiveInputType'] = request.live_input_type
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.repeat_times):
            query['RepeatTimes'] = request.repeat_times
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.resource_url):
            query['ResourceUrl'] = request.resource_url
        if not UtilClient.is_unset(request.show_name):
            query['ShowName'] = request.show_name
        if not UtilClient.is_unset(request.spot):
            query['Spot'] = request.spot
        if not UtilClient.is_unset(request.is_batch_mode):
            query['isBatchMode'] = request.is_batch_mode
        if not UtilClient.is_unset(request.show_list):
            query['showList'] = request.show_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddShowIntoShowList',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.AddShowIntoShowListResponse(),
            self.call_api(params, req, runtime)
        )

    def add_show_into_show_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_show_into_show_list_with_options(request, runtime)

    def add_studio_layout_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bg_image_config):
            query['BgImageConfig'] = request.bg_image_config
        if not UtilClient.is_unset(request.caster_id):
            query['CasterId'] = request.caster_id
        if not UtilClient.is_unset(request.common_config):
            query['CommonConfig'] = request.common_config
        if not UtilClient.is_unset(request.layer_order_config_list):
            query['LayerOrderConfigList'] = request.layer_order_config_list
        if not UtilClient.is_unset(request.layout_name):
            query['LayoutName'] = request.layout_name
        if not UtilClient.is_unset(request.layout_type):
            query['LayoutType'] = request.layout_type
        if not UtilClient.is_unset(request.media_input_config_list):
            query['MediaInputConfigList'] = request.media_input_config_list
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.screen_input_config_list):
            query['ScreenInputConfigList'] = request.screen_input_config_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddStudioLayout',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.AddStudioLayoutResponse(),
            self.call_api(params, req, runtime)
        )

    def add_studio_layout(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_studio_layout_with_options(request, runtime)

    def add_trancode_seiwith_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.delay):
            query['Delay'] = request.delay
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.pattern):
            query['Pattern'] = request.pattern
        if not UtilClient.is_unset(request.repeat):
            query['Repeat'] = request.repeat
        if not UtilClient.is_unset(request.stream_name):
            query['StreamName'] = request.stream_name
        if not UtilClient.is_unset(request.text):
            query['Text'] = request.text
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddTrancodeSEI',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.AddTrancodeSEIResponse(),
            self.call_api(params, req, runtime)
        )

    def add_trancode_sei(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_trancode_seiwith_options(request, runtime)

    def allow_push_stream_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.room_id):
            query['RoomId'] = request.room_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AllowPushStream',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.AllowPushStreamResponse(),
            self.call_api(params, req, runtime)
        )

    def allow_push_stream(self, request):
        runtime = util_models.RuntimeOptions()
        return self.allow_push_stream_with_options(request, runtime)

    def batch_delete_live_domain_configs_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_names):
            query['DomainNames'] = request.domain_names
        if not UtilClient.is_unset(request.function_names):
            query['FunctionNames'] = request.function_names
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BatchDeleteLiveDomainConfigs',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.BatchDeleteLiveDomainConfigsResponse(),
            self.call_api(params, req, runtime)
        )

    def batch_delete_live_domain_configs(self, request):
        runtime = util_models.RuntimeOptions()
        return self.batch_delete_live_domain_configs_with_options(request, runtime)

    def batch_set_live_domain_configs_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_names):
            query['DomainNames'] = request.domain_names
        if not UtilClient.is_unset(request.functions):
            query['Functions'] = request.functions
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BatchSetLiveDomainConfigs',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.BatchSetLiveDomainConfigsResponse(),
            self.call_api(params, req, runtime)
        )

    def batch_set_live_domain_configs(self, request):
        runtime = util_models.RuntimeOptions()
        return self.batch_set_live_domain_configs_with_options(request, runtime)

    def cancel_mute_all_group_user_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.group_id):
            body['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.operator_user_id):
            body['OperatorUserId'] = request.operator_user_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CancelMuteAllGroupUser',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.CancelMuteAllGroupUserResponse(),
            self.call_api(params, req, runtime)
        )

    def cancel_mute_all_group_user(self, request):
        runtime = util_models.RuntimeOptions()
        return self.cancel_mute_all_group_user_with_options(request, runtime)

    def close_live_shift_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.stream_name):
            query['StreamName'] = request.stream_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CloseLiveShift',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.CloseLiveShiftResponse(),
            self.call_api(params, req, runtime)
        )

    def close_live_shift(self, request):
        runtime = util_models.RuntimeOptions()
        return self.close_live_shift_with_options(request, runtime)

    def close_message_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.group_id):
            body['GroupId'] = request.group_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CloseMessageGroup',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.CloseMessageGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def close_message_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.close_message_group_with_options(request, runtime)

    def copy_caster_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.caster_name):
            query['CasterName'] = request.caster_name
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.src_caster_id):
            query['SrcCasterId'] = request.src_caster_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CopyCaster',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.CopyCasterResponse(),
            self.call_api(params, req, runtime)
        )

    def copy_caster(self, request):
        runtime = util_models.RuntimeOptions()
        return self.copy_caster_with_options(request, runtime)

    def copy_caster_scene_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.caster_id):
            query['CasterId'] = request.caster_id
        if not UtilClient.is_unset(request.from_scene_id):
            query['FromSceneId'] = request.from_scene_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.to_scene_id):
            query['ToSceneId'] = request.to_scene_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CopyCasterSceneConfig',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.CopyCasterSceneConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def copy_caster_scene_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.copy_caster_scene_config_with_options(request, runtime)

    def create_caster_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.caster_name):
            query['CasterName'] = request.caster_name
        if not UtilClient.is_unset(request.caster_template):
            query['CasterTemplate'] = request.caster_template
        if not UtilClient.is_unset(request.charge_type):
            query['ChargeType'] = request.charge_type
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.expire_time):
            query['ExpireTime'] = request.expire_time
        if not UtilClient.is_unset(request.norm_type):
            query['NormType'] = request.norm_type
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.purchase_time):
            query['PurchaseTime'] = request.purchase_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateCaster',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.CreateCasterResponse(),
            self.call_api(params, req, runtime)
        )

    def create_caster(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_caster_with_options(request, runtime)

    def create_custom_template_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.custom_template):
            query['CustomTemplate'] = request.custom_template
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.template):
            query['Template'] = request.template
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateCustomTemplate',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.CreateCustomTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    def create_custom_template(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_custom_template_with_options(request, runtime)

    def create_live_real_time_log_delivery_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateLiveRealTimeLogDelivery',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.CreateLiveRealTimeLogDeliveryResponse(),
            self.call_api(params, req, runtime)
        )

    def create_live_real_time_log_delivery(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_live_real_time_log_delivery_with_options(request, runtime)

    def create_live_stream_monitor_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app):
            query['App'] = request.app
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.input_list):
            query['InputList'] = request.input_list
        if not UtilClient.is_unset(request.monitor_name):
            query['MonitorName'] = request.monitor_name
        if not UtilClient.is_unset(request.output_template):
            query['OutputTemplate'] = request.output_template
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.stream):
            query['Stream'] = request.stream
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateLiveStreamMonitor',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.CreateLiveStreamMonitorResponse(),
            self.call_api(params, req, runtime)
        )

    def create_live_stream_monitor(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_live_stream_monitor_with_options(request, runtime)

    def create_live_stream_record_index_files_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.oss_bucket):
            query['OssBucket'] = request.oss_bucket
        if not UtilClient.is_unset(request.oss_endpoint):
            query['OssEndpoint'] = request.oss_endpoint
        if not UtilClient.is_unset(request.oss_object):
            query['OssObject'] = request.oss_object
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.stream_name):
            query['StreamName'] = request.stream_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateLiveStreamRecordIndexFiles',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.CreateLiveStreamRecordIndexFilesResponse(),
            self.call_api(params, req, runtime)
        )

    def create_live_stream_record_index_files(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_live_stream_record_index_files_with_options(request, runtime)

    def create_live_transcode_template_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.template_config):
            query['TemplateConfig'] = request.template_config
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateLiveTranscodeTemplate',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.CreateLiveTranscodeTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    def create_live_transcode_template(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_live_transcode_template_with_options(request, runtime)

    def create_message_group_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = live_20161101_models.CreateMessageGroupShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.extension):
            request.extension_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.extension, 'Extension', 'json')
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.creator_id):
            body['CreatorId'] = request.creator_id
        if not UtilClient.is_unset(request.extension_shrink):
            body['Extension'] = request.extension_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateMessageGroup',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.CreateMessageGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def create_message_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_message_group_with_options(request, runtime)

    def create_mix_stream_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.callback_config):
            query['CallbackConfig'] = request.callback_config
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.input_stream_list):
            query['InputStreamList'] = request.input_stream_list
        if not UtilClient.is_unset(request.layout_id):
            query['LayoutId'] = request.layout_id
        if not UtilClient.is_unset(request.output_config):
            query['OutputConfig'] = request.output_config
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateMixStream',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.CreateMixStreamResponse(),
            self.call_api(params, req, runtime)
        )

    def create_mix_stream(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_mix_stream_with_options(request, runtime)

    def delete_caster_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.caster_id):
            query['CasterId'] = request.caster_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteCaster',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DeleteCasterResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_caster(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_caster_with_options(request, runtime)

    def delete_caster_component_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.caster_id):
            query['CasterId'] = request.caster_id
        if not UtilClient.is_unset(request.component_id):
            query['ComponentId'] = request.component_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteCasterComponent',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DeleteCasterComponentResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_caster_component(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_caster_component_with_options(request, runtime)

    def delete_caster_episode_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.caster_id):
            query['CasterId'] = request.caster_id
        if not UtilClient.is_unset(request.episode_id):
            query['EpisodeId'] = request.episode_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteCasterEpisode',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DeleteCasterEpisodeResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_caster_episode(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_caster_episode_with_options(request, runtime)

    def delete_caster_episode_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.program_id):
            query['ProgramId'] = request.program_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteCasterEpisodeGroup',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DeleteCasterEpisodeGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_caster_episode_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_caster_episode_group_with_options(request, runtime)

    def delete_caster_layout_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.caster_id):
            query['CasterId'] = request.caster_id
        if not UtilClient.is_unset(request.layout_id):
            query['LayoutId'] = request.layout_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteCasterLayout',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DeleteCasterLayoutResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_caster_layout(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_caster_layout_with_options(request, runtime)

    def delete_caster_program_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.caster_id):
            query['CasterId'] = request.caster_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteCasterProgram',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DeleteCasterProgramResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_caster_program(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_caster_program_with_options(request, runtime)

    def delete_caster_scene_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.caster_id):
            query['CasterId'] = request.caster_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.scene_id):
            query['SceneId'] = request.scene_id
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteCasterSceneConfig',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DeleteCasterSceneConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_caster_scene_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_caster_scene_config_with_options(request, runtime)

    def delete_caster_video_resource_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.caster_id):
            query['CasterId'] = request.caster_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteCasterVideoResource',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DeleteCasterVideoResourceResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_caster_video_resource(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_caster_video_resource_with_options(request, runtime)

    def delete_custom_template_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.template):
            query['Template'] = request.template
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteCustomTemplate',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DeleteCustomTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_custom_template(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_custom_template_with_options(request, runtime)

    def delete_live_app_record_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.stream_name):
            query['StreamName'] = request.stream_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteLiveAppRecordConfig',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DeleteLiveAppRecordConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_live_app_record_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_live_app_record_config_with_options(request, runtime)

    def delete_live_app_snapshot_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteLiveAppSnapshotConfig',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DeleteLiveAppSnapshotConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_live_app_snapshot_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_live_app_snapshot_config_with_options(request, runtime)

    def delete_live_audio_audit_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.stream_name):
            query['StreamName'] = request.stream_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteLiveAudioAuditConfig',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DeleteLiveAudioAuditConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_live_audio_audit_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_live_audio_audit_config_with_options(request, runtime)

    def delete_live_audio_audit_notify_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteLiveAudioAuditNotifyConfig',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DeleteLiveAudioAuditNotifyConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_live_audio_audit_notify_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_live_audio_audit_notify_config_with_options(request, runtime)

    def delete_live_detect_notify_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteLiveDetectNotifyConfig',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DeleteLiveDetectNotifyConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_live_detect_notify_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_live_detect_notify_config_with_options(request, runtime)

    def delete_live_domain_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteLiveDomain',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DeleteLiveDomainResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_live_domain(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_live_domain_with_options(request, runtime)

    def delete_live_domain_mapping_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.pull_domain):
            query['PullDomain'] = request.pull_domain
        if not UtilClient.is_unset(request.push_domain):
            query['PushDomain'] = request.push_domain
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteLiveDomainMapping',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DeleteLiveDomainMappingResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_live_domain_mapping(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_live_domain_mapping_with_options(request, runtime)

    def delete_live_domain_play_mapping_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.play_domain):
            query['PlayDomain'] = request.play_domain
        if not UtilClient.is_unset(request.pull_domain):
            query['PullDomain'] = request.pull_domain
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteLiveDomainPlayMapping',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DeleteLiveDomainPlayMappingResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_live_domain_play_mapping(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_live_domain_play_mapping_with_options(request, runtime)

    def delete_live_edge_transfer_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteLiveEdgeTransfer',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DeleteLiveEdgeTransferResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_live_edge_transfer(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_live_edge_transfer_with_options(request, runtime)

    def delete_live_lazy_pull_stream_info_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteLiveLazyPullStreamInfoConfig',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DeleteLiveLazyPullStreamInfoConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_live_lazy_pull_stream_info_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_live_lazy_pull_stream_info_config_with_options(request, runtime)

    def delete_live_pull_stream_info_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.stream_name):
            query['StreamName'] = request.stream_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteLivePullStreamInfoConfig',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DeleteLivePullStreamInfoConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_live_pull_stream_info_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_live_pull_stream_info_config_with_options(request, runtime)

    def delete_live_real_time_log_logstore_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteLiveRealTimeLogLogstore',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DeleteLiveRealTimeLogLogstoreResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_live_real_time_log_logstore(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_live_real_time_log_logstore_with_options(request, runtime)

    def delete_live_realtime_log_delivery_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteLiveRealtimeLogDelivery',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DeleteLiveRealtimeLogDeliveryResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_live_realtime_log_delivery(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_live_realtime_log_delivery_with_options(request, runtime)

    def delete_live_record_notify_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteLiveRecordNotifyConfig',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DeleteLiveRecordNotifyConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_live_record_notify_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_live_record_notify_config_with_options(request, runtime)

    def delete_live_record_vod_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.stream_name):
            query['StreamName'] = request.stream_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteLiveRecordVodConfig',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DeleteLiveRecordVodConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_live_record_vod_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_live_record_vod_config_with_options(request, runtime)

    def delete_live_snapshot_detect_porn_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteLiveSnapshotDetectPornConfig',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DeleteLiveSnapshotDetectPornConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_live_snapshot_detect_porn_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_live_snapshot_detect_porn_config_with_options(request, runtime)

    def delete_live_specific_staging_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.config_id):
            query['ConfigId'] = request.config_id
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteLiveSpecificStagingConfig',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DeleteLiveSpecificStagingConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_live_specific_staging_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_live_specific_staging_config_with_options(request, runtime)

    def delete_live_stream_monitor_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.monitor_id):
            query['MonitorId'] = request.monitor_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteLiveStreamMonitor',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DeleteLiveStreamMonitorResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_live_stream_monitor(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_live_stream_monitor_with_options(request, runtime)

    def delete_live_stream_record_index_files_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.record_id):
            query['RecordId'] = request.record_id
        if not UtilClient.is_unset(request.remove_file):
            query['RemoveFile'] = request.remove_file
        if not UtilClient.is_unset(request.stream_name):
            query['StreamName'] = request.stream_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteLiveStreamRecordIndexFiles',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DeleteLiveStreamRecordIndexFilesResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_live_stream_record_index_files(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_live_stream_record_index_files_with_options(request, runtime)

    def delete_live_stream_transcode_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app):
            query['App'] = request.app
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.template):
            query['Template'] = request.template
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteLiveStreamTranscode',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DeleteLiveStreamTranscodeResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_live_stream_transcode(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_live_stream_transcode_with_options(request, runtime)

    def delete_live_stream_watermark_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteLiveStreamWatermark',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DeleteLiveStreamWatermarkResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_live_stream_watermark(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_live_stream_watermark_with_options(request, runtime)

    def delete_live_stream_watermark_rule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app):
            query['App'] = request.app
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.rule_id):
            query['RuleId'] = request.rule_id
        if not UtilClient.is_unset(request.stream):
            query['Stream'] = request.stream
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteLiveStreamWatermarkRule',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DeleteLiveStreamWatermarkRuleResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_live_stream_watermark_rule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_live_stream_watermark_rule_with_options(request, runtime)

    def delete_live_streams_notify_url_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteLiveStreamsNotifyUrlConfig',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DeleteLiveStreamsNotifyUrlConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_live_streams_notify_url_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_live_streams_notify_url_config_with_options(request, runtime)

    def delete_message_app_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteMessageApp',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DeleteMessageAppResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_message_app(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_message_app_with_options(request, runtime)

    def delete_mix_stream_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.mix_stream_id):
            query['MixStreamId'] = request.mix_stream_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.stream_name):
            query['StreamName'] = request.stream_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteMixStream',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DeleteMixStreamResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_mix_stream(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_mix_stream_with_options(request, runtime)

    def delete_multi_rate_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app):
            query['App'] = request.app
        if not UtilClient.is_unset(request.delete_all):
            query['DeleteAll'] = request.delete_all
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.templates):
            query['Templates'] = request.templates
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteMultiRateConfig',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DeleteMultiRateConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_multi_rate_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_multi_rate_config_with_options(request, runtime)

    def delete_playlist_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.program_id):
            query['ProgramId'] = request.program_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeletePlaylist',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DeletePlaylistResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_playlist(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_playlist_with_options(request, runtime)

    def delete_playlist_items_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.program_id):
            query['ProgramId'] = request.program_id
        if not UtilClient.is_unset(request.program_item_ids):
            query['ProgramItemIds'] = request.program_item_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeletePlaylistItems',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DeletePlaylistItemsResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_playlist_items(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_playlist_items_with_options(request, runtime)

    def delete_room_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.room_id):
            query['RoomId'] = request.room_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteRoom',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DeleteRoomResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_room(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_room_with_options(request, runtime)

    def delete_snapshot_callback_auth_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteSnapshotCallbackAuth',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DeleteSnapshotCallbackAuthResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_snapshot_callback_auth(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_snapshot_callback_auth_with_options(request, runtime)

    def delete_snapshot_files_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.create_timestamp_list):
            query['CreateTimestampList'] = request.create_timestamp_list
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.remove_file):
            query['RemoveFile'] = request.remove_file
        if not UtilClient.is_unset(request.stream_name):
            query['StreamName'] = request.stream_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteSnapshotFiles',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DeleteSnapshotFilesResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_snapshot_files(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_snapshot_files_with_options(request, runtime)

    def delete_studio_layout_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.caster_id):
            query['CasterId'] = request.caster_id
        if not UtilClient.is_unset(request.layout_id):
            query['LayoutId'] = request.layout_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteStudioLayout',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DeleteStudioLayoutResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_studio_layout(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_studio_layout_with_options(request, runtime)

    def describe_auto_show_list_tasks_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.caster_id):
            query['CasterId'] = request.caster_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAutoShowListTasks',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeAutoShowListTasksResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_auto_show_list_tasks(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_auto_show_list_tasks_with_options(request, runtime)

    def describe_caster_channels_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.caster_id):
            query['CasterId'] = request.caster_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCasterChannels',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeCasterChannelsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_caster_channels(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_caster_channels_with_options(request, runtime)

    def describe_caster_components_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.caster_id):
            query['CasterId'] = request.caster_id
        if not UtilClient.is_unset(request.component_id):
            query['ComponentId'] = request.component_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCasterComponents',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeCasterComponentsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_caster_components(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_caster_components_with_options(request, runtime)

    def describe_caster_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.caster_id):
            query['CasterId'] = request.caster_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCasterConfig',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeCasterConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_caster_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_caster_config_with_options(request, runtime)

    def describe_caster_layouts_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.caster_id):
            query['CasterId'] = request.caster_id
        if not UtilClient.is_unset(request.layout_id):
            query['LayoutId'] = request.layout_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCasterLayouts',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeCasterLayoutsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_caster_layouts(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_caster_layouts_with_options(request, runtime)

    def describe_caster_program_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.caster_id):
            query['CasterId'] = request.caster_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.episode_id):
            query['EpisodeId'] = request.episode_id
        if not UtilClient.is_unset(request.episode_type):
            query['EpisodeType'] = request.episode_type
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCasterProgram',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeCasterProgramResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_caster_program(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_caster_program_with_options(request, runtime)

    def describe_caster_scene_audio_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.caster_id):
            query['CasterId'] = request.caster_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.scene_id):
            query['SceneId'] = request.scene_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCasterSceneAudio',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeCasterSceneAudioResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_caster_scene_audio(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_caster_scene_audio_with_options(request, runtime)

    def describe_caster_scenes_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.caster_id):
            query['CasterId'] = request.caster_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.scene_id):
            query['SceneId'] = request.scene_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCasterScenes',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeCasterScenesResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_caster_scenes(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_caster_scenes_with_options(request, runtime)

    def describe_caster_stream_url_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.caster_id):
            query['CasterId'] = request.caster_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCasterStreamUrl',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeCasterStreamUrlResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_caster_stream_url(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_caster_stream_url_with_options(request, runtime)

    def describe_caster_sync_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.caster_id):
            query['CasterId'] = request.caster_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCasterSyncGroup',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeCasterSyncGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_caster_sync_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_caster_sync_group_with_options(request, runtime)

    def describe_caster_video_resources_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.caster_id):
            query['CasterId'] = request.caster_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCasterVideoResources',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeCasterVideoResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_caster_video_resources(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_caster_video_resources_with_options(request, runtime)

    def describe_casters_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.caster_id):
            query['CasterId'] = request.caster_id
        if not UtilClient.is_unset(request.caster_name):
            query['CasterName'] = request.caster_name
        if not UtilClient.is_unset(request.charge_type):
            query['ChargeType'] = request.charge_type
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.norm_type):
            query['NormType'] = request.norm_type
        if not UtilClient.is_unset(request.order_by_modify_asc):
            query['OrderByModifyAsc'] = request.order_by_modify_asc
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCasters',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeCastersResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_casters(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_casters_with_options(request, runtime)

    def describe_domain_usage_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.area):
            query['Area'] = request.area
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.field):
            query['Field'] = request.field
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDomainUsageData',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeDomainUsageDataResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_domain_usage_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_usage_data_with_options(request, runtime)

    def describe_domain_with_integrity_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDomainWithIntegrity',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeDomainWithIntegrityResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_domain_with_integrity(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_with_integrity_with_options(request, runtime)

    def describe_forbid_push_stream_room_list_with_options(self, request, runtime):
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
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeForbidPushStreamRoomList',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeForbidPushStreamRoomListResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_forbid_push_stream_room_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_forbid_push_stream_room_list_with_options(request, runtime)

    def describe_hls_live_stream_real_time_bps_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeHlsLiveStreamRealTimeBpsData',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeHlsLiveStreamRealTimeBpsDataResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_hls_live_stream_real_time_bps_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_hls_live_stream_real_time_bps_data_with_options(request, runtime)

    def describe_live_audio_audit_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.stream_name):
            query['StreamName'] = request.stream_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLiveAudioAuditConfig',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveAudioAuditConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_live_audio_audit_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_live_audio_audit_config_with_options(request, runtime)

    def describe_live_audio_audit_notify_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLiveAudioAuditNotifyConfig',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveAudioAuditNotifyConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_live_audio_audit_notify_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_live_audio_audit_notify_config_with_options(request, runtime)

    def describe_live_certificate_detail_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cert_name):
            query['CertName'] = request.cert_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLiveCertificateDetail',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveCertificateDetailResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_live_certificate_detail(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_live_certificate_detail_with_options(request, runtime)

    def describe_live_certificate_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLiveCertificateList',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveCertificateListResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_live_certificate_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_live_certificate_list_with_options(request, runtime)

    def describe_live_detect_notify_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLiveDetectNotifyConfig',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveDetectNotifyConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_live_detect_notify_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_live_detect_notify_config_with_options(request, runtime)

    def describe_live_detect_porn_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app):
            query['App'] = request.app
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.fee):
            query['Fee'] = request.fee
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        if not UtilClient.is_unset(request.scene):
            query['Scene'] = request.scene
        if not UtilClient.is_unset(request.split_by):
            query['SplitBy'] = request.split_by
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.stream):
            query['Stream'] = request.stream
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLiveDetectPornData',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveDetectPornDataResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_live_detect_porn_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_live_detect_porn_data_with_options(request, runtime)

    def describe_live_domain_bps_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.isp_name_en):
            query['IspNameEn'] = request.isp_name_en
        if not UtilClient.is_unset(request.location_name_en):
            query['LocationNameEn'] = request.location_name_en
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLiveDomainBpsData',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveDomainBpsDataResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_live_domain_bps_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_live_domain_bps_data_with_options(request, runtime)

    def describe_live_domain_bps_data_by_layer_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.isp_name_en):
            query['IspNameEn'] = request.isp_name_en
        if not UtilClient.is_unset(request.layer):
            query['Layer'] = request.layer
        if not UtilClient.is_unset(request.location_name_en):
            query['LocationNameEn'] = request.location_name_en
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLiveDomainBpsDataByLayer',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveDomainBpsDataByLayerResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_live_domain_bps_data_by_layer(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_live_domain_bps_data_by_layer_with_options(request, runtime)

    def describe_live_domain_bps_data_by_time_stamp_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.isp_names):
            query['IspNames'] = request.isp_names
        if not UtilClient.is_unset(request.location_names):
            query['LocationNames'] = request.location_names
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.time_point):
            query['TimePoint'] = request.time_point
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLiveDomainBpsDataByTimeStamp',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveDomainBpsDataByTimeStampResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_live_domain_bps_data_by_time_stamp(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_live_domain_bps_data_by_time_stamp_with_options(request, runtime)

    def describe_live_domain_certificate_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLiveDomainCertificateInfo',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveDomainCertificateInfoResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_live_domain_certificate_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_live_domain_certificate_info_with_options(request, runtime)

    def describe_live_domain_configs_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.function_names):
            query['FunctionNames'] = request.function_names
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLiveDomainConfigs',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveDomainConfigsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_live_domain_configs(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_live_domain_configs_with_options(request, runtime)

    def describe_live_domain_detail_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLiveDomainDetail',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveDomainDetailResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_live_domain_detail(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_live_domain_detail_with_options(request, runtime)

    def describe_live_domain_frame_rate_and_bit_rate_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.query_time):
            query['QueryTime'] = request.query_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLiveDomainFrameRateAndBitRateData',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveDomainFrameRateAndBitRateDataResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_live_domain_frame_rate_and_bit_rate_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_live_domain_frame_rate_and_bit_rate_data_with_options(request, runtime)

    def describe_live_domain_limit_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLiveDomainLimit',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveDomainLimitResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_live_domain_limit(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_live_domain_limit_with_options(request, runtime)

    def describe_live_domain_log_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLiveDomainLog',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveDomainLogResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_live_domain_log(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_live_domain_log_with_options(request, runtime)

    def describe_live_domain_mapping_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLiveDomainMapping',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveDomainMappingResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_live_domain_mapping(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_live_domain_mapping_with_options(request, runtime)

    def describe_live_domain_online_user_num_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.query_time):
            query['QueryTime'] = request.query_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLiveDomainOnlineUserNum',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveDomainOnlineUserNumResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_live_domain_online_user_num(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_live_domain_online_user_num_with_options(request, runtime)

    def describe_live_domain_push_bps_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.isp_name_en):
            query['IspNameEn'] = request.isp_name_en
        if not UtilClient.is_unset(request.location_name_en):
            query['LocationNameEn'] = request.location_name_en
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLiveDomainPushBpsData',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveDomainPushBpsDataResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_live_domain_push_bps_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_live_domain_push_bps_data_with_options(request, runtime)

    def describe_live_domain_push_traffic_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.isp_name_en):
            query['IspNameEn'] = request.isp_name_en
        if not UtilClient.is_unset(request.location_name_en):
            query['LocationNameEn'] = request.location_name_en
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLiveDomainPushTrafficData',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveDomainPushTrafficDataResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_live_domain_push_traffic_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_live_domain_push_traffic_data_with_options(request, runtime)

    def describe_live_domain_pv_uv_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLiveDomainPvUvData',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveDomainPvUvDataResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_live_domain_pv_uv_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_live_domain_pv_uv_data_with_options(request, runtime)

    def describe_live_domain_real_time_bps_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLiveDomainRealTimeBpsData',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveDomainRealTimeBpsDataResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_live_domain_real_time_bps_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_live_domain_real_time_bps_data_with_options(request, runtime)

    def describe_live_domain_real_time_http_code_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.isp_name_en):
            query['IspNameEn'] = request.isp_name_en
        if not UtilClient.is_unset(request.location_name_en):
            query['LocationNameEn'] = request.location_name_en
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLiveDomainRealTimeHttpCodeData',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveDomainRealTimeHttpCodeDataResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_live_domain_real_time_http_code_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_live_domain_real_time_http_code_data_with_options(request, runtime)

    def describe_live_domain_real_time_traffic_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.isp_name_en):
            query['IspNameEn'] = request.isp_name_en
        if not UtilClient.is_unset(request.location_name_en):
            query['LocationNameEn'] = request.location_name_en
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLiveDomainRealTimeTrafficData',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveDomainRealTimeTrafficDataResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_live_domain_real_time_traffic_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_live_domain_real_time_traffic_data_with_options(request, runtime)

    def describe_live_domain_realtime_log_delivery_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLiveDomainRealtimeLogDelivery',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveDomainRealtimeLogDeliveryResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_live_domain_realtime_log_delivery(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_live_domain_realtime_log_delivery_with_options(request, runtime)

    def describe_live_domain_record_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.record_type):
            query['RecordType'] = request.record_type
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLiveDomainRecordData',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveDomainRecordDataResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_live_domain_record_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_live_domain_record_data_with_options(request, runtime)

    def describe_live_domain_record_usage_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.split_by):
            query['SplitBy'] = request.split_by
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLiveDomainRecordUsageData',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveDomainRecordUsageDataResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_live_domain_record_usage_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_live_domain_record_usage_data_with_options(request, runtime)

    def describe_live_domain_snapshot_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLiveDomainSnapshotData',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveDomainSnapshotDataResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_live_domain_snapshot_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_live_domain_snapshot_data_with_options(request, runtime)

    def describe_live_domain_staging_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.function_names):
            query['FunctionNames'] = request.function_names
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLiveDomainStagingConfig',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveDomainStagingConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_live_domain_staging_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_live_domain_staging_config_with_options(request, runtime)

    def describe_live_domain_stream_transcode_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.split):
            query['Split'] = request.split
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLiveDomainStreamTranscodeData',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveDomainStreamTranscodeDataResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_live_domain_stream_transcode_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_live_domain_stream_transcode_data_with_options(request, runtime)

    def describe_live_domain_time_shift_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLiveDomainTimeShiftData',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveDomainTimeShiftDataResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_live_domain_time_shift_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_live_domain_time_shift_data_with_options(request, runtime)

    def describe_live_domain_traffic_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.isp_name_en):
            query['IspNameEn'] = request.isp_name_en
        if not UtilClient.is_unset(request.location_name_en):
            query['LocationNameEn'] = request.location_name_en
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLiveDomainTrafficData',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveDomainTrafficDataResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_live_domain_traffic_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_live_domain_traffic_data_with_options(request, runtime)

    def describe_live_domain_transcode_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLiveDomainTranscodeData',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveDomainTranscodeDataResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_live_domain_transcode_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_live_domain_transcode_data_with_options(request, runtime)

    def describe_live_drm_usage_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.split_by):
            query['SplitBy'] = request.split_by
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLiveDrmUsageData',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveDrmUsageDataResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_live_drm_usage_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_live_drm_usage_data_with_options(request, runtime)

    def describe_live_edge_transfer_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLiveEdgeTransfer',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveEdgeTransferResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_live_edge_transfer(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_live_edge_transfer_with_options(request, runtime)

    def describe_live_lazy_pull_stream_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLiveLazyPullStreamConfig',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveLazyPullStreamConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_live_lazy_pull_stream_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_live_lazy_pull_stream_config_with_options(request, runtime)

    def describe_live_producer_usage_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.instance):
            query['Instance'] = request.instance
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        if not UtilClient.is_unset(request.split_by):
            query['SplitBy'] = request.split_by
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        if not UtilClient.is_unset(request.app):
            query['app'] = request.app
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLiveProducerUsageData',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveProducerUsageDataResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_live_producer_usage_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_live_producer_usage_data_with_options(request, runtime)

    def describe_live_pull_stream_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLivePullStreamConfig',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLivePullStreamConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_live_pull_stream_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_live_pull_stream_config_with_options(request, runtime)

    def describe_live_realtime_delivery_acc_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.log_store):
            query['LogStore'] = request.log_store
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.project):
            query['Project'] = request.project
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLiveRealtimeDeliveryAcc',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveRealtimeDeliveryAccResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_live_realtime_delivery_acc(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_live_realtime_delivery_acc_with_options(request, runtime)

    def describe_live_realtime_log_authorized_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLiveRealtimeLogAuthorized',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveRealtimeLogAuthorizedResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_live_realtime_log_authorized(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_live_realtime_log_authorized_with_options(request, runtime)

    def describe_live_record_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.stream_name):
            query['StreamName'] = request.stream_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLiveRecordConfig',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveRecordConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_live_record_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_live_record_config_with_options(request, runtime)

    def describe_live_record_notify_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLiveRecordNotifyConfig',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveRecordNotifyConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_live_record_notify_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_live_record_notify_config_with_options(request, runtime)

    def describe_live_record_vod_configs_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.stream_name):
            query['StreamName'] = request.stream_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLiveRecordVodConfigs',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveRecordVodConfigsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_live_record_vod_configs(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_live_record_vod_configs_with_options(request, runtime)

    def describe_live_shift_configs_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLiveShiftConfigs',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveShiftConfigsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_live_shift_configs(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_live_shift_configs_with_options(request, runtime)

    def describe_live_snapshot_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLiveSnapshotConfig',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveSnapshotConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_live_snapshot_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_live_snapshot_config_with_options(request, runtime)

    def describe_live_snapshot_detect_porn_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLiveSnapshotDetectPornConfig',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveSnapshotDetectPornConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_live_snapshot_detect_porn_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_live_snapshot_detect_porn_config_with_options(request, runtime)

    def describe_live_stream_bit_rate_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.stream_name):
            query['StreamName'] = request.stream_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLiveStreamBitRateData',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveStreamBitRateDataResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_live_stream_bit_rate_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_live_stream_bit_rate_data_with_options(request, runtime)

    def describe_live_stream_count_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLiveStreamCount',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveStreamCountResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_live_stream_count(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_live_stream_count_with_options(request, runtime)

    def describe_live_stream_delay_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLiveStreamDelayConfig',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveStreamDelayConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_live_stream_delay_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_live_stream_delay_config_with_options(request, runtime)

    def describe_live_stream_history_user_num_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.stream_name):
            query['StreamName'] = request.stream_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLiveStreamHistoryUserNum',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveStreamHistoryUserNumResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_live_stream_history_user_num(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_live_stream_history_user_num_with_options(request, runtime)

    def describe_live_stream_metric_detail_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.next_page_token):
            query['NextPageToken'] = request.next_page_token
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.protocol):
            query['Protocol'] = request.protocol
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.stream_name):
            query['StreamName'] = request.stream_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLiveStreamMetricDetailData',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveStreamMetricDetailDataResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_live_stream_metric_detail_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_live_stream_metric_detail_data_with_options(request, runtime)

    def describe_live_stream_monitor_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.monitor_id):
            query['MonitorId'] = request.monitor_id
        if not UtilClient.is_unset(request.order_rule):
            query['OrderRule'] = request.order_rule
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
            action='DescribeLiveStreamMonitorList',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveStreamMonitorListResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_live_stream_monitor_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_live_stream_monitor_list_with_options(request, runtime)

    def describe_live_stream_optimized_feature_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.config_name):
            query['ConfigName'] = request.config_name
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLiveStreamOptimizedFeatureConfig',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveStreamOptimizedFeatureConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_live_stream_optimized_feature_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_live_stream_optimized_feature_config_with_options(request, runtime)

    def describe_live_stream_record_content_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.stream_name):
            query['StreamName'] = request.stream_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLiveStreamRecordContent',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveStreamRecordContentResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_live_stream_record_content(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_live_stream_record_content_with_options(request, runtime)

    def describe_live_stream_record_index_file_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.record_id):
            query['RecordId'] = request.record_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.stream_name):
            query['StreamName'] = request.stream_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLiveStreamRecordIndexFile',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveStreamRecordIndexFileResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_live_stream_record_index_file(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_live_stream_record_index_file_with_options(request, runtime)

    def describe_live_stream_record_index_files_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.stream_name):
            query['StreamName'] = request.stream_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLiveStreamRecordIndexFiles',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveStreamRecordIndexFilesResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_live_stream_record_index_files(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_live_stream_record_index_files_with_options(request, runtime)

    def describe_live_stream_snapshot_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.limit):
            query['Limit'] = request.limit
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.stream_name):
            query['StreamName'] = request.stream_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLiveStreamSnapshotInfo',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveStreamSnapshotInfoResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_live_stream_snapshot_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_live_stream_snapshot_info_with_options(request, runtime)

    def describe_live_stream_state_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.stream_name):
            query['StreamName'] = request.stream_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLiveStreamState',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveStreamStateResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_live_stream_state(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_live_stream_state_with_options(request, runtime)

    def describe_live_stream_transcode_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_transcode_name):
            query['DomainTranscodeName'] = request.domain_transcode_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLiveStreamTranscodeInfo',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveStreamTranscodeInfoResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_live_stream_transcode_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_live_stream_transcode_info_with_options(request, runtime)

    def describe_live_stream_transcode_stream_num_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLiveStreamTranscodeStreamNum',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveStreamTranscodeStreamNumResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_live_stream_transcode_stream_num(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_live_stream_transcode_stream_num_with_options(request, runtime)

    def describe_live_stream_watermark_rules_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLiveStreamWatermarkRules',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveStreamWatermarkRulesResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_live_stream_watermark_rules(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_live_stream_watermark_rules_with_options(request, runtime)

    def describe_live_stream_watermarks_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLiveStreamWatermarks',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveStreamWatermarksResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_live_stream_watermarks(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_live_stream_watermarks_with_options(request, runtime)

    def describe_live_streams_block_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLiveStreamsBlockList',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveStreamsBlockListResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_live_streams_block_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_live_streams_block_list_with_options(request, runtime)

    def describe_live_streams_control_history_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLiveStreamsControlHistory',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveStreamsControlHistoryResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_live_streams_control_history(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_live_streams_control_history_with_options(request, runtime)

    def describe_live_streams_notify_url_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLiveStreamsNotifyUrlConfig',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveStreamsNotifyUrlConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_live_streams_notify_url_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_live_streams_notify_url_config_with_options(request, runtime)

    def describe_live_streams_online_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.only_stream):
            query['OnlyStream'] = request.only_stream
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.query_type):
            query['QueryType'] = request.query_type
        if not UtilClient.is_unset(request.stream_name):
            query['StreamName'] = request.stream_name
        if not UtilClient.is_unset(request.stream_type):
            query['StreamType'] = request.stream_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLiveStreamsOnlineList',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveStreamsOnlineListResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_live_streams_online_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_live_streams_online_list_with_options(request, runtime)

    def describe_live_streams_publish_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.order_by):
            query['OrderBy'] = request.order_by
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.query_type):
            query['QueryType'] = request.query_type
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.stream_name):
            query['StreamName'] = request.stream_name
        if not UtilClient.is_unset(request.stream_type):
            query['StreamType'] = request.stream_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLiveStreamsPublishList',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveStreamsPublishListResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_live_streams_publish_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_live_streams_publish_list_with_options(request, runtime)

    def describe_live_tag_resources_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLiveTagResources',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveTagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_live_tag_resources(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_live_tag_resources_with_options(request, runtime)

    def describe_live_top_domains_by_flow_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.limit):
            query['Limit'] = request.limit
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLiveTopDomainsByFlow',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveTopDomainsByFlowResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_live_top_domains_by_flow(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_live_top_domains_by_flow_with_options(request, runtime)

    def describe_live_user_bill_prediction_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.area):
            query['Area'] = request.area
        if not UtilClient.is_unset(request.dimension):
            query['Dimension'] = request.dimension
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLiveUserBillPrediction',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveUserBillPredictionResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_live_user_bill_prediction(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_live_user_bill_prediction_with_options(request, runtime)

    def describe_live_user_domains_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.domain_search_type):
            query['DomainSearchType'] = request.domain_search_type
        if not UtilClient.is_unset(request.domain_status):
            query['DomainStatus'] = request.domain_status
        if not UtilClient.is_unset(request.live_domain_type):
            query['LiveDomainType'] = request.live_domain_type
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_name):
            query['RegionName'] = request.region_name
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLiveUserDomains',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveUserDomainsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_live_user_domains(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_live_user_domains_with_options(request, runtime)

    def describe_live_user_tags_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLiveUserTags',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeLiveUserTagsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_live_user_tags(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_live_user_tags_with_options(request, runtime)

    def describe_meter_live_rtc_duration_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.service_area):
            query['ServiceArea'] = request.service_area
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.app_id):
            query['appId'] = request.app_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeMeterLiveRtcDuration',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeMeterLiveRtcDurationResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_meter_live_rtc_duration(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_meter_live_rtc_duration_with_options(request, runtime)

    def describe_mix_stream_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.mix_stream_id):
            query['MixStreamId'] = request.mix_stream_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.stream_name):
            query['StreamName'] = request.stream_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeMixStreamList',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeMixStreamListResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_mix_stream_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_mix_stream_list_with_options(request, runtime)

    def describe_rtsnative_sdkfirst_frame_cost_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = live_20161101_models.DescribeRTSNativeSDKFirstFrameCostShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.domain_name_list):
            request.domain_name_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.domain_name_list, 'DomainNameList', 'json')
        query = {}
        if not UtilClient.is_unset(request.data_interval):
            query['DataInterval'] = request.data_interval
        if not UtilClient.is_unset(request.domain_name_list_shrink):
            query['DomainNameList'] = request.domain_name_list_shrink
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRTSNativeSDKFirstFrameCost',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeRTSNativeSDKFirstFrameCostResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_rtsnative_sdkfirst_frame_cost(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_rtsnative_sdkfirst_frame_cost_with_options(request, runtime)

    def describe_rtsnative_sdkfirst_frame_delay_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = live_20161101_models.DescribeRTSNativeSDKFirstFrameDelayShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.domain_name_list):
            request.domain_name_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.domain_name_list, 'DomainNameList', 'json')
        query = {}
        if not UtilClient.is_unset(request.data_interval):
            query['DataInterval'] = request.data_interval
        if not UtilClient.is_unset(request.domain_name_list_shrink):
            query['DomainNameList'] = request.domain_name_list_shrink
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRTSNativeSDKFirstFrameDelay',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeRTSNativeSDKFirstFrameDelayResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_rtsnative_sdkfirst_frame_delay(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_rtsnative_sdkfirst_frame_delay_with_options(request, runtime)

    def describe_rtsnative_sdkplay_fail_status_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = live_20161101_models.DescribeRTSNativeSDKPlayFailStatusShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.domain_name_list):
            request.domain_name_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.domain_name_list, 'DomainNameList', 'json')
        query = {}
        if not UtilClient.is_unset(request.data_interval):
            query['DataInterval'] = request.data_interval
        if not UtilClient.is_unset(request.domain_name_list_shrink):
            query['DomainNameList'] = request.domain_name_list_shrink
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRTSNativeSDKPlayFailStatus',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeRTSNativeSDKPlayFailStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_rtsnative_sdkplay_fail_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_rtsnative_sdkplay_fail_status_with_options(request, runtime)

    def describe_rtsnative_sdkplay_time_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = live_20161101_models.DescribeRTSNativeSDKPlayTimeShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.domain_name_list):
            request.domain_name_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.domain_name_list, 'DomainNameList', 'json')
        query = {}
        if not UtilClient.is_unset(request.data_interval):
            query['DataInterval'] = request.data_interval
        if not UtilClient.is_unset(request.domain_name_list_shrink):
            query['DomainNameList'] = request.domain_name_list_shrink
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRTSNativeSDKPlayTime',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeRTSNativeSDKPlayTimeResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_rtsnative_sdkplay_time(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_rtsnative_sdkplay_time_with_options(request, runtime)

    def describe_rtsnative_sdkvv_data_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = live_20161101_models.DescribeRTSNativeSDKVvDataShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.domain_name_list):
            request.domain_name_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.domain_name_list, 'DomainNameList', 'json')
        query = {}
        if not UtilClient.is_unset(request.data_interval):
            query['DataInterval'] = request.data_interval
        if not UtilClient.is_unset(request.domain_name_list_shrink):
            query['DomainNameList'] = request.domain_name_list_shrink
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRTSNativeSDKVvData',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeRTSNativeSDKVvDataResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_rtsnative_sdkvv_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_rtsnative_sdkvv_data_with_options(request, runtime)

    def describe_room_kickout_user_list_with_options(self, request, runtime):
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
        if not UtilClient.is_unset(request.room_id):
            query['RoomId'] = request.room_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRoomKickoutUserList',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeRoomKickoutUserListResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_room_kickout_user_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_room_kickout_user_list_with_options(request, runtime)

    def describe_room_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.anchor_id):
            query['AnchorId'] = request.anchor_id
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.room_id):
            query['RoomId'] = request.room_id
        if not UtilClient.is_unset(request.room_status):
            query['RoomStatus'] = request.room_status
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRoomList',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeRoomListResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_room_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_room_list_with_options(request, runtime)

    def describe_room_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.room_id):
            query['RoomId'] = request.room_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRoomStatus',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeRoomStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_room_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_room_status_with_options(request, runtime)

    def describe_show_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.caster_id):
            query['CasterId'] = request.caster_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeShowList',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeShowListResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_show_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_show_list_with_options(request, runtime)

    def describe_studio_layouts_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.caster_id):
            query['CasterId'] = request.caster_id
        if not UtilClient.is_unset(request.layout_id):
            query['LayoutId'] = request.layout_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeStudioLayouts',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeStudioLayoutsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_studio_layouts(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_studio_layouts_with_options(request, runtime)

    def describe_toutiao_live_play_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app):
            query['App'] = request.app
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.stream):
            query['Stream'] = request.stream
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeToutiaoLivePlay',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeToutiaoLivePlayResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_toutiao_live_play(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_toutiao_live_play_with_options(request, runtime)

    def describe_toutiao_live_publish_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app):
            query['App'] = request.app
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.stream):
            query['Stream'] = request.stream
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeToutiaoLivePublish',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeToutiaoLivePublishResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_toutiao_live_publish(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_toutiao_live_publish_with_options(request, runtime)

    def describe_up_bps_peak_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.domain_switch):
            query['DomainSwitch'] = request.domain_switch
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeUpBpsPeakData',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeUpBpsPeakDataResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_up_bps_peak_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_up_bps_peak_data_with_options(request, runtime)

    def describe_up_bps_peak_of_line_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.domain_switch):
            query['DomainSwitch'] = request.domain_switch
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.line):
            query['Line'] = request.line
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeUpBpsPeakOfLine',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeUpBpsPeakOfLineResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_up_bps_peak_of_line(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_up_bps_peak_of_line_with_options(request, runtime)

    def describe_up_peak_publish_stream_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.domain_switch):
            query['DomainSwitch'] = request.domain_switch
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeUpPeakPublishStreamData',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DescribeUpPeakPublishStreamDataResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_up_peak_publish_stream_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_up_peak_publish_stream_data_with_options(request, runtime)

    def disable_live_realtime_log_delivery_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DisableLiveRealtimeLogDelivery',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DisableLiveRealtimeLogDeliveryResponse(),
            self.call_api(params, req, runtime)
        )

    def disable_live_realtime_log_delivery(self, request):
        runtime = util_models.RuntimeOptions()
        return self.disable_live_realtime_log_delivery_with_options(request, runtime)

    def dynamic_update_water_mark_stream_rule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app):
            query['App'] = request.app
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.stream):
            query['Stream'] = request.stream
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DynamicUpdateWaterMarkStreamRule',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.DynamicUpdateWaterMarkStreamRuleResponse(),
            self.call_api(params, req, runtime)
        )

    def dynamic_update_water_mark_stream_rule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.dynamic_update_water_mark_stream_rule_with_options(request, runtime)

    def edit_playlist_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.program_config):
            query['ProgramConfig'] = request.program_config
        if not UtilClient.is_unset(request.program_id):
            query['ProgramId'] = request.program_id
        if not UtilClient.is_unset(request.program_items):
            query['ProgramItems'] = request.program_items
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EditPlaylist',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.EditPlaylistResponse(),
            self.call_api(params, req, runtime)
        )

    def edit_playlist(self, request):
        runtime = util_models.RuntimeOptions()
        return self.edit_playlist_with_options(request, runtime)

    def edit_show_and_replace_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.caster_id):
            query['CasterId'] = request.caster_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.show_id):
            query['ShowId'] = request.show_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.storage_info):
            query['StorageInfo'] = request.storage_info
        if not UtilClient.is_unset(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EditShowAndReplace',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.EditShowAndReplaceResponse(),
            self.call_api(params, req, runtime)
        )

    def edit_show_and_replace(self, request):
        runtime = util_models.RuntimeOptions()
        return self.edit_show_and_replace_with_options(request, runtime)

    def effect_caster_urgent_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.caster_id):
            query['CasterId'] = request.caster_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.scene_id):
            query['SceneId'] = request.scene_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EffectCasterUrgent',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.EffectCasterUrgentResponse(),
            self.call_api(params, req, runtime)
        )

    def effect_caster_urgent(self, request):
        runtime = util_models.RuntimeOptions()
        return self.effect_caster_urgent_with_options(request, runtime)

    def effect_caster_video_resource_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.caster_id):
            query['CasterId'] = request.caster_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.scene_id):
            query['SceneId'] = request.scene_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EffectCasterVideoResource',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.EffectCasterVideoResourceResponse(),
            self.call_api(params, req, runtime)
        )

    def effect_caster_video_resource(self, request):
        runtime = util_models.RuntimeOptions()
        return self.effect_caster_video_resource_with_options(request, runtime)

    def enable_live_realtime_log_delivery_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnableLiveRealtimeLogDelivery',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.EnableLiveRealtimeLogDeliveryResponse(),
            self.call_api(params, req, runtime)
        )

    def enable_live_realtime_log_delivery(self, request):
        runtime = util_models.RuntimeOptions()
        return self.enable_live_realtime_log_delivery_with_options(request, runtime)

    def forbid_live_stream_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.live_stream_type):
            query['LiveStreamType'] = request.live_stream_type
        if not UtilClient.is_unset(request.oneshot):
            query['Oneshot'] = request.oneshot
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resume_time):
            query['ResumeTime'] = request.resume_time
        if not UtilClient.is_unset(request.stream_name):
            query['StreamName'] = request.stream_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ForbidLiveStream',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.ForbidLiveStreamResponse(),
            self.call_api(params, req, runtime)
        )

    def forbid_live_stream(self, request):
        runtime = util_models.RuntimeOptions()
        return self.forbid_live_stream_with_options(request, runtime)

    def forbid_push_stream_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.room_id):
            query['RoomId'] = request.room_id
        if not UtilClient.is_unset(request.user_data):
            query['UserData'] = request.user_data
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ForbidPushStream',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.ForbidPushStreamResponse(),
            self.call_api(params, req, runtime)
        )

    def forbid_push_stream(self, request):
        runtime = util_models.RuntimeOptions()
        return self.forbid_push_stream_with_options(request, runtime)

    def get_all_custom_templates_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAllCustomTemplates',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.GetAllCustomTemplatesResponse(),
            self.call_api(params, req, runtime)
        )

    def get_all_custom_templates(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_all_custom_templates_with_options(request, runtime)

    def get_custom_template_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.template):
            query['Template'] = request.template
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetCustomTemplate',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.GetCustomTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    def get_custom_template(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_custom_template_with_options(request, runtime)

    def get_editing_job_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.caster_id):
            query['CasterId'] = request.caster_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.show_id):
            query['ShowId'] = request.show_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetEditingJobInfo',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.GetEditingJobInfoResponse(),
            self.call_api(params, req, runtime)
        )

    def get_editing_job_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_editing_job_info_with_options(request, runtime)

    def get_message_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.group_id):
            body['GroupId'] = request.group_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetMessageGroup',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.GetMessageGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def get_message_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_message_group_with_options(request, runtime)

    def get_message_token_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.device_id):
            body['DeviceId'] = request.device_id
        if not UtilClient.is_unset(request.device_type):
            body['DeviceType'] = request.device_type
        if not UtilClient.is_unset(request.user_id):
            body['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetMessageToken',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.GetMessageTokenResponse(),
            self.call_api(params, req, runtime)
        )

    def get_message_token(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_message_token_with_options(request, runtime)

    def get_message_user_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.cloud_uid):
            body['CloudUid'] = request.cloud_uid
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetMessageUserInfo',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.GetMessageUserInfoResponse(),
            self.call_api(params, req, runtime)
        )

    def get_message_user_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_message_user_info_with_options(request, runtime)

    def get_multi_rate_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app):
            query['App'] = request.app
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetMultiRateConfig',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.GetMultiRateConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def get_multi_rate_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_multi_rate_config_with_options(request, runtime)

    def get_multi_rate_config_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetMultiRateConfigList',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.GetMultiRateConfigListResponse(),
            self.call_api(params, req, runtime)
        )

    def get_multi_rate_config_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_multi_rate_config_list_with_options(request, runtime)

    def hot_live_rtc_stream_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.audio_msid):
            query['AudioMsid'] = request.audio_msid
        if not UtilClient.is_unset(request.connection_timeout):
            query['ConnectionTimeout'] = request.connection_timeout
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.media_timeout):
            query['MediaTimeout'] = request.media_timeout
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_code):
            query['RegionCode'] = request.region_code
        if not UtilClient.is_unset(request.stream_name):
            query['StreamName'] = request.stream_name
        if not UtilClient.is_unset(request.video_msid):
            query['VideoMsid'] = request.video_msid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='HotLiveRtcStream',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.HotLiveRtcStreamResponse(),
            self.call_api(params, req, runtime)
        )

    def hot_live_rtc_stream(self, request):
        runtime = util_models.RuntimeOptions()
        return self.hot_live_rtc_stream_with_options(request, runtime)

    def initialize_auto_show_list_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.call_back_url):
            query['CallBackUrl'] = request.call_back_url
        if not UtilClient.is_unset(request.caster_config):
            query['CasterConfig'] = request.caster_config
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_ids):
            query['ResourceIds'] = request.resource_ids
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='InitializeAutoShowListTask',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.InitializeAutoShowListTaskResponse(),
            self.call_api(params, req, runtime)
        )

    def initialize_auto_show_list_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.initialize_auto_show_list_task_with_options(request, runtime)

    def join_message_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.broad_cast_statistics):
            body['BroadCastStatistics'] = request.broad_cast_statistics
        if not UtilClient.is_unset(request.broad_cast_type):
            body['BroadCastType'] = request.broad_cast_type
        if not UtilClient.is_unset(request.group_id):
            body['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.user_id):
            body['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='JoinMessageGroup',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.JoinMessageGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def join_message_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.join_message_group_with_options(request, runtime)

    def leave_message_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.broad_cast_statistics):
            body['BroadCastStatistics'] = request.broad_cast_statistics
        if not UtilClient.is_unset(request.broad_cast_type):
            body['BroadCastType'] = request.broad_cast_type
        if not UtilClient.is_unset(request.group_id):
            body['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.user_id):
            body['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='LeaveMessageGroup',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.LeaveMessageGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def leave_message_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.leave_message_group_with_options(request, runtime)

    def list_live_realtime_log_delivery_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListLiveRealtimeLogDelivery',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.ListLiveRealtimeLogDeliveryResponse(),
            self.call_api(params, req, runtime)
        )

    def list_live_realtime_log_delivery(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_live_realtime_log_delivery_with_options(request, runtime)

    def list_live_realtime_log_delivery_domains_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListLiveRealtimeLogDeliveryDomains',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.ListLiveRealtimeLogDeliveryDomainsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_live_realtime_log_delivery_domains(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_live_realtime_log_delivery_domains_with_options(request, runtime)

    def list_live_realtime_log_delivery_infos_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListLiveRealtimeLogDeliveryInfos',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.ListLiveRealtimeLogDeliveryInfosResponse(),
            self.call_api(params, req, runtime)
        )

    def list_live_realtime_log_delivery_infos(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_live_realtime_log_delivery_infos_with_options(request, runtime)

    def list_message_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.group_id):
            body['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.page_num):
            body['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.sort_type):
            body['SortType'] = request.sort_type
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListMessage',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.ListMessageResponse(),
            self.call_api(params, req, runtime)
        )

    def list_message(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_message_with_options(request, runtime)

    def list_message_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.page_num):
            body['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.sort_type):
            body['SortType'] = request.sort_type
        if not UtilClient.is_unset(request.user_id):
            body['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListMessageGroup',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.ListMessageGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def list_message_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_message_group_with_options(request, runtime)

    def list_message_group_user_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.group_id):
            body['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.page_num):
            body['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.sort_type):
            body['SortType'] = request.sort_type
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListMessageGroupUser',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.ListMessageGroupUserResponse(),
            self.call_api(params, req, runtime)
        )

    def list_message_group_user(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_message_group_user_with_options(request, runtime)

    def list_playlist_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page):
            query['Page'] = request.page
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.program_id):
            query['ProgramId'] = request.program_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPlaylist',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.ListPlaylistResponse(),
            self.call_api(params, req, runtime)
        )

    def list_playlist(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_playlist_with_options(request, runtime)

    def list_playlist_items_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.program_id):
            query['ProgramId'] = request.program_id
        if not UtilClient.is_unset(request.program_item_ids):
            query['ProgramItemIds'] = request.program_item_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPlaylistItems',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.ListPlaylistItemsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_playlist_items(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_playlist_items_with_options(request, runtime)

    def modify_caster_component_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.caption_layer_content):
            query['CaptionLayerContent'] = request.caption_layer_content
        if not UtilClient.is_unset(request.caster_id):
            query['CasterId'] = request.caster_id
        if not UtilClient.is_unset(request.component_id):
            query['ComponentId'] = request.component_id
        if not UtilClient.is_unset(request.component_layer):
            query['ComponentLayer'] = request.component_layer
        if not UtilClient.is_unset(request.component_name):
            query['ComponentName'] = request.component_name
        if not UtilClient.is_unset(request.component_type):
            query['ComponentType'] = request.component_type
        if not UtilClient.is_unset(request.effect):
            query['Effect'] = request.effect
        if not UtilClient.is_unset(request.image_layer_content):
            query['ImageLayerContent'] = request.image_layer_content
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.text_layer_content):
            query['TextLayerContent'] = request.text_layer_content
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyCasterComponent',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.ModifyCasterComponentResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_caster_component(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_caster_component_with_options(request, runtime)

    def modify_caster_episode_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.caster_id):
            query['CasterId'] = request.caster_id
        if not UtilClient.is_unset(request.component_id):
            query['ComponentId'] = request.component_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.episode_id):
            query['EpisodeId'] = request.episode_id
        if not UtilClient.is_unset(request.episode_name):
            query['EpisodeName'] = request.episode_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.switch_type):
            query['SwitchType'] = request.switch_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyCasterEpisode',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.ModifyCasterEpisodeResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_caster_episode(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_caster_episode_with_options(request, runtime)

    def modify_caster_layout_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.audio_layer):
            query['AudioLayer'] = request.audio_layer
        if not UtilClient.is_unset(request.blend_list):
            query['BlendList'] = request.blend_list
        if not UtilClient.is_unset(request.caster_id):
            query['CasterId'] = request.caster_id
        if not UtilClient.is_unset(request.layout_id):
            query['LayoutId'] = request.layout_id
        if not UtilClient.is_unset(request.mix_list):
            query['MixList'] = request.mix_list
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.video_layer):
            query['VideoLayer'] = request.video_layer
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyCasterLayout',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.ModifyCasterLayoutResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_caster_layout(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_caster_layout_with_options(request, runtime)

    def modify_caster_program_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.caster_id):
            query['CasterId'] = request.caster_id
        if not UtilClient.is_unset(request.episode):
            query['Episode'] = request.episode
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyCasterProgram',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.ModifyCasterProgramResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_caster_program(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_caster_program_with_options(request, runtime)

    def modify_caster_video_resource_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.begin_offset):
            query['BeginOffset'] = request.begin_offset
        if not UtilClient.is_unset(request.caster_id):
            query['CasterId'] = request.caster_id
        if not UtilClient.is_unset(request.end_offset):
            query['EndOffset'] = request.end_offset
        if not UtilClient.is_unset(request.live_stream_url):
            query['LiveStreamUrl'] = request.live_stream_url
        if not UtilClient.is_unset(request.material_id):
            query['MaterialId'] = request.material_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.pts_callback_interval):
            query['PtsCallbackInterval'] = request.pts_callback_interval
        if not UtilClient.is_unset(request.repeat_num):
            query['RepeatNum'] = request.repeat_num
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_name):
            query['ResourceName'] = request.resource_name
        if not UtilClient.is_unset(request.vod_url):
            query['VodUrl'] = request.vod_url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyCasterVideoResource',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.ModifyCasterVideoResourceResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_caster_video_resource(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_caster_video_resource_with_options(request, runtime)

    def modify_live_domain_schdm_by_property_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.property):
            query['Property'] = request.property
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyLiveDomainSchdmByProperty',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.ModifyLiveDomainSchdmByPropertyResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_live_domain_schdm_by_property(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_live_domain_schdm_by_property_with_options(request, runtime)

    def modify_live_realtime_log_delivery_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyLiveRealtimeLogDelivery',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.ModifyLiveRealtimeLogDeliveryResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_live_realtime_log_delivery(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_live_realtime_log_delivery_with_options(request, runtime)

    def modify_show_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.caster_id):
            query['CasterId'] = request.caster_id
        if not UtilClient.is_unset(request.high_priority_show_id):
            query['HighPriorityShowId'] = request.high_priority_show_id
        if not UtilClient.is_unset(request.high_priority_show_start_time):
            query['HighPriorityShowStartTime'] = request.high_priority_show_start_time
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.repeat_times):
            query['RepeatTimes'] = request.repeat_times
        if not UtilClient.is_unset(request.show_id):
            query['ShowId'] = request.show_id
        if not UtilClient.is_unset(request.spot):
            query['Spot'] = request.spot
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyShowList',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.ModifyShowListResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_show_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_show_list_with_options(request, runtime)

    def modify_studio_layout_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bg_image_config):
            query['BgImageConfig'] = request.bg_image_config
        if not UtilClient.is_unset(request.caster_id):
            query['CasterId'] = request.caster_id
        if not UtilClient.is_unset(request.common_config):
            query['CommonConfig'] = request.common_config
        if not UtilClient.is_unset(request.layer_order_config_list):
            query['LayerOrderConfigList'] = request.layer_order_config_list
        if not UtilClient.is_unset(request.layout_id):
            query['LayoutId'] = request.layout_id
        if not UtilClient.is_unset(request.layout_name):
            query['LayoutName'] = request.layout_name
        if not UtilClient.is_unset(request.media_input_config_list):
            query['MediaInputConfigList'] = request.media_input_config_list
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.screen_input_config_list):
            query['ScreenInputConfigList'] = request.screen_input_config_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyStudioLayout',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.ModifyStudioLayoutResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_studio_layout(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_studio_layout_with_options(request, runtime)

    def open_live_shift_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.duration):
            query['Duration'] = request.duration
        if not UtilClient.is_unset(request.ignore_transcode):
            query['IgnoreTranscode'] = request.ignore_transcode
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.stream_name):
            query['StreamName'] = request.stream_name
        if not UtilClient.is_unset(request.vision):
            query['Vision'] = request.vision
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='OpenLiveShift',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.OpenLiveShiftResponse(),
            self.call_api(params, req, runtime)
        )

    def open_live_shift(self, request):
        runtime = util_models.RuntimeOptions()
        return self.open_live_shift_with_options(request, runtime)

    def play_choosen_show_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.caster_id):
            query['CasterId'] = request.caster_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.show_id):
            query['ShowId'] = request.show_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PlayChoosenShow',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.PlayChoosenShowResponse(),
            self.call_api(params, req, runtime)
        )

    def play_choosen_show(self, request):
        runtime = util_models.RuntimeOptions()
        return self.play_choosen_show_with_options(request, runtime)

    def publish_live_staging_config_to_production_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.function_name):
            query['FunctionName'] = request.function_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PublishLiveStagingConfigToProduction',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.PublishLiveStagingConfigToProductionResponse(),
            self.call_api(params, req, runtime)
        )

    def publish_live_staging_config_to_production(self, request):
        runtime = util_models.RuntimeOptions()
        return self.publish_live_staging_config_to_production_with_options(request, runtime)

    def query_snapshot_callback_auth_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QuerySnapshotCallbackAuth',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.QuerySnapshotCallbackAuthResponse(),
            self.call_api(params, req, runtime)
        )

    def query_snapshot_callback_auth(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_snapshot_callback_auth_with_options(request, runtime)

    def real_time_record_command_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.command):
            query['Command'] = request.command
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.stream_name):
            query['StreamName'] = request.stream_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RealTimeRecordCommand',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.RealTimeRecordCommandResponse(),
            self.call_api(params, req, runtime)
        )

    def real_time_record_command(self, request):
        runtime = util_models.RuntimeOptions()
        return self.real_time_record_command_with_options(request, runtime)

    def real_time_snapshot_command_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.command):
            query['Command'] = request.command
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.mode):
            query['Mode'] = request.mode
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        if not UtilClient.is_unset(request.stream_name):
            query['StreamName'] = request.stream_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RealTimeSnapshotCommand',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.RealTimeSnapshotCommandResponse(),
            self.call_api(params, req, runtime)
        )

    def real_time_snapshot_command(self, request):
        runtime = util_models.RuntimeOptions()
        return self.real_time_snapshot_command_with_options(request, runtime)

    def remove_show_from_show_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.caster_id):
            query['CasterId'] = request.caster_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.show_id):
            query['ShowId'] = request.show_id
        if not UtilClient.is_unset(request.is_batch_mode):
            query['isBatchMode'] = request.is_batch_mode
        if not UtilClient.is_unset(request.show_id_list):
            query['showIdList'] = request.show_id_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemoveShowFromShowList',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.RemoveShowFromShowListResponse(),
            self.call_api(params, req, runtime)
        )

    def remove_show_from_show_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.remove_show_from_show_list_with_options(request, runtime)

    def resume_live_stream_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.live_stream_type):
            query['LiveStreamType'] = request.live_stream_type
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.stream_name):
            query['StreamName'] = request.stream_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ResumeLiveStream',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.ResumeLiveStreamResponse(),
            self.call_api(params, req, runtime)
        )

    def resume_live_stream(self, request):
        runtime = util_models.RuntimeOptions()
        return self.resume_live_stream_with_options(request, runtime)

    def rollback_live_staging_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.function_name):
            query['FunctionName'] = request.function_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RollbackLiveStagingConfig',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.RollbackLiveStagingConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def rollback_live_staging_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.rollback_live_staging_config_with_options(request, runtime)

    def send_room_notification_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.app_uid):
            query['AppUid'] = request.app_uid
        if not UtilClient.is_unset(request.data):
            query['Data'] = request.data
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.priority):
            query['Priority'] = request.priority
        if not UtilClient.is_unset(request.room_id):
            query['RoomId'] = request.room_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SendRoomNotification',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.SendRoomNotificationResponse(),
            self.call_api(params, req, runtime)
        )

    def send_room_notification(self, request):
        runtime = util_models.RuntimeOptions()
        return self.send_room_notification_with_options(request, runtime)

    def send_room_user_notification_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.app_uid):
            query['AppUid'] = request.app_uid
        if not UtilClient.is_unset(request.data):
            query['Data'] = request.data
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.priority):
            query['Priority'] = request.priority
        if not UtilClient.is_unset(request.room_id):
            query['RoomId'] = request.room_id
        if not UtilClient.is_unset(request.to_app_uid):
            query['ToAppUid'] = request.to_app_uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SendRoomUserNotification',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.SendRoomUserNotificationResponse(),
            self.call_api(params, req, runtime)
        )

    def send_room_user_notification(self, request):
        runtime = util_models.RuntimeOptions()
        return self.send_room_user_notification_with_options(request, runtime)

    def set_caster_channel_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.caster_id):
            query['CasterId'] = request.caster_id
        if not UtilClient.is_unset(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.face_beauty):
            query['FaceBeauty'] = request.face_beauty
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.play_status):
            query['PlayStatus'] = request.play_status
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.seek_offset):
            query['SeekOffset'] = request.seek_offset
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetCasterChannel',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.SetCasterChannelResponse(),
            self.call_api(params, req, runtime)
        )

    def set_caster_channel(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_caster_channel_with_options(request, runtime)

    def set_caster_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.callback_url):
            query['CallbackUrl'] = request.callback_url
        if not UtilClient.is_unset(request.caster_id):
            query['CasterId'] = request.caster_id
        if not UtilClient.is_unset(request.caster_name):
            query['CasterName'] = request.caster_name
        if not UtilClient.is_unset(request.channel_enable):
            query['ChannelEnable'] = request.channel_enable
        if not UtilClient.is_unset(request.delay):
            query['Delay'] = request.delay
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.program_effect):
            query['ProgramEffect'] = request.program_effect
        if not UtilClient.is_unset(request.program_name):
            query['ProgramName'] = request.program_name
        if not UtilClient.is_unset(request.record_config):
            query['RecordConfig'] = request.record_config
        if not UtilClient.is_unset(request.side_output_url):
            query['SideOutputUrl'] = request.side_output_url
        if not UtilClient.is_unset(request.side_output_url_list):
            query['SideOutputUrlList'] = request.side_output_url_list
        if not UtilClient.is_unset(request.sync_groups_config):
            query['SyncGroupsConfig'] = request.sync_groups_config
        if not UtilClient.is_unset(request.transcode_config):
            query['TranscodeConfig'] = request.transcode_config
        if not UtilClient.is_unset(request.urgent_live_stream_url):
            query['UrgentLiveStreamUrl'] = request.urgent_live_stream_url
        if not UtilClient.is_unset(request.urgent_material_id):
            query['UrgentMaterialId'] = request.urgent_material_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetCasterConfig',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.SetCasterConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def set_caster_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_caster_config_with_options(request, runtime)

    def set_caster_scene_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.caster_id):
            query['CasterId'] = request.caster_id
        if not UtilClient.is_unset(request.component_id):
            query['ComponentId'] = request.component_id
        if not UtilClient.is_unset(request.layout_id):
            query['LayoutId'] = request.layout_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.scene_id):
            query['SceneId'] = request.scene_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetCasterSceneConfig',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.SetCasterSceneConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def set_caster_scene_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_caster_scene_config_with_options(request, runtime)

    def set_caster_sync_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.caster_id):
            query['CasterId'] = request.caster_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.sync_group):
            query['SyncGroup'] = request.sync_group
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetCasterSyncGroup',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.SetCasterSyncGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def set_caster_sync_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_caster_sync_group_with_options(request, runtime)

    def set_caster_timed_event_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.caster_id):
            query['CasterId'] = request.caster_id
        if not UtilClient.is_unset(request.event_name):
            query['EventName'] = request.event_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.start_time_utc):
            query['StartTimeUTC'] = request.start_time_utc
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetCasterTimedEvent',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.SetCasterTimedEventResponse(),
            self.call_api(params, req, runtime)
        )

    def set_caster_timed_event(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_caster_timed_event_with_options(request, runtime)

    def set_live_domain_certificate_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cert_name):
            query['CertName'] = request.cert_name
        if not UtilClient.is_unset(request.cert_type):
            query['CertType'] = request.cert_type
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.force_set):
            query['ForceSet'] = request.force_set
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.sslpri):
            query['SSLPri'] = request.sslpri
        if not UtilClient.is_unset(request.sslprotocol):
            query['SSLProtocol'] = request.sslprotocol
        if not UtilClient.is_unset(request.sslpub):
            query['SSLPub'] = request.sslpub
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetLiveDomainCertificate',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.SetLiveDomainCertificateResponse(),
            self.call_api(params, req, runtime)
        )

    def set_live_domain_certificate(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_live_domain_certificate_with_options(request, runtime)

    def set_live_domain_staging_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.functions):
            query['Functions'] = request.functions
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetLiveDomainStagingConfig',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.SetLiveDomainStagingConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def set_live_domain_staging_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_live_domain_staging_config_with_options(request, runtime)

    def set_live_edge_transfer_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.http_dns):
            query['HttpDns'] = request.http_dns
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.stream_name):
            query['StreamName'] = request.stream_name
        if not UtilClient.is_unset(request.target_domain_list):
            query['TargetDomainList'] = request.target_domain_list
        if not UtilClient.is_unset(request.transfer_args):
            query['TransferArgs'] = request.transfer_args
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetLiveEdgeTransfer',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.SetLiveEdgeTransferResponse(),
            self.call_api(params, req, runtime)
        )

    def set_live_edge_transfer(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_live_edge_transfer_with_options(request, runtime)

    def set_live_lazy_pull_stream_info_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.pull_app_name):
            query['PullAppName'] = request.pull_app_name
        if not UtilClient.is_unset(request.pull_domain_name):
            query['PullDomainName'] = request.pull_domain_name
        if not UtilClient.is_unset(request.pull_protocol):
            query['PullProtocol'] = request.pull_protocol
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetLiveLazyPullStreamInfoConfig',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.SetLiveLazyPullStreamInfoConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def set_live_lazy_pull_stream_info_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_live_lazy_pull_stream_info_config_with_options(request, runtime)

    def set_live_stream_delay_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.flv_delay):
            query['FlvDelay'] = request.flv_delay
        if not UtilClient.is_unset(request.flv_level):
            query['FlvLevel'] = request.flv_level
        if not UtilClient.is_unset(request.hls_delay):
            query['HlsDelay'] = request.hls_delay
        if not UtilClient.is_unset(request.hls_level):
            query['HlsLevel'] = request.hls_level
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.rtmp_delay):
            query['RtmpDelay'] = request.rtmp_delay
        if not UtilClient.is_unset(request.rtmp_level):
            query['RtmpLevel'] = request.rtmp_level
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetLiveStreamDelayConfig',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.SetLiveStreamDelayConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def set_live_stream_delay_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_live_stream_delay_config_with_options(request, runtime)

    def set_live_stream_optimized_feature_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.config_name):
            query['ConfigName'] = request.config_name
        if not UtilClient.is_unset(request.config_status):
            query['ConfigStatus'] = request.config_status
        if not UtilClient.is_unset(request.config_value):
            query['ConfigValue'] = request.config_value
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetLiveStreamOptimizedFeatureConfig',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.SetLiveStreamOptimizedFeatureConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def set_live_stream_optimized_feature_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_live_stream_optimized_feature_config_with_options(request, runtime)

    def set_live_streams_notify_url_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.notify_auth_key):
            query['NotifyAuthKey'] = request.notify_auth_key
        if not UtilClient.is_unset(request.notify_req_auth):
            query['NotifyReqAuth'] = request.notify_req_auth
        if not UtilClient.is_unset(request.notify_url):
            query['NotifyUrl'] = request.notify_url
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetLiveStreamsNotifyUrlConfig',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.SetLiveStreamsNotifyUrlConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def set_live_streams_notify_url_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_live_streams_notify_url_config_with_options(request, runtime)

    def set_snapshot_callback_auth_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.callback_auth_key):
            query['CallbackAuthKey'] = request.callback_auth_key
        if not UtilClient.is_unset(request.callback_req_auth):
            query['CallbackReqAuth'] = request.callback_req_auth
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetSnapshotCallbackAuth',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.SetSnapshotCallbackAuthResponse(),
            self.call_api(params, req, runtime)
        )

    def set_snapshot_callback_auth(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_snapshot_callback_auth_with_options(request, runtime)

    def start_caster_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.caster_id):
            query['CasterId'] = request.caster_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartCaster',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.StartCasterResponse(),
            self.call_api(params, req, runtime)
        )

    def start_caster(self, request):
        runtime = util_models.RuntimeOptions()
        return self.start_caster_with_options(request, runtime)

    def start_caster_scene_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.caster_id):
            query['CasterId'] = request.caster_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.scene_id):
            query['SceneId'] = request.scene_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartCasterScene',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.StartCasterSceneResponse(),
            self.call_api(params, req, runtime)
        )

    def start_caster_scene(self, request):
        runtime = util_models.RuntimeOptions()
        return self.start_caster_scene_with_options(request, runtime)

    def start_live_domain_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartLiveDomain',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.StartLiveDomainResponse(),
            self.call_api(params, req, runtime)
        )

    def start_live_domain(self, request):
        runtime = util_models.RuntimeOptions()
        return self.start_live_domain_with_options(request, runtime)

    def start_live_stream_monitor_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.monitor_id):
            query['MonitorId'] = request.monitor_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartLiveStreamMonitor',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.StartLiveStreamMonitorResponse(),
            self.call_api(params, req, runtime)
        )

    def start_live_stream_monitor(self, request):
        runtime = util_models.RuntimeOptions()
        return self.start_live_stream_monitor_with_options(request, runtime)

    def start_playlist_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.offset):
            query['Offset'] = request.offset
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.program_id):
            query['ProgramId'] = request.program_id
        if not UtilClient.is_unset(request.resume_mode):
            query['ResumeMode'] = request.resume_mode
        if not UtilClient.is_unset(request.start_item_id):
            query['StartItemId'] = request.start_item_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartPlaylist',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.StartPlaylistResponse(),
            self.call_api(params, req, runtime)
        )

    def start_playlist(self, request):
        runtime = util_models.RuntimeOptions()
        return self.start_playlist_with_options(request, runtime)

    def stop_caster_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.caster_id):
            query['CasterId'] = request.caster_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopCaster',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.StopCasterResponse(),
            self.call_api(params, req, runtime)
        )

    def stop_caster(self, request):
        runtime = util_models.RuntimeOptions()
        return self.stop_caster_with_options(request, runtime)

    def stop_caster_scene_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.caster_id):
            query['CasterId'] = request.caster_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.scene_id):
            query['SceneId'] = request.scene_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopCasterScene',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.StopCasterSceneResponse(),
            self.call_api(params, req, runtime)
        )

    def stop_caster_scene(self, request):
        runtime = util_models.RuntimeOptions()
        return self.stop_caster_scene_with_options(request, runtime)

    def stop_live_domain_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopLiveDomain',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.StopLiveDomainResponse(),
            self.call_api(params, req, runtime)
        )

    def stop_live_domain(self, request):
        runtime = util_models.RuntimeOptions()
        return self.stop_live_domain_with_options(request, runtime)

    def stop_live_stream_monitor_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.monitor_id):
            query['MonitorId'] = request.monitor_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopLiveStreamMonitor',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.StopLiveStreamMonitorResponse(),
            self.call_api(params, req, runtime)
        )

    def stop_live_stream_monitor(self, request):
        runtime = util_models.RuntimeOptions()
        return self.stop_live_stream_monitor_with_options(request, runtime)

    def stop_playlist_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.program_id):
            query['ProgramId'] = request.program_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopPlaylist',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.StopPlaylistResponse(),
            self.call_api(params, req, runtime)
        )

    def stop_playlist(self, request):
        runtime = util_models.RuntimeOptions()
        return self.stop_playlist_with_options(request, runtime)

    def tag_live_resources_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TagLiveResources',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.TagLiveResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    def tag_live_resources(self, request):
        runtime = util_models.RuntimeOptions()
        return self.tag_live_resources_with_options(request, runtime)

    def un_tag_live_resources_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.all):
            query['All'] = request.all
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag_key):
            query['TagKey'] = request.tag_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UnTagLiveResources',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.UnTagLiveResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    def un_tag_live_resources(self, request):
        runtime = util_models.RuntimeOptions()
        return self.un_tag_live_resources_with_options(request, runtime)

    def update_caster_scene_audio_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.audio_layer):
            query['AudioLayer'] = request.audio_layer
        if not UtilClient.is_unset(request.caster_id):
            query['CasterId'] = request.caster_id
        if not UtilClient.is_unset(request.follow_enable):
            query['FollowEnable'] = request.follow_enable
        if not UtilClient.is_unset(request.mix_list):
            query['MixList'] = request.mix_list
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.scene_id):
            query['SceneId'] = request.scene_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateCasterSceneAudio',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.UpdateCasterSceneAudioResponse(),
            self.call_api(params, req, runtime)
        )

    def update_caster_scene_audio(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_caster_scene_audio_with_options(request, runtime)

    def update_caster_scene_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.caster_id):
            query['CasterId'] = request.caster_id
        if not UtilClient.is_unset(request.component_id):
            query['ComponentId'] = request.component_id
        if not UtilClient.is_unset(request.layout_id):
            query['LayoutId'] = request.layout_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.scene_id):
            query['SceneId'] = request.scene_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateCasterSceneConfig',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.UpdateCasterSceneConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def update_caster_scene_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_caster_scene_config_with_options(request, runtime)

    def update_live_app_snapshot_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.callback):
            query['Callback'] = request.callback
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.oss_bucket):
            query['OssBucket'] = request.oss_bucket
        if not UtilClient.is_unset(request.oss_endpoint):
            query['OssEndpoint'] = request.oss_endpoint
        if not UtilClient.is_unset(request.overwrite_oss_object):
            query['OverwriteOssObject'] = request.overwrite_oss_object
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.sequence_oss_object):
            query['SequenceOssObject'] = request.sequence_oss_object
        if not UtilClient.is_unset(request.time_interval):
            query['TimeInterval'] = request.time_interval
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateLiveAppSnapshotConfig',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.UpdateLiveAppSnapshotConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def update_live_app_snapshot_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_live_app_snapshot_config_with_options(request, runtime)

    def update_live_audio_audit_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.biz_type):
            query['BizType'] = request.biz_type
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.oss_bucket):
            query['OssBucket'] = request.oss_bucket
        if not UtilClient.is_unset(request.oss_endpoint):
            query['OssEndpoint'] = request.oss_endpoint
        if not UtilClient.is_unset(request.oss_object):
            query['OssObject'] = request.oss_object
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.stream_name):
            query['StreamName'] = request.stream_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateLiveAudioAuditConfig',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.UpdateLiveAudioAuditConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def update_live_audio_audit_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_live_audio_audit_config_with_options(request, runtime)

    def update_live_audio_audit_notify_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.callback):
            query['Callback'] = request.callback
        if not UtilClient.is_unset(request.callback_template):
            query['CallbackTemplate'] = request.callback_template
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateLiveAudioAuditNotifyConfig',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.UpdateLiveAudioAuditNotifyConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def update_live_audio_audit_notify_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_live_audio_audit_notify_config_with_options(request, runtime)

    def update_live_detect_notify_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.notify_url):
            query['NotifyUrl'] = request.notify_url
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateLiveDetectNotifyConfig',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.UpdateLiveDetectNotifyConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def update_live_detect_notify_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_live_detect_notify_config_with_options(request, runtime)

    def update_live_pull_stream_info_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateLivePullStreamInfoConfig',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.UpdateLivePullStreamInfoConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def update_live_pull_stream_info_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_live_pull_stream_info_config_with_options(request, runtime)

    def update_live_record_notify_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.need_status_notify):
            query['NeedStatusNotify'] = request.need_status_notify
        if not UtilClient.is_unset(request.notify_url):
            query['NotifyUrl'] = request.notify_url
        if not UtilClient.is_unset(request.on_demand_url):
            query['OnDemandUrl'] = request.on_demand_url
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateLiveRecordNotifyConfig',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.UpdateLiveRecordNotifyConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def update_live_record_notify_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_live_record_notify_config_with_options(request, runtime)

    def update_live_snapshot_detect_porn_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.oss_bucket):
            query['OssBucket'] = request.oss_bucket
        if not UtilClient.is_unset(request.oss_endpoint):
            query['OssEndpoint'] = request.oss_endpoint
        if not UtilClient.is_unset(request.oss_object):
            query['OssObject'] = request.oss_object
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.scene):
            query['Scene'] = request.scene
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateLiveSnapshotDetectPornConfig',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.UpdateLiveSnapshotDetectPornConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def update_live_snapshot_detect_porn_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_live_snapshot_detect_porn_config_with_options(request, runtime)

    def update_live_stream_monitor_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app):
            query['App'] = request.app
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.input_list):
            query['InputList'] = request.input_list
        if not UtilClient.is_unset(request.monitor_id):
            query['MonitorId'] = request.monitor_id
        if not UtilClient.is_unset(request.monitor_name):
            query['MonitorName'] = request.monitor_name
        if not UtilClient.is_unset(request.output_template):
            query['OutputTemplate'] = request.output_template
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.stream):
            query['Stream'] = request.stream
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateLiveStreamMonitor',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.UpdateLiveStreamMonitorResponse(),
            self.call_api(params, req, runtime)
        )

    def update_live_stream_monitor(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_live_stream_monitor_with_options(request, runtime)

    def update_live_stream_watermark_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.height):
            query['Height'] = request.height
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.offset_corner):
            query['OffsetCorner'] = request.offset_corner
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.picture_url):
            query['PictureUrl'] = request.picture_url
        if not UtilClient.is_unset(request.ref_height):
            query['RefHeight'] = request.ref_height
        if not UtilClient.is_unset(request.ref_width):
            query['RefWidth'] = request.ref_width
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        if not UtilClient.is_unset(request.transparency):
            query['Transparency'] = request.transparency
        if not UtilClient.is_unset(request.xoffset):
            query['XOffset'] = request.xoffset
        if not UtilClient.is_unset(request.yoffset):
            query['YOffset'] = request.yoffset
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateLiveStreamWatermark',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.UpdateLiveStreamWatermarkResponse(),
            self.call_api(params, req, runtime)
        )

    def update_live_stream_watermark(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_live_stream_watermark_with_options(request, runtime)

    def update_live_stream_watermark_rule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.rule_id):
            query['RuleId'] = request.rule_id
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateLiveStreamWatermarkRule',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.UpdateLiveStreamWatermarkRuleResponse(),
            self.call_api(params, req, runtime)
        )

    def update_live_stream_watermark_rule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_live_stream_watermark_rule_with_options(request, runtime)

    def update_live_top_level_domain_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        if not UtilClient.is_unset(request.top_level_domain):
            query['TopLevelDomain'] = request.top_level_domain
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateLiveTopLevelDomain',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.UpdateLiveTopLevelDomainResponse(),
            self.call_api(params, req, runtime)
        )

    def update_live_top_level_domain(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_live_top_level_domain_with_options(request, runtime)

    def update_mix_stream_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.input_stream_list):
            query['InputStreamList'] = request.input_stream_list
        if not UtilClient.is_unset(request.layout_id):
            query['LayoutId'] = request.layout_id
        if not UtilClient.is_unset(request.mix_stream_id):
            query['MixStreamId'] = request.mix_stream_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateMixStream',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.UpdateMixStreamResponse(),
            self.call_api(params, req, runtime)
        )

    def update_mix_stream(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_mix_stream_with_options(request, runtime)

    def verify_live_domain_owner_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.verify_type):
            query['VerifyType'] = request.verify_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='VerifyLiveDomainOwner',
            version='2016-11-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            live_20161101_models.VerifyLiveDomainOwnerResponse(),
            self.call_api(params, req, runtime)
        )

    def verify_live_domain_owner(self, request):
        runtime = util_models.RuntimeOptions()
        return self.verify_live_domain_owner_with_options(request, runtime)
