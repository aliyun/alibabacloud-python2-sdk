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
from alibabacloud_openapi_util.client import Client as OpenApiUtilClient


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
        query = {}
        if not UtilClient.is_unset(request.config):
            query['Config'] = request.config
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.protocol):
            query['Protocol'] = request.protocol
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddDevice',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.AddDeviceResponse(),
            self.call_api(params, req, runtime)
        )

    def add_device(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_device_with_options(request, runtime)

    def add_registered_device_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dsn):
            query['Dsn'] = request.dsn
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.register_code):
            query['RegisterCode'] = request.register_code
        if not UtilClient.is_unset(request.secret_key):
            query['SecretKey'] = request.secret_key
        if not UtilClient.is_unset(request.vendor):
            query['Vendor'] = request.vendor
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddRegisteredDevice',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.AddRegisteredDeviceResponse(),
            self.call_api(params, req, runtime)
        )

    def add_registered_device(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_registered_device_with_options(request, runtime)

    def add_registered_vendor_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddRegisteredVendor',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.AddRegisteredVendorResponse(),
            self.call_api(params, req, runtime)
        )

    def add_registered_vendor(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_registered_vendor_with_options(request, runtime)

    def add_rendering_device_internet_ports_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.isp):
            query['ISP'] = request.isp
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not UtilClient.is_unset(request.internal_port):
            query['InternalPort'] = request.internal_port
        if not UtilClient.is_unset(request.ip_protocol):
            query['IpProtocol'] = request.ip_protocol
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddRenderingDeviceInternetPorts',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.AddRenderingDeviceInternetPortsResponse(),
            self.call_api(params, req, runtime)
        )

    def add_rendering_device_internet_ports(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_rendering_device_internet_ports_with_options(request, runtime)

    def add_vs_pull_stream_info_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.always):
            query['Always'] = request.always
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
            action='AddVsPullStreamInfoConfig',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.AddVsPullStreamInfoConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def add_vs_pull_stream_info_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_vs_pull_stream_info_config_with_options(request, runtime)

    def batch_bind_directories_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.device_id):
            query['DeviceId'] = request.device_id
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BatchBindDirectories',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.BatchBindDirectoriesResponse(),
            self.call_api(params, req, runtime)
        )

    def batch_bind_directories(self, request):
        runtime = util_models.RuntimeOptions()
        return self.batch_bind_directories_with_options(request, runtime)

    def batch_bind_parent_platform_devices_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.device_id):
            query['DeviceId'] = request.device_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.parent_platform_id):
            query['ParentPlatformId'] = request.parent_platform_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BatchBindParentPlatformDevices',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.BatchBindParentPlatformDevicesResponse(),
            self.call_api(params, req, runtime)
        )

    def batch_bind_parent_platform_devices(self, request):
        runtime = util_models.RuntimeOptions()
        return self.batch_bind_parent_platform_devices_with_options(request, runtime)

    def batch_bind_purchased_devices_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.device_id):
            query['DeviceId'] = request.device_id
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BatchBindPurchasedDevices',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.BatchBindPurchasedDevicesResponse(),
            self.call_api(params, req, runtime)
        )

    def batch_bind_purchased_devices(self, request):
        runtime = util_models.RuntimeOptions()
        return self.batch_bind_purchased_devices_with_options(request, runtime)

    def batch_bind_template_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.apply_all):
            query['ApplyAll'] = request.apply_all
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.replace):
            query['Replace'] = request.replace
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BatchBindTemplate',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.BatchBindTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    def batch_bind_template(self, request):
        runtime = util_models.RuntimeOptions()
        return self.batch_bind_template_with_options(request, runtime)

    def batch_bind_templates_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.apply_all):
            query['ApplyAll'] = request.apply_all
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.replace):
            query['Replace'] = request.replace
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        if not UtilClient.is_unset(request.template_type):
            query['TemplateType'] = request.template_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BatchBindTemplates',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.BatchBindTemplatesResponse(),
            self.call_api(params, req, runtime)
        )

    def batch_bind_templates(self, request):
        runtime = util_models.RuntimeOptions()
        return self.batch_bind_templates_with_options(request, runtime)

    def batch_delete_devices_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BatchDeleteDevices',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.BatchDeleteDevicesResponse(),
            self.call_api(params, req, runtime)
        )

    def batch_delete_devices(self, request):
        runtime = util_models.RuntimeOptions()
        return self.batch_delete_devices_with_options(request, runtime)

    def batch_delete_vs_domain_configs_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_names):
            query['DomainNames'] = request.domain_names
        if not UtilClient.is_unset(request.function_names):
            query['FunctionNames'] = request.function_names
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BatchDeleteVsDomainConfigs',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.BatchDeleteVsDomainConfigsResponse(),
            self.call_api(params, req, runtime)
        )

    def batch_delete_vs_domain_configs(self, request):
        runtime = util_models.RuntimeOptions()
        return self.batch_delete_vs_domain_configs_with_options(request, runtime)

    def batch_forbid_vs_stream_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.channel):
            query['Channel'] = request.channel
        if not UtilClient.is_unset(request.control_stream_action):
            query['ControlStreamAction'] = request.control_stream_action
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
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BatchForbidVsStream',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.BatchForbidVsStreamResponse(),
            self.call_api(params, req, runtime)
        )

    def batch_forbid_vs_stream(self, request):
        runtime = util_models.RuntimeOptions()
        return self.batch_forbid_vs_stream_with_options(request, runtime)

    def batch_resume_vs_stream_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.channel):
            query['Channel'] = request.channel
        if not UtilClient.is_unset(request.control_stream_action):
            query['ControlStreamAction'] = request.control_stream_action
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.live_stream_type):
            query['LiveStreamType'] = request.live_stream_type
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BatchResumeVsStream',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.BatchResumeVsStreamResponse(),
            self.call_api(params, req, runtime)
        )

    def batch_resume_vs_stream(self, request):
        runtime = util_models.RuntimeOptions()
        return self.batch_resume_vs_stream_with_options(request, runtime)

    def batch_set_vs_domain_configs_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_names):
            query['DomainNames'] = request.domain_names
        if not UtilClient.is_unset(request.functions):
            query['Functions'] = request.functions
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BatchSetVsDomainConfigs',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.BatchSetVsDomainConfigsResponse(),
            self.call_api(params, req, runtime)
        )

    def batch_set_vs_domain_configs(self, request):
        runtime = util_models.RuntimeOptions()
        return self.batch_set_vs_domain_configs_with_options(request, runtime)

    def batch_start_devices_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BatchStartDevices',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.BatchStartDevicesResponse(),
            self.call_api(params, req, runtime)
        )

    def batch_start_devices(self, request):
        runtime = util_models.RuntimeOptions()
        return self.batch_start_devices_with_options(request, runtime)

    def batch_start_streams_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BatchStartStreams',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.BatchStartStreamsResponse(),
            self.call_api(params, req, runtime)
        )

    def batch_start_streams(self, request):
        runtime = util_models.RuntimeOptions()
        return self.batch_start_streams_with_options(request, runtime)

    def batch_stop_devices_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BatchStopDevices',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.BatchStopDevicesResponse(),
            self.call_api(params, req, runtime)
        )

    def batch_stop_devices(self, request):
        runtime = util_models.RuntimeOptions()
        return self.batch_stop_devices_with_options(request, runtime)

    def batch_stop_streams_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BatchStopStreams',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.BatchStopStreamsResponse(),
            self.call_api(params, req, runtime)
        )

    def batch_stop_streams(self, request):
        runtime = util_models.RuntimeOptions()
        return self.batch_stop_streams_with_options(request, runtime)

    def batch_unbind_directories_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.device_id):
            query['DeviceId'] = request.device_id
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BatchUnbindDirectories',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.BatchUnbindDirectoriesResponse(),
            self.call_api(params, req, runtime)
        )

    def batch_unbind_directories(self, request):
        runtime = util_models.RuntimeOptions()
        return self.batch_unbind_directories_with_options(request, runtime)

    def batch_unbind_parent_platform_devices_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.device_id):
            query['DeviceId'] = request.device_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.parent_platform_id):
            query['ParentPlatformId'] = request.parent_platform_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BatchUnbindParentPlatformDevices',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.BatchUnbindParentPlatformDevicesResponse(),
            self.call_api(params, req, runtime)
        )

    def batch_unbind_parent_platform_devices(self, request):
        runtime = util_models.RuntimeOptions()
        return self.batch_unbind_parent_platform_devices_with_options(request, runtime)

    def batch_unbind_purchased_devices_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.device_id):
            query['DeviceId'] = request.device_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BatchUnbindPurchasedDevices',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.BatchUnbindPurchasedDevicesResponse(),
            self.call_api(params, req, runtime)
        )

    def batch_unbind_purchased_devices(self, request):
        runtime = util_models.RuntimeOptions()
        return self.batch_unbind_purchased_devices_with_options(request, runtime)

    def batch_unbind_template_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        if not UtilClient.is_unset(request.template_type):
            query['TemplateType'] = request.template_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BatchUnbindTemplate',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.BatchUnbindTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    def batch_unbind_template(self, request):
        runtime = util_models.RuntimeOptions()
        return self.batch_unbind_template_with_options(request, runtime)

    def batch_unbind_templates_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        if not UtilClient.is_unset(request.template_type):
            query['TemplateType'] = request.template_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BatchUnbindTemplates',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.BatchUnbindTemplatesResponse(),
            self.call_api(params, req, runtime)
        )

    def batch_unbind_templates(self, request):
        runtime = util_models.RuntimeOptions()
        return self.batch_unbind_templates_with_options(request, runtime)

    def bind_directory_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.device_id):
            query['DeviceId'] = request.device_id
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BindDirectory',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.BindDirectoryResponse(),
            self.call_api(params, req, runtime)
        )

    def bind_directory(self, request):
        runtime = util_models.RuntimeOptions()
        return self.bind_directory_with_options(request, runtime)

    def bind_parent_platform_device_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.device_id):
            query['DeviceId'] = request.device_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.parent_platform_id):
            query['ParentPlatformId'] = request.parent_platform_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BindParentPlatformDevice',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.BindParentPlatformDeviceResponse(),
            self.call_api(params, req, runtime)
        )

    def bind_parent_platform_device(self, request):
        runtime = util_models.RuntimeOptions()
        return self.bind_parent_platform_device_with_options(request, runtime)

    def bind_purchased_device_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.device_id):
            query['DeviceId'] = request.device_id
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BindPurchasedDevice',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.BindPurchasedDeviceResponse(),
            self.call_api(params, req, runtime)
        )

    def bind_purchased_device(self, request):
        runtime = util_models.RuntimeOptions()
        return self.bind_purchased_device_with_options(request, runtime)

    def bind_template_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.apply_all):
            query['ApplyAll'] = request.apply_all
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.replace):
            query['Replace'] = request.replace
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        if not UtilClient.is_unset(request.template_type):
            query['TemplateType'] = request.template_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BindTemplate',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.BindTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    def bind_template(self, request):
        runtime = util_models.RuntimeOptions()
        return self.bind_template_with_options(request, runtime)

    def capture_device_snapshot_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.device_id):
            query['DeviceId'] = request.device_id
        if not UtilClient.is_unset(request.mode):
            query['Mode'] = request.mode
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.snapshot_config):
            query['SnapshotConfig'] = request.snapshot_config
        if not UtilClient.is_unset(request.stream_id):
            query['StreamId'] = request.stream_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CaptureDeviceSnapshot',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.CaptureDeviceSnapshotResponse(),
            self.call_api(params, req, runtime)
        )

    def capture_device_snapshot(self, request):
        runtime = util_models.RuntimeOptions()
        return self.capture_device_snapshot_with_options(request, runtime)

    def continuous_adjust_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.focus):
            query['Focus'] = request.focus
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.iris):
            query['Iris'] = request.iris
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ContinuousAdjust',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.ContinuousAdjustResponse(),
            self.call_api(params, req, runtime)
        )

    def continuous_adjust(self, request):
        runtime = util_models.RuntimeOptions()
        return self.continuous_adjust_with_options(request, runtime)

    def continuous_move_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.pan):
            query['Pan'] = request.pan
        if not UtilClient.is_unset(request.tilt):
            query['Tilt'] = request.tilt
        if not UtilClient.is_unset(request.zoom):
            query['Zoom'] = request.zoom
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ContinuousMove',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.ContinuousMoveResponse(),
            self.call_api(params, req, runtime)
        )

    def continuous_move(self, request):
        runtime = util_models.RuntimeOptions()
        return self.continuous_move_with_options(request, runtime)

    def create_aiconfig_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.capture_interval):
            query['CaptureInterval'] = request.capture_interval
        if not UtilClient.is_unset(request.configs):
            query['Configs'] = request.configs
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.features):
            query['Features'] = request.features
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateAIConfig',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.CreateAIConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def create_aiconfig(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_aiconfig_with_options(request, runtime)

    def create_cluster_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.internal_ports):
            query['InternalPorts'] = request.internal_ports
        if not UtilClient.is_unset(request.maintain_time):
            query['MaintainTime'] = request.maintain_time
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.security_group_id):
            query['SecurityGroupId'] = request.security_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateCluster',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.CreateClusterResponse(),
            self.call_api(params, req, runtime)
        )

    def create_cluster(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_cluster_with_options(request, runtime)

    def create_device_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alarm_method):
            query['AlarmMethod'] = request.alarm_method
        if not UtilClient.is_unset(request.auto_pos):
            query['AutoPos'] = request.auto_pos
        if not UtilClient.is_unset(request.auto_start):
            query['AutoStart'] = request.auto_start
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not UtilClient.is_unset(request.dsn):
            query['Dsn'] = request.dsn
        if not UtilClient.is_unset(request.gb_id):
            query['GbId'] = request.gb_id
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.ip):
            query['Ip'] = request.ip
        if not UtilClient.is_unset(request.latitude):
            query['Latitude'] = request.latitude
        if not UtilClient.is_unset(request.longitude):
            query['Longitude'] = request.longitude
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.params):
            query['Params'] = request.params
        if not UtilClient.is_unset(request.parent_id):
            query['ParentId'] = request.parent_id
        if not UtilClient.is_unset(request.password):
            query['Password'] = request.password
        if not UtilClient.is_unset(request.port):
            query['Port'] = request.port
        if not UtilClient.is_unset(request.pos_interval):
            query['PosInterval'] = request.pos_interval
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        if not UtilClient.is_unset(request.username):
            query['Username'] = request.username
        if not UtilClient.is_unset(request.vendor):
            query['Vendor'] = request.vendor
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDevice',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.CreateDeviceResponse(),
            self.call_api(params, req, runtime)
        )

    def create_device(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_device_with_options(request, runtime)

    def create_device_alarm_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alarm):
            query['Alarm'] = request.alarm
        if not UtilClient.is_unset(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.expire):
            query['Expire'] = request.expire
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.object_type):
            query['ObjectType'] = request.object_type
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.sub_alarm):
            query['SubAlarm'] = request.sub_alarm
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDeviceAlarm',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.CreateDeviceAlarmResponse(),
            self.call_api(params, req, runtime)
        )

    def create_device_alarm(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_device_alarm_with_options(request, runtime)

    def create_device_snapshot_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.device_id):
            query['DeviceId'] = request.device_id
        if not UtilClient.is_unset(request.mode):
            query['Mode'] = request.mode
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.snapshot_config):
            query['SnapshotConfig'] = request.snapshot_config
        if not UtilClient.is_unset(request.stream_id):
            query['StreamId'] = request.stream_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDeviceSnapshot',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.CreateDeviceSnapshotResponse(),
            self.call_api(params, req, runtime)
        )

    def create_device_snapshot(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_device_snapshot_with_options(request, runtime)

    def create_directory_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.parent_id):
            query['ParentId'] = request.parent_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDirectory',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.CreateDirectoryResponse(),
            self.call_api(params, req, runtime)
        )

    def create_directory(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_directory_with_options(request, runtime)

    def create_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app):
            query['App'] = request.app
        if not UtilClient.is_unset(request.callback):
            query['Callback'] = request.callback
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.in_protocol):
            query['InProtocol'] = request.in_protocol
        if not UtilClient.is_unset(request.lazy_pull):
            query['LazyPull'] = request.lazy_pull
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.out_protocol):
            query['OutProtocol'] = request.out_protocol
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.play_domain):
            query['PlayDomain'] = request.play_domain
        if not UtilClient.is_unset(request.push_domain):
            query['PushDomain'] = request.push_domain
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateGroup',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.CreateGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def create_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_group_with_options(request, runtime)

    def create_parent_platform_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_start):
            query['AutoStart'] = request.auto_start
        if not UtilClient.is_unset(request.client_auth):
            query['ClientAuth'] = request.client_auth
        if not UtilClient.is_unset(request.client_password):
            query['ClientPassword'] = request.client_password
        if not UtilClient.is_unset(request.client_username):
            query['ClientUsername'] = request.client_username
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.gb_id):
            query['GbId'] = request.gb_id
        if not UtilClient.is_unset(request.ip):
            query['Ip'] = request.ip
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.port):
            query['Port'] = request.port
        if not UtilClient.is_unset(request.protocol):
            query['Protocol'] = request.protocol
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateParentPlatform',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.CreateParentPlatformResponse(),
            self.call_api(params, req, runtime)
        )

    def create_parent_platform(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_parent_platform_with_options(request, runtime)

    def create_rendering_device_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_renew):
            query['AutoRenew'] = request.auto_renew
        if not UtilClient.is_unset(request.auto_renew_period):
            query['AutoRenewPeriod'] = request.auto_renew_period
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.count):
            query['Count'] = request.count
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.edge_node_name):
            query['EdgeNodeName'] = request.edge_node_name
        if not UtilClient.is_unset(request.isp):
            query['ISP'] = request.isp
        if not UtilClient.is_unset(request.image_id):
            query['ImageId'] = request.image_id
        if not UtilClient.is_unset(request.instance_charge_type):
            query['InstanceChargeType'] = request.instance_charge_type
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.password):
            query['Password'] = request.password
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.period_unit):
            query['PeriodUnit'] = request.period_unit
        if not UtilClient.is_unset(request.security_group_id):
            query['SecurityGroupId'] = request.security_group_id
        if not UtilClient.is_unset(request.specification):
            query['Specification'] = request.specification
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateRenderingDevice',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.CreateRenderingDeviceResponse(),
            self.call_api(params, req, runtime)
        )

    def create_rendering_device(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_rendering_device_with_options(request, runtime)

    def create_stream_snapshot_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.location):
            query['Location'] = request.location
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateStreamSnapshot',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.CreateStreamSnapshotResponse(),
            self.call_api(params, req, runtime)
        )

    def create_stream_snapshot(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_stream_snapshot_with_options(request, runtime)

    def create_template_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.callback):
            query['Callback'] = request.callback
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.file_format):
            query['FileFormat'] = request.file_format
        if not UtilClient.is_unset(request.flv):
            query['Flv'] = request.flv
        if not UtilClient.is_unset(request.hls_m3u_8):
            query['HlsM3u8'] = request.hls_m3u_8
        if not UtilClient.is_unset(request.hls_ts):
            query['HlsTs'] = request.hls_ts
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.jpg_on_demand):
            query['JpgOnDemand'] = request.jpg_on_demand
        if not UtilClient.is_unset(request.jpg_overwrite):
            query['JpgOverwrite'] = request.jpg_overwrite
        if not UtilClient.is_unset(request.jpg_sequence):
            query['JpgSequence'] = request.jpg_sequence
        if not UtilClient.is_unset(request.mp_4):
            query['Mp4'] = request.mp_4
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
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        if not UtilClient.is_unset(request.retention):
            query['Retention'] = request.retention
        if not UtilClient.is_unset(request.trans_configs_json):
            query['TransConfigsJSON'] = request.trans_configs_json
        if not UtilClient.is_unset(request.trigger):
            query['Trigger'] = request.trigger
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateTemplate',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.CreateTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    def create_template(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_template_with_options(request, runtime)

    def delete_aiconfig_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.config_id):
            query['ConfigId'] = request.config_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteAIConfig',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.DeleteAIConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_aiconfig(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_aiconfig_with_options(request, runtime)

    def delete_bucket_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bucket_name):
            query['BucketName'] = request.bucket_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteBucket',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.DeleteBucketResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_bucket(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_bucket_with_options(request, runtime)

    def delete_cluster_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteCluster',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.DeleteClusterResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_cluster(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_cluster_with_options(request, runtime)

    def delete_device_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDevice',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.DeleteDeviceResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_device(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_device_with_options(request, runtime)

    def delete_directory_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDirectory',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.DeleteDirectoryResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_directory(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_directory_with_options(request, runtime)

    def delete_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteGroup',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.DeleteGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_group_with_options(request, runtime)

    def delete_parent_platform_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteParentPlatform',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.DeleteParentPlatformResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_parent_platform(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_parent_platform_with_options(request, runtime)

    def delete_preset_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.preset_id):
            query['PresetId'] = request.preset_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeletePreset',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.DeletePresetResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_preset(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_preset_with_options(request, runtime)

    def delete_purchased_device_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeletePurchasedDevice',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.DeletePurchasedDeviceResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_purchased_device(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_purchased_device_with_options(request, runtime)

    def delete_rendering_device_internet_ports_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.isp):
            query['ISP'] = request.isp
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not UtilClient.is_unset(request.internal_port):
            query['InternalPort'] = request.internal_port
        if not UtilClient.is_unset(request.ip_protocol):
            query['IpProtocol'] = request.ip_protocol
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteRenderingDeviceInternetPorts',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.DeleteRenderingDeviceInternetPortsResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_rendering_device_internet_ports(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_rendering_device_internet_ports_with_options(request, runtime)

    def delete_rendering_devices_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteRenderingDevices',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.DeleteRenderingDevicesResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_rendering_devices(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_rendering_devices_with_options(request, runtime)

    def delete_template_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteTemplate',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.DeleteTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_template(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_template_with_options(request, runtime)

    def delete_vs_pull_stream_info_config_with_options(self, request, runtime):
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
            action='DeleteVsPullStreamInfoConfig',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.DeleteVsPullStreamInfoConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_vs_pull_stream_info_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_vs_pull_stream_info_config_with_options(request, runtime)

    def delete_vs_streams_notify_url_config_with_options(self, request, runtime):
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
            action='DeleteVsStreamsNotifyUrlConfig',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.DeleteVsStreamsNotifyUrlConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_vs_streams_notify_url_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_vs_streams_notify_url_config_with_options(request, runtime)

    def describe_aiconfig_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.config_id):
            query['ConfigId'] = request.config_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAIConfig',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.DescribeAIConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_aiconfig(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_aiconfig_with_options(request, runtime)

    def describe_aiconfig_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAIConfigList',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.DescribeAIConfigListResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_aiconfig_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_aiconfig_list_with_options(request, runtime)

    def describe_aievent_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAIEventList',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.DescribeAIEventListResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_aievent_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_aievent_list_with_options(request, runtime)

    def describe_account_stat_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAccountStat',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.DescribeAccountStatResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_account_stat(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_account_stat_with_options(request, runtime)

    def describe_cluster_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCluster',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.DescribeClusterResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_cluster(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_cluster_with_options(request, runtime)

    def describe_cluster_devices_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.edge_node_name):
            query['EdgeNodeName'] = request.edge_node_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.platform):
            query['Platform'] = request.platform
        if not UtilClient.is_unset(request.specification):
            query['Specification'] = request.specification
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeClusterDevices',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.DescribeClusterDevicesResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_cluster_devices(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_cluster_devices_with_options(request, runtime)

    def describe_clusters_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeClusters',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.DescribeClustersResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_clusters(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_clusters_with_options(request, runtime)

    def describe_container_instance_id_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.node_name):
            query['NodeName'] = request.node_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.pod_index):
            query['PodIndex'] = request.pod_index
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeContainerInstanceId',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.DescribeContainerInstanceIdResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_container_instance_id(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_container_instance_id_with_options(request, runtime)

    def describe_device_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.include_directory):
            query['IncludeDirectory'] = request.include_directory
        if not UtilClient.is_unset(request.include_stats):
            query['IncludeStats'] = request.include_stats
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDevice',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.DescribeDeviceResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_device(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_device_with_options(request, runtime)

    def describe_device_channels_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
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
            action='DescribeDeviceChannels',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.DescribeDeviceChannelsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_device_channels(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_device_channels_with_options(request, runtime)

    def describe_device_gateway_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_ip):
            query['ClientIp'] = request.client_ip
        if not UtilClient.is_unset(request.expire):
            query['Expire'] = request.expire
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDeviceGateway',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.DescribeDeviceGatewayResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_device_gateway(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_device_gateway_with_options(request, runtime)

    def describe_device_urlwith_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auth):
            query['Auth'] = request.auth
        if not UtilClient.is_unset(request.expire):
            query['Expire'] = request.expire
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.mode):
            query['Mode'] = request.mode
        if not UtilClient.is_unset(request.out_protocol):
            query['OutProtocol'] = request.out_protocol
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.stream):
            query['Stream'] = request.stream
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDeviceURL',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.DescribeDeviceURLResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_device_url(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_device_urlwith_options(request, runtime)

    def describe_devices_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not UtilClient.is_unset(request.dsn):
            query['Dsn'] = request.dsn
        if not UtilClient.is_unset(request.gb_id):
            query['GbId'] = request.gb_id
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.include_directory):
            query['IncludeDirectory'] = request.include_directory
        if not UtilClient.is_unset(request.include_stats):
            query['IncludeStats'] = request.include_stats
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.parent_id):
            query['ParentId'] = request.parent_id
        if not UtilClient.is_unset(request.sort_by):
            query['SortBy'] = request.sort_by
        if not UtilClient.is_unset(request.sort_direction):
            query['SortDirection'] = request.sort_direction
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        if not UtilClient.is_unset(request.vendor):
            query['Vendor'] = request.vendor
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDevices',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.DescribeDevicesResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_devices(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_devices_with_options(request, runtime)

    def describe_directories_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.no_pagination):
            query['NoPagination'] = request.no_pagination
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.parent_id):
            query['ParentId'] = request.parent_id
        if not UtilClient.is_unset(request.sort_by):
            query['SortBy'] = request.sort_by
        if not UtilClient.is_unset(request.sort_direction):
            query['SortDirection'] = request.sort_direction
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDirectories',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.DescribeDirectoriesResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_directories(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_directories_with_options(request, runtime)

    def describe_directory_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDirectory',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.DescribeDirectoryResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_directory(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_directory_with_options(request, runtime)

    def describe_external_stream_urlwith_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.kind):
            query['Kind'] = request.kind
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.profile):
            query['Profile'] = request.profile
        if not UtilClient.is_unset(request.tx_id):
            query['TxId'] = request.tx_id
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeExternalStreamURL',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.DescribeExternalStreamURLResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_external_stream_url(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_external_stream_urlwith_options(request, runtime)

    def describe_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.include_stats):
            query['IncludeStats'] = request.include_stats
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeGroup',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.DescribeGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_group_with_options(request, runtime)

    def describe_groups_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.in_protocol):
            query['InProtocol'] = request.in_protocol
        if not UtilClient.is_unset(request.include_stats):
            query['IncludeStats'] = request.include_stats
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        if not UtilClient.is_unset(request.sort_by):
            query['SortBy'] = request.sort_by
        if not UtilClient.is_unset(request.sort_direction):
            query['SortDirection'] = request.sort_direction
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeGroups',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.DescribeGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_groups(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_groups_with_options(request, runtime)

    def describe_node_devices_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.node_name):
            query['NodeName'] = request.node_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeNodeDevicesInfo',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.DescribeNodeDevicesInfoResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_node_devices_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_node_devices_info_with_options(request, runtime)

    def describe_parent_platform_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeParentPlatform',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.DescribeParentPlatformResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_parent_platform(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_parent_platform_with_options(request, runtime)

    def describe_parent_platform_devices_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.sort_by):
            query['SortBy'] = request.sort_by
        if not UtilClient.is_unset(request.sort_direction):
            query['SortDirection'] = request.sort_direction
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeParentPlatformDevices',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.DescribeParentPlatformDevicesResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_parent_platform_devices(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_parent_platform_devices_with_options(request, runtime)

    def describe_parent_platforms_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.gb_id):
            query['GbId'] = request.gb_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.sort_by):
            query['SortBy'] = request.sort_by
        if not UtilClient.is_unset(request.sort_direction):
            query['SortDirection'] = request.sort_direction
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeParentPlatforms',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.DescribeParentPlatformsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_parent_platforms(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_parent_platforms_with_options(request, runtime)

    def describe_presets_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePresets',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.DescribePresetsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_presets(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_presets_with_options(request, runtime)

    def describe_purchased_device_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePurchasedDevice',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.DescribePurchasedDeviceResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_purchased_device(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_purchased_device_with_options(request, runtime)

    def describe_purchased_devices_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.sort_by):
            query['SortBy'] = request.sort_by
        if not UtilClient.is_unset(request.sort_direction):
            query['SortDirection'] = request.sort_direction
        if not UtilClient.is_unset(request.sub_type):
            query['SubType'] = request.sub_type
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        if not UtilClient.is_unset(request.vendor):
            query['Vendor'] = request.vendor
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePurchasedDevices',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.DescribePurchasedDevicesResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_purchased_devices(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_purchased_devices_with_options(request, runtime)

    def describe_records_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.private_bucket):
            query['PrivateBucket'] = request.private_bucket
        if not UtilClient.is_unset(request.sort_by):
            query['SortBy'] = request.sort_by
        if not UtilClient.is_unset(request.sort_direction):
            query['SortDirection'] = request.sort_direction
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.stream_id):
            query['StreamId'] = request.stream_id
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRecords',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.DescribeRecordsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_records(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_records_with_options(request, runtime)

    def describe_rendering_devices_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRenderingDevices',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.DescribeRenderingDevicesResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_rendering_devices(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_rendering_devices_with_options(request, runtime)

    def describe_stream_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeStream',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.DescribeStreamResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_stream(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_stream_with_options(request, runtime)

    def describe_stream_urlwith_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auth):
            query['Auth'] = request.auth
        if not UtilClient.is_unset(request.auth_key):
            query['AuthKey'] = request.auth_key
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.expire):
            query['Expire'] = request.expire
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.out_protocol):
            query['OutProtocol'] = request.out_protocol
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.transcode):
            query['Transcode'] = request.transcode
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeStreamURL',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.DescribeStreamURLResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_stream_url(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_stream_urlwith_options(request, runtime)

    def describe_stream_vod_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeStreamVodList',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.DescribeStreamVodListResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_stream_vod_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_stream_vod_list_with_options(request, runtime)

    def describe_streams_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app):
            query['App'] = request.app
        if not UtilClient.is_unset(request.device_id):
            query['DeviceId'] = request.device_id
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.parent_id):
            query['ParentId'] = request.parent_id
        if not UtilClient.is_unset(request.sort_by):
            query['SortBy'] = request.sort_by
        if not UtilClient.is_unset(request.sort_direction):
            query['SortDirection'] = request.sort_direction
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeStreams',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.DescribeStreamsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_streams(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_streams_with_options(request, runtime)

    def describe_template_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeTemplate',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.DescribeTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_template(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_template_with_options(request, runtime)

    def describe_templates_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.sort_by):
            query['SortBy'] = request.sort_by
        if not UtilClient.is_unset(request.sort_direction):
            query['SortDirection'] = request.sort_direction
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeTemplates',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.DescribeTemplatesResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_templates(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_templates_with_options(request, runtime)

    def describe_vod_stream_urlwith_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.tx_id):
            query['TxId'] = request.tx_id
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeVodStreamURL',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.DescribeVodStreamURLResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_vod_stream_url(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_vod_stream_urlwith_options(request, runtime)

    def describe_vs_certificate_detail_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cert_name):
            query['CertName'] = request.cert_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeVsCertificateDetail',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.DescribeVsCertificateDetailResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_vs_certificate_detail(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_vs_certificate_detail_with_options(request, runtime)

    def describe_vs_certificate_list_with_options(self, request, runtime):
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
            action='DescribeVsCertificateList',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.DescribeVsCertificateListResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_vs_certificate_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_vs_certificate_list_with_options(request, runtime)

    def describe_vs_devices_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeVsDevicesData',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.DescribeVsDevicesDataResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_vs_devices_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_vs_devices_data_with_options(request, runtime)

    def describe_vs_domain_bps_data_with_options(self, request, runtime):
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
            action='DescribeVsDomainBpsData',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.DescribeVsDomainBpsDataResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_vs_domain_bps_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_vs_domain_bps_data_with_options(request, runtime)

    def describe_vs_domain_certificate_info_with_options(self, request, runtime):
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
            action='DescribeVsDomainCertificateInfo',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.DescribeVsDomainCertificateInfoResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_vs_domain_certificate_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_vs_domain_certificate_info_with_options(request, runtime)

    def describe_vs_domain_configs_with_options(self, request, runtime):
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
            action='DescribeVsDomainConfigs',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.DescribeVsDomainConfigsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_vs_domain_configs(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_vs_domain_configs_with_options(request, runtime)

    def describe_vs_domain_detail_with_options(self, request, runtime):
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
            action='DescribeVsDomainDetail',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.DescribeVsDomainDetailResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_vs_domain_detail(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_vs_domain_detail_with_options(request, runtime)

    def describe_vs_domain_online_user_num_with_options(self, request, runtime):
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
            action='DescribeVsDomainOnlineUserNum',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.DescribeVsDomainOnlineUserNumResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_vs_domain_online_user_num(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_vs_domain_online_user_num_with_options(request, runtime)

    def describe_vs_domain_pv_data_with_options(self, request, runtime):
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
            action='DescribeVsDomainPvData',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.DescribeVsDomainPvDataResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_vs_domain_pv_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_vs_domain_pv_data_with_options(request, runtime)

    def describe_vs_domain_pv_uv_data_with_options(self, request, runtime):
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
            action='DescribeVsDomainPvUvData',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.DescribeVsDomainPvUvDataResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_vs_domain_pv_uv_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_vs_domain_pv_uv_data_with_options(request, runtime)

    def describe_vs_domain_record_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeVsDomainRecordData',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.DescribeVsDomainRecordDataResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_vs_domain_record_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_vs_domain_record_data_with_options(request, runtime)

    def describe_vs_domain_region_data_with_options(self, request, runtime):
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
            action='DescribeVsDomainRegionData',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.DescribeVsDomainRegionDataResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_vs_domain_region_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_vs_domain_region_data_with_options(request, runtime)

    def describe_vs_domain_req_bps_data_with_options(self, request, runtime):
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
            action='DescribeVsDomainReqBpsData',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.DescribeVsDomainReqBpsDataResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_vs_domain_req_bps_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_vs_domain_req_bps_data_with_options(request, runtime)

    def describe_vs_domain_req_traffic_data_with_options(self, request, runtime):
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
            action='DescribeVsDomainReqTrafficData',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.DescribeVsDomainReqTrafficDataResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_vs_domain_req_traffic_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_vs_domain_req_traffic_data_with_options(request, runtime)

    def describe_vs_domain_snapshot_data_with_options(self, request, runtime):
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
            action='DescribeVsDomainSnapshotData',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.DescribeVsDomainSnapshotDataResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_vs_domain_snapshot_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_vs_domain_snapshot_data_with_options(request, runtime)

    def describe_vs_domain_traffic_data_with_options(self, request, runtime):
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
            action='DescribeVsDomainTrafficData',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.DescribeVsDomainTrafficDataResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_vs_domain_traffic_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_vs_domain_traffic_data_with_options(request, runtime)

    def describe_vs_domain_uv_data_with_options(self, request, runtime):
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
            action='DescribeVsDomainUvData',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.DescribeVsDomainUvDataResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_vs_domain_uv_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_vs_domain_uv_data_with_options(request, runtime)

    def describe_vs_pull_stream_config_with_options(self, request, runtime):
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
            action='DescribeVsPullStreamConfig',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.DescribeVsPullStreamConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_vs_pull_stream_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_vs_pull_stream_config_with_options(request, runtime)

    def describe_vs_pull_stream_info_config_with_options(self, request, runtime):
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
            action='DescribeVsPullStreamInfoConfig',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.DescribeVsPullStreamInfoConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_vs_pull_stream_info_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_vs_pull_stream_info_config_with_options(request, runtime)

    def describe_vs_storage_traffic_usage_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bucket):
            query['Bucket'] = request.bucket
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
            action='DescribeVsStorageTrafficUsageData',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.DescribeVsStorageTrafficUsageDataResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_vs_storage_traffic_usage_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_vs_storage_traffic_usage_data_with_options(request, runtime)

    def describe_vs_storage_usage_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bucket):
            query['Bucket'] = request.bucket
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
            action='DescribeVsStorageUsageData',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.DescribeVsStorageUsageDataResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_vs_storage_usage_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_vs_storage_usage_data_with_options(request, runtime)

    def describe_vs_streams_notify_url_config_with_options(self, request, runtime):
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
            action='DescribeVsStreamsNotifyUrlConfig',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.DescribeVsStreamsNotifyUrlConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_vs_streams_notify_url_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_vs_streams_notify_url_config_with_options(request, runtime)

    def describe_vs_streams_online_list_with_options(self, request, runtime):
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
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
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
            action='DescribeVsStreamsOnlineList',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.DescribeVsStreamsOnlineListResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_vs_streams_online_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_vs_streams_online_list_with_options(request, runtime)

    def describe_vs_streams_publish_list_with_options(self, request, runtime):
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
            action='DescribeVsStreamsPublishList',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.DescribeVsStreamsPublishListResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_vs_streams_publish_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_vs_streams_publish_list_with_options(request, runtime)

    def describe_vs_top_domains_by_flow_with_options(self, request, runtime):
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
            action='DescribeVsTopDomainsByFlow',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.DescribeVsTopDomainsByFlowResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_vs_top_domains_by_flow(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_vs_top_domains_by_flow_with_options(request, runtime)

    def describe_vs_up_peak_publish_stream_data_with_options(self, request, runtime):
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
            action='DescribeVsUpPeakPublishStreamData',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.DescribeVsUpPeakPublishStreamDataResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_vs_up_peak_publish_stream_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_vs_up_peak_publish_stream_data_with_options(request, runtime)

    def describe_vs_user_resource_package_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeVsUserResourcePackage',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.DescribeVsUserResourcePackageResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_vs_user_resource_package(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_vs_user_resource_package_with_options(request, runtime)

    def forbid_vs_stream_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.control_stream_action):
            query['ControlStreamAction'] = request.control_stream_action
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
            action='ForbidVsStream',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.ForbidVsStreamResponse(),
            self.call_api(params, req, runtime)
        )

    def forbid_vs_stream(self, request):
        runtime = util_models.RuntimeOptions()
        return self.forbid_vs_stream_with_options(request, runtime)

    def get_bucket_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bucket_name):
            query['BucketName'] = request.bucket_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetBucketInfo',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.GetBucketInfoResponse(),
            self.call_api(params, req, runtime)
        )

    def get_bucket_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_bucket_info_with_options(request, runtime)

    def get_object_total_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bucket_name):
            query['BucketName'] = request.bucket_name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetObjectTotal',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.GetObjectTotalResponse(),
            self.call_api(params, req, runtime)
        )

    def get_object_total(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_object_total_with_options(request, runtime)

    def goto_preset_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.preset_id):
            query['PresetId'] = request.preset_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GotoPreset',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.GotoPresetResponse(),
            self.call_api(params, req, runtime)
        )

    def goto_preset(self, request):
        runtime = util_models.RuntimeOptions()
        return self.goto_preset_with_options(request, runtime)

    def list_buckets_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.keyword):
            query['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.marker):
            query['Marker'] = request.marker
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.prefix):
            query['Prefix'] = request.prefix
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListBuckets',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.ListBucketsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_buckets(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_buckets_with_options(request, runtime)

    def list_device_channels_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.device_id):
            query['DeviceId'] = request.device_id
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
            action='ListDeviceChannels',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.ListDeviceChannelsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_device_channels(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_device_channels_with_options(request, runtime)

    def list_device_records_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.device_id):
            query['DeviceId'] = request.device_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search_criteria):
            query['SearchCriteria'] = request.search_criteria
        if not UtilClient.is_unset(request.stream_id):
            query['StreamId'] = request.stream_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDeviceRecords',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.ListDeviceRecordsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_device_records(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_device_records_with_options(request, runtime)

    def list_objects_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bucket_name):
            query['BucketName'] = request.bucket_name
        if not UtilClient.is_unset(request.continuation_token):
            query['ContinuationToken'] = request.continuation_token
        if not UtilClient.is_unset(request.delimiter):
            query['Delimiter'] = request.delimiter
        if not UtilClient.is_unset(request.encoding_type):
            query['EncodingType'] = request.encoding_type
        if not UtilClient.is_unset(request.marker):
            query['Marker'] = request.marker
        if not UtilClient.is_unset(request.max_keys):
            query['MaxKeys'] = request.max_keys
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.prefix):
            query['Prefix'] = request.prefix
        if not UtilClient.is_unset(request.start_after):
            query['StartAfter'] = request.start_after
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListObjects',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.ListObjectsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_objects(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_objects_with_options(request, runtime)

    def modify_device_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alarm_method):
            query['AlarmMethod'] = request.alarm_method
        if not UtilClient.is_unset(request.auto_pos):
            query['AutoPos'] = request.auto_pos
        if not UtilClient.is_unset(request.auto_start):
            query['AutoStart'] = request.auto_start
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not UtilClient.is_unset(request.gb_id):
            query['GbId'] = request.gb_id
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.ip):
            query['Ip'] = request.ip
        if not UtilClient.is_unset(request.latitude):
            query['Latitude'] = request.latitude
        if not UtilClient.is_unset(request.longitude):
            query['Longitude'] = request.longitude
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.params):
            query['Params'] = request.params
        if not UtilClient.is_unset(request.parent_id):
            query['ParentId'] = request.parent_id
        if not UtilClient.is_unset(request.password):
            query['Password'] = request.password
        if not UtilClient.is_unset(request.port):
            query['Port'] = request.port
        if not UtilClient.is_unset(request.pos_interval):
            query['PosInterval'] = request.pos_interval
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        if not UtilClient.is_unset(request.username):
            query['Username'] = request.username
        if not UtilClient.is_unset(request.vendor):
            query['Vendor'] = request.vendor
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDevice',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.ModifyDeviceResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_device(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_device_with_options(request, runtime)

    def modify_device_alarm_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alarm_id):
            query['AlarmId'] = request.alarm_id
        if not UtilClient.is_unset(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDeviceAlarm',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.ModifyDeviceAlarmResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_device_alarm(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_device_alarm_with_options(request, runtime)

    def modify_device_capture_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.image):
            query['Image'] = request.image
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.video):
            query['Video'] = request.video
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDeviceCapture',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.ModifyDeviceCaptureResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_device_capture(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_device_capture_with_options(request, runtime)

    def modify_device_channels_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.channels):
            query['Channels'] = request.channels
        if not UtilClient.is_unset(request.device_status):
            query['DeviceStatus'] = request.device_status
        if not UtilClient.is_unset(request.dsn):
            query['Dsn'] = request.dsn
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDeviceChannels',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.ModifyDeviceChannelsResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_device_channels(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_device_channels_with_options(request, runtime)

    def modify_directory_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyDirectory',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.ModifyDirectoryResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_directory(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_directory_with_options(request, runtime)

    def modify_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.callback):
            query['Callback'] = request.callback
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.enabled):
            query['Enabled'] = request.enabled
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.in_protocol):
            query['InProtocol'] = request.in_protocol
        if not UtilClient.is_unset(request.lazy_pull):
            query['LazyPull'] = request.lazy_pull
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.out_protocol):
            query['OutProtocol'] = request.out_protocol
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.play_domain):
            query['PlayDomain'] = request.play_domain
        if not UtilClient.is_unset(request.push_domain):
            query['PushDomain'] = request.push_domain
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyGroup',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.ModifyGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_group_with_options(request, runtime)

    def modify_parent_platform_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_start):
            query['AutoStart'] = request.auto_start
        if not UtilClient.is_unset(request.client_auth):
            query['ClientAuth'] = request.client_auth
        if not UtilClient.is_unset(request.client_password):
            query['ClientPassword'] = request.client_password
        if not UtilClient.is_unset(request.client_username):
            query['ClientUsername'] = request.client_username
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.gb_id):
            query['GbId'] = request.gb_id
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.ip):
            query['Ip'] = request.ip
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.port):
            query['Port'] = request.port
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyParentPlatform',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.ModifyParentPlatformResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_parent_platform(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_parent_platform_with_options(request, runtime)

    def modify_purchased_device_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.order_id):
            query['OrderId'] = request.order_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.register_code):
            query['RegisterCode'] = request.register_code
        if not UtilClient.is_unset(request.sub_type):
            query['SubType'] = request.sub_type
        if not UtilClient.is_unset(request.vendor):
            query['Vendor'] = request.vendor
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyPurchasedDevice',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.ModifyPurchasedDeviceResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_purchased_device(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_purchased_device_with_options(request, runtime)

    def modify_template_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.callback):
            query['Callback'] = request.callback
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.file_format):
            query['FileFormat'] = request.file_format
        if not UtilClient.is_unset(request.flv):
            query['Flv'] = request.flv
        if not UtilClient.is_unset(request.hls_m3u_8):
            query['HlsM3u8'] = request.hls_m3u_8
        if not UtilClient.is_unset(request.hls_ts):
            query['HlsTs'] = request.hls_ts
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.jpg_on_demand):
            query['JpgOnDemand'] = request.jpg_on_demand
        if not UtilClient.is_unset(request.jpg_overwrite):
            query['JpgOverwrite'] = request.jpg_overwrite
        if not UtilClient.is_unset(request.jpg_sequence):
            query['JpgSequence'] = request.jpg_sequence
        if not UtilClient.is_unset(request.mp_4):
            query['Mp4'] = request.mp_4
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
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        if not UtilClient.is_unset(request.retention):
            query['Retention'] = request.retention
        if not UtilClient.is_unset(request.trans_configs_json):
            query['TransConfigsJSON'] = request.trans_configs_json
        if not UtilClient.is_unset(request.trigger):
            query['Trigger'] = request.trigger
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyTemplate',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.ModifyTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_template(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_template_with_options(request, runtime)

    def open_vs_service_with_options(self, runtime):
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='OpenVsService',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.OpenVsServiceResponse(),
            self.call_api(params, req, runtime)
        )

    def open_vs_service(self):
        runtime = util_models.RuntimeOptions()
        return self.open_vs_service_with_options(runtime)

    def operate_rendering_devices_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not UtilClient.is_unset(request.operation):
            query['Operation'] = request.operation
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.pod_id):
            query['PodId'] = request.pod_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='OperateRenderingDevices',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.OperateRenderingDevicesResponse(),
            self.call_api(params, req, runtime)
        )

    def operate_rendering_devices(self, request):
        runtime = util_models.RuntimeOptions()
        return self.operate_rendering_devices_with_options(request, runtime)

    def prepare_upload_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bucket_name):
            query['BucketName'] = request.bucket_name
        if not UtilClient.is_unset(request.client_ip):
            query['ClientIp'] = request.client_ip
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PrepareUpload',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.PrepareUploadResponse(),
            self.call_api(params, req, runtime)
        )

    def prepare_upload(self, request):
        runtime = util_models.RuntimeOptions()
        return self.prepare_upload_with_options(request, runtime)

    def put_bucket_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bucket_acl):
            query['BucketAcl'] = request.bucket_acl
        if not UtilClient.is_unset(request.bucket_name):
            query['BucketName'] = request.bucket_name
        if not UtilClient.is_unset(request.comment):
            query['Comment'] = request.comment
        if not UtilClient.is_unset(request.data_redundancy_type):
            query['DataRedundancyType'] = request.data_redundancy_type
        if not UtilClient.is_unset(request.dispatcher_type):
            query['DispatcherType'] = request.dispatcher_type
        if not UtilClient.is_unset(request.endpoint):
            query['Endpoint'] = request.endpoint
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.storage_class):
            query['StorageClass'] = request.storage_class
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PutBucket',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.PutBucketResponse(),
            self.call_api(params, req, runtime)
        )

    def put_bucket(self, request):
        runtime = util_models.RuntimeOptions()
        return self.put_bucket_with_options(request, runtime)

    def reset_rendering_devices_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.image_id):
            query['ImageId'] = request.image_id
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.pod_id):
            query['PodId'] = request.pod_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ResetRenderingDevices',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.ResetRenderingDevicesResponse(),
            self.call_api(params, req, runtime)
        )

    def reset_rendering_devices(self, request):
        runtime = util_models.RuntimeOptions()
        return self.reset_rendering_devices_with_options(request, runtime)

    def resume_vs_stream_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.control_stream_action):
            query['ControlStreamAction'] = request.control_stream_action
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.live_stream_type):
            query['LiveStreamType'] = request.live_stream_type
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.stream_name):
            query['StreamName'] = request.stream_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ResumeVsStream',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.ResumeVsStreamResponse(),
            self.call_api(params, req, runtime)
        )

    def resume_vs_stream(self, request):
        runtime = util_models.RuntimeOptions()
        return self.resume_vs_stream_with_options(request, runtime)

    def set_preset_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.preset_id):
            query['PresetId'] = request.preset_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetPreset',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.SetPresetResponse(),
            self.call_api(params, req, runtime)
        )

    def set_preset(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_preset_with_options(request, runtime)

    def set_vs_domain_certificate_with_options(self, request, runtime):
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
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        if not UtilClient.is_unset(request.sslpri):
            query['SSLPri'] = request.sslpri
        if not UtilClient.is_unset(request.sslprotocol):
            query['SSLProtocol'] = request.sslprotocol
        if not UtilClient.is_unset(request.sslpub):
            query['SSLPub'] = request.sslpub
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetVsDomainCertificate',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.SetVsDomainCertificateResponse(),
            self.call_api(params, req, runtime)
        )

    def set_vs_domain_certificate(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_vs_domain_certificate_with_options(request, runtime)

    def set_vs_streams_notify_url_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auth_key):
            query['AuthKey'] = request.auth_key
        if not UtilClient.is_unset(request.auth_type):
            query['AuthType'] = request.auth_type
        if not UtilClient.is_unset(request.domain_name):
            query['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.notify_url):
            query['NotifyUrl'] = request.notify_url
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetVsStreamsNotifyUrlConfig',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.SetVsStreamsNotifyUrlConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def set_vs_streams_notify_url_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_vs_streams_notify_url_config_with_options(request, runtime)

    def start_device_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartDevice',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.StartDeviceResponse(),
            self.call_api(params, req, runtime)
        )

    def start_device(self, request):
        runtime = util_models.RuntimeOptions()
        return self.start_device_with_options(request, runtime)

    def start_parent_platform_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartParentPlatform',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.StartParentPlatformResponse(),
            self.call_api(params, req, runtime)
        )

    def start_parent_platform(self, request):
        runtime = util_models.RuntimeOptions()
        return self.start_parent_platform_with_options(request, runtime)

    def start_record_stream_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app):
            query['App'] = request.app
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.play_domain):
            query['PlayDomain'] = request.play_domain
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartRecordStream',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.StartRecordStreamResponse(),
            self.call_api(params, req, runtime)
        )

    def start_record_stream(self, request):
        runtime = util_models.RuntimeOptions()
        return self.start_record_stream_with_options(request, runtime)

    def start_stream_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartStream',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.StartStreamResponse(),
            self.call_api(params, req, runtime)
        )

    def start_stream(self, request):
        runtime = util_models.RuntimeOptions()
        return self.start_stream_with_options(request, runtime)

    def start_transfer_stream_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.transcode):
            query['Transcode'] = request.transcode
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartTransferStream',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.StartTransferStreamResponse(),
            self.call_api(params, req, runtime)
        )

    def start_transfer_stream(self, request):
        runtime = util_models.RuntimeOptions()
        return self.start_transfer_stream_with_options(request, runtime)

    def stop_adjust_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.focus):
            query['Focus'] = request.focus
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.iris):
            query['Iris'] = request.iris
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopAdjust',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.StopAdjustResponse(),
            self.call_api(params, req, runtime)
        )

    def stop_adjust(self, request):
        runtime = util_models.RuntimeOptions()
        return self.stop_adjust_with_options(request, runtime)

    def stop_device_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopDevice',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.StopDeviceResponse(),
            self.call_api(params, req, runtime)
        )

    def stop_device(self, request):
        runtime = util_models.RuntimeOptions()
        return self.stop_device_with_options(request, runtime)

    def stop_move_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.pan):
            query['Pan'] = request.pan
        if not UtilClient.is_unset(request.tilt):
            query['Tilt'] = request.tilt
        if not UtilClient.is_unset(request.zoom):
            query['Zoom'] = request.zoom
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopMove',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.StopMoveResponse(),
            self.call_api(params, req, runtime)
        )

    def stop_move(self, request):
        runtime = util_models.RuntimeOptions()
        return self.stop_move_with_options(request, runtime)

    def stop_parent_platform_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopParentPlatform',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.StopParentPlatformResponse(),
            self.call_api(params, req, runtime)
        )

    def stop_parent_platform(self, request):
        runtime = util_models.RuntimeOptions()
        return self.stop_parent_platform_with_options(request, runtime)

    def stop_record_stream_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app):
            query['App'] = request.app
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.play_domain):
            query['PlayDomain'] = request.play_domain
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopRecordStream',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.StopRecordStreamResponse(),
            self.call_api(params, req, runtime)
        )

    def stop_record_stream(self, request):
        runtime = util_models.RuntimeOptions()
        return self.stop_record_stream_with_options(request, runtime)

    def stop_stream_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopStream',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.StopStreamResponse(),
            self.call_api(params, req, runtime)
        )

    def stop_stream(self, request):
        runtime = util_models.RuntimeOptions()
        return self.stop_stream_with_options(request, runtime)

    def stop_transfer_stream_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.transcode):
            query['Transcode'] = request.transcode
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopTransferStream',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.StopTransferStreamResponse(),
            self.call_api(params, req, runtime)
        )

    def stop_transfer_stream(self, request):
        runtime = util_models.RuntimeOptions()
        return self.stop_transfer_stream_with_options(request, runtime)

    def sync_catalogs_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SyncCatalogs',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.SyncCatalogsResponse(),
            self.call_api(params, req, runtime)
        )

    def sync_catalogs(self, request):
        runtime = util_models.RuntimeOptions()
        return self.sync_catalogs_with_options(request, runtime)

    def sync_device_channels_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.device_id):
            query['DeviceId'] = request.device_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SyncDeviceChannels',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.SyncDeviceChannelsResponse(),
            self.call_api(params, req, runtime)
        )

    def sync_device_channels(self, request):
        runtime = util_models.RuntimeOptions()
        return self.sync_device_channels_with_options(request, runtime)

    def unbind_directory_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.device_id):
            query['DeviceId'] = request.device_id
        if not UtilClient.is_unset(request.directory_id):
            query['DirectoryId'] = request.directory_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UnbindDirectory',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.UnbindDirectoryResponse(),
            self.call_api(params, req, runtime)
        )

    def unbind_directory(self, request):
        runtime = util_models.RuntimeOptions()
        return self.unbind_directory_with_options(request, runtime)

    def unbind_parent_platform_device_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.device_id):
            query['DeviceId'] = request.device_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.parent_platform_id):
            query['ParentPlatformId'] = request.parent_platform_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UnbindParentPlatformDevice',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.UnbindParentPlatformDeviceResponse(),
            self.call_api(params, req, runtime)
        )

    def unbind_parent_platform_device(self, request):
        runtime = util_models.RuntimeOptions()
        return self.unbind_parent_platform_device_with_options(request, runtime)

    def unbind_purchased_device_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.device_id):
            query['DeviceId'] = request.device_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UnbindPurchasedDevice',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.UnbindPurchasedDeviceResponse(),
            self.call_api(params, req, runtime)
        )

    def unbind_purchased_device(self, request):
        runtime = util_models.RuntimeOptions()
        return self.unbind_purchased_device_with_options(request, runtime)

    def unbind_template_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        if not UtilClient.is_unset(request.template_type):
            query['TemplateType'] = request.template_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UnbindTemplate',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.UnbindTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    def unbind_template(self, request):
        runtime = util_models.RuntimeOptions()
        return self.unbind_template_with_options(request, runtime)

    def unlock_device_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UnlockDevice',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.UnlockDeviceResponse(),
            self.call_api(params, req, runtime)
        )

    def unlock_device(self, request):
        runtime = util_models.RuntimeOptions()
        return self.unlock_device_with_options(request, runtime)

    def update_aiconfig_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.capture_interval):
            query['CaptureInterval'] = request.capture_interval
        if not UtilClient.is_unset(request.config_id):
            query['ConfigId'] = request.config_id
        if not UtilClient.is_unset(request.configs):
            query['Configs'] = request.configs
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.features):
            query['Features'] = request.features
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateAIConfig',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.UpdateAIConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def update_aiconfig(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_aiconfig_with_options(request, runtime)

    def update_bucket_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bucket_name):
            query['BucketName'] = request.bucket_name
        if not UtilClient.is_unset(request.comment):
            query['Comment'] = request.comment
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateBucketInfo',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.UpdateBucketInfoResponse(),
            self.call_api(params, req, runtime)
        )

    def update_bucket_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_bucket_info_with_options(request, runtime)

    def update_cluster_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.effective_time):
            query['EffectiveTime'] = request.effective_time
        if not UtilClient.is_unset(request.internal_ports):
            query['InternalPorts'] = request.internal_ports
        if not UtilClient.is_unset(request.maintain_time):
            query['MaintainTime'] = request.maintain_time
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.security_group_id):
            query['SecurityGroupId'] = request.security_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateCluster',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.UpdateClusterResponse(),
            self.call_api(params, req, runtime)
        )

    def update_cluster(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_cluster_with_options(request, runtime)

    def update_rendering_device_spec_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_renew):
            query['AutoRenew'] = request.auto_renew
        if not UtilClient.is_unset(request.auto_renew_period):
            query['AutoRenewPeriod'] = request.auto_renew_period
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.effective_time):
            query['EffectiveTime'] = request.effective_time
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.period):
            query['Period'] = request.period
        if not UtilClient.is_unset(request.period_unit):
            query['PeriodUnit'] = request.period_unit
        if not UtilClient.is_unset(request.specification):
            query['Specification'] = request.specification
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateRenderingDeviceSpec',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.UpdateRenderingDeviceSpecResponse(),
            self.call_api(params, req, runtime)
        )

    def update_rendering_device_spec(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_rendering_device_spec_with_options(request, runtime)

    def update_vs_pull_stream_info_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.always):
            query['Always'] = request.always
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
            action='UpdateVsPullStreamInfoConfig',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.UpdateVsPullStreamInfoConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def update_vs_pull_stream_info_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_vs_pull_stream_info_config_with_options(request, runtime)

    def upgrade_rendering_devices_host_oswith_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.rom_name):
            query['RomName'] = request.rom_name
        if not UtilClient.is_unset(request.rom_path):
            query['RomPath'] = request.rom_path
        if not UtilClient.is_unset(request.rom_version):
            query['RomVersion'] = request.rom_version
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpgradeRenderingDevicesHostOS',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.UpgradeRenderingDevicesHostOSResponse(),
            self.call_api(params, req, runtime)
        )

    def upgrade_rendering_devices_host_os(self, request):
        runtime = util_models.RuntimeOptions()
        return self.upgrade_rendering_devices_host_oswith_options(request, runtime)

    def upgrade_rendering_devices_image_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.image_id):
            query['ImageId'] = request.image_id
        if not UtilClient.is_unset(request.instance_ids):
            query['InstanceIds'] = request.instance_ids
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpgradeRenderingDevicesImage',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.UpgradeRenderingDevicesImageResponse(),
            self.call_api(params, req, runtime)
        )

    def upgrade_rendering_devices_image(self, request):
        runtime = util_models.RuntimeOptions()
        return self.upgrade_rendering_devices_image_with_options(request, runtime)

    def upload_device_record_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.device_id):
            query['DeviceId'] = request.device_id
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.search_criteria):
            query['SearchCriteria'] = request.search_criteria
        if not UtilClient.is_unset(request.stream_id):
            query['StreamId'] = request.stream_id
        if not UtilClient.is_unset(request.upload_id):
            query['UploadId'] = request.upload_id
        if not UtilClient.is_unset(request.upload_mode):
            query['UploadMode'] = request.upload_mode
        if not UtilClient.is_unset(request.upload_params):
            query['UploadParams'] = request.upload_params
        if not UtilClient.is_unset(request.upload_type):
            query['UploadType'] = request.upload_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UploadDeviceRecord',
            version='2018-12-12',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vs_20181212_models.UploadDeviceRecordResponse(),
            self.call_api(params, req, runtime)
        )

    def upload_device_record(self, request):
        runtime = util_models.RuntimeOptions()
        return self.upload_device_record_with_options(request, runtime)
