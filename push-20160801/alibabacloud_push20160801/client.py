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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            push_20160801_models.BindAliasResponse(),
            self.do_rpcrequest('BindAlias', '2016-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def bind_alias(self, request):
        runtime = util_models.RuntimeOptions()
        return self.bind_alias_with_options(request, runtime)

    def bind_phone_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            push_20160801_models.BindPhoneResponse(),
            self.do_rpcrequest('BindPhone', '2016-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def bind_phone(self, request):
        runtime = util_models.RuntimeOptions()
        return self.bind_phone_with_options(request, runtime)

    def bind_tag_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            push_20160801_models.BindTagResponse(),
            self.do_rpcrequest('BindTag', '2016-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def bind_tag(self, request):
        runtime = util_models.RuntimeOptions()
        return self.bind_tag_with_options(request, runtime)

    def cancel_push_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            push_20160801_models.CancelPushResponse(),
            self.do_rpcrequest('CancelPush', '2016-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def cancel_push(self, request):
        runtime = util_models.RuntimeOptions()
        return self.cancel_push_with_options(request, runtime)

    def check_certificate_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            push_20160801_models.CheckCertificateResponse(),
            self.do_rpcrequest('CheckCertificate', '2016-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def check_certificate(self, request):
        runtime = util_models.RuntimeOptions()
        return self.check_certificate_with_options(request, runtime)

    def check_device_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            push_20160801_models.CheckDeviceResponse(),
            self.do_rpcrequest('CheckDevice', '2016-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def check_device(self, request):
        runtime = util_models.RuntimeOptions()
        return self.check_device_with_options(request, runtime)

    def check_devices_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            push_20160801_models.CheckDevicesResponse(),
            self.do_rpcrequest('CheckDevices', '2016-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def check_devices(self, request):
        runtime = util_models.RuntimeOptions()
        return self.check_devices_with_options(request, runtime)

    def complete_continuously_push_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            push_20160801_models.CompleteContinuouslyPushResponse(),
            self.do_rpcrequest('CompleteContinuouslyPush', '2016-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def complete_continuously_push(self, request):
        runtime = util_models.RuntimeOptions()
        return self.complete_continuously_push_with_options(request, runtime)

    def continuously_push_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            push_20160801_models.ContinuouslyPushResponse(),
            self.do_rpcrequest('ContinuouslyPush', '2016-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def continuously_push(self, request):
        runtime = util_models.RuntimeOptions()
        return self.continuously_push_with_options(request, runtime)

    def list_summary_apps_with_options(self, runtime):
        req = open_api_models.OpenApiRequest()
        return TeaCore.from_map(
            push_20160801_models.ListSummaryAppsResponse(),
            self.do_rpcrequest('ListSummaryApps', '2016-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_summary_apps(self):
        runtime = util_models.RuntimeOptions()
        return self.list_summary_apps_with_options(runtime)

    def list_tags_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            push_20160801_models.ListTagsResponse(),
            self.do_rpcrequest('ListTags', '2016-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_tags(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_tags_with_options(request, runtime)

    def mass_push_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            push_20160801_models.MassPushResponse(),
            self.do_rpcrequest('MassPush', '2016-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def mass_push(self, request):
        runtime = util_models.RuntimeOptions()
        return self.mass_push_with_options(request, runtime)

    def push_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            push_20160801_models.PushResponse(),
            self.do_rpcrequest('Push', '2016-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def push(self, request):
        runtime = util_models.RuntimeOptions()
        return self.push_with_options(request, runtime)

    def push_message_to_android_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            push_20160801_models.PushMessageToAndroidResponse(),
            self.do_rpcrequest('PushMessageToAndroid', '2016-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def push_message_to_android(self, request):
        runtime = util_models.RuntimeOptions()
        return self.push_message_to_android_with_options(request, runtime)

    def push_message_toi_oswith_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            push_20160801_models.PushMessageToiOSResponse(),
            self.do_rpcrequest('PushMessageToiOS', '2016-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def push_message_toi_os(self, request):
        runtime = util_models.RuntimeOptions()
        return self.push_message_toi_oswith_options(request, runtime)

    def push_notice_to_android_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            push_20160801_models.PushNoticeToAndroidResponse(),
            self.do_rpcrequest('PushNoticeToAndroid', '2016-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def push_notice_to_android(self, request):
        runtime = util_models.RuntimeOptions()
        return self.push_notice_to_android_with_options(request, runtime)

    def push_notice_toi_oswith_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            push_20160801_models.PushNoticeToiOSResponse(),
            self.do_rpcrequest('PushNoticeToiOS', '2016-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def push_notice_toi_os(self, request):
        runtime = util_models.RuntimeOptions()
        return self.push_notice_toi_oswith_options(request, runtime)

    def query_aliases_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            push_20160801_models.QueryAliasesResponse(),
            self.do_rpcrequest('QueryAliases', '2016-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_aliases(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_aliases_with_options(request, runtime)

    def query_device_count_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            push_20160801_models.QueryDeviceCountResponse(),
            self.do_rpcrequest('QueryDeviceCount', '2016-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_device_count(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_device_count_with_options(request, runtime)

    def query_device_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            push_20160801_models.QueryDeviceInfoResponse(),
            self.do_rpcrequest('QueryDeviceInfo', '2016-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_device_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_device_info_with_options(request, runtime)

    def query_devices_by_account_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            push_20160801_models.QueryDevicesByAccountResponse(),
            self.do_rpcrequest('QueryDevicesByAccount', '2016-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_devices_by_account(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_devices_by_account_with_options(request, runtime)

    def query_devices_by_alias_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            push_20160801_models.QueryDevicesByAliasResponse(),
            self.do_rpcrequest('QueryDevicesByAlias', '2016-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_devices_by_alias(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_devices_by_alias_with_options(request, runtime)

    def query_device_stat_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            push_20160801_models.QueryDeviceStatResponse(),
            self.do_rpcrequest('QueryDeviceStat', '2016-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_device_stat(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_device_stat_with_options(request, runtime)

    def query_push_records_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            push_20160801_models.QueryPushRecordsResponse(),
            self.do_rpcrequest('QueryPushRecords', '2016-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_push_records(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_push_records_with_options(request, runtime)

    def query_push_stat_by_app_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            push_20160801_models.QueryPushStatByAppResponse(),
            self.do_rpcrequest('QueryPushStatByApp', '2016-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_push_stat_by_app(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_push_stat_by_app_with_options(request, runtime)

    def query_push_stat_by_msg_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            push_20160801_models.QueryPushStatByMsgResponse(),
            self.do_rpcrequest('QueryPushStatByMsg', '2016-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_push_stat_by_msg(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_push_stat_by_msg_with_options(request, runtime)

    def query_tags_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            push_20160801_models.QueryTagsResponse(),
            self.do_rpcrequest('QueryTags', '2016-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_tags(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_tags_with_options(request, runtime)

    def query_unique_device_stat_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            push_20160801_models.QueryUniqueDeviceStatResponse(),
            self.do_rpcrequest('QueryUniqueDeviceStat', '2016-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_unique_device_stat(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_unique_device_stat_with_options(request, runtime)

    def remove_tag_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            push_20160801_models.RemoveTagResponse(),
            self.do_rpcrequest('RemoveTag', '2016-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def remove_tag(self, request):
        runtime = util_models.RuntimeOptions()
        return self.remove_tag_with_options(request, runtime)

    def unbind_alias_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            push_20160801_models.UnbindAliasResponse(),
            self.do_rpcrequest('UnbindAlias', '2016-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def unbind_alias(self, request):
        runtime = util_models.RuntimeOptions()
        return self.unbind_alias_with_options(request, runtime)

    def unbind_phone_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            push_20160801_models.UnbindPhoneResponse(),
            self.do_rpcrequest('UnbindPhone', '2016-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def unbind_phone(self, request):
        runtime = util_models.RuntimeOptions()
        return self.unbind_phone_with_options(request, runtime)

    def unbind_tag_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            push_20160801_models.UnbindTagResponse(),
            self.do_rpcrequest('UnbindTag', '2016-08-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def unbind_tag(self, request):
        runtime = util_models.RuntimeOptions()
        return self.unbind_tag_with_options(request, runtime)
