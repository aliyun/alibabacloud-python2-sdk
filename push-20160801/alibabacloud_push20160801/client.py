# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_push20160801 import models as push_20160801_models
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
            'ap-northeast-1': 'cloudpush.aliyuncs.com',
            'ap-northeast-2-pop': 'cloudpush.aliyuncs.com',
            'ap-south-1': 'cloudpush.aliyuncs.com',
            'ap-southeast-1': 'cloudpush.aliyuncs.com',
            'ap-southeast-2': 'cloudpush.aliyuncs.com',
            'ap-southeast-3': 'cloudpush.aliyuncs.com',
            'ap-southeast-5': 'cloudpush.aliyuncs.com',
            'cn-beijing': 'cloudpush.aliyuncs.com',
            'cn-beijing-finance-1': 'cloudpush.aliyuncs.com',
            'cn-beijing-finance-pop': 'cloudpush.aliyuncs.com',
            'cn-beijing-gov-1': 'cloudpush.aliyuncs.com',
            'cn-beijing-nu16-b01': 'cloudpush.aliyuncs.com',
            'cn-chengdu': 'cloudpush.aliyuncs.com',
            'cn-edge-1': 'cloudpush.aliyuncs.com',
            'cn-fujian': 'cloudpush.aliyuncs.com',
            'cn-haidian-cm12-c01': 'cloudpush.aliyuncs.com',
            'cn-hangzhou': 'cloudpush.aliyuncs.com',
            'cn-hangzhou-bj-b01': 'cloudpush.aliyuncs.com',
            'cn-hangzhou-finance': 'cloudpush.aliyuncs.com',
            'cn-hangzhou-internal-prod-1': 'cloudpush.aliyuncs.com',
            'cn-hangzhou-internal-test-1': 'cloudpush.aliyuncs.com',
            'cn-hangzhou-internal-test-2': 'cloudpush.aliyuncs.com',
            'cn-hangzhou-internal-test-3': 'cloudpush.aliyuncs.com',
            'cn-hangzhou-test-306': 'cloudpush.aliyuncs.com',
            'cn-hongkong': 'cloudpush.aliyuncs.com',
            'cn-hongkong-finance-pop': 'cloudpush.aliyuncs.com',
            'cn-huhehaote': 'cloudpush.aliyuncs.com',
            'cn-north-2-gov-1': 'cloudpush.aliyuncs.com',
            'cn-qingdao': 'cloudpush.aliyuncs.com',
            'cn-qingdao-nebula': 'cloudpush.aliyuncs.com',
            'cn-shanghai': 'cloudpush.aliyuncs.com',
            'cn-shanghai-et15-b01': 'cloudpush.aliyuncs.com',
            'cn-shanghai-et2-b01': 'cloudpush.aliyuncs.com',
            'cn-shanghai-finance-1': 'cloudpush.aliyuncs.com',
            'cn-shanghai-inner': 'cloudpush.aliyuncs.com',
            'cn-shanghai-internal-test-1': 'cloudpush.aliyuncs.com',
            'cn-shenzhen': 'cloudpush.aliyuncs.com',
            'cn-shenzhen-finance-1': 'cloudpush.aliyuncs.com',
            'cn-shenzhen-inner': 'cloudpush.aliyuncs.com',
            'cn-shenzhen-st4-d01': 'cloudpush.aliyuncs.com',
            'cn-shenzhen-su18-b01': 'cloudpush.aliyuncs.com',
            'cn-wuhan': 'cloudpush.aliyuncs.com',
            'cn-yushanfang': 'cloudpush.aliyuncs.com',
            'cn-zhangbei-na61-b01': 'cloudpush.aliyuncs.com',
            'cn-zhangjiakou': 'cloudpush.aliyuncs.com',
            'cn-zhangjiakou-na62-a01': 'cloudpush.aliyuncs.com',
            'cn-zhengzhou-nebula-1': 'cloudpush.aliyuncs.com',
            'eu-central-1': 'cloudpush.aliyuncs.com',
            'eu-west-1': 'cloudpush.aliyuncs.com',
            'eu-west-1-oxs': 'cloudpush.aliyuncs.com',
            'me-east-1': 'cloudpush.aliyuncs.com',
            'rus-west-1-pop': 'cloudpush.aliyuncs.com',
            'us-east-1': 'cloudpush.aliyuncs.com',
            'us-west-1': 'cloudpush.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('push', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def bind_alias_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alias_name):
            query['AliasName'] = request.alias_name
        if not UtilClient.is_unset(request.app_key):
            query['AppKey'] = request.app_key
        if not UtilClient.is_unset(request.device_id):
            query['DeviceId'] = request.device_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BindAlias',
            version='2016-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            push_20160801_models.BindAliasResponse(),
            self.call_api(params, req, runtime)
        )

    def bind_alias(self, request):
        runtime = util_models.RuntimeOptions()
        return self.bind_alias_with_options(request, runtime)

    def bind_phone_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_key):
            query['AppKey'] = request.app_key
        if not UtilClient.is_unset(request.device_id):
            query['DeviceId'] = request.device_id
        if not UtilClient.is_unset(request.phone_number):
            query['PhoneNumber'] = request.phone_number
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BindPhone',
            version='2016-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            push_20160801_models.BindPhoneResponse(),
            self.call_api(params, req, runtime)
        )

    def bind_phone(self, request):
        runtime = util_models.RuntimeOptions()
        return self.bind_phone_with_options(request, runtime)

    def bind_tag_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_key):
            query['AppKey'] = request.app_key
        if not UtilClient.is_unset(request.client_key):
            query['ClientKey'] = request.client_key
        if not UtilClient.is_unset(request.key_type):
            query['KeyType'] = request.key_type
        if not UtilClient.is_unset(request.tag_name):
            query['TagName'] = request.tag_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BindTag',
            version='2016-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            push_20160801_models.BindTagResponse(),
            self.call_api(params, req, runtime)
        )

    def bind_tag(self, request):
        runtime = util_models.RuntimeOptions()
        return self.bind_tag_with_options(request, runtime)

    def cancel_push_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_key):
            query['AppKey'] = request.app_key
        if not UtilClient.is_unset(request.message_id):
            query['MessageId'] = request.message_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CancelPush',
            version='2016-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            push_20160801_models.CancelPushResponse(),
            self.call_api(params, req, runtime)
        )

    def cancel_push(self, request):
        runtime = util_models.RuntimeOptions()
        return self.cancel_push_with_options(request, runtime)

    def check_certificate_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_key):
            query['AppKey'] = request.app_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CheckCertificate',
            version='2016-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            push_20160801_models.CheckCertificateResponse(),
            self.call_api(params, req, runtime)
        )

    def check_certificate(self, request):
        runtime = util_models.RuntimeOptions()
        return self.check_certificate_with_options(request, runtime)

    def check_device_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_key):
            query['AppKey'] = request.app_key
        if not UtilClient.is_unset(request.device_id):
            query['DeviceId'] = request.device_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CheckDevice',
            version='2016-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            push_20160801_models.CheckDeviceResponse(),
            self.call_api(params, req, runtime)
        )

    def check_device(self, request):
        runtime = util_models.RuntimeOptions()
        return self.check_device_with_options(request, runtime)

    def check_devices_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_key):
            query['AppKey'] = request.app_key
        if not UtilClient.is_unset(request.device_ids):
            query['DeviceIds'] = request.device_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CheckDevices',
            version='2016-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            push_20160801_models.CheckDevicesResponse(),
            self.call_api(params, req, runtime)
        )

    def check_devices(self, request):
        runtime = util_models.RuntimeOptions()
        return self.check_devices_with_options(request, runtime)

    def complete_continuously_push_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_key):
            query['AppKey'] = request.app_key
        if not UtilClient.is_unset(request.message_id):
            query['MessageId'] = request.message_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CompleteContinuouslyPush',
            version='2016-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            push_20160801_models.CompleteContinuouslyPushResponse(),
            self.call_api(params, req, runtime)
        )

    def complete_continuously_push(self, request):
        runtime = util_models.RuntimeOptions()
        return self.complete_continuously_push_with_options(request, runtime)

    def continuously_push_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_key):
            query['AppKey'] = request.app_key
        if not UtilClient.is_unset(request.message_id):
            query['MessageId'] = request.message_id
        if not UtilClient.is_unset(request.target):
            query['Target'] = request.target
        if not UtilClient.is_unset(request.target_value):
            query['TargetValue'] = request.target_value
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ContinuouslyPush',
            version='2016-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            push_20160801_models.ContinuouslyPushResponse(),
            self.call_api(params, req, runtime)
        )

    def continuously_push(self, request):
        runtime = util_models.RuntimeOptions()
        return self.continuously_push_with_options(request, runtime)

    def list_summary_apps_with_options(self, runtime):
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='ListSummaryApps',
            version='2016-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            push_20160801_models.ListSummaryAppsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_summary_apps(self):
        runtime = util_models.RuntimeOptions()
        return self.list_summary_apps_with_options(runtime)

    def list_tags_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_key):
            query['AppKey'] = request.app_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTags',
            version='2016-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            push_20160801_models.ListTagsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_tags(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_tags_with_options(request, runtime)

    def mass_push_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_key):
            query['AppKey'] = request.app_key
        body = {}
        if not UtilClient.is_unset(request.push_task):
            body['PushTask'] = request.push_task
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='MassPush',
            version='2016-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            push_20160801_models.MassPushResponse(),
            self.call_api(params, req, runtime)
        )

    def mass_push(self, request):
        runtime = util_models.RuntimeOptions()
        return self.mass_push_with_options(request, runtime)

    def push_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.android_activity):
            query['AndroidActivity'] = request.android_activity
        if not UtilClient.is_unset(request.android_big_body):
            query['AndroidBigBody'] = request.android_big_body
        if not UtilClient.is_unset(request.android_big_picture_url):
            query['AndroidBigPictureUrl'] = request.android_big_picture_url
        if not UtilClient.is_unset(request.android_big_title):
            query['AndroidBigTitle'] = request.android_big_title
        if not UtilClient.is_unset(request.android_ext_parameters):
            query['AndroidExtParameters'] = request.android_ext_parameters
        if not UtilClient.is_unset(request.android_image_url):
            query['AndroidImageUrl'] = request.android_image_url
        if not UtilClient.is_unset(request.android_inbox_body):
            query['AndroidInboxBody'] = request.android_inbox_body
        if not UtilClient.is_unset(request.android_message_huawei_category):
            query['AndroidMessageHuaweiCategory'] = request.android_message_huawei_category
        if not UtilClient.is_unset(request.android_message_huawei_urgency):
            query['AndroidMessageHuaweiUrgency'] = request.android_message_huawei_urgency
        if not UtilClient.is_unset(request.android_music):
            query['AndroidMusic'] = request.android_music
        if not UtilClient.is_unset(request.android_notification_bar_priority):
            query['AndroidNotificationBarPriority'] = request.android_notification_bar_priority
        if not UtilClient.is_unset(request.android_notification_bar_type):
            query['AndroidNotificationBarType'] = request.android_notification_bar_type
        if not UtilClient.is_unset(request.android_notification_channel):
            query['AndroidNotificationChannel'] = request.android_notification_channel
        if not UtilClient.is_unset(request.android_notification_huawei_channel):
            query['AndroidNotificationHuaweiChannel'] = request.android_notification_huawei_channel
        if not UtilClient.is_unset(request.android_notification_notify_id):
            query['AndroidNotificationNotifyId'] = request.android_notification_notify_id
        if not UtilClient.is_unset(request.android_notification_vivo_channel):
            query['AndroidNotificationVivoChannel'] = request.android_notification_vivo_channel
        if not UtilClient.is_unset(request.android_notification_xiaomi_channel):
            query['AndroidNotificationXiaomiChannel'] = request.android_notification_xiaomi_channel
        if not UtilClient.is_unset(request.android_notify_type):
            query['AndroidNotifyType'] = request.android_notify_type
        if not UtilClient.is_unset(request.android_open_type):
            query['AndroidOpenType'] = request.android_open_type
        if not UtilClient.is_unset(request.android_open_url):
            query['AndroidOpenUrl'] = request.android_open_url
        if not UtilClient.is_unset(request.android_popup_activity):
            query['AndroidPopupActivity'] = request.android_popup_activity
        if not UtilClient.is_unset(request.android_popup_body):
            query['AndroidPopupBody'] = request.android_popup_body
        if not UtilClient.is_unset(request.android_popup_title):
            query['AndroidPopupTitle'] = request.android_popup_title
        if not UtilClient.is_unset(request.android_remind):
            query['AndroidRemind'] = request.android_remind
        if not UtilClient.is_unset(request.android_render_style):
            query['AndroidRenderStyle'] = request.android_render_style
        if not UtilClient.is_unset(request.android_xiao_mi_activity):
            query['AndroidXiaoMiActivity'] = request.android_xiao_mi_activity
        if not UtilClient.is_unset(request.android_xiao_mi_notify_body):
            query['AndroidXiaoMiNotifyBody'] = request.android_xiao_mi_notify_body
        if not UtilClient.is_unset(request.android_xiao_mi_notify_title):
            query['AndroidXiaoMiNotifyTitle'] = request.android_xiao_mi_notify_title
        if not UtilClient.is_unset(request.android_xiaomi_big_picture_url):
            query['AndroidXiaomiBigPictureUrl'] = request.android_xiaomi_big_picture_url
        if not UtilClient.is_unset(request.android_xiaomi_image_url):
            query['AndroidXiaomiImageUrl'] = request.android_xiaomi_image_url
        if not UtilClient.is_unset(request.app_key):
            query['AppKey'] = request.app_key
        if not UtilClient.is_unset(request.body):
            query['Body'] = request.body
        if not UtilClient.is_unset(request.device_type):
            query['DeviceType'] = request.device_type
        if not UtilClient.is_unset(request.expire_time):
            query['ExpireTime'] = request.expire_time
        if not UtilClient.is_unset(request.job_key):
            query['JobKey'] = request.job_key
        if not UtilClient.is_unset(request.push_time):
            query['PushTime'] = request.push_time
        if not UtilClient.is_unset(request.push_type):
            query['PushType'] = request.push_type
        if not UtilClient.is_unset(request.send_channels):
            query['SendChannels'] = request.send_channels
        if not UtilClient.is_unset(request.send_speed):
            query['SendSpeed'] = request.send_speed
        if not UtilClient.is_unset(request.sms_delay_secs):
            query['SmsDelaySecs'] = request.sms_delay_secs
        if not UtilClient.is_unset(request.sms_params):
            query['SmsParams'] = request.sms_params
        if not UtilClient.is_unset(request.sms_send_policy):
            query['SmsSendPolicy'] = request.sms_send_policy
        if not UtilClient.is_unset(request.sms_sign_name):
            query['SmsSignName'] = request.sms_sign_name
        if not UtilClient.is_unset(request.sms_template_name):
            query['SmsTemplateName'] = request.sms_template_name
        if not UtilClient.is_unset(request.store_offline):
            query['StoreOffline'] = request.store_offline
        if not UtilClient.is_unset(request.target):
            query['Target'] = request.target
        if not UtilClient.is_unset(request.target_value):
            query['TargetValue'] = request.target_value
        if not UtilClient.is_unset(request.title):
            query['Title'] = request.title
        if not UtilClient.is_unset(request.i_osapns_env):
            query['iOSApnsEnv'] = request.i_osapns_env
        if not UtilClient.is_unset(request.i_osbadge):
            query['iOSBadge'] = request.i_osbadge
        if not UtilClient.is_unset(request.i_osbadge_auto_increment):
            query['iOSBadgeAutoIncrement'] = request.i_osbadge_auto_increment
        if not UtilClient.is_unset(request.i_osext_parameters):
            query['iOSExtParameters'] = request.i_osext_parameters
        if not UtilClient.is_unset(request.i_osmusic):
            query['iOSMusic'] = request.i_osmusic
        if not UtilClient.is_unset(request.i_osmutable_content):
            query['iOSMutableContent'] = request.i_osmutable_content
        if not UtilClient.is_unset(request.i_osnotification_category):
            query['iOSNotificationCategory'] = request.i_osnotification_category
        if not UtilClient.is_unset(request.i_osnotification_collapse_id):
            query['iOSNotificationCollapseId'] = request.i_osnotification_collapse_id
        if not UtilClient.is_unset(request.i_osnotification_thread_id):
            query['iOSNotificationThreadId'] = request.i_osnotification_thread_id
        if not UtilClient.is_unset(request.i_osremind):
            query['iOSRemind'] = request.i_osremind
        if not UtilClient.is_unset(request.i_osremind_body):
            query['iOSRemindBody'] = request.i_osremind_body
        if not UtilClient.is_unset(request.i_ossilent_notification):
            query['iOSSilentNotification'] = request.i_ossilent_notification
        if not UtilClient.is_unset(request.i_ossubtitle):
            query['iOSSubtitle'] = request.i_ossubtitle
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='Push',
            version='2016-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            push_20160801_models.PushResponse(),
            self.call_api(params, req, runtime)
        )

    def push(self, request):
        runtime = util_models.RuntimeOptions()
        return self.push_with_options(request, runtime)

    def push_message_to_android_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_key):
            query['AppKey'] = request.app_key
        if not UtilClient.is_unset(request.body):
            query['Body'] = request.body
        if not UtilClient.is_unset(request.job_key):
            query['JobKey'] = request.job_key
        if not UtilClient.is_unset(request.target):
            query['Target'] = request.target
        if not UtilClient.is_unset(request.target_value):
            query['TargetValue'] = request.target_value
        if not UtilClient.is_unset(request.title):
            query['Title'] = request.title
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PushMessageToAndroid',
            version='2016-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            push_20160801_models.PushMessageToAndroidResponse(),
            self.call_api(params, req, runtime)
        )

    def push_message_to_android(self, request):
        runtime = util_models.RuntimeOptions()
        return self.push_message_to_android_with_options(request, runtime)

    def push_message_toi_oswith_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_key):
            query['AppKey'] = request.app_key
        if not UtilClient.is_unset(request.body):
            query['Body'] = request.body
        if not UtilClient.is_unset(request.job_key):
            query['JobKey'] = request.job_key
        if not UtilClient.is_unset(request.target):
            query['Target'] = request.target
        if not UtilClient.is_unset(request.target_value):
            query['TargetValue'] = request.target_value
        if not UtilClient.is_unset(request.title):
            query['Title'] = request.title
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PushMessageToiOS',
            version='2016-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            push_20160801_models.PushMessageToiOSResponse(),
            self.call_api(params, req, runtime)
        )

    def push_message_toi_os(self, request):
        runtime = util_models.RuntimeOptions()
        return self.push_message_toi_oswith_options(request, runtime)

    def push_notice_to_android_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_key):
            query['AppKey'] = request.app_key
        if not UtilClient.is_unset(request.body):
            query['Body'] = request.body
        if not UtilClient.is_unset(request.ext_parameters):
            query['ExtParameters'] = request.ext_parameters
        if not UtilClient.is_unset(request.job_key):
            query['JobKey'] = request.job_key
        if not UtilClient.is_unset(request.target):
            query['Target'] = request.target
        if not UtilClient.is_unset(request.target_value):
            query['TargetValue'] = request.target_value
        if not UtilClient.is_unset(request.title):
            query['Title'] = request.title
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PushNoticeToAndroid',
            version='2016-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            push_20160801_models.PushNoticeToAndroidResponse(),
            self.call_api(params, req, runtime)
        )

    def push_notice_to_android(self, request):
        runtime = util_models.RuntimeOptions()
        return self.push_notice_to_android_with_options(request, runtime)

    def push_notice_toi_oswith_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.apns_env):
            query['ApnsEnv'] = request.apns_env
        if not UtilClient.is_unset(request.app_key):
            query['AppKey'] = request.app_key
        if not UtilClient.is_unset(request.body):
            query['Body'] = request.body
        if not UtilClient.is_unset(request.ext_parameters):
            query['ExtParameters'] = request.ext_parameters
        if not UtilClient.is_unset(request.job_key):
            query['JobKey'] = request.job_key
        if not UtilClient.is_unset(request.target):
            query['Target'] = request.target
        if not UtilClient.is_unset(request.target_value):
            query['TargetValue'] = request.target_value
        if not UtilClient.is_unset(request.title):
            query['Title'] = request.title
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PushNoticeToiOS',
            version='2016-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            push_20160801_models.PushNoticeToiOSResponse(),
            self.call_api(params, req, runtime)
        )

    def push_notice_toi_os(self, request):
        runtime = util_models.RuntimeOptions()
        return self.push_notice_toi_oswith_options(request, runtime)

    def query_aliases_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_key):
            query['AppKey'] = request.app_key
        if not UtilClient.is_unset(request.device_id):
            query['DeviceId'] = request.device_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryAliases',
            version='2016-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            push_20160801_models.QueryAliasesResponse(),
            self.call_api(params, req, runtime)
        )

    def query_aliases(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_aliases_with_options(request, runtime)

    def query_device_count_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_key):
            query['AppKey'] = request.app_key
        if not UtilClient.is_unset(request.target):
            query['Target'] = request.target
        if not UtilClient.is_unset(request.target_value):
            query['TargetValue'] = request.target_value
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryDeviceCount',
            version='2016-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            push_20160801_models.QueryDeviceCountResponse(),
            self.call_api(params, req, runtime)
        )

    def query_device_count(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_device_count_with_options(request, runtime)

    def query_device_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_key):
            query['AppKey'] = request.app_key
        if not UtilClient.is_unset(request.device_id):
            query['DeviceId'] = request.device_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryDeviceInfo',
            version='2016-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            push_20160801_models.QueryDeviceInfoResponse(),
            self.call_api(params, req, runtime)
        )

    def query_device_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_device_info_with_options(request, runtime)

    def query_device_stat_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_key):
            query['AppKey'] = request.app_key
        if not UtilClient.is_unset(request.device_type):
            query['DeviceType'] = request.device_type
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.query_type):
            query['QueryType'] = request.query_type
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryDeviceStat',
            version='2016-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            push_20160801_models.QueryDeviceStatResponse(),
            self.call_api(params, req, runtime)
        )

    def query_device_stat(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_device_stat_with_options(request, runtime)

    def query_devices_by_account_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account):
            query['Account'] = request.account
        if not UtilClient.is_unset(request.app_key):
            query['AppKey'] = request.app_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryDevicesByAccount',
            version='2016-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            push_20160801_models.QueryDevicesByAccountResponse(),
            self.call_api(params, req, runtime)
        )

    def query_devices_by_account(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_devices_by_account_with_options(request, runtime)

    def query_devices_by_alias_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alias):
            query['Alias'] = request.alias
        if not UtilClient.is_unset(request.app_key):
            query['AppKey'] = request.app_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryDevicesByAlias',
            version='2016-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            push_20160801_models.QueryDevicesByAliasResponse(),
            self.call_api(params, req, runtime)
        )

    def query_devices_by_alias(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_devices_by_alias_with_options(request, runtime)

    def query_push_records_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_key):
            query['AppKey'] = request.app_key
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.keyword):
            query['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.page):
            query['Page'] = request.page
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.push_type):
            query['PushType'] = request.push_type
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.target):
            query['Target'] = request.target
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryPushRecords',
            version='2016-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            push_20160801_models.QueryPushRecordsResponse(),
            self.call_api(params, req, runtime)
        )

    def query_push_records(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_push_records_with_options(request, runtime)

    def query_push_stat_by_app_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_key):
            query['AppKey'] = request.app_key
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.granularity):
            query['Granularity'] = request.granularity
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryPushStatByApp',
            version='2016-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            push_20160801_models.QueryPushStatByAppResponse(),
            self.call_api(params, req, runtime)
        )

    def query_push_stat_by_app(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_push_stat_by_app_with_options(request, runtime)

    def query_push_stat_by_msg_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_key):
            query['AppKey'] = request.app_key
        if not UtilClient.is_unset(request.message_id):
            query['MessageId'] = request.message_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryPushStatByMsg',
            version='2016-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            push_20160801_models.QueryPushStatByMsgResponse(),
            self.call_api(params, req, runtime)
        )

    def query_push_stat_by_msg(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_push_stat_by_msg_with_options(request, runtime)

    def query_tags_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_key):
            query['AppKey'] = request.app_key
        if not UtilClient.is_unset(request.client_key):
            query['ClientKey'] = request.client_key
        if not UtilClient.is_unset(request.key_type):
            query['KeyType'] = request.key_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryTags',
            version='2016-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            push_20160801_models.QueryTagsResponse(),
            self.call_api(params, req, runtime)
        )

    def query_tags(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_tags_with_options(request, runtime)

    def query_unique_device_stat_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_key):
            query['AppKey'] = request.app_key
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.granularity):
            query['Granularity'] = request.granularity
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryUniqueDeviceStat',
            version='2016-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            push_20160801_models.QueryUniqueDeviceStatResponse(),
            self.call_api(params, req, runtime)
        )

    def query_unique_device_stat(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_unique_device_stat_with_options(request, runtime)

    def remove_tag_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_key):
            query['AppKey'] = request.app_key
        if not UtilClient.is_unset(request.tag_name):
            query['TagName'] = request.tag_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemoveTag',
            version='2016-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            push_20160801_models.RemoveTagResponse(),
            self.call_api(params, req, runtime)
        )

    def remove_tag(self, request):
        runtime = util_models.RuntimeOptions()
        return self.remove_tag_with_options(request, runtime)

    def unbind_alias_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alias_name):
            query['AliasName'] = request.alias_name
        if not UtilClient.is_unset(request.app_key):
            query['AppKey'] = request.app_key
        if not UtilClient.is_unset(request.device_id):
            query['DeviceId'] = request.device_id
        if not UtilClient.is_unset(request.unbind_all):
            query['UnbindAll'] = request.unbind_all
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UnbindAlias',
            version='2016-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            push_20160801_models.UnbindAliasResponse(),
            self.call_api(params, req, runtime)
        )

    def unbind_alias(self, request):
        runtime = util_models.RuntimeOptions()
        return self.unbind_alias_with_options(request, runtime)

    def unbind_phone_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_key):
            query['AppKey'] = request.app_key
        if not UtilClient.is_unset(request.device_id):
            query['DeviceId'] = request.device_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UnbindPhone',
            version='2016-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            push_20160801_models.UnbindPhoneResponse(),
            self.call_api(params, req, runtime)
        )

    def unbind_phone(self, request):
        runtime = util_models.RuntimeOptions()
        return self.unbind_phone_with_options(request, runtime)

    def unbind_tag_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_key):
            query['AppKey'] = request.app_key
        if not UtilClient.is_unset(request.client_key):
            query['ClientKey'] = request.client_key
        if not UtilClient.is_unset(request.key_type):
            query['KeyType'] = request.key_type
        if not UtilClient.is_unset(request.tag_name):
            query['TagName'] = request.tag_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UnbindTag',
            version='2016-08-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            push_20160801_models.UnbindTagResponse(),
            self.call_api(params, req, runtime)
        )

    def unbind_tag(self, request):
        runtime = util_models.RuntimeOptions()
        return self.unbind_tag_with_options(request, runtime)
