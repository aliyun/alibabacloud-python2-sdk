# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_vdmeter20210425 import models as vdmeter_20210425_models
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
        self._endpoint = self.get_endpoint('vdmeter', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def describe_hu_ya_record_by_domain_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.business_type):
            query['BusinessType'] = request.business_type
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeHuYaRecordByDomain',
            version='2021-04-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vdmeter_20210425_models.DescribeHuYaRecordByDomainResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_hu_ya_record_by_domain(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_hu_ya_record_by_domain_with_options(request, runtime)

    def describe_hu_ya_screenshot_by_domain_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.business_type):
            query['BusinessType'] = request.business_type
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeHuYaScreenshotByDomain',
            version='2021-04-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vdmeter_20210425_models.DescribeHuYaScreenshotByDomainResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_hu_ya_screenshot_by_domain(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_hu_ya_screenshot_by_domain_with_options(request, runtime)

    def describe_hu_ya_transcode_by_domain_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.business_type):
            query['BusinessType'] = request.business_type
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeHuYaTranscodeByDomain',
            version='2021-04-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vdmeter_20210425_models.DescribeHuYaTranscodeByDomainResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_hu_ya_transcode_by_domain(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_hu_ya_transcode_by_domain_with_options(request, runtime)

    def describe_meter_bypass_rt_usage_by_task_profile_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.end_ts):
            query['EndTs'] = request.end_ts
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.service_area):
            query['ServiceArea'] = request.service_area
        if not UtilClient.is_unset(request.start_ts):
            query['StartTs'] = request.start_ts
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeMeterBypassRtUsageByTaskProfile',
            version='2021-04-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vdmeter_20210425_models.DescribeMeterBypassRtUsageByTaskProfileResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_meter_bypass_rt_usage_by_task_profile(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_meter_bypass_rt_usage_by_task_profile_with_options(request, runtime)

    def describe_meter_mpu_transcode_rt_usage_by_task_profile_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.end_ts):
            query['EndTs'] = request.end_ts
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.service_area):
            query['ServiceArea'] = request.service_area
        if not UtilClient.is_unset(request.start_ts):
            query['StartTs'] = request.start_ts
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeMeterMpuTranscodeRtUsageByTaskProfile',
            version='2021-04-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vdmeter_20210425_models.DescribeMeterMpuTranscodeRtUsageByTaskProfileResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_meter_mpu_transcode_rt_usage_by_task_profile(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_meter_mpu_transcode_rt_usage_by_task_profile_with_options(request, runtime)

    def describe_meter_record_rt_usage_by_task_profile_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.end_ts):
            query['EndTs'] = request.end_ts
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.service_area):
            query['ServiceArea'] = request.service_area
        if not UtilClient.is_unset(request.start_ts):
            query['StartTs'] = request.start_ts
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeMeterRecordRtUsageByTaskProfile',
            version='2021-04-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vdmeter_20210425_models.DescribeMeterRecordRtUsageByTaskProfileResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_meter_record_rt_usage_by_task_profile(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_meter_record_rt_usage_by_task_profile_with_options(request, runtime)

    def describe_meter_rtc_approx_peak_rate_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.end_ts):
            query['EndTs'] = request.end_ts
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.service_area):
            query['ServiceArea'] = request.service_area
        if not UtilClient.is_unset(request.start_ts):
            query['StartTs'] = request.start_ts
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeMeterRtcApproxPeakRate',
            version='2021-04-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vdmeter_20210425_models.DescribeMeterRtcApproxPeakRateResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_meter_rtc_approx_peak_rate(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_meter_rtc_approx_peak_rate_with_options(request, runtime)

    def describe_meter_rtc_channel_cnt_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.end_ts):
            query['EndTs'] = request.end_ts
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.service_area):
            query['ServiceArea'] = request.service_area
        if not UtilClient.is_unset(request.start_ts):
            query['StartTs'] = request.start_ts
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeMeterRtcChannelCntData',
            version='2021-04-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vdmeter_20210425_models.DescribeMeterRtcChannelCntDataResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_meter_rtc_channel_cnt_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_meter_rtc_channel_cnt_data_with_options(request, runtime)

    def describe_meter_rtc_duration_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.end_ts):
            query['EndTs'] = request.end_ts
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.service_area):
            query['ServiceArea'] = request.service_area
        if not UtilClient.is_unset(request.start_ts):
            query['StartTs'] = request.start_ts
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeMeterRtcDuration',
            version='2021-04-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vdmeter_20210425_models.DescribeMeterRtcDurationResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_meter_rtc_duration(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_meter_rtc_duration_with_options(request, runtime)

    def describe_meter_rtc_peak_channel_cnt_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.end_ts):
            query['EndTs'] = request.end_ts
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.service_area):
            query['ServiceArea'] = request.service_area
        if not UtilClient.is_unset(request.start_ts):
            query['StartTs'] = request.start_ts
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeMeterRtcPeakChannelCntData',
            version='2021-04-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vdmeter_20210425_models.DescribeMeterRtcPeakChannelCntDataResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_meter_rtc_peak_channel_cnt_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_meter_rtc_peak_channel_cnt_data_with_options(request, runtime)

    def describe_meter_rtc_peak_user_cnt_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.end_ts):
            query['EndTs'] = request.end_ts
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.service_area):
            query['ServiceArea'] = request.service_area
        if not UtilClient.is_unset(request.start_ts):
            query['StartTs'] = request.start_ts
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeMeterRtcPeakUserCntData',
            version='2021-04-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vdmeter_20210425_models.DescribeMeterRtcPeakUserCntDataResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_meter_rtc_peak_user_cnt_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_meter_rtc_peak_user_cnt_data_with_options(request, runtime)

    def describe_meter_rtc_rt_band_width_usage_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.end_ts):
            query['EndTs'] = request.end_ts
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.service_area):
            query['ServiceArea'] = request.service_area
        if not UtilClient.is_unset(request.start_ts):
            query['StartTs'] = request.start_ts
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeMeterRtcRtBandWidthUsage',
            version='2021-04-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vdmeter_20210425_models.DescribeMeterRtcRtBandWidthUsageResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_meter_rtc_rt_band_width_usage(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_meter_rtc_rt_band_width_usage_with_options(request, runtime)

    def describe_meter_rtc_rt_flow_usage_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.end_ts):
            query['EndTs'] = request.end_ts
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.service_area):
            query['ServiceArea'] = request.service_area
        if not UtilClient.is_unset(request.start_ts):
            query['StartTs'] = request.start_ts
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeMeterRtcRtFlowUsage',
            version='2021-04-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vdmeter_20210425_models.DescribeMeterRtcRtFlowUsageResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_meter_rtc_rt_flow_usage(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_meter_rtc_rt_flow_usage_with_options(request, runtime)

    def describe_meter_rtc_user_cnt_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.end_ts):
            query['EndTs'] = request.end_ts
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.service_area):
            query['ServiceArea'] = request.service_area
        if not UtilClient.is_unset(request.start_ts):
            query['StartTs'] = request.start_ts
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeMeterRtcUserCntData',
            version='2021-04-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vdmeter_20210425_models.DescribeMeterRtcUserCntDataResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_meter_rtc_user_cnt_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_meter_rtc_user_cnt_data_with_options(request, runtime)

    def describe_new_play_video_play_session_event_detail_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_date):
            query['BizDate'] = request.biz_date
        if not UtilClient.is_unset(request.input_status):
            query['InputStatus'] = request.input_status
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.vps):
            query['VPS'] = request.vps
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeNewPlayVideoPlaySessionEventDetail',
            version='2021-04-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vdmeter_20210425_models.DescribeNewPlayVideoPlaySessionEventDetailResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_new_play_video_play_session_event_detail(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_new_play_video_play_session_event_detail_with_options(request, runtime)

    def describe_new_play_video_play_session_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time_stamp):
            query['EndTimeStamp'] = request.end_time_stamp
        if not UtilClient.is_unset(request.input_status):
            query['InputStatus'] = request.input_status
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.start_time_stamp):
            query['StartTimeStamp'] = request.start_time_stamp
        if not UtilClient.is_unset(request.unique_id):
            query['UniqueId'] = request.unique_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeNewPlayVideoPlaySessionList',
            version='2021-04-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vdmeter_20210425_models.DescribeNewPlayVideoPlaySessionListResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_new_play_video_play_session_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_new_play_video_play_session_list_with_options(request, runtime)

    def describe_new_play_video_play_sessioninfo_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.vps):
            query['VPS'] = request.vps
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeNewPlayVideoPlaySessioninfo',
            version='2021-04-25',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vdmeter_20210425_models.DescribeNewPlayVideoPlaySessioninfoResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_new_play_video_play_sessioninfo(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_new_play_video_play_sessioninfo_with_options(request, runtime)
