# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_vs20181212 import models as vs_20181212_models
from alibabacloud_tea_util import models as util_models


class Client(OpenApiClient):
    """
    *\
    """
    def __init__(self, config):
        super(Client, self).__init__(config)
        self._endpoint_rule = 'regional'
        self.check_config(config)
        self._endpoint = self.get_endpoint('vs', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def add_device_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vs_20181212_models.AddDeviceResponse(),
            self.do_rpcrequest('AddDevice', '2018-12-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def add_device(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_device_with_options(request, runtime)

    def add_vs_pull_stream_info_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vs_20181212_models.AddVsPullStreamInfoConfigResponse(),
            self.do_rpcrequest('AddVsPullStreamInfoConfig', '2018-12-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def add_vs_pull_stream_info_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_vs_pull_stream_info_config_with_options(request, runtime)

    def batch_bind_directories_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vs_20181212_models.BatchBindDirectoriesResponse(),
            self.do_rpcrequest('BatchBindDirectories', '2018-12-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def batch_bind_directories(self, request):
        runtime = util_models.RuntimeOptions()
        return self.batch_bind_directories_with_options(request, runtime)

    def batch_bind_parent_platform_devices_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vs_20181212_models.BatchBindParentPlatformDevicesResponse(),
            self.do_rpcrequest('BatchBindParentPlatformDevices', '2018-12-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def batch_bind_parent_platform_devices(self, request):
        runtime = util_models.RuntimeOptions()
        return self.batch_bind_parent_platform_devices_with_options(request, runtime)

    def batch_bind_purchased_devices_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vs_20181212_models.BatchBindPurchasedDevicesResponse(),
            self.do_rpcrequest('BatchBindPurchasedDevices', '2018-12-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def batch_bind_purchased_devices(self, request):
        runtime = util_models.RuntimeOptions()
        return self.batch_bind_purchased_devices_with_options(request, runtime)

    def batch_bind_template_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vs_20181212_models.BatchBindTemplateResponse(),
            self.do_rpcrequest('BatchBindTemplate', '2018-12-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def batch_bind_template(self, request):
        runtime = util_models.RuntimeOptions()
        return self.batch_bind_template_with_options(request, runtime)

    def batch_bind_templates_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vs_20181212_models.BatchBindTemplatesResponse(),
            self.do_rpcrequest('BatchBindTemplates', '2018-12-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def batch_bind_templates(self, request):
        runtime = util_models.RuntimeOptions()
        return self.batch_bind_templates_with_options(request, runtime)

    def batch_delete_devices_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vs_20181212_models.BatchDeleteDevicesResponse(),
            self.do_rpcrequest('BatchDeleteDevices', '2018-12-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def batch_delete_devices(self, request):
        runtime = util_models.RuntimeOptions()
        return self.batch_delete_devices_with_options(request, runtime)

    def batch_delete_vs_domain_configs_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vs_20181212_models.BatchDeleteVsDomainConfigsResponse(),
            self.do_rpcrequest('BatchDeleteVsDomainConfigs', '2018-12-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def batch_delete_vs_domain_configs(self, request):
        runtime = util_models.RuntimeOptions()
        return self.batch_delete_vs_domain_configs_with_options(request, runtime)

    def batch_forbid_vs_stream_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vs_20181212_models.BatchForbidVsStreamResponse(),
            self.do_rpcrequest('BatchForbidVsStream', '2018-12-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def batch_forbid_vs_stream(self, request):
        runtime = util_models.RuntimeOptions()
        return self.batch_forbid_vs_stream_with_options(request, runtime)

    def batch_resume_vs_stream_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vs_20181212_models.BatchResumeVsStreamResponse(),
            self.do_rpcrequest('BatchResumeVsStream', '2018-12-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def batch_resume_vs_stream(self, request):
        runtime = util_models.RuntimeOptions()
        return self.batch_resume_vs_stream_with_options(request, runtime)

    def batch_set_vs_domain_configs_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vs_20181212_models.BatchSetVsDomainConfigsResponse(),
            self.do_rpcrequest('BatchSetVsDomainConfigs', '2018-12-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def batch_set_vs_domain_configs(self, request):
        runtime = util_models.RuntimeOptions()
        return self.batch_set_vs_domain_configs_with_options(request, runtime)

    def batch_start_devices_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vs_20181212_models.BatchStartDevicesResponse(),
            self.do_rpcrequest('BatchStartDevices', '2018-12-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def batch_start_devices(self, request):
        runtime = util_models.RuntimeOptions()
        return self.batch_start_devices_with_options(request, runtime)

    def batch_start_streams_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vs_20181212_models.BatchStartStreamsResponse(),
            self.do_rpcrequest('BatchStartStreams', '2018-12-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def batch_start_streams(self, request):
        runtime = util_models.RuntimeOptions()
        return self.batch_start_streams_with_options(request, runtime)

    def batch_stop_devices_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vs_20181212_models.BatchStopDevicesResponse(),
            self.do_rpcrequest('BatchStopDevices', '2018-12-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def batch_stop_devices(self, request):
        runtime = util_models.RuntimeOptions()
        return self.batch_stop_devices_with_options(request, runtime)

    def batch_stop_streams_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vs_20181212_models.BatchStopStreamsResponse(),
            self.do_rpcrequest('BatchStopStreams', '2018-12-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def batch_stop_streams(self, request):
        runtime = util_models.RuntimeOptions()
        return self.batch_stop_streams_with_options(request, runtime)

    def batch_unbind_directories_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vs_20181212_models.BatchUnbindDirectoriesResponse(),
            self.do_rpcrequest('BatchUnbindDirectories', '2018-12-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def batch_unbind_directories(self, request):
        runtime = util_models.RuntimeOptions()
        return self.batch_unbind_directories_with_options(request, runtime)

    def batch_unbind_parent_platform_devices_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vs_20181212_models.BatchUnbindParentPlatformDevicesResponse(),
            self.do_rpcrequest('BatchUnbindParentPlatformDevices', '2018-12-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def batch_unbind_parent_platform_devices(self, request):
        runtime = util_models.RuntimeOptions()
        return self.batch_unbind_parent_platform_devices_with_options(request, runtime)

    def batch_unbind_purchased_devices_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vs_20181212_models.BatchUnbindPurchasedDevicesResponse(),
            self.do_rpcrequest('BatchUnbindPurchasedDevices', '2018-12-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def batch_unbind_purchased_devices(self, request):
        runtime = util_models.RuntimeOptions()
        return self.batch_unbind_purchased_devices_with_options(request, runtime)

    def batch_unbind_template_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vs_20181212_models.BatchUnbindTemplateResponse(),
            self.do_rpcrequest('BatchUnbindTemplate', '2018-12-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def batch_unbind_template(self, request):
        runtime = util_models.RuntimeOptions()
        return self.batch_unbind_template_with_options(request, runtime)

    def batch_unbind_templates_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vs_20181212_models.BatchUnbindTemplatesResponse(),
            self.do_rpcrequest('BatchUnbindTemplates', '2018-12-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def batch_unbind_templates(self, request):
        runtime = util_models.RuntimeOptions()
        return self.batch_unbind_templates_with_options(request, runtime)

    def bind_directory_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vs_20181212_models.BindDirectoryResponse(),
            self.do_rpcrequest('BindDirectory', '2018-12-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def bind_directory(self, request):
        runtime = util_models.RuntimeOptions()
        return self.bind_directory_with_options(request, runtime)

    def bind_parent_platform_device_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vs_20181212_models.BindParentPlatformDeviceResponse(),
            self.do_rpcrequest('BindParentPlatformDevice', '2018-12-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def bind_parent_platform_device(self, request):
        runtime = util_models.RuntimeOptions()
        return self.bind_parent_platform_device_with_options(request, runtime)

    def bind_purchased_device_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vs_20181212_models.BindPurchasedDeviceResponse(),
            self.do_rpcrequest('BindPurchasedDevice', '2018-12-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def bind_purchased_device(self, request):
        runtime = util_models.RuntimeOptions()
        return self.bind_purchased_device_with_options(request, runtime)

    def bind_template_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vs_20181212_models.BindTemplateResponse(),
            self.do_rpcrequest('BindTemplate', '2018-12-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def bind_template(self, request):
        runtime = util_models.RuntimeOptions()
        return self.bind_template_with_options(request, runtime)

    def continuous_adjust_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vs_20181212_models.ContinuousAdjustResponse(),
            self.do_rpcrequest('ContinuousAdjust', '2018-12-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def continuous_adjust(self, request):
        runtime = util_models.RuntimeOptions()
        return self.continuous_adjust_with_options(request, runtime)

    def continuous_move_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vs_20181212_models.ContinuousMoveResponse(),
            self.do_rpcrequest('ContinuousMove', '2018-12-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def continuous_move(self, request):
        runtime = util_models.RuntimeOptions()
        return self.continuous_move_with_options(request, runtime)

    def create_device_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vs_20181212_models.CreateDeviceResponse(),
            self.do_rpcrequest('CreateDevice', '2018-12-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_device(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_device_with_options(request, runtime)

    def create_device_alarm_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vs_20181212_models.CreateDeviceAlarmResponse(),
            self.do_rpcrequest('CreateDeviceAlarm', '2018-12-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_device_alarm(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_device_alarm_with_options(request, runtime)

    def create_device_snapshot_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vs_20181212_models.CreateDeviceSnapshotResponse(),
            self.do_rpcrequest('CreateDeviceSnapshot', '2018-12-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_device_snapshot(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_device_snapshot_with_options(request, runtime)

    def create_directory_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vs_20181212_models.CreateDirectoryResponse(),
            self.do_rpcrequest('CreateDirectory', '2018-12-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_directory(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_directory_with_options(request, runtime)

    def create_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vs_20181212_models.CreateGroupResponse(),
            self.do_rpcrequest('CreateGroup', '2018-12-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_group_with_options(request, runtime)

    def create_parent_platform_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vs_20181212_models.CreateParentPlatformResponse(),
            self.do_rpcrequest('CreateParentPlatform', '2018-12-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_parent_platform(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_parent_platform_with_options(request, runtime)

    def create_stream_snapshot_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vs_20181212_models.CreateStreamSnapshotResponse(),
            self.do_rpcrequest('CreateStreamSnapshot', '2018-12-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_stream_snapshot(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_stream_snapshot_with_options(request, runtime)

    def create_template_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vs_20181212_models.CreateTemplateResponse(),
            self.do_rpcrequest('CreateTemplate', '2018-12-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_template(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_template_with_options(request, runtime)

    def delete_bucket_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vs_20181212_models.DeleteBucketResponse(),
            self.do_rpcrequest('DeleteBucket', '2018-12-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_bucket(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_bucket_with_options(request, runtime)

    def delete_device_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vs_20181212_models.DeleteDeviceResponse(),
            self.do_rpcrequest('DeleteDevice', '2018-12-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_device(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_device_with_options(request, runtime)

    def delete_directory_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vs_20181212_models.DeleteDirectoryResponse(),
            self.do_rpcrequest('DeleteDirectory', '2018-12-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_directory(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_directory_with_options(request, runtime)

    def delete_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vs_20181212_models.DeleteGroupResponse(),
            self.do_rpcrequest('DeleteGroup', '2018-12-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_group_with_options(request, runtime)

    def delete_parent_platform_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vs_20181212_models.DeleteParentPlatformResponse(),
            self.do_rpcrequest('DeleteParentPlatform', '2018-12-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_parent_platform(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_parent_platform_with_options(request, runtime)

    def delete_preset_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vs_20181212_models.DeletePresetResponse(),
            self.do_rpcrequest('DeletePreset', '2018-12-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_preset(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_preset_with_options(request, runtime)

    def delete_template_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vs_20181212_models.DeleteTemplateResponse(),
            self.do_rpcrequest('DeleteTemplate', '2018-12-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_template(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_template_with_options(request, runtime)

    def delete_vs_pull_stream_info_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vs_20181212_models.DeleteVsPullStreamInfoConfigResponse(),
            self.do_rpcrequest('DeleteVsPullStreamInfoConfig', '2018-12-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_vs_pull_stream_info_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_vs_pull_stream_info_config_with_options(request, runtime)

    def delete_vs_streams_notify_url_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vs_20181212_models.DeleteVsStreamsNotifyUrlConfigResponse(),
            self.do_rpcrequest('DeleteVsStreamsNotifyUrlConfig', '2018-12-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_vs_streams_notify_url_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_vs_streams_notify_url_config_with_options(request, runtime)

    def describe_account_stat_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vs_20181212_models.DescribeAccountStatResponse(),
            self.do_rpcrequest('DescribeAccountStat', '2018-12-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_account_stat(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_account_stat_with_options(request, runtime)

    def describe_device_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vs_20181212_models.DescribeDeviceResponse(),
            self.do_rpcrequest('DescribeDevice', '2018-12-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_device(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_device_with_options(request, runtime)

    def describe_device_channels_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vs_20181212_models.DescribeDeviceChannelsResponse(),
            self.do_rpcrequest('DescribeDeviceChannels', '2018-12-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_device_channels(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_device_channels_with_options(request, runtime)

    def describe_device_gateway_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vs_20181212_models.DescribeDeviceGatewayResponse(),
            self.do_rpcrequest('DescribeDeviceGateway', '2018-12-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_device_gateway(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_device_gateway_with_options(request, runtime)

    def describe_devices_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vs_20181212_models.DescribeDevicesResponse(),
            self.do_rpcrequest('DescribeDevices', '2018-12-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_devices(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_devices_with_options(request, runtime)

    def describe_device_urlwith_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vs_20181212_models.DescribeDeviceURLResponse(),
            self.do_rpcrequest('DescribeDeviceURL', '2018-12-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_device_url(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_device_urlwith_options(request, runtime)

    def describe_directories_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vs_20181212_models.DescribeDirectoriesResponse(),
            self.do_rpcrequest('DescribeDirectories', '2018-12-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_directories(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_directories_with_options(request, runtime)

    def describe_directory_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vs_20181212_models.DescribeDirectoryResponse(),
            self.do_rpcrequest('DescribeDirectory', '2018-12-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_directory(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_directory_with_options(request, runtime)

    def describe_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vs_20181212_models.DescribeGroupResponse(),
            self.do_rpcrequest('DescribeGroup', '2018-12-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_group_with_options(request, runtime)

    def describe_groups_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vs_20181212_models.DescribeGroupsResponse(),
            self.do_rpcrequest('DescribeGroups', '2018-12-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_groups(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_groups_with_options(request, runtime)

    def describe_parent_platform_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vs_20181212_models.DescribeParentPlatformResponse(),
            self.do_rpcrequest('DescribeParentPlatform', '2018-12-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_parent_platform(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_parent_platform_with_options(request, runtime)

    def describe_parent_platform_devices_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vs_20181212_models.DescribeParentPlatformDevicesResponse(),
            self.do_rpcrequest('DescribeParentPlatformDevices', '2018-12-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_parent_platform_devices(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_parent_platform_devices_with_options(request, runtime)

    def describe_parent_platforms_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vs_20181212_models.DescribeParentPlatformsResponse(),
            self.do_rpcrequest('DescribeParentPlatforms', '2018-12-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_parent_platforms(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_parent_platforms_with_options(request, runtime)

    def describe_presets_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vs_20181212_models.DescribePresetsResponse(),
            self.do_rpcrequest('DescribePresets', '2018-12-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_presets(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_presets_with_options(request, runtime)

    def describe_purchased_device_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vs_20181212_models.DescribePurchasedDeviceResponse(),
            self.do_rpcrequest('DescribePurchasedDevice', '2018-12-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_purchased_device(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_purchased_device_with_options(request, runtime)

    def describe_purchased_devices_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vs_20181212_models.DescribePurchasedDevicesResponse(),
            self.do_rpcrequest('DescribePurchasedDevices', '2018-12-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_purchased_devices(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_purchased_devices_with_options(request, runtime)

    def describe_records_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vs_20181212_models.DescribeRecordsResponse(),
            self.do_rpcrequest('DescribeRecords', '2018-12-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_records(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_records_with_options(request, runtime)

    def describe_stream_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vs_20181212_models.DescribeStreamResponse(),
            self.do_rpcrequest('DescribeStream', '2018-12-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_stream(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_stream_with_options(request, runtime)

    def describe_streams_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vs_20181212_models.DescribeStreamsResponse(),
            self.do_rpcrequest('DescribeStreams', '2018-12-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_streams(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_streams_with_options(request, runtime)

    def describe_stream_urlwith_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vs_20181212_models.DescribeStreamURLResponse(),
            self.do_rpcrequest('DescribeStreamURL', '2018-12-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_stream_url(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_stream_urlwith_options(request, runtime)

    def describe_stream_vod_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vs_20181212_models.DescribeStreamVodListResponse(),
            self.do_rpcrequest('DescribeStreamVodList', '2018-12-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_stream_vod_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_stream_vod_list_with_options(request, runtime)

    def describe_template_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vs_20181212_models.DescribeTemplateResponse(),
            self.do_rpcrequest('DescribeTemplate', '2018-12-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_template(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_template_with_options(request, runtime)

    def describe_templates_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vs_20181212_models.DescribeTemplatesResponse(),
            self.do_rpcrequest('DescribeTemplates', '2018-12-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_templates(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_templates_with_options(request, runtime)

    def describe_vod_stream_urlwith_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vs_20181212_models.DescribeVodStreamURLResponse(),
            self.do_rpcrequest('DescribeVodStreamURL', '2018-12-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_vod_stream_url(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_vod_stream_urlwith_options(request, runtime)

    def describe_vs_certificate_detail_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vs_20181212_models.DescribeVsCertificateDetailResponse(),
            self.do_rpcrequest('DescribeVsCertificateDetail', '2018-12-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_vs_certificate_detail(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_vs_certificate_detail_with_options(request, runtime)

    def describe_vs_certificate_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vs_20181212_models.DescribeVsCertificateListResponse(),
            self.do_rpcrequest('DescribeVsCertificateList', '2018-12-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_vs_certificate_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_vs_certificate_list_with_options(request, runtime)

    def describe_vs_domain_bps_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vs_20181212_models.DescribeVsDomainBpsDataResponse(),
            self.do_rpcrequest('DescribeVsDomainBpsData', '2018-12-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_vs_domain_bps_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_vs_domain_bps_data_with_options(request, runtime)

    def describe_vs_domain_certificate_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vs_20181212_models.DescribeVsDomainCertificateInfoResponse(),
            self.do_rpcrequest('DescribeVsDomainCertificateInfo', '2018-12-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_vs_domain_certificate_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_vs_domain_certificate_info_with_options(request, runtime)

    def describe_vs_domain_configs_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vs_20181212_models.DescribeVsDomainConfigsResponse(),
            self.do_rpcrequest('DescribeVsDomainConfigs', '2018-12-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_vs_domain_configs(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_vs_domain_configs_with_options(request, runtime)

    def describe_vs_domain_detail_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vs_20181212_models.DescribeVsDomainDetailResponse(),
            self.do_rpcrequest('DescribeVsDomainDetail', '2018-12-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_vs_domain_detail(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_vs_domain_detail_with_options(request, runtime)

    def describe_vs_domain_pv_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vs_20181212_models.DescribeVsDomainPvDataResponse(),
            self.do_rpcrequest('DescribeVsDomainPvData', '2018-12-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_vs_domain_pv_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_vs_domain_pv_data_with_options(request, runtime)

    def describe_vs_domain_pv_uv_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vs_20181212_models.DescribeVsDomainPvUvDataResponse(),
            self.do_rpcrequest('DescribeVsDomainPvUvData', '2018-12-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_vs_domain_pv_uv_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_vs_domain_pv_uv_data_with_options(request, runtime)

    def describe_vs_domain_record_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vs_20181212_models.DescribeVsDomainRecordDataResponse(),
            self.do_rpcrequest('DescribeVsDomainRecordData', '2018-12-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_vs_domain_record_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_vs_domain_record_data_with_options(request, runtime)

    def describe_vs_domain_region_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vs_20181212_models.DescribeVsDomainRegionDataResponse(),
            self.do_rpcrequest('DescribeVsDomainRegionData', '2018-12-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_vs_domain_region_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_vs_domain_region_data_with_options(request, runtime)

    def describe_vs_domain_req_bps_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vs_20181212_models.DescribeVsDomainReqBpsDataResponse(),
            self.do_rpcrequest('DescribeVsDomainReqBpsData', '2018-12-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_vs_domain_req_bps_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_vs_domain_req_bps_data_with_options(request, runtime)

    def describe_vs_domain_req_traffic_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vs_20181212_models.DescribeVsDomainReqTrafficDataResponse(),
            self.do_rpcrequest('DescribeVsDomainReqTrafficData', '2018-12-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_vs_domain_req_traffic_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_vs_domain_req_traffic_data_with_options(request, runtime)

    def describe_vs_domain_snapshot_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vs_20181212_models.DescribeVsDomainSnapshotDataResponse(),
            self.do_rpcrequest('DescribeVsDomainSnapshotData', '2018-12-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_vs_domain_snapshot_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_vs_domain_snapshot_data_with_options(request, runtime)

    def describe_vs_domain_traffic_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vs_20181212_models.DescribeVsDomainTrafficDataResponse(),
            self.do_rpcrequest('DescribeVsDomainTrafficData', '2018-12-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_vs_domain_traffic_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_vs_domain_traffic_data_with_options(request, runtime)

    def describe_vs_domain_uv_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vs_20181212_models.DescribeVsDomainUvDataResponse(),
            self.do_rpcrequest('DescribeVsDomainUvData', '2018-12-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_vs_domain_uv_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_vs_domain_uv_data_with_options(request, runtime)

    def describe_vs_pull_stream_info_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vs_20181212_models.DescribeVsPullStreamInfoConfigResponse(),
            self.do_rpcrequest('DescribeVsPullStreamInfoConfig', '2018-12-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_vs_pull_stream_info_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_vs_pull_stream_info_config_with_options(request, runtime)

    def describe_vs_storage_usage_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vs_20181212_models.DescribeVsStorageUsageDataResponse(),
            self.do_rpcrequest('DescribeVsStorageUsageData', '2018-12-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_vs_storage_usage_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_vs_storage_usage_data_with_options(request, runtime)

    def describe_vs_streams_notify_url_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vs_20181212_models.DescribeVsStreamsNotifyUrlConfigResponse(),
            self.do_rpcrequest('DescribeVsStreamsNotifyUrlConfig', '2018-12-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_vs_streams_notify_url_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_vs_streams_notify_url_config_with_options(request, runtime)

    def describe_vs_streams_online_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vs_20181212_models.DescribeVsStreamsOnlineListResponse(),
            self.do_rpcrequest('DescribeVsStreamsOnlineList', '2018-12-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_vs_streams_online_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_vs_streams_online_list_with_options(request, runtime)

    def describe_vs_streams_publish_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vs_20181212_models.DescribeVsStreamsPublishListResponse(),
            self.do_rpcrequest('DescribeVsStreamsPublishList', '2018-12-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_vs_streams_publish_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_vs_streams_publish_list_with_options(request, runtime)

    def describe_vs_top_domains_by_flow_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vs_20181212_models.DescribeVsTopDomainsByFlowResponse(),
            self.do_rpcrequest('DescribeVsTopDomainsByFlow', '2018-12-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_vs_top_domains_by_flow(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_vs_top_domains_by_flow_with_options(request, runtime)

    def describe_vs_up_peak_publish_stream_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vs_20181212_models.DescribeVsUpPeakPublishStreamDataResponse(),
            self.do_rpcrequest('DescribeVsUpPeakPublishStreamData', '2018-12-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_vs_up_peak_publish_stream_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_vs_up_peak_publish_stream_data_with_options(request, runtime)

    def describe_vs_user_resource_package_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vs_20181212_models.DescribeVsUserResourcePackageResponse(),
            self.do_rpcrequest('DescribeVsUserResourcePackage', '2018-12-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_vs_user_resource_package(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_vs_user_resource_package_with_options(request, runtime)

    def forbid_vs_stream_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vs_20181212_models.ForbidVsStreamResponse(),
            self.do_rpcrequest('ForbidVsStream', '2018-12-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def forbid_vs_stream(self, request):
        runtime = util_models.RuntimeOptions()
        return self.forbid_vs_stream_with_options(request, runtime)

    def get_bucket_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vs_20181212_models.GetBucketInfoResponse(),
            self.do_rpcrequest('GetBucketInfo', '2018-12-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_bucket_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_bucket_info_with_options(request, runtime)

    def goto_preset_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vs_20181212_models.GotoPresetResponse(),
            self.do_rpcrequest('GotoPreset', '2018-12-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def goto_preset(self, request):
        runtime = util_models.RuntimeOptions()
        return self.goto_preset_with_options(request, runtime)

    def list_buckets_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vs_20181212_models.ListBucketsResponse(),
            self.do_rpcrequest('ListBuckets', '2018-12-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_buckets(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_buckets_with_options(request, runtime)

    def list_device_channels_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vs_20181212_models.ListDeviceChannelsResponse(),
            self.do_rpcrequest('ListDeviceChannels', '2018-12-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_device_channels(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_device_channels_with_options(request, runtime)

    def list_device_records_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vs_20181212_models.ListDeviceRecordsResponse(),
            self.do_rpcrequest('ListDeviceRecords', '2018-12-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_device_records(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_device_records_with_options(request, runtime)

    def list_objects_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vs_20181212_models.ListObjectsResponse(),
            self.do_rpcrequest('ListObjects', '2018-12-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_objects(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_objects_with_options(request, runtime)

    def modify_device_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vs_20181212_models.ModifyDeviceResponse(),
            self.do_rpcrequest('ModifyDevice', '2018-12-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_device(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_device_with_options(request, runtime)

    def modify_device_alarm_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vs_20181212_models.ModifyDeviceAlarmResponse(),
            self.do_rpcrequest('ModifyDeviceAlarm', '2018-12-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_device_alarm(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_device_alarm_with_options(request, runtime)

    def modify_device_capture_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vs_20181212_models.ModifyDeviceCaptureResponse(),
            self.do_rpcrequest('ModifyDeviceCapture', '2018-12-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_device_capture(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_device_capture_with_options(request, runtime)

    def modify_device_channels_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vs_20181212_models.ModifyDeviceChannelsResponse(),
            self.do_rpcrequest('ModifyDeviceChannels', '2018-12-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_device_channels(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_device_channels_with_options(request, runtime)

    def modify_directory_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vs_20181212_models.ModifyDirectoryResponse(),
            self.do_rpcrequest('ModifyDirectory', '2018-12-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_directory(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_directory_with_options(request, runtime)

    def modify_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vs_20181212_models.ModifyGroupResponse(),
            self.do_rpcrequest('ModifyGroup', '2018-12-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_group_with_options(request, runtime)

    def modify_parent_platform_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vs_20181212_models.ModifyParentPlatformResponse(),
            self.do_rpcrequest('ModifyParentPlatform', '2018-12-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_parent_platform(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_parent_platform_with_options(request, runtime)

    def modify_template_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vs_20181212_models.ModifyTemplateResponse(),
            self.do_rpcrequest('ModifyTemplate', '2018-12-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_template(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_template_with_options(request, runtime)

    def open_vs_service_with_options(self, runtime):
        req = open_api_models.OpenApiRequest()
        return TeaCore.from_map(
            vs_20181212_models.OpenVsServiceResponse(),
            self.do_rpcrequest('OpenVsService', '2018-12-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def open_vs_service(self):
        runtime = util_models.RuntimeOptions()
        return self.open_vs_service_with_options(runtime)

    def prepare_upload_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vs_20181212_models.PrepareUploadResponse(),
            self.do_rpcrequest('PrepareUpload', '2018-12-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def prepare_upload(self, request):
        runtime = util_models.RuntimeOptions()
        return self.prepare_upload_with_options(request, runtime)

    def put_bucket_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vs_20181212_models.PutBucketResponse(),
            self.do_rpcrequest('PutBucket', '2018-12-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def put_bucket(self, request):
        runtime = util_models.RuntimeOptions()
        return self.put_bucket_with_options(request, runtime)

    def resume_vs_stream_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vs_20181212_models.ResumeVsStreamResponse(),
            self.do_rpcrequest('ResumeVsStream', '2018-12-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def resume_vs_stream(self, request):
        runtime = util_models.RuntimeOptions()
        return self.resume_vs_stream_with_options(request, runtime)

    def set_preset_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vs_20181212_models.SetPresetResponse(),
            self.do_rpcrequest('SetPreset', '2018-12-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def set_preset(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_preset_with_options(request, runtime)

    def set_vs_domain_certificate_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vs_20181212_models.SetVsDomainCertificateResponse(),
            self.do_rpcrequest('SetVsDomainCertificate', '2018-12-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def set_vs_domain_certificate(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_vs_domain_certificate_with_options(request, runtime)

    def set_vs_streams_notify_url_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vs_20181212_models.SetVsStreamsNotifyUrlConfigResponse(),
            self.do_rpcrequest('SetVsStreamsNotifyUrlConfig', '2018-12-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def set_vs_streams_notify_url_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_vs_streams_notify_url_config_with_options(request, runtime)

    def start_device_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vs_20181212_models.StartDeviceResponse(),
            self.do_rpcrequest('StartDevice', '2018-12-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def start_device(self, request):
        runtime = util_models.RuntimeOptions()
        return self.start_device_with_options(request, runtime)

    def start_parent_platform_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vs_20181212_models.StartParentPlatformResponse(),
            self.do_rpcrequest('StartParentPlatform', '2018-12-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def start_parent_platform(self, request):
        runtime = util_models.RuntimeOptions()
        return self.start_parent_platform_with_options(request, runtime)

    def start_record_stream_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vs_20181212_models.StartRecordStreamResponse(),
            self.do_rpcrequest('StartRecordStream', '2018-12-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def start_record_stream(self, request):
        runtime = util_models.RuntimeOptions()
        return self.start_record_stream_with_options(request, runtime)

    def start_stream_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vs_20181212_models.StartStreamResponse(),
            self.do_rpcrequest('StartStream', '2018-12-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def start_stream(self, request):
        runtime = util_models.RuntimeOptions()
        return self.start_stream_with_options(request, runtime)

    def start_transfer_stream_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vs_20181212_models.StartTransferStreamResponse(),
            self.do_rpcrequest('StartTransferStream', '2018-12-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def start_transfer_stream(self, request):
        runtime = util_models.RuntimeOptions()
        return self.start_transfer_stream_with_options(request, runtime)

    def stop_adjust_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vs_20181212_models.StopAdjustResponse(),
            self.do_rpcrequest('StopAdjust', '2018-12-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def stop_adjust(self, request):
        runtime = util_models.RuntimeOptions()
        return self.stop_adjust_with_options(request, runtime)

    def stop_device_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vs_20181212_models.StopDeviceResponse(),
            self.do_rpcrequest('StopDevice', '2018-12-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def stop_device(self, request):
        runtime = util_models.RuntimeOptions()
        return self.stop_device_with_options(request, runtime)

    def stop_move_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vs_20181212_models.StopMoveResponse(),
            self.do_rpcrequest('StopMove', '2018-12-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def stop_move(self, request):
        runtime = util_models.RuntimeOptions()
        return self.stop_move_with_options(request, runtime)

    def stop_record_stream_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vs_20181212_models.StopRecordStreamResponse(),
            self.do_rpcrequest('StopRecordStream', '2018-12-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def stop_record_stream(self, request):
        runtime = util_models.RuntimeOptions()
        return self.stop_record_stream_with_options(request, runtime)

    def stop_stream_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vs_20181212_models.StopStreamResponse(),
            self.do_rpcrequest('StopStream', '2018-12-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def stop_stream(self, request):
        runtime = util_models.RuntimeOptions()
        return self.stop_stream_with_options(request, runtime)

    def stop_transfer_stream_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vs_20181212_models.StopTransferStreamResponse(),
            self.do_rpcrequest('StopTransferStream', '2018-12-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def stop_transfer_stream(self, request):
        runtime = util_models.RuntimeOptions()
        return self.stop_transfer_stream_with_options(request, runtime)

    def sync_catalogs_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vs_20181212_models.SyncCatalogsResponse(),
            self.do_rpcrequest('SyncCatalogs', '2018-12-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def sync_catalogs(self, request):
        runtime = util_models.RuntimeOptions()
        return self.sync_catalogs_with_options(request, runtime)

    def sync_device_channels_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vs_20181212_models.SyncDeviceChannelsResponse(),
            self.do_rpcrequest('SyncDeviceChannels', '2018-12-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def sync_device_channels(self, request):
        runtime = util_models.RuntimeOptions()
        return self.sync_device_channels_with_options(request, runtime)

    def unbind_directory_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vs_20181212_models.UnbindDirectoryResponse(),
            self.do_rpcrequest('UnbindDirectory', '2018-12-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def unbind_directory(self, request):
        runtime = util_models.RuntimeOptions()
        return self.unbind_directory_with_options(request, runtime)

    def unbind_parent_platform_device_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vs_20181212_models.UnbindParentPlatformDeviceResponse(),
            self.do_rpcrequest('UnbindParentPlatformDevice', '2018-12-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def unbind_parent_platform_device(self, request):
        runtime = util_models.RuntimeOptions()
        return self.unbind_parent_platform_device_with_options(request, runtime)

    def unbind_purchased_device_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vs_20181212_models.UnbindPurchasedDeviceResponse(),
            self.do_rpcrequest('UnbindPurchasedDevice', '2018-12-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def unbind_purchased_device(self, request):
        runtime = util_models.RuntimeOptions()
        return self.unbind_purchased_device_with_options(request, runtime)

    def unbind_template_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vs_20181212_models.UnbindTemplateResponse(),
            self.do_rpcrequest('UnbindTemplate', '2018-12-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def unbind_template(self, request):
        runtime = util_models.RuntimeOptions()
        return self.unbind_template_with_options(request, runtime)

    def unlock_device_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vs_20181212_models.UnlockDeviceResponse(),
            self.do_rpcrequest('UnlockDevice', '2018-12-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def unlock_device(self, request):
        runtime = util_models.RuntimeOptions()
        return self.unlock_device_with_options(request, runtime)

    def update_bucket_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vs_20181212_models.UpdateBucketInfoResponse(),
            self.do_rpcrequest('UpdateBucketInfo', '2018-12-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_bucket_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_bucket_info_with_options(request, runtime)

    def update_vs_pull_stream_info_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vs_20181212_models.UpdateVsPullStreamInfoConfigResponse(),
            self.do_rpcrequest('UpdateVsPullStreamInfoConfig', '2018-12-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_vs_pull_stream_info_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_vs_pull_stream_info_config_with_options(request, runtime)

    def upload_device_record_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            vs_20181212_models.UploadDeviceRecordResponse(),
            self.do_rpcrequest('UploadDeviceRecord', '2018-12-12', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def upload_device_record(self, request):
        runtime = util_models.RuntimeOptions()
        return self.upload_device_record_with_options(request, runtime)
