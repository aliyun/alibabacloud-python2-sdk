# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from Tea.core import TeaCore

from alibabacloud_tea_rpc.client import Client as RPCClient
from alibabacloud_iot20180120 import models as iot_20180120_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_rpc_util.client import Client as RPCUtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient


class Client(RPCClient):
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

    def add_data_for_api_source_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.AddDataForApiSourceResponse(),
            self.do_request('AddDataForApiSource', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def add_data_for_api_source(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_data_for_api_source_with_options(request, runtime)

    def add_share_task_device_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.AddShareTaskDeviceResponse(),
            self.do_request('AddShareTaskDevice', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def add_share_task_device(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_share_task_device_with_options(request, runtime)

    def attach_destination_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.AttachDestinationResponse(),
            self.do_request('AttachDestination', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def attach_destination(self, request):
        runtime = util_models.RuntimeOptions()
        return self.attach_destination_with_options(request, runtime)

    def attach_parser_data_source_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.AttachParserDataSourceResponse(),
            self.do_request('AttachParserDataSource', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def attach_parser_data_source(self, request):
        runtime = util_models.RuntimeOptions()
        return self.attach_parser_data_source_with_options(request, runtime)

    def batch_add_data_for_api_source_with_options(self, tmp, runtime):
        UtilClient.validate_model(tmp)
        request = iot_20180120_models.BatchAddDataForApiSourceShrinkRequest()
        RPCUtilClient.convert(tmp, request)
        if not UtilClient.is_unset(tmp.content_list):
            request.content_list_shrink = UtilClient.to_jsonstring(tmp.content_list)
        return TeaCore.from_map(
            iot_20180120_models.BatchAddDataForApiSourceResponse(),
            self.do_request('BatchAddDataForApiSource', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def batch_add_data_for_api_source(self, request):
        runtime = util_models.RuntimeOptions()
        return self.batch_add_data_for_api_source_with_options(request, runtime)

    def batch_add_device_group_relations_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.BatchAddDeviceGroupRelationsResponse(),
            self.do_request('BatchAddDeviceGroupRelations', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def batch_add_device_group_relations(self, request):
        runtime = util_models.RuntimeOptions()
        return self.batch_add_device_group_relations_with_options(request, runtime)

    def batch_add_thing_topo_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.BatchAddThingTopoResponse(),
            self.do_request('BatchAddThingTopo', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def batch_add_thing_topo(self, request):
        runtime = util_models.RuntimeOptions()
        return self.batch_add_thing_topo_with_options(request, runtime)

    def batch_bind_device_to_edge_instance_with_driver_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.BatchBindDeviceToEdgeInstanceWithDriverResponse(),
            self.do_request('BatchBindDeviceToEdgeInstanceWithDriver', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def batch_bind_device_to_edge_instance_with_driver(self, request):
        runtime = util_models.RuntimeOptions()
        return self.batch_bind_device_to_edge_instance_with_driver_with_options(request, runtime)

    def batch_bind_devices_into_project_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.BatchBindDevicesIntoProjectResponse(),
            self.do_request('BatchBindDevicesIntoProject', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def batch_bind_devices_into_project(self, request):
        runtime = util_models.RuntimeOptions()
        return self.batch_bind_devices_into_project_with_options(request, runtime)

    def batch_bind_products_into_project_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.BatchBindProductsIntoProjectResponse(),
            self.do_request('BatchBindProductsIntoProject', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def batch_bind_products_into_project(self, request):
        runtime = util_models.RuntimeOptions()
        return self.batch_bind_products_into_project_with_options(request, runtime)

    def batch_check_device_names_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.BatchCheckDeviceNamesResponse(),
            self.do_request('BatchCheckDeviceNames', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def batch_check_device_names(self, request):
        runtime = util_models.RuntimeOptions()
        return self.batch_check_device_names_with_options(request, runtime)

    def batch_check_import_device_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.BatchCheckImportDeviceResponse(),
            self.do_request('BatchCheckImportDevice', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def batch_check_import_device(self, request):
        runtime = util_models.RuntimeOptions()
        return self.batch_check_import_device_with_options(request, runtime)

    def batch_check_vehicle_device_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.BatchCheckVehicleDeviceResponse(),
            self.do_request('BatchCheckVehicleDevice', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def batch_check_vehicle_device(self, request):
        runtime = util_models.RuntimeOptions()
        return self.batch_check_vehicle_device_with_options(request, runtime)

    def batch_clear_edge_instance_device_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.BatchClearEdgeInstanceDeviceConfigResponse(),
            self.do_request('BatchClearEdgeInstanceDeviceConfig', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def batch_clear_edge_instance_device_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.batch_clear_edge_instance_device_config_with_options(request, runtime)

    def batch_create_sound_code_label_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.BatchCreateSoundCodeLabelResponse(),
            self.do_request('BatchCreateSoundCodeLabel', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def batch_create_sound_code_label(self, request):
        runtime = util_models.RuntimeOptions()
        return self.batch_create_sound_code_label_with_options(request, runtime)

    def batch_create_sound_code_label_with_labels_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.BatchCreateSoundCodeLabelWithLabelsResponse(),
            self.do_request('BatchCreateSoundCodeLabelWithLabels', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def batch_create_sound_code_label_with_labels(self, request):
        runtime = util_models.RuntimeOptions()
        return self.batch_create_sound_code_label_with_labels_with_options(request, runtime)

    def batch_delete_device_group_relations_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.BatchDeleteDeviceGroupRelationsResponse(),
            self.do_request('BatchDeleteDeviceGroupRelations', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def batch_delete_device_group_relations(self, request):
        runtime = util_models.RuntimeOptions()
        return self.batch_delete_device_group_relations_with_options(request, runtime)

    def batch_delete_edge_instance_channel_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.BatchDeleteEdgeInstanceChannelResponse(),
            self.do_request('BatchDeleteEdgeInstanceChannel', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def batch_delete_edge_instance_channel(self, request):
        runtime = util_models.RuntimeOptions()
        return self.batch_delete_edge_instance_channel_with_options(request, runtime)

    def batch_get_device_bind_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.BatchGetDeviceBindStatusResponse(),
            self.do_request('BatchGetDeviceBindStatus', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def batch_get_device_bind_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.batch_get_device_bind_status_with_options(request, runtime)

    def batch_get_device_state_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.BatchGetDeviceStateResponse(),
            self.do_request('BatchGetDeviceState', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def batch_get_device_state(self, request):
        runtime = util_models.RuntimeOptions()
        return self.batch_get_device_state_with_options(request, runtime)

    def batch_get_edge_driver_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.BatchGetEdgeDriverResponse(),
            self.do_request('BatchGetEdgeDriver', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def batch_get_edge_driver(self, request):
        runtime = util_models.RuntimeOptions()
        return self.batch_get_edge_driver_with_options(request, runtime)

    def batch_get_edge_instance_channel_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.BatchGetEdgeInstanceChannelResponse(),
            self.do_request('BatchGetEdgeInstanceChannel', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def batch_get_edge_instance_channel(self, request):
        runtime = util_models.RuntimeOptions()
        return self.batch_get_edge_instance_channel_with_options(request, runtime)

    def batch_get_edge_instance_device_channel_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.BatchGetEdgeInstanceDeviceChannelResponse(),
            self.do_request('BatchGetEdgeInstanceDeviceChannel', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def batch_get_edge_instance_device_channel(self, request):
        runtime = util_models.RuntimeOptions()
        return self.batch_get_edge_instance_device_channel_with_options(request, runtime)

    def batch_get_edge_instance_device_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.BatchGetEdgeInstanceDeviceConfigResponse(),
            self.do_request('BatchGetEdgeInstanceDeviceConfig', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def batch_get_edge_instance_device_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.batch_get_edge_instance_device_config_with_options(request, runtime)

    def batch_get_edge_instance_device_driver_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.BatchGetEdgeInstanceDeviceDriverResponse(),
            self.do_request('BatchGetEdgeInstanceDeviceDriver', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def batch_get_edge_instance_device_driver(self, request):
        runtime = util_models.RuntimeOptions()
        return self.batch_get_edge_instance_device_driver_with_options(request, runtime)

    def batch_get_edge_instance_driver_configs_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.BatchGetEdgeInstanceDriverConfigsResponse(),
            self.do_request('BatchGetEdgeInstanceDriverConfigs', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def batch_get_edge_instance_driver_configs(self, request):
        runtime = util_models.RuntimeOptions()
        return self.batch_get_edge_instance_driver_configs_with_options(request, runtime)

    def batch_import_device_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.BatchImportDeviceResponse(),
            self.do_request('BatchImportDevice', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def batch_import_device(self, request):
        runtime = util_models.RuntimeOptions()
        return self.batch_import_device_with_options(request, runtime)

    def batch_import_vehicle_device_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.BatchImportVehicleDeviceResponse(),
            self.do_request('BatchImportVehicleDevice', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def batch_import_vehicle_device(self, request):
        runtime = util_models.RuntimeOptions()
        return self.batch_import_vehicle_device_with_options(request, runtime)

    def batch_pub_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.BatchPubResponse(),
            self.do_request('BatchPub', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def batch_pub(self, request):
        runtime = util_models.RuntimeOptions()
        return self.batch_pub_with_options(request, runtime)

    def batch_query_device_detail_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.BatchQueryDeviceDetailResponse(),
            self.do_request('BatchQueryDeviceDetail', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def batch_query_device_detail(self, request):
        runtime = util_models.RuntimeOptions()
        return self.batch_query_device_detail_with_options(request, runtime)

    def batch_register_device_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.BatchRegisterDeviceResponse(),
            self.do_request('BatchRegisterDevice', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def batch_register_device(self, request):
        runtime = util_models.RuntimeOptions()
        return self.batch_register_device_with_options(request, runtime)

    def batch_register_device_with_apply_id_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.BatchRegisterDeviceWithApplyIdResponse(),
            self.do_request('BatchRegisterDeviceWithApplyId', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def batch_register_device_with_apply_id(self, request):
        runtime = util_models.RuntimeOptions()
        return self.batch_register_device_with_apply_id_with_options(request, runtime)

    def batch_set_edge_instance_device_channel_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.BatchSetEdgeInstanceDeviceChannelResponse(),
            self.do_request('BatchSetEdgeInstanceDeviceChannel', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def batch_set_edge_instance_device_channel(self, request):
        runtime = util_models.RuntimeOptions()
        return self.batch_set_edge_instance_device_channel_with_options(request, runtime)

    def batch_set_edge_instance_device_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.BatchSetEdgeInstanceDeviceConfigResponse(),
            self.do_request('BatchSetEdgeInstanceDeviceConfig', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def batch_set_edge_instance_device_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.batch_set_edge_instance_device_config_with_options(request, runtime)

    def batch_unbind_device_from_edge_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.BatchUnbindDeviceFromEdgeInstanceResponse(),
            self.do_request('BatchUnbindDeviceFromEdgeInstance', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def batch_unbind_device_from_edge_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.batch_unbind_device_from_edge_instance_with_options(request, runtime)

    def batch_unbind_project_devices_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.BatchUnbindProjectDevicesResponse(),
            self.do_request('BatchUnbindProjectDevices', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def batch_unbind_project_devices(self, request):
        runtime = util_models.RuntimeOptions()
        return self.batch_unbind_project_devices_with_options(request, runtime)

    def batch_unbind_project_products_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.BatchUnbindProjectProductsResponse(),
            self.do_request('BatchUnbindProjectProducts', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def batch_unbind_project_products(self, request):
        runtime = util_models.RuntimeOptions()
        return self.batch_unbind_project_products_with_options(request, runtime)

    def batch_update_device_nickname_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.BatchUpdateDeviceNicknameResponse(),
            self.do_request('BatchUpdateDeviceNickname', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def batch_update_device_nickname(self, request):
        runtime = util_models.RuntimeOptions()
        return self.batch_update_device_nickname_with_options(request, runtime)

    def bind_application_to_edge_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.BindApplicationToEdgeInstanceResponse(),
            self.do_request('BindApplicationToEdgeInstance', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def bind_application_to_edge_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.bind_application_to_edge_instance_with_options(request, runtime)

    def bind_driver_to_edge_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.BindDriverToEdgeInstanceResponse(),
            self.do_request('BindDriverToEdgeInstance', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def bind_driver_to_edge_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.bind_driver_to_edge_instance_with_options(request, runtime)

    def bind_gateway_to_edge_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.BindGatewayToEdgeInstanceResponse(),
            self.do_request('BindGatewayToEdgeInstance', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def bind_gateway_to_edge_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.bind_gateway_to_edge_instance_with_options(request, runtime)

    def bind_license_device_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.BindLicenseDeviceResponse(),
            self.do_request('BindLicenseDevice', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def bind_license_device(self, request):
        runtime = util_models.RuntimeOptions()
        return self.bind_license_device_with_options(request, runtime)

    def bind_license_product_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.BindLicenseProductResponse(),
            self.do_request('BindLicenseProduct', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def bind_license_product(self, request):
        runtime = util_models.RuntimeOptions()
        return self.bind_license_product_with_options(request, runtime)

    def bind_role_to_edge_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.BindRoleToEdgeInstanceResponse(),
            self.do_request('BindRoleToEdgeInstance', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def bind_role_to_edge_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.bind_role_to_edge_instance_with_options(request, runtime)

    def bind_scene_rule_to_edge_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.BindSceneRuleToEdgeInstanceResponse(),
            self.do_request('BindSceneRuleToEdgeInstance', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def bind_scene_rule_to_edge_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.bind_scene_rule_to_edge_instance_with_options(request, runtime)

    def cancel_job_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.CancelJobResponse(),
            self.do_request('CancelJob', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def cancel_job(self, request):
        runtime = util_models.RuntimeOptions()
        return self.cancel_job_with_options(request, runtime)

    def cancel_otastrategy_by_job_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.CancelOTAStrategyByJobResponse(),
            self.do_request('CancelOTAStrategyByJob', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def cancel_otastrategy_by_job(self, request):
        runtime = util_models.RuntimeOptions()
        return self.cancel_otastrategy_by_job_with_options(request, runtime)

    def cancel_otatask_by_device_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.CancelOTATaskByDeviceResponse(),
            self.do_request('CancelOTATaskByDevice', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def cancel_otatask_by_device(self, request):
        runtime = util_models.RuntimeOptions()
        return self.cancel_otatask_by_device_with_options(request, runtime)

    def cancel_otatask_by_job_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.CancelOTATaskByJobResponse(),
            self.do_request('CancelOTATaskByJob', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def cancel_otatask_by_job(self, request):
        runtime = util_models.RuntimeOptions()
        return self.cancel_otatask_by_job_with_options(request, runtime)

    def cancel_release_product_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.CancelReleaseProductResponse(),
            self.do_request('CancelReleaseProduct', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def cancel_release_product(self, request):
        runtime = util_models.RuntimeOptions()
        return self.cancel_release_product_with_options(request, runtime)

    def check_bind_license_device_progress_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.CheckBindLicenseDeviceProgressResponse(),
            self.do_request('CheckBindLicenseDeviceProgress', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def check_bind_license_device_progress(self, request):
        runtime = util_models.RuntimeOptions()
        return self.check_bind_license_device_progress_with_options(request, runtime)

    def clear_device_desired_property_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.ClearDeviceDesiredPropertyResponse(),
            self.do_request('ClearDeviceDesiredProperty', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def clear_device_desired_property(self, request):
        runtime = util_models.RuntimeOptions()
        return self.clear_device_desired_property_with_options(request, runtime)

    def clear_edge_instance_driver_configs_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.ClearEdgeInstanceDriverConfigsResponse(),
            self.do_request('ClearEdgeInstanceDriverConfigs', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def clear_edge_instance_driver_configs(self, request):
        runtime = util_models.RuntimeOptions()
        return self.clear_edge_instance_driver_configs_with_options(request, runtime)

    def close_device_tunnel_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.CloseDeviceTunnelResponse(),
            self.do_request('CloseDeviceTunnel', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def close_device_tunnel(self, request):
        runtime = util_models.RuntimeOptions()
        return self.close_device_tunnel_with_options(request, runtime)

    def close_edge_instance_deployment_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.CloseEdgeInstanceDeploymentResponse(),
            self.do_request('CloseEdgeInstanceDeployment', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def close_edge_instance_deployment(self, request):
        runtime = util_models.RuntimeOptions()
        return self.close_edge_instance_deployment_with_options(request, runtime)

    def confirm_otatask_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.ConfirmOTATaskResponse(),
            self.do_request('ConfirmOTATask', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def confirm_otatask(self, request):
        runtime = util_models.RuntimeOptions()
        return self.confirm_otatask_with_options(request, runtime)

    def copy_thing_model_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.CopyThingModelResponse(),
            self.do_request('CopyThingModel', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def copy_thing_model(self, request):
        runtime = util_models.RuntimeOptions()
        return self.copy_thing_model_with_options(request, runtime)

    def count_speech_broadcast_hour_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.CountSpeechBroadcastHourResponse(),
            self.do_request('CountSpeechBroadcastHour', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def count_speech_broadcast_hour(self, request):
        runtime = util_models.RuntimeOptions()
        return self.count_speech_broadcast_hour_with_options(request, runtime)

    def create_consumer_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.CreateConsumerGroupResponse(),
            self.do_request('CreateConsumerGroup', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def create_consumer_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_consumer_group_with_options(request, runtime)

    def create_consumer_group_subscribe_relation_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.CreateConsumerGroupSubscribeRelationResponse(),
            self.do_request('CreateConsumerGroupSubscribeRelation', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def create_consumer_group_subscribe_relation(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_consumer_group_subscribe_relation_with_options(request, runtime)

    def create_data_apiservice_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.CreateDataAPIServiceResponse(),
            self.do_request('CreateDataAPIService', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def create_data_apiservice(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_data_apiservice_with_options(request, runtime)

    def create_data_source_item_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.CreateDataSourceItemResponse(),
            self.do_request('CreateDataSourceItem', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def create_data_source_item(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_data_source_item_with_options(request, runtime)

    def create_destination_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.CreateDestinationResponse(),
            self.do_request('CreateDestination', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def create_destination(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_destination_with_options(request, runtime)

    def create_device_distribute_job_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.CreateDeviceDistributeJobResponse(),
            self.do_request('CreateDeviceDistributeJob', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def create_device_distribute_job(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_device_distribute_job_with_options(request, runtime)

    def create_device_dynamic_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.CreateDeviceDynamicGroupResponse(),
            self.do_request('CreateDeviceDynamicGroup', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def create_device_dynamic_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_device_dynamic_group_with_options(request, runtime)

    def create_device_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.CreateDeviceGroupResponse(),
            self.do_request('CreateDeviceGroup', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def create_device_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_device_group_with_options(request, runtime)

    def create_device_tunnel_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.CreateDeviceTunnelResponse(),
            self.do_request('CreateDeviceTunnel', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def create_device_tunnel(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_device_tunnel_with_options(request, runtime)

    def create_download_data_job_with_options(self, tmp, runtime):
        UtilClient.validate_model(tmp)
        request = iot_20180120_models.CreateDownloadDataJobShrinkRequest()
        RPCUtilClient.convert(tmp, request)
        if not UtilClient.is_unset(tmp.context):
            request.context_shrink = UtilClient.to_jsonstring(tmp.context)
        if not UtilClient.is_unset(tmp.file_config):
            request.file_config_shrink = UtilClient.to_jsonstring(tmp.file_config)
        return TeaCore.from_map(
            iot_20180120_models.CreateDownloadDataJobResponse(),
            self.do_request('CreateDownloadDataJob', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def create_download_data_job(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_download_data_job_with_options(request, runtime)

    def create_edge_driver_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.CreateEdgeDriverResponse(),
            self.do_request('CreateEdgeDriver', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def create_edge_driver(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_edge_driver_with_options(request, runtime)

    def create_edge_driver_version_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.CreateEdgeDriverVersionResponse(),
            self.do_request('CreateEdgeDriverVersion', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def create_edge_driver_version(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_edge_driver_version_with_options(request, runtime)

    def create_edge_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.CreateEdgeInstanceResponse(),
            self.do_request('CreateEdgeInstance', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def create_edge_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_edge_instance_with_options(request, runtime)

    def create_edge_instance_channel_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.CreateEdgeInstanceChannelResponse(),
            self.do_request('CreateEdgeInstanceChannel', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def create_edge_instance_channel(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_edge_instance_channel_with_options(request, runtime)

    def create_edge_instance_deployment_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.CreateEdgeInstanceDeploymentResponse(),
            self.do_request('CreateEdgeInstanceDeployment', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def create_edge_instance_deployment(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_edge_instance_deployment_with_options(request, runtime)

    def create_edge_instance_message_routing_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.CreateEdgeInstanceMessageRoutingResponse(),
            self.do_request('CreateEdgeInstanceMessageRouting', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def create_edge_instance_message_routing(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_edge_instance_message_routing_with_options(request, runtime)

    def create_edge_oss_pre_signed_address_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.CreateEdgeOssPreSignedAddressResponse(),
            self.do_request('CreateEdgeOssPreSignedAddress', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def create_edge_oss_pre_signed_address(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_edge_oss_pre_signed_address_with_options(request, runtime)

    def create_job_with_options(self, tmp, runtime):
        UtilClient.validate_model(tmp)
        request = iot_20180120_models.CreateJobShrinkRequest()
        RPCUtilClient.convert(tmp, request)
        if not UtilClient.is_unset(tmp.job_file):
            request.job_file_shrink = UtilClient.to_jsonstring(tmp.job_file)
        if not UtilClient.is_unset(tmp.rollout_config):
            request.rollout_config_shrink = UtilClient.to_jsonstring(tmp.rollout_config)
        if not UtilClient.is_unset(tmp.target_config):
            request.target_config_shrink = UtilClient.to_jsonstring(tmp.target_config)
        if not UtilClient.is_unset(tmp.timeout_config):
            request.timeout_config_shrink = UtilClient.to_jsonstring(tmp.timeout_config)
        return TeaCore.from_map(
            iot_20180120_models.CreateJobResponse(),
            self.do_request('CreateJob', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def create_job(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_job_with_options(request, runtime)

    def create_lo_ra_nodes_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.CreateLoRaNodesTaskResponse(),
            self.do_request('CreateLoRaNodesTask', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def create_lo_ra_nodes_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_lo_ra_nodes_task_with_options(request, runtime)

    def create_otadynamic_upgrade_job_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.CreateOTADynamicUpgradeJobResponse(),
            self.do_request('CreateOTADynamicUpgradeJob', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def create_otadynamic_upgrade_job(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_otadynamic_upgrade_job_with_options(request, runtime)

    def create_otafirmware_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.CreateOTAFirmwareResponse(),
            self.do_request('CreateOTAFirmware', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def create_otafirmware(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_otafirmware_with_options(request, runtime)

    def create_otamodule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.CreateOTAModuleResponse(),
            self.do_request('CreateOTAModule', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def create_otamodule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_otamodule_with_options(request, runtime)

    def create_otastatic_upgrade_job_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.CreateOTAStaticUpgradeJobResponse(),
            self.do_request('CreateOTAStaticUpgradeJob', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def create_otastatic_upgrade_job(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_otastatic_upgrade_job_with_options(request, runtime)

    def create_otaverify_job_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.CreateOTAVerifyJobResponse(),
            self.do_request('CreateOTAVerifyJob', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def create_otaverify_job(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_otaverify_job_with_options(request, runtime)

    def create_parser_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.CreateParserResponse(),
            self.do_request('CreateParser', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def create_parser(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_parser_with_options(request, runtime)

    def create_parser_data_source_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.CreateParserDataSourceResponse(),
            self.do_request('CreateParserDataSource', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def create_parser_data_source(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_parser_data_source_with_options(request, runtime)

    def create_product_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.CreateProductResponse(),
            self.do_request('CreateProduct', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def create_product(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_product_with_options(request, runtime)

    def create_product_distribute_job_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.CreateProductDistributeJobResponse(),
            self.do_request('CreateProductDistributeJob', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def create_product_distribute_job(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_product_distribute_job_with_options(request, runtime)

    def create_product_tags_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.CreateProductTagsResponse(),
            self.do_request('CreateProductTags', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def create_product_tags(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_product_tags_with_options(request, runtime)

    def create_product_topic_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.CreateProductTopicResponse(),
            self.do_request('CreateProductTopic', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def create_product_topic(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_product_topic_with_options(request, runtime)

    def create_rule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.CreateRuleResponse(),
            self.do_request('CreateRule', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def create_rule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_rule_with_options(request, runtime)

    def create_rule_action_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.CreateRuleActionResponse(),
            self.do_request('CreateRuleAction', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def create_rule_action(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_rule_action_with_options(request, runtime)

    def create_scene_rule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.CreateSceneRuleResponse(),
            self.do_request('CreateSceneRule', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def create_scene_rule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_scene_rule_with_options(request, runtime)

    def create_schedule_period_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.CreateSchedulePeriodResponse(),
            self.do_request('CreateSchedulePeriod', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def create_schedule_period(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_schedule_period_with_options(request, runtime)

    def create_sound_code_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.CreateSoundCodeResponse(),
            self.do_request('CreateSoundCode', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def create_sound_code(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_sound_code_with_options(request, runtime)

    def create_sound_code_label_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.CreateSoundCodeLabelResponse(),
            self.do_request('CreateSoundCodeLabel', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def create_sound_code_label(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_sound_code_label_with_options(request, runtime)

    def create_sound_code_schedule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.CreateSoundCodeScheduleResponse(),
            self.do_request('CreateSoundCodeSchedule', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def create_sound_code_schedule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_sound_code_schedule_with_options(request, runtime)

    def create_speech_with_options(self, tmp, runtime):
        UtilClient.validate_model(tmp)
        request = iot_20180120_models.CreateSpeechShrinkRequest()
        RPCUtilClient.convert(tmp, request)
        if not UtilClient.is_unset(tmp.sound_code_config):
            request.sound_code_config_shrink = UtilClient.to_jsonstring(tmp.sound_code_config)
        return TeaCore.from_map(
            iot_20180120_models.CreateSpeechResponse(),
            self.do_request('CreateSpeech', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def create_speech(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_speech_with_options(request, runtime)

    def create_studio_app_domain_open_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.CreateStudioAppDomainOpenResponse(),
            self.do_request('CreateStudioAppDomainOpen', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def create_studio_app_domain_open(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_studio_app_domain_open_with_options(request, runtime)

    def create_subscribe_relation_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.CreateSubscribeRelationResponse(),
            self.do_request('CreateSubscribeRelation', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def create_subscribe_relation(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_subscribe_relation_with_options(request, runtime)

    def create_thing_model_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.CreateThingModelResponse(),
            self.do_request('CreateThingModel', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def create_thing_model(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_thing_model_with_options(request, runtime)

    def create_thing_script_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.CreateThingScriptResponse(),
            self.do_request('CreateThingScript', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def create_thing_script(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_thing_script_with_options(request, runtime)

    def create_topic_route_table_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.CreateTopicRouteTableResponse(),
            self.do_request('CreateTopicRouteTable', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def create_topic_route_table(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_topic_route_table_with_options(request, runtime)

    def delete_client_ids_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.DeleteClientIdsResponse(),
            self.do_request('DeleteClientIds', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def delete_client_ids(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_client_ids_with_options(request, runtime)

    def delete_consumer_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.DeleteConsumerGroupResponse(),
            self.do_request('DeleteConsumerGroup', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def delete_consumer_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_consumer_group_with_options(request, runtime)

    def delete_consumer_group_subscribe_relation_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.DeleteConsumerGroupSubscribeRelationResponse(),
            self.do_request('DeleteConsumerGroupSubscribeRelation', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def delete_consumer_group_subscribe_relation(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_consumer_group_subscribe_relation_with_options(request, runtime)

    def delete_data_source_item_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.DeleteDataSourceItemResponse(),
            self.do_request('DeleteDataSourceItem', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def delete_data_source_item(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_data_source_item_with_options(request, runtime)

    def delete_destination_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.DeleteDestinationResponse(),
            self.do_request('DeleteDestination', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def delete_destination(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_destination_with_options(request, runtime)

    def delete_device_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.DeleteDeviceResponse(),
            self.do_request('DeleteDevice', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def delete_device(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_device_with_options(request, runtime)

    def delete_device_distribute_job_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.DeleteDeviceDistributeJobResponse(),
            self.do_request('DeleteDeviceDistributeJob', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def delete_device_distribute_job(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_device_distribute_job_with_options(request, runtime)

    def delete_device_dynamic_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.DeleteDeviceDynamicGroupResponse(),
            self.do_request('DeleteDeviceDynamicGroup', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def delete_device_dynamic_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_device_dynamic_group_with_options(request, runtime)

    def delete_device_file_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.DeleteDeviceFileResponse(),
            self.do_request('DeleteDeviceFile', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def delete_device_file(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_device_file_with_options(request, runtime)

    def delete_device_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.DeleteDeviceGroupResponse(),
            self.do_request('DeleteDeviceGroup', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def delete_device_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_device_group_with_options(request, runtime)

    def delete_device_prop_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.DeleteDevicePropResponse(),
            self.do_request('DeleteDeviceProp', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def delete_device_prop(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_device_prop_with_options(request, runtime)

    def delete_device_speech_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.DeleteDeviceSpeechResponse(),
            self.do_request('DeleteDeviceSpeech', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def delete_device_speech(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_device_speech_with_options(request, runtime)

    def delete_device_tunnel_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.DeleteDeviceTunnelResponse(),
            self.do_request('DeleteDeviceTunnel', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def delete_device_tunnel(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_device_tunnel_with_options(request, runtime)

    def delete_edge_driver_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.DeleteEdgeDriverResponse(),
            self.do_request('DeleteEdgeDriver', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def delete_edge_driver(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_edge_driver_with_options(request, runtime)

    def delete_edge_driver_version_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.DeleteEdgeDriverVersionResponse(),
            self.do_request('DeleteEdgeDriverVersion', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def delete_edge_driver_version(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_edge_driver_version_with_options(request, runtime)

    def delete_edge_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.DeleteEdgeInstanceResponse(),
            self.do_request('DeleteEdgeInstance', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def delete_edge_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_edge_instance_with_options(request, runtime)

    def delete_edge_instance_message_routing_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.DeleteEdgeInstanceMessageRoutingResponse(),
            self.do_request('DeleteEdgeInstanceMessageRouting', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def delete_edge_instance_message_routing(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_edge_instance_message_routing_with_options(request, runtime)

    def delete_job_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.DeleteJobResponse(),
            self.do_request('DeleteJob', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def delete_job(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_job_with_options(request, runtime)

    def delete_otafirmware_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.DeleteOTAFirmwareResponse(),
            self.do_request('DeleteOTAFirmware', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def delete_otafirmware(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_otafirmware_with_options(request, runtime)

    def delete_otamodule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.DeleteOTAModuleResponse(),
            self.do_request('DeleteOTAModule', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def delete_otamodule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_otamodule_with_options(request, runtime)

    def delete_parser_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.DeleteParserResponse(),
            self.do_request('DeleteParser', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def delete_parser(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_parser_with_options(request, runtime)

    def delete_parser_data_source_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.DeleteParserDataSourceResponse(),
            self.do_request('DeleteParserDataSource', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def delete_parser_data_source(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_parser_data_source_with_options(request, runtime)

    def delete_product_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.DeleteProductResponse(),
            self.do_request('DeleteProduct', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def delete_product(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_product_with_options(request, runtime)

    def delete_product_tags_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.DeleteProductTagsResponse(),
            self.do_request('DeleteProductTags', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def delete_product_tags(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_product_tags_with_options(request, runtime)

    def delete_product_topic_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.DeleteProductTopicResponse(),
            self.do_request('DeleteProductTopic', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def delete_product_topic(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_product_topic_with_options(request, runtime)

    def delete_rule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.DeleteRuleResponse(),
            self.do_request('DeleteRule', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def delete_rule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_rule_with_options(request, runtime)

    def delete_rule_action_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.DeleteRuleActionResponse(),
            self.do_request('DeleteRuleAction', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def delete_rule_action(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_rule_action_with_options(request, runtime)

    def delete_scene_rule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.DeleteSceneRuleResponse(),
            self.do_request('DeleteSceneRule', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def delete_scene_rule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_scene_rule_with_options(request, runtime)

    def delete_schedule_period_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.DeleteSchedulePeriodResponse(),
            self.do_request('DeleteSchedulePeriod', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def delete_schedule_period(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_schedule_period_with_options(request, runtime)

    def delete_share_task_device_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.DeleteShareTaskDeviceResponse(),
            self.do_request('DeleteShareTaskDevice', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def delete_share_task_device(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_share_task_device_with_options(request, runtime)

    def delete_sound_code_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.DeleteSoundCodeResponse(),
            self.do_request('DeleteSoundCode', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def delete_sound_code(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_sound_code_with_options(request, runtime)

    def delete_sound_code_label_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.DeleteSoundCodeLabelResponse(),
            self.do_request('DeleteSoundCodeLabel', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def delete_sound_code_label(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_sound_code_label_with_options(request, runtime)

    def delete_sound_code_schedule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.DeleteSoundCodeScheduleResponse(),
            self.do_request('DeleteSoundCodeSchedule', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def delete_sound_code_schedule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_sound_code_schedule_with_options(request, runtime)

    def delete_speech_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.DeleteSpeechResponse(),
            self.do_request('DeleteSpeech', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def delete_speech(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_speech_with_options(request, runtime)

    def delete_studio_app_domain_open_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.DeleteStudioAppDomainOpenResponse(),
            self.do_request('DeleteStudioAppDomainOpen', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def delete_studio_app_domain_open(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_studio_app_domain_open_with_options(request, runtime)

    def delete_subscribe_relation_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.DeleteSubscribeRelationResponse(),
            self.do_request('DeleteSubscribeRelation', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def delete_subscribe_relation(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_subscribe_relation_with_options(request, runtime)

    def delete_thing_model_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.DeleteThingModelResponse(),
            self.do_request('DeleteThingModel', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def delete_thing_model(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_thing_model_with_options(request, runtime)

    def delete_topic_route_table_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.DeleteTopicRouteTableResponse(),
            self.do_request('DeleteTopicRouteTable', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def delete_topic_route_table(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_topic_route_table_with_options(request, runtime)

    def detach_destination_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.DetachDestinationResponse(),
            self.do_request('DetachDestination', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def detach_destination(self, request):
        runtime = util_models.RuntimeOptions()
        return self.detach_destination_with_options(request, runtime)

    def detach_parser_data_source_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.DetachParserDataSourceResponse(),
            self.do_request('DetachParserDataSource', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def detach_parser_data_source(self, request):
        runtime = util_models.RuntimeOptions()
        return self.detach_parser_data_source_with_options(request, runtime)

    def disable_device_tunnel_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.DisableDeviceTunnelResponse(),
            self.do_request('DisableDeviceTunnel', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def disable_device_tunnel(self, request):
        runtime = util_models.RuntimeOptions()
        return self.disable_device_tunnel_with_options(request, runtime)

    def disable_device_tunnel_share_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.DisableDeviceTunnelShareResponse(),
            self.do_request('DisableDeviceTunnelShare', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def disable_device_tunnel_share(self, request):
        runtime = util_models.RuntimeOptions()
        return self.disable_device_tunnel_share_with_options(request, runtime)

    def disable_scene_rule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.DisableSceneRuleResponse(),
            self.do_request('DisableSceneRule', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def disable_scene_rule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.disable_scene_rule_with_options(request, runtime)

    def disable_thing_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.DisableThingResponse(),
            self.do_request('DisableThing', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def disable_thing(self, request):
        runtime = util_models.RuntimeOptions()
        return self.disable_thing_with_options(request, runtime)

    def enable_device_tunnel_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.EnableDeviceTunnelResponse(),
            self.do_request('EnableDeviceTunnel', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def enable_device_tunnel(self, request):
        runtime = util_models.RuntimeOptions()
        return self.enable_device_tunnel_with_options(request, runtime)

    def enable_device_tunnel_share_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.EnableDeviceTunnelShareResponse(),
            self.do_request('EnableDeviceTunnelShare', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def enable_device_tunnel_share(self, request):
        runtime = util_models.RuntimeOptions()
        return self.enable_device_tunnel_share_with_options(request, runtime)

    def enable_scene_rule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.EnableSceneRuleResponse(),
            self.do_request('EnableSceneRule', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def enable_scene_rule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.enable_scene_rule_with_options(request, runtime)

    def enable_thing_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.EnableThingResponse(),
            self.do_request('EnableThing', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def enable_thing(self, request):
        runtime = util_models.RuntimeOptions()
        return self.enable_thing_with_options(request, runtime)

    def generate_device_name_list_urlwith_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.GenerateDeviceNameListURLResponse(),
            self.do_request('GenerateDeviceNameListURL', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def generate_device_name_list_url(self, request):
        runtime = util_models.RuntimeOptions()
        return self.generate_device_name_list_urlwith_options(request, runtime)

    def generate_file_upload_urlwith_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.GenerateFileUploadURLResponse(),
            self.do_request('GenerateFileUploadURL', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def generate_file_upload_url(self, request):
        runtime = util_models.RuntimeOptions()
        return self.generate_file_upload_urlwith_options(request, runtime)

    def generate_otaupload_urlwith_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.GenerateOTAUploadURLResponse(),
            self.do_request('GenerateOTAUploadURL', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def generate_otaupload_url(self, request):
        runtime = util_models.RuntimeOptions()
        return self.generate_otaupload_urlwith_options(request, runtime)

    def get_data_apiservice_detail_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.GetDataAPIServiceDetailResponse(),
            self.do_request('GetDataAPIServiceDetail', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def get_data_apiservice_detail(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_data_apiservice_detail_with_options(request, runtime)

    def get_destination_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.GetDestinationResponse(),
            self.do_request('GetDestination', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def get_destination(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_destination_with_options(request, runtime)

    def get_device_shadow_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.GetDeviceShadowResponse(),
            self.do_request('GetDeviceShadow', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def get_device_shadow(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_device_shadow_with_options(request, runtime)

    def get_device_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.GetDeviceStatusResponse(),
            self.do_request('GetDeviceStatus', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def get_device_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_device_status_with_options(request, runtime)

    def get_device_tunnel_share_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.GetDeviceTunnelShareStatusResponse(),
            self.do_request('GetDeviceTunnelShareStatus', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def get_device_tunnel_share_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_device_tunnel_share_status_with_options(request, runtime)

    def get_device_tunnel_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.GetDeviceTunnelStatusResponse(),
            self.do_request('GetDeviceTunnelStatus', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def get_device_tunnel_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_device_tunnel_status_with_options(request, runtime)

    def get_download_file_with_options(self, tmp, runtime):
        UtilClient.validate_model(tmp)
        request = iot_20180120_models.GetDownloadFileShrinkRequest()
        RPCUtilClient.convert(tmp, request)
        if not UtilClient.is_unset(tmp.context):
            request.context_shrink = UtilClient.to_jsonstring(tmp.context)
        return TeaCore.from_map(
            iot_20180120_models.GetDownloadFileResponse(),
            self.do_request('GetDownloadFile', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def get_download_file(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_download_file_with_options(request, runtime)

    def get_edge_driver_version_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.GetEdgeDriverVersionResponse(),
            self.do_request('GetEdgeDriverVersion', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def get_edge_driver_version(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_edge_driver_version_with_options(request, runtime)

    def get_edge_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.GetEdgeInstanceResponse(),
            self.do_request('GetEdgeInstance', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def get_edge_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_edge_instance_with_options(request, runtime)

    def get_edge_instance_deployment_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.GetEdgeInstanceDeploymentResponse(),
            self.do_request('GetEdgeInstanceDeployment', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def get_edge_instance_deployment(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_edge_instance_deployment_with_options(request, runtime)

    def get_edge_instance_message_routing_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.GetEdgeInstanceMessageRoutingResponse(),
            self.do_request('GetEdgeInstanceMessageRouting', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def get_edge_instance_message_routing(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_edge_instance_message_routing_with_options(request, runtime)

    def get_gateway_by_sub_device_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.GetGatewayBySubDeviceResponse(),
            self.do_request('GetGatewayBySubDevice', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def get_gateway_by_sub_device(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_gateway_by_sub_device_with_options(request, runtime)

    def get_lora_nodes_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.GetLoraNodesTaskResponse(),
            self.do_request('GetLoraNodesTask', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def get_lora_nodes_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_lora_nodes_task_with_options(request, runtime)

    def get_parser_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.GetParserResponse(),
            self.do_request('GetParser', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def get_parser(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_parser_with_options(request, runtime)

    def get_parser_data_source_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.GetParserDataSourceResponse(),
            self.do_request('GetParserDataSource', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def get_parser_data_source(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_parser_data_source_with_options(request, runtime)

    def get_rule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.GetRuleResponse(),
            self.do_request('GetRule', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def get_rule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_rule_with_options(request, runtime)

    def get_rule_action_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.GetRuleActionResponse(),
            self.do_request('GetRuleAction', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def get_rule_action(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_rule_action_with_options(request, runtime)

    def get_scene_rule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.GetSceneRuleResponse(),
            self.do_request('GetSceneRule', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def get_scene_rule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_scene_rule_with_options(request, runtime)

    def get_share_task_by_device_open_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.GetShareTaskByDeviceOpenResponse(),
            self.do_request('GetShareTaskByDeviceOpen', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def get_share_task_by_device_open(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_share_task_by_device_open_with_options(request, runtime)

    def get_sound_code_audio_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.GetSoundCodeAudioResponse(),
            self.do_request('GetSoundCodeAudio', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def get_sound_code_audio(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_sound_code_audio_with_options(request, runtime)

    def get_sound_code_schedule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.GetSoundCodeScheduleResponse(),
            self.do_request('GetSoundCodeSchedule', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def get_sound_code_schedule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_sound_code_schedule_with_options(request, runtime)

    def get_speech_device_detail_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.GetSpeechDeviceDetailResponse(),
            self.do_request('GetSpeechDeviceDetail', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def get_speech_device_detail(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_speech_device_detail_with_options(request, runtime)

    def get_speech_license_device_statistics_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.GetSpeechLicenseDeviceStatisticsResponse(),
            self.do_request('GetSpeechLicenseDeviceStatistics', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def get_speech_license_device_statistics(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_speech_license_device_statistics_with_options(request, runtime)

    def get_speech_voice_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.GetSpeechVoiceResponse(),
            self.do_request('GetSpeechVoice', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def get_speech_voice(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_speech_voice_with_options(request, runtime)

    def get_studio_app_token_open_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.GetStudioAppTokenOpenResponse(),
            self.do_request('GetStudioAppTokenOpen', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def get_studio_app_token_open(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_studio_app_token_open_with_options(request, runtime)

    def get_thing_model_tsl_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.GetThingModelTslResponse(),
            self.do_request('GetThingModelTsl', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def get_thing_model_tsl(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_thing_model_tsl_with_options(request, runtime)

    def get_thing_model_tsl_published_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.GetThingModelTslPublishedResponse(),
            self.do_request('GetThingModelTslPublished', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def get_thing_model_tsl_published(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_thing_model_tsl_published_with_options(request, runtime)

    def get_thing_script_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.GetThingScriptResponse(),
            self.do_request('GetThingScript', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def get_thing_script(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_thing_script_with_options(request, runtime)

    def get_thing_template_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.GetThingTemplateResponse(),
            self.do_request('GetThingTemplate', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def get_thing_template(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_thing_template_with_options(request, runtime)

    def get_thing_topo_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.GetThingTopoResponse(),
            self.do_request('GetThingTopo', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def get_thing_topo(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_thing_topo_with_options(request, runtime)

    def gis_query_device_location_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.GisQueryDeviceLocationResponse(),
            self.do_request('GisQueryDeviceLocation', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def gis_query_device_location(self, request):
        runtime = util_models.RuntimeOptions()
        return self.gis_query_device_location_with_options(request, runtime)

    def gis_search_device_trace_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.GisSearchDeviceTraceResponse(),
            self.do_request('GisSearchDeviceTrace', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def gis_search_device_trace(self, request):
        runtime = util_models.RuntimeOptions()
        return self.gis_search_device_trace_with_options(request, runtime)

    def import_dtdata_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.ImportDTDataResponse(),
            self.do_request('ImportDTData', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def import_dtdata(self, request):
        runtime = util_models.RuntimeOptions()
        return self.import_dtdata_with_options(request, runtime)

    def import_device_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.ImportDeviceResponse(),
            self.do_request('ImportDevice', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def import_device(self, request):
        runtime = util_models.RuntimeOptions()
        return self.import_device_with_options(request, runtime)

    def import_thing_model_tsl_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.ImportThingModelTslResponse(),
            self.do_request('ImportThingModelTsl', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def import_thing_model_tsl(self, request):
        runtime = util_models.RuntimeOptions()
        return self.import_thing_model_tsl_with_options(request, runtime)

    def invoke_data_apiservice_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.InvokeDataAPIServiceResponse(),
            self.do_request('InvokeDataAPIService', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def invoke_data_apiservice(self, request):
        runtime = util_models.RuntimeOptions()
        return self.invoke_data_apiservice_with_options(request, runtime)

    def invoke_thing_service_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.InvokeThingServiceResponse(),
            self.do_request('InvokeThingService', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def invoke_thing_service(self, request):
        runtime = util_models.RuntimeOptions()
        return self.invoke_thing_service_with_options(request, runtime)

    def invoke_things_service_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.InvokeThingsServiceResponse(),
            self.do_request('InvokeThingsService', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def invoke_things_service(self, request):
        runtime = util_models.RuntimeOptions()
        return self.invoke_things_service_with_options(request, runtime)

    def list_analytics_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.ListAnalyticsDataResponse(),
            self.do_request('ListAnalyticsData', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def list_analytics_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_analytics_data_with_options(request, runtime)

    def list_data_source_item_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.ListDataSourceItemResponse(),
            self.do_request('ListDataSourceItem', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def list_data_source_item(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_data_source_item_with_options(request, runtime)

    def list_destination_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.ListDestinationResponse(),
            self.do_request('ListDestination', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def list_destination(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_destination_with_options(request, runtime)

    def list_device_distribute_job_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.ListDeviceDistributeJobResponse(),
            self.do_request('ListDeviceDistributeJob', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def list_device_distribute_job(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_device_distribute_job_with_options(request, runtime)

    def list_distributed_device_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.ListDistributedDeviceResponse(),
            self.do_request('ListDistributedDevice', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def list_distributed_device(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_distributed_device_with_options(request, runtime)

    def list_distributed_product_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.ListDistributedProductResponse(),
            self.do_request('ListDistributedProduct', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def list_distributed_product(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_distributed_product_with_options(request, runtime)

    def list_job_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.ListJobResponse(),
            self.do_request('ListJob', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def list_job(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_job_with_options(request, runtime)

    def list_otafirmware_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.ListOTAFirmwareResponse(),
            self.do_request('ListOTAFirmware', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def list_otafirmware(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_otafirmware_with_options(request, runtime)

    def list_otajob_by_device_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.ListOTAJobByDeviceResponse(),
            self.do_request('ListOTAJobByDevice', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def list_otajob_by_device(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_otajob_by_device_with_options(request, runtime)

    def list_otajob_by_firmware_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.ListOTAJobByFirmwareResponse(),
            self.do_request('ListOTAJobByFirmware', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def list_otajob_by_firmware(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_otajob_by_firmware_with_options(request, runtime)

    def list_otamodule_by_product_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.ListOTAModuleByProductResponse(),
            self.do_request('ListOTAModuleByProduct', 'HTTPS', 'GET', '2018-01-20', 'AK', TeaCore.to_map(request), None, runtime)
        )

    def list_otamodule_by_product(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_otamodule_by_product_with_options(request, runtime)

    def list_otamodule_versions_by_device_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.ListOTAModuleVersionsByDeviceResponse(),
            self.do_request('ListOTAModuleVersionsByDevice', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def list_otamodule_versions_by_device(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_otamodule_versions_by_device_with_options(request, runtime)

    def list_otatask_by_job_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.ListOTATaskByJobResponse(),
            self.do_request('ListOTATaskByJob', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def list_otatask_by_job(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_otatask_by_job_with_options(request, runtime)

    def list_otaunfinished_task_by_device_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.ListOTAUnfinishedTaskByDeviceResponse(),
            self.do_request('ListOTAUnfinishedTaskByDevice', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def list_otaunfinished_task_by_device(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_otaunfinished_task_by_device_with_options(request, runtime)

    def list_parser_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.ListParserResponse(),
            self.do_request('ListParser', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def list_parser(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_parser_with_options(request, runtime)

    def list_parser_data_source_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.ListParserDataSourceResponse(),
            self.do_request('ListParserDataSource', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def list_parser_data_source(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_parser_data_source_with_options(request, runtime)

    def list_parser_destination_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.ListParserDestinationResponse(),
            self.do_request('ListParserDestination', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def list_parser_destination(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_parser_destination_with_options(request, runtime)

    def list_product_by_tags_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.ListProductByTagsResponse(),
            self.do_request('ListProductByTags', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def list_product_by_tags(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_product_by_tags_with_options(request, runtime)

    def list_product_tags_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.ListProductTagsResponse(),
            self.do_request('ListProductTags', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def list_product_tags(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_product_tags_with_options(request, runtime)

    def list_rule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.ListRuleResponse(),
            self.do_request('ListRule', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def list_rule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_rule_with_options(request, runtime)

    def list_rule_actions_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.ListRuleActionsResponse(),
            self.do_request('ListRuleActions', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def list_rule_actions(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_rule_actions_with_options(request, runtime)

    def list_task_with_options(self, tmp, runtime):
        UtilClient.validate_model(tmp)
        request = iot_20180120_models.ListTaskShrinkRequest()
        RPCUtilClient.convert(tmp, request)
        if not UtilClient.is_unset(tmp.device):
            request.device_shrink = UtilClient.to_jsonstring(tmp.device)
        return TeaCore.from_map(
            iot_20180120_models.ListTaskResponse(),
            self.do_request('ListTask', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def list_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_task_with_options(request, runtime)

    def list_thing_model_version_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.ListThingModelVersionResponse(),
            self.do_request('ListThingModelVersion', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def list_thing_model_version(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_thing_model_version_with_options(request, runtime)

    def list_thing_templates_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.ListThingTemplatesResponse(),
            self.do_request('ListThingTemplates', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def list_thing_templates(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_thing_templates_with_options(request, runtime)

    def notify_add_thing_topo_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.NotifyAddThingTopoResponse(),
            self.do_request('NotifyAddThingTopo', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def notify_add_thing_topo(self, request):
        runtime = util_models.RuntimeOptions()
        return self.notify_add_thing_topo_with_options(request, runtime)

    def open_iot_service_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.OpenIotServiceResponse(),
            self.do_request('OpenIotService', 'HTTPS', 'POST', '2018-01-20', 'AK,APP,PrivateKey,BearerToken', None, TeaCore.to_map(request), runtime)
        )

    def open_iot_service(self, request):
        runtime = util_models.RuntimeOptions()
        return self.open_iot_service_with_options(request, runtime)

    def package_sound_code_label_batch_audio_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.PackageSoundCodeLabelBatchAudioResponse(),
            self.do_request('PackageSoundCodeLabelBatchAudio', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def package_sound_code_label_batch_audio(self, request):
        runtime = util_models.RuntimeOptions()
        return self.package_sound_code_label_batch_audio_with_options(request, runtime)

    def page_query_shared_speech_open_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.PageQuerySharedSpeechOpenResponse(),
            self.do_request('PageQuerySharedSpeechOpen', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def page_query_shared_speech_open(self, request):
        runtime = util_models.RuntimeOptions()
        return self.page_query_shared_speech_open_with_options(request, runtime)

    def page_query_speech_broadcast_hour_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.PageQuerySpeechBroadcastHourResponse(),
            self.do_request('PageQuerySpeechBroadcastHour', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def page_query_speech_broadcast_hour(self, request):
        runtime = util_models.RuntimeOptions()
        return self.page_query_speech_broadcast_hour_with_options(request, runtime)

    def print_by_template_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.PrintByTemplateResponse(),
            self.do_request('PrintByTemplate', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def print_by_template(self, request):
        runtime = util_models.RuntimeOptions()
        return self.print_by_template_with_options(request, runtime)

    def pub_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.PubResponse(),
            self.do_request('Pub', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def pub(self, request):
        runtime = util_models.RuntimeOptions()
        return self.pub_with_options(request, runtime)

    def pub_broadcast_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.PubBroadcastResponse(),
            self.do_request('PubBroadcast', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def pub_broadcast(self, request):
        runtime = util_models.RuntimeOptions()
        return self.pub_broadcast_with_options(request, runtime)

    def publish_script_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.PublishScriptResponse(),
            self.do_request('PublishScript', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def publish_script(self, request):
        runtime = util_models.RuntimeOptions()
        return self.publish_script_with_options(request, runtime)

    def publish_studio_app_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.PublishStudioAppResponse(),
            self.do_request('PublishStudioApp', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def publish_studio_app(self, request):
        runtime = util_models.RuntimeOptions()
        return self.publish_studio_app_with_options(request, runtime)

    def publish_thing_model_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.PublishThingModelResponse(),
            self.do_request('PublishThingModel', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def publish_thing_model(self, request):
        runtime = util_models.RuntimeOptions()
        return self.publish_thing_model_with_options(request, runtime)

    def push_speech_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.PushSpeechResponse(),
            self.do_request('PushSpeech', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def push_speech(self, request):
        runtime = util_models.RuntimeOptions()
        return self.push_speech_with_options(request, runtime)

    def query_batch_register_device_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QueryBatchRegisterDeviceStatusResponse(),
            self.do_request('QueryBatchRegisterDeviceStatus', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def query_batch_register_device_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_batch_register_device_status_with_options(request, runtime)

    def query_cert_url_by_apply_id_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QueryCertUrlByApplyIdResponse(),
            self.do_request('QueryCertUrlByApplyId', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def query_cert_url_by_apply_id(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_cert_url_by_apply_id_with_options(request, runtime)

    def query_client_ids_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QueryClientIdsResponse(),
            self.do_request('QueryClientIds', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def query_client_ids(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_client_ids_with_options(request, runtime)

    def query_consumer_group_by_group_id_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QueryConsumerGroupByGroupIdResponse(),
            self.do_request('QueryConsumerGroupByGroupId', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def query_consumer_group_by_group_id(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_consumer_group_by_group_id_with_options(request, runtime)

    def query_consumer_group_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QueryConsumerGroupListResponse(),
            self.do_request('QueryConsumerGroupList', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def query_consumer_group_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_consumer_group_list_with_options(request, runtime)

    def query_consumer_group_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QueryConsumerGroupStatusResponse(),
            self.do_request('QueryConsumerGroupStatus', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def query_consumer_group_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_consumer_group_status_with_options(request, runtime)

    def query_detail_scene_rule_log_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QueryDetailSceneRuleLogResponse(),
            self.do_request('QueryDetailSceneRuleLog', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def query_detail_scene_rule_log(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_detail_scene_rule_log_with_options(request, runtime)

    def query_device_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QueryDeviceResponse(),
            self.do_request('QueryDevice', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def query_device(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_device_with_options(request, runtime)

    def query_device_by_sqlwith_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QueryDeviceBySQLResponse(),
            self.do_request('QueryDeviceBySQL', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def query_device_by_sql(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_device_by_sqlwith_options(request, runtime)

    def query_device_by_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QueryDeviceByStatusResponse(),
            self.do_request('QueryDeviceByStatus', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def query_device_by_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_device_by_status_with_options(request, runtime)

    def query_device_by_tags_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QueryDeviceByTagsResponse(),
            self.do_request('QueryDeviceByTags', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def query_device_by_tags(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_device_by_tags_with_options(request, runtime)

    def query_device_cert_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QueryDeviceCertResponse(),
            self.do_request('QueryDeviceCert', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def query_device_cert(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_device_cert_with_options(request, runtime)

    def query_device_desired_property_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QueryDeviceDesiredPropertyResponse(),
            self.do_request('QueryDeviceDesiredProperty', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def query_device_desired_property(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_device_desired_property_with_options(request, runtime)

    def query_device_detail_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QueryDeviceDetailResponse(),
            self.do_request('QueryDeviceDetail', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def query_device_detail(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_device_detail_with_options(request, runtime)

    def query_device_distribute_detail_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QueryDeviceDistributeDetailResponse(),
            self.do_request('QueryDeviceDistributeDetail', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def query_device_distribute_detail(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_device_distribute_detail_with_options(request, runtime)

    def query_device_distribute_job_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QueryDeviceDistributeJobResponse(),
            self.do_request('QueryDeviceDistributeJob', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def query_device_distribute_job(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_device_distribute_job_with_options(request, runtime)

    def query_device_event_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QueryDeviceEventDataResponse(),
            self.do_request('QueryDeviceEventData', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def query_device_event_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_device_event_data_with_options(request, runtime)

    def query_device_file_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QueryDeviceFileResponse(),
            self.do_request('QueryDeviceFile', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def query_device_file(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_device_file_with_options(request, runtime)

    def query_device_file_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QueryDeviceFileListResponse(),
            self.do_request('QueryDeviceFileList', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def query_device_file_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_device_file_list_with_options(request, runtime)

    def query_device_group_by_device_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QueryDeviceGroupByDeviceResponse(),
            self.do_request('QueryDeviceGroupByDevice', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def query_device_group_by_device(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_device_group_by_device_with_options(request, runtime)

    def query_device_group_by_tags_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QueryDeviceGroupByTagsResponse(),
            self.do_request('QueryDeviceGroupByTags', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def query_device_group_by_tags(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_device_group_by_tags_with_options(request, runtime)

    def query_device_group_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QueryDeviceGroupInfoResponse(),
            self.do_request('QueryDeviceGroupInfo', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def query_device_group_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_device_group_info_with_options(request, runtime)

    def query_device_group_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QueryDeviceGroupListResponse(),
            self.do_request('QueryDeviceGroupList', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def query_device_group_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_device_group_list_with_options(request, runtime)

    def query_device_group_tag_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QueryDeviceGroupTagListResponse(),
            self.do_request('QueryDeviceGroupTagList', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def query_device_group_tag_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_device_group_tag_list_with_options(request, runtime)

    def query_device_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QueryDeviceInfoResponse(),
            self.do_request('QueryDeviceInfo', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def query_device_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_device_info_with_options(request, runtime)

    def query_device_list_by_device_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QueryDeviceListByDeviceGroupResponse(),
            self.do_request('QueryDeviceListByDeviceGroup', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def query_device_list_by_device_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_device_list_by_device_group_with_options(request, runtime)

    def query_device_original_event_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QueryDeviceOriginalEventDataResponse(),
            self.do_request('QueryDeviceOriginalEventData', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def query_device_original_event_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_device_original_event_data_with_options(request, runtime)

    def query_device_original_property_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QueryDeviceOriginalPropertyDataResponse(),
            self.do_request('QueryDeviceOriginalPropertyData', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def query_device_original_property_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_device_original_property_data_with_options(request, runtime)

    def query_device_original_property_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QueryDeviceOriginalPropertyStatusResponse(),
            self.do_request('QueryDeviceOriginalPropertyStatus', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def query_device_original_property_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_device_original_property_status_with_options(request, runtime)

    def query_device_original_service_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QueryDeviceOriginalServiceDataResponse(),
            self.do_request('QueryDeviceOriginalServiceData', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def query_device_original_service_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_device_original_service_data_with_options(request, runtime)

    def query_device_prop_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QueryDevicePropResponse(),
            self.do_request('QueryDeviceProp', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def query_device_prop(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_device_prop_with_options(request, runtime)

    def query_device_properties_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QueryDevicePropertiesDataResponse(),
            self.do_request('QueryDevicePropertiesData', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def query_device_properties_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_device_properties_data_with_options(request, runtime)

    def query_device_property_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QueryDevicePropertyDataResponse(),
            self.do_request('QueryDevicePropertyData', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def query_device_property_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_device_property_data_with_options(request, runtime)

    def query_device_property_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QueryDevicePropertyStatusResponse(),
            self.do_request('QueryDevicePropertyStatus', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def query_device_property_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_device_property_status_with_options(request, runtime)

    def query_device_service_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QueryDeviceServiceDataResponse(),
            self.do_request('QueryDeviceServiceData', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def query_device_service_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_device_service_data_with_options(request, runtime)

    def query_device_speech_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QueryDeviceSpeechResponse(),
            self.do_request('QueryDeviceSpeech', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def query_device_speech(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_device_speech_with_options(request, runtime)

    def query_device_statistics_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QueryDeviceStatisticsResponse(),
            self.do_request('QueryDeviceStatistics', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def query_device_statistics(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_device_statistics_with_options(request, runtime)

    def query_device_sub_topic_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QueryDeviceSubTopicResponse(),
            self.do_request('QueryDeviceSubTopic', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def query_device_sub_topic(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_device_sub_topic_with_options(request, runtime)

    def query_device_tunnel_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QueryDeviceTunnelResponse(),
            self.do_request('QueryDeviceTunnel', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def query_device_tunnel(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_device_tunnel_with_options(request, runtime)

    def query_devices_hot_storage_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QueryDevicesHotStorageDataResponse(),
            self.do_request('QueryDevicesHotStorageData', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def query_devices_hot_storage_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_devices_hot_storage_data_with_options(request, runtime)

    def query_devices_hot_storage_data_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QueryDevicesHotStorageDataStatusResponse(),
            self.do_request('QueryDevicesHotStorageDataStatus', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def query_devices_hot_storage_data_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_devices_hot_storage_data_status_with_options(request, runtime)

    def query_dynamic_group_devices_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QueryDynamicGroupDevicesResponse(),
            self.do_request('QueryDynamicGroupDevices', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def query_dynamic_group_devices(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_dynamic_group_devices_with_options(request, runtime)

    def query_edge_driver_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QueryEdgeDriverResponse(),
            self.do_request('QueryEdgeDriver', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def query_edge_driver(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_edge_driver_with_options(request, runtime)

    def query_edge_driver_version_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QueryEdgeDriverVersionResponse(),
            self.do_request('QueryEdgeDriverVersion', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def query_edge_driver_version(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_edge_driver_version_with_options(request, runtime)

    def query_edge_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QueryEdgeInstanceResponse(),
            self.do_request('QueryEdgeInstance', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def query_edge_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_edge_instance_with_options(request, runtime)

    def query_edge_instance_channel_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QueryEdgeInstanceChannelResponse(),
            self.do_request('QueryEdgeInstanceChannel', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def query_edge_instance_channel(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_edge_instance_channel_with_options(request, runtime)

    def query_edge_instance_device_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QueryEdgeInstanceDeviceResponse(),
            self.do_request('QueryEdgeInstanceDevice', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def query_edge_instance_device(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_edge_instance_device_with_options(request, runtime)

    def query_edge_instance_device_by_driver_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QueryEdgeInstanceDeviceByDriverResponse(),
            self.do_request('QueryEdgeInstanceDeviceByDriver', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def query_edge_instance_device_by_driver(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_edge_instance_device_by_driver_with_options(request, runtime)

    def query_edge_instance_driver_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QueryEdgeInstanceDriverResponse(),
            self.do_request('QueryEdgeInstanceDriver', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def query_edge_instance_driver(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_edge_instance_driver_with_options(request, runtime)

    def query_edge_instance_gateway_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QueryEdgeInstanceGatewayResponse(),
            self.do_request('QueryEdgeInstanceGateway', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def query_edge_instance_gateway(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_edge_instance_gateway_with_options(request, runtime)

    def query_edge_instance_historic_deployment_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QueryEdgeInstanceHistoricDeploymentResponse(),
            self.do_request('QueryEdgeInstanceHistoricDeployment', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def query_edge_instance_historic_deployment(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_edge_instance_historic_deployment_with_options(request, runtime)

    def query_edge_instance_message_routing_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QueryEdgeInstanceMessageRoutingResponse(),
            self.do_request('QueryEdgeInstanceMessageRouting', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def query_edge_instance_message_routing(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_edge_instance_message_routing_with_options(request, runtime)

    def query_edge_instance_scene_rule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QueryEdgeInstanceSceneRuleResponse(),
            self.do_request('QueryEdgeInstanceSceneRule', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def query_edge_instance_scene_rule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_edge_instance_scene_rule_with_options(request, runtime)

    def query_imported_device_by_apply_id_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QueryImportedDeviceByApplyIdResponse(),
            self.do_request('QueryImportedDeviceByApplyId', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def query_imported_device_by_apply_id(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_imported_device_by_apply_id_with_options(request, runtime)

    def query_job_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QueryJobResponse(),
            self.do_request('QueryJob', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def query_job(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_job_with_options(request, runtime)

    def query_job_statistics_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QueryJobStatisticsResponse(),
            self.do_request('QueryJobStatistics', 'HTTPS', 'GET', '2018-01-20', 'AK', TeaCore.to_map(request), None, runtime)
        )

    def query_job_statistics(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_job_statistics_with_options(request, runtime)

    def query_license_device_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QueryLicenseDeviceListResponse(),
            self.do_request('QueryLicenseDeviceList', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def query_license_device_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_license_device_list_with_options(request, runtime)

    def query_lo_ra_join_permissions_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QueryLoRaJoinPermissionsResponse(),
            self.do_request('QueryLoRaJoinPermissions', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def query_lo_ra_join_permissions(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_lo_ra_join_permissions_with_options(request, runtime)

    def query_message_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QueryMessageInfoResponse(),
            self.do_request('QueryMessageInfo', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def query_message_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_message_info_with_options(request, runtime)

    def query_otafirmware_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QueryOTAFirmwareResponse(),
            self.do_request('QueryOTAFirmware', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def query_otafirmware(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_otafirmware_with_options(request, runtime)

    def query_otajob_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QueryOTAJobResponse(),
            self.do_request('QueryOTAJob', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def query_otajob(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_otajob_with_options(request, runtime)

    def query_page_by_apply_id_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QueryPageByApplyIdResponse(),
            self.do_request('QueryPageByApplyId', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def query_page_by_apply_id(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_page_by_apply_id_with_options(request, runtime)

    def query_product_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QueryProductResponse(),
            self.do_request('QueryProduct', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def query_product(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_product_with_options(request, runtime)

    def query_product_cert_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QueryProductCertInfoResponse(),
            self.do_request('QueryProductCertInfo', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def query_product_cert_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_product_cert_info_with_options(request, runtime)

    def query_product_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QueryProductListResponse(),
            self.do_request('QueryProductList', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def query_product_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_product_list_with_options(request, runtime)

    def query_product_topic_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QueryProductTopicResponse(),
            self.do_request('QueryProductTopic', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def query_product_topic(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_product_topic_with_options(request, runtime)

    def query_project_share_device_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QueryProjectShareDeviceListResponse(),
            self.do_request('QueryProjectShareDeviceList', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def query_project_share_device_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_project_share_device_list_with_options(request, runtime)

    def query_scene_rule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QuerySceneRuleResponse(),
            self.do_request('QuerySceneRule', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def query_scene_rule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_scene_rule_with_options(request, runtime)

    def query_schedule_period_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QuerySchedulePeriodListResponse(),
            self.do_request('QuerySchedulePeriodList', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def query_schedule_period_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_schedule_period_list_with_options(request, runtime)

    def query_share_task_device_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QueryShareTaskDeviceListResponse(),
            self.do_request('QueryShareTaskDeviceList', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def query_share_task_device_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_share_task_device_list_with_options(request, runtime)

    def query_solution_device_group_page_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QuerySolutionDeviceGroupPageResponse(),
            self.do_request('QuerySolutionDeviceGroupPage', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def query_solution_device_group_page(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_solution_device_group_page_with_options(request, runtime)

    def query_sound_code_label_batch_failed_result_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QuerySoundCodeLabelBatchFailedResultResponse(),
            self.do_request('QuerySoundCodeLabelBatchFailedResult', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def query_sound_code_label_batch_failed_result(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_sound_code_label_batch_failed_result_with_options(request, runtime)

    def query_sound_code_label_batch_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QuerySoundCodeLabelBatchListResponse(),
            self.do_request('QuerySoundCodeLabelBatchList', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def query_sound_code_label_batch_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_sound_code_label_batch_list_with_options(request, runtime)

    def query_sound_code_label_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QuerySoundCodeLabelListResponse(),
            self.do_request('QuerySoundCodeLabelList', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def query_sound_code_label_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_sound_code_label_list_with_options(request, runtime)

    def query_sound_code_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QuerySoundCodeListResponse(),
            self.do_request('QuerySoundCodeList', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def query_sound_code_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_sound_code_list_with_options(request, runtime)

    def query_sound_code_schedule_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QuerySoundCodeScheduleListResponse(),
            self.do_request('QuerySoundCodeScheduleList', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def query_sound_code_schedule_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_sound_code_schedule_list_with_options(request, runtime)

    def query_speech_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QuerySpeechResponse(),
            self.do_request('QuerySpeech', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def query_speech(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_speech_with_options(request, runtime)

    def query_speech_device_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QuerySpeechDeviceResponse(),
            self.do_request('QuerySpeechDevice', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def query_speech_device(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_speech_device_with_options(request, runtime)

    def query_speech_license_device_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QuerySpeechLicenseDeviceListResponse(),
            self.do_request('QuerySpeechLicenseDeviceList', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def query_speech_license_device_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_speech_license_device_list_with_options(request, runtime)

    def query_speech_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QuerySpeechListResponse(),
            self.do_request('QuerySpeechList', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def query_speech_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_speech_list_with_options(request, runtime)

    def query_speech_push_job_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QuerySpeechPushJobResponse(),
            self.do_request('QuerySpeechPushJob', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def query_speech_push_job(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_speech_push_job_with_options(request, runtime)

    def query_speech_push_job_device_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QuerySpeechPushJobDeviceResponse(),
            self.do_request('QuerySpeechPushJobDevice', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def query_speech_push_job_device(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_speech_push_job_device_with_options(request, runtime)

    def query_speech_push_job_speech_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QuerySpeechPushJobSpeechResponse(),
            self.do_request('QuerySpeechPushJobSpeech', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def query_speech_push_job_speech(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_speech_push_job_speech_with_options(request, runtime)

    def query_studio_app_domain_list_open_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QueryStudioAppDomainListOpenResponse(),
            self.do_request('QueryStudioAppDomainListOpen', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def query_studio_app_domain_list_open(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_studio_app_domain_list_open_with_options(request, runtime)

    def query_studio_app_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QueryStudioAppListResponse(),
            self.do_request('QueryStudioAppList', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def query_studio_app_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_studio_app_list_with_options(request, runtime)

    def query_studio_app_page_list_open_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QueryStudioAppPageListOpenResponse(),
            self.do_request('QueryStudioAppPageListOpen', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def query_studio_app_page_list_open(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_studio_app_page_list_open_with_options(request, runtime)

    def query_studio_project_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QueryStudioProjectListResponse(),
            self.do_request('QueryStudioProjectList', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def query_studio_project_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_studio_project_list_with_options(request, runtime)

    def query_subscribe_relation_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QuerySubscribeRelationResponse(),
            self.do_request('QuerySubscribeRelation', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def query_subscribe_relation(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_subscribe_relation_with_options(request, runtime)

    def query_summary_scene_rule_log_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QuerySummarySceneRuleLogResponse(),
            self.do_request('QuerySummarySceneRuleLog', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def query_summary_scene_rule_log(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_summary_scene_rule_log_with_options(request, runtime)

    def query_super_device_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QuerySuperDeviceGroupResponse(),
            self.do_request('QuerySuperDeviceGroup', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def query_super_device_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_super_device_group_with_options(request, runtime)

    def query_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QueryTaskResponse(),
            self.do_request('QueryTask', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def query_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_task_with_options(request, runtime)

    def query_thing_model_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QueryThingModelResponse(),
            self.do_request('QueryThingModel', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def query_thing_model(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_thing_model_with_options(request, runtime)

    def query_thing_model_extend_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QueryThingModelExtendConfigResponse(),
            self.do_request('QueryThingModelExtendConfig', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def query_thing_model_extend_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_thing_model_extend_config_with_options(request, runtime)

    def query_thing_model_extend_config_published_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QueryThingModelExtendConfigPublishedResponse(),
            self.do_request('QueryThingModelExtendConfigPublished', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def query_thing_model_extend_config_published(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_thing_model_extend_config_published_with_options(request, runtime)

    def query_thing_model_published_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QueryThingModelPublishedResponse(),
            self.do_request('QueryThingModelPublished', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def query_thing_model_published(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_thing_model_published_with_options(request, runtime)

    def query_topic_reverse_route_table_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QueryTopicReverseRouteTableResponse(),
            self.do_request('QueryTopicReverseRouteTable', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def query_topic_reverse_route_table(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_topic_reverse_route_table_with_options(request, runtime)

    def query_topic_route_table_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QueryTopicRouteTableResponse(),
            self.do_request('QueryTopicRouteTable', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def query_topic_route_table(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_topic_route_table_with_options(request, runtime)

    def query_vehicle_device_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.QueryVehicleDeviceResponse(),
            self.do_request('QueryVehicleDevice', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def query_vehicle_device(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_vehicle_device_with_options(request, runtime)

    def rrpc_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.RRpcResponse(),
            self.do_request('RRpc', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def rrpc(self, request):
        runtime = util_models.RuntimeOptions()
        return self.rrpc_with_options(request, runtime)

    def re_bind_license_device_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.ReBindLicenseDeviceResponse(),
            self.do_request('ReBindLicenseDevice', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def re_bind_license_device(self, request):
        runtime = util_models.RuntimeOptions()
        return self.re_bind_license_device_with_options(request, runtime)

    def recognize_car_num_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.RecognizeCarNumResponse(),
            self.do_request('RecognizeCarNum', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def recognize_car_num(self, request):
        runtime = util_models.RuntimeOptions()
        return self.recognize_car_num_with_options(request, runtime)

    def recognize_picture_general_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.RecognizePictureGeneralResponse(),
            self.do_request('RecognizePictureGeneral', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def recognize_picture_general(self, request):
        runtime = util_models.RuntimeOptions()
        return self.recognize_picture_general_with_options(request, runtime)

    def refresh_device_tunnel_share_password_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.RefreshDeviceTunnelSharePasswordResponse(),
            self.do_request('RefreshDeviceTunnelSharePassword', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def refresh_device_tunnel_share_password(self, request):
        runtime = util_models.RuntimeOptions()
        return self.refresh_device_tunnel_share_password_with_options(request, runtime)

    def refresh_studio_app_token_open_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.RefreshStudioAppTokenOpenResponse(),
            self.do_request('RefreshStudioAppTokenOpen', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def refresh_studio_app_token_open(self, request):
        runtime = util_models.RuntimeOptions()
        return self.refresh_studio_app_token_open_with_options(request, runtime)

    def register_device_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.RegisterDeviceResponse(),
            self.do_request('RegisterDevice', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def register_device(self, request):
        runtime = util_models.RuntimeOptions()
        return self.register_device_with_options(request, runtime)

    def release_edge_driver_version_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.ReleaseEdgeDriverVersionResponse(),
            self.do_request('ReleaseEdgeDriverVersion', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def release_edge_driver_version(self, request):
        runtime = util_models.RuntimeOptions()
        return self.release_edge_driver_version_with_options(request, runtime)

    def release_product_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.ReleaseProductResponse(),
            self.do_request('ReleaseProduct', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def release_product(self, request):
        runtime = util_models.RuntimeOptions()
        return self.release_product_with_options(request, runtime)

    def remove_thing_topo_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.RemoveThingTopoResponse(),
            self.do_request('RemoveThingTopo', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def remove_thing_topo(self, request):
        runtime = util_models.RuntimeOptions()
        return self.remove_thing_topo_with_options(request, runtime)

    def replace_edge_instance_gateway_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.ReplaceEdgeInstanceGatewayResponse(),
            self.do_request('ReplaceEdgeInstanceGateway', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def replace_edge_instance_gateway(self, request):
        runtime = util_models.RuntimeOptions()
        return self.replace_edge_instance_gateway_with_options(request, runtime)

    def rerun_job_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.RerunJobResponse(),
            self.do_request('RerunJob', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def rerun_job(self, request):
        runtime = util_models.RuntimeOptions()
        return self.rerun_job_with_options(request, runtime)

    def reset_consumer_group_position_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.ResetConsumerGroupPositionResponse(),
            self.do_request('ResetConsumerGroupPosition', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def reset_consumer_group_position(self, request):
        runtime = util_models.RuntimeOptions()
        return self.reset_consumer_group_position_with_options(request, runtime)

    def reset_thing_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.ResetThingResponse(),
            self.do_request('ResetThing', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def reset_thing(self, request):
        runtime = util_models.RuntimeOptions()
        return self.reset_thing_with_options(request, runtime)

    def retry_sound_code_label_batch_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.RetrySoundCodeLabelBatchResponse(),
            self.do_request('RetrySoundCodeLabelBatch', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def retry_sound_code_label_batch(self, request):
        runtime = util_models.RuntimeOptions()
        return self.retry_sound_code_label_batch_with_options(request, runtime)

    def reupgrade_otatask_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.ReupgradeOTATaskResponse(),
            self.do_request('ReupgradeOTATask', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def reupgrade_otatask(self, request):
        runtime = util_models.RuntimeOptions()
        return self.reupgrade_otatask_with_options(request, runtime)

    def save_device_prop_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.SaveDevicePropResponse(),
            self.do_request('SaveDeviceProp', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def save_device_prop(self, request):
        runtime = util_models.RuntimeOptions()
        return self.save_device_prop_with_options(request, runtime)

    def save_script_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.SaveScriptResponse(),
            self.do_request('SaveScript', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def save_script(self, request):
        runtime = util_models.RuntimeOptions()
        return self.save_script_with_options(request, runtime)

    def set_device_desired_property_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.SetDeviceDesiredPropertyResponse(),
            self.do_request('SetDeviceDesiredProperty', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def set_device_desired_property(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_device_desired_property_with_options(request, runtime)

    def set_device_group_tags_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.SetDeviceGroupTagsResponse(),
            self.do_request('SetDeviceGroupTags', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def set_device_group_tags(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_device_group_tags_with_options(request, runtime)

    def set_device_property_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.SetDevicePropertyResponse(),
            self.do_request('SetDeviceProperty', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def set_device_property(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_device_property_with_options(request, runtime)

    def set_devices_property_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.SetDevicesPropertyResponse(),
            self.do_request('SetDevicesProperty', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def set_devices_property(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_devices_property_with_options(request, runtime)

    def set_edge_instance_driver_configs_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.SetEdgeInstanceDriverConfigsResponse(),
            self.do_request('SetEdgeInstanceDriverConfigs', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def set_edge_instance_driver_configs(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_edge_instance_driver_configs_with_options(request, runtime)

    def set_product_cert_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.SetProductCertInfoResponse(),
            self.do_request('SetProductCertInfo', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def set_product_cert_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_product_cert_info_with_options(request, runtime)

    def set_studio_project_cooperation_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.SetStudioProjectCooperationResponse(),
            self.do_request('SetStudioProjectCooperation', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def set_studio_project_cooperation(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_studio_project_cooperation_with_options(request, runtime)

    def setup_studio_app_auth_mode_open_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.SetupStudioAppAuthModeOpenResponse(),
            self.do_request('SetupStudioAppAuthModeOpen', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def setup_studio_app_auth_mode_open(self, request):
        runtime = util_models.RuntimeOptions()
        return self.setup_studio_app_auth_mode_open_with_options(request, runtime)

    def share_speech_by_combination_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.ShareSpeechByCombinationResponse(),
            self.do_request('ShareSpeechByCombination', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def share_speech_by_combination(self, request):
        runtime = util_models.RuntimeOptions()
        return self.share_speech_by_combination_with_options(request, runtime)

    def speech_by_combination_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.SpeechByCombinationResponse(),
            self.do_request('SpeechByCombination', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def speech_by_combination(self, request):
        runtime = util_models.RuntimeOptions()
        return self.speech_by_combination_with_options(request, runtime)

    def speech_by_synthesis_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.SpeechBySynthesisResponse(),
            self.do_request('SpeechBySynthesis', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def speech_by_synthesis(self, request):
        runtime = util_models.RuntimeOptions()
        return self.speech_by_synthesis_with_options(request, runtime)

    def start_parser_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.StartParserResponse(),
            self.do_request('StartParser', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def start_parser(self, request):
        runtime = util_models.RuntimeOptions()
        return self.start_parser_with_options(request, runtime)

    def start_rule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.StartRuleResponse(),
            self.do_request('StartRule', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def start_rule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.start_rule_with_options(request, runtime)

    def stop_parser_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.StopParserResponse(),
            self.do_request('StopParser', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def stop_parser(self, request):
        runtime = util_models.RuntimeOptions()
        return self.stop_parser_with_options(request, runtime)

    def stop_rule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.StopRuleResponse(),
            self.do_request('StopRule', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def stop_rule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.stop_rule_with_options(request, runtime)

    def subscribe_topic_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.SubscribeTopicResponse(),
            self.do_request('SubscribeTopic', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def subscribe_topic(self, request):
        runtime = util_models.RuntimeOptions()
        return self.subscribe_topic_with_options(request, runtime)

    def sync_speech_by_combination_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.SyncSpeechByCombinationResponse(),
            self.do_request('SyncSpeechByCombination', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def sync_speech_by_combination(self, request):
        runtime = util_models.RuntimeOptions()
        return self.sync_speech_by_combination_with_options(request, runtime)

    def test_speech_with_options(self, tmp, runtime):
        UtilClient.validate_model(tmp)
        request = iot_20180120_models.TestSpeechShrinkRequest()
        RPCUtilClient.convert(tmp, request)
        if not UtilClient.is_unset(tmp.sound_code_config):
            request.sound_code_config_shrink = UtilClient.to_jsonstring(tmp.sound_code_config)
        return TeaCore.from_map(
            iot_20180120_models.TestSpeechResponse(),
            self.do_request('TestSpeech', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def test_speech(self, request):
        runtime = util_models.RuntimeOptions()
        return self.test_speech_with_options(request, runtime)

    def transform_client_id_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.TransformClientIdResponse(),
            self.do_request('TransformClientId', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def transform_client_id(self, request):
        runtime = util_models.RuntimeOptions()
        return self.transform_client_id_with_options(request, runtime)

    def trigger_scene_rule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.TriggerSceneRuleResponse(),
            self.do_request('TriggerSceneRule', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def trigger_scene_rule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.trigger_scene_rule_with_options(request, runtime)

    def unbind_application_from_edge_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.UnbindApplicationFromEdgeInstanceResponse(),
            self.do_request('UnbindApplicationFromEdgeInstance', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def unbind_application_from_edge_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.unbind_application_from_edge_instance_with_options(request, runtime)

    def unbind_driver_from_edge_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.UnbindDriverFromEdgeInstanceResponse(),
            self.do_request('UnbindDriverFromEdgeInstance', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def unbind_driver_from_edge_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.unbind_driver_from_edge_instance_with_options(request, runtime)

    def unbind_license_product_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.UnbindLicenseProductResponse(),
            self.do_request('UnbindLicenseProduct', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def unbind_license_product(self, request):
        runtime = util_models.RuntimeOptions()
        return self.unbind_license_product_with_options(request, runtime)

    def unbind_role_from_edge_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.UnbindRoleFromEdgeInstanceResponse(),
            self.do_request('UnbindRoleFromEdgeInstance', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def unbind_role_from_edge_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.unbind_role_from_edge_instance_with_options(request, runtime)

    def unbind_scene_rule_from_edge_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.UnbindSceneRuleFromEdgeInstanceResponse(),
            self.do_request('UnbindSceneRuleFromEdgeInstance', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def unbind_scene_rule_from_edge_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.unbind_scene_rule_from_edge_instance_with_options(request, runtime)

    def update_consumer_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.UpdateConsumerGroupResponse(),
            self.do_request('UpdateConsumerGroup', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def update_consumer_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_consumer_group_with_options(request, runtime)

    def update_destination_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.UpdateDestinationResponse(),
            self.do_request('UpdateDestination', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def update_destination(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_destination_with_options(request, runtime)

    def update_device_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.UpdateDeviceGroupResponse(),
            self.do_request('UpdateDeviceGroup', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def update_device_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_device_group_with_options(request, runtime)

    def update_device_shadow_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.UpdateDeviceShadowResponse(),
            self.do_request('UpdateDeviceShadow', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def update_device_shadow(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_device_shadow_with_options(request, runtime)

    def update_edge_driver_version_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.UpdateEdgeDriverVersionResponse(),
            self.do_request('UpdateEdgeDriverVersion', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def update_edge_driver_version(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_edge_driver_version_with_options(request, runtime)

    def update_edge_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.UpdateEdgeInstanceResponse(),
            self.do_request('UpdateEdgeInstance', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def update_edge_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_edge_instance_with_options(request, runtime)

    def update_edge_instance_channel_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.UpdateEdgeInstanceChannelResponse(),
            self.do_request('UpdateEdgeInstanceChannel', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def update_edge_instance_channel(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_edge_instance_channel_with_options(request, runtime)

    def update_edge_instance_message_routing_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.UpdateEdgeInstanceMessageRoutingResponse(),
            self.do_request('UpdateEdgeInstanceMessageRouting', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def update_edge_instance_message_routing(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_edge_instance_message_routing_with_options(request, runtime)

    def update_job_with_options(self, tmp, runtime):
        UtilClient.validate_model(tmp)
        request = iot_20180120_models.UpdateJobShrinkRequest()
        RPCUtilClient.convert(tmp, request)
        if not UtilClient.is_unset(tmp.rollout_config):
            request.rollout_config_shrink = UtilClient.to_jsonstring(tmp.rollout_config)
        if not UtilClient.is_unset(tmp.timeout_config):
            request.timeout_config_shrink = UtilClient.to_jsonstring(tmp.timeout_config)
        return TeaCore.from_map(
            iot_20180120_models.UpdateJobResponse(),
            self.do_request('UpdateJob', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def update_job(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_job_with_options(request, runtime)

    def update_otamodule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.UpdateOTAModuleResponse(),
            self.do_request('UpdateOTAModule', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def update_otamodule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_otamodule_with_options(request, runtime)

    def update_parser_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.UpdateParserResponse(),
            self.do_request('UpdateParser', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def update_parser(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_parser_with_options(request, runtime)

    def update_parser_data_source_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.UpdateParserDataSourceResponse(),
            self.do_request('UpdateParserDataSource', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def update_parser_data_source(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_parser_data_source_with_options(request, runtime)

    def update_product_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.UpdateProductResponse(),
            self.do_request('UpdateProduct', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def update_product(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_product_with_options(request, runtime)

    def update_product_filter_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.UpdateProductFilterConfigResponse(),
            self.do_request('UpdateProductFilterConfig', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def update_product_filter_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_product_filter_config_with_options(request, runtime)

    def update_product_tags_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.UpdateProductTagsResponse(),
            self.do_request('UpdateProductTags', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def update_product_tags(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_product_tags_with_options(request, runtime)

    def update_product_topic_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.UpdateProductTopicResponse(),
            self.do_request('UpdateProductTopic', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def update_product_topic(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_product_topic_with_options(request, runtime)

    def update_rule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.UpdateRuleResponse(),
            self.do_request('UpdateRule', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def update_rule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_rule_with_options(request, runtime)

    def update_rule_action_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.UpdateRuleActionResponse(),
            self.do_request('UpdateRuleAction', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def update_rule_action(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_rule_action_with_options(request, runtime)

    def update_scene_rule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.UpdateSceneRuleResponse(),
            self.do_request('UpdateSceneRule', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def update_scene_rule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_scene_rule_with_options(request, runtime)

    def update_schedule_period_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.UpdateSchedulePeriodResponse(),
            self.do_request('UpdateSchedulePeriod', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def update_schedule_period(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_schedule_period_with_options(request, runtime)

    def update_sound_code_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.UpdateSoundCodeResponse(),
            self.do_request('UpdateSoundCode', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def update_sound_code(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_sound_code_with_options(request, runtime)

    def update_sound_code_label_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.UpdateSoundCodeLabelResponse(),
            self.do_request('UpdateSoundCodeLabel', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def update_sound_code_label(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_sound_code_label_with_options(request, runtime)

    def update_sound_code_schedule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.UpdateSoundCodeScheduleResponse(),
            self.do_request('UpdateSoundCodeSchedule', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def update_sound_code_schedule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_sound_code_schedule_with_options(request, runtime)

    def update_speech_with_options(self, tmp, runtime):
        UtilClient.validate_model(tmp)
        request = iot_20180120_models.UpdateSpeechShrinkRequest()
        RPCUtilClient.convert(tmp, request)
        if not UtilClient.is_unset(tmp.sound_code_config):
            request.sound_code_config_shrink = UtilClient.to_jsonstring(tmp.sound_code_config)
        return TeaCore.from_map(
            iot_20180120_models.UpdateSpeechResponse(),
            self.do_request('UpdateSpeech', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def update_speech(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_speech_with_options(request, runtime)

    def update_subscribe_relation_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.UpdateSubscribeRelationResponse(),
            self.do_request('UpdateSubscribeRelation', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def update_subscribe_relation(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_subscribe_relation_with_options(request, runtime)

    def update_thing_model_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.UpdateThingModelResponse(),
            self.do_request('UpdateThingModel', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def update_thing_model(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_thing_model_with_options(request, runtime)

    def update_thing_script_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.UpdateThingScriptResponse(),
            self.do_request('UpdateThingScript', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def update_thing_script(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_thing_script_with_options(request, runtime)

    def write_devices_hot_storage_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        return TeaCore.from_map(
            iot_20180120_models.WriteDevicesHotStorageDataResponse(),
            self.do_request('WriteDevicesHotStorageData', 'HTTPS', 'POST', '2018-01-20', 'AK', None, TeaCore.to_map(request), runtime)
        )

    def write_devices_hot_storage_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.write_devices_hot_storage_data_with_options(request, runtime)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)
