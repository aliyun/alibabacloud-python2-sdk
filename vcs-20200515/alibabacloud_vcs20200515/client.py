# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_vcs20200515 import models as vcs_20200515_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_openapi_util.client import Client as OpenApiUtilClient


class Client(OpenApiClient):
    """
    *\
    """
    def __init__(self, config):
        super(Client, self).__init__(config)
        self._signature_algorithm = 'v2'
        self._endpoint_rule = 'regional'
        self.check_config(config)
        self._endpoint = self.get_endpoint('vcs', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def add_aiot_devices_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = vcs_20200515_models.AddAiotDevicesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.aiot_device_list):
            request.aiot_device_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.aiot_device_list, 'AiotDeviceList', 'json')
        body = {}
        if not UtilClient.is_unset(request.aiot_device_list_shrink):
            body['AiotDeviceList'] = request.aiot_device_list_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddAiotDevices',
            version='2020-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vcs_20200515_models.AddAiotDevicesResponse(),
            self.call_api(params, req, runtime)
        )

    def add_aiot_devices(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_aiot_devices_with_options(request, runtime)

    def add_aiot_person_table_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        body_flat = {}
        if not UtilClient.is_unset(request.person_table):
            body_flat['PersonTable'] = request.person_table
        body = TeaCore.merge(body,
            OpenApiUtilClient.query(body_flat))
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddAiotPersonTable',
            version='2020-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vcs_20200515_models.AddAiotPersonTableResponse(),
            self.call_api(params, req, runtime)
        )

    def add_aiot_person_table(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_aiot_person_table_with_options(request, runtime)

    def add_aiot_person_table_items_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.person_table_id):
            body['PersonTableId'] = request.person_table_id
        body_flat = {}
        if not UtilClient.is_unset(request.person_table_item_list):
            body_flat['PersonTableItemList'] = request.person_table_item_list
        body = TeaCore.merge(body,
            OpenApiUtilClient.query(body_flat))
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddAiotPersonTableItems',
            version='2020-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vcs_20200515_models.AddAiotPersonTableItemsResponse(),
            self.call_api(params, req, runtime)
        )

    def add_aiot_person_table_items(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_aiot_person_table_items_with_options(request, runtime)

    def add_aiot_person_table_items_for_tables_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        body_flat = {}
        if not UtilClient.is_unset(request.person_table_item_list):
            body_flat['PersonTableItemList'] = request.person_table_item_list
        if not UtilClient.is_unset(request.person_table_list):
            body_flat['PersonTableList'] = request.person_table_list
        body = TeaCore.merge(body,
            OpenApiUtilClient.query(body_flat))
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddAiotPersonTableItemsForTables',
            version='2020-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vcs_20200515_models.AddAiotPersonTableItemsForTablesResponse(),
            self.call_api(params, req, runtime)
        )

    def add_aiot_person_table_items_for_tables(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_aiot_person_table_items_for_tables_with_options(request, runtime)

    def add_aiot_vehicle_table_items_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = vcs_20200515_models.AddAiotVehicleTableItemsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.vehicle_table_item):
            request.vehicle_table_item_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.vehicle_table_item), 'VehicleTableItem', 'json')
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.vehicle_table_id):
            body['VehicleTableId'] = request.vehicle_table_id
        if not UtilClient.is_unset(request.vehicle_table_item_shrink):
            body['VehicleTableItem'] = request.vehicle_table_item_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddAiotVehicleTableItems',
            version='2020-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vcs_20200515_models.AddAiotVehicleTableItemsResponse(),
            self.call_api(params, req, runtime)
        )

    def add_aiot_vehicle_table_items(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_aiot_vehicle_table_items_with_options(request, runtime)

    def add_camera_for_instance_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = vcs_20200515_models.AddCameraForInstanceShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.camera_ids):
            request.camera_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.camera_ids, 'CameraIds', 'json')
        body = {}
        if not UtilClient.is_unset(request.camera_ids_shrink):
            body['CameraIds'] = request.camera_ids_shrink
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddCameraForInstance',
            version='2020-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vcs_20200515_models.AddCameraForInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    def add_camera_for_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_camera_for_instance_with_options(request, runtime)

    def add_channel_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.parent_device_gb_id):
            body['ParentDeviceGbId'] = request.parent_device_gb_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddChannel',
            version='2020-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vcs_20200515_models.AddChannelResponse(),
            self.call_api(params, req, runtime)
        )

    def add_channel(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_channel_with_options(request, runtime)

    def add_data_source_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.corp_id):
            body['CorpId'] = request.corp_id
        if not UtilClient.is_unset(request.data_source_name):
            body['DataSourceName'] = request.data_source_name
        if not UtilClient.is_unset(request.data_source_type):
            body['DataSourceType'] = request.data_source_type
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.url):
            body['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddDataSource',
            version='2020-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vcs_20200515_models.AddDataSourceResponse(),
            self.call_api(params, req, runtime)
        )

    def add_data_source(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_data_source_with_options(request, runtime)

    def add_device_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.bit_rate):
            body['BitRate'] = request.bit_rate
        if not UtilClient.is_unset(request.corp_id):
            body['CorpId'] = request.corp_id
        if not UtilClient.is_unset(request.device_address):
            body['DeviceAddress'] = request.device_address
        if not UtilClient.is_unset(request.device_direction):
            body['DeviceDirection'] = request.device_direction
        if not UtilClient.is_unset(request.device_name):
            body['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.device_resolution):
            body['DeviceResolution'] = request.device_resolution
        if not UtilClient.is_unset(request.device_site):
            body['DeviceSite'] = request.device_site
        if not UtilClient.is_unset(request.device_type):
            body['DeviceType'] = request.device_type
        if not UtilClient.is_unset(request.gb_id):
            body['GbId'] = request.gb_id
        if not UtilClient.is_unset(request.vendor):
            body['Vendor'] = request.vendor
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddDevice',
            version='2020-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vcs_20200515_models.AddDeviceResponse(),
            self.call_api(params, req, runtime)
        )

    def add_device(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_device_with_options(request, runtime)

    def add_double_verification_groups_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        body_flat = {}
        if not UtilClient.is_unset(request.double_verification_group_list):
            body_flat['DoubleVerificationGroupList'] = request.double_verification_group_list
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        body = TeaCore.merge(body,
            OpenApiUtilClient.query(body_flat))
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddDoubleVerificationGroups',
            version='2020-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vcs_20200515_models.AddDoubleVerificationGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    def add_double_verification_groups(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_double_verification_groups_with_options(request, runtime)

    def add_monitor_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.algorithm_vendor):
            body['AlgorithmVendor'] = request.algorithm_vendor
        if not UtilClient.is_unset(request.batch_indicator):
            body['BatchIndicator'] = request.batch_indicator
        if not UtilClient.is_unset(request.corp_id):
            body['CorpId'] = request.corp_id
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.monitor_type):
            body['MonitorType'] = request.monitor_type
        if not UtilClient.is_unset(request.notifier_app_secret):
            body['NotifierAppSecret'] = request.notifier_app_secret
        if not UtilClient.is_unset(request.notifier_extend_values):
            body['NotifierExtendValues'] = request.notifier_extend_values
        if not UtilClient.is_unset(request.notifier_time_out):
            body['NotifierTimeOut'] = request.notifier_time_out
        if not UtilClient.is_unset(request.notifier_type):
            body['NotifierType'] = request.notifier_type
        if not UtilClient.is_unset(request.notifier_url):
            body['NotifierUrl'] = request.notifier_url
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddMonitor',
            version='2020-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vcs_20200515_models.AddMonitorResponse(),
            self.call_api(params, req, runtime)
        )

    def add_monitor(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_monitor_with_options(request, runtime)

    def add_profile_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.biz_id):
            body['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.catalog_id):
            body['CatalogId'] = request.catalog_id
        if not UtilClient.is_unset(request.corp_id):
            body['CorpId'] = request.corp_id
        if not UtilClient.is_unset(request.face_url):
            body['FaceUrl'] = request.face_url
        if not UtilClient.is_unset(request.gender):
            body['Gender'] = request.gender
        if not UtilClient.is_unset(request.id_number):
            body['IdNumber'] = request.id_number
        if not UtilClient.is_unset(request.isv_sub_id):
            body['IsvSubId'] = request.isv_sub_id
        if not UtilClient.is_unset(request.live_address):
            body['LiveAddress'] = request.live_address
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.phone_no):
            body['PhoneNo'] = request.phone_no
        if not UtilClient.is_unset(request.plate_no):
            body['PlateNo'] = request.plate_no
        if not UtilClient.is_unset(request.scene_type):
            body['SceneType'] = request.scene_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddProfile',
            version='2020-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vcs_20200515_models.AddProfileResponse(),
            self.call_api(params, req, runtime)
        )

    def add_profile(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_profile_with_options(request, runtime)

    def add_profile_catalog_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.catalog_name):
            body['CatalogName'] = request.catalog_name
        if not UtilClient.is_unset(request.corp_id):
            body['CorpId'] = request.corp_id
        if not UtilClient.is_unset(request.isv_sub_id):
            body['IsvSubId'] = request.isv_sub_id
        if not UtilClient.is_unset(request.parent_catalog_id):
            body['ParentCatalogId'] = request.parent_catalog_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddProfileCatalog',
            version='2020-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vcs_20200515_models.AddProfileCatalogResponse(),
            self.call_api(params, req, runtime)
        )

    def add_profile_catalog(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_profile_catalog_with_options(request, runtime)

    def add_search_items_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = vcs_20200515_models.AddSearchItemsShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.search_item_list):
            request.search_item_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.search_item_list, 'SearchItemList', 'json')
        body = {}
        if not UtilClient.is_unset(request.search_item_list_shrink):
            body['SearchItemList'] = request.search_item_list_shrink
        if not UtilClient.is_unset(request.search_table_id):
            body['SearchTableId'] = request.search_table_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddSearchItems',
            version='2020-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vcs_20200515_models.AddSearchItemsResponse(),
            self.call_api(params, req, runtime)
        )

    def add_search_items(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_search_items_with_options(request, runtime)

    def add_watch_items_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        body_flat = {}
        if not UtilClient.is_unset(request.watch_item_list):
            body_flat['WatchItemList'] = request.watch_item_list
        if not UtilClient.is_unset(request.watch_policy_id):
            body['WatchPolicyId'] = request.watch_policy_id
        body = TeaCore.merge(body,
            OpenApiUtilClient.query(body_flat))
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddWatchItems',
            version='2020-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vcs_20200515_models.AddWatchItemsResponse(),
            self.call_api(params, req, runtime)
        )

    def add_watch_items(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_watch_items_with_options(request, runtime)

    def batch_delete_instance_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = vcs_20200515_models.BatchDeleteInstanceShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.instance_ids):
            request.instance_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.instance_ids, 'InstanceIds', 'json')
        body = {}
        if not UtilClient.is_unset(request.instance_ids_shrink):
            body['InstanceIds'] = request.instance_ids_shrink
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='BatchDeleteInstance',
            version='2020-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vcs_20200515_models.BatchDeleteInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    def batch_delete_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.batch_delete_instance_with_options(request, runtime)

    def bind_corp_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.corp_group_id):
            body['CorpGroupId'] = request.corp_group_id
        if not UtilClient.is_unset(request.corp_id):
            body['CorpId'] = request.corp_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='BindCorpGroup',
            version='2020-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vcs_20200515_models.BindCorpGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def bind_corp_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.bind_corp_group_with_options(request, runtime)

    def bind_devices_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = vcs_20200515_models.BindDevicesShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.sub_device_list):
            request.sub_device_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.sub_device_list, 'SubDeviceList', 'json')
        body = {}
        if not UtilClient.is_unset(request.corp_id):
            body['CorpId'] = request.corp_id
        if not UtilClient.is_unset(request.device_id):
            body['DeviceId'] = request.device_id
        if not UtilClient.is_unset(request.sub_device_list_shrink):
            body['SubDeviceList'] = request.sub_device_list_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='BindDevices',
            version='2020-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vcs_20200515_models.BindDevicesResponse(),
            self.call_api(params, req, runtime)
        )

    def bind_devices(self, request):
        runtime = util_models.RuntimeOptions()
        return self.bind_devices_with_options(request, runtime)

    def bind_person_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.corp_id):
            body['CorpId'] = request.corp_id
        if not UtilClient.is_unset(request.isv_sub_id):
            body['IsvSubId'] = request.isv_sub_id
        if not UtilClient.is_unset(request.person_id):
            body['PersonId'] = request.person_id
        if not UtilClient.is_unset(request.person_matching_rate):
            body['PersonMatchingRate'] = request.person_matching_rate
        if not UtilClient.is_unset(request.profile_id):
            body['ProfileId'] = request.profile_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='BindPerson',
            version='2020-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vcs_20200515_models.BindPersonResponse(),
            self.call_api(params, req, runtime)
        )

    def bind_person(self, request):
        runtime = util_models.RuntimeOptions()
        return self.bind_person_with_options(request, runtime)

    def bind_user_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.corp_id):
            body['CorpId'] = request.corp_id
        if not UtilClient.is_unset(request.isv_sub_id):
            body['IsvSubId'] = request.isv_sub_id
        if not UtilClient.is_unset(request.matching_rate):
            body['MatchingRate'] = request.matching_rate
        if not UtilClient.is_unset(request.person_id):
            body['PersonId'] = request.person_id
        if not UtilClient.is_unset(request.user_id):
            body['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='BindUser',
            version='2020-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vcs_20200515_models.BindUserResponse(),
            self.call_api(params, req, runtime)
        )

    def bind_user(self, request):
        runtime = util_models.RuntimeOptions()
        return self.bind_user_with_options(request, runtime)

    def check_aiinstance_name_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_name):
            body['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.instance_type):
            body['InstanceType'] = request.instance_type
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CheckAIInstanceName',
            version='2020-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vcs_20200515_models.CheckAIInstanceNameResponse(),
            self.call_api(params, req, runtime)
        )

    def check_aiinstance_name(self, request):
        runtime = util_models.RuntimeOptions()
        return self.check_aiinstance_name_with_options(request, runtime)

    def check_slrwith_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.service_name):
            query['ServiceName'] = request.service_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CheckSLR',
            version='2020-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vcs_20200515_models.CheckSLRResponse(),
            self.call_api(params, req, runtime)
        )

    def check_slr(self, request):
        runtime = util_models.RuntimeOptions()
        return self.check_slrwith_options(request, runtime)

    def control_aiot_device_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.associated_device_id):
            body['AssociatedDeviceId'] = request.associated_device_id
        if not UtilClient.is_unset(request.associated_ipaddr):
            body['AssociatedIPAddr'] = request.associated_ipaddr
        if not UtilClient.is_unset(request.associated_port):
            body['AssociatedPort'] = request.associated_port
        if not UtilClient.is_unset(request.associated_verification_enable):
            body['AssociatedVerificationEnable'] = request.associated_verification_enable
        if not UtilClient.is_unset(request.barrier_command):
            body['BarrierCommand'] = request.barrier_command
        if not UtilClient.is_unset(request.check_enabled):
            body['CheckEnabled'] = request.check_enabled
        if not UtilClient.is_unset(request.command_type):
            body['CommandType'] = request.command_type
        if not UtilClient.is_unset(request.double_verification_group_enabled):
            body['DoubleVerificationGroupEnabled'] = request.double_verification_group_enabled
        if not UtilClient.is_unset(request.gate_ctl_status):
            body['GateCtlStatus'] = request.gate_ctl_status
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.identity_number):
            body['IdentityNumber'] = request.identity_number
        if not UtilClient.is_unset(request.is_proxy):
            body['IsProxy'] = request.is_proxy
        body_flat = {}
        if not UtilClient.is_unset(request.mi_fare_card):
            body_flat['MiFareCard'] = request.mi_fare_card
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.reboot_device):
            body['RebootDevice'] = request.reboot_device
        if not UtilClient.is_unset(request.single_interval):
            body['SingleInterval'] = request.single_interval
        if not UtilClient.is_unset(request.super_password):
            body['SuperPassword'] = request.super_password
        if not UtilClient.is_unset(request.upgrade_file_url):
            body['UpgradeFileURL'] = request.upgrade_file_url
        body = TeaCore.merge(body,
            OpenApiUtilClient.query(body_flat))
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ControlAiotDevice',
            version='2020-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vcs_20200515_models.ControlAiotDeviceResponse(),
            self.call_api(params, req, runtime)
        )

    def control_aiot_device(self, request):
        runtime = util_models.RuntimeOptions()
        return self.control_aiot_device_with_options(request, runtime)

    def create_aiinstance_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = vcs_20200515_models.CreateAIInstanceShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.data_source_times):
            request.data_source_times_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.data_source_times, 'DataSourceTimes', 'json')
        if not UtilClient.is_unset(tmp_req.schedule_cycle_dates):
            request.schedule_cycle_dates_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.schedule_cycle_dates, 'ScheduleCycleDates', 'json')
        if not UtilClient.is_unset(tmp_req.schedule_times):
            request.schedule_times_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.schedule_times, 'ScheduleTimes', 'json')
        body = {}
        if not UtilClient.is_unset(request.algorithm_id):
            body['AlgorithmId'] = request.algorithm_id
        if not UtilClient.is_unset(request.algorithm_name):
            body['AlgorithmName'] = request.algorithm_name
        if not UtilClient.is_unset(request.compute_type):
            body['ComputeType'] = request.compute_type
        if not UtilClient.is_unset(request.data_source):
            body['DataSource'] = request.data_source
        if not UtilClient.is_unset(request.data_source_times_shrink):
            body['DataSourceTimes'] = request.data_source_times_shrink
        if not UtilClient.is_unset(request.data_type):
            body['DataType'] = request.data_type
        if not UtilClient.is_unset(request.instance_name):
            body['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.instance_type):
            body['InstanceType'] = request.instance_type
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.schedule_cycle_dates_shrink):
            body['ScheduleCycleDates'] = request.schedule_cycle_dates_shrink
        if not UtilClient.is_unset(request.schedule_times_shrink):
            body['ScheduleTimes'] = request.schedule_times_shrink
        if not UtilClient.is_unset(request.schedule_type):
            body['ScheduleType'] = request.schedule_type
        if not UtilClient.is_unset(request.spf):
            body['Spf'] = request.spf
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateAIInstance',
            version='2020-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vcs_20200515_models.CreateAIInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    def create_aiinstance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_aiinstance_with_options(request, runtime)

    def create_compute_instance_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = vcs_20200515_models.CreateComputeInstanceShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.algorithms):
            request.algorithms_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.algorithms, 'Algorithms', 'json')
        if not UtilClient.is_unset(tmp_req.devices):
            request.devices_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.devices, 'Devices', 'json')
        body = {}
        if not UtilClient.is_unset(request.acu_used):
            body['AcuUsed'] = request.acu_used
        if not UtilClient.is_unset(request.algorithm_type):
            body['AlgorithmType'] = request.algorithm_type
        if not UtilClient.is_unset(request.algorithms_shrink):
            body['Algorithms'] = request.algorithms_shrink
        if not UtilClient.is_unset(request.compute_picture_type):
            body['ComputePictureType'] = request.compute_picture_type
        if not UtilClient.is_unset(request.compute_picture_value):
            body['ComputePictureValue'] = request.compute_picture_value
        if not UtilClient.is_unset(request.datasource_type):
            body['DatasourceType'] = request.datasource_type
        if not UtilClient.is_unset(request.devices_shrink):
            body['Devices'] = request.devices_shrink
        if not UtilClient.is_unset(request.instance_name):
            body['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.is_frame_extraction):
            body['IsFrameExtraction'] = request.is_frame_extraction
        if not UtilClient.is_unset(request.is_polling):
            body['IsPolling'] = request.is_polling
        if not UtilClient.is_unset(request.overall_execution_time):
            body['OverallExecutionTime'] = request.overall_execution_time
        if not UtilClient.is_unset(request.pic_topic):
            body['PicTopic'] = request.pic_topic
        if not UtilClient.is_unset(request.pic_type):
            body['PicType'] = request.pic_type
        if not UtilClient.is_unset(request.polling_configs):
            body['PollingConfigs'] = request.polling_configs
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.schedule_cycle_date):
            body['ScheduleCycleDate'] = request.schedule_cycle_date
        if not UtilClient.is_unset(request.schedule_day):
            body['ScheduleDay'] = request.schedule_day
        if not UtilClient.is_unset(request.schedule_day_size):
            body['ScheduleDaySize'] = request.schedule_day_size
        if not UtilClient.is_unset(request.schedule_times):
            body['ScheduleTimes'] = request.schedule_times
        if not UtilClient.is_unset(request.schedule_type):
            body['ScheduleType'] = request.schedule_type
        if not UtilClient.is_unset(request.slice_execution_time):
            body['SliceExecutionTime'] = request.slice_execution_time
        if not UtilClient.is_unset(request.storage_used):
            body['StorageUsed'] = request.storage_used
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateComputeInstance',
            version='2020-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vcs_20200515_models.CreateComputeInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    def create_compute_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_compute_instance_with_options(request, runtime)

    def create_corp_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.algorithm_type):
            body['AlgorithmType'] = request.algorithm_type
        if not UtilClient.is_unset(request.app_name):
            body['AppName'] = request.app_name
        if not UtilClient.is_unset(request.corp_name):
            body['CorpName'] = request.corp_name
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.icon_path):
            body['IconPath'] = request.icon_path
        if not UtilClient.is_unset(request.isv_sub_id):
            body['IsvSubId'] = request.isv_sub_id
        if not UtilClient.is_unset(request.parent_corp_id):
            body['ParentCorpId'] = request.parent_corp_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateCorp',
            version='2020-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vcs_20200515_models.CreateCorpResponse(),
            self.call_api(params, req, runtime)
        )

    def create_corp(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_corp_with_options(request, runtime)

    def create_corp_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.corp_id):
            body['CorpId'] = request.corp_id
        if not UtilClient.is_unset(request.group_id):
            body['GroupId'] = request.group_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateCorpGroup',
            version='2020-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vcs_20200515_models.CreateCorpGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def create_corp_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_corp_group_with_options(request, runtime)

    def create_device_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.activate_code):
            body['ActivateCode'] = request.activate_code
        if not UtilClient.is_unset(request.audio_enable):
            body['AudioEnable'] = request.audio_enable
        if not UtilClient.is_unset(request.city_code):
            body['CityCode'] = request.city_code
        if not UtilClient.is_unset(request.corp_id):
            body['CorpId'] = request.corp_id
        if not UtilClient.is_unset(request.data_source_type):
            body['DataSourceType'] = request.data_source_type
        if not UtilClient.is_unset(request.device_address):
            body['DeviceAddress'] = request.device_address
        if not UtilClient.is_unset(request.device_direction):
            body['DeviceDirection'] = request.device_direction
        if not UtilClient.is_unset(request.device_id):
            body['DeviceId'] = request.device_id
        if not UtilClient.is_unset(request.device_model):
            body['DeviceModel'] = request.device_model
        if not UtilClient.is_unset(request.device_name):
            body['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.device_rate):
            body['DeviceRate'] = request.device_rate
        if not UtilClient.is_unset(request.device_resolution):
            body['DeviceResolution'] = request.device_resolution
        if not UtilClient.is_unset(request.device_site):
            body['DeviceSite'] = request.device_site
        if not UtilClient.is_unset(request.device_sn):
            body['DeviceSn'] = request.device_sn
        if not UtilClient.is_unset(request.device_type):
            body['DeviceType'] = request.device_type
        if not UtilClient.is_unset(request.encode_format):
            body['EncodeFormat'] = request.encode_format
        if not UtilClient.is_unset(request.frame_rate):
            body['FrameRate'] = request.frame_rate
        if not UtilClient.is_unset(request.gov_length):
            body['GovLength'] = request.gov_length
        if not UtilClient.is_unset(request.in_protocol):
            body['InProtocol'] = request.in_protocol
        if not UtilClient.is_unset(request.latitude):
            body['Latitude'] = request.latitude
        if not UtilClient.is_unset(request.longitude):
            body['Longitude'] = request.longitude
        if not UtilClient.is_unset(request.osdtime_enable):
            body['OSDTimeEnable'] = request.osdtime_enable
        if not UtilClient.is_unset(request.osdtime_type):
            body['OSDTimeType'] = request.osdtime_type
        if not UtilClient.is_unset(request.osdtime_x):
            body['OSDTimeX'] = request.osdtime_x
        if not UtilClient.is_unset(request.osdtime_y):
            body['OSDTimeY'] = request.osdtime_y
        if not UtilClient.is_unset(request.parent_device_id):
            body['ParentDeviceId'] = request.parent_device_id
        if not UtilClient.is_unset(request.sub_device_count):
            body['SubDeviceCount'] = request.sub_device_count
        if not UtilClient.is_unset(request.sub_device_id_list):
            body['SubDeviceIdList'] = request.sub_device_id_list
        if not UtilClient.is_unset(request.up_stream_mode):
            body['UpStreamMode'] = request.up_stream_mode
        if not UtilClient.is_unset(request.vendor):
            body['Vendor'] = request.vendor
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateDevice',
            version='2020-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vcs_20200515_models.CreateDeviceResponse(),
            self.call_api(params, req, runtime)
        )

    def create_device(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_device_with_options(request, runtime)

    def create_model_service_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.algorithm_code):
            body['AlgorithmCode'] = request.algorithm_code
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.instance_name):
            body['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.qpsrequired):
            body['QPSRequired'] = request.qpsrequired
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateModelService',
            version='2020-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vcs_20200515_models.CreateModelServiceResponse(),
            self.call_api(params, req, runtime)
        )

    def create_model_service(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_model_service_with_options(request, runtime)

    def create_new_device_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.city_code):
            body['CityCode'] = request.city_code
        if not UtilClient.is_unset(request.corp_id):
            body['CorpId'] = request.corp_id
        if not UtilClient.is_unset(request.data_source_type):
            body['DataSourceType'] = request.data_source_type
        if not UtilClient.is_unset(request.device_address):
            body['DeviceAddress'] = request.device_address
        if not UtilClient.is_unset(request.device_id):
            body['DeviceId'] = request.device_id
        if not UtilClient.is_unset(request.device_model):
            body['DeviceModel'] = request.device_model
        if not UtilClient.is_unset(request.device_name):
            body['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.device_type):
            body['DeviceType'] = request.device_type
        if not UtilClient.is_unset(request.file_path):
            body['FilePath'] = request.file_path
        if not UtilClient.is_unset(request.in_protocol):
            body['InProtocol'] = request.in_protocol
        if not UtilClient.is_unset(request.latitude):
            body['Latitude'] = request.latitude
        if not UtilClient.is_unset(request.longitude):
            body['Longitude'] = request.longitude
        if not UtilClient.is_unset(request.sub_device_count):
            body['SubDeviceCount'] = request.sub_device_count
        if not UtilClient.is_unset(request.vendor):
            body['Vendor'] = request.vendor
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateNewDevice',
            version='2020-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vcs_20200515_models.CreateNewDeviceResponse(),
            self.call_api(params, req, runtime)
        )

    def create_new_device(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_new_device_with_options(request, runtime)

    def create_scan_device_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.audio_enable):
            body['AudioEnable'] = request.audio_enable
        if not UtilClient.is_unset(request.city_code):
            body['CityCode'] = request.city_code
        if not UtilClient.is_unset(request.corp_id):
            body['CorpId'] = request.corp_id
        if not UtilClient.is_unset(request.data_source_type):
            body['DataSourceType'] = request.data_source_type
        if not UtilClient.is_unset(request.device_address):
            body['DeviceAddress'] = request.device_address
        if not UtilClient.is_unset(request.device_direction):
            body['DeviceDirection'] = request.device_direction
        if not UtilClient.is_unset(request.device_id):
            body['DeviceId'] = request.device_id
        if not UtilClient.is_unset(request.device_model):
            body['DeviceModel'] = request.device_model
        if not UtilClient.is_unset(request.device_name):
            body['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.device_rate):
            body['DeviceRate'] = request.device_rate
        if not UtilClient.is_unset(request.device_resolution):
            body['DeviceResolution'] = request.device_resolution
        if not UtilClient.is_unset(request.device_site):
            body['DeviceSite'] = request.device_site
        if not UtilClient.is_unset(request.device_sn):
            body['DeviceSn'] = request.device_sn
        if not UtilClient.is_unset(request.device_type):
            body['DeviceType'] = request.device_type
        if not UtilClient.is_unset(request.encode_format):
            body['EncodeFormat'] = request.encode_format
        if not UtilClient.is_unset(request.frame_rate):
            body['FrameRate'] = request.frame_rate
        if not UtilClient.is_unset(request.gov_length):
            body['GovLength'] = request.gov_length
        if not UtilClient.is_unset(request.in_protocol):
            body['InProtocol'] = request.in_protocol
        if not UtilClient.is_unset(request.latitude):
            body['Latitude'] = request.latitude
        if not UtilClient.is_unset(request.longitude):
            body['Longitude'] = request.longitude
        if not UtilClient.is_unset(request.osdtime_enable):
            body['OSDTimeEnable'] = request.osdtime_enable
        if not UtilClient.is_unset(request.osdtime_type):
            body['OSDTimeType'] = request.osdtime_type
        if not UtilClient.is_unset(request.osdtime_x):
            body['OSDTimeX'] = request.osdtime_x
        if not UtilClient.is_unset(request.osdtime_y):
            body['OSDTimeY'] = request.osdtime_y
        if not UtilClient.is_unset(request.sub_device_count):
            body['SubDeviceCount'] = request.sub_device_count
        if not UtilClient.is_unset(request.vendor):
            body['Vendor'] = request.vendor
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateScanDevice',
            version='2020-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vcs_20200515_models.CreateScanDeviceResponse(),
            self.call_api(params, req, runtime)
        )

    def create_scan_device(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_scan_device_with_options(request, runtime)

    def create_search_table_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.algorithm_id):
            body['AlgorithmId'] = request.algorithm_id
        if not UtilClient.is_unset(request.search_table_name):
            body['SearchTableName'] = request.search_table_name
        if not UtilClient.is_unset(request.target_type):
            body['TargetType'] = request.target_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateSearchTable',
            version='2020-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vcs_20200515_models.CreateSearchTableResponse(),
            self.call_api(params, req, runtime)
        )

    def create_search_table(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_search_table_with_options(request, runtime)

    def create_subscribe_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.device_id):
            body['DeviceId'] = request.device_id
        if not UtilClient.is_unset(request.push_config):
            body['PushConfig'] = request.push_config
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateSubscribe',
            version='2020-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vcs_20200515_models.CreateSubscribeResponse(),
            self.call_api(params, req, runtime)
        )

    def create_subscribe(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_subscribe_with_options(request, runtime)

    def create_user_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.address):
            body['Address'] = request.address
        if not UtilClient.is_unset(request.age):
            body['Age'] = request.age
        if not UtilClient.is_unset(request.attachment):
            body['Attachment'] = request.attachment
        if not UtilClient.is_unset(request.biz_id):
            body['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.corp_id):
            body['CorpId'] = request.corp_id
        if not UtilClient.is_unset(request.face_image_url):
            body['FaceImageUrl'] = request.face_image_url
        if not UtilClient.is_unset(request.gender):
            body['Gender'] = request.gender
        if not UtilClient.is_unset(request.id_number):
            body['IdNumber'] = request.id_number
        if not UtilClient.is_unset(request.isv_sub_id):
            body['IsvSubId'] = request.isv_sub_id
        if not UtilClient.is_unset(request.phone_no):
            body['PhoneNo'] = request.phone_no
        if not UtilClient.is_unset(request.plate_no):
            body['PlateNo'] = request.plate_no
        if not UtilClient.is_unset(request.user_group_id):
            body['UserGroupId'] = request.user_group_id
        if not UtilClient.is_unset(request.user_name):
            body['UserName'] = request.user_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateUser',
            version='2020-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vcs_20200515_models.CreateUserResponse(),
            self.call_api(params, req, runtime)
        )

    def create_user(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_user_with_options(request, runtime)

    def create_user_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.corp_id):
            body['CorpId'] = request.corp_id
        if not UtilClient.is_unset(request.isv_sub_id):
            body['IsvSubId'] = request.isv_sub_id
        if not UtilClient.is_unset(request.parent_user_group_id):
            body['ParentUserGroupId'] = request.parent_user_group_id
        if not UtilClient.is_unset(request.user_group_name):
            body['UserGroupName'] = request.user_group_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateUserGroup',
            version='2020-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vcs_20200515_models.CreateUserGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def create_user_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_user_group_with_options(request, runtime)

    def create_video_compose_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.audio_file_name):
            body['AudioFileName'] = request.audio_file_name
        if not UtilClient.is_unset(request.bucket_name):
            body['BucketName'] = request.bucket_name
        if not UtilClient.is_unset(request.corp_id):
            body['CorpId'] = request.corp_id
        if not UtilClient.is_unset(request.domain_name):
            body['DomainName'] = request.domain_name
        if not UtilClient.is_unset(request.image_file_names):
            body['ImageFileNames'] = request.image_file_names
        if not UtilClient.is_unset(request.image_parameters):
            body['ImageParameters'] = request.image_parameters
        if not UtilClient.is_unset(request.video_format):
            body['VideoFormat'] = request.video_format
        if not UtilClient.is_unset(request.video_frame_rate):
            body['VideoFrameRate'] = request.video_frame_rate
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateVideoComposeTask',
            version='2020-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vcs_20200515_models.CreateVideoComposeTaskResponse(),
            self.call_api(params, req, runtime)
        )

    def create_video_compose_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_video_compose_task_with_options(request, runtime)

    def create_video_summary_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.corp_id):
            body['CorpId'] = request.corp_id
        if not UtilClient.is_unset(request.device_id):
            body['DeviceId'] = request.device_id
        if not UtilClient.is_unset(request.end_time_stamp):
            body['EndTimeStamp'] = request.end_time_stamp
        if not UtilClient.is_unset(request.live_video_summary):
            body['LiveVideoSummary'] = request.live_video_summary
        if not UtilClient.is_unset(request.option_list):
            body['OptionList'] = request.option_list
        if not UtilClient.is_unset(request.start_time_stamp):
            body['StartTimeStamp'] = request.start_time_stamp
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateVideoSummaryTask',
            version='2020-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vcs_20200515_models.CreateVideoSummaryTaskResponse(),
            self.call_api(params, req, runtime)
        )

    def create_video_summary_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_video_summary_task_with_options(request, runtime)

    def create_watch_policy_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.item_match_type):
            body['ItemMatchType'] = request.item_match_type
        if not UtilClient.is_unset(request.similarity_threshold):
            body['SimilarityThreshold'] = request.similarity_threshold
        if not UtilClient.is_unset(request.target_type):
            body['TargetType'] = request.target_type
        if not UtilClient.is_unset(request.watch_mode):
            body['WatchMode'] = request.watch_mode
        if not UtilClient.is_unset(request.watch_policy_name):
            body['WatchPolicyName'] = request.watch_policy_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateWatchPolicy',
            version='2020-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vcs_20200515_models.CreateWatchPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    def create_watch_policy(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_watch_policy_with_options(request, runtime)

    def create_watch_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.corp_id):
            body['CorpId'] = request.corp_id
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.device_list):
            body['DeviceList'] = request.device_list
        if not UtilClient.is_unset(request.message_receiver):
            body['MessageReceiver'] = request.message_receiver
        if not UtilClient.is_unset(request.schedule_cycle_dates):
            body['ScheduleCycleDates'] = request.schedule_cycle_dates
        if not UtilClient.is_unset(request.schedule_times):
            body['ScheduleTimes'] = request.schedule_times
        if not UtilClient.is_unset(request.schedule_type):
            body['ScheduleType'] = request.schedule_type
        if not UtilClient.is_unset(request.task_name):
            body['TaskName'] = request.task_name
        if not UtilClient.is_unset(request.watch_policy_ids):
            body['WatchPolicyIds'] = request.watch_policy_ids
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateWatchTask',
            version='2020-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vcs_20200515_models.CreateWatchTaskResponse(),
            self.call_api(params, req, runtime)
        )

    def create_watch_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_watch_task_with_options(request, runtime)

    def delete_aiinstance_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = vcs_20200515_models.DeleteAIInstanceShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.instance_ids):
            request.instance_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.instance_ids, 'InstanceIds', 'json')
        body = {}
        if not UtilClient.is_unset(request.instance_ids_shrink):
            body['InstanceIds'] = request.instance_ids_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteAIInstance',
            version='2020-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vcs_20200515_models.DeleteAIInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_aiinstance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_aiinstance_with_options(request, runtime)

    def delete_aiot_device_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteAiotDevice',
            version='2020-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vcs_20200515_models.DeleteAiotDeviceResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_aiot_device(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_aiot_device_with_options(request, runtime)

    def delete_aiot_person_table_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.person_table_id):
            body['PersonTableId'] = request.person_table_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteAiotPersonTable',
            version='2020-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vcs_20200515_models.DeleteAiotPersonTableResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_aiot_person_table(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_aiot_person_table_with_options(request, runtime)

    def delete_aiot_person_table_item_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.person_table_id):
            body['PersonTableId'] = request.person_table_id
        if not UtilClient.is_unset(request.person_table_item_id):
            body['PersonTableItemId'] = request.person_table_item_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteAiotPersonTableItem',
            version='2020-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vcs_20200515_models.DeleteAiotPersonTableItemResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_aiot_person_table_item(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_aiot_person_table_item_with_options(request, runtime)

    def delete_aiot_vehicle_table_item_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.vehicle_table_id):
            body['VehicleTableId'] = request.vehicle_table_id
        if not UtilClient.is_unset(request.vehicle_table_item_id):
            body['VehicleTableItemId'] = request.vehicle_table_item_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteAiotVehicleTableItem',
            version='2020-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vcs_20200515_models.DeleteAiotVehicleTableItemResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_aiot_vehicle_table_item(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_aiot_vehicle_table_item_with_options(request, runtime)

    def delete_channel_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.device_codes):
            body['DeviceCodes'] = request.device_codes
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteChannel',
            version='2020-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vcs_20200515_models.DeleteChannelResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_channel(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_channel_with_options(request, runtime)

    def delete_corp_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.corp_id):
            body['CorpId'] = request.corp_id
        if not UtilClient.is_unset(request.group_id):
            body['GroupId'] = request.group_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteCorpGroup',
            version='2020-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vcs_20200515_models.DeleteCorpGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_corp_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_corp_group_with_options(request, runtime)

    def delete_data_source_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.corp_id):
            body['CorpId'] = request.corp_id
        if not UtilClient.is_unset(request.data_source_id):
            body['DataSourceId'] = request.data_source_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteDataSource',
            version='2020-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vcs_20200515_models.DeleteDataSourceResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_data_source(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_data_source_with_options(request, runtime)

    def delete_data_sources_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.data_source_id_list):
            body['DataSourceIdList'] = request.data_source_id_list
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteDataSources',
            version='2020-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vcs_20200515_models.DeleteDataSourcesResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_data_sources(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_data_sources_with_options(request, runtime)

    def delete_device_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.corp_id):
            body['CorpId'] = request.corp_id
        if not UtilClient.is_unset(request.gb_id):
            body['GbId'] = request.gb_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteDevice',
            version='2020-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vcs_20200515_models.DeleteDeviceResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_device(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_device_with_options(request, runtime)

    def delete_device_for_instance_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = vcs_20200515_models.DeleteDeviceForInstanceShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.devices):
            request.devices_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.devices, 'Devices', 'json')
        body = {}
        if not UtilClient.is_unset(request.algorithm_id):
            body['AlgorithmId'] = request.algorithm_id
        if not UtilClient.is_unset(request.delete_instance_flag):
            body['DeleteInstanceFlag'] = request.delete_instance_flag
        if not UtilClient.is_unset(request.device_count):
            body['DeviceCount'] = request.device_count
        if not UtilClient.is_unset(request.devices_shrink):
            body['Devices'] = request.devices_shrink
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteDeviceForInstance',
            version='2020-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vcs_20200515_models.DeleteDeviceForInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_device_for_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_device_for_instance_with_options(request, runtime)

    def delete_devices_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.device_id_list):
            body['DeviceIdList'] = request.device_id_list
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteDevices',
            version='2020-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vcs_20200515_models.DeleteDevicesResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_devices(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_devices_with_options(request, runtime)

    def delete_double_verification_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.double_verification_group_id):
            body['DoubleVerificationGroupId'] = request.double_verification_group_id
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteDoubleVerificationGroup',
            version='2020-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vcs_20200515_models.DeleteDoubleVerificationGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_double_verification_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_double_verification_group_with_options(request, runtime)

    def delete_ipcdevice_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.device_codes):
            body['DeviceCodes'] = request.device_codes
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteIPCDevice',
            version='2020-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vcs_20200515_models.DeleteIPCDeviceResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_ipcdevice(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_ipcdevice_with_options(request, runtime)

    def delete_model_service_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.model_service_id):
            body['ModelServiceId'] = request.model_service_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteModelService',
            version='2020-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vcs_20200515_models.DeleteModelServiceResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_model_service(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_model_service_with_options(request, runtime)

    def delete_nvrdevice_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.device_codes):
            body['DeviceCodes'] = request.device_codes
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteNVRDevice',
            version='2020-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vcs_20200515_models.DeleteNVRDeviceResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_nvrdevice(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_nvrdevice_with_options(request, runtime)

    def delete_profile_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.corp_id):
            body['CorpId'] = request.corp_id
        if not UtilClient.is_unset(request.isv_sub_id):
            body['IsvSubId'] = request.isv_sub_id
        if not UtilClient.is_unset(request.profile_id):
            body['ProfileId'] = request.profile_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteProfile',
            version='2020-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vcs_20200515_models.DeleteProfileResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_profile(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_profile_with_options(request, runtime)

    def delete_profile_catalog_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.catalog_id):
            body['CatalogId'] = request.catalog_id
        if not UtilClient.is_unset(request.corp_id):
            body['CorpId'] = request.corp_id
        if not UtilClient.is_unset(request.isv_sub_id):
            body['IsvSubId'] = request.isv_sub_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteProfileCatalog',
            version='2020-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vcs_20200515_models.DeleteProfileCatalogResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_profile_catalog(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_profile_catalog_with_options(request, runtime)

    def delete_project_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.project_ids):
            query['ProjectIds'] = request.project_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteProject',
            version='2020-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vcs_20200515_models.DeleteProjectResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_project(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_project_with_options(request, runtime)

    def delete_records_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.algorithm_type):
            body['AlgorithmType'] = request.algorithm_type
        if not UtilClient.is_unset(request.attribute_name):
            body['AttributeName'] = request.attribute_name
        if not UtilClient.is_unset(request.corp_id):
            body['CorpId'] = request.corp_id
        if not UtilClient.is_unset(request.operator_type):
            body['OperatorType'] = request.operator_type
        if not UtilClient.is_unset(request.value):
            body['Value'] = request.value
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteRecords',
            version='2020-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vcs_20200515_models.DeleteRecordsResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_records(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_records_with_options(request, runtime)

    def delete_search_tables_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.search_table_ids):
            body['SearchTableIds'] = request.search_table_ids
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteSearchTables',
            version='2020-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vcs_20200515_models.DeleteSearchTablesResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_search_tables(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_search_tables_with_options(request, runtime)

    def delete_subscribe_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.device_id):
            body['DeviceId'] = request.device_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteSubscribe',
            version='2020-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vcs_20200515_models.DeleteSubscribeResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_subscribe(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_subscribe_with_options(request, runtime)

    def delete_user_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.corp_id):
            body['CorpId'] = request.corp_id
        if not UtilClient.is_unset(request.isv_sub_id):
            body['IsvSubId'] = request.isv_sub_id
        if not UtilClient.is_unset(request.user_id):
            body['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteUser',
            version='2020-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vcs_20200515_models.DeleteUserResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_user(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_user_with_options(request, runtime)

    def delete_user_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.corp_id):
            body['CorpId'] = request.corp_id
        if not UtilClient.is_unset(request.isv_sub_id):
            body['IsvSubId'] = request.isv_sub_id
        if not UtilClient.is_unset(request.user_group_id):
            body['UserGroupId'] = request.user_group_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteUserGroup',
            version='2020-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vcs_20200515_models.DeleteUserGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_user_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_user_group_with_options(request, runtime)

    def delete_video_summary_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.corp_id):
            body['CorpId'] = request.corp_id
        if not UtilClient.is_unset(request.task_id):
            body['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteVideoSummaryTask',
            version='2020-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vcs_20200515_models.DeleteVideoSummaryTaskResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_video_summary_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_video_summary_task_with_options(request, runtime)

    def delete_watch_policies_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.watch_policy_ids):
            body['WatchPolicyIds'] = request.watch_policy_ids
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteWatchPolicies',
            version='2020-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vcs_20200515_models.DeleteWatchPoliciesResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_watch_policies(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_watch_policies_with_options(request, runtime)

    def delete_watch_tasks_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.watch_task_ids):
            body['WatchTaskIds'] = request.watch_task_ids
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteWatchTasks',
            version='2020-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vcs_20200515_models.DeleteWatchTasksResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_watch_tasks(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_watch_tasks_with_options(request, runtime)

    def describe_aiinstance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_name):
            body['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.instance_type):
            body['InstanceType'] = request.instance_type
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeAIInstance',
            version='2020-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vcs_20200515_models.DescribeAIInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_aiinstance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_aiinstance_with_options(request, runtime)

    def describe_aiot_devices_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.corp_id_list):
            body['CorpIdList'] = request.corp_id_list
        if not UtilClient.is_unset(request.id_list):
            body['IdList'] = request.id_list
        if not UtilClient.is_unset(request.page_num):
            body['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeAiotDevices',
            version='2020-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vcs_20200515_models.DescribeAiotDevicesResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_aiot_devices(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_aiot_devices_with_options(request, runtime)

    def describe_aiot_person_table_items_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.page_num):
            body['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.person_table_id):
            body['PersonTableId'] = request.person_table_id
        if not UtilClient.is_unset(request.person_table_item_id):
            body['PersonTableItemId'] = request.person_table_item_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeAiotPersonTableItems',
            version='2020-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vcs_20200515_models.DescribeAiotPersonTableItemsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_aiot_person_table_items(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_aiot_person_table_items_with_options(request, runtime)

    def describe_aiot_person_tables_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.person_table_id_list):
            body['PersonTableIdList'] = request.person_table_id_list
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeAiotPersonTables',
            version='2020-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vcs_20200515_models.DescribeAiotPersonTablesResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_aiot_person_tables(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_aiot_person_tables_with_options(request, runtime)

    def describe_aiot_vehicle_table_items_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.page_num):
            body['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.vehicle_table_id):
            body['VehicleTableId'] = request.vehicle_table_id
        if not UtilClient.is_unset(request.vehicle_table_item_id):
            body['VehicleTableItemId'] = request.vehicle_table_item_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeAiotVehicleTableItems',
            version='2020-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vcs_20200515_models.DescribeAiotVehicleTableItemsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_aiot_vehicle_table_items(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_aiot_vehicle_table_items_with_options(request, runtime)

    def describe_aiot_vehicle_tables_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.vehicle_table_id_list):
            body['VehicleTableIdList'] = request.vehicle_table_id_list
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeAiotVehicleTables',
            version='2020-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vcs_20200515_models.DescribeAiotVehicleTablesResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_aiot_vehicle_tables(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_aiot_vehicle_tables_with_options(request, runtime)

    def describe_camera_for_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeCameraForInstance',
            version='2020-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vcs_20200515_models.DescribeCameraForInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_camera_for_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_camera_for_instance_with_options(request, runtime)

    def describe_channels_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.device_filter):
            body['DeviceFilter'] = request.device_filter
        if not UtilClient.is_unset(request.device_status):
            body['DeviceStatus'] = request.device_status
        if not UtilClient.is_unset(request.nvr_id):
            body['NvrId'] = request.nvr_id
        if not UtilClient.is_unset(request.page_num):
            body['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.show_un_config):
            body['ShowUnConfig'] = request.show_un_config
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeChannels',
            version='2020-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vcs_20200515_models.DescribeChannelsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_channels(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_channels_with_options(request, runtime)

    def describe_data_sources_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.corp_id_list):
            body['CorpIdList'] = request.corp_id_list
        if not UtilClient.is_unset(request.data_source_category):
            body['DataSourceCategory'] = request.data_source_category
        if not UtilClient.is_unset(request.data_source_filter):
            body['DataSourceFilter'] = request.data_source_filter
        if not UtilClient.is_unset(request.data_source_id_list):
            body['DataSourceIdList'] = request.data_source_id_list
        if not UtilClient.is_unset(request.data_source_type):
            body['DataSourceType'] = request.data_source_type
        if not UtilClient.is_unset(request.page_num):
            body['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.stream_status):
            body['StreamStatus'] = request.stream_status
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeDataSources',
            version='2020-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vcs_20200515_models.DescribeDataSourcesResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_data_sources(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_data_sources_with_options(request, runtime)

    def describe_devices_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.corp_id_list):
            body['CorpIdList'] = request.corp_id_list
        if not UtilClient.is_unset(request.device_id_list):
            body['DeviceIdList'] = request.device_id_list
        if not UtilClient.is_unset(request.page_num):
            body['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeDevices',
            version='2020-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vcs_20200515_models.DescribeDevicesResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_devices(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_devices_with_options(request, runtime)

    def describe_ipcs_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.corp_id_list):
            body['CorpIdList'] = request.corp_id_list
        if not UtilClient.is_unset(request.device_filter):
            body['DeviceFilter'] = request.device_filter
        if not UtilClient.is_unset(request.device_id_list):
            body['DeviceIdList'] = request.device_id_list
        if not UtilClient.is_unset(request.device_status):
            body['DeviceStatus'] = request.device_status
        if not UtilClient.is_unset(request.nvr_id_list):
            body['NvrIdList'] = request.nvr_id_list
        if not UtilClient.is_unset(request.page_num):
            body['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.parent_device_type):
            body['ParentDeviceType'] = request.parent_device_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeIpcs',
            version='2020-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vcs_20200515_models.DescribeIpcsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_ipcs(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_ipcs_with_options(request, runtime)

    def describe_model_service_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.model_service_id):
            body['ModelServiceId'] = request.model_service_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeModelService',
            version='2020-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vcs_20200515_models.DescribeModelServiceResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_model_service(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_model_service_with_options(request, runtime)

    def describe_model_service_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.algorithm_code):
            body['AlgorithmCode'] = request.algorithm_code
        if not UtilClient.is_unset(request.include_deleted):
            body['IncludeDeleted'] = request.include_deleted
        if not UtilClient.is_unset(request.model_service_name):
            body['ModelServiceName'] = request.model_service_name
        if not UtilClient.is_unset(request.page_num):
            body['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeModelServiceList',
            version='2020-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vcs_20200515_models.DescribeModelServiceListResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_model_service_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_model_service_list_with_options(request, runtime)

    def describe_nvr_devices_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.corp_id_list):
            body['CorpIdList'] = request.corp_id_list
        if not UtilClient.is_unset(request.device_filter):
            body['DeviceFilter'] = request.device_filter
        if not UtilClient.is_unset(request.nvr_device_id_list):
            body['NvrDeviceIdList'] = request.nvr_device_id_list
        if not UtilClient.is_unset(request.page_num):
            body['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeNvrDevices',
            version='2020-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vcs_20200515_models.DescribeNvrDevicesResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_nvr_devices(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_nvr_devices_with_options(request, runtime)

    def describe_nvrs_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.corp_id_list):
            body['CorpIdList'] = request.corp_id_list
        if not UtilClient.is_unset(request.device_filter):
            body['DeviceFilter'] = request.device_filter
        if not UtilClient.is_unset(request.nvr_device_id_list):
            body['NvrDeviceIdList'] = request.nvr_device_id_list
        if not UtilClient.is_unset(request.page_num):
            body['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeNvrs',
            version='2020-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vcs_20200515_models.DescribeNvrsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_nvrs(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_nvrs_with_options(request, runtime)

    def describe_search_items_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search_item_ids):
            body['SearchItemIds'] = request.search_item_ids
        if not UtilClient.is_unset(request.search_table_id):
            body['SearchTableId'] = request.search_table_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeSearchItems',
            version='2020-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vcs_20200515_models.DescribeSearchItemsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_search_items(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_search_items_with_options(request, runtime)

    def describe_search_tables_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search_table_ids):
            body['SearchTableIds'] = request.search_table_ids
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeSearchTables',
            version='2020-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vcs_20200515_models.DescribeSearchTablesResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_search_tables(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_search_tables_with_options(request, runtime)

    def describe_watch_items_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.watch_item_ids):
            body['WatchItemIds'] = request.watch_item_ids
        if not UtilClient.is_unset(request.watch_policy_id):
            body['WatchPolicyId'] = request.watch_policy_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeWatchItems',
            version='2020-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vcs_20200515_models.DescribeWatchItemsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_watch_items(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_watch_items_with_options(request, runtime)

    def describe_watch_policies_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.watch_policy_ids):
            body['WatchPolicyIds'] = request.watch_policy_ids
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeWatchPolicies',
            version='2020-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vcs_20200515_models.DescribeWatchPoliciesResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_watch_policies(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_watch_policies_with_options(request, runtime)

    def describe_watch_tasks_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.watch_task_ids):
            body['WatchTaskIds'] = request.watch_task_ids
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeWatchTasks',
            version='2020-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vcs_20200515_models.DescribeWatchTasksResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_watch_tasks(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_watch_tasks_with_options(request, runtime)

    def describes_double_verification_groups_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.double_verification_group_ids):
            body['DoubleVerificationGroupIds'] = request.double_verification_group_ids
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.page_num):
            body['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribesDoubleVerificationGroups',
            version='2020-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vcs_20200515_models.DescribesDoubleVerificationGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    def describes_double_verification_groups(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describes_double_verification_groups_with_options(request, runtime)

    def echo_status_with_options(self, runtime):
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='EchoStatus',
            version='2020-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vcs_20200515_models.EchoStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def echo_status(self):
        runtime = util_models.RuntimeOptions()
        return self.echo_status_with_options(runtime)

    def get_aiot_storage_info_with_options(self, runtime):
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='GetAiotStorageInfo',
            version='2020-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vcs_20200515_models.GetAiotStorageInfoResponse(),
            self.call_api(params, req, runtime)
        )

    def get_aiot_storage_info(self):
        runtime = util_models.RuntimeOptions()
        return self.get_aiot_storage_info_with_options(runtime)

    def get_body_options_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.corp_id):
            body['CorpId'] = request.corp_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetBodyOptions',
            version='2020-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vcs_20200515_models.GetBodyOptionsResponse(),
            self.call_api(params, req, runtime)
        )

    def get_body_options(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_body_options_with_options(request, runtime)

    def get_catalog_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.corp_id):
            query['CorpId'] = request.corp_id
        if not UtilClient.is_unset(request.isv_sub_id):
            query['IsvSubId'] = request.isv_sub_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetCatalogList',
            version='2020-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vcs_20200515_models.GetCatalogListResponse(),
            self.call_api(params, req, runtime)
        )

    def get_catalog_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_catalog_list_with_options(request, runtime)

    def get_city_code_with_options(self, runtime):
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='GetCityCode',
            version='2020-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vcs_20200515_models.GetCityCodeResponse(),
            self.call_api(params, req, runtime)
        )

    def get_city_code(self):
        runtime = util_models.RuntimeOptions()
        return self.get_city_code_with_options(runtime)

    def get_data_source_stats_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.corp_id_list):
            body['CorpIdList'] = request.corp_id_list
        if not UtilClient.is_unset(request.data_source_type):
            body['DataSourceType'] = request.data_source_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetDataSourceStats',
            version='2020-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vcs_20200515_models.GetDataSourceStatsResponse(),
            self.call_api(params, req, runtime)
        )

    def get_data_source_stats(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_data_source_stats_with_options(request, runtime)

    def get_device_capture_strategy_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.device_code):
            body['DeviceCode'] = request.device_code
        if not UtilClient.is_unset(request.device_type):
            body['DeviceType'] = request.device_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetDeviceCaptureStrategy',
            version='2020-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vcs_20200515_models.GetDeviceCaptureStrategyResponse(),
            self.call_api(params, req, runtime)
        )

    def get_device_capture_strategy(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_device_capture_strategy_with_options(request, runtime)

    def get_device_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.device_sn):
            body['DeviceSn'] = request.device_sn
        if not UtilClient.is_unset(request.device_time_stamp):
            body['DeviceTimeStamp'] = request.device_time_stamp
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetDeviceConfig',
            version='2020-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vcs_20200515_models.GetDeviceConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def get_device_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_device_config_with_options(request, runtime)

    def get_device_count_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.up_stream_mode):
            body['UpStreamMode'] = request.up_stream_mode
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetDeviceCount',
            version='2020-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vcs_20200515_models.GetDeviceCountResponse(),
            self.call_api(params, req, runtime)
        )

    def get_device_count(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_device_count_with_options(request, runtime)

    def get_device_live_url_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.corp_id):
            body['CorpId'] = request.corp_id
        if not UtilClient.is_unset(request.device_id):
            body['DeviceId'] = request.device_id
        if not UtilClient.is_unset(request.gb_id):
            body['GbId'] = request.gb_id
        if not UtilClient.is_unset(request.out_protocol):
            body['OutProtocol'] = request.out_protocol
        if not UtilClient.is_unset(request.stream_type):
            body['StreamType'] = request.stream_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetDeviceLiveUrl',
            version='2020-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vcs_20200515_models.GetDeviceLiveUrlResponse(),
            self.call_api(params, req, runtime)
        )

    def get_device_live_url(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_device_live_url_with_options(request, runtime)

    def get_device_picture_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.device_id):
            body['DeviceId'] = request.device_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetDevicePicture',
            version='2020-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vcs_20200515_models.GetDevicePictureResponse(),
            self.call_api(params, req, runtime)
        )

    def get_device_picture(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_device_picture_with_options(request, runtime)

    def get_device_stats_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.corp_id_list):
            body['CorpIdList'] = request.corp_id_list
        if not UtilClient.is_unset(request.device_status):
            body['DeviceStatus'] = request.device_status
        if not UtilClient.is_unset(request.device_type):
            body['DeviceType'] = request.device_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetDeviceStats',
            version='2020-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vcs_20200515_models.GetDeviceStatsResponse(),
            self.call_api(params, req, runtime)
        )

    def get_device_stats(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_device_stats_with_options(request, runtime)

    def get_device_video_url_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.corp_id):
            body['CorpId'] = request.corp_id
        if not UtilClient.is_unset(request.device_id):
            body['DeviceId'] = request.device_id
        if not UtilClient.is_unset(request.end_time):
            body['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.gb_id):
            body['GbId'] = request.gb_id
        if not UtilClient.is_unset(request.out_protocol):
            body['OutProtocol'] = request.out_protocol
        if not UtilClient.is_unset(request.start_time):
            body['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.storage_type):
            body['StorageType'] = request.storage_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetDeviceVideoUrl',
            version='2020-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vcs_20200515_models.GetDeviceVideoUrlResponse(),
            self.call_api(params, req, runtime)
        )

    def get_device_video_url(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_device_video_url_with_options(request, runtime)

    def get_face_model_result_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.picture_content):
            body['PictureContent'] = request.picture_content
        if not UtilClient.is_unset(request.picture_id):
            body['PictureId'] = request.picture_id
        if not UtilClient.is_unset(request.picture_url):
            body['PictureUrl'] = request.picture_url
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetFaceModelResult',
            version='2020-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vcs_20200515_models.GetFaceModelResultResponse(),
            self.call_api(params, req, runtime)
        )

    def get_face_model_result(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_face_model_result_with_options(request, runtime)

    def get_face_options_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.corp_id):
            body['CorpId'] = request.corp_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetFaceOptions',
            version='2020-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vcs_20200515_models.GetFaceOptionsResponse(),
            self.call_api(params, req, runtime)
        )

    def get_face_options(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_face_options_with_options(request, runtime)

    def get_inventory_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.commodity_code):
            body['CommodityCode'] = request.commodity_code
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetInventory',
            version='2020-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vcs_20200515_models.GetInventoryResponse(),
            self.call_api(params, req, runtime)
        )

    def get_inventory(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_inventory_with_options(request, runtime)

    def get_monitor_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.corp_id):
            body['CorpId'] = request.corp_id
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetMonitorList',
            version='2020-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vcs_20200515_models.GetMonitorListResponse(),
            self.call_api(params, req, runtime)
        )

    def get_monitor_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_monitor_list_with_options(request, runtime)

    def get_monitor_result_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.algorithm_vendor):
            body['AlgorithmVendor'] = request.algorithm_vendor
        if not UtilClient.is_unset(request.corp_id):
            body['CorpId'] = request.corp_id
        if not UtilClient.is_unset(request.end_time):
            body['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.min_record_id):
            body['MinRecordId'] = request.min_record_id
        if not UtilClient.is_unset(request.start_time):
            body['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.task_id):
            body['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetMonitorResult',
            version='2020-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vcs_20200515_models.GetMonitorResultResponse(),
            self.call_api(params, req, runtime)
        )

    def get_monitor_result(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_monitor_result_with_options(request, runtime)

    def get_odps_result_with_options(self, runtime):
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='GetOdpsResult',
            version='2020-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vcs_20200515_models.GetOdpsResultResponse(),
            self.call_api(params, req, runtime)
        )

    def get_odps_result(self):
        runtime = util_models.RuntimeOptions()
        return self.get_odps_result_with_options(runtime)

    def get_person_detail_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.algorithm_type):
            body['AlgorithmType'] = request.algorithm_type
        if not UtilClient.is_unset(request.corp_id):
            body['CorpId'] = request.corp_id
        if not UtilClient.is_unset(request.person_id):
            body['PersonID'] = request.person_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetPersonDetail',
            version='2020-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vcs_20200515_models.GetPersonDetailResponse(),
            self.call_api(params, req, runtime)
        )

    def get_person_detail(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_person_detail_with_options(request, runtime)

    def get_person_list_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = vcs_20200515_models.GetPersonListShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.corp_id_list):
            request.corp_id_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.corp_id_list, 'CorpIdList', 'json')
        if not UtilClient.is_unset(tmp_req.person_id_list):
            request.person_id_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.person_id_list, 'PersonIdList', 'json')
        body = {}
        if not UtilClient.is_unset(request.corp_id):
            body['CorpId'] = request.corp_id
        if not UtilClient.is_unset(request.corp_id_list_shrink):
            body['CorpIdList'] = request.corp_id_list_shrink
        if not UtilClient.is_unset(request.face_matching_rate_threshold):
            body['FaceMatchingRateThreshold'] = request.face_matching_rate_threshold
        if not UtilClient.is_unset(request.face_url):
            body['FaceUrl'] = request.face_url
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.person_id_list_shrink):
            body['PersonIdList'] = request.person_id_list_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetPersonList',
            version='2020-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vcs_20200515_models.GetPersonListResponse(),
            self.call_api(params, req, runtime)
        )

    def get_person_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_person_list_with_options(request, runtime)

    def get_picture_url_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.expire_time):
            body['ExpireTime'] = request.expire_time
        if not UtilClient.is_unset(request.origin_url):
            body['OriginUrl'] = request.origin_url
        if not UtilClient.is_unset(request.protocol):
            body['Protocol'] = request.protocol
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetPictureUrl',
            version='2020-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vcs_20200515_models.GetPictureUrlResponse(),
            self.call_api(params, req, runtime)
        )

    def get_picture_url(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_picture_url_with_options(request, runtime)

    def get_profile_detail_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.corp_id):
            body['CorpId'] = request.corp_id
        if not UtilClient.is_unset(request.isv_sub_id):
            body['IsvSubId'] = request.isv_sub_id
        if not UtilClient.is_unset(request.profile_id):
            body['ProfileId'] = request.profile_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetProfileDetail',
            version='2020-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vcs_20200515_models.GetProfileDetailResponse(),
            self.call_api(params, req, runtime)
        )

    def get_profile_detail(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_profile_detail_with_options(request, runtime)

    def get_profile_list_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = vcs_20200515_models.GetProfileListShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.person_id_list):
            request.person_id_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.person_id_list, 'PersonIdList', 'json')
        if not UtilClient.is_unset(tmp_req.profile_id_list):
            request.profile_id_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.profile_id_list, 'ProfileIdList', 'json')
        body = {}
        if not UtilClient.is_unset(request.biz_id):
            body['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.catalog_id):
            body['CatalogId'] = request.catalog_id
        if not UtilClient.is_unset(request.corp_id):
            body['CorpId'] = request.corp_id
        if not UtilClient.is_unset(request.face_image_id):
            body['FaceImageId'] = request.face_image_id
        if not UtilClient.is_unset(request.face_url):
            body['FaceUrl'] = request.face_url
        if not UtilClient.is_unset(request.gender):
            body['Gender'] = request.gender
        if not UtilClient.is_unset(request.id_number):
            body['IdNumber'] = request.id_number
        if not UtilClient.is_unset(request.isv_sub_id):
            body['IsvSubId'] = request.isv_sub_id
        if not UtilClient.is_unset(request.live_address):
            body['LiveAddress'] = request.live_address
        if not UtilClient.is_unset(request.matching_rate_threshold):
            body['MatchingRateThreshold'] = request.matching_rate_threshold
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.person_id_list_shrink):
            body['PersonIdList'] = request.person_id_list_shrink
        if not UtilClient.is_unset(request.phone_no):
            body['PhoneNo'] = request.phone_no
        if not UtilClient.is_unset(request.plate_no):
            body['PlateNo'] = request.plate_no
        if not UtilClient.is_unset(request.profile_id_list_shrink):
            body['ProfileIdList'] = request.profile_id_list_shrink
        if not UtilClient.is_unset(request.scene_type):
            body['SceneType'] = request.scene_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetProfileList',
            version='2020-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vcs_20200515_models.GetProfileListResponse(),
            self.call_api(params, req, runtime)
        )

    def get_profile_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_profile_list_with_options(request, runtime)

    def get_scan_sub_devices_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.corp_id):
            body['CorpId'] = request.corp_id
        if not UtilClient.is_unset(request.device_id):
            body['DeviceId'] = request.device_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetScanSubDevices',
            version='2020-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vcs_20200515_models.GetScanSubDevicesResponse(),
            self.call_api(params, req, runtime)
        )

    def get_scan_sub_devices(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_scan_sub_devices_with_options(request, runtime)

    def get_user_detail_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.corp_id):
            body['CorpId'] = request.corp_id
        if not UtilClient.is_unset(request.isv_sub_id):
            body['IsvSubId'] = request.isv_sub_id
        if not UtilClient.is_unset(request.need_face_detail):
            body['NeedFaceDetail'] = request.need_face_detail
        if not UtilClient.is_unset(request.user_id):
            body['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetUserDetail',
            version='2020-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vcs_20200515_models.GetUserDetailResponse(),
            self.call_api(params, req, runtime)
        )

    def get_user_detail(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_user_detail_with_options(request, runtime)

    def get_video_compose_result_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.corp_id):
            body['CorpId'] = request.corp_id
        if not UtilClient.is_unset(request.task_request_id):
            body['TaskRequestId'] = request.task_request_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetVideoComposeResult',
            version='2020-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vcs_20200515_models.GetVideoComposeResultResponse(),
            self.call_api(params, req, runtime)
        )

    def get_video_compose_result(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_video_compose_result_with_options(request, runtime)

    def get_video_summary_task_result_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.corp_id):
            body['CorpId'] = request.corp_id
        if not UtilClient.is_unset(request.task_id):
            body['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetVideoSummaryTaskResult',
            version='2020-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vcs_20200515_models.GetVideoSummaryTaskResultResponse(),
            self.call_api(params, req, runtime)
        )

    def get_video_summary_task_result(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_video_summary_task_result_with_options(request, runtime)

    def invoke_motor_model_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.corp_id):
            body['CorpId'] = request.corp_id
        if not UtilClient.is_unset(request.pic_id):
            body['PicId'] = request.pic_id
        if not UtilClient.is_unset(request.pic_path):
            body['PicPath'] = request.pic_path
        if not UtilClient.is_unset(request.pic_url):
            body['PicUrl'] = request.pic_url
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='InvokeMotorModel',
            version='2020-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vcs_20200515_models.InvokeMotorModelResponse(),
            self.call_api(params, req, runtime)
        )

    def invoke_motor_model(self, request):
        runtime = util_models.RuntimeOptions()
        return self.invoke_motor_model_with_options(request, runtime)

    def list_access_number_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.corp_id_list):
            body['CorpIdList'] = request.corp_id_list
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListAccessNumber',
            version='2020-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vcs_20200515_models.ListAccessNumberResponse(),
            self.call_api(params, req, runtime)
        )

    def list_access_number(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_access_number_with_options(request, runtime)

    def list_algorithm_names_by_device_ids_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAlgorithmNamesByDeviceIds',
            version='2020-05-15',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vcs_20200515_models.ListAlgorithmNamesByDeviceIdsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_algorithm_names_by_device_ids(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_algorithm_names_by_device_ids_with_options(request, runtime)

    def list_body_algorithm_results_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.algorithm_type):
            body['AlgorithmType'] = request.algorithm_type
        if not UtilClient.is_unset(request.cap_style):
            body['CapStyle'] = request.cap_style
        if not UtilClient.is_unset(request.corp_id):
            body['CorpId'] = request.corp_id
        if not UtilClient.is_unset(request.data_source_id):
            body['DataSourceId'] = request.data_source_id
        if not UtilClient.is_unset(request.end_time):
            body['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.start_time):
            body['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListBodyAlgorithmResults',
            version='2020-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vcs_20200515_models.ListBodyAlgorithmResultsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_body_algorithm_results(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_body_algorithm_results_with_options(request, runtime)

    def list_corp_group_metrics_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.corp_id):
            body['CorpId'] = request.corp_id
        if not UtilClient.is_unset(request.device_group):
            body['DeviceGroup'] = request.device_group
        if not UtilClient.is_unset(request.device_id):
            body['DeviceId'] = request.device_id
        if not UtilClient.is_unset(request.end_time):
            body['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.group_id):
            body['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.start_time):
            body['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.tag_code):
            body['TagCode'] = request.tag_code
        if not UtilClient.is_unset(request.user_group):
            body['UserGroup'] = request.user_group
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListCorpGroupMetrics',
            version='2020-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vcs_20200515_models.ListCorpGroupMetricsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_corp_group_metrics(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_corp_group_metrics_with_options(request, runtime)

    def list_corp_groups_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.corp_id):
            body['CorpId'] = request.corp_id
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListCorpGroups',
            version='2020-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vcs_20200515_models.ListCorpGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_corp_groups(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_corp_groups_with_options(request, runtime)

    def list_corp_metrics_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.corp_id):
            body['CorpId'] = request.corp_id
        if not UtilClient.is_unset(request.device_group_list):
            body['DeviceGroupList'] = request.device_group_list
        if not UtilClient.is_unset(request.device_id_list):
            body['DeviceIdList'] = request.device_id_list
        if not UtilClient.is_unset(request.end_time):
            body['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.start_time):
            body['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.tag_code):
            body['TagCode'] = request.tag_code
        if not UtilClient.is_unset(request.user_group_list):
            body['UserGroupList'] = request.user_group_list
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListCorpMetrics',
            version='2020-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vcs_20200515_models.ListCorpMetricsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_corp_metrics(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_corp_metrics_with_options(request, runtime)

    def list_corps_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.corp_name):
            body['CorpName'] = request.corp_name
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListCorps',
            version='2020-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vcs_20200515_models.ListCorpsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_corps(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_corps_with_options(request, runtime)

    def list_device_groups_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.corp_id_list):
            body['CorpIdList'] = request.corp_id_list
        if not UtilClient.is_unset(request.data_source_type):
            body['DataSourceType'] = request.data_source_type
        if not UtilClient.is_unset(request.device_code_list):
            body['DeviceCodeList'] = request.device_code_list
        if not UtilClient.is_unset(request.group):
            body['Group'] = request.group
        if not UtilClient.is_unset(request.is_page):
            body['IsPage'] = request.is_page
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.page_num):
            body['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListDeviceGroups',
            version='2020-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vcs_20200515_models.ListDeviceGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_device_groups(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_device_groups_with_options(request, runtime)

    def list_devices_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.corp_id):
            body['CorpId'] = request.corp_id
        if not UtilClient.is_unset(request.device_name):
            body['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.gb_id):
            body['GbId'] = request.gb_id
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListDevices',
            version='2020-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vcs_20200515_models.ListDevicesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_devices(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_devices_with_options(request, runtime)

    def list_event_algorithm_details_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.corp_id):
            body['CorpId'] = request.corp_id
        if not UtilClient.is_unset(request.data_source_id):
            body['DataSourceId'] = request.data_source_id
        if not UtilClient.is_unset(request.end_time):
            body['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.event_type):
            body['EventType'] = request.event_type
        if not UtilClient.is_unset(request.event_value):
            body['EventValue'] = request.event_value
        if not UtilClient.is_unset(request.extend_value):
            body['ExtendValue'] = request.extend_value
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.record_id):
            body['RecordId'] = request.record_id
        if not UtilClient.is_unset(request.source_id):
            body['SourceId'] = request.source_id
        if not UtilClient.is_unset(request.start_time):
            body['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListEventAlgorithmDetails',
            version='2020-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vcs_20200515_models.ListEventAlgorithmDetailsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_event_algorithm_details(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_event_algorithm_details_with_options(request, runtime)

    def list_event_algorithm_results_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.corp_id):
            body['CorpId'] = request.corp_id
        if not UtilClient.is_unset(request.data_source_id):
            body['DataSourceId'] = request.data_source_id
        if not UtilClient.is_unset(request.end_time):
            body['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.event_type):
            body['EventType'] = request.event_type
        if not UtilClient.is_unset(request.extend_value):
            body['ExtendValue'] = request.extend_value
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.start_time):
            body['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListEventAlgorithmResults',
            version='2020-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vcs_20200515_models.ListEventAlgorithmResultsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_event_algorithm_results(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_event_algorithm_results_with_options(request, runtime)

    def list_face_algorithm_results_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.algorithm_type):
            body['AlgorithmType'] = request.algorithm_type
        if not UtilClient.is_unset(request.corp_id):
            body['CorpId'] = request.corp_id
        if not UtilClient.is_unset(request.data_source_id):
            body['DataSourceId'] = request.data_source_id
        if not UtilClient.is_unset(request.end_time):
            body['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.start_time):
            body['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListFaceAlgorithmResults',
            version='2020-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vcs_20200515_models.ListFaceAlgorithmResultsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_face_algorithm_results(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_face_algorithm_results_with_options(request, runtime)

    def list_instances_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListInstances',
            version='2020-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vcs_20200515_models.ListInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_instances(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_instances_with_options(request, runtime)

    def list_metrics_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.aggregate_type):
            body['AggregateType'] = request.aggregate_type
        if not UtilClient.is_unset(request.corp_id):
            body['CorpId'] = request.corp_id
        if not UtilClient.is_unset(request.end_time):
            body['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.start_time):
            body['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.tag_code):
            body['TagCode'] = request.tag_code
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListMetrics',
            version='2020-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vcs_20200515_models.ListMetricsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_metrics(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_metrics_with_options(request, runtime)

    def list_motor_algorithm_results_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.algorithm_type):
            body['AlgorithmType'] = request.algorithm_type
        if not UtilClient.is_unset(request.corp_id):
            body['CorpId'] = request.corp_id
        if not UtilClient.is_unset(request.data_source_id):
            body['DataSourceId'] = request.data_source_id
        if not UtilClient.is_unset(request.end_time):
            body['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.plate_number):
            body['PlateNumber'] = request.plate_number
        if not UtilClient.is_unset(request.start_time):
            body['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListMotorAlgorithmResults',
            version='2020-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vcs_20200515_models.ListMotorAlgorithmResultsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_motor_algorithm_results(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_motor_algorithm_results_with_options(request, runtime)

    def list_nvrchannel_device_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.device_code):
            body['DeviceCode'] = request.device_code
        if not UtilClient.is_unset(request.is_page):
            body['IsPage'] = request.is_page
        if not UtilClient.is_unset(request.page_num):
            body['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListNVRChannelDevice',
            version='2020-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vcs_20200515_models.ListNVRChannelDeviceResponse(),
            self.call_api(params, req, runtime)
        )

    def list_nvrchannel_device(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_nvrchannel_device_with_options(request, runtime)

    def list_nvrdevice_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.corp_id_list):
            body['CorpIdList'] = request.corp_id_list
        if not UtilClient.is_unset(request.device_code):
            body['DeviceCode'] = request.device_code
        if not UtilClient.is_unset(request.is_page):
            body['IsPage'] = request.is_page
        if not UtilClient.is_unset(request.page_num):
            body['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListNVRDevice',
            version='2020-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vcs_20200515_models.ListNVRDeviceResponse(),
            self.call_api(params, req, runtime)
        )

    def list_nvrdevice(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_nvrdevice_with_options(request, runtime)

    def list_person_trace_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.corp_id):
            body['CorpId'] = request.corp_id
        if not UtilClient.is_unset(request.data_source_id):
            body['DataSourceId'] = request.data_source_id
        if not UtilClient.is_unset(request.end_time):
            body['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.group_id):
            body['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.person_id):
            body['PersonId'] = request.person_id
        if not UtilClient.is_unset(request.start_time):
            body['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListPersonTrace',
            version='2020-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vcs_20200515_models.ListPersonTraceResponse(),
            self.call_api(params, req, runtime)
        )

    def list_person_trace(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_person_trace_with_options(request, runtime)

    def list_person_trace_details_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.corp_id):
            body['CorpId'] = request.corp_id
        if not UtilClient.is_unset(request.data_source_id):
            body['DataSourceId'] = request.data_source_id
        if not UtilClient.is_unset(request.end_time):
            body['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.person_id):
            body['PersonId'] = request.person_id
        if not UtilClient.is_unset(request.start_time):
            body['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.sub_id):
            body['SubId'] = request.sub_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListPersonTraceDetails',
            version='2020-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vcs_20200515_models.ListPersonTraceDetailsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_person_trace_details(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_person_trace_details_with_options(request, runtime)

    def list_person_visit_count_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.aggregate_type):
            body['AggregateType'] = request.aggregate_type
        if not UtilClient.is_unset(request.corp_id):
            body['CorpId'] = request.corp_id
        if not UtilClient.is_unset(request.count_type):
            body['CountType'] = request.count_type
        if not UtilClient.is_unset(request.end_time):
            body['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.max_val):
            body['MaxVal'] = request.max_val
        if not UtilClient.is_unset(request.min_val):
            body['MinVal'] = request.min_val
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.start_time):
            body['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.tag_code):
            body['TagCode'] = request.tag_code
        if not UtilClient.is_unset(request.time_aggregate_type):
            body['TimeAggregateType'] = request.time_aggregate_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListPersonVisitCount',
            version='2020-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vcs_20200515_models.ListPersonVisitCountResponse(),
            self.call_api(params, req, runtime)
        )

    def list_person_visit_count(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_person_visit_count_with_options(request, runtime)

    def list_persons_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.algorithm_type):
            body['AlgorithmType'] = request.algorithm_type
        if not UtilClient.is_unset(request.corp_id):
            body['CorpId'] = request.corp_id
        if not UtilClient.is_unset(request.end_time):
            body['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.page_no):
            body['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.start_time):
            body['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListPersons',
            version='2020-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vcs_20200515_models.ListPersonsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_persons(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_persons_with_options(request, runtime)

    def list_user_groups_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.corp_id):
            query['CorpId'] = request.corp_id
        if not UtilClient.is_unset(request.isv_sub_id):
            query['IsvSubId'] = request.isv_sub_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListUserGroups',
            version='2020-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vcs_20200515_models.ListUserGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_user_groups(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_user_groups_with_options(request, runtime)

    def list_users_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = vcs_20200515_models.ListUsersShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.person_list):
            request.person_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.person_list, 'PersonList', 'json')
        if not UtilClient.is_unset(tmp_req.user_list):
            request.user_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.user_list, 'UserList', 'json')
        body = {}
        if not UtilClient.is_unset(request.address):
            body['Address'] = request.address
        if not UtilClient.is_unset(request.age):
            body['Age'] = request.age
        if not UtilClient.is_unset(request.attachment):
            body['Attachment'] = request.attachment
        if not UtilClient.is_unset(request.biz_id):
            body['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.corp_id):
            body['CorpId'] = request.corp_id
        if not UtilClient.is_unset(request.face_image_url):
            body['FaceImageUrl'] = request.face_image_url
        if not UtilClient.is_unset(request.gender):
            body['Gender'] = request.gender
        if not UtilClient.is_unset(request.id_number):
            body['IdNumber'] = request.id_number
        if not UtilClient.is_unset(request.isv_sub_id):
            body['IsvSubId'] = request.isv_sub_id
        if not UtilClient.is_unset(request.matching_rate_threshold):
            body['MatchingRateThreshold'] = request.matching_rate_threshold
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.person_list_shrink):
            body['PersonList'] = request.person_list_shrink
        if not UtilClient.is_unset(request.phone_no):
            body['PhoneNo'] = request.phone_no
        if not UtilClient.is_unset(request.plate_no):
            body['PlateNo'] = request.plate_no
        if not UtilClient.is_unset(request.user_group_id):
            body['UserGroupId'] = request.user_group_id
        if not UtilClient.is_unset(request.user_list_shrink):
            body['UserList'] = request.user_list_shrink
        if not UtilClient.is_unset(request.user_name):
            body['UserName'] = request.user_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListUsers',
            version='2020-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vcs_20200515_models.ListUsersResponse(),
            self.call_api(params, req, runtime)
        )

    def list_users(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_users_with_options(request, runtime)

    def modify_device_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.audio_enable):
            body['AudioEnable'] = request.audio_enable
        if not UtilClient.is_unset(request.device_address):
            body['DeviceAddress'] = request.device_address
        if not UtilClient.is_unset(request.device_direction):
            body['DeviceDirection'] = request.device_direction
        if not UtilClient.is_unset(request.device_id):
            body['DeviceId'] = request.device_id
        if not UtilClient.is_unset(request.device_ip):
            body['DeviceIp'] = request.device_ip
        if not UtilClient.is_unset(request.device_model):
            body['DeviceModel'] = request.device_model
        if not UtilClient.is_unset(request.device_name):
            body['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.device_rate):
            body['DeviceRate'] = request.device_rate
        if not UtilClient.is_unset(request.device_resolution):
            body['DeviceResolution'] = request.device_resolution
        if not UtilClient.is_unset(request.device_site):
            body['DeviceSite'] = request.device_site
        if not UtilClient.is_unset(request.device_sub_type):
            body['DeviceSubType'] = request.device_sub_type
        if not UtilClient.is_unset(request.encode_format):
            body['EncodeFormat'] = request.encode_format
        if not UtilClient.is_unset(request.frame_rate):
            body['FrameRate'] = request.frame_rate
        if not UtilClient.is_unset(request.gov_length):
            body['GovLength'] = request.gov_length
        if not UtilClient.is_unset(request.latitude):
            body['Latitude'] = request.latitude
        if not UtilClient.is_unset(request.longitude):
            body['Longitude'] = request.longitude
        if not UtilClient.is_unset(request.osdtime_enable):
            body['OSDTimeEnable'] = request.osdtime_enable
        if not UtilClient.is_unset(request.osdtime_type):
            body['OSDTimeType'] = request.osdtime_type
        if not UtilClient.is_unset(request.osdtime_x):
            body['OSDTimeX'] = request.osdtime_x
        if not UtilClient.is_unset(request.osdtime_y):
            body['OSDTimeY'] = request.osdtime_y
        if not UtilClient.is_unset(request.password):
            body['Password'] = request.password
        if not UtilClient.is_unset(request.vendor):
            body['Vendor'] = request.vendor
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifyDevice',
            version='2020-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vcs_20200515_models.ModifyDeviceResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_device(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_device_with_options(request, runtime)

    def peek_nvr_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.corp_id):
            body['CorpId'] = request.corp_id
        if not UtilClient.is_unset(request.device_id):
            body['DeviceId'] = request.device_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PeekNvr',
            version='2020-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vcs_20200515_models.PeekNvrResponse(),
            self.call_api(params, req, runtime)
        )

    def peek_nvr(self, request):
        runtime = util_models.RuntimeOptions()
        return self.peek_nvr_with_options(request, runtime)

    def raise_devices_storage_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.json):
            body['Json'] = request.json
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RaiseDevicesStorage',
            version='2020-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vcs_20200515_models.RaiseDevicesStorageResponse(),
            self.call_api(params, req, runtime)
        )

    def raise_devices_storage(self, request):
        runtime = util_models.RuntimeOptions()
        return self.raise_devices_storage_with_options(request, runtime)

    def recognize_face_quality_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.corp_id):
            body['CorpId'] = request.corp_id
        if not UtilClient.is_unset(request.pic_content):
            body['PicContent'] = request.pic_content
        if not UtilClient.is_unset(request.pic_format):
            body['PicFormat'] = request.pic_format
        if not UtilClient.is_unset(request.pic_url):
            body['PicUrl'] = request.pic_url
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RecognizeFaceQuality',
            version='2020-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vcs_20200515_models.RecognizeFaceQualityResponse(),
            self.call_api(params, req, runtime)
        )

    def recognize_face_quality(self, request):
        runtime = util_models.RuntimeOptions()
        return self.recognize_face_quality_with_options(request, runtime)

    def recognize_image_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.corp_id):
            body['CorpId'] = request.corp_id
        if not UtilClient.is_unset(request.pic_content):
            body['PicContent'] = request.pic_content
        if not UtilClient.is_unset(request.pic_format):
            body['PicFormat'] = request.pic_format
        if not UtilClient.is_unset(request.pic_url):
            body['PicUrl'] = request.pic_url
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RecognizeImage',
            version='2020-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vcs_20200515_models.RecognizeImageResponse(),
            self.call_api(params, req, runtime)
        )

    def recognize_image(self, request):
        runtime = util_models.RuntimeOptions()
        return self.recognize_image_with_options(request, runtime)

    def register_device_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.device_id):
            body['DeviceId'] = request.device_id
        if not UtilClient.is_unset(request.device_sn):
            body['DeviceSn'] = request.device_sn
        if not UtilClient.is_unset(request.device_time_stamp):
            body['DeviceTimeStamp'] = request.device_time_stamp
        if not UtilClient.is_unset(request.server_id):
            body['ServerId'] = request.server_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RegisterDevice',
            version='2020-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vcs_20200515_models.RegisterDeviceResponse(),
            self.call_api(params, req, runtime)
        )

    def register_device(self, request):
        runtime = util_models.RuntimeOptions()
        return self.register_device_with_options(request, runtime)

    def remove_camera_for_instance_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = vcs_20200515_models.RemoveCameraForInstanceShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.camera_ids):
            request.camera_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.camera_ids, 'CameraIds', 'json')
        body = {}
        if not UtilClient.is_unset(request.camera_ids_shrink):
            body['CameraIds'] = request.camera_ids_shrink
        if not UtilClient.is_unset(request.instance_id):
            body['InstanceId'] = request.instance_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RemoveCameraForInstance',
            version='2020-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vcs_20200515_models.RemoveCameraForInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    def remove_camera_for_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.remove_camera_for_instance_with_options(request, runtime)

    def remove_search_items_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.search_item_ids):
            body['SearchItemIds'] = request.search_item_ids
        if not UtilClient.is_unset(request.search_table_id):
            body['SearchTableId'] = request.search_table_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RemoveSearchItems',
            version='2020-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vcs_20200515_models.RemoveSearchItemsResponse(),
            self.call_api(params, req, runtime)
        )

    def remove_search_items(self, request):
        runtime = util_models.RuntimeOptions()
        return self.remove_search_items_with_options(request, runtime)

    def remove_watch_items_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.watch_item_ids):
            body['WatchItemIds'] = request.watch_item_ids
        if not UtilClient.is_unset(request.watch_policy_id):
            body['WatchPolicyId'] = request.watch_policy_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RemoveWatchItems',
            version='2020-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vcs_20200515_models.RemoveWatchItemsResponse(),
            self.call_api(params, req, runtime)
        )

    def remove_watch_items(self, request):
        runtime = util_models.RuntimeOptions()
        return self.remove_watch_items_with_options(request, runtime)

    def save_video_summary_task_video_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.corp_id):
            body['CorpId'] = request.corp_id
        if not UtilClient.is_unset(request.save_video):
            body['SaveVideo'] = request.save_video
        if not UtilClient.is_unset(request.task_id):
            body['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SaveVideoSummaryTaskVideo',
            version='2020-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vcs_20200515_models.SaveVideoSummaryTaskVideoResponse(),
            self.call_api(params, req, runtime)
        )

    def save_video_summary_task_video(self, request):
        runtime = util_models.RuntimeOptions()
        return self.save_video_summary_task_video_with_options(request, runtime)

    def scan_sub_device_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.corp_id):
            body['CorpId'] = request.corp_id
        if not UtilClient.is_unset(request.device_id):
            body['DeviceId'] = request.device_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ScanSubDevice',
            version='2020-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vcs_20200515_models.ScanSubDeviceResponse(),
            self.call_api(params, req, runtime)
        )

    def scan_sub_device(self, request):
        runtime = util_models.RuntimeOptions()
        return self.scan_sub_device_with_options(request, runtime)

    def search_body_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = vcs_20200515_models.SearchBodyShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.option_list):
            request.option_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.option_list, 'OptionList', 'json')
        body = {}
        if not UtilClient.is_unset(request.corp_id):
            body['CorpId'] = request.corp_id
        if not UtilClient.is_unset(request.end_time_stamp):
            body['EndTimeStamp'] = request.end_time_stamp
        if not UtilClient.is_unset(request.gb_id):
            body['GbId'] = request.gb_id
        if not UtilClient.is_unset(request.option_list_shrink):
            body['OptionList'] = request.option_list_shrink
        if not UtilClient.is_unset(request.page_no):
            body['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.start_time_stamp):
            body['StartTimeStamp'] = request.start_time_stamp
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SearchBody',
            version='2020-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vcs_20200515_models.SearchBodyResponse(),
            self.call_api(params, req, runtime)
        )

    def search_body(self, request):
        runtime = util_models.RuntimeOptions()
        return self.search_body_with_options(request, runtime)

    def search_face_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = vcs_20200515_models.SearchFaceShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.option_list):
            request.option_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.option_list, 'OptionList', 'json')
        body = {}
        if not UtilClient.is_unset(request.corp_id):
            body['CorpId'] = request.corp_id
        if not UtilClient.is_unset(request.end_time_stamp):
            body['EndTimeStamp'] = request.end_time_stamp
        if not UtilClient.is_unset(request.gb_id):
            body['GbId'] = request.gb_id
        if not UtilClient.is_unset(request.option_list_shrink):
            body['OptionList'] = request.option_list_shrink
        if not UtilClient.is_unset(request.page_no):
            body['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.start_time_stamp):
            body['StartTimeStamp'] = request.start_time_stamp
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SearchFace',
            version='2020-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vcs_20200515_models.SearchFaceResponse(),
            self.call_api(params, req, runtime)
        )

    def search_face(self, request):
        runtime = util_models.RuntimeOptions()
        return self.search_face_with_options(request, runtime)

    def search_item_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.item_image_data):
            body['ItemImageData'] = request.item_image_data
        if not UtilClient.is_unset(request.item_image_url):
            body['ItemImageUrl'] = request.item_image_url
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search_table_ids):
            body['SearchTableIds'] = request.search_table_ids
        if not UtilClient.is_unset(request.similarity_threshold):
            body['SimilarityThreshold'] = request.similarity_threshold
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SearchItem',
            version='2020-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vcs_20200515_models.SearchItemResponse(),
            self.call_api(params, req, runtime)
        )

    def search_item(self, request):
        runtime = util_models.RuntimeOptions()
        return self.search_item_with_options(request, runtime)

    def search_object_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = vcs_20200515_models.SearchObjectShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.conditions):
            request.conditions_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.conditions, 'Conditions', 'json')
        if not UtilClient.is_unset(tmp_req.device_list):
            request.device_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.device_list, 'DeviceList', 'json')
        if not UtilClient.is_unset(tmp_req.image_path):
            request.image_path_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.image_path, 'ImagePath', 'json')
        body = {}
        if not UtilClient.is_unset(request.algorithm_type):
            body['AlgorithmType'] = request.algorithm_type
        if not UtilClient.is_unset(request.conditions_shrink):
            body['Conditions'] = request.conditions_shrink
        if not UtilClient.is_unset(request.corp_id):
            body['CorpId'] = request.corp_id
        if not UtilClient.is_unset(request.device_list_shrink):
            body['DeviceList'] = request.device_list_shrink
        if not UtilClient.is_unset(request.end_time):
            body['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.image_path_shrink):
            body['ImagePath'] = request.image_path_shrink
        if not UtilClient.is_unset(request.object_type):
            body['ObjectType'] = request.object_type
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.pic_url):
            body['PicUrl'] = request.pic_url
        if not UtilClient.is_unset(request.start_time):
            body['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SearchObject',
            version='2020-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vcs_20200515_models.SearchObjectResponse(),
            self.call_api(params, req, runtime)
        )

    def search_object(self, request):
        runtime = util_models.RuntimeOptions()
        return self.search_object_with_options(request, runtime)

    def search_target_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.begin_time):
            body['BeginTime'] = request.begin_time
        if not UtilClient.is_unset(request.corp_id):
            body['CorpId'] = request.corp_id
        if not UtilClient.is_unset(request.device_list):
            body['DeviceList'] = request.device_list
        if not UtilClient.is_unset(request.end_time):
            body['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.model_id):
            body['ModelId'] = request.model_id
        if not UtilClient.is_unset(request.order_by):
            body['OrderBy'] = request.order_by
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.similarity_threshold):
            body['SimilarityThreshold'] = request.similarity_threshold
        if not UtilClient.is_unset(request.target_attributes):
            body['TargetAttributes'] = request.target_attributes
        if not UtilClient.is_unset(request.target_image_data):
            body['TargetImageData'] = request.target_image_data
        if not UtilClient.is_unset(request.target_image_url):
            body['TargetImageUrl'] = request.target_image_url
        if not UtilClient.is_unset(request.target_type):
            body['TargetType'] = request.target_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SearchTarget',
            version='2020-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vcs_20200515_models.SearchTargetResponse(),
            self.call_api(params, req, runtime)
        )

    def search_target(self, request):
        runtime = util_models.RuntimeOptions()
        return self.search_target_with_options(request, runtime)

    def set_aiot_storage_info_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = vcs_20200515_models.SetAiotStorageInfoShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.event_alarm_mq):
            request.event_alarm_mq_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.event_alarm_mq), 'EventAlarmMq', 'json')
        if not UtilClient.is_unset(tmp_req.event_alarm_picture_storage):
            request.event_alarm_picture_storage_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.event_alarm_picture_storage), 'EventAlarmPictureStorage', 'json')
        body = {}
        if not UtilClient.is_unset(request.event_alarm_mq_shrink):
            body['EventAlarmMq'] = request.event_alarm_mq_shrink
        if not UtilClient.is_unset(request.event_alarm_picture_storage_shrink):
            body['EventAlarmPictureStorage'] = request.event_alarm_picture_storage_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SetAiotStorageInfo',
            version='2020-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vcs_20200515_models.SetAiotStorageInfoResponse(),
            self.call_api(params, req, runtime)
        )

    def set_aiot_storage_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_aiot_storage_info_with_options(request, runtime)

    def set_stream_mode_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.device_id_list):
            body['DeviceIdList'] = request.device_id_list
        if not UtilClient.is_unset(request.stream_mode):
            body['StreamMode'] = request.stream_mode
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SetStreamMode',
            version='2020-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vcs_20200515_models.SetStreamModeResponse(),
            self.call_api(params, req, runtime)
        )

    def set_stream_mode(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_stream_mode_with_options(request, runtime)

    def start_model_service_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.model_service_id):
            body['ModelServiceId'] = request.model_service_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='StartModelService',
            version='2020-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vcs_20200515_models.StartModelServiceResponse(),
            self.call_api(params, req, runtime)
        )

    def start_model_service(self, request):
        runtime = util_models.RuntimeOptions()
        return self.start_model_service_with_options(request, runtime)

    def start_streams_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.device_id_list):
            body['DeviceIdList'] = request.device_id_list
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='StartStreams',
            version='2020-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vcs_20200515_models.StartStreamsResponse(),
            self.call_api(params, req, runtime)
        )

    def start_streams(self, request):
        runtime = util_models.RuntimeOptions()
        return self.start_streams_with_options(request, runtime)

    def stop_model_service_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.model_service_id):
            body['ModelServiceId'] = request.model_service_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='StopModelService',
            version='2020-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vcs_20200515_models.StopModelServiceResponse(),
            self.call_api(params, req, runtime)
        )

    def stop_model_service(self, request):
        runtime = util_models.RuntimeOptions()
        return self.stop_model_service_with_options(request, runtime)

    def stop_monitor_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.algorithm_vendor):
            body['AlgorithmVendor'] = request.algorithm_vendor
        if not UtilClient.is_unset(request.task_id):
            body['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='StopMonitor',
            version='2020-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vcs_20200515_models.StopMonitorResponse(),
            self.call_api(params, req, runtime)
        )

    def stop_monitor(self, request):
        runtime = util_models.RuntimeOptions()
        return self.stop_monitor_with_options(request, runtime)

    def stop_streams_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.device_id_list):
            body['DeviceIdList'] = request.device_id_list
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='StopStreams',
            version='2020-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vcs_20200515_models.StopStreamsResponse(),
            self.call_api(params, req, runtime)
        )

    def stop_streams(self, request):
        runtime = util_models.RuntimeOptions()
        return self.stop_streams_with_options(request, runtime)

    def sync_device_time_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.device_sn):
            body['DeviceSn'] = request.device_sn
        if not UtilClient.is_unset(request.device_time_stamp):
            body['DeviceTimeStamp'] = request.device_time_stamp
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SyncDeviceTime',
            version='2020-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vcs_20200515_models.SyncDeviceTimeResponse(),
            self.call_api(params, req, runtime)
        )

    def sync_device_time(self, request):
        runtime = util_models.RuntimeOptions()
        return self.sync_device_time_with_options(request, runtime)

    def test_cross_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.data):
            body['Data'] = request.data
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='TestCross',
            version='2020-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='string'
        )
        return TeaCore.from_map(
            vcs_20200515_models.TestCrossResponse(),
            self.call_api(params, req, runtime)
        )

    def test_cross(self, request):
        runtime = util_models.RuntimeOptions()
        return self.test_cross_with_options(request, runtime)

    def unbind_corp_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.corp_group_id):
            body['CorpGroupId'] = request.corp_group_id
        if not UtilClient.is_unset(request.corp_id):
            body['CorpId'] = request.corp_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UnbindCorpGroup',
            version='2020-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vcs_20200515_models.UnbindCorpGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def unbind_corp_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.unbind_corp_group_with_options(request, runtime)

    def unbind_devices_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.corp_id):
            body['CorpId'] = request.corp_id
        if not UtilClient.is_unset(request.device_id):
            body['DeviceId'] = request.device_id
        if not UtilClient.is_unset(request.sub_device_id_list):
            body['SubDeviceIdList'] = request.sub_device_id_list
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UnbindDevices',
            version='2020-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vcs_20200515_models.UnbindDevicesResponse(),
            self.call_api(params, req, runtime)
        )

    def unbind_devices(self, request):
        runtime = util_models.RuntimeOptions()
        return self.unbind_devices_with_options(request, runtime)

    def unbind_person_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.corp_id):
            body['CorpId'] = request.corp_id
        if not UtilClient.is_unset(request.isv_sub_id):
            body['IsvSubId'] = request.isv_sub_id
        if not UtilClient.is_unset(request.profile_id):
            body['ProfileId'] = request.profile_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UnbindPerson',
            version='2020-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vcs_20200515_models.UnbindPersonResponse(),
            self.call_api(params, req, runtime)
        )

    def unbind_person(self, request):
        runtime = util_models.RuntimeOptions()
        return self.unbind_person_with_options(request, runtime)

    def unbind_user_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.corp_id):
            body['CorpId'] = request.corp_id
        if not UtilClient.is_unset(request.isv_sub_id):
            body['IsvSubId'] = request.isv_sub_id
        if not UtilClient.is_unset(request.user_id):
            body['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UnbindUser',
            version='2020-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vcs_20200515_models.UnbindUserResponse(),
            self.call_api(params, req, runtime)
        )

    def unbind_user(self, request):
        runtime = util_models.RuntimeOptions()
        return self.unbind_user_with_options(request, runtime)

    def update_aiot_device_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = vcs_20200515_models.UpdateAiotDeviceShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.aiot_device):
            request.aiot_device_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.aiot_device), 'AiotDevice', 'json')
        body = {}
        if not UtilClient.is_unset(request.aiot_device_shrink):
            body['AiotDevice'] = request.aiot_device_shrink
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateAiotDevice',
            version='2020-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vcs_20200515_models.UpdateAiotDeviceResponse(),
            self.call_api(params, req, runtime)
        )

    def update_aiot_device(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_aiot_device_with_options(request, runtime)

    def update_aiot_person_table_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        body_flat = {}
        if not UtilClient.is_unset(request.person_table):
            body_flat['PersonTable'] = request.person_table
        body = TeaCore.merge(body,
            OpenApiUtilClient.query(body_flat))
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateAiotPersonTable',
            version='2020-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vcs_20200515_models.UpdateAiotPersonTableResponse(),
            self.call_api(params, req, runtime)
        )

    def update_aiot_person_table(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_aiot_person_table_with_options(request, runtime)

    def update_aiot_person_table_item_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.person_table_id):
            body['PersonTableId'] = request.person_table_id
        body_flat = {}
        if not UtilClient.is_unset(request.person_table_item):
            body_flat['PersonTableItem'] = request.person_table_item
        body = TeaCore.merge(body,
            OpenApiUtilClient.query(body_flat))
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateAiotPersonTableItem',
            version='2020-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vcs_20200515_models.UpdateAiotPersonTableItemResponse(),
            self.call_api(params, req, runtime)
        )

    def update_aiot_person_table_item(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_aiot_person_table_item_with_options(request, runtime)

    def update_aiot_vehicle_table_item_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = vcs_20200515_models.UpdateAiotVehicleTableItemShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.vehicle_table_item):
            request.vehicle_table_item_shrink = OpenApiUtilClient.array_to_string_with_specified_style(TeaCore.to_map(tmp_req.vehicle_table_item), 'VehicleTableItem', 'json')
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.vehicle_table_id):
            body['VehicleTableId'] = request.vehicle_table_id
        if not UtilClient.is_unset(request.vehicle_table_item_shrink):
            body['VehicleTableItem'] = request.vehicle_table_item_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateAiotVehicleTableItem',
            version='2020-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vcs_20200515_models.UpdateAiotVehicleTableItemResponse(),
            self.call_api(params, req, runtime)
        )

    def update_aiot_vehicle_table_item(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_aiot_vehicle_table_item_with_options(request, runtime)

    def update_corp_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_name):
            body['AppName'] = request.app_name
        if not UtilClient.is_unset(request.corp_id):
            body['CorpId'] = request.corp_id
        if not UtilClient.is_unset(request.corp_name):
            body['CorpName'] = request.corp_name
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.icon_path):
            body['IconPath'] = request.icon_path
        if not UtilClient.is_unset(request.isv_sub_id):
            body['IsvSubId'] = request.isv_sub_id
        if not UtilClient.is_unset(request.parent_corp_id):
            body['ParentCorpId'] = request.parent_corp_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateCorp',
            version='2020-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vcs_20200515_models.UpdateCorpResponse(),
            self.call_api(params, req, runtime)
        )

    def update_corp(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_corp_with_options(request, runtime)

    def update_data_source_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.data_source_id):
            body['DataSourceId'] = request.data_source_id
        if not UtilClient.is_unset(request.data_source_name):
            body['DataSourceName'] = request.data_source_name
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.url):
            body['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateDataSource',
            version='2020-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vcs_20200515_models.UpdateDataSourceResponse(),
            self.call_api(params, req, runtime)
        )

    def update_data_source(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_data_source_with_options(request, runtime)

    def update_device_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.bit_rate):
            body['BitRate'] = request.bit_rate
        if not UtilClient.is_unset(request.corp_id):
            body['CorpId'] = request.corp_id
        if not UtilClient.is_unset(request.device_address):
            body['DeviceAddress'] = request.device_address
        if not UtilClient.is_unset(request.device_direction):
            body['DeviceDirection'] = request.device_direction
        if not UtilClient.is_unset(request.device_name):
            body['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.device_resolution):
            body['DeviceResolution'] = request.device_resolution
        if not UtilClient.is_unset(request.device_site):
            body['DeviceSite'] = request.device_site
        if not UtilClient.is_unset(request.device_type):
            body['DeviceType'] = request.device_type
        if not UtilClient.is_unset(request.gb_id):
            body['GbId'] = request.gb_id
        if not UtilClient.is_unset(request.vendor):
            body['Vendor'] = request.vendor
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateDevice',
            version='2020-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vcs_20200515_models.UpdateDeviceResponse(),
            self.call_api(params, req, runtime)
        )

    def update_device(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_device_with_options(request, runtime)

    def update_device_capture_strategy_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.device_code):
            body['DeviceCode'] = request.device_code
        if not UtilClient.is_unset(request.device_type):
            body['DeviceType'] = request.device_type
        if not UtilClient.is_unset(request.monday_capture_strategy):
            body['MondayCaptureStrategy'] = request.monday_capture_strategy
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateDeviceCaptureStrategy',
            version='2020-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vcs_20200515_models.UpdateDeviceCaptureStrategyResponse(),
            self.call_api(params, req, runtime)
        )

    def update_device_capture_strategy(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_device_capture_strategy_with_options(request, runtime)

    def update_devices_storage_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = vcs_20200515_models.UpdateDevicesStorageShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.update_storage_requests):
            request.update_storage_requests_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.update_storage_requests, 'UpdateStorageRequests', 'json')
        body = {}
        if not UtilClient.is_unset(request.update_storage_requests_shrink):
            body['UpdateStorageRequests'] = request.update_storage_requests_shrink
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateDevicesStorage',
            version='2020-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vcs_20200515_models.UpdateDevicesStorageResponse(),
            self.call_api(params, req, runtime)
        )

    def update_devices_storage(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_devices_storage_with_options(request, runtime)

    def update_double_verification_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        body_flat = {}
        if not UtilClient.is_unset(request.double_verification_group):
            body_flat['DoubleVerificationGroup'] = request.double_verification_group
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        body = TeaCore.merge(body,
            OpenApiUtilClient.query(body_flat))
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateDoubleVerificationGroup',
            version='2020-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vcs_20200515_models.UpdateDoubleVerificationGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def update_double_verification_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_double_verification_group_with_options(request, runtime)

    def update_model_service_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.model_service_id):
            body['ModelServiceId'] = request.model_service_id
        if not UtilClient.is_unset(request.model_service_name):
            body['ModelServiceName'] = request.model_service_name
        if not UtilClient.is_unset(request.qps_required):
            body['QpsRequired'] = request.qps_required
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateModelService',
            version='2020-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vcs_20200515_models.UpdateModelServiceResponse(),
            self.call_api(params, req, runtime)
        )

    def update_model_service(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_model_service_with_options(request, runtime)

    def update_monitor_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.algorithm_vendor):
            body['AlgorithmVendor'] = request.algorithm_vendor
        if not UtilClient.is_unset(request.attribute_name):
            body['AttributeName'] = request.attribute_name
        if not UtilClient.is_unset(request.attribute_operate_type):
            body['AttributeOperateType'] = request.attribute_operate_type
        if not UtilClient.is_unset(request.attribute_value_list):
            body['AttributeValueList'] = request.attribute_value_list
        if not UtilClient.is_unset(request.corp_id):
            body['CorpId'] = request.corp_id
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.device_list):
            body['DeviceList'] = request.device_list
        if not UtilClient.is_unset(request.device_operate_type):
            body['DeviceOperateType'] = request.device_operate_type
        if not UtilClient.is_unset(request.notifier_app_secret):
            body['NotifierAppSecret'] = request.notifier_app_secret
        if not UtilClient.is_unset(request.notifier_extend_values):
            body['NotifierExtendValues'] = request.notifier_extend_values
        if not UtilClient.is_unset(request.notifier_time_out):
            body['NotifierTimeOut'] = request.notifier_time_out
        if not UtilClient.is_unset(request.notifier_type):
            body['NotifierType'] = request.notifier_type
        if not UtilClient.is_unset(request.notifier_url):
            body['NotifierUrl'] = request.notifier_url
        if not UtilClient.is_unset(request.pic_list):
            body['PicList'] = request.pic_list
        if not UtilClient.is_unset(request.pic_operate_type):
            body['PicOperateType'] = request.pic_operate_type
        if not UtilClient.is_unset(request.rule_expression):
            body['RuleExpression'] = request.rule_expression
        if not UtilClient.is_unset(request.rule_name):
            body['RuleName'] = request.rule_name
        if not UtilClient.is_unset(request.task_id):
            body['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateMonitor',
            version='2020-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vcs_20200515_models.UpdateMonitorResponse(),
            self.call_api(params, req, runtime)
        )

    def update_monitor(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_monitor_with_options(request, runtime)

    def update_profile_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.biz_id):
            body['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.catalog_id):
            body['CatalogId'] = request.catalog_id
        if not UtilClient.is_unset(request.corp_id):
            body['CorpId'] = request.corp_id
        if not UtilClient.is_unset(request.face_url):
            body['FaceUrl'] = request.face_url
        if not UtilClient.is_unset(request.gender):
            body['Gender'] = request.gender
        if not UtilClient.is_unset(request.id_number):
            body['IdNumber'] = request.id_number
        if not UtilClient.is_unset(request.isv_sub_id):
            body['IsvSubId'] = request.isv_sub_id
        if not UtilClient.is_unset(request.live_address):
            body['LiveAddress'] = request.live_address
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.phone_no):
            body['PhoneNo'] = request.phone_no
        if not UtilClient.is_unset(request.plate_no):
            body['PlateNo'] = request.plate_no
        if not UtilClient.is_unset(request.profile_id):
            body['ProfileId'] = request.profile_id
        if not UtilClient.is_unset(request.scene_type):
            body['SceneType'] = request.scene_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateProfile',
            version='2020-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vcs_20200515_models.UpdateProfileResponse(),
            self.call_api(params, req, runtime)
        )

    def update_profile(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_profile_with_options(request, runtime)

    def update_profile_catalog_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.catalog_id):
            body['CatalogId'] = request.catalog_id
        if not UtilClient.is_unset(request.catalog_name):
            body['CatalogName'] = request.catalog_name
        if not UtilClient.is_unset(request.corp_id):
            body['CorpId'] = request.corp_id
        if not UtilClient.is_unset(request.isv_sub_id):
            body['IsvSubId'] = request.isv_sub_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateProfileCatalog',
            version='2020-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vcs_20200515_models.UpdateProfileCatalogResponse(),
            self.call_api(params, req, runtime)
        )

    def update_profile_catalog(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_profile_catalog_with_options(request, runtime)

    def update_search_table_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.search_table_id):
            body['SearchTableId'] = request.search_table_id
        if not UtilClient.is_unset(request.search_table_name):
            body['SearchTableName'] = request.search_table_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateSearchTable',
            version='2020-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vcs_20200515_models.UpdateSearchTableResponse(),
            self.call_api(params, req, runtime)
        )

    def update_search_table(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_search_table_with_options(request, runtime)

    def update_user_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.address):
            body['Address'] = request.address
        if not UtilClient.is_unset(request.age):
            body['Age'] = request.age
        if not UtilClient.is_unset(request.attachment):
            body['Attachment'] = request.attachment
        if not UtilClient.is_unset(request.biz_id):
            body['BizId'] = request.biz_id
        if not UtilClient.is_unset(request.corp_id):
            body['CorpId'] = request.corp_id
        if not UtilClient.is_unset(request.face_image_content):
            body['FaceImageContent'] = request.face_image_content
        if not UtilClient.is_unset(request.face_image_url):
            body['FaceImageUrl'] = request.face_image_url
        if not UtilClient.is_unset(request.gender):
            body['Gender'] = request.gender
        if not UtilClient.is_unset(request.id_number):
            body['IdNumber'] = request.id_number
        if not UtilClient.is_unset(request.isv_sub_id):
            body['IsvSubId'] = request.isv_sub_id
        if not UtilClient.is_unset(request.phone_no):
            body['PhoneNo'] = request.phone_no
        if not UtilClient.is_unset(request.plate_no):
            body['PlateNo'] = request.plate_no
        if not UtilClient.is_unset(request.user_group_id):
            body['UserGroupId'] = request.user_group_id
        if not UtilClient.is_unset(request.user_id):
            body['UserId'] = request.user_id
        if not UtilClient.is_unset(request.user_name):
            body['UserName'] = request.user_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateUser',
            version='2020-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vcs_20200515_models.UpdateUserResponse(),
            self.call_api(params, req, runtime)
        )

    def update_user(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_user_with_options(request, runtime)

    def update_user_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.corp_id):
            body['CorpId'] = request.corp_id
        if not UtilClient.is_unset(request.isv_sub_id):
            body['IsvSubId'] = request.isv_sub_id
        if not UtilClient.is_unset(request.user_group_id):
            body['UserGroupId'] = request.user_group_id
        if not UtilClient.is_unset(request.user_group_name):
            body['UserGroupName'] = request.user_group_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateUserGroup',
            version='2020-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vcs_20200515_models.UpdateUserGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def update_user_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_user_group_with_options(request, runtime)

    def update_watch_policy_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.item_match_type):
            body['ItemMatchType'] = request.item_match_type
        if not UtilClient.is_unset(request.similarity_threshold):
            body['SimilarityThreshold'] = request.similarity_threshold
        if not UtilClient.is_unset(request.target_type):
            body['TargetType'] = request.target_type
        if not UtilClient.is_unset(request.watch_mode):
            body['WatchMode'] = request.watch_mode
        if not UtilClient.is_unset(request.watch_policy_id):
            body['WatchPolicyId'] = request.watch_policy_id
        if not UtilClient.is_unset(request.watch_policy_name):
            body['WatchPolicyName'] = request.watch_policy_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateWatchPolicy',
            version='2020-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vcs_20200515_models.UpdateWatchPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    def update_watch_policy(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_watch_policy_with_options(request, runtime)

    def update_watch_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.device_list):
            body['DeviceList'] = request.device_list
        if not UtilClient.is_unset(request.message_receiver):
            body['MessageReceiver'] = request.message_receiver
        if not UtilClient.is_unset(request.schedule_cycle_dates):
            body['ScheduleCycleDates'] = request.schedule_cycle_dates
        if not UtilClient.is_unset(request.schedule_times):
            body['ScheduleTimes'] = request.schedule_times
        if not UtilClient.is_unset(request.schedule_type):
            body['ScheduleType'] = request.schedule_type
        if not UtilClient.is_unset(request.task_name):
            body['TaskName'] = request.task_name
        if not UtilClient.is_unset(request.watch_policy_ids):
            body['WatchPolicyIds'] = request.watch_policy_ids
        if not UtilClient.is_unset(request.watch_task_id):
            body['WatchTaskId'] = request.watch_task_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateWatchTask',
            version='2020-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vcs_20200515_models.UpdateWatchTaskResponse(),
            self.call_api(params, req, runtime)
        )

    def update_watch_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_watch_task_with_options(request, runtime)

    def upload_file_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.corp_id):
            body['CorpId'] = request.corp_id
        if not UtilClient.is_unset(request.data_source_id):
            body['DataSourceId'] = request.data_source_id
        if not UtilClient.is_unset(request.file_alias_name):
            body['FileAliasName'] = request.file_alias_name
        if not UtilClient.is_unset(request.file_content):
            body['FileContent'] = request.file_content
        if not UtilClient.is_unset(request.file_name):
            body['FileName'] = request.file_name
        if not UtilClient.is_unset(request.file_path):
            body['FilePath'] = request.file_path
        if not UtilClient.is_unset(request.file_type):
            body['FileType'] = request.file_type
        if not UtilClient.is_unset(request.md5):
            body['MD5'] = request.md5
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UploadFile',
            version='2020-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vcs_20200515_models.UploadFileResponse(),
            self.call_api(params, req, runtime)
        )

    def upload_file(self, request):
        runtime = util_models.RuntimeOptions()
        return self.upload_file_with_options(request, runtime)

    def upload_image_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.image_url):
            body['ImageUrl'] = request.image_url
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UploadImage',
            version='2020-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vcs_20200515_models.UploadImageResponse(),
            self.call_api(params, req, runtime)
        )

    def upload_image(self, request):
        runtime = util_models.RuntimeOptions()
        return self.upload_image_with_options(request, runtime)

    def verify_device_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.device_address):
            body['DeviceAddress'] = request.device_address
        if not UtilClient.is_unset(request.file_path):
            body['FilePath'] = request.file_path
        if not UtilClient.is_unset(request.nvr_existed):
            body['NvrExisted'] = request.nvr_existed
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='VerifyDevice',
            version='2020-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            vcs_20200515_models.VerifyDeviceResponse(),
            self.call_api(params, req, runtime)
        )

    def verify_device(self, request):
        runtime = util_models.RuntimeOptions()
        return self.verify_device_with_options(request, runtime)
