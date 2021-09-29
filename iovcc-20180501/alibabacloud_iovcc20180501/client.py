# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_iovcc20180501 import models as iovcc_20180501_models
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
        self._endpoint = self.get_endpoint('iovcc', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def list_device_brands_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            iovcc_20180501_models.ListDeviceBrandsResponse(),
            self.do_rpcrequest('ListDeviceBrands', '2018-05-01', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def list_device_brands(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_device_brands_with_options(request, runtime)

    def list_function_execute_log_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iovcc_20180501_models.ListFunctionExecuteLogResponse(),
            self.do_rpcrequest('ListFunctionExecuteLog', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_function_execute_log(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_function_execute_log_with_options(request, runtime)

    def list_device_models_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            iovcc_20180501_models.ListDeviceModelsResponse(),
            self.do_rpcrequest('ListDeviceModels', '2018-05-01', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def list_device_models(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_device_models_with_options(request, runtime)

    def list_mqtt_message_logs_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iovcc_20180501_models.ListMqttMessageLogsResponse(),
            self.do_rpcrequest('ListMqttMessageLogs', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_mqtt_message_logs(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_mqtt_message_logs_with_options(request, runtime)

    def delete_namespace_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iovcc_20180501_models.DeleteNamespaceResponse(),
            self.do_rpcrequest('DeleteNamespace', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_namespace(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_namespace_with_options(request, runtime)

    def list_offline_messages_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iovcc_20180501_models.ListOfflineMessagesResponse(),
            self.do_rpcrequest('ListOfflineMessages', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_offline_messages(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_offline_messages_with_options(request, runtime)

    def push_message_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iovcc_20180501_models.PushMessageResponse(),
            self.do_rpcrequest('PushMessage', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def push_message(self, request):
        runtime = util_models.RuntimeOptions()
        return self.push_message_with_options(request, runtime)

    def delete_customized_filter_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iovcc_20180501_models.DeleteCustomizedFilterResponse(),
            self.do_rpcrequest('DeleteCustomizedFilter', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_customized_filter(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_customized_filter_with_options(request, runtime)

    def describe_mqtt_client_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iovcc_20180501_models.DescribeMqttClientStatusResponse(),
            self.do_rpcrequest('DescribeMqttClientStatus', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_mqtt_client_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_mqtt_client_status_with_options(request, runtime)

    def delete_device_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iovcc_20180501_models.DeleteDeviceResponse(),
            self.do_rpcrequest('DeleteDevice', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_device(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_device_with_options(request, runtime)

    def update_device_model_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iovcc_20180501_models.UpdateDeviceModelResponse(),
            self.do_rpcrequest('UpdateDeviceModel', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_device_model(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_device_model_with_options(request, runtime)

    def update_api_gateway_app_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iovcc_20180501_models.UpdateApiGatewayAppStatusResponse(),
            self.do_rpcrequest('UpdateApiGatewayAppStatus', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_api_gateway_app_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_api_gateway_app_status_with_options(request, runtime)

    def list_camera_shooting_attachments_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iovcc_20180501_models.ListCameraShootingAttachmentsResponse(),
            self.do_rpcrequest('ListCameraShootingAttachments', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_camera_shooting_attachments(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_camera_shooting_attachments_with_options(request, runtime)

    def list_assist_histories_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            iovcc_20180501_models.ListAssistHistoriesResponse(),
            self.do_rpcrequest('ListAssistHistories', '2018-05-01', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def list_assist_histories(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_assist_histories_with_options(request, runtime)

    def get_device_system_update_funnel_events_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iovcc_20180501_models.GetDeviceSystemUpdateFunnelEventsResponse(),
            self.do_rpcrequest('GetDeviceSystemUpdateFunnelEvents', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_device_system_update_funnel_events(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_device_system_update_funnel_events_with_options(request, runtime)

    def delete_all_customized_filters_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iovcc_20180501_models.DeleteAllCustomizedFiltersResponse(),
            self.do_rpcrequest('DeleteAllCustomizedFilters', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_all_customized_filters(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_all_customized_filters_with_options(request, runtime)

    def generate_assist_file_upload_url_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iovcc_20180501_models.GenerateAssistFileUploadUrlResponse(),
            self.do_rpcrequest('GenerateAssistFileUploadUrl', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def generate_assist_file_upload_url(self, request):
        runtime = util_models.RuntimeOptions()
        return self.generate_assist_file_upload_url_with_options(request, runtime)

    def describe_assist_wsserver_address_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            iovcc_20180501_models.DescribeAssistWSServerAddressResponse(),
            self.do_rpcrequest('DescribeAssistWSServerAddress', '2018-05-01', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def describe_assist_wsserver_address(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_assist_wsserver_address_with_options(request, runtime)

    def find_prepublishes_by_version_id_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iovcc_20180501_models.FindPrepublishesByVersionIdResponse(),
            self.do_rpcrequest('FindPrepublishesByVersionId', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def find_prepublishes_by_version_id(self, request):
        runtime = util_models.RuntimeOptions()
        return self.find_prepublishes_by_version_id_with_options(request, runtime)

    def find_version_messages_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iovcc_20180501_models.FindVersionMessagesResponse(),
            self.do_rpcrequest('FindVersionMessages', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def find_version_messages(self, request):
        runtime = util_models.RuntimeOptions()
        return self.find_version_messages_with_options(request, runtime)

    def update_upstream_app_server_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iovcc_20180501_models.UpdateUpstreamAppServerResponse(),
            self.do_rpcrequest('UpdateUpstreamAppServer', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_upstream_app_server(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_upstream_app_server_with_options(request, runtime)

    def get_vehicle_track_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            iovcc_20180501_models.GetVehicleTrackResponse(),
            self.do_rpcrequest('GetVehicleTrack', '2018-05-01', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def get_vehicle_track(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_vehicle_track_with_options(request, runtime)

    def create_version_test_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iovcc_20180501_models.CreateVersionTestResponse(),
            self.do_rpcrequest('CreateVersionTest', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_version_test(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_version_test_with_options(request, runtime)

    def list_deployed_functions_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iovcc_20180501_models.ListDeployedFunctionsResponse(),
            self.do_rpcrequest('ListDeployedFunctions', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_deployed_functions(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_deployed_functions_with_options(request, runtime)

    def list_device_model_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            iovcc_20180501_models.ListDeviceModelResponse(),
            self.do_rpcrequest('ListDeviceModel', '2018-05-01', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def list_device_model(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_device_model_with_options(request, runtime)

    def create_schema_subscribe_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iovcc_20180501_models.CreateSchemaSubscribeResponse(),
            self.do_rpcrequest('CreateSchemaSubscribe', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_schema_subscribe(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_schema_subscribe_with_options(request, runtime)

    def describe_assist_rtmpserver_address_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            iovcc_20180501_models.DescribeAssistRTMPServerAddressResponse(),
            self.do_rpcrequest('DescribeAssistRTMPServerAddress', '2018-05-01', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def describe_assist_rtmpserver_address(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_assist_rtmpserver_address_with_options(request, runtime)

    def delete_shadow_schema_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iovcc_20180501_models.DeleteShadowSchemaResponse(),
            self.do_rpcrequest('DeleteShadowSchema', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_shadow_schema(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_shadow_schema_with_options(request, runtime)

    def describe_project_app_security_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iovcc_20180501_models.DescribeProjectAppSecurityResponse(),
            self.do_rpcrequest('DescribeProjectAppSecurity', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_project_app_security(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_project_app_security_with_options(request, runtime)

    def create_device_brand_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iovcc_20180501_models.CreateDeviceBrandResponse(),
            self.do_rpcrequest('CreateDeviceBrand', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_device_brand(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_device_brand_with_options(request, runtime)

    def create_mqtt_root_topic_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iovcc_20180501_models.CreateMqttRootTopicResponse(),
            self.do_rpcrequest('CreateMqttRootTopic', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_mqtt_root_topic(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_mqtt_root_topic_with_options(request, runtime)

    def delay_publish_os_version_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iovcc_20180501_models.DelayPublishOsVersionResponse(),
            self.do_rpcrequest('DelayPublishOsVersion', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delay_publish_os_version(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delay_publish_os_version_with_options(request, runtime)

    def list_pre_checks_with_options(self, runtime):
        req = open_api_models.OpenApiRequest()
        return TeaCore.from_map(
            iovcc_20180501_models.ListPreChecksResponse(),
            self.do_rpcrequest('ListPreChecks', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_pre_checks(self):
        runtime = util_models.RuntimeOptions()
        return self.list_pre_checks_with_options(runtime)

    def list_apps_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iovcc_20180501_models.ListAppsResponse(),
            self.do_rpcrequest('ListApps', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_apps(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_apps_with_options(request, runtime)

    def delete_camera_shooting_record_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iovcc_20180501_models.DeleteCameraShootingRecordResponse(),
            self.do_rpcrequest('DeleteCameraShootingRecord', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_camera_shooting_record(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_camera_shooting_record_with_options(request, runtime)

    def describe_device_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iovcc_20180501_models.DescribeDeviceResponse(),
            self.do_rpcrequest('DescribeDevice', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_device(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_device_with_options(request, runtime)

    def add_version_group_devices_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iovcc_20180501_models.AddVersionGroupDevicesResponse(),
            self.do_rpcrequest('AddVersionGroupDevices', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def add_version_group_devices(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_version_group_devices_with_options(request, runtime)

    def list_project_apps_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iovcc_20180501_models.ListProjectAppsResponse(),
            self.do_rpcrequest('ListProjectApps', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_project_apps(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_project_apps_with_options(request, runtime)

    def connect_assist_device_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iovcc_20180501_models.ConnectAssistDeviceResponse(),
            self.do_rpcrequest('ConnectAssistDevice', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def connect_assist_device(self, request):
        runtime = util_models.RuntimeOptions()
        return self.connect_assist_device_with_options(request, runtime)

    def list_api_gateway_apps_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iovcc_20180501_models.ListApiGatewayAppsResponse(),
            self.do_rpcrequest('ListApiGatewayApps', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_api_gateway_apps(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_api_gateway_apps_with_options(request, runtime)

    def delete_rpc_service_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iovcc_20180501_models.DeleteRpcServiceResponse(),
            self.do_rpcrequest('DeleteRpcService', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_rpc_service(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_rpc_service_with_options(request, runtime)

    def find_prepublish_passed_devices_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iovcc_20180501_models.FindPrepublishPassedDevicesResponse(),
            self.do_rpcrequest('FindPrepublishPassedDevices', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def find_prepublish_passed_devices(self, request):
        runtime = util_models.RuntimeOptions()
        return self.find_prepublish_passed_devices_with_options(request, runtime)

    def delete_version_black_devices_by_id_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iovcc_20180501_models.DeleteVersionBlackDevicesByIdResponse(),
            self.do_rpcrequest('DeleteVersionBlackDevicesById', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_version_black_devices_by_id(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_version_black_devices_by_id_with_options(request, runtime)

    def describe_open_account_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            iovcc_20180501_models.DescribeOpenAccountResponse(),
            self.do_rpcrequest('DescribeOpenAccount', '2018-05-01', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def describe_open_account(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_open_account_with_options(request, runtime)

    def find_customized_filters_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iovcc_20180501_models.FindCustomizedFiltersResponse(),
            self.do_rpcrequest('FindCustomizedFilters', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def find_customized_filters(self, request):
        runtime = util_models.RuntimeOptions()
        return self.find_customized_filters_with_options(request, runtime)

    def deploy_function_file_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iovcc_20180501_models.DeployFunctionFileResponse(),
            self.do_rpcrequest('DeployFunctionFile', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def deploy_function_file(self, request):
        runtime = util_models.RuntimeOptions()
        return self.deploy_function_file_with_options(request, runtime)

    def list_assist_action_details_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            iovcc_20180501_models.ListAssistActionDetailsResponse(),
            self.do_rpcrequest('ListAssistActionDetails', '2018-05-01', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def list_assist_action_details(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_assist_action_details_with_options(request, runtime)

    def describe_mqtt_topic_subscription_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iovcc_20180501_models.DescribeMqttTopicSubscriptionResponse(),
            self.do_rpcrequest('DescribeMqttTopicSubscription', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_mqtt_topic_subscription(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_mqtt_topic_subscription_with_options(request, runtime)

    def push_version_message_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iovcc_20180501_models.PushVersionMessageResponse(),
            self.do_rpcrequest('PushVersionMessage', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def push_version_message(self, request):
        runtime = util_models.RuntimeOptions()
        return self.push_version_message_with_options(request, runtime)

    def count_device_models_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            iovcc_20180501_models.CountDeviceModelsResponse(),
            self.do_rpcrequest('CountDeviceModels', '2018-05-01', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def count_device_models(self, request):
        runtime = util_models.RuntimeOptions()
        return self.count_device_models_with_options(request, runtime)

    def create_device_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iovcc_20180501_models.CreateDeviceResponse(),
            self.do_rpcrequest('CreateDevice', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_device(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_device_with_options(request, runtime)

    def create_namespace_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iovcc_20180501_models.CreateNamespaceResponse(),
            self.do_rpcrequest('CreateNamespace', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_namespace(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_namespace_with_options(request, runtime)

    def find_version_device_groups_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iovcc_20180501_models.FindVersionDeviceGroupsResponse(),
            self.do_rpcrequest('FindVersionDeviceGroups', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def find_version_device_groups(self, request):
        runtime = util_models.RuntimeOptions()
        return self.find_version_device_groups_with_options(request, runtime)

    def execute_remote_command_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iovcc_20180501_models.ExecuteRemoteCommandResponse(),
            self.do_rpcrequest('ExecuteRemoteCommand', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def execute_remote_command(self, request):
        runtime = util_models.RuntimeOptions()
        return self.execute_remote_command_with_options(request, runtime)

    def create_version_device_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iovcc_20180501_models.CreateVersionDeviceGroupResponse(),
            self.do_rpcrequest('CreateVersionDeviceGroup', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_version_device_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_version_device_group_with_options(request, runtime)

    def describe_assist_report_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            iovcc_20180501_models.DescribeAssistReportResponse(),
            self.do_rpcrequest('DescribeAssistReport', '2018-05-01', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def describe_assist_report(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_assist_report_with_options(request, runtime)

    def list_connect_logs_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iovcc_20180501_models.ListConnectLogsResponse(),
            self.do_rpcrequest('ListConnectLogs', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_connect_logs(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_connect_logs_with_options(request, runtime)

    def list_client_plugins_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iovcc_20180501_models.ListClientPluginsResponse(),
            self.do_rpcrequest('ListClientPlugins', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_client_plugins(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_client_plugins_with_options(request, runtime)

    def describe_shadow_schema_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iovcc_20180501_models.DescribeShadowSchemaResponse(),
            self.do_rpcrequest('DescribeShadowSchema', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_shadow_schema(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_shadow_schema_with_options(request, runtime)

    def find_version_black_devices_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iovcc_20180501_models.FindVersionBlackDevicesResponse(),
            self.do_rpcrequest('FindVersionBlackDevices', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def find_version_black_devices(self, request):
        runtime = util_models.RuntimeOptions()
        return self.find_version_black_devices_with_options(request, runtime)

    def list_function_files_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iovcc_20180501_models.ListFunctionFilesResponse(),
            self.do_rpcrequest('ListFunctionFiles', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_function_files(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_function_files_with_options(request, runtime)

    def update_namespace_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iovcc_20180501_models.UpdateNamespaceDataResponse(),
            self.do_rpcrequest('UpdateNamespaceData', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_namespace_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_namespace_data_with_options(request, runtime)

    def list_edge_devices_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iovcc_20180501_models.ListEdgeDevicesResponse(),
            self.do_rpcrequest('ListEdgeDevices', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_edge_devices(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_edge_devices_with_options(request, runtime)

    def delete_customized_property_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iovcc_20180501_models.DeleteCustomizedPropertyResponse(),
            self.do_rpcrequest('DeleteCustomizedProperty', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_customized_property(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_customized_property_with_options(request, runtime)

    def update_app_version_release_note_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iovcc_20180501_models.UpdateAppVersionReleaseNoteResponse(),
            self.do_rpcrequest('UpdateAppVersionReleaseNote', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_app_version_release_note(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_app_version_release_note_with_options(request, runtime)

    def create_trigger_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iovcc_20180501_models.CreateTriggerResponse(),
            self.do_rpcrequest('CreateTrigger', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_trigger(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_trigger_with_options(request, runtime)

    def diagnosis_version_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iovcc_20180501_models.DiagnosisVersionResponse(),
            self.do_rpcrequest('DiagnosisVersion', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def diagnosis_version(self, request):
        runtime = util_models.RuntimeOptions()
        return self.diagnosis_version_with_options(request, runtime)

    def list_shadow_schema_device_models_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            iovcc_20180501_models.ListShadowSchemaDeviceModelsResponse(),
            self.do_rpcrequest('ListShadowSchemaDeviceModels', '2018-05-01', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def list_shadow_schema_device_models(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_shadow_schema_device_models_with_options(request, runtime)

    def push_config_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iovcc_20180501_models.PushConfigInfoResponse(),
            self.do_rpcrequest('PushConfigInfo', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def push_config_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.push_config_info_with_options(request, runtime)

    def generate_oss_upload_meta_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iovcc_20180501_models.GenerateOssUploadMetaResponse(),
            self.do_rpcrequest('GenerateOssUploadMeta', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def generate_oss_upload_meta(self, request):
        runtime = util_models.RuntimeOptions()
        return self.generate_oss_upload_meta_with_options(request, runtime)

    def add_version_black_devices_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iovcc_20180501_models.AddVersionBlackDevicesResponse(),
            self.do_rpcrequest('AddVersionBlackDevices', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def add_version_black_devices(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_version_black_devices_with_options(request, runtime)

    def describe_customized_filter_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iovcc_20180501_models.DescribeCustomizedFilterResponse(),
            self.do_rpcrequest('DescribeCustomizedFilter', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_customized_filter(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_customized_filter_with_options(request, runtime)

    def describe_device_id_by_outer_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            iovcc_20180501_models.DescribeDeviceIdByOuterInfoResponse(),
            self.do_rpcrequest('DescribeDeviceIdByOuterInfo', '2018-05-01', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def describe_device_id_by_outer_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_device_id_by_outer_info_with_options(request, runtime)

    def create_app_version_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iovcc_20180501_models.CreateAppVersionResponse(),
            self.do_rpcrequest('CreateAppVersion', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_app_version(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_app_version_with_options(request, runtime)

    def count_activated_or_new_registration_device_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iovcc_20180501_models.CountActivatedOrNewRegistrationDeviceResponse(),
            self.do_rpcrequest('CountActivatedOrNewRegistrationDevice', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def count_activated_or_new_registration_device(self, request):
        runtime = util_models.RuntimeOptions()
        return self.count_activated_or_new_registration_device_with_options(request, runtime)

    def list_devices_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            iovcc_20180501_models.ListDevicesResponse(),
            self.do_rpcrequest('ListDevices', '2018-05-01', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def list_devices(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_devices_with_options(request, runtime)

    def find_version_tests_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iovcc_20180501_models.FindVersionTestsResponse(),
            self.do_rpcrequest('FindVersionTests', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def find_version_tests(self, request):
        runtime = util_models.RuntimeOptions()
        return self.find_version_tests_with_options(request, runtime)

    def publish_os_version_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iovcc_20180501_models.PublishOsVersionResponse(),
            self.do_rpcrequest('PublishOsVersion', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def publish_os_version(self, request):
        runtime = util_models.RuntimeOptions()
        return self.publish_os_version_with_options(request, runtime)

    def create_upstream_app_key_relations_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iovcc_20180501_models.CreateUpstreamAppKeyRelationsResponse(),
            self.do_rpcrequest('CreateUpstreamAppKeyRelations', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_upstream_app_key_relations(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_upstream_app_key_relations_with_options(request, runtime)

    def update_os_version_release_note_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iovcc_20180501_models.UpdateOsVersionReleaseNoteResponse(),
            self.do_rpcrequest('UpdateOsVersionReleaseNote', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_os_version_release_note(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_os_version_release_note_with_options(request, runtime)

    def publish_app_version_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iovcc_20180501_models.PublishAppVersionResponse(),
            self.do_rpcrequest('PublishAppVersion', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def publish_app_version(self, request):
        runtime = util_models.RuntimeOptions()
        return self.publish_app_version_with_options(request, runtime)

    def publish_mqtt_message_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iovcc_20180501_models.PublishMqttMessageResponse(),
            self.do_rpcrequest('PublishMqttMessage', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def publish_mqtt_message(self, request):
        runtime = util_models.RuntimeOptions()
        return self.publish_mqtt_message_with_options(request, runtime)

    def delete_version_group_device_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iovcc_20180501_models.DeleteVersionGroupDeviceResponse(),
            self.do_rpcrequest('DeleteVersionGroupDevice', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_version_group_device(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_version_group_device_with_options(request, runtime)

    def delete_function_file_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iovcc_20180501_models.DeleteFunctionFileResponse(),
            self.do_rpcrequest('DeleteFunctionFile', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_function_file(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_function_file_with_options(request, runtime)

    def add_version_white_devices_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iovcc_20180501_models.AddVersionWhiteDevicesResponse(),
            self.do_rpcrequest('AddVersionWhiteDevices', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def add_version_white_devices(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_version_white_devices_with_options(request, runtime)

    def list_assist_history_details_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            iovcc_20180501_models.ListAssistHistoryDetailsResponse(),
            self.do_rpcrequest('ListAssistHistoryDetails', '2018-05-01', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def list_assist_history_details(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_assist_history_details_with_options(request, runtime)

    def create_customized_filter_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iovcc_20180501_models.CreateCustomizedFilterResponse(),
            self.do_rpcrequest('CreateCustomizedFilter', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_customized_filter(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_customized_filter_with_options(request, runtime)

    def delete_upstream_app_key_relation_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iovcc_20180501_models.DeleteUpstreamAppKeyRelationResponse(),
            self.do_rpcrequest('DeleteUpstreamAppKeyRelation', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_upstream_app_key_relation(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_upstream_app_key_relation_with_options(request, runtime)

    def describe_app_version_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iovcc_20180501_models.DescribeAppVersionResponse(),
            self.do_rpcrequest('DescribeAppVersion', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_app_version(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_app_version_with_options(request, runtime)

    def list_vehicle_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            iovcc_20180501_models.ListVehicleResponse(),
            self.do_rpcrequest('ListVehicle', '2018-05-01', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def list_vehicle(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_vehicle_with_options(request, runtime)

    def execute_camera_shooting_command_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iovcc_20180501_models.ExecuteCameraShootingCommandResponse(),
            self.do_rpcrequest('ExecuteCameraShootingCommand', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def execute_camera_shooting_command(self, request):
        runtime = util_models.RuntimeOptions()
        return self.execute_camera_shooting_command_with_options(request, runtime)

    def delete_version_device_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iovcc_20180501_models.DeleteVersionDeviceGroupResponse(),
            self.do_rpcrequest('DeleteVersionDeviceGroup', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_version_device_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_version_device_group_with_options(request, runtime)

    def list_function_files_by_project_id_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iovcc_20180501_models.ListFunctionFilesByProjectIdResponse(),
            self.do_rpcrequest('ListFunctionFilesByProjectId', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_function_files_by_project_id(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_function_files_by_project_id_with_options(request, runtime)

    def find_version_white_devices_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iovcc_20180501_models.FindVersionWhiteDevicesResponse(),
            self.do_rpcrequest('FindVersionWhiteDevices', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def find_version_white_devices(self, request):
        runtime = util_models.RuntimeOptions()
        return self.find_version_white_devices_with_options(request, runtime)

    def create_upstream_app_server_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iovcc_20180501_models.CreateUpstreamAppServerResponse(),
            self.do_rpcrequest('CreateUpstreamAppServer', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_upstream_app_server(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_upstream_app_server_with_options(request, runtime)

    def describe_version_device_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iovcc_20180501_models.DescribeVersionDeviceGroupResponse(),
            self.do_rpcrequest('DescribeVersionDeviceGroup', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_version_device_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_version_device_group_with_options(request, runtime)

    def update_app_version_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iovcc_20180501_models.UpdateAppVersionResponse(),
            self.do_rpcrequest('UpdateAppVersion', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_app_version(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_app_version_with_options(request, runtime)

    def create_customized_property_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iovcc_20180501_models.CreateCustomizedPropertyResponse(),
            self.do_rpcrequest('CreateCustomizedProperty', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_customized_property(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_customized_property_with_options(request, runtime)

    def list_schema_subscribes_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            iovcc_20180501_models.ListSchemaSubscribesResponse(),
            self.do_rpcrequest('ListSchemaSubscribes', '2018-05-01', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def list_schema_subscribes(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_schema_subscribes_with_options(request, runtime)

    def update_schema_subscribe_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iovcc_20180501_models.UpdateSchemaSubscribeResponse(),
            self.do_rpcrequest('UpdateSchemaSubscribe', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_schema_subscribe(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_schema_subscribe_with_options(request, runtime)

    def delete_all_version_group_devices_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iovcc_20180501_models.DeleteAllVersionGroupDevicesResponse(),
            self.do_rpcrequest('DeleteAllVersionGroupDevices', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_all_version_group_devices(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_all_version_group_devices_with_options(request, runtime)

    def delete_version_white_devices_by_id_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iovcc_20180501_models.DeleteVersionWhiteDevicesByIdResponse(),
            self.do_rpcrequest('DeleteVersionWhiteDevicesById', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_version_white_devices_by_id(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_version_white_devices_by_id_with_options(request, runtime)

    def update_os_version_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iovcc_20180501_models.UpdateOsVersionResponse(),
            self.do_rpcrequest('UpdateOsVersion', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_os_version(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_os_version_with_options(request, runtime)

    def generate_oss_post_policy_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iovcc_20180501_models.GenerateOssPostPolicyResponse(),
            self.do_rpcrequest('GenerateOssPostPolicy', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def generate_oss_post_policy(self, request):
        runtime = util_models.RuntimeOptions()
        return self.generate_oss_post_policy_with_options(request, runtime)

    def find_version_group_devices_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iovcc_20180501_models.FindVersionGroupDevicesResponse(),
            self.do_rpcrequest('FindVersionGroupDevices', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def find_version_group_devices(self, request):
        runtime = util_models.RuntimeOptions()
        return self.find_version_group_devices_with_options(request, runtime)

    def delete_open_account_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            iovcc_20180501_models.DeleteOpenAccountResponse(),
            self.do_rpcrequest('DeleteOpenAccount', '2018-05-01', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def delete_open_account(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_open_account_with_options(request, runtime)

    def describe_default_schema_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iovcc_20180501_models.DescribeDefaultSchemaResponse(),
            self.do_rpcrequest('DescribeDefaultSchema', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_default_schema(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_default_schema_with_options(request, runtime)

    def list_upstream_app_servers_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iovcc_20180501_models.ListUpstreamAppServersResponse(),
            self.do_rpcrequest('ListUpstreamAppServers', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_upstream_app_servers(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_upstream_app_servers_with_options(request, runtime)

    def delete_version_test_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iovcc_20180501_models.DeleteVersionTestResponse(),
            self.do_rpcrequest('DeleteVersionTest', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_version_test(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_version_test_with_options(request, runtime)

    def create_upstream_app_key_relation_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iovcc_20180501_models.CreateUpstreamAppKeyRelationResponse(),
            self.do_rpcrequest('CreateUpstreamAppKeyRelation', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_upstream_app_key_relation(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_upstream_app_key_relation_with_options(request, runtime)

    def find_app_versions_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iovcc_20180501_models.FindAppVersionsResponse(),
            self.do_rpcrequest('FindAppVersions', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def find_app_versions(self, request):
        runtime = util_models.RuntimeOptions()
        return self.find_app_versions_with_options(request, runtime)

    def list_mqtt_root_topics_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iovcc_20180501_models.ListMqttRootTopicsResponse(),
            self.do_rpcrequest('ListMqttRootTopics', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_mqtt_root_topics(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_mqtt_root_topics_with_options(request, runtime)

    def list_assist_devices_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            iovcc_20180501_models.ListAssistDevicesResponse(),
            self.do_rpcrequest('ListAssistDevices', '2018-05-01', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def list_assist_devices(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_assist_devices_with_options(request, runtime)

    def delete_upstream_app_server_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iovcc_20180501_models.DeleteUpstreamAppServerResponse(),
            self.do_rpcrequest('DeleteUpstreamAppServer', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_upstream_app_server(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_upstream_app_server_with_options(request, runtime)

    def update_version_device_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iovcc_20180501_models.UpdateVersionDeviceGroupResponse(),
            self.do_rpcrequest('UpdateVersionDeviceGroup', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_version_device_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_version_device_group_with_options(request, runtime)

    def list_open_accounts_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            iovcc_20180501_models.ListOpenAccountsResponse(),
            self.do_rpcrequest('ListOpenAccounts', '2018-05-01', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def list_open_accounts(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_open_accounts_with_options(request, runtime)

    def update_os_version_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iovcc_20180501_models.UpdateOsVersionStatusResponse(),
            self.do_rpcrequest('UpdateOsVersionStatus', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_os_version_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_os_version_status_with_options(request, runtime)

    def count_projects_with_options(self, runtime):
        req = open_api_models.OpenApiRequest()
        return TeaCore.from_map(
            iovcc_20180501_models.CountProjectsResponse(),
            self.do_rpcrequest('CountProjects', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def count_projects(self):
        runtime = util_models.RuntimeOptions()
        return self.count_projects_with_options(runtime)

    def list_commercial_vehicle_devices_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iovcc_20180501_models.ListCommercialVehicleDevicesResponse(),
            self.do_rpcrequest('ListCommercialVehicleDevices', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_commercial_vehicle_devices(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_commercial_vehicle_devices_with_options(request, runtime)

    def list_message_receivers_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iovcc_20180501_models.ListMessageReceiversResponse(),
            self.do_rpcrequest('ListMessageReceivers', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_message_receivers(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_message_receivers_with_options(request, runtime)

    def count_devices_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            iovcc_20180501_models.CountDevicesResponse(),
            self.do_rpcrequest('CountDevices', '2018-05-01', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def count_devices(self, request):
        runtime = util_models.RuntimeOptions()
        return self.count_devices_with_options(request, runtime)

    def update_os_black_white_versions_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iovcc_20180501_models.UpdateOsBlackWhiteVersionsResponse(),
            self.do_rpcrequest('UpdateOsBlackWhiteVersions', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_os_black_white_versions(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_os_black_white_versions_with_options(request, runtime)

    def get_namespace_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iovcc_20180501_models.GetNamespaceDataResponse(),
            self.do_rpcrequest('GetNamespaceData', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_namespace_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_namespace_data_with_options(request, runtime)

    def update_os_version_remark_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iovcc_20180501_models.UpdateOsVersionRemarkResponse(),
            self.do_rpcrequest('UpdateOsVersionRemark', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_os_version_remark(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_os_version_remark_with_options(request, runtime)

    def query_prepublish_passed_device_count_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iovcc_20180501_models.QueryPrepublishPassedDeviceCountResponse(),
            self.do_rpcrequest('QueryPrepublishPassedDeviceCount', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_prepublish_passed_device_count(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_prepublish_passed_device_count_with_options(request, runtime)

    def create_project_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iovcc_20180501_models.CreateProjectResponse(),
            self.do_rpcrequest('CreateProject', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_project(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_project_with_options(request, runtime)

    def list_namespaces_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iovcc_20180501_models.ListNamespacesResponse(),
            self.do_rpcrequest('ListNamespaces', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_namespaces(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_namespaces_with_options(request, runtime)

    def list_support_features_with_options(self, runtime):
        req = open_api_models.OpenApiRequest()
        return TeaCore.from_map(
            iovcc_20180501_models.ListSupportFeaturesResponse(),
            self.do_rpcrequest('ListSupportFeatures', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_support_features(self):
        runtime = util_models.RuntimeOptions()
        return self.list_support_features_with_options(runtime)

    def delete_mqtt_root_topic_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iovcc_20180501_models.DeleteMqttRootTopicResponse(),
            self.do_rpcrequest('DeleteMqttRootTopic', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_mqtt_root_topic(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_mqtt_root_topic_with_options(request, runtime)

    def delete_version_group_device_by_id_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iovcc_20180501_models.DeleteVersionGroupDeviceByIdResponse(),
            self.do_rpcrequest('DeleteVersionGroupDeviceById', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_version_group_device_by_id(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_version_group_device_by_id_with_options(request, runtime)

    def list_client_plugin_versions_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iovcc_20180501_models.ListClientPluginVersionsResponse(),
            self.do_rpcrequest('ListClientPluginVersions', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_client_plugin_versions(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_client_plugin_versions_with_options(request, runtime)

    def find_version_message_send_records_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iovcc_20180501_models.FindVersionMessageSendRecordsResponse(),
            self.do_rpcrequest('FindVersionMessageSendRecords', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def find_version_message_send_records(self, request):
        runtime = util_models.RuntimeOptions()
        return self.find_version_message_send_records_with_options(request, runtime)

    def generate_sys_app_download_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iovcc_20180501_models.GenerateSysAppDownloadInfoResponse(),
            self.do_rpcrequest('GenerateSysAppDownloadInfo', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def generate_sys_app_download_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.generate_sys_app_download_info_with_options(request, runtime)

    def delete_trigger_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iovcc_20180501_models.DeleteTriggerResponse(),
            self.do_rpcrequest('DeleteTrigger', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_trigger(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_trigger_with_options(request, runtime)

    def describe_device_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            iovcc_20180501_models.DescribeDeviceInfoResponse(),
            self.do_rpcrequest('DescribeDeviceInfo', '2018-05-01', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def describe_device_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_device_info_with_options(request, runtime)

    def create_device_model_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iovcc_20180501_models.CreateDeviceModelResponse(),
            self.do_rpcrequest('CreateDeviceModel', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_device_model(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_device_model_with_options(request, runtime)

    def update_app_version_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iovcc_20180501_models.UpdateAppVersionStatusResponse(),
            self.do_rpcrequest('UpdateAppVersionStatus', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_app_version_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_app_version_status_with_options(request, runtime)

    def update_shadow_schema_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iovcc_20180501_models.UpdateShadowSchemaResponse(),
            self.do_rpcrequest('UpdateShadowSchema', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_shadow_schema(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_shadow_schema_with_options(request, runtime)

    def describe_device_shadow_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iovcc_20180501_models.DescribeDeviceShadowResponse(),
            self.do_rpcrequest('DescribeDeviceShadow', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_device_shadow(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_device_shadow_with_options(request, runtime)

    def list_triggers_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iovcc_20180501_models.ListTriggersResponse(),
            self.do_rpcrequest('ListTriggers', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_triggers(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_triggers_with_options(request, runtime)

    def update_customized_filter_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iovcc_20180501_models.UpdateCustomizedFilterResponse(),
            self.do_rpcrequest('UpdateCustomizedFilter', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_customized_filter(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_customized_filter_with_options(request, runtime)

    def create_version_prepublish_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iovcc_20180501_models.CreateVersionPrepublishResponse(),
            self.do_rpcrequest('CreateVersionPrepublish', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_version_prepublish(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_version_prepublish_with_options(request, runtime)

    def update_app_version_remark_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iovcc_20180501_models.UpdateAppVersionRemarkResponse(),
            self.do_rpcrequest('UpdateAppVersionRemark', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_app_version_remark(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_app_version_remark_with_options(request, runtime)

    def describe_device_model_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            iovcc_20180501_models.DescribeDeviceModelResponse(),
            self.do_rpcrequest('DescribeDeviceModel', '2018-05-01', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def describe_device_model(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_device_model_with_options(request, runtime)

    def list_device_types_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            iovcc_20180501_models.ListDeviceTypesResponse(),
            self.do_rpcrequest('ListDeviceTypes', '2018-05-01', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def list_device_types(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_device_types_with_options(request, runtime)

    def generate_sdk_download_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iovcc_20180501_models.GenerateSdkDownloadInfoResponse(),
            self.do_rpcrequest('GenerateSdkDownloadInfo', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def generate_sdk_download_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.generate_sdk_download_info_with_options(request, runtime)

    def execute_vehicle_control_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iovcc_20180501_models.ExecuteVehicleControlResponse(),
            self.do_rpcrequest('ExecuteVehicleControl', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def execute_vehicle_control(self, request):
        runtime = util_models.RuntimeOptions()
        return self.execute_vehicle_control_with_options(request, runtime)

    def describe_api_gateway_app_security_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iovcc_20180501_models.DescribeApiGatewayAppSecurityResponse(),
            self.do_rpcrequest('DescribeApiGatewayAppSecurity', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_api_gateway_app_security(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_api_gateway_app_security_with_options(request, runtime)

    def describe_device_online_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iovcc_20180501_models.DescribeDeviceOnlineInfoResponse(),
            self.do_rpcrequest('DescribeDeviceOnlineInfo', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_device_online_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_device_online_info_with_options(request, runtime)

    def create_rpc_service_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iovcc_20180501_models.CreateRpcServiceResponse(),
            self.do_rpcrequest('CreateRpcService', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_rpc_service(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_rpc_service_with_options(request, runtime)

    def delete_version_white_devices_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iovcc_20180501_models.DeleteVersionWhiteDevicesResponse(),
            self.do_rpcrequest('DeleteVersionWhiteDevices', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_version_white_devices(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_version_white_devices_with_options(request, runtime)

    def list_projects_with_options(self, runtime):
        req = open_api_models.OpenApiRequest()
        return TeaCore.from_map(
            iovcc_20180501_models.ListProjectsResponse(),
            self.do_rpcrequest('ListProjects', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_projects(self):
        runtime = util_models.RuntimeOptions()
        return self.list_projects_with_options(runtime)

    def generate_function_file_upload_meta_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iovcc_20180501_models.GenerateFunctionFileUploadMetaResponse(),
            self.do_rpcrequest('GenerateFunctionFileUploadMeta', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def generate_function_file_upload_meta(self, request):
        runtime = util_models.RuntimeOptions()
        return self.generate_function_file_upload_meta_with_options(request, runtime)

    def describe_project_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iovcc_20180501_models.DescribeProjectResponse(),
            self.do_rpcrequest('DescribeProject', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_project(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_project_with_options(request, runtime)

    def describe_mqtt_message_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iovcc_20180501_models.DescribeMqttMessageResponse(),
            self.do_rpcrequest('DescribeMqttMessage', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_mqtt_message(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_mqtt_message_with_options(request, runtime)

    def list_camera_shooting_records_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iovcc_20180501_models.ListCameraShootingRecordsResponse(),
            self.do_rpcrequest('ListCameraShootingRecords', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_camera_shooting_records(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_camera_shooting_records_with_options(request, runtime)

    def delete_version_black_devices_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iovcc_20180501_models.DeleteVersionBlackDevicesResponse(),
            self.do_rpcrequest('DeleteVersionBlackDevices', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_version_black_devices(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_version_black_devices_with_options(request, runtime)

    def describe_os_version_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iovcc_20180501_models.DescribeOsVersionResponse(),
            self.do_rpcrequest('DescribeOsVersion', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_os_version(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_os_version_with_options(request, runtime)

    def list_rpc_services_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iovcc_20180501_models.ListRpcServicesResponse(),
            self.do_rpcrequest('ListRpcServices', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_rpc_services(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_rpc_services_with_options(request, runtime)

    def delete_schema_subscribe_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iovcc_20180501_models.DeleteSchemaSubscribeResponse(),
            self.do_rpcrequest('DeleteSchemaSubscribe', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_schema_subscribe(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_schema_subscribe_with_options(request, runtime)

    def add_uploaded_function_file_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iovcc_20180501_models.AddUploadedFunctionFileInfoResponse(),
            self.do_rpcrequest('AddUploadedFunctionFileInfo', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def add_uploaded_function_file_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_uploaded_function_file_info_with_options(request, runtime)

    def create_project_app_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iovcc_20180501_models.CreateProjectAppResponse(),
            self.do_rpcrequest('CreateProjectApp', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_project_app(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_project_app_with_options(request, runtime)

    def list_services_with_options(self, runtime):
        req = open_api_models.OpenApiRequest()
        return TeaCore.from_map(
            iovcc_20180501_models.ListServicesResponse(),
            self.do_rpcrequest('ListServices', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_services(self):
        runtime = util_models.RuntimeOptions()
        return self.list_services_with_options(runtime)

    def find_os_versions_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iovcc_20180501_models.FindOsVersionsResponse(),
            self.do_rpcrequest('FindOsVersions', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def find_os_versions(self, request):
        runtime = util_models.RuntimeOptions()
        return self.find_os_versions_with_options(request, runtime)

    def update_version_prepublish_active_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iovcc_20180501_models.UpdateVersionPrepublishActiveStatusResponse(),
            self.do_rpcrequest('UpdateVersionPrepublishActiveStatus', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_version_prepublish_active_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_version_prepublish_active_status_with_options(request, runtime)

    def create_os_version_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iovcc_20180501_models.CreateOsVersionResponse(),
            self.do_rpcrequest('CreateOsVersion', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_os_version(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_os_version_with_options(request, runtime)

    def count_device_brands_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            iovcc_20180501_models.CountDeviceBrandsResponse(),
            self.do_rpcrequest('CountDeviceBrands', '2018-05-01', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def count_device_brands(self, request):
        runtime = util_models.RuntimeOptions()
        return self.count_device_brands_with_options(request, runtime)

    def describe_device_brand_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            iovcc_20180501_models.DescribeDeviceBrandResponse(),
            self.do_rpcrequest('DescribeDeviceBrand', '2018-05-01', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def describe_device_brand(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_device_brand_with_options(request, runtime)

    def create_shadow_schema_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iovcc_20180501_models.CreateShadowSchemaResponse(),
            self.do_rpcrequest('CreateShadowSchema', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_shadow_schema(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_shadow_schema_with_options(request, runtime)

    def describe_device_validity_schema_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iovcc_20180501_models.DescribeDeviceValiditySchemaResponse(),
            self.do_rpcrequest('DescribeDeviceValiditySchema', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_device_validity_schema(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_device_validity_schema_with_options(request, runtime)

    def get_oss_upload_meta_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iovcc_20180501_models.GetOssUploadMetaResponse(),
            self.do_rpcrequest('GetOssUploadMeta', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_oss_upload_meta(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_oss_upload_meta_with_options(request, runtime)

    def list_upstream_app_key_relations_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iovcc_20180501_models.ListUpstreamAppKeyRelationsResponse(),
            self.do_rpcrequest('ListUpstreamAppKeyRelations', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_upstream_app_key_relations(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_upstream_app_key_relations_with_options(request, runtime)

    def list_shadow_schemas_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iovcc_20180501_models.ListShadowSchemasResponse(),
            self.do_rpcrequest('ListShadowSchemas', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_shadow_schemas(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_shadow_schemas_with_options(request, runtime)

    def delete_project_app_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iovcc_20180501_models.DeleteProjectAppResponse(),
            self.do_rpcrequest('DeleteProjectApp', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_project_app(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_project_app_with_options(request, runtime)

    def count_yun_id_info_with_options(self, runtime):
        req = open_api_models.OpenApiRequest()
        return TeaCore.from_map(
            iovcc_20180501_models.CountYunIdInfoResponse(),
            self.do_rpcrequest('CountYunIdInfo', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def count_yun_id_info(self):
        runtime = util_models.RuntimeOptions()
        return self.count_yun_id_info_with_options(runtime)

    def find_prepublishes_by_parent_id_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iovcc_20180501_models.FindPrepublishesByParentIdResponse(),
            self.do_rpcrequest('FindPrepublishesByParentId', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def find_prepublishes_by_parent_id(self, request):
        runtime = util_models.RuntimeOptions()
        return self.find_prepublishes_by_parent_id_with_options(request, runtime)

    def get_vehicle_control_result_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            iovcc_20180501_models.GetVehicleControlResultResponse(),
            self.do_rpcrequest('GetVehicleControlResult', '2018-05-01', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def get_vehicle_control_result(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_vehicle_control_result_with_options(request, runtime)

    def update_trigger_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iovcc_20180501_models.UpdateTriggerResponse(),
            self.do_rpcrequest('UpdateTrigger', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_trigger(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_trigger_with_options(request, runtime)

    def list_client_sdks_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iovcc_20180501_models.ListClientSdksResponse(),
            self.do_rpcrequest('ListClientSdks', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_client_sdks(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_client_sdks_with_options(request, runtime)

    def list_version_device_groups_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iovcc_20180501_models.ListVersionDeviceGroupsResponse(),
            self.do_rpcrequest('ListVersionDeviceGroups', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_version_device_groups(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_version_device_groups_with_options(request, runtime)

    def get_commercial_vehicle_device_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iovcc_20180501_models.GetCommercialVehicleDeviceResponse(),
            self.do_rpcrequest('GetCommercialVehicleDevice', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_commercial_vehicle_device(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_commercial_vehicle_device_with_options(request, runtime)

    def submit_assist_report_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iovcc_20180501_models.SubmitAssistReportResponse(),
            self.do_rpcrequest('SubmitAssistReport', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def submit_assist_report(self, request):
        runtime = util_models.RuntimeOptions()
        return self.submit_assist_report_with_options(request, runtime)

    def delete_version_all_black_devices_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iovcc_20180501_models.DeleteVersionAllBlackDevicesResponse(),
            self.do_rpcrequest('DeleteVersionAllBlackDevices', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_version_all_black_devices(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_version_all_black_devices_with_options(request, runtime)

    def list_open_account_links_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            iovcc_20180501_models.ListOpenAccountLinksResponse(),
            self.do_rpcrequest('ListOpenAccountLinks', '2018-05-01', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def list_open_account_links(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_open_account_links_with_options(request, runtime)

    def add_version_white_devices_by_device_groups_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iovcc_20180501_models.AddVersionWhiteDevicesByDeviceGroupsResponse(),
            self.do_rpcrequest('AddVersionWhiteDevicesByDeviceGroups', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def add_version_white_devices_by_device_groups(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_version_white_devices_by_device_groups_with_options(request, runtime)

    def find_customized_properties_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iovcc_20180501_models.FindCustomizedPropertiesResponse(),
            self.do_rpcrequest('FindCustomizedProperties', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def find_customized_properties(self, request):
        runtime = util_models.RuntimeOptions()
        return self.find_customized_properties_with_options(request, runtime)

    def list_message_acks_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iovcc_20180501_models.ListMessageAcksResponse(),
            self.do_rpcrequest('ListMessageAcks', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_message_acks(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_message_acks_with_options(request, runtime)

    def get_commercial_vehicle_track_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iovcc_20180501_models.GetCommercialVehicleTrackResponse(),
            self.do_rpcrequest('GetCommercialVehicleTrack', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_commercial_vehicle_track(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_commercial_vehicle_track_with_options(request, runtime)

    def list_host_devices_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iovcc_20180501_models.ListHostDevicesResponse(),
            self.do_rpcrequest('ListHostDevices', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_host_devices(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_host_devices_with_options(request, runtime)

    def list_mqtt_client_subscriptions_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iovcc_20180501_models.ListMqttClientSubscriptionsResponse(),
            self.do_rpcrequest('ListMqttClientSubscriptions', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_mqtt_client_subscriptions(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_mqtt_client_subscriptions_with_options(request, runtime)

    def invoke_function_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iovcc_20180501_models.InvokeFunctionResponse(),
            self.do_rpcrequest('InvokeFunction', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def invoke_function(self, request):
        runtime = util_models.RuntimeOptions()
        return self.invoke_function_with_options(request, runtime)

    def delete_version_all_white_devices_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iovcc_20180501_models.DeleteVersionAllWhiteDevicesResponse(),
            self.do_rpcrequest('DeleteVersionAllWhiteDevices', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_version_all_white_devices(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_version_all_white_devices_with_options(request, runtime)

    def describe_message_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iovcc_20180501_models.DescribeMessageResponse(),
            self.do_rpcrequest('DescribeMessage', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_message(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_message_with_options(request, runtime)

    def update_project_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iovcc_20180501_models.UpdateProjectResponse(),
            self.do_rpcrequest('UpdateProject', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_project(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_project_with_options(request, runtime)

    def update_app_black_white_versions_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iovcc_20180501_models.UpdateAppBlackWhiteVersionsResponse(),
            self.do_rpcrequest('UpdateAppBlackWhiteVersions', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_app_black_white_versions(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_app_black_white_versions_with_options(request, runtime)

    def get_device_app_update_funnel_events_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iovcc_20180501_models.GetDeviceAppUpdateFunnelEventsResponse(),
            self.do_rpcrequest('GetDeviceAppUpdateFunnelEvents', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_device_app_update_funnel_events(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_device_app_update_funnel_events_with_options(request, runtime)

    def get_namespace_statistics_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            iovcc_20180501_models.GetNamespaceStatisticsDataResponse(),
            self.do_rpcrequest('GetNamespaceStatisticsData', '2018-05-01', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_namespace_statistics_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_namespace_statistics_data_with_options(request, runtime)
