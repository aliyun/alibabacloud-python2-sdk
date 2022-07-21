# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_iot20180120 import models as iot_20180120_models
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
            'ap-northeast-2-pop': 'iot.aliyuncs.com',
            'ap-south-1': 'iot.aliyuncs.com',
            'ap-southeast-2': 'iot.aliyuncs.com',
            'ap-southeast-3': 'iot.aliyuncs.com',
            'ap-southeast-5': 'iot.aliyuncs.com',
            'cn-beijing-finance-1': 'iot.aliyuncs.com',
            'cn-beijing-finance-pop': 'iot.aliyuncs.com',
            'cn-beijing-gov-1': 'iot.aliyuncs.com',
            'cn-beijing-nu16-b01': 'iot.aliyuncs.com',
            'cn-chengdu': 'iot.aliyuncs.com',
            'cn-edge-1': 'iot.aliyuncs.com',
            'cn-fujian': 'iot.aliyuncs.com',
            'cn-haidian-cm12-c01': 'iot.aliyuncs.com',
            'cn-hangzhou-bj-b01': 'iot.aliyuncs.com',
            'cn-hangzhou-finance': 'iot.aliyuncs.com',
            'cn-hangzhou-internal-prod-1': 'iot.aliyuncs.com',
            'cn-hangzhou-internal-test-1': 'iot.aliyuncs.com',
            'cn-hangzhou-internal-test-2': 'iot.aliyuncs.com',
            'cn-hangzhou-internal-test-3': 'iot.aliyuncs.com',
            'cn-hangzhou-test-306': 'iot.aliyuncs.com',
            'cn-hongkong': 'iot.aliyuncs.com',
            'cn-hongkong-finance-pop': 'iot.aliyuncs.com',
            'cn-huhehaote': 'iot.aliyuncs.com',
            'cn-huhehaote-nebula-1': 'iot.aliyuncs.com',
            'cn-qingdao': 'iot.aliyuncs.com',
            'cn-qingdao-nebula': 'iot.aliyuncs.com',
            'cn-shanghai-et15-b01': 'iot.aliyuncs.com',
            'cn-shanghai-et2-b01': 'iot.aliyuncs.com',
            'cn-shanghai-finance-1': 'iot.aliyuncs.com',
            'cn-shanghai-inner': 'iot.aliyuncs.com',
            'cn-shanghai-internal-test-1': 'iot.aliyuncs.com',
            'cn-shenzhen-finance-1': 'iot.aliyuncs.com',
            'cn-shenzhen-inner': 'iot.aliyuncs.com',
            'cn-shenzhen-st4-d01': 'iot.aliyuncs.com',
            'cn-shenzhen-su18-b01': 'iot.aliyuncs.com',
            'cn-wuhan': 'iot.aliyuncs.com',
            'cn-wulanchabu': 'iot.aliyuncs.com',
            'cn-yushanfang': 'iot.aliyuncs.com',
            'cn-zhangbei': 'iot.aliyuncs.com',
            'cn-zhangbei-na61-b01': 'iot.aliyuncs.com',
            'cn-zhangjiakou': 'iot.aliyuncs.com',
            'cn-zhangjiakou-na62-a01': 'iot.aliyuncs.com',
            'cn-zhengzhou-nebula-1': 'iot.aliyuncs.com',
            'eu-west-1': 'iot.aliyuncs.com',
            'eu-west-1-oxs': 'iot.aliyuncs.com',
            'me-east-1': 'iot.aliyuncs.com',
            'rus-west-1-pop': 'iot.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('iot', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def add_data_for_api_source_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_id):
            query['ApiId'] = request.api_id
        if not UtilClient.is_unset(request.content):
            query['Content'] = request.content
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddDataForApiSource',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.AddDataForApiSourceResponse(),
            self.call_api(params, req, runtime)
        )

    def add_data_for_api_source(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_data_for_api_source_with_options(request, runtime)

    def attach_destination_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.destination_id):
            query['DestinationId'] = request.destination_id
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.is_failover):
            query['IsFailover'] = request.is_failover
        if not UtilClient.is_unset(request.parser_id):
            query['ParserId'] = request.parser_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AttachDestination',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.AttachDestinationResponse(),
            self.call_api(params, req, runtime)
        )

    def attach_destination(self, request):
        runtime = util_models.RuntimeOptions()
        return self.attach_destination_with_options(request, runtime)

    def attach_parser_data_source_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.data_source_id):
            query['DataSourceId'] = request.data_source_id
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.parser_id):
            query['ParserId'] = request.parser_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AttachParserDataSource',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.AttachParserDataSourceResponse(),
            self.call_api(params, req, runtime)
        )

    def attach_parser_data_source(self, request):
        runtime = util_models.RuntimeOptions()
        return self.attach_parser_data_source_with_options(request, runtime)

    def batch_add_data_for_api_source_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = iot_20180120_models.BatchAddDataForApiSourceShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.content_list):
            request.content_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.content_list, 'ContentList', 'json')
        query = {}
        if not UtilClient.is_unset(request.api_id):
            query['ApiId'] = request.api_id
        if not UtilClient.is_unset(request.content_list_shrink):
            query['ContentList'] = request.content_list_shrink
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BatchAddDataForApiSource',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.BatchAddDataForApiSourceResponse(),
            self.call_api(params, req, runtime)
        )

    def batch_add_data_for_api_source(self, request):
        runtime = util_models.RuntimeOptions()
        return self.batch_add_data_for_api_source_with_options(request, runtime)

    def batch_add_device_group_relations_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.device):
            query['Device'] = request.device
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BatchAddDeviceGroupRelations',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.BatchAddDeviceGroupRelationsResponse(),
            self.call_api(params, req, runtime)
        )

    def batch_add_device_group_relations(self, request):
        runtime = util_models.RuntimeOptions()
        return self.batch_add_device_group_relations_with_options(request, runtime)

    def batch_add_thing_topo_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.gw_device_name):
            query['GwDeviceName'] = request.gw_device_name
        if not UtilClient.is_unset(request.gw_product_key):
            query['GwProductKey'] = request.gw_product_key
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.topo_add_item):
            query['TopoAddItem'] = request.topo_add_item
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BatchAddThingTopo',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.BatchAddThingTopoResponse(),
            self.call_api(params, req, runtime)
        )

    def batch_add_thing_topo(self, request):
        runtime = util_models.RuntimeOptions()
        return self.batch_add_thing_topo_with_options(request, runtime)

    def batch_bind_device_to_edge_instance_with_driver_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.driver_id):
            query['DriverId'] = request.driver_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.iot_ids):
            query['IotIds'] = request.iot_ids
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BatchBindDeviceToEdgeInstanceWithDriver',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.BatchBindDeviceToEdgeInstanceWithDriverResponse(),
            self.call_api(params, req, runtime)
        )

    def batch_bind_device_to_edge_instance_with_driver(self, request):
        runtime = util_models.RuntimeOptions()
        return self.batch_bind_device_to_edge_instance_with_driver_with_options(request, runtime)

    def batch_bind_devices_into_project_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.devices):
            body['Devices'] = request.devices
        if not UtilClient.is_unset(request.iot_instance_id):
            body['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='BatchBindDevicesIntoProject',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.BatchBindDevicesIntoProjectResponse(),
            self.call_api(params, req, runtime)
        )

    def batch_bind_devices_into_project(self, request):
        runtime = util_models.RuntimeOptions()
        return self.batch_bind_devices_into_project_with_options(request, runtime)

    def batch_bind_products_into_project_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.iot_instance_id):
            body['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.product_keys):
            body['ProductKeys'] = request.product_keys
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='BatchBindProductsIntoProject',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.BatchBindProductsIntoProjectResponse(),
            self.call_api(params, req, runtime)
        )

    def batch_bind_products_into_project(self, request):
        runtime = util_models.RuntimeOptions()
        return self.batch_bind_products_into_project_with_options(request, runtime)

    def batch_check_device_names_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.device_name):
            query['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.device_name_list):
            query['DeviceNameList'] = request.device_name_list
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BatchCheckDeviceNames',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.BatchCheckDeviceNamesResponse(),
            self.call_api(params, req, runtime)
        )

    def batch_check_device_names(self, request):
        runtime = util_models.RuntimeOptions()
        return self.batch_check_device_names_with_options(request, runtime)

    def batch_check_import_device_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.device_list):
            query['DeviceList'] = request.device_list
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BatchCheckImportDevice',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.BatchCheckImportDeviceResponse(),
            self.call_api(params, req, runtime)
        )

    def batch_check_import_device(self, request):
        runtime = util_models.RuntimeOptions()
        return self.batch_check_import_device_with_options(request, runtime)

    def batch_clear_edge_instance_device_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.iot_ids):
            query['IotIds'] = request.iot_ids
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BatchClearEdgeInstanceDeviceConfig',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.BatchClearEdgeInstanceDeviceConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def batch_clear_edge_instance_device_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.batch_clear_edge_instance_device_config_with_options(request, runtime)

    def batch_create_sound_code_label_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.iot_instance_id):
            body['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.schedule_code):
            body['ScheduleCode'] = request.schedule_code
        if not UtilClient.is_unset(request.total):
            body['Total'] = request.total
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='BatchCreateSoundCodeLabel',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.BatchCreateSoundCodeLabelResponse(),
            self.call_api(params, req, runtime)
        )

    def batch_create_sound_code_label(self, request):
        runtime = util_models.RuntimeOptions()
        return self.batch_create_sound_code_label_with_options(request, runtime)

    def batch_create_sound_code_label_with_labels_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.iot_instance_id):
            body['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.labels):
            body['Labels'] = request.labels
        if not UtilClient.is_unset(request.schedule_code):
            body['ScheduleCode'] = request.schedule_code
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='BatchCreateSoundCodeLabelWithLabels',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.BatchCreateSoundCodeLabelWithLabelsResponse(),
            self.call_api(params, req, runtime)
        )

    def batch_create_sound_code_label_with_labels(self, request):
        runtime = util_models.RuntimeOptions()
        return self.batch_create_sound_code_label_with_labels_with_options(request, runtime)

    def batch_delete_device_group_relations_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.device):
            query['Device'] = request.device
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BatchDeleteDeviceGroupRelations',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.BatchDeleteDeviceGroupRelationsResponse(),
            self.call_api(params, req, runtime)
        )

    def batch_delete_device_group_relations(self, request):
        runtime = util_models.RuntimeOptions()
        return self.batch_delete_device_group_relations_with_options(request, runtime)

    def batch_delete_edge_instance_channel_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.channel_ids):
            query['ChannelIds'] = request.channel_ids
        if not UtilClient.is_unset(request.driver_id):
            query['DriverId'] = request.driver_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BatchDeleteEdgeInstanceChannel',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.BatchDeleteEdgeInstanceChannelResponse(),
            self.call_api(params, req, runtime)
        )

    def batch_delete_edge_instance_channel(self, request):
        runtime = util_models.RuntimeOptions()
        return self.batch_delete_edge_instance_channel_with_options(request, runtime)

    def batch_get_device_bind_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.iot_ids):
            query['IotIds'] = request.iot_ids
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BatchGetDeviceBindStatus',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.BatchGetDeviceBindStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def batch_get_device_bind_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.batch_get_device_bind_status_with_options(request, runtime)

    def batch_get_device_state_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.device_name):
            query['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.iot_id):
            query['IotId'] = request.iot_id
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BatchGetDeviceState',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.BatchGetDeviceStateResponse(),
            self.call_api(params, req, runtime)
        )

    def batch_get_device_state(self, request):
        runtime = util_models.RuntimeOptions()
        return self.batch_get_device_state_with_options(request, runtime)

    def batch_get_edge_driver_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.driver_ids):
            query['DriverIds'] = request.driver_ids
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BatchGetEdgeDriver',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.BatchGetEdgeDriverResponse(),
            self.call_api(params, req, runtime)
        )

    def batch_get_edge_driver(self, request):
        runtime = util_models.RuntimeOptions()
        return self.batch_get_edge_driver_with_options(request, runtime)

    def batch_get_edge_instance_channel_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.channel_ids):
            query['ChannelIds'] = request.channel_ids
        if not UtilClient.is_unset(request.driver_id):
            query['DriverId'] = request.driver_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BatchGetEdgeInstanceChannel',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.BatchGetEdgeInstanceChannelResponse(),
            self.call_api(params, req, runtime)
        )

    def batch_get_edge_instance_channel(self, request):
        runtime = util_models.RuntimeOptions()
        return self.batch_get_edge_instance_channel_with_options(request, runtime)

    def batch_get_edge_instance_device_channel_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.driver_id):
            query['DriverId'] = request.driver_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.iot_ids):
            query['IotIds'] = request.iot_ids
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BatchGetEdgeInstanceDeviceChannel',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.BatchGetEdgeInstanceDeviceChannelResponse(),
            self.call_api(params, req, runtime)
        )

    def batch_get_edge_instance_device_channel(self, request):
        runtime = util_models.RuntimeOptions()
        return self.batch_get_edge_instance_device_channel_with_options(request, runtime)

    def batch_get_edge_instance_device_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.iot_ids):
            query['IotIds'] = request.iot_ids
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BatchGetEdgeInstanceDeviceConfig',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.BatchGetEdgeInstanceDeviceConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def batch_get_edge_instance_device_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.batch_get_edge_instance_device_config_with_options(request, runtime)

    def batch_get_edge_instance_device_driver_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.iot_ids):
            query['IotIds'] = request.iot_ids
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BatchGetEdgeInstanceDeviceDriver',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.BatchGetEdgeInstanceDeviceDriverResponse(),
            self.call_api(params, req, runtime)
        )

    def batch_get_edge_instance_device_driver(self, request):
        runtime = util_models.RuntimeOptions()
        return self.batch_get_edge_instance_device_driver_with_options(request, runtime)

    def batch_get_edge_instance_driver_configs_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.driver_ids):
            query['DriverIds'] = request.driver_ids
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BatchGetEdgeInstanceDriverConfigs',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.BatchGetEdgeInstanceDriverConfigsResponse(),
            self.call_api(params, req, runtime)
        )

    def batch_get_edge_instance_driver_configs(self, request):
        runtime = util_models.RuntimeOptions()
        return self.batch_get_edge_instance_driver_configs_with_options(request, runtime)

    def batch_import_device_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.device_list):
            query['DeviceList'] = request.device_list
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BatchImportDevice',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.BatchImportDeviceResponse(),
            self.call_api(params, req, runtime)
        )

    def batch_import_device(self, request):
        runtime = util_models.RuntimeOptions()
        return self.batch_import_device_with_options(request, runtime)

    def batch_pub_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.device_name):
            query['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.message_content):
            query['MessageContent'] = request.message_content
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        if not UtilClient.is_unset(request.qos):
            query['Qos'] = request.qos
        if not UtilClient.is_unset(request.topic_short_name):
            query['TopicShortName'] = request.topic_short_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BatchPub',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.BatchPubResponse(),
            self.call_api(params, req, runtime)
        )

    def batch_pub(self, request):
        runtime = util_models.RuntimeOptions()
        return self.batch_pub_with_options(request, runtime)

    def batch_query_device_detail_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.device_name):
            query['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BatchQueryDeviceDetail',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.BatchQueryDeviceDetailResponse(),
            self.call_api(params, req, runtime)
        )

    def batch_query_device_detail(self, request):
        runtime = util_models.RuntimeOptions()
        return self.batch_query_device_detail_with_options(request, runtime)

    def batch_register_device_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.count):
            query['Count'] = request.count
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BatchRegisterDevice',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.BatchRegisterDeviceResponse(),
            self.call_api(params, req, runtime)
        )

    def batch_register_device(self, request):
        runtime = util_models.RuntimeOptions()
        return self.batch_register_device_with_options(request, runtime)

    def batch_register_device_with_apply_id_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.apply_id):
            query['ApplyId'] = request.apply_id
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BatchRegisterDeviceWithApplyId',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.BatchRegisterDeviceWithApplyIdResponse(),
            self.call_api(params, req, runtime)
        )

    def batch_register_device_with_apply_id(self, request):
        runtime = util_models.RuntimeOptions()
        return self.batch_register_device_with_apply_id_with_options(request, runtime)

    def batch_set_edge_instance_device_channel_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.driver_id):
            query['DriverId'] = request.driver_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.iot_ids):
            query['IotIds'] = request.iot_ids
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BatchSetEdgeInstanceDeviceChannel',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.BatchSetEdgeInstanceDeviceChannelResponse(),
            self.call_api(params, req, runtime)
        )

    def batch_set_edge_instance_device_channel(self, request):
        runtime = util_models.RuntimeOptions()
        return self.batch_set_edge_instance_device_channel_with_options(request, runtime)

    def batch_set_edge_instance_device_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.device_configs):
            query['DeviceConfigs'] = request.device_configs
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BatchSetEdgeInstanceDeviceConfig',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.BatchSetEdgeInstanceDeviceConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def batch_set_edge_instance_device_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.batch_set_edge_instance_device_config_with_options(request, runtime)

    def batch_unbind_device_from_edge_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.iot_ids):
            query['IotIds'] = request.iot_ids
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BatchUnbindDeviceFromEdgeInstance',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.BatchUnbindDeviceFromEdgeInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    def batch_unbind_device_from_edge_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.batch_unbind_device_from_edge_instance_with_options(request, runtime)

    def batch_unbind_project_devices_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.devices):
            body['Devices'] = request.devices
        if not UtilClient.is_unset(request.iot_instance_id):
            body['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='BatchUnbindProjectDevices',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.BatchUnbindProjectDevicesResponse(),
            self.call_api(params, req, runtime)
        )

    def batch_unbind_project_devices(self, request):
        runtime = util_models.RuntimeOptions()
        return self.batch_unbind_project_devices_with_options(request, runtime)

    def batch_unbind_project_products_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.iot_instance_id):
            body['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.product_keys):
            body['ProductKeys'] = request.product_keys
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='BatchUnbindProjectProducts',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.BatchUnbindProjectProductsResponse(),
            self.call_api(params, req, runtime)
        )

    def batch_unbind_project_products(self, request):
        runtime = util_models.RuntimeOptions()
        return self.batch_unbind_project_products_with_options(request, runtime)

    def batch_update_device_nickname_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.device_nickname_info):
            query['DeviceNicknameInfo'] = request.device_nickname_info
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BatchUpdateDeviceNickname',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.BatchUpdateDeviceNicknameResponse(),
            self.call_api(params, req, runtime)
        )

    def batch_update_device_nickname(self, request):
        runtime = util_models.RuntimeOptions()
        return self.batch_update_device_nickname_with_options(request, runtime)

    def bind_application_to_edge_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_id):
            query['ApplicationId'] = request.application_id
        if not UtilClient.is_unset(request.application_version):
            query['ApplicationVersion'] = request.application_version
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BindApplicationToEdgeInstance',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.BindApplicationToEdgeInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    def bind_application_to_edge_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.bind_application_to_edge_instance_with_options(request, runtime)

    def bind_driver_to_edge_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.driver_id):
            query['DriverId'] = request.driver_id
        if not UtilClient.is_unset(request.driver_version):
            query['DriverVersion'] = request.driver_version
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.order_id):
            query['OrderId'] = request.order_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BindDriverToEdgeInstance',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.BindDriverToEdgeInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    def bind_driver_to_edge_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.bind_driver_to_edge_instance_with_options(request, runtime)

    def bind_gateway_to_edge_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.device_name):
            query['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.iot_id):
            query['IotId'] = request.iot_id
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BindGatewayToEdgeInstance',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.BindGatewayToEdgeInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    def bind_gateway_to_edge_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.bind_gateway_to_edge_instance_with_options(request, runtime)

    def bind_license_device_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.iot_id_list):
            query['IotIdList'] = request.iot_id_list
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.license_code):
            query['LicenseCode'] = request.license_code
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BindLicenseDevice',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.BindLicenseDeviceResponse(),
            self.call_api(params, req, runtime)
        )

    def bind_license_device(self, request):
        runtime = util_models.RuntimeOptions()
        return self.bind_license_device_with_options(request, runtime)

    def bind_license_product_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.license_code):
            query['LicenseCode'] = request.license_code
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BindLicenseProduct',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.BindLicenseProductResponse(),
            self.call_api(params, req, runtime)
        )

    def bind_license_product(self, request):
        runtime = util_models.RuntimeOptions()
        return self.bind_license_product_with_options(request, runtime)

    def bind_role_to_edge_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.role_arn):
            query['RoleArn'] = request.role_arn
        if not UtilClient.is_unset(request.role_name):
            query['RoleName'] = request.role_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BindRoleToEdgeInstance',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.BindRoleToEdgeInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    def bind_role_to_edge_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.bind_role_to_edge_instance_with_options(request, runtime)

    def bind_scene_rule_to_edge_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.rule_id):
            query['RuleId'] = request.rule_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BindSceneRuleToEdgeInstance',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.BindSceneRuleToEdgeInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    def bind_scene_rule_to_edge_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.bind_scene_rule_to_edge_instance_with_options(request, runtime)

    def cancel_job_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CancelJob',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.CancelJobResponse(),
            self.call_api(params, req, runtime)
        )

    def cancel_job(self, request):
        runtime = util_models.RuntimeOptions()
        return self.cancel_job_with_options(request, runtime)

    def cancel_otastrategy_by_job_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CancelOTAStrategyByJob',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.CancelOTAStrategyByJobResponse(),
            self.call_api(params, req, runtime)
        )

    def cancel_otastrategy_by_job(self, request):
        runtime = util_models.RuntimeOptions()
        return self.cancel_otastrategy_by_job_with_options(request, runtime)

    def cancel_otatask_by_device_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.device_name):
            query['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.firmware_id):
            query['FirmwareId'] = request.firmware_id
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CancelOTATaskByDevice',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.CancelOTATaskByDeviceResponse(),
            self.call_api(params, req, runtime)
        )

    def cancel_otatask_by_device(self, request):
        runtime = util_models.RuntimeOptions()
        return self.cancel_otatask_by_device_with_options(request, runtime)

    def cancel_otatask_by_job_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cancel_in_progress_task):
            query['CancelInProgressTask'] = request.cancel_in_progress_task
        if not UtilClient.is_unset(request.cancel_notified_task):
            query['CancelNotifiedTask'] = request.cancel_notified_task
        if not UtilClient.is_unset(request.cancel_queued_task):
            query['CancelQueuedTask'] = request.cancel_queued_task
        if not UtilClient.is_unset(request.cancel_scheduled_task):
            query['CancelScheduledTask'] = request.cancel_scheduled_task
        if not UtilClient.is_unset(request.cancel_unconfirmed_task):
            query['CancelUnconfirmedTask'] = request.cancel_unconfirmed_task
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CancelOTATaskByJob',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.CancelOTATaskByJobResponse(),
            self.call_api(params, req, runtime)
        )

    def cancel_otatask_by_job(self, request):
        runtime = util_models.RuntimeOptions()
        return self.cancel_otatask_by_job_with_options(request, runtime)

    def cancel_release_product_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CancelReleaseProduct',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.CancelReleaseProductResponse(),
            self.call_api(params, req, runtime)
        )

    def cancel_release_product(self, request):
        runtime = util_models.RuntimeOptions()
        return self.cancel_release_product_with_options(request, runtime)

    def check_bind_license_device_progress_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.check_progress_id):
            query['CheckProgressId'] = request.check_progress_id
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.license_code):
            query['LicenseCode'] = request.license_code
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CheckBindLicenseDeviceProgress',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.CheckBindLicenseDeviceProgressResponse(),
            self.call_api(params, req, runtime)
        )

    def check_bind_license_device_progress(self, request):
        runtime = util_models.RuntimeOptions()
        return self.check_bind_license_device_progress_with_options(request, runtime)

    def clear_edge_instance_driver_configs_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.driver_id):
            query['DriverId'] = request.driver_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ClearEdgeInstanceDriverConfigs',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.ClearEdgeInstanceDriverConfigsResponse(),
            self.call_api(params, req, runtime)
        )

    def clear_edge_instance_driver_configs(self, request):
        runtime = util_models.RuntimeOptions()
        return self.clear_edge_instance_driver_configs_with_options(request, runtime)

    def close_device_tunnel_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.tunnel_id):
            query['TunnelId'] = request.tunnel_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CloseDeviceTunnel',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.CloseDeviceTunnelResponse(),
            self.call_api(params, req, runtime)
        )

    def close_device_tunnel(self, request):
        runtime = util_models.RuntimeOptions()
        return self.close_device_tunnel_with_options(request, runtime)

    def close_edge_instance_deployment_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CloseEdgeInstanceDeployment',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.CloseEdgeInstanceDeploymentResponse(),
            self.call_api(params, req, runtime)
        )

    def close_edge_instance_deployment(self, request):
        runtime = util_models.RuntimeOptions()
        return self.close_edge_instance_deployment_with_options(request, runtime)

    def confirm_otatask_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ConfirmOTATask',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.ConfirmOTATaskResponse(),
            self.call_api(params, req, runtime)
        )

    def confirm_otatask(self, request):
        runtime = util_models.RuntimeOptions()
        return self.confirm_otatask_with_options(request, runtime)

    def copy_thing_model_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.source_model_version):
            query['SourceModelVersion'] = request.source_model_version
        if not UtilClient.is_unset(request.source_product_key):
            query['SourceProductKey'] = request.source_product_key
        if not UtilClient.is_unset(request.target_product_key):
            query['TargetProductKey'] = request.target_product_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CopyThingModel',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.CopyThingModelResponse(),
            self.call_api(params, req, runtime)
        )

    def copy_thing_model(self, request):
        runtime = util_models.RuntimeOptions()
        return self.copy_thing_model_with_options(request, runtime)

    def create_consumer_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_name):
            query['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateConsumerGroup',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.CreateConsumerGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def create_consumer_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_consumer_group_with_options(request, runtime)

    def create_consumer_group_subscribe_relation_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.consumer_group_id):
            query['ConsumerGroupId'] = request.consumer_group_id
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateConsumerGroupSubscribeRelation',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.CreateConsumerGroupSubscribeRelationResponse(),
            self.call_api(params, req, runtime)
        )

    def create_consumer_group_subscribe_relation(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_consumer_group_subscribe_relation_with_options(request, runtime)

    def create_data_apiservice_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.api_path):
            body['ApiPath'] = request.api_path
        if not UtilClient.is_unset(request.desc):
            body['Desc'] = request.desc
        if not UtilClient.is_unset(request.display_name):
            body['DisplayName'] = request.display_name
        if not UtilClient.is_unset(request.iot_instance_id):
            body['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.origin_sql):
            body['OriginSql'] = request.origin_sql
        if not UtilClient.is_unset(request.request_param):
            body['RequestParam'] = request.request_param
        if not UtilClient.is_unset(request.response_param):
            body['ResponseParam'] = request.response_param
        if not UtilClient.is_unset(request.template_sql):
            body['TemplateSql'] = request.template_sql
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateDataAPIService',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.CreateDataAPIServiceResponse(),
            self.call_api(params, req, runtime)
        )

    def create_data_apiservice(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_data_apiservice_with_options(request, runtime)

    def create_data_source_item_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.data_source_id):
            query['DataSourceId'] = request.data_source_id
        if not UtilClient.is_unset(request.device_name):
            query['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        if not UtilClient.is_unset(request.scope_type):
            query['ScopeType'] = request.scope_type
        if not UtilClient.is_unset(request.topic):
            query['Topic'] = request.topic
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDataSourceItem',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.CreateDataSourceItemResponse(),
            self.call_api(params, req, runtime)
        )

    def create_data_source_item(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_data_source_item_with_options(request, runtime)

    def create_destination_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.configuration):
            query['Configuration'] = request.configuration
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDestination',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.CreateDestinationResponse(),
            self.call_api(params, req, runtime)
        )

    def create_destination(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_destination_with_options(request, runtime)

    def create_device_distribute_job_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.device_name):
            body['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.product_key):
            body['ProductKey'] = request.product_key
        if not UtilClient.is_unset(request.source_instance_id):
            body['SourceInstanceId'] = request.source_instance_id
        if not UtilClient.is_unset(request.strategy):
            body['Strategy'] = request.strategy
        if not UtilClient.is_unset(request.target_aliyun_id):
            body['TargetAliyunId'] = request.target_aliyun_id
        if not UtilClient.is_unset(request.target_instance_config):
            body['TargetInstanceConfig'] = request.target_instance_config
        if not UtilClient.is_unset(request.target_uid):
            body['TargetUid'] = request.target_uid
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateDeviceDistributeJob',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.CreateDeviceDistributeJobResponse(),
            self.call_api(params, req, runtime)
        )

    def create_device_distribute_job(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_device_distribute_job_with_options(request, runtime)

    def create_device_dynamic_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dynamic_group_expression):
            query['DynamicGroupExpression'] = request.dynamic_group_expression
        if not UtilClient.is_unset(request.group_desc):
            query['GroupDesc'] = request.group_desc
        if not UtilClient.is_unset(request.group_name):
            query['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDeviceDynamicGroup',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.CreateDeviceDynamicGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def create_device_dynamic_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_device_dynamic_group_with_options(request, runtime)

    def create_device_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_desc):
            query['GroupDesc'] = request.group_desc
        if not UtilClient.is_unset(request.group_name):
            query['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.super_group_id):
            query['SuperGroupId'] = request.super_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDeviceGroup',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.CreateDeviceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def create_device_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_device_group_with_options(request, runtime)

    def create_device_tunnel_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.device_name):
            query['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.iot_id):
            query['IotId'] = request.iot_id
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        if not UtilClient.is_unset(request.udi):
            query['Udi'] = request.udi
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDeviceTunnel',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.CreateDeviceTunnelResponse(),
            self.call_api(params, req, runtime)
        )

    def create_device_tunnel(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_device_tunnel_with_options(request, runtime)

    def create_edge_driver_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cpu_arch):
            query['CpuArch'] = request.cpu_arch
        if not UtilClient.is_unset(request.driver_name):
            query['DriverName'] = request.driver_name
        if not UtilClient.is_unset(request.driver_protocol):
            query['DriverProtocol'] = request.driver_protocol
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.is_built_in):
            query['IsBuiltIn'] = request.is_built_in
        if not UtilClient.is_unset(request.runtime):
            query['Runtime'] = request.runtime
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateEdgeDriver',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.CreateEdgeDriverResponse(),
            self.call_api(params, req, runtime)
        )

    def create_edge_driver(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_edge_driver_with_options(request, runtime)

    def create_edge_driver_version_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.argument):
            query['Argument'] = request.argument
        if not UtilClient.is_unset(request.config_check_rule):
            query['ConfigCheckRule'] = request.config_check_rule
        if not UtilClient.is_unset(request.container_config):
            query['ContainerConfig'] = request.container_config
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.driver_config):
            query['DriverConfig'] = request.driver_config
        if not UtilClient.is_unset(request.driver_id):
            query['DriverId'] = request.driver_id
        if not UtilClient.is_unset(request.driver_version):
            query['DriverVersion'] = request.driver_version
        if not UtilClient.is_unset(request.edge_version):
            query['EdgeVersion'] = request.edge_version
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.source_config):
            query['SourceConfig'] = request.source_config
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateEdgeDriverVersion',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.CreateEdgeDriverVersionResponse(),
            self.call_api(params, req, runtime)
        )

    def create_edge_driver_version(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_edge_driver_version_with_options(request, runtime)

    def create_edge_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.spec):
            query['Spec'] = request.spec
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateEdgeInstance',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.CreateEdgeInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    def create_edge_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_edge_instance_with_options(request, runtime)

    def create_edge_instance_channel_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.channel_name):
            query['ChannelName'] = request.channel_name
        if not UtilClient.is_unset(request.configs):
            query['Configs'] = request.configs
        if not UtilClient.is_unset(request.driver_id):
            query['DriverId'] = request.driver_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateEdgeInstanceChannel',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.CreateEdgeInstanceChannelResponse(),
            self.call_api(params, req, runtime)
        )

    def create_edge_instance_channel(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_edge_instance_channel_with_options(request, runtime)

    def create_edge_instance_deployment_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateEdgeInstanceDeployment',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.CreateEdgeInstanceDeploymentResponse(),
            self.call_api(params, req, runtime)
        )

    def create_edge_instance_deployment(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_edge_instance_deployment_with_options(request, runtime)

    def create_edge_instance_message_routing_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.source_data):
            query['SourceData'] = request.source_data
        if not UtilClient.is_unset(request.source_type):
            query['SourceType'] = request.source_type
        if not UtilClient.is_unset(request.target_data):
            query['TargetData'] = request.target_data
        if not UtilClient.is_unset(request.target_iot_hub_qos):
            query['TargetIotHubQos'] = request.target_iot_hub_qos
        if not UtilClient.is_unset(request.target_type):
            query['TargetType'] = request.target_type
        if not UtilClient.is_unset(request.topic_filter):
            query['TopicFilter'] = request.topic_filter
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateEdgeInstanceMessageRouting',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.CreateEdgeInstanceMessageRoutingResponse(),
            self.call_api(params, req, runtime)
        )

    def create_edge_instance_message_routing(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_edge_instance_message_routing_with_options(request, runtime)

    def create_edge_oss_pre_signed_address_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_name):
            query['FileName'] = request.file_name
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_version):
            query['ResourceVersion'] = request.resource_version
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateEdgeOssPreSignedAddress',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.CreateEdgeOssPreSignedAddressResponse(),
            self.call_api(params, req, runtime)
        )

    def create_edge_oss_pre_signed_address(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_edge_oss_pre_signed_address_with_options(request, runtime)

    def create_job_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = iot_20180120_models.CreateJobShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.job_file):
            request.job_file_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.job_file, 'JobFile', 'json')
        if not UtilClient.is_unset(tmp_req.rollout_config):
            request.rollout_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.rollout_config, 'RolloutConfig', 'json')
        if not UtilClient.is_unset(tmp_req.target_config):
            request.target_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.target_config, 'TargetConfig', 'json')
        if not UtilClient.is_unset(tmp_req.timeout_config):
            request.timeout_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.timeout_config, 'TimeoutConfig', 'json')
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.job_document):
            query['JobDocument'] = request.job_document
        if not UtilClient.is_unset(request.job_file_shrink):
            query['JobFile'] = request.job_file_shrink
        if not UtilClient.is_unset(request.job_name):
            query['JobName'] = request.job_name
        if not UtilClient.is_unset(request.rollout_config_shrink):
            query['RolloutConfig'] = request.rollout_config_shrink
        if not UtilClient.is_unset(request.scheduled_time):
            query['ScheduledTime'] = request.scheduled_time
        if not UtilClient.is_unset(request.target_config_shrink):
            query['TargetConfig'] = request.target_config_shrink
        if not UtilClient.is_unset(request.timeout_config_shrink):
            query['TimeoutConfig'] = request.timeout_config_shrink
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateJob',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.CreateJobResponse(),
            self.call_api(params, req, runtime)
        )

    def create_job(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_job_with_options(request, runtime)

    def create_lo_ra_nodes_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.device_info):
            query['DeviceInfo'] = request.device_info
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateLoRaNodesTask',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.CreateLoRaNodesTaskResponse(),
            self.call_api(params, req, runtime)
        )

    def create_lo_ra_nodes_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_lo_ra_nodes_task_with_options(request, runtime)

    def create_otadynamic_upgrade_job_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.download_protocol):
            query['DownloadProtocol'] = request.download_protocol
        if not UtilClient.is_unset(request.dynamic_mode):
            query['DynamicMode'] = request.dynamic_mode
        if not UtilClient.is_unset(request.firmware_id):
            query['FirmwareId'] = request.firmware_id
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.group_type):
            query['GroupType'] = request.group_type
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.maximum_per_minute):
            query['MaximumPerMinute'] = request.maximum_per_minute
        if not UtilClient.is_unset(request.multi_module_mode):
            query['MultiModuleMode'] = request.multi_module_mode
        if not UtilClient.is_unset(request.need_confirm):
            query['NeedConfirm'] = request.need_confirm
        if not UtilClient.is_unset(request.need_push):
            query['NeedPush'] = request.need_push
        if not UtilClient.is_unset(request.overwrite_mode):
            query['OverwriteMode'] = request.overwrite_mode
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        if not UtilClient.is_unset(request.retry_count):
            query['RetryCount'] = request.retry_count
        if not UtilClient.is_unset(request.retry_interval):
            query['RetryInterval'] = request.retry_interval
        if not UtilClient.is_unset(request.src_version):
            query['SrcVersion'] = request.src_version
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.timeout_in_minutes):
            query['TimeoutInMinutes'] = request.timeout_in_minutes
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateOTADynamicUpgradeJob',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.CreateOTADynamicUpgradeJobResponse(),
            self.call_api(params, req, runtime)
        )

    def create_otadynamic_upgrade_job(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_otadynamic_upgrade_job_with_options(request, runtime)

    def create_otafirmware_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dest_version):
            query['DestVersion'] = request.dest_version
        if not UtilClient.is_unset(request.firmware_desc):
            query['FirmwareDesc'] = request.firmware_desc
        if not UtilClient.is_unset(request.firmware_name):
            query['FirmwareName'] = request.firmware_name
        if not UtilClient.is_unset(request.firmware_sign):
            query['FirmwareSign'] = request.firmware_sign
        if not UtilClient.is_unset(request.firmware_size):
            query['FirmwareSize'] = request.firmware_size
        if not UtilClient.is_unset(request.firmware_url):
            query['FirmwareUrl'] = request.firmware_url
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.module_name):
            query['ModuleName'] = request.module_name
        if not UtilClient.is_unset(request.multi_files):
            query['MultiFiles'] = request.multi_files
        if not UtilClient.is_unset(request.need_to_verify):
            query['NeedToVerify'] = request.need_to_verify
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        if not UtilClient.is_unset(request.sign_method):
            query['SignMethod'] = request.sign_method
        if not UtilClient.is_unset(request.src_version):
            query['SrcVersion'] = request.src_version
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        if not UtilClient.is_unset(request.udi):
            query['Udi'] = request.udi
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateOTAFirmware',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.CreateOTAFirmwareResponse(),
            self.call_api(params, req, runtime)
        )

    def create_otafirmware(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_otafirmware_with_options(request, runtime)

    def create_otamodule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alias_name):
            query['AliasName'] = request.alias_name
        if not UtilClient.is_unset(request.desc):
            query['Desc'] = request.desc
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.module_name):
            query['ModuleName'] = request.module_name
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateOTAModule',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.CreateOTAModuleResponse(),
            self.call_api(params, req, runtime)
        )

    def create_otamodule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_otamodule_with_options(request, runtime)

    def create_otastatic_upgrade_job_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dn_list_file_url):
            query['DnListFileUrl'] = request.dn_list_file_url
        if not UtilClient.is_unset(request.download_protocol):
            query['DownloadProtocol'] = request.download_protocol
        if not UtilClient.is_unset(request.firmware_id):
            query['FirmwareId'] = request.firmware_id
        if not UtilClient.is_unset(request.gray_percent):
            query['GrayPercent'] = request.gray_percent
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.group_type):
            query['GroupType'] = request.group_type
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.maximum_per_minute):
            query['MaximumPerMinute'] = request.maximum_per_minute
        if not UtilClient.is_unset(request.multi_module_mode):
            query['MultiModuleMode'] = request.multi_module_mode
        if not UtilClient.is_unset(request.need_confirm):
            query['NeedConfirm'] = request.need_confirm
        if not UtilClient.is_unset(request.need_push):
            query['NeedPush'] = request.need_push
        if not UtilClient.is_unset(request.overwrite_mode):
            query['OverwriteMode'] = request.overwrite_mode
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        if not UtilClient.is_unset(request.retry_count):
            query['RetryCount'] = request.retry_count
        if not UtilClient.is_unset(request.retry_interval):
            query['RetryInterval'] = request.retry_interval
        if not UtilClient.is_unset(request.schedule_finish_time):
            query['ScheduleFinishTime'] = request.schedule_finish_time
        if not UtilClient.is_unset(request.schedule_time):
            query['ScheduleTime'] = request.schedule_time
        if not UtilClient.is_unset(request.src_version):
            query['SrcVersion'] = request.src_version
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.target_device_name):
            query['TargetDeviceName'] = request.target_device_name
        if not UtilClient.is_unset(request.target_selection):
            query['TargetSelection'] = request.target_selection
        if not UtilClient.is_unset(request.timeout_in_minutes):
            query['TimeoutInMinutes'] = request.timeout_in_minutes
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateOTAStaticUpgradeJob',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.CreateOTAStaticUpgradeJobResponse(),
            self.call_api(params, req, runtime)
        )

    def create_otastatic_upgrade_job(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_otastatic_upgrade_job_with_options(request, runtime)

    def create_otaverify_job_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.download_protocol):
            query['DownloadProtocol'] = request.download_protocol
        if not UtilClient.is_unset(request.firmware_id):
            query['FirmwareId'] = request.firmware_id
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.need_confirm):
            query['NeedConfirm'] = request.need_confirm
        if not UtilClient.is_unset(request.need_push):
            query['NeedPush'] = request.need_push
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.target_device_name):
            query['TargetDeviceName'] = request.target_device_name
        if not UtilClient.is_unset(request.timeout_in_minutes):
            query['TimeoutInMinutes'] = request.timeout_in_minutes
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateOTAVerifyJob',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.CreateOTAVerifyJobResponse(),
            self.call_api(params, req, runtime)
        )

    def create_otaverify_job(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_otaverify_job_with_options(request, runtime)

    def create_parser_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateParser',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.CreateParserResponse(),
            self.call_api(params, req, runtime)
        )

    def create_parser(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_parser_with_options(request, runtime)

    def create_parser_data_source_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateParserDataSource',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.CreateParserDataSourceResponse(),
            self.call_api(params, req, runtime)
        )

    def create_parser_data_source(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_parser_data_source_with_options(request, runtime)

    def create_product_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aliyun_commodity_code):
            query['AliyunCommodityCode'] = request.aliyun_commodity_code
        if not UtilClient.is_unset(request.auth_type):
            query['AuthType'] = request.auth_type
        if not UtilClient.is_unset(request.category_key):
            query['CategoryKey'] = request.category_key
        if not UtilClient.is_unset(request.data_format):
            query['DataFormat'] = request.data_format
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.id_2):
            query['Id2'] = request.id_2
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.join_permission_id):
            query['JoinPermissionId'] = request.join_permission_id
        if not UtilClient.is_unset(request.net_type):
            query['NetType'] = request.net_type
        if not UtilClient.is_unset(request.node_type):
            query['NodeType'] = request.node_type
        if not UtilClient.is_unset(request.product_name):
            query['ProductName'] = request.product_name
        if not UtilClient.is_unset(request.protocol_type):
            query['ProtocolType'] = request.protocol_type
        if not UtilClient.is_unset(request.publish_auto):
            query['PublishAuto'] = request.publish_auto
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.validate_type):
            query['ValidateType'] = request.validate_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateProduct',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.CreateProductResponse(),
            self.call_api(params, req, runtime)
        )

    def create_product(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_product_with_options(request, runtime)

    def create_product_distribute_job_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        if not UtilClient.is_unset(request.source_instance_id):
            query['SourceInstanceId'] = request.source_instance_id
        if not UtilClient.is_unset(request.target_aliyun_id):
            query['TargetAliyunId'] = request.target_aliyun_id
        if not UtilClient.is_unset(request.target_instance_id):
            query['TargetInstanceId'] = request.target_instance_id
        if not UtilClient.is_unset(request.target_uid):
            query['TargetUid'] = request.target_uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateProductDistributeJob',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.CreateProductDistributeJobResponse(),
            self.call_api(params, req, runtime)
        )

    def create_product_distribute_job(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_product_distribute_job_with_options(request, runtime)

    def create_product_tags_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        if not UtilClient.is_unset(request.product_tag):
            query['ProductTag'] = request.product_tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateProductTags',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.CreateProductTagsResponse(),
            self.call_api(params, req, runtime)
        )

    def create_product_tags(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_product_tags_with_options(request, runtime)

    def create_product_topic_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.desc):
            query['Desc'] = request.desc
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.operation):
            query['Operation'] = request.operation
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        if not UtilClient.is_unset(request.topic_short_name):
            query['TopicShortName'] = request.topic_short_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateProductTopic',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.CreateProductTopicResponse(),
            self.call_api(params, req, runtime)
        )

    def create_product_topic(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_product_topic_with_options(request, runtime)

    def create_rule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.data_type):
            query['DataType'] = request.data_type
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.rule_desc):
            query['RuleDesc'] = request.rule_desc
        if not UtilClient.is_unset(request.select):
            query['Select'] = request.select
        if not UtilClient.is_unset(request.short_topic):
            query['ShortTopic'] = request.short_topic
        if not UtilClient.is_unset(request.topic):
            query['Topic'] = request.topic
        if not UtilClient.is_unset(request.topic_type):
            query['TopicType'] = request.topic_type
        if not UtilClient.is_unset(request.where):
            query['Where'] = request.where
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateRule',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.CreateRuleResponse(),
            self.call_api(params, req, runtime)
        )

    def create_rule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_rule_with_options(request, runtime)

    def create_rule_action_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.configuration):
            query['Configuration'] = request.configuration
        if not UtilClient.is_unset(request.error_action_flag):
            query['ErrorActionFlag'] = request.error_action_flag
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.rule_id):
            query['RuleId'] = request.rule_id
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateRuleAction',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.CreateRuleActionResponse(),
            self.call_api(params, req, runtime)
        )

    def create_rule_action(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_rule_action_with_options(request, runtime)

    def create_scene_rule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.rule_content):
            query['RuleContent'] = request.rule_content
        if not UtilClient.is_unset(request.rule_description):
            query['RuleDescription'] = request.rule_description
        if not UtilClient.is_unset(request.rule_name):
            query['RuleName'] = request.rule_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateSceneRule',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.CreateSceneRuleResponse(),
            self.call_api(params, req, runtime)
        )

    def create_scene_rule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_scene_rule_with_options(request, runtime)

    def create_schedule_period_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.end_time):
            body['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.iot_instance_id):
            body['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.schedule_code):
            body['ScheduleCode'] = request.schedule_code
        if not UtilClient.is_unset(request.sound_code_content):
            body['SoundCodeContent'] = request.sound_code_content
        if not UtilClient.is_unset(request.start_time):
            body['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateSchedulePeriod',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.CreateSchedulePeriodResponse(),
            self.call_api(params, req, runtime)
        )

    def create_schedule_period(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_schedule_period_with_options(request, runtime)

    def create_sound_code_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.duration):
            body['Duration'] = request.duration
        if not UtilClient.is_unset(request.iot_instance_id):
            body['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.open_type):
            body['OpenType'] = request.open_type
        if not UtilClient.is_unset(request.sound_code_content):
            body['SoundCodeContent'] = request.sound_code_content
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateSoundCode',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.CreateSoundCodeResponse(),
            self.call_api(params, req, runtime)
        )

    def create_sound_code(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_sound_code_with_options(request, runtime)

    def create_sound_code_label_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.iot_instance_id):
            body['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.label):
            body['Label'] = request.label
        if not UtilClient.is_unset(request.schedule_code):
            body['ScheduleCode'] = request.schedule_code
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateSoundCodeLabel',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.CreateSoundCodeLabelResponse(),
            self.call_api(params, req, runtime)
        )

    def create_sound_code_label(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_sound_code_label_with_options(request, runtime)

    def create_sound_code_schedule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.end_date):
            body['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.iot_instance_id):
            body['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.open_type):
            body['OpenType'] = request.open_type
        if not UtilClient.is_unset(request.start_date):
            body['StartDate'] = request.start_date
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateSoundCodeSchedule',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.CreateSoundCodeScheduleResponse(),
            self.call_api(params, req, runtime)
        )

    def create_sound_code_schedule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_sound_code_schedule_with_options(request, runtime)

    def create_speech_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = iot_20180120_models.CreateSpeechShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.sound_code_config):
            request.sound_code_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.sound_code_config, 'SoundCodeConfig', 'json')
        body = {}
        if not UtilClient.is_unset(request.audio_format):
            body['AudioFormat'] = request.audio_format
        if not UtilClient.is_unset(request.biz_code):
            body['BizCode'] = request.biz_code
        if not UtilClient.is_unset(request.enable_sound_code):
            body['EnableSoundCode'] = request.enable_sound_code
        if not UtilClient.is_unset(request.iot_instance_id):
            body['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.project_code):
            body['ProjectCode'] = request.project_code
        if not UtilClient.is_unset(request.sound_code_config_shrink):
            body['SoundCodeConfig'] = request.sound_code_config_shrink
        if not UtilClient.is_unset(request.speech_rate):
            body['SpeechRate'] = request.speech_rate
        if not UtilClient.is_unset(request.speech_type):
            body['SpeechType'] = request.speech_type
        if not UtilClient.is_unset(request.text):
            body['Text'] = request.text
        if not UtilClient.is_unset(request.voice):
            body['Voice'] = request.voice
        if not UtilClient.is_unset(request.volume):
            body['Volume'] = request.volume
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateSpeech',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.CreateSpeechResponse(),
            self.call_api(params, req, runtime)
        )

    def create_speech(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_speech_with_options(request, runtime)

    def create_studio_app_domain_open_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.host):
            body['Host'] = request.host
        if not UtilClient.is_unset(request.iot_instance_id):
            body['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.protocol):
            body['Protocol'] = request.protocol
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateStudioAppDomainOpen',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.CreateStudioAppDomainOpenResponse(),
            self.call_api(params, req, runtime)
        )

    def create_studio_app_domain_open(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_studio_app_domain_open_with_options(request, runtime)

    def create_subscribe_relation_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.consumer_group_ids):
            query['ConsumerGroupIds'] = request.consumer_group_ids
        if not UtilClient.is_unset(request.device_data_flag):
            query['DeviceDataFlag'] = request.device_data_flag
        if not UtilClient.is_unset(request.device_life_cycle_flag):
            query['DeviceLifeCycleFlag'] = request.device_life_cycle_flag
        if not UtilClient.is_unset(request.device_status_change_flag):
            query['DeviceStatusChangeFlag'] = request.device_status_change_flag
        if not UtilClient.is_unset(request.device_tag_flag):
            query['DeviceTagFlag'] = request.device_tag_flag
        if not UtilClient.is_unset(request.device_topo_life_cycle_flag):
            query['DeviceTopoLifeCycleFlag'] = request.device_topo_life_cycle_flag
        if not UtilClient.is_unset(request.found_device_list_flag):
            query['FoundDeviceListFlag'] = request.found_device_list_flag
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.mns_configuration):
            query['MnsConfiguration'] = request.mns_configuration
        if not UtilClient.is_unset(request.ota_event_flag):
            query['OtaEventFlag'] = request.ota_event_flag
        if not UtilClient.is_unset(request.ota_job_flag):
            query['OtaJobFlag'] = request.ota_job_flag
        if not UtilClient.is_unset(request.ota_version_flag):
            query['OtaVersionFlag'] = request.ota_version_flag
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        if not UtilClient.is_unset(request.thing_history_flag):
            query['ThingHistoryFlag'] = request.thing_history_flag
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateSubscribeRelation',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.CreateSubscribeRelationResponse(),
            self.call_api(params, req, runtime)
        )

    def create_subscribe_relation(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_subscribe_relation_with_options(request, runtime)

    def create_thing_model_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.function_block_id):
            query['FunctionBlockId'] = request.function_block_id
        if not UtilClient.is_unset(request.function_block_name):
            query['FunctionBlockName'] = request.function_block_name
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        if not UtilClient.is_unset(request.thing_model_json):
            query['ThingModelJson'] = request.thing_model_json
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateThingModel',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.CreateThingModelResponse(),
            self.call_api(params, req, runtime)
        )

    def create_thing_model(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_thing_model_with_options(request, runtime)

    def create_thing_script_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        if not UtilClient.is_unset(request.script_content):
            query['ScriptContent'] = request.script_content
        if not UtilClient.is_unset(request.script_type):
            query['ScriptType'] = request.script_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateThingScript',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.CreateThingScriptResponse(),
            self.call_api(params, req, runtime)
        )

    def create_thing_script(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_thing_script_with_options(request, runtime)

    def create_topic_route_table_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dst_topic):
            query['DstTopic'] = request.dst_topic
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.src_topic):
            query['SrcTopic'] = request.src_topic
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateTopicRouteTable',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.CreateTopicRouteTableResponse(),
            self.call_api(params, req, runtime)
        )

    def create_topic_route_table(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_topic_route_table_with_options(request, runtime)

    def delete_client_ids_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.iot_id):
            query['IotId'] = request.iot_id
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteClientIds',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.DeleteClientIdsResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_client_ids(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_client_ids_with_options(request, runtime)

    def delete_consumer_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteConsumerGroup',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.DeleteConsumerGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_consumer_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_consumer_group_with_options(request, runtime)

    def delete_consumer_group_subscribe_relation_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.consumer_group_id):
            query['ConsumerGroupId'] = request.consumer_group_id
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteConsumerGroupSubscribeRelation',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.DeleteConsumerGroupSubscribeRelationResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_consumer_group_subscribe_relation(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_consumer_group_subscribe_relation_with_options(request, runtime)

    def delete_data_source_item_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.data_source_id):
            query['DataSourceId'] = request.data_source_id
        if not UtilClient.is_unset(request.data_source_item_id):
            query['DataSourceItemId'] = request.data_source_item_id
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDataSourceItem',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.DeleteDataSourceItemResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_data_source_item(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_data_source_item_with_options(request, runtime)

    def delete_destination_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.destination_id):
            query['DestinationId'] = request.destination_id
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDestination',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.DeleteDestinationResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_destination(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_destination_with_options(request, runtime)

    def delete_device_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.device_name):
            query['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.iot_id):
            query['IotId'] = request.iot_id
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDevice',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.DeleteDeviceResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_device(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_device_with_options(request, runtime)

    def delete_device_distribute_job_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDeviceDistributeJob',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.DeleteDeviceDistributeJobResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_device_distribute_job(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_device_distribute_job_with_options(request, runtime)

    def delete_device_dynamic_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDeviceDynamicGroup',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.DeleteDeviceDynamicGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_device_dynamic_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_device_dynamic_group_with_options(request, runtime)

    def delete_device_file_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.device_name):
            query['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.file_id):
            query['FileId'] = request.file_id
        if not UtilClient.is_unset(request.iot_id):
            query['IotId'] = request.iot_id
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDeviceFile',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.DeleteDeviceFileResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_device_file(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_device_file_with_options(request, runtime)

    def delete_device_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDeviceGroup',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.DeleteDeviceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_device_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_device_group_with_options(request, runtime)

    def delete_device_prop_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.device_name):
            query['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.iot_id):
            query['IotId'] = request.iot_id
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        if not UtilClient.is_unset(request.prop_key):
            query['PropKey'] = request.prop_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDeviceProp',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.DeleteDevicePropResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_device_prop(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_device_prop_with_options(request, runtime)

    def delete_device_speech_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.device_speech_list):
            body['DeviceSpeechList'] = request.device_speech_list
        if not UtilClient.is_unset(request.iot_id):
            body['IotId'] = request.iot_id
        if not UtilClient.is_unset(request.iot_instance_id):
            body['IotInstanceId'] = request.iot_instance_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteDeviceSpeech',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.DeleteDeviceSpeechResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_device_speech(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_device_speech_with_options(request, runtime)

    def delete_device_tunnel_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.tunnel_id):
            query['TunnelId'] = request.tunnel_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDeviceTunnel',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.DeleteDeviceTunnelResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_device_tunnel(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_device_tunnel_with_options(request, runtime)

    def delete_edge_driver_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.driver_id):
            query['DriverId'] = request.driver_id
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteEdgeDriver',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.DeleteEdgeDriverResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_edge_driver(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_edge_driver_with_options(request, runtime)

    def delete_edge_driver_version_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.driver_id):
            query['DriverId'] = request.driver_id
        if not UtilClient.is_unset(request.driver_version):
            query['DriverVersion'] = request.driver_version
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteEdgeDriverVersion',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.DeleteEdgeDriverVersionResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_edge_driver_version(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_edge_driver_version_with_options(request, runtime)

    def delete_edge_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteEdgeInstance',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.DeleteEdgeInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_edge_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_edge_instance_with_options(request, runtime)

    def delete_edge_instance_message_routing_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.route_id):
            query['RouteId'] = request.route_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteEdgeInstanceMessageRouting',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.DeleteEdgeInstanceMessageRoutingResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_edge_instance_message_routing(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_edge_instance_message_routing_with_options(request, runtime)

    def delete_job_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteJob',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.DeleteJobResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_job(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_job_with_options(request, runtime)

    def delete_otafirmware_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.firmware_id):
            query['FirmwareId'] = request.firmware_id
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteOTAFirmware',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.DeleteOTAFirmwareResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_otafirmware(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_otafirmware_with_options(request, runtime)

    def delete_otamodule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.module_name):
            query['ModuleName'] = request.module_name
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteOTAModule',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.DeleteOTAModuleResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_otamodule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_otamodule_with_options(request, runtime)

    def delete_parser_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.parser_id):
            query['ParserId'] = request.parser_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteParser',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.DeleteParserResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_parser(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_parser_with_options(request, runtime)

    def delete_parser_data_source_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.data_source_id):
            query['DataSourceId'] = request.data_source_id
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteParserDataSource',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.DeleteParserDataSourceResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_parser_data_source(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_parser_data_source_with_options(request, runtime)

    def delete_product_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteProduct',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.DeleteProductResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_product(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_product_with_options(request, runtime)

    def delete_product_tags_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        if not UtilClient.is_unset(request.product_tag_key):
            query['ProductTagKey'] = request.product_tag_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteProductTags',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.DeleteProductTagsResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_product_tags(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_product_tags_with_options(request, runtime)

    def delete_product_topic_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.topic_id):
            query['TopicId'] = request.topic_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteProductTopic',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.DeleteProductTopicResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_product_topic(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_product_topic_with_options(request, runtime)

    def delete_rule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.rule_id):
            query['RuleId'] = request.rule_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteRule',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.DeleteRuleResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_rule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_rule_with_options(request, runtime)

    def delete_rule_action_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.action_id):
            query['ActionId'] = request.action_id
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteRuleAction',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.DeleteRuleActionResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_rule_action(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_rule_action_with_options(request, runtime)

    def delete_scene_rule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.rule_id):
            query['RuleId'] = request.rule_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteSceneRule',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.DeleteSceneRuleResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_scene_rule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_scene_rule_with_options(request, runtime)

    def delete_schedule_period_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.iot_instance_id):
            body['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.period_code):
            body['PeriodCode'] = request.period_code
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteSchedulePeriod',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.DeleteSchedulePeriodResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_schedule_period(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_schedule_period_with_options(request, runtime)

    def delete_sound_code_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.iot_instance_id):
            body['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.sound_code):
            body['SoundCode'] = request.sound_code
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteSoundCode',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.DeleteSoundCodeResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_sound_code(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_sound_code_with_options(request, runtime)

    def delete_sound_code_label_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.iot_instance_id):
            body['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.sound_code):
            body['SoundCode'] = request.sound_code
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteSoundCodeLabel',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.DeleteSoundCodeLabelResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_sound_code_label(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_sound_code_label_with_options(request, runtime)

    def delete_sound_code_schedule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.iot_instance_id):
            body['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.schedule_code):
            body['ScheduleCode'] = request.schedule_code
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteSoundCodeSchedule',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.DeleteSoundCodeScheduleResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_sound_code_schedule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_sound_code_schedule_with_options(request, runtime)

    def delete_speech_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.iot_instance_id):
            body['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.speech_code_list):
            body['SpeechCodeList'] = request.speech_code_list
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteSpeech',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.DeleteSpeechResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_speech(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_speech_with_options(request, runtime)

    def delete_studio_app_domain_open_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.domain_id):
            body['DomainId'] = request.domain_id
        if not UtilClient.is_unset(request.iot_instance_id):
            body['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteStudioAppDomainOpen',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.DeleteStudioAppDomainOpenResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_studio_app_domain_open(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_studio_app_domain_open_with_options(request, runtime)

    def delete_subscribe_relation_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteSubscribeRelation',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.DeleteSubscribeRelationResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_subscribe_relation(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_subscribe_relation_with_options(request, runtime)

    def delete_thing_model_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.event_identifier):
            query['EventIdentifier'] = request.event_identifier
        if not UtilClient.is_unset(request.function_block_id):
            query['FunctionBlockId'] = request.function_block_id
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        if not UtilClient.is_unset(request.property_identifier):
            query['PropertyIdentifier'] = request.property_identifier
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.service_identifier):
            query['ServiceIdentifier'] = request.service_identifier
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteThingModel',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.DeleteThingModelResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_thing_model(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_thing_model_with_options(request, runtime)

    def delete_topic_route_table_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dst_topic):
            query['DstTopic'] = request.dst_topic
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.src_topic):
            query['SrcTopic'] = request.src_topic
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteTopicRouteTable',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.DeleteTopicRouteTableResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_topic_route_table(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_topic_route_table_with_options(request, runtime)

    def detach_destination_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.destination_id):
            query['DestinationId'] = request.destination_id
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.parser_id):
            query['ParserId'] = request.parser_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DetachDestination',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.DetachDestinationResponse(),
            self.call_api(params, req, runtime)
        )

    def detach_destination(self, request):
        runtime = util_models.RuntimeOptions()
        return self.detach_destination_with_options(request, runtime)

    def detach_parser_data_source_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.data_source_id):
            query['DataSourceId'] = request.data_source_id
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.parser_id):
            query['ParserId'] = request.parser_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DetachParserDataSource',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.DetachParserDataSourceResponse(),
            self.call_api(params, req, runtime)
        )

    def detach_parser_data_source(self, request):
        runtime = util_models.RuntimeOptions()
        return self.detach_parser_data_source_with_options(request, runtime)

    def disable_device_tunnel_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.device_name):
            query['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DisableDeviceTunnel',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.DisableDeviceTunnelResponse(),
            self.call_api(params, req, runtime)
        )

    def disable_device_tunnel(self, request):
        runtime = util_models.RuntimeOptions()
        return self.disable_device_tunnel_with_options(request, runtime)

    def disable_device_tunnel_share_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.device_name):
            query['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DisableDeviceTunnelShare',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.DisableDeviceTunnelShareResponse(),
            self.call_api(params, req, runtime)
        )

    def disable_device_tunnel_share(self, request):
        runtime = util_models.RuntimeOptions()
        return self.disable_device_tunnel_share_with_options(request, runtime)

    def disable_scene_rule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.rule_id):
            query['RuleId'] = request.rule_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DisableSceneRule',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.DisableSceneRuleResponse(),
            self.call_api(params, req, runtime)
        )

    def disable_scene_rule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.disable_scene_rule_with_options(request, runtime)

    def disable_thing_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.device_name):
            query['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.iot_id):
            query['IotId'] = request.iot_id
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DisableThing',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.DisableThingResponse(),
            self.call_api(params, req, runtime)
        )

    def disable_thing(self, request):
        runtime = util_models.RuntimeOptions()
        return self.disable_thing_with_options(request, runtime)

    def enable_device_tunnel_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.device_name):
            query['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnableDeviceTunnel',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.EnableDeviceTunnelResponse(),
            self.call_api(params, req, runtime)
        )

    def enable_device_tunnel(self, request):
        runtime = util_models.RuntimeOptions()
        return self.enable_device_tunnel_with_options(request, runtime)

    def enable_device_tunnel_share_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.device_name):
            query['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnableDeviceTunnelShare',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.EnableDeviceTunnelShareResponse(),
            self.call_api(params, req, runtime)
        )

    def enable_device_tunnel_share(self, request):
        runtime = util_models.RuntimeOptions()
        return self.enable_device_tunnel_share_with_options(request, runtime)

    def enable_scene_rule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.rule_id):
            query['RuleId'] = request.rule_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnableSceneRule',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.EnableSceneRuleResponse(),
            self.call_api(params, req, runtime)
        )

    def enable_scene_rule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.enable_scene_rule_with_options(request, runtime)

    def enable_thing_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.device_name):
            query['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.iot_id):
            query['IotId'] = request.iot_id
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnableThing',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.EnableThingResponse(),
            self.call_api(params, req, runtime)
        )

    def enable_thing(self, request):
        runtime = util_models.RuntimeOptions()
        return self.enable_thing_with_options(request, runtime)

    def generate_device_name_list_urlwith_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GenerateDeviceNameListURL',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.GenerateDeviceNameListURLResponse(),
            self.call_api(params, req, runtime)
        )

    def generate_device_name_list_url(self, request):
        runtime = util_models.RuntimeOptions()
        return self.generate_device_name_list_urlwith_options(request, runtime)

    def generate_file_upload_urlwith_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_code):
            query['BizCode'] = request.biz_code
        if not UtilClient.is_unset(request.file_name):
            query['FileName'] = request.file_name
        if not UtilClient.is_unset(request.file_suffix):
            query['FileSuffix'] = request.file_suffix
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GenerateFileUploadURL',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.GenerateFileUploadURLResponse(),
            self.call_api(params, req, runtime)
        )

    def generate_file_upload_url(self, request):
        runtime = util_models.RuntimeOptions()
        return self.generate_file_upload_urlwith_options(request, runtime)

    def generate_otaupload_urlwith_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.file_suffix):
            query['FileSuffix'] = request.file_suffix
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GenerateOTAUploadURL',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.GenerateOTAUploadURLResponse(),
            self.call_api(params, req, runtime)
        )

    def generate_otaupload_url(self, request):
        runtime = util_models.RuntimeOptions()
        return self.generate_otaupload_urlwith_options(request, runtime)

    def get_data_apiservice_detail_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.api_srn):
            body['ApiSrn'] = request.api_srn
        if not UtilClient.is_unset(request.iot_instance_id):
            body['IotInstanceId'] = request.iot_instance_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetDataAPIServiceDetail',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.GetDataAPIServiceDetailResponse(),
            self.call_api(params, req, runtime)
        )

    def get_data_apiservice_detail(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_data_apiservice_detail_with_options(request, runtime)

    def get_destination_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.destination_id):
            query['DestinationId'] = request.destination_id
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDestination',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.GetDestinationResponse(),
            self.call_api(params, req, runtime)
        )

    def get_destination(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_destination_with_options(request, runtime)

    def get_device_shadow_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.device_name):
            query['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDeviceShadow',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.GetDeviceShadowResponse(),
            self.call_api(params, req, runtime)
        )

    def get_device_shadow(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_device_shadow_with_options(request, runtime)

    def get_device_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.device_name):
            query['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.iot_id):
            query['IotId'] = request.iot_id
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDeviceStatus',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.GetDeviceStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def get_device_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_device_status_with_options(request, runtime)

    def get_device_tunnel_share_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.device_name):
            query['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDeviceTunnelShareStatus',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.GetDeviceTunnelShareStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def get_device_tunnel_share_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_device_tunnel_share_status_with_options(request, runtime)

    def get_device_tunnel_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.device_name):
            query['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDeviceTunnelStatus',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.GetDeviceTunnelStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def get_device_tunnel_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_device_tunnel_status_with_options(request, runtime)

    def get_edge_driver_version_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.driver_id):
            query['DriverId'] = request.driver_id
        if not UtilClient.is_unset(request.driver_version):
            query['DriverVersion'] = request.driver_version
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetEdgeDriverVersion',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.GetEdgeDriverVersionResponse(),
            self.call_api(params, req, runtime)
        )

    def get_edge_driver_version(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_edge_driver_version_with_options(request, runtime)

    def get_edge_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetEdgeInstance',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.GetEdgeInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    def get_edge_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_edge_instance_with_options(request, runtime)

    def get_edge_instance_deployment_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.deployment_id):
            query['DeploymentId'] = request.deployment_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetEdgeInstanceDeployment',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.GetEdgeInstanceDeploymentResponse(),
            self.call_api(params, req, runtime)
        )

    def get_edge_instance_deployment(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_edge_instance_deployment_with_options(request, runtime)

    def get_edge_instance_message_routing_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.route_id):
            query['RouteId'] = request.route_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetEdgeInstanceMessageRouting',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.GetEdgeInstanceMessageRoutingResponse(),
            self.call_api(params, req, runtime)
        )

    def get_edge_instance_message_routing(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_edge_instance_message_routing_with_options(request, runtime)

    def get_gateway_by_sub_device_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.device_name):
            query['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.iot_id):
            query['IotId'] = request.iot_id
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetGatewayBySubDevice',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.GetGatewayBySubDeviceResponse(),
            self.call_api(params, req, runtime)
        )

    def get_gateway_by_sub_device(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_gateway_by_sub_device_with_options(request, runtime)

    def get_lora_nodes_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetLoraNodesTask',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.GetLoraNodesTaskResponse(),
            self.call_api(params, req, runtime)
        )

    def get_lora_nodes_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_lora_nodes_task_with_options(request, runtime)

    def get_parser_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.parser_id):
            query['ParserId'] = request.parser_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetParser',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.GetParserResponse(),
            self.call_api(params, req, runtime)
        )

    def get_parser(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_parser_with_options(request, runtime)

    def get_parser_data_source_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.data_source_id):
            query['DataSourceId'] = request.data_source_id
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetParserDataSource',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.GetParserDataSourceResponse(),
            self.call_api(params, req, runtime)
        )

    def get_parser_data_source(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_parser_data_source_with_options(request, runtime)

    def get_rule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.rule_id):
            query['RuleId'] = request.rule_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetRule',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.GetRuleResponse(),
            self.call_api(params, req, runtime)
        )

    def get_rule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_rule_with_options(request, runtime)

    def get_rule_action_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.action_id):
            query['ActionId'] = request.action_id
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetRuleAction',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.GetRuleActionResponse(),
            self.call_api(params, req, runtime)
        )

    def get_rule_action(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_rule_action_with_options(request, runtime)

    def get_scene_rule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.rule_id):
            query['RuleId'] = request.rule_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSceneRule',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.GetSceneRuleResponse(),
            self.call_api(params, req, runtime)
        )

    def get_scene_rule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_scene_rule_with_options(request, runtime)

    def get_sound_code_audio_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.iot_instance_id):
            body['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.sound_code_list):
            body['SoundCodeList'] = request.sound_code_list
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetSoundCodeAudio',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.GetSoundCodeAudioResponse(),
            self.call_api(params, req, runtime)
        )

    def get_sound_code_audio(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_sound_code_audio_with_options(request, runtime)

    def get_sound_code_schedule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.iot_instance_id):
            body['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.schedule_code):
            body['ScheduleCode'] = request.schedule_code
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetSoundCodeSchedule',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.GetSoundCodeScheduleResponse(),
            self.call_api(params, req, runtime)
        )

    def get_sound_code_schedule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_sound_code_schedule_with_options(request, runtime)

    def get_speech_device_detail_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.iot_id):
            body['IotId'] = request.iot_id
        if not UtilClient.is_unset(request.iot_instance_id):
            body['IotInstanceId'] = request.iot_instance_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetSpeechDeviceDetail',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.GetSpeechDeviceDetailResponse(),
            self.call_api(params, req, runtime)
        )

    def get_speech_device_detail(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_speech_device_detail_with_options(request, runtime)

    def get_speech_voice_with_options(self, runtime):
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='GetSpeechVoice',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.GetSpeechVoiceResponse(),
            self.call_api(params, req, runtime)
        )

    def get_speech_voice(self):
        runtime = util_models.RuntimeOptions()
        return self.get_speech_voice_with_options(runtime)

    def get_studio_app_token_open_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.iot_instance_id):
            body['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetStudioAppTokenOpen',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.GetStudioAppTokenOpenResponse(),
            self.call_api(params, req, runtime)
        )

    def get_studio_app_token_open(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_studio_app_token_open_with_options(request, runtime)

    def get_thing_model_tsl_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.function_block_id):
            query['FunctionBlockId'] = request.function_block_id
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.model_version):
            query['ModelVersion'] = request.model_version
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        if not UtilClient.is_unset(request.simple):
            query['Simple'] = request.simple
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetThingModelTsl',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.GetThingModelTslResponse(),
            self.call_api(params, req, runtime)
        )

    def get_thing_model_tsl(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_thing_model_tsl_with_options(request, runtime)

    def get_thing_model_tsl_published_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.function_block_id):
            query['FunctionBlockId'] = request.function_block_id
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.model_version):
            query['ModelVersion'] = request.model_version
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.simple):
            query['Simple'] = request.simple
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetThingModelTslPublished',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.GetThingModelTslPublishedResponse(),
            self.call_api(params, req, runtime)
        )

    def get_thing_model_tsl_published(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_thing_model_tsl_published_with_options(request, runtime)

    def get_thing_script_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetThingScript',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.GetThingScriptResponse(),
            self.call_api(params, req, runtime)
        )

    def get_thing_script(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_thing_script_with_options(request, runtime)

    def get_thing_template_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.category_key):
            query['CategoryKey'] = request.category_key
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetThingTemplate',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.GetThingTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    def get_thing_template(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_thing_template_with_options(request, runtime)

    def get_thing_topo_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.device_name):
            query['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.iot_id):
            query['IotId'] = request.iot_id
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetThingTopo',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.GetThingTopoResponse(),
            self.call_api(params, req, runtime)
        )

    def get_thing_topo(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_thing_topo_with_options(request, runtime)

    def gis_query_device_location_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.thing_list):
            query['ThingList'] = request.thing_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GisQueryDeviceLocation',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.GisQueryDeviceLocationResponse(),
            self.call_api(params, req, runtime)
        )

    def gis_query_device_location(self, request):
        runtime = util_models.RuntimeOptions()
        return self.gis_query_device_location_with_options(request, runtime)

    def gis_search_device_trace_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.device_name):
            query['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.map_match):
            query['MapMatch'] = request.map_match
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GisSearchDeviceTrace',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.GisSearchDeviceTraceResponse(),
            self.call_api(params, req, runtime)
        )

    def gis_search_device_trace(self, request):
        runtime = util_models.RuntimeOptions()
        return self.gis_search_device_trace_with_options(request, runtime)

    def import_device_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.device_name):
            query['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.device_secret):
            query['DeviceSecret'] = request.device_secret
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.nickname):
            query['Nickname'] = request.nickname
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        if not UtilClient.is_unset(request.sn):
            query['Sn'] = request.sn
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ImportDevice',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.ImportDeviceResponse(),
            self.call_api(params, req, runtime)
        )

    def import_device(self, request):
        runtime = util_models.RuntimeOptions()
        return self.import_device_with_options(request, runtime)

    def import_thing_model_tsl_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.function_block_id):
            query['FunctionBlockId'] = request.function_block_id
        if not UtilClient.is_unset(request.function_block_name):
            query['FunctionBlockName'] = request.function_block_name
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.tsl_str):
            query['TslStr'] = request.tsl_str
        if not UtilClient.is_unset(request.tsl_url):
            query['TslUrl'] = request.tsl_url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ImportThingModelTsl',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.ImportThingModelTslResponse(),
            self.call_api(params, req, runtime)
        )

    def import_thing_model_tsl(self, request):
        runtime = util_models.RuntimeOptions()
        return self.import_thing_model_tsl_with_options(request, runtime)

    def invoke_data_apiservice_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.api_srn):
            body['ApiSrn'] = request.api_srn
        if not UtilClient.is_unset(request.iot_instance_id):
            body['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.param):
            body['Param'] = request.param
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='InvokeDataAPIService',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.InvokeDataAPIServiceResponse(),
            self.call_api(params, req, runtime)
        )

    def invoke_data_apiservice(self, request):
        runtime = util_models.RuntimeOptions()
        return self.invoke_data_apiservice_with_options(request, runtime)

    def invoke_thing_service_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.args):
            query['Args'] = request.args
        if not UtilClient.is_unset(request.device_name):
            query['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.identifier):
            query['Identifier'] = request.identifier
        if not UtilClient.is_unset(request.iot_id):
            query['IotId'] = request.iot_id
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='InvokeThingService',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.InvokeThingServiceResponse(),
            self.call_api(params, req, runtime)
        )

    def invoke_thing_service(self, request):
        runtime = util_models.RuntimeOptions()
        return self.invoke_thing_service_with_options(request, runtime)

    def invoke_things_service_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.args):
            query['Args'] = request.args
        if not UtilClient.is_unset(request.device_name):
            query['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.identifier):
            query['Identifier'] = request.identifier
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='InvokeThingsService',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.InvokeThingsServiceResponse(),
            self.call_api(params, req, runtime)
        )

    def invoke_things_service(self, request):
        runtime = util_models.RuntimeOptions()
        return self.invoke_things_service_with_options(request, runtime)

    def list_analytics_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.api_path):
            query['ApiPath'] = request.api_path
        if not UtilClient.is_unset(request.condition):
            query['Condition'] = request.condition
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.iso_id):
            query['IsoId'] = request.iso_id
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAnalyticsData',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.ListAnalyticsDataResponse(),
            self.call_api(params, req, runtime)
        )

    def list_analytics_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_analytics_data_with_options(request, runtime)

    def list_data_source_item_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.data_source_id):
            query['DataSourceId'] = request.data_source_id
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.page):
            query['Page'] = request.page
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search_name):
            query['SearchName'] = request.search_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDataSourceItem',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.ListDataSourceItemResponse(),
            self.call_api(params, req, runtime)
        )

    def list_data_source_item(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_data_source_item_with_options(request, runtime)

    def list_destination_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.page):
            query['Page'] = request.page
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search_name):
            query['SearchName'] = request.search_name
        if not UtilClient.is_unset(request.types):
            query['Types'] = request.types
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDestination',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.ListDestinationResponse(),
            self.call_api(params, req, runtime)
        )

    def list_destination(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_destination_with_options(request, runtime)

    def list_device_distribute_job_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.target_uid):
            query['TargetUid'] = request.target_uid
        body = {}
        if not UtilClient.is_unset(request.job_id):
            body['JobId'] = request.job_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListDeviceDistributeJob',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.ListDeviceDistributeJobResponse(),
            self.call_api(params, req, runtime)
        )

    def list_device_distribute_job(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_device_distribute_job_with_options(request, runtime)

    def list_distributed_device_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.device_name):
            query['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        if not UtilClient.is_unset(request.source_instance_id):
            query['SourceInstanceId'] = request.source_instance_id
        if not UtilClient.is_unset(request.target_uid):
            query['TargetUid'] = request.target_uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDistributedDevice',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.ListDistributedDeviceResponse(),
            self.call_api(params, req, runtime)
        )

    def list_distributed_device(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_distributed_device_with_options(request, runtime)

    def list_distributed_product_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        if not UtilClient.is_unset(request.source_instance_id):
            query['SourceInstanceId'] = request.source_instance_id
        if not UtilClient.is_unset(request.target_instance_id):
            query['TargetInstanceId'] = request.target_instance_id
        if not UtilClient.is_unset(request.target_uid):
            query['TargetUid'] = request.target_uid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDistributedProduct',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.ListDistributedProductResponse(),
            self.call_api(params, req, runtime)
        )

    def list_distributed_product(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_distributed_product_with_options(request, runtime)

    def list_job_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListJob',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.ListJobResponse(),
            self.call_api(params, req, runtime)
        )

    def list_job(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_job_with_options(request, runtime)

    def list_otafirmware_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.dest_version):
            query['DestVersion'] = request.dest_version
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListOTAFirmware',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.ListOTAFirmwareResponse(),
            self.call_api(params, req, runtime)
        )

    def list_otafirmware(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_otafirmware_with_options(request, runtime)

    def list_otajob_by_device_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.device_name):
            query['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.firmware_id):
            query['FirmwareId'] = request.firmware_id
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListOTAJobByDevice',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.ListOTAJobByDeviceResponse(),
            self.call_api(params, req, runtime)
        )

    def list_otajob_by_device(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_otajob_by_device_with_options(request, runtime)

    def list_otajob_by_firmware_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.firmware_id):
            query['FirmwareId'] = request.firmware_id
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListOTAJobByFirmware',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.ListOTAJobByFirmwareResponse(),
            self.call_api(params, req, runtime)
        )

    def list_otajob_by_firmware(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_otajob_by_firmware_with_options(request, runtime)

    def list_otamodule_by_product_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListOTAModuleByProduct',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.ListOTAModuleByProductResponse(),
            self.call_api(params, req, runtime)
        )

    def list_otamodule_by_product(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_otamodule_by_product_with_options(request, runtime)

    def list_otamodule_versions_by_device_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.device_name):
            query['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.iot_id):
            query['IotId'] = request.iot_id
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListOTAModuleVersionsByDevice',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.ListOTAModuleVersionsByDeviceResponse(),
            self.call_api(params, req, runtime)
        )

    def list_otamodule_versions_by_device(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_otamodule_versions_by_device_with_options(request, runtime)

    def list_otatask_by_job_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.device_names):
            query['DeviceNames'] = request.device_names
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.task_status):
            query['TaskStatus'] = request.task_status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListOTATaskByJob',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.ListOTATaskByJobResponse(),
            self.call_api(params, req, runtime)
        )

    def list_otatask_by_job(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_otatask_by_job_with_options(request, runtime)

    def list_otaunfinished_task_by_device_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.device_name):
            query['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.iot_id):
            query['IotId'] = request.iot_id
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.module_name):
            query['ModuleName'] = request.module_name
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        if not UtilClient.is_unset(request.task_status):
            query['TaskStatus'] = request.task_status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListOTAUnfinishedTaskByDevice',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.ListOTAUnfinishedTaskByDeviceResponse(),
            self.call_api(params, req, runtime)
        )

    def list_otaunfinished_task_by_device(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_otaunfinished_task_by_device_with_options(request, runtime)

    def list_parser_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search_name):
            query['SearchName'] = request.search_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListParser',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.ListParserResponse(),
            self.call_api(params, req, runtime)
        )

    def list_parser(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_parser_with_options(request, runtime)

    def list_parser_data_source_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.page):
            query['Page'] = request.page
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.search_name):
            query['SearchName'] = request.search_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListParserDataSource',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.ListParserDataSourceResponse(),
            self.call_api(params, req, runtime)
        )

    def list_parser_data_source(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_parser_data_source_with_options(request, runtime)

    def list_parser_destination_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.is_failover):
            query['IsFailover'] = request.is_failover
        if not UtilClient.is_unset(request.parser_id):
            query['ParserId'] = request.parser_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListParserDestination',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.ListParserDestinationResponse(),
            self.call_api(params, req, runtime)
        )

    def list_parser_destination(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_parser_destination_with_options(request, runtime)

    def list_product_by_tags_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.product_tag):
            query['ProductTag'] = request.product_tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListProductByTags',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.ListProductByTagsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_product_by_tags(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_product_by_tags_with_options(request, runtime)

    def list_product_tags_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListProductTags',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.ListProductTagsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_product_tags(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_product_tags_with_options(request, runtime)

    def list_rule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListRule',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.ListRuleResponse(),
            self.call_api(params, req, runtime)
        )

    def list_rule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_rule_with_options(request, runtime)

    def list_rule_actions_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.rule_id):
            query['RuleId'] = request.rule_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListRuleActions',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.ListRuleActionsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_rule_actions(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_rule_actions_with_options(request, runtime)

    def list_task_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = iot_20180120_models.ListTaskShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.device):
            request.device_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.device, 'Device', 'json')
        query = {}
        if not UtilClient.is_unset(request.device_shrink):
            query['Device'] = request.device_shrink
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        if not UtilClient.is_unset(request.limit):
            query['Limit'] = request.limit
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTask',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.ListTaskResponse(),
            self.call_api(params, req, runtime)
        )

    def list_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_task_with_options(request, runtime)

    def list_thing_model_version_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListThingModelVersion',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.ListThingModelVersionResponse(),
            self.call_api(params, req, runtime)
        )

    def list_thing_model_version(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_thing_model_version_with_options(request, runtime)

    def list_thing_templates_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListThingTemplates',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.ListThingTemplatesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_thing_templates(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_thing_templates_with_options(request, runtime)

    def notify_add_thing_topo_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.device_list_str):
            query['DeviceListStr'] = request.device_list_str
        if not UtilClient.is_unset(request.gw_device_name):
            query['GwDeviceName'] = request.gw_device_name
        if not UtilClient.is_unset(request.gw_iot_id):
            query['GwIotId'] = request.gw_iot_id
        if not UtilClient.is_unset(request.gw_product_key):
            query['GwProductKey'] = request.gw_product_key
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='NotifyAddThingTopo',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.NotifyAddThingTopoResponse(),
            self.call_api(params, req, runtime)
        )

    def notify_add_thing_topo(self, request):
        runtime = util_models.RuntimeOptions()
        return self.notify_add_thing_topo_with_options(request, runtime)

    def open_iot_service_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='OpenIotService',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.OpenIotServiceResponse(),
            self.call_api(params, req, runtime)
        )

    def open_iot_service(self, request):
        runtime = util_models.RuntimeOptions()
        return self.open_iot_service_with_options(request, runtime)

    def package_sound_code_label_batch_audio_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.batch_code):
            body['BatchCode'] = request.batch_code
        if not UtilClient.is_unset(request.iot_instance_id):
            body['IotInstanceId'] = request.iot_instance_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PackageSoundCodeLabelBatchAudio',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.PackageSoundCodeLabelBatchAudioResponse(),
            self.call_api(params, req, runtime)
        )

    def package_sound_code_label_batch_audio(self, request):
        runtime = util_models.RuntimeOptions()
        return self.package_sound_code_label_batch_audio_with_options(request, runtime)

    def print_by_template_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.device_name):
            body['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.history_print_topic):
            body['HistoryPrintTopic'] = request.history_print_topic
        if not UtilClient.is_unset(request.iot_id):
            body['IotId'] = request.iot_id
        if not UtilClient.is_unset(request.iot_instance_id):
            body['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.params_json_string):
            body['ParamsJsonString'] = request.params_json_string
        if not UtilClient.is_unset(request.product_key):
            body['ProductKey'] = request.product_key
        if not UtilClient.is_unset(request.template_biz_code):
            body['TemplateBizCode'] = request.template_biz_code
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PrintByTemplate',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.PrintByTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    def print_by_template(self, request):
        runtime = util_models.RuntimeOptions()
        return self.print_by_template_with_options(request, runtime)

    def pub_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.correlation_data):
            query['CorrelationData'] = request.correlation_data
        if not UtilClient.is_unset(request.device_name):
            query['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        if not UtilClient.is_unset(request.qos):
            query['Qos'] = request.qos
        if not UtilClient.is_unset(request.response_topic):
            query['ResponseTopic'] = request.response_topic
        if not UtilClient.is_unset(request.topic_full_name):
            query['TopicFullName'] = request.topic_full_name
        if not UtilClient.is_unset(request.user_prop):
            query['UserProp'] = request.user_prop
        body = {}
        if not UtilClient.is_unset(request.message_content):
            body['MessageContent'] = request.message_content
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='Pub',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.PubResponse(),
            self.call_api(params, req, runtime)
        )

    def pub(self, request):
        runtime = util_models.RuntimeOptions()
        return self.pub_with_options(request, runtime)

    def pub_broadcast_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.message_content):
            query['MessageContent'] = request.message_content
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        if not UtilClient.is_unset(request.topic_full_name):
            query['TopicFullName'] = request.topic_full_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PubBroadcast',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.PubBroadcastResponse(),
            self.call_api(params, req, runtime)
        )

    def pub_broadcast(self, request):
        runtime = util_models.RuntimeOptions()
        return self.pub_broadcast_with_options(request, runtime)

    def publish_script_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.parser_id):
            query['ParserId'] = request.parser_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PublishScript',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.PublishScriptResponse(),
            self.call_api(params, req, runtime)
        )

    def publish_script(self, request):
        runtime = util_models.RuntimeOptions()
        return self.publish_script_with_options(request, runtime)

    def publish_studio_app_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.iot_instance_id):
            body['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PublishStudioApp',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.PublishStudioAppResponse(),
            self.call_api(params, req, runtime)
        )

    def publish_studio_app(self, request):
        runtime = util_models.RuntimeOptions()
        return self.publish_studio_app_with_options(request, runtime)

    def publish_thing_model_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.model_version):
            query['ModelVersion'] = request.model_version
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PublishThingModel',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.PublishThingModelResponse(),
            self.call_api(params, req, runtime)
        )

    def publish_thing_model(self, request):
        runtime = util_models.RuntimeOptions()
        return self.publish_thing_model_with_options(request, runtime)

    def push_speech_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        body = {}
        if not UtilClient.is_unset(request.device_name):
            body['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.iot_id):
            body['IotId'] = request.iot_id
        if not UtilClient.is_unset(request.iot_instance_id):
            body['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.product_key):
            body['ProductKey'] = request.product_key
        if not UtilClient.is_unset(request.project_code):
            body['ProjectCode'] = request.project_code
        if not UtilClient.is_unset(request.push_mode):
            body['PushMode'] = request.push_mode
        if not UtilClient.is_unset(request.speech_code_list):
            body['SpeechCodeList'] = request.speech_code_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PushSpeech',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.PushSpeechResponse(),
            self.call_api(params, req, runtime)
        )

    def push_speech(self, request):
        runtime = util_models.RuntimeOptions()
        return self.push_speech_with_options(request, runtime)

    def query_batch_register_device_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.apply_id):
            query['ApplyId'] = request.apply_id
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryBatchRegisterDeviceStatus',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.QueryBatchRegisterDeviceStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def query_batch_register_device_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_batch_register_device_status_with_options(request, runtime)

    def query_cert_url_by_apply_id_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.apply_id):
            query['ApplyId'] = request.apply_id
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryCertUrlByApplyId',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.QueryCertUrlByApplyIdResponse(),
            self.call_api(params, req, runtime)
        )

    def query_cert_url_by_apply_id(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_cert_url_by_apply_id_with_options(request, runtime)

    def query_client_ids_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.iot_id):
            query['IotId'] = request.iot_id
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryClientIds',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.QueryClientIdsResponse(),
            self.call_api(params, req, runtime)
        )

    def query_client_ids(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_client_ids_with_options(request, runtime)

    def query_consumer_group_by_group_id_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryConsumerGroupByGroupId',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.QueryConsumerGroupByGroupIdResponse(),
            self.call_api(params, req, runtime)
        )

    def query_consumer_group_by_group_id(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_consumer_group_by_group_id_with_options(request, runtime)

    def query_consumer_group_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.fuzzy):
            query['Fuzzy'] = request.fuzzy
        if not UtilClient.is_unset(request.group_name):
            query['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryConsumerGroupList',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.QueryConsumerGroupListResponse(),
            self.call_api(params, req, runtime)
        )

    def query_consumer_group_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_consumer_group_list_with_options(request, runtime)

    def query_consumer_group_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryConsumerGroupStatus',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.QueryConsumerGroupStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def query_consumer_group_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_consumer_group_status_with_options(request, runtime)

    def query_detail_scene_rule_log_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.rule_id):
            query['RuleId'] = request.rule_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.trace_id):
            query['TraceId'] = request.trace_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryDetailSceneRuleLog',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.QueryDetailSceneRuleLogResponse(),
            self.call_api(params, req, runtime)
        )

    def query_detail_scene_rule_log(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_detail_scene_rule_log_with_options(request, runtime)

    def query_device_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryDevice',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.QueryDeviceResponse(),
            self.call_api(params, req, runtime)
        )

    def query_device(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_device_with_options(request, runtime)

    def query_device_by_sqlwith_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.sql):
            query['SQL'] = request.sql
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryDeviceBySQL',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.QueryDeviceBySQLResponse(),
            self.call_api(params, req, runtime)
        )

    def query_device_by_sql(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_device_by_sqlwith_options(request, runtime)

    def query_device_by_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryDeviceByStatus',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.QueryDeviceByStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def query_device_by_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_device_by_status_with_options(request, runtime)

    def query_device_by_tags_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryDeviceByTags',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.QueryDeviceByTagsResponse(),
            self.call_api(params, req, runtime)
        )

    def query_device_by_tags(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_device_by_tags_with_options(request, runtime)

    def query_device_cert_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.device_name):
            query['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryDeviceCert',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.QueryDeviceCertResponse(),
            self.call_api(params, req, runtime)
        )

    def query_device_cert(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_device_cert_with_options(request, runtime)

    def query_device_desired_property_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.device_name):
            query['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.function_block_id):
            query['FunctionBlockId'] = request.function_block_id
        if not UtilClient.is_unset(request.identifier):
            query['Identifier'] = request.identifier
        if not UtilClient.is_unset(request.iot_id):
            query['IotId'] = request.iot_id
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryDeviceDesiredProperty',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.QueryDeviceDesiredPropertyResponse(),
            self.call_api(params, req, runtime)
        )

    def query_device_desired_property(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_device_desired_property_with_options(request, runtime)

    def query_device_detail_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.device_name):
            query['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.iot_id):
            query['IotId'] = request.iot_id
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryDeviceDetail',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.QueryDeviceDetailResponse(),
            self.call_api(params, req, runtime)
        )

    def query_device_detail(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_device_detail_with_options(request, runtime)

    def query_device_distribute_detail_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryDeviceDistributeDetail',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.QueryDeviceDistributeDetailResponse(),
            self.call_api(params, req, runtime)
        )

    def query_device_distribute_detail(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_device_distribute_detail_with_options(request, runtime)

    def query_device_distribute_job_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryDeviceDistributeJob',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.QueryDeviceDistributeJobResponse(),
            self.call_api(params, req, runtime)
        )

    def query_device_distribute_job(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_device_distribute_job_with_options(request, runtime)

    def query_device_event_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.asc):
            query['Asc'] = request.asc
        if not UtilClient.is_unset(request.device_name):
            query['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.event_type):
            query['EventType'] = request.event_type
        if not UtilClient.is_unset(request.identifier):
            query['Identifier'] = request.identifier
        if not UtilClient.is_unset(request.iot_id):
            query['IotId'] = request.iot_id
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryDeviceEventData',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.QueryDeviceEventDataResponse(),
            self.call_api(params, req, runtime)
        )

    def query_device_event_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_device_event_data_with_options(request, runtime)

    def query_device_file_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.device_name):
            query['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.file_id):
            query['FileId'] = request.file_id
        if not UtilClient.is_unset(request.iot_id):
            query['IotId'] = request.iot_id
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryDeviceFile',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.QueryDeviceFileResponse(),
            self.call_api(params, req, runtime)
        )

    def query_device_file(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_device_file_with_options(request, runtime)

    def query_device_file_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.device_name):
            query['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.iot_id):
            query['IotId'] = request.iot_id
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryDeviceFileList',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.QueryDeviceFileListResponse(),
            self.call_api(params, req, runtime)
        )

    def query_device_file_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_device_file_list_with_options(request, runtime)

    def query_device_group_by_device_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.device_name):
            query['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryDeviceGroupByDevice',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.QueryDeviceGroupByDeviceResponse(),
            self.call_api(params, req, runtime)
        )

    def query_device_group_by_device(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_device_group_by_device_with_options(request, runtime)

    def query_device_group_by_tags_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryDeviceGroupByTags',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.QueryDeviceGroupByTagsResponse(),
            self.call_api(params, req, runtime)
        )

    def query_device_group_by_tags(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_device_group_by_tags_with_options(request, runtime)

    def query_device_group_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.group_type):
            query['GroupType'] = request.group_type
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryDeviceGroupInfo',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.QueryDeviceGroupInfoResponse(),
            self.call_api(params, req, runtime)
        )

    def query_device_group_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_device_group_info_with_options(request, runtime)

    def query_device_group_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.group_name):
            query['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.group_types):
            query['GroupTypes'] = request.group_types
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.super_group_id):
            query['SuperGroupId'] = request.super_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryDeviceGroupList',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.QueryDeviceGroupListResponse(),
            self.call_api(params, req, runtime)
        )

    def query_device_group_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_device_group_list_with_options(request, runtime)

    def query_device_group_tag_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.group_type):
            query['GroupType'] = request.group_type
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryDeviceGroupTagList',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.QueryDeviceGroupTagListResponse(),
            self.call_api(params, req, runtime)
        )

    def query_device_group_tag_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_device_group_tag_list_with_options(request, runtime)

    def query_device_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.device_name):
            query['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.iot_id):
            query['IotId'] = request.iot_id
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryDeviceInfo',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.QueryDeviceInfoResponse(),
            self.call_api(params, req, runtime)
        )

    def query_device_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_device_info_with_options(request, runtime)

    def query_device_list_by_device_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryDeviceListByDeviceGroup',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.QueryDeviceListByDeviceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def query_device_list_by_device_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_device_list_by_device_group_with_options(request, runtime)

    def query_device_original_event_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.asc):
            query['Asc'] = request.asc
        if not UtilClient.is_unset(request.device_name):
            query['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.identifier):
            query['Identifier'] = request.identifier
        if not UtilClient.is_unset(request.iot_id):
            query['IotId'] = request.iot_id
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.next_page_token):
            query['NextPageToken'] = request.next_page_token
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryDeviceOriginalEventData',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.QueryDeviceOriginalEventDataResponse(),
            self.call_api(params, req, runtime)
        )

    def query_device_original_event_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_device_original_event_data_with_options(request, runtime)

    def query_device_original_property_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.asc):
            query['Asc'] = request.asc
        if not UtilClient.is_unset(request.device_name):
            query['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.identifier):
            query['Identifier'] = request.identifier
        if not UtilClient.is_unset(request.iot_id):
            query['IotId'] = request.iot_id
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.next_page_token):
            query['NextPageToken'] = request.next_page_token
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryDeviceOriginalPropertyData',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.QueryDeviceOriginalPropertyDataResponse(),
            self.call_api(params, req, runtime)
        )

    def query_device_original_property_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_device_original_property_data_with_options(request, runtime)

    def query_device_original_property_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.asc):
            query['Asc'] = request.asc
        if not UtilClient.is_unset(request.device_name):
            query['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.iot_id):
            query['IotId'] = request.iot_id
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.next_page_token):
            query['NextPageToken'] = request.next_page_token
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryDeviceOriginalPropertyStatus',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.QueryDeviceOriginalPropertyStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def query_device_original_property_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_device_original_property_status_with_options(request, runtime)

    def query_device_original_service_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.asc):
            query['Asc'] = request.asc
        if not UtilClient.is_unset(request.device_name):
            query['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.identifier):
            query['Identifier'] = request.identifier
        if not UtilClient.is_unset(request.iot_id):
            query['IotId'] = request.iot_id
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.next_page_token):
            query['NextPageToken'] = request.next_page_token
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryDeviceOriginalServiceData',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.QueryDeviceOriginalServiceDataResponse(),
            self.call_api(params, req, runtime)
        )

    def query_device_original_service_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_device_original_service_data_with_options(request, runtime)

    def query_device_prop_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.device_name):
            query['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.iot_id):
            query['IotId'] = request.iot_id
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryDeviceProp',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.QueryDevicePropResponse(),
            self.call_api(params, req, runtime)
        )

    def query_device_prop(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_device_prop_with_options(request, runtime)

    def query_device_properties_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.asc):
            query['Asc'] = request.asc
        if not UtilClient.is_unset(request.device_name):
            query['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.identifier):
            query['Identifier'] = request.identifier
        if not UtilClient.is_unset(request.iot_id):
            query['IotId'] = request.iot_id
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryDevicePropertiesData',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.QueryDevicePropertiesDataResponse(),
            self.call_api(params, req, runtime)
        )

    def query_device_properties_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_device_properties_data_with_options(request, runtime)

    def query_device_property_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.asc):
            query['Asc'] = request.asc
        if not UtilClient.is_unset(request.device_name):
            query['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.identifier):
            query['Identifier'] = request.identifier
        if not UtilClient.is_unset(request.iot_id):
            query['IotId'] = request.iot_id
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryDevicePropertyData',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.QueryDevicePropertyDataResponse(),
            self.call_api(params, req, runtime)
        )

    def query_device_property_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_device_property_data_with_options(request, runtime)

    def query_device_property_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.device_name):
            query['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.function_block_id):
            query['FunctionBlockId'] = request.function_block_id
        if not UtilClient.is_unset(request.iot_id):
            query['IotId'] = request.iot_id
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryDevicePropertyStatus',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.QueryDevicePropertyStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def query_device_property_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_device_property_status_with_options(request, runtime)

    def query_device_service_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.asc):
            query['Asc'] = request.asc
        if not UtilClient.is_unset(request.device_name):
            query['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.identifier):
            query['Identifier'] = request.identifier
        if not UtilClient.is_unset(request.iot_id):
            query['IotId'] = request.iot_id
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryDeviceServiceData',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.QueryDeviceServiceDataResponse(),
            self.call_api(params, req, runtime)
        )

    def query_device_service_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_device_service_data_with_options(request, runtime)

    def query_device_speech_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.iot_id):
            body['IotId'] = request.iot_id
        if not UtilClient.is_unset(request.iot_instance_id):
            body['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.page_id):
            body['PageId'] = request.page_id
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryDeviceSpeech',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.QueryDeviceSpeechResponse(),
            self.call_api(params, req, runtime)
        )

    def query_device_speech(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_device_speech_with_options(request, runtime)

    def query_device_statistics_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryDeviceStatistics',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.QueryDeviceStatisticsResponse(),
            self.call_api(params, req, runtime)
        )

    def query_device_statistics(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_device_statistics_with_options(request, runtime)

    def query_device_tunnel_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.tunnel_id):
            query['TunnelId'] = request.tunnel_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryDeviceTunnel',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.QueryDeviceTunnelResponse(),
            self.call_api(params, req, runtime)
        )

    def query_device_tunnel(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_device_tunnel_with_options(request, runtime)

    def query_dynamic_group_devices_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.device_name):
            query['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.fuzzy_name):
            query['FuzzyName'] = request.fuzzy_name
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryDynamicGroupDevices',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.QueryDynamicGroupDevicesResponse(),
            self.call_api(params, req, runtime)
        )

    def query_dynamic_group_devices(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_dynamic_group_devices_with_options(request, runtime)

    def query_edge_driver_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.driver_name):
            query['DriverName'] = request.driver_name
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryEdgeDriver',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.QueryEdgeDriverResponse(),
            self.call_api(params, req, runtime)
        )

    def query_edge_driver(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_edge_driver_with_options(request, runtime)

    def query_edge_driver_version_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.driver_id):
            query['DriverId'] = request.driver_id
        if not UtilClient.is_unset(request.driver_version):
            query['DriverVersion'] = request.driver_version
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.version_state):
            query['VersionState'] = request.version_state
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryEdgeDriverVersion',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.QueryEdgeDriverVersionResponse(),
            self.call_api(params, req, runtime)
        )

    def query_edge_driver_version(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_edge_driver_version_with_options(request, runtime)

    def query_edge_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryEdgeInstance',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.QueryEdgeInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    def query_edge_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_edge_instance_with_options(request, runtime)

    def query_edge_instance_channel_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.channel_name):
            query['ChannelName'] = request.channel_name
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.driver_id):
            query['DriverId'] = request.driver_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryEdgeInstanceChannel',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.QueryEdgeInstanceChannelResponse(),
            self.call_api(params, req, runtime)
        )

    def query_edge_instance_channel(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_edge_instance_channel_with_options(request, runtime)

    def query_edge_instance_device_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryEdgeInstanceDevice',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.QueryEdgeInstanceDeviceResponse(),
            self.call_api(params, req, runtime)
        )

    def query_edge_instance_device(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_edge_instance_device_with_options(request, runtime)

    def query_edge_instance_device_by_driver_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.driver_id):
            query['DriverId'] = request.driver_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryEdgeInstanceDeviceByDriver',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.QueryEdgeInstanceDeviceByDriverResponse(),
            self.call_api(params, req, runtime)
        )

    def query_edge_instance_device_by_driver(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_edge_instance_device_by_driver_with_options(request, runtime)

    def query_edge_instance_driver_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryEdgeInstanceDriver',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.QueryEdgeInstanceDriverResponse(),
            self.call_api(params, req, runtime)
        )

    def query_edge_instance_driver(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_edge_instance_driver_with_options(request, runtime)

    def query_edge_instance_gateway_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryEdgeInstanceGateway',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.QueryEdgeInstanceGatewayResponse(),
            self.call_api(params, req, runtime)
        )

    def query_edge_instance_gateway(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_edge_instance_gateway_with_options(request, runtime)

    def query_edge_instance_historic_deployment_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryEdgeInstanceHistoricDeployment',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.QueryEdgeInstanceHistoricDeploymentResponse(),
            self.call_api(params, req, runtime)
        )

    def query_edge_instance_historic_deployment(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_edge_instance_historic_deployment_with_options(request, runtime)

    def query_edge_instance_message_routing_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryEdgeInstanceMessageRouting',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.QueryEdgeInstanceMessageRoutingResponse(),
            self.call_api(params, req, runtime)
        )

    def query_edge_instance_message_routing(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_edge_instance_message_routing_with_options(request, runtime)

    def query_edge_instance_scene_rule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryEdgeInstanceSceneRule',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.QueryEdgeInstanceSceneRuleResponse(),
            self.call_api(params, req, runtime)
        )

    def query_edge_instance_scene_rule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_edge_instance_scene_rule_with_options(request, runtime)

    def query_imported_device_by_apply_id_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.apply_id):
            query['ApplyId'] = request.apply_id
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryImportedDeviceByApplyId',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.QueryImportedDeviceByApplyIdResponse(),
            self.call_api(params, req, runtime)
        )

    def query_imported_device_by_apply_id(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_imported_device_by_apply_id_with_options(request, runtime)

    def query_job_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryJob',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.QueryJobResponse(),
            self.call_api(params, req, runtime)
        )

    def query_job(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_job_with_options(request, runtime)

    def query_job_statistics_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryJobStatistics',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.QueryJobStatisticsResponse(),
            self.call_api(params, req, runtime)
        )

    def query_job_statistics(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_job_statistics_with_options(request, runtime)

    def query_license_device_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.iot_id):
            query['IotId'] = request.iot_id
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.license_code):
            query['LicenseCode'] = request.license_code
        if not UtilClient.is_unset(request.page_id):
            query['PageId'] = request.page_id
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryLicenseDeviceList',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.QueryLicenseDeviceListResponse(),
            self.call_api(params, req, runtime)
        )

    def query_license_device_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_license_device_list_with_options(request, runtime)

    def query_lo_ra_join_permissions_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryLoRaJoinPermissions',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.QueryLoRaJoinPermissionsResponse(),
            self.call_api(params, req, runtime)
        )

    def query_lo_ra_join_permissions(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_lo_ra_join_permissions_with_options(request, runtime)

    def query_message_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.uni_msg_id):
            query['UniMsgId'] = request.uni_msg_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryMessageInfo',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.QueryMessageInfoResponse(),
            self.call_api(params, req, runtime)
        )

    def query_message_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_message_info_with_options(request, runtime)

    def query_otafirmware_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.firmware_id):
            query['FirmwareId'] = request.firmware_id
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryOTAFirmware',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.QueryOTAFirmwareResponse(),
            self.call_api(params, req, runtime)
        )

    def query_otafirmware(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_otafirmware_with_options(request, runtime)

    def query_otajob_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryOTAJob',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.QueryOTAJobResponse(),
            self.call_api(params, req, runtime)
        )

    def query_otajob(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_otajob_with_options(request, runtime)

    def query_page_by_apply_id_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.apply_id):
            query['ApplyId'] = request.apply_id
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryPageByApplyId',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.QueryPageByApplyIdResponse(),
            self.call_api(params, req, runtime)
        )

    def query_page_by_apply_id(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_page_by_apply_id_with_options(request, runtime)

    def query_product_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryProduct',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.QueryProductResponse(),
            self.call_api(params, req, runtime)
        )

    def query_product(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_product_with_options(request, runtime)

    def query_product_cert_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryProductCertInfo',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.QueryProductCertInfoResponse(),
            self.call_api(params, req, runtime)
        )

    def query_product_cert_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_product_cert_info_with_options(request, runtime)

    def query_product_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.aliyun_commodity_code):
            query['AliyunCommodityCode'] = request.aliyun_commodity_code
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryProductList',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.QueryProductListResponse(),
            self.call_api(params, req, runtime)
        )

    def query_product_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_product_list_with_options(request, runtime)

    def query_product_topic_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryProductTopic',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.QueryProductTopicResponse(),
            self.call_api(params, req, runtime)
        )

    def query_product_topic(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_product_topic_with_options(request, runtime)

    def query_scene_rule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.rule_name):
            query['RuleName'] = request.rule_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QuerySceneRule',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.QuerySceneRuleResponse(),
            self.call_api(params, req, runtime)
        )

    def query_scene_rule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_scene_rule_with_options(request, runtime)

    def query_schedule_period_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.iot_instance_id):
            body['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.page_id):
            body['PageId'] = request.page_id
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.schedule_code):
            body['ScheduleCode'] = request.schedule_code
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QuerySchedulePeriodList',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.QuerySchedulePeriodListResponse(),
            self.call_api(params, req, runtime)
        )

    def query_schedule_period_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_schedule_period_list_with_options(request, runtime)

    def query_solution_device_group_page_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.fuzzy_group_name):
            query['FuzzyGroupName'] = request.fuzzy_group_name
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.page_id):
            query['PageId'] = request.page_id
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.project_code):
            query['ProjectCode'] = request.project_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QuerySolutionDeviceGroupPage',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.QuerySolutionDeviceGroupPageResponse(),
            self.call_api(params, req, runtime)
        )

    def query_solution_device_group_page(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_solution_device_group_page_with_options(request, runtime)

    def query_sound_code_label_batch_failed_result_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.batch_code):
            body['BatchCode'] = request.batch_code
        if not UtilClient.is_unset(request.iot_instance_id):
            body['IotInstanceId'] = request.iot_instance_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QuerySoundCodeLabelBatchFailedResult',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.QuerySoundCodeLabelBatchFailedResultResponse(),
            self.call_api(params, req, runtime)
        )

    def query_sound_code_label_batch_failed_result(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_sound_code_label_batch_failed_result_with_options(request, runtime)

    def query_sound_code_label_batch_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.iot_instance_id):
            body['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.page_id):
            body['PageId'] = request.page_id
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.schedule_code):
            body['ScheduleCode'] = request.schedule_code
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QuerySoundCodeLabelBatchList',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.QuerySoundCodeLabelBatchListResponse(),
            self.call_api(params, req, runtime)
        )

    def query_sound_code_label_batch_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_sound_code_label_batch_list_with_options(request, runtime)

    def query_sound_code_label_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.iot_instance_id):
            body['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.page_id):
            body['PageId'] = request.page_id
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.schedule_code):
            body['ScheduleCode'] = request.schedule_code
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QuerySoundCodeLabelList',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.QuerySoundCodeLabelListResponse(),
            self.call_api(params, req, runtime)
        )

    def query_sound_code_label_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_sound_code_label_list_with_options(request, runtime)

    def query_sound_code_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.iot_instance_id):
            body['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.page_id):
            body['PageId'] = request.page_id
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QuerySoundCodeList',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.QuerySoundCodeListResponse(),
            self.call_api(params, req, runtime)
        )

    def query_sound_code_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_sound_code_list_with_options(request, runtime)

    def query_sound_code_schedule_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.iot_instance_id):
            body['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.page_id):
            body['PageId'] = request.page_id
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QuerySoundCodeScheduleList',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.QuerySoundCodeScheduleListResponse(),
            self.call_api(params, req, runtime)
        )

    def query_sound_code_schedule_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_sound_code_schedule_list_with_options(request, runtime)

    def query_speech_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.iot_instance_id):
            body['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.speech_code):
            body['SpeechCode'] = request.speech_code
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QuerySpeech',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.QuerySpeechResponse(),
            self.call_api(params, req, runtime)
        )

    def query_speech(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_speech_with_options(request, runtime)

    def query_speech_device_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.available_space):
            body['AvailableSpace'] = request.available_space
        if not UtilClient.is_unset(request.available_space_scope):
            body['AvailableSpaceScope'] = request.available_space_scope
        if not UtilClient.is_unset(request.device_name):
            body['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.iot_instance_id):
            body['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.page_id):
            body['PageId'] = request.page_id
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.project_code):
            body['ProjectCode'] = request.project_code
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QuerySpeechDevice',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.QuerySpeechDeviceResponse(),
            self.call_api(params, req, runtime)
        )

    def query_speech_device(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_speech_device_with_options(request, runtime)

    def query_speech_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.audio_format):
            body['AudioFormat'] = request.audio_format
        if not UtilClient.is_unset(request.iot_instance_id):
            body['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.page_id):
            body['PageId'] = request.page_id
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.project_code):
            body['ProjectCode'] = request.project_code
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QuerySpeechList',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.QuerySpeechListResponse(),
            self.call_api(params, req, runtime)
        )

    def query_speech_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_speech_list_with_options(request, runtime)

    def query_speech_push_job_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.job_code):
            query['JobCode'] = request.job_code
        body = {}
        if not UtilClient.is_unset(request.iot_instance_id):
            body['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.page_id):
            body['PageId'] = request.page_id
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.project_code):
            body['ProjectCode'] = request.project_code
        if not UtilClient.is_unset(request.push_mode):
            body['PushMode'] = request.push_mode
        if not UtilClient.is_unset(request.status_list):
            body['StatusList'] = request.status_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QuerySpeechPushJob',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.QuerySpeechPushJobResponse(),
            self.call_api(params, req, runtime)
        )

    def query_speech_push_job(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_speech_push_job_with_options(request, runtime)

    def query_speech_push_job_device_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.device_name):
            body['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.iot_instance_id):
            body['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.job_code):
            body['JobCode'] = request.job_code
        if not UtilClient.is_unset(request.page_id):
            body['PageId'] = request.page_id
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QuerySpeechPushJobDevice',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.QuerySpeechPushJobDeviceResponse(),
            self.call_api(params, req, runtime)
        )

    def query_speech_push_job_device(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_speech_push_job_device_with_options(request, runtime)

    def query_speech_push_job_speech_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.iot_instance_id):
            body['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.job_code):
            body['JobCode'] = request.job_code
        if not UtilClient.is_unset(request.page_id):
            body['PageId'] = request.page_id
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QuerySpeechPushJobSpeech',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.QuerySpeechPushJobSpeechResponse(),
            self.call_api(params, req, runtime)
        )

    def query_speech_push_job_speech(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_speech_push_job_speech_with_options(request, runtime)

    def query_studio_app_domain_list_open_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.iot_instance_id):
            body['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryStudioAppDomainListOpen',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.QueryStudioAppDomainListOpenResponse(),
            self.call_api(params, req, runtime)
        )

    def query_studio_app_domain_list_open(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_studio_app_domain_list_open_with_options(request, runtime)

    def query_studio_app_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.fuzzy_name):
            body['FuzzyName'] = request.fuzzy_name
        if not UtilClient.is_unset(request.iot_instance_id):
            body['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.page_no):
            body['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        if not UtilClient.is_unset(request.types):
            body['Types'] = request.types
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryStudioAppList',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.QueryStudioAppListResponse(),
            self.call_api(params, req, runtime)
        )

    def query_studio_app_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_studio_app_list_with_options(request, runtime)

    def query_studio_app_page_list_open_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.iot_instance_id):
            body['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.is_release):
            body['IsRelease'] = request.is_release
        if not UtilClient.is_unset(request.page_no):
            body['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryStudioAppPageListOpen',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.QueryStudioAppPageListOpenResponse(),
            self.call_api(params, req, runtime)
        )

    def query_studio_app_page_list_open(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_studio_app_page_list_open_with_options(request, runtime)

    def query_studio_project_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.iot_instance_id):
            body['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.page_no):
            body['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryStudioProjectList',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.QueryStudioProjectListResponse(),
            self.call_api(params, req, runtime)
        )

    def query_studio_project_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_studio_project_list_with_options(request, runtime)

    def query_subscribe_relation_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QuerySubscribeRelation',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.QuerySubscribeRelationResponse(),
            self.call_api(params, req, runtime)
        )

    def query_subscribe_relation(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_subscribe_relation_with_options(request, runtime)

    def query_summary_scene_rule_log_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.rule_id):
            query['RuleId'] = request.rule_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QuerySummarySceneRuleLog',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.QuerySummarySceneRuleLogResponse(),
            self.call_api(params, req, runtime)
        )

    def query_summary_scene_rule_log(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_summary_scene_rule_log_with_options(request, runtime)

    def query_super_device_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QuerySuperDeviceGroup',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.QuerySuperDeviceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def query_super_device_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_super_device_group_with_options(request, runtime)

    def query_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryTask',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.QueryTaskResponse(),
            self.call_api(params, req, runtime)
        )

    def query_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_task_with_options(request, runtime)

    def query_thing_model_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.function_block_id):
            query['FunctionBlockId'] = request.function_block_id
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.model_version):
            query['ModelVersion'] = request.model_version
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryThingModel',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.QueryThingModelResponse(),
            self.call_api(params, req, runtime)
        )

    def query_thing_model(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_thing_model_with_options(request, runtime)

    def query_thing_model_extend_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.function_block_id):
            query['FunctionBlockId'] = request.function_block_id
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.model_version):
            query['ModelVersion'] = request.model_version
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryThingModelExtendConfig',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.QueryThingModelExtendConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def query_thing_model_extend_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_thing_model_extend_config_with_options(request, runtime)

    def query_thing_model_extend_config_published_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.function_block_id):
            query['FunctionBlockId'] = request.function_block_id
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.model_version):
            query['ModelVersion'] = request.model_version
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryThingModelExtendConfigPublished',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.QueryThingModelExtendConfigPublishedResponse(),
            self.call_api(params, req, runtime)
        )

    def query_thing_model_extend_config_published(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_thing_model_extend_config_published_with_options(request, runtime)

    def query_thing_model_published_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.function_block_id):
            query['FunctionBlockId'] = request.function_block_id
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.model_version):
            query['ModelVersion'] = request.model_version
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryThingModelPublished',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.QueryThingModelPublishedResponse(),
            self.call_api(params, req, runtime)
        )

    def query_thing_model_published(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_thing_model_published_with_options(request, runtime)

    def query_topic_reverse_route_table_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.topic):
            query['Topic'] = request.topic
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryTopicReverseRouteTable',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.QueryTopicReverseRouteTableResponse(),
            self.call_api(params, req, runtime)
        )

    def query_topic_reverse_route_table(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_topic_reverse_route_table_with_options(request, runtime)

    def query_topic_route_table_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.topic):
            query['Topic'] = request.topic
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryTopicRouteTable',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.QueryTopicRouteTableResponse(),
            self.call_api(params, req, runtime)
        )

    def query_topic_route_table(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_topic_route_table_with_options(request, runtime)

    def r_rpc_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.device_name):
            query['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        if not UtilClient.is_unset(request.request_base_64byte):
            query['RequestBase64Byte'] = request.request_base_64byte
        if not UtilClient.is_unset(request.timeout):
            query['Timeout'] = request.timeout
        if not UtilClient.is_unset(request.topic):
            query['Topic'] = request.topic
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RRpc',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.RRpcResponse(),
            self.call_api(params, req, runtime)
        )

    def r_rpc(self, request):
        runtime = util_models.RuntimeOptions()
        return self.r_rpc_with_options(request, runtime)

    def recognize_car_num_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RecognizeCarNum',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.RecognizeCarNumResponse(),
            self.call_api(params, req, runtime)
        )

    def recognize_car_num(self, request):
        runtime = util_models.RuntimeOptions()
        return self.recognize_car_num_with_options(request, runtime)

    def recognize_picture_general_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RecognizePictureGeneral',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.RecognizePictureGeneralResponse(),
            self.call_api(params, req, runtime)
        )

    def recognize_picture_general(self, request):
        runtime = util_models.RuntimeOptions()
        return self.recognize_picture_general_with_options(request, runtime)

    def refresh_device_tunnel_share_password_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.device_name):
            query['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RefreshDeviceTunnelSharePassword',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.RefreshDeviceTunnelSharePasswordResponse(),
            self.call_api(params, req, runtime)
        )

    def refresh_device_tunnel_share_password(self, request):
        runtime = util_models.RuntimeOptions()
        return self.refresh_device_tunnel_share_password_with_options(request, runtime)

    def refresh_studio_app_token_open_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.iot_instance_id):
            body['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RefreshStudioAppTokenOpen',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.RefreshStudioAppTokenOpenResponse(),
            self.call_api(params, req, runtime)
        )

    def refresh_studio_app_token_open(self, request):
        runtime = util_models.RuntimeOptions()
        return self.refresh_studio_app_token_open_with_options(request, runtime)

    def register_device_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_key):
            query['AppKey'] = request.app_key
        if not UtilClient.is_unset(request.dev_eui):
            query['DevEui'] = request.dev_eui
        if not UtilClient.is_unset(request.device_name):
            query['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.join_eui):
            query['JoinEui'] = request.join_eui
        if not UtilClient.is_unset(request.lora_node_type):
            query['LoraNodeType'] = request.lora_node_type
        if not UtilClient.is_unset(request.nickname):
            query['Nickname'] = request.nickname
        if not UtilClient.is_unset(request.pin_code):
            query['PinCode'] = request.pin_code
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RegisterDevice',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.RegisterDeviceResponse(),
            self.call_api(params, req, runtime)
        )

    def register_device(self, request):
        runtime = util_models.RuntimeOptions()
        return self.register_device_with_options(request, runtime)

    def release_edge_driver_version_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.driver_id):
            query['DriverId'] = request.driver_id
        if not UtilClient.is_unset(request.driver_version):
            query['DriverVersion'] = request.driver_version
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ReleaseEdgeDriverVersion',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.ReleaseEdgeDriverVersionResponse(),
            self.call_api(params, req, runtime)
        )

    def release_edge_driver_version(self, request):
        runtime = util_models.RuntimeOptions()
        return self.release_edge_driver_version_with_options(request, runtime)

    def release_product_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ReleaseProduct',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.ReleaseProductResponse(),
            self.call_api(params, req, runtime)
        )

    def release_product(self, request):
        runtime = util_models.RuntimeOptions()
        return self.release_product_with_options(request, runtime)

    def remove_thing_topo_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.device_name):
            query['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.iot_id):
            query['IotId'] = request.iot_id
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemoveThingTopo',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.RemoveThingTopoResponse(),
            self.call_api(params, req, runtime)
        )

    def remove_thing_topo(self, request):
        runtime = util_models.RuntimeOptions()
        return self.remove_thing_topo_with_options(request, runtime)

    def replace_edge_instance_gateway_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_gateway_id):
            query['CurrentGatewayId'] = request.current_gateway_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.new_gateway_id):
            query['NewGatewayId'] = request.new_gateway_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ReplaceEdgeInstanceGateway',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.ReplaceEdgeInstanceGatewayResponse(),
            self.call_api(params, req, runtime)
        )

    def replace_edge_instance_gateway(self, request):
        runtime = util_models.RuntimeOptions()
        return self.replace_edge_instance_gateway_with_options(request, runtime)

    def rerun_job_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RerunJob',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.RerunJobResponse(),
            self.call_api(params, req, runtime)
        )

    def rerun_job(self, request):
        runtime = util_models.RuntimeOptions()
        return self.rerun_job_with_options(request, runtime)

    def reset_consumer_group_position_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ResetConsumerGroupPosition',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.ResetConsumerGroupPositionResponse(),
            self.call_api(params, req, runtime)
        )

    def reset_consumer_group_position(self, request):
        runtime = util_models.RuntimeOptions()
        return self.reset_consumer_group_position_with_options(request, runtime)

    def reset_thing_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.device_name):
            query['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.iot_id):
            query['IotId'] = request.iot_id
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ResetThing',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.ResetThingResponse(),
            self.call_api(params, req, runtime)
        )

    def reset_thing(self, request):
        runtime = util_models.RuntimeOptions()
        return self.reset_thing_with_options(request, runtime)

    def retry_sound_code_label_batch_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.batch_code):
            body['BatchCode'] = request.batch_code
        if not UtilClient.is_unset(request.iot_instance_id):
            body['IotInstanceId'] = request.iot_instance_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RetrySoundCodeLabelBatch',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.RetrySoundCodeLabelBatchResponse(),
            self.call_api(params, req, runtime)
        )

    def retry_sound_code_label_batch(self, request):
        runtime = util_models.RuntimeOptions()
        return self.retry_sound_code_label_batch_with_options(request, runtime)

    def reupgrade_otatask_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ReupgradeOTATask',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.ReupgradeOTATaskResponse(),
            self.call_api(params, req, runtime)
        )

    def reupgrade_otatask(self, request):
        runtime = util_models.RuntimeOptions()
        return self.reupgrade_otatask_with_options(request, runtime)

    def save_device_prop_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.device_name):
            query['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.iot_id):
            query['IotId'] = request.iot_id
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        if not UtilClient.is_unset(request.props):
            query['Props'] = request.props
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SaveDeviceProp',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.SaveDevicePropResponse(),
            self.call_api(params, req, runtime)
        )

    def save_device_prop(self, request):
        runtime = util_models.RuntimeOptions()
        return self.save_device_prop_with_options(request, runtime)

    def save_script_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.parser_id):
            query['ParserId'] = request.parser_id
        if not UtilClient.is_unset(request.script_draft):
            query['ScriptDraft'] = request.script_draft
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SaveScript',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.SaveScriptResponse(),
            self.call_api(params, req, runtime)
        )

    def save_script(self, request):
        runtime = util_models.RuntimeOptions()
        return self.save_script_with_options(request, runtime)

    def set_device_desired_property_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.device_name):
            query['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.iot_id):
            query['IotId'] = request.iot_id
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.items):
            query['Items'] = request.items
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        if not UtilClient.is_unset(request.versions):
            query['Versions'] = request.versions
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetDeviceDesiredProperty',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.SetDeviceDesiredPropertyResponse(),
            self.call_api(params, req, runtime)
        )

    def set_device_desired_property(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_device_desired_property_with_options(request, runtime)

    def set_device_group_tags_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.group_type):
            query['GroupType'] = request.group_type
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.tag_string):
            query['TagString'] = request.tag_string
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetDeviceGroupTags',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.SetDeviceGroupTagsResponse(),
            self.call_api(params, req, runtime)
        )

    def set_device_group_tags(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_device_group_tags_with_options(request, runtime)

    def set_device_property_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.device_name):
            query['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.iot_id):
            query['IotId'] = request.iot_id
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.items):
            query['Items'] = request.items
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetDeviceProperty',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.SetDevicePropertyResponse(),
            self.call_api(params, req, runtime)
        )

    def set_device_property(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_device_property_with_options(request, runtime)

    def set_devices_property_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.device_name):
            query['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.items):
            query['Items'] = request.items
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetDevicesProperty',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.SetDevicesPropertyResponse(),
            self.call_api(params, req, runtime)
        )

    def set_devices_property(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_devices_property_with_options(request, runtime)

    def set_edge_instance_driver_configs_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.configs):
            query['Configs'] = request.configs
        if not UtilClient.is_unset(request.driver_id):
            query['DriverId'] = request.driver_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetEdgeInstanceDriverConfigs',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.SetEdgeInstanceDriverConfigsResponse(),
            self.call_api(params, req, runtime)
        )

    def set_edge_instance_driver_configs(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_edge_instance_driver_configs_with_options(request, runtime)

    def set_product_cert_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.issue_model):
            query['IssueModel'] = request.issue_model
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetProductCertInfo',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.SetProductCertInfoResponse(),
            self.call_api(params, req, runtime)
        )

    def set_product_cert_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_product_cert_info_with_options(request, runtime)

    def set_studio_project_cooperation_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.iot_instance_id):
            body['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SetStudioProjectCooperation',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.SetStudioProjectCooperationResponse(),
            self.call_api(params, req, runtime)
        )

    def set_studio_project_cooperation(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_studio_project_cooperation_with_options(request, runtime)

    def setup_studio_app_auth_mode_open_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.auth_mode):
            body['AuthMode'] = request.auth_mode
        if not UtilClient.is_unset(request.iot_instance_id):
            body['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.project_id):
            body['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SetupStudioAppAuthModeOpen',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.SetupStudioAppAuthModeOpenResponse(),
            self.call_api(params, req, runtime)
        )

    def setup_studio_app_auth_mode_open(self, request):
        runtime = util_models.RuntimeOptions()
        return self.setup_studio_app_auth_mode_open_with_options(request, runtime)

    def speech_by_combination_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.audio_format):
            body['AudioFormat'] = request.audio_format
        if not UtilClient.is_unset(request.combination_list):
            body['CombinationList'] = request.combination_list
        if not UtilClient.is_unset(request.device_name):
            body['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.iot_id):
            body['IotId'] = request.iot_id
        if not UtilClient.is_unset(request.iot_instance_id):
            body['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.product_key):
            body['ProductKey'] = request.product_key
        if not UtilClient.is_unset(request.speech_id):
            body['SpeechId'] = request.speech_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SpeechByCombination',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.SpeechByCombinationResponse(),
            self.call_api(params, req, runtime)
        )

    def speech_by_combination(self, request):
        runtime = util_models.RuntimeOptions()
        return self.speech_by_combination_with_options(request, runtime)

    def speech_by_synthesis_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.audio_format):
            body['AudioFormat'] = request.audio_format
        if not UtilClient.is_unset(request.device_name):
            body['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.iot_id):
            body['IotId'] = request.iot_id
        if not UtilClient.is_unset(request.iot_instance_id):
            body['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.product_key):
            body['ProductKey'] = request.product_key
        if not UtilClient.is_unset(request.speech_id):
            body['SpeechId'] = request.speech_id
        if not UtilClient.is_unset(request.speech_rate):
            body['SpeechRate'] = request.speech_rate
        if not UtilClient.is_unset(request.text):
            body['Text'] = request.text
        if not UtilClient.is_unset(request.voice):
            body['Voice'] = request.voice
        if not UtilClient.is_unset(request.volume):
            body['Volume'] = request.volume
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SpeechBySynthesis',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.SpeechBySynthesisResponse(),
            self.call_api(params, req, runtime)
        )

    def speech_by_synthesis(self, request):
        runtime = util_models.RuntimeOptions()
        return self.speech_by_synthesis_with_options(request, runtime)

    def start_cpu_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.iot_id):
            query['IotId'] = request.iot_id
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.target_value):
            query['TargetValue'] = request.target_value
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartCpu',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.StartCpuResponse(),
            self.call_api(params, req, runtime)
        )

    def start_cpu(self, request):
        runtime = util_models.RuntimeOptions()
        return self.start_cpu_with_options(request, runtime)

    def start_parser_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.parser_id):
            query['ParserId'] = request.parser_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartParser',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.StartParserResponse(),
            self.call_api(params, req, runtime)
        )

    def start_parser(self, request):
        runtime = util_models.RuntimeOptions()
        return self.start_parser_with_options(request, runtime)

    def start_rule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.rule_id):
            query['RuleId'] = request.rule_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartRule',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.StartRuleResponse(),
            self.call_api(params, req, runtime)
        )

    def start_rule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.start_rule_with_options(request, runtime)

    def stop_parser_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.parser_id):
            query['ParserId'] = request.parser_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopParser',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.StopParserResponse(),
            self.call_api(params, req, runtime)
        )

    def stop_parser(self, request):
        runtime = util_models.RuntimeOptions()
        return self.stop_parser_with_options(request, runtime)

    def stop_rule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.rule_id):
            query['RuleId'] = request.rule_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopRule',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.StopRuleResponse(),
            self.call_api(params, req, runtime)
        )

    def stop_rule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.stop_rule_with_options(request, runtime)

    def subscribe_topic_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.device_name):
            query['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        if not UtilClient.is_unset(request.topic):
            query['Topic'] = request.topic
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SubscribeTopic',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.SubscribeTopicResponse(),
            self.call_api(params, req, runtime)
        )

    def subscribe_topic(self, request):
        runtime = util_models.RuntimeOptions()
        return self.subscribe_topic_with_options(request, runtime)

    def sync_speech_by_combination_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.audio_format):
            body['AudioFormat'] = request.audio_format
        if not UtilClient.is_unset(request.combination_list):
            body['CombinationList'] = request.combination_list
        if not UtilClient.is_unset(request.device_name):
            body['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.iot_id):
            body['IotId'] = request.iot_id
        if not UtilClient.is_unset(request.iot_instance_id):
            body['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.product_key):
            body['ProductKey'] = request.product_key
        if not UtilClient.is_unset(request.speech_id):
            body['SpeechId'] = request.speech_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SyncSpeechByCombination',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.SyncSpeechByCombinationResponse(),
            self.call_api(params, req, runtime)
        )

    def sync_speech_by_combination(self, request):
        runtime = util_models.RuntimeOptions()
        return self.sync_speech_by_combination_with_options(request, runtime)

    def test_speech_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = iot_20180120_models.TestSpeechShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.sound_code_config):
            request.sound_code_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.sound_code_config, 'SoundCodeConfig', 'json')
        body = {}
        if not UtilClient.is_unset(request.audio_format):
            body['AudioFormat'] = request.audio_format
        if not UtilClient.is_unset(request.enable_sound_code):
            body['EnableSoundCode'] = request.enable_sound_code
        if not UtilClient.is_unset(request.iot_instance_id):
            body['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.project_code):
            body['ProjectCode'] = request.project_code
        if not UtilClient.is_unset(request.sound_code_config_shrink):
            body['SoundCodeConfig'] = request.sound_code_config_shrink
        if not UtilClient.is_unset(request.speech_rate):
            body['SpeechRate'] = request.speech_rate
        if not UtilClient.is_unset(request.speech_type):
            body['SpeechType'] = request.speech_type
        if not UtilClient.is_unset(request.text):
            body['Text'] = request.text
        if not UtilClient.is_unset(request.voice):
            body['Voice'] = request.voice
        if not UtilClient.is_unset(request.volume):
            body['Volume'] = request.volume
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='TestSpeech',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.TestSpeechResponse(),
            self.call_api(params, req, runtime)
        )

    def test_speech(self, request):
        runtime = util_models.RuntimeOptions()
        return self.test_speech_with_options(request, runtime)

    def transform_client_id_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.client_id):
            query['ClientId'] = request.client_id
        if not UtilClient.is_unset(request.iot_id):
            query['IotId'] = request.iot_id
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TransformClientId',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.TransformClientIdResponse(),
            self.call_api(params, req, runtime)
        )

    def transform_client_id(self, request):
        runtime = util_models.RuntimeOptions()
        return self.transform_client_id_with_options(request, runtime)

    def trigger_scene_rule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.rule_id):
            query['RuleId'] = request.rule_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TriggerSceneRule',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.TriggerSceneRuleResponse(),
            self.call_api(params, req, runtime)
        )

    def trigger_scene_rule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.trigger_scene_rule_with_options(request, runtime)

    def unbind_application_from_edge_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_id):
            query['ApplicationId'] = request.application_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UnbindApplicationFromEdgeInstance',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.UnbindApplicationFromEdgeInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    def unbind_application_from_edge_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.unbind_application_from_edge_instance_with_options(request, runtime)

    def unbind_driver_from_edge_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.driver_id):
            query['DriverId'] = request.driver_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UnbindDriverFromEdgeInstance',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.UnbindDriverFromEdgeInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    def unbind_driver_from_edge_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.unbind_driver_from_edge_instance_with_options(request, runtime)

    def unbind_license_product_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.license_code):
            query['LicenseCode'] = request.license_code
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UnbindLicenseProduct',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.UnbindLicenseProductResponse(),
            self.call_api(params, req, runtime)
        )

    def unbind_license_product(self, request):
        runtime = util_models.RuntimeOptions()
        return self.unbind_license_product_with_options(request, runtime)

    def unbind_role_from_edge_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UnbindRoleFromEdgeInstance',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.UnbindRoleFromEdgeInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    def unbind_role_from_edge_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.unbind_role_from_edge_instance_with_options(request, runtime)

    def unbind_scene_rule_from_edge_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.rule_id):
            query['RuleId'] = request.rule_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UnbindSceneRuleFromEdgeInstance',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.UnbindSceneRuleFromEdgeInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    def unbind_scene_rule_from_edge_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.unbind_scene_rule_from_edge_instance_with_options(request, runtime)

    def update_consumer_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.new_group_name):
            query['NewGroupName'] = request.new_group_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateConsumerGroup',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.UpdateConsumerGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def update_consumer_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_consumer_group_with_options(request, runtime)

    def update_destination_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.configuration):
            query['Configuration'] = request.configuration
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.destination_id):
            query['DestinationId'] = request.destination_id
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateDestination',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.UpdateDestinationResponse(),
            self.call_api(params, req, runtime)
        )

    def update_destination(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_destination_with_options(request, runtime)

    def update_device_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.group_desc):
            query['GroupDesc'] = request.group_desc
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.group_type):
            query['GroupType'] = request.group_type
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateDeviceGroup',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.UpdateDeviceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def update_device_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_device_group_with_options(request, runtime)

    def update_device_shadow_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.delta_update):
            query['DeltaUpdate'] = request.delta_update
        if not UtilClient.is_unset(request.device_name):
            query['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        if not UtilClient.is_unset(request.shadow_message):
            query['ShadowMessage'] = request.shadow_message
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateDeviceShadow',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.UpdateDeviceShadowResponse(),
            self.call_api(params, req, runtime)
        )

    def update_device_shadow(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_device_shadow_with_options(request, runtime)

    def update_edge_driver_version_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.argument):
            query['Argument'] = request.argument
        if not UtilClient.is_unset(request.config_check_rule):
            query['ConfigCheckRule'] = request.config_check_rule
        if not UtilClient.is_unset(request.container_config):
            query['ContainerConfig'] = request.container_config
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.driver_config):
            query['DriverConfig'] = request.driver_config
        if not UtilClient.is_unset(request.driver_id):
            query['DriverId'] = request.driver_id
        if not UtilClient.is_unset(request.driver_version):
            query['DriverVersion'] = request.driver_version
        if not UtilClient.is_unset(request.edge_version):
            query['EdgeVersion'] = request.edge_version
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.source_config):
            query['SourceConfig'] = request.source_config
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateEdgeDriverVersion',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.UpdateEdgeDriverVersionResponse(),
            self.call_api(params, req, runtime)
        )

    def update_edge_driver_version(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_edge_driver_version_with_options(request, runtime)

    def update_edge_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_enable):
            query['BizEnable'] = request.biz_enable
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.spec):
            query['Spec'] = request.spec
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateEdgeInstance',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.UpdateEdgeInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    def update_edge_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_edge_instance_with_options(request, runtime)

    def update_edge_instance_channel_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.channel_id):
            query['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.channel_name):
            query['ChannelName'] = request.channel_name
        if not UtilClient.is_unset(request.configs):
            query['Configs'] = request.configs
        if not UtilClient.is_unset(request.driver_id):
            query['DriverId'] = request.driver_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateEdgeInstanceChannel',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.UpdateEdgeInstanceChannelResponse(),
            self.call_api(params, req, runtime)
        )

    def update_edge_instance_channel(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_edge_instance_channel_with_options(request, runtime)

    def update_edge_instance_message_routing_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.route_id):
            query['RouteId'] = request.route_id
        if not UtilClient.is_unset(request.source_data):
            query['SourceData'] = request.source_data
        if not UtilClient.is_unset(request.source_type):
            query['SourceType'] = request.source_type
        if not UtilClient.is_unset(request.target_data):
            query['TargetData'] = request.target_data
        if not UtilClient.is_unset(request.target_iot_hub_qos):
            query['TargetIotHubQos'] = request.target_iot_hub_qos
        if not UtilClient.is_unset(request.target_type):
            query['TargetType'] = request.target_type
        if not UtilClient.is_unset(request.topic_filter):
            query['TopicFilter'] = request.topic_filter
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateEdgeInstanceMessageRouting',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.UpdateEdgeInstanceMessageRoutingResponse(),
            self.call_api(params, req, runtime)
        )

    def update_edge_instance_message_routing(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_edge_instance_message_routing_with_options(request, runtime)

    def update_job_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = iot_20180120_models.UpdateJobShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.rollout_config):
            request.rollout_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.rollout_config, 'RolloutConfig', 'json')
        if not UtilClient.is_unset(tmp_req.timeout_config):
            request.timeout_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.timeout_config, 'TimeoutConfig', 'json')
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        if not UtilClient.is_unset(request.rollout_config_shrink):
            query['RolloutConfig'] = request.rollout_config_shrink
        if not UtilClient.is_unset(request.timeout_config_shrink):
            query['TimeoutConfig'] = request.timeout_config_shrink
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateJob',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.UpdateJobResponse(),
            self.call_api(params, req, runtime)
        )

    def update_job(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_job_with_options(request, runtime)

    def update_otamodule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alias_name):
            query['AliasName'] = request.alias_name
        if not UtilClient.is_unset(request.desc):
            query['Desc'] = request.desc
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.module_name):
            query['ModuleName'] = request.module_name
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateOTAModule',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.UpdateOTAModuleResponse(),
            self.call_api(params, req, runtime)
        )

    def update_otamodule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_otamodule_with_options(request, runtime)

    def update_parser_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.parser_id):
            query['ParserId'] = request.parser_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateParser',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.UpdateParserResponse(),
            self.call_api(params, req, runtime)
        )

    def update_parser(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_parser_with_options(request, runtime)

    def update_parser_data_source_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.data_source_id):
            query['DataSourceId'] = request.data_source_id
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateParserDataSource',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.UpdateParserDataSourceResponse(),
            self.call_api(params, req, runtime)
        )

    def update_parser_data_source(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_parser_data_source_with_options(request, runtime)

    def update_product_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        if not UtilClient.is_unset(request.product_name):
            query['ProductName'] = request.product_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateProduct',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.UpdateProductResponse(),
            self.call_api(params, req, runtime)
        )

    def update_product(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_product_with_options(request, runtime)

    def update_product_filter_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        if not UtilClient.is_unset(request.property_timestamp_filter):
            query['PropertyTimestampFilter'] = request.property_timestamp_filter
        if not UtilClient.is_unset(request.property_value_filter):
            query['PropertyValueFilter'] = request.property_value_filter
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateProductFilterConfig',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.UpdateProductFilterConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def update_product_filter_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_product_filter_config_with_options(request, runtime)

    def update_product_tags_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        if not UtilClient.is_unset(request.product_tag):
            query['ProductTag'] = request.product_tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateProductTags',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.UpdateProductTagsResponse(),
            self.call_api(params, req, runtime)
        )

    def update_product_tags(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_product_tags_with_options(request, runtime)

    def update_product_topic_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.desc):
            query['Desc'] = request.desc
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.operation):
            query['Operation'] = request.operation
        if not UtilClient.is_unset(request.topic_id):
            query['TopicId'] = request.topic_id
        if not UtilClient.is_unset(request.topic_short_name):
            query['TopicShortName'] = request.topic_short_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateProductTopic',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.UpdateProductTopicResponse(),
            self.call_api(params, req, runtime)
        )

    def update_product_topic(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_product_topic_with_options(request, runtime)

    def update_rule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        if not UtilClient.is_unset(request.rule_desc):
            query['RuleDesc'] = request.rule_desc
        if not UtilClient.is_unset(request.rule_id):
            query['RuleId'] = request.rule_id
        if not UtilClient.is_unset(request.select):
            query['Select'] = request.select
        if not UtilClient.is_unset(request.short_topic):
            query['ShortTopic'] = request.short_topic
        if not UtilClient.is_unset(request.topic):
            query['Topic'] = request.topic
        if not UtilClient.is_unset(request.topic_type):
            query['TopicType'] = request.topic_type
        if not UtilClient.is_unset(request.where):
            query['Where'] = request.where
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateRule',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.UpdateRuleResponse(),
            self.call_api(params, req, runtime)
        )

    def update_rule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_rule_with_options(request, runtime)

    def update_rule_action_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.action_id):
            query['ActionId'] = request.action_id
        if not UtilClient.is_unset(request.configuration):
            query['Configuration'] = request.configuration
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateRuleAction',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.UpdateRuleActionResponse(),
            self.call_api(params, req, runtime)
        )

    def update_rule_action(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_rule_action_with_options(request, runtime)

    def update_scene_rule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.rule_content):
            query['RuleContent'] = request.rule_content
        if not UtilClient.is_unset(request.rule_description):
            query['RuleDescription'] = request.rule_description
        if not UtilClient.is_unset(request.rule_id):
            query['RuleId'] = request.rule_id
        if not UtilClient.is_unset(request.rule_name):
            query['RuleName'] = request.rule_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateSceneRule',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.UpdateSceneRuleResponse(),
            self.call_api(params, req, runtime)
        )

    def update_scene_rule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_scene_rule_with_options(request, runtime)

    def update_schedule_period_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.end_time):
            body['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.iot_instance_id):
            body['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.period_code):
            body['PeriodCode'] = request.period_code
        if not UtilClient.is_unset(request.sound_code_content):
            body['SoundCodeContent'] = request.sound_code_content
        if not UtilClient.is_unset(request.start_time):
            body['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateSchedulePeriod',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.UpdateSchedulePeriodResponse(),
            self.call_api(params, req, runtime)
        )

    def update_schedule_period(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_schedule_period_with_options(request, runtime)

    def update_sound_code_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.duration):
            body['Duration'] = request.duration
        if not UtilClient.is_unset(request.iot_instance_id):
            body['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.sound_code):
            body['SoundCode'] = request.sound_code
        if not UtilClient.is_unset(request.sound_code_content):
            body['SoundCodeContent'] = request.sound_code_content
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateSoundCode',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.UpdateSoundCodeResponse(),
            self.call_api(params, req, runtime)
        )

    def update_sound_code(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_sound_code_with_options(request, runtime)

    def update_sound_code_label_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.iot_instance_id):
            body['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.label):
            body['Label'] = request.label
        if not UtilClient.is_unset(request.sound_code):
            body['SoundCode'] = request.sound_code
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateSoundCodeLabel',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.UpdateSoundCodeLabelResponse(),
            self.call_api(params, req, runtime)
        )

    def update_sound_code_label(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_sound_code_label_with_options(request, runtime)

    def update_sound_code_schedule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.end_date):
            body['EndDate'] = request.end_date
        if not UtilClient.is_unset(request.end_time):
            body['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.iot_instance_id):
            body['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.schedule_code):
            body['ScheduleCode'] = request.schedule_code
        if not UtilClient.is_unset(request.start_date):
            body['StartDate'] = request.start_date
        if not UtilClient.is_unset(request.start_time):
            body['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateSoundCodeSchedule',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.UpdateSoundCodeScheduleResponse(),
            self.call_api(params, req, runtime)
        )

    def update_sound_code_schedule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_sound_code_schedule_with_options(request, runtime)

    def update_speech_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = iot_20180120_models.UpdateSpeechShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.sound_code_config):
            request.sound_code_config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.sound_code_config, 'SoundCodeConfig', 'json')
        body = {}
        if not UtilClient.is_unset(request.enable_sound_code):
            body['EnableSoundCode'] = request.enable_sound_code
        if not UtilClient.is_unset(request.iot_instance_id):
            body['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.project_code):
            body['ProjectCode'] = request.project_code
        if not UtilClient.is_unset(request.sound_code_config_shrink):
            body['SoundCodeConfig'] = request.sound_code_config_shrink
        if not UtilClient.is_unset(request.speech_code):
            body['SpeechCode'] = request.speech_code
        if not UtilClient.is_unset(request.speech_rate):
            body['SpeechRate'] = request.speech_rate
        if not UtilClient.is_unset(request.voice):
            body['Voice'] = request.voice
        if not UtilClient.is_unset(request.volume):
            body['Volume'] = request.volume
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateSpeech',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.UpdateSpeechResponse(),
            self.call_api(params, req, runtime)
        )

    def update_speech(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_speech_with_options(request, runtime)

    def update_subscribe_relation_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.consumer_group_ids):
            query['ConsumerGroupIds'] = request.consumer_group_ids
        if not UtilClient.is_unset(request.device_data_flag):
            query['DeviceDataFlag'] = request.device_data_flag
        if not UtilClient.is_unset(request.device_life_cycle_flag):
            query['DeviceLifeCycleFlag'] = request.device_life_cycle_flag
        if not UtilClient.is_unset(request.device_status_change_flag):
            query['DeviceStatusChangeFlag'] = request.device_status_change_flag
        if not UtilClient.is_unset(request.device_tag_flag):
            query['DeviceTagFlag'] = request.device_tag_flag
        if not UtilClient.is_unset(request.device_topo_life_cycle_flag):
            query['DeviceTopoLifeCycleFlag'] = request.device_topo_life_cycle_flag
        if not UtilClient.is_unset(request.found_device_list_flag):
            query['FoundDeviceListFlag'] = request.found_device_list_flag
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.mns_configuration):
            query['MnsConfiguration'] = request.mns_configuration
        if not UtilClient.is_unset(request.ota_event_flag):
            query['OtaEventFlag'] = request.ota_event_flag
        if not UtilClient.is_unset(request.ota_job_flag):
            query['OtaJobFlag'] = request.ota_job_flag
        if not UtilClient.is_unset(request.ota_version_flag):
            query['OtaVersionFlag'] = request.ota_version_flag
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        if not UtilClient.is_unset(request.thing_history_flag):
            query['ThingHistoryFlag'] = request.thing_history_flag
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateSubscribeRelation',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.UpdateSubscribeRelationResponse(),
            self.call_api(params, req, runtime)
        )

    def update_subscribe_relation(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_subscribe_relation_with_options(request, runtime)

    def update_thing_model_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.function_block_id):
            query['FunctionBlockId'] = request.function_block_id
        if not UtilClient.is_unset(request.function_block_name):
            query['FunctionBlockName'] = request.function_block_name
        if not UtilClient.is_unset(request.identifier):
            query['Identifier'] = request.identifier
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        if not UtilClient.is_unset(request.thing_model_json):
            query['ThingModelJson'] = request.thing_model_json
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateThingModel',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.UpdateThingModelResponse(),
            self.call_api(params, req, runtime)
        )

    def update_thing_model(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_thing_model_with_options(request, runtime)

    def update_thing_script_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        if not UtilClient.is_unset(request.script_content):
            query['ScriptContent'] = request.script_content
        if not UtilClient.is_unset(request.script_type):
            query['ScriptType'] = request.script_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateThingScript',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            iot_20180120_models.UpdateThingScriptResponse(),
            self.call_api(params, req, runtime)
        )

    def update_thing_script(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_thing_script_with_options(request, runtime)
