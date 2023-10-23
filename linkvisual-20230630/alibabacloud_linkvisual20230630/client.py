# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_linkvisual20230630 import models as linkvisual_20230630_models
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
            'ap-northeast-1': 'linkvisual.aliyuncs.com',
            'ap-northeast-2-pop': 'linkvisual.aliyuncs.com',
            'ap-south-1': 'linkvisual.aliyuncs.com',
            'ap-southeast-1': 'linkvisual.aliyuncs.com',
            'ap-southeast-2': 'linkvisual.aliyuncs.com',
            'ap-southeast-3': 'linkvisual.aliyuncs.com',
            'ap-southeast-5': 'linkvisual.aliyuncs.com',
            'cn-beijing': 'linkvisual.aliyuncs.com',
            'cn-beijing-finance-1': 'linkvisual.aliyuncs.com',
            'cn-beijing-finance-pop': 'linkvisual.aliyuncs.com',
            'cn-beijing-gov-1': 'linkvisual.aliyuncs.com',
            'cn-beijing-nu16-b01': 'linkvisual.aliyuncs.com',
            'cn-chengdu': 'linkvisual.aliyuncs.com',
            'cn-edge-1': 'linkvisual.aliyuncs.com',
            'cn-fujian': 'linkvisual.aliyuncs.com',
            'cn-haidian-cm12-c01': 'linkvisual.aliyuncs.com',
            'cn-hangzhou-bj-b01': 'linkvisual.aliyuncs.com',
            'cn-hangzhou-finance': 'linkvisual.aliyuncs.com',
            'cn-hangzhou-internal-prod-1': 'linkvisual.aliyuncs.com',
            'cn-hangzhou-internal-test-1': 'linkvisual.aliyuncs.com',
            'cn-hangzhou-internal-test-2': 'linkvisual.aliyuncs.com',
            'cn-hangzhou-internal-test-3': 'linkvisual.aliyuncs.com',
            'cn-hangzhou-test-306': 'linkvisual.aliyuncs.com',
            'cn-hongkong': 'linkvisual.aliyuncs.com',
            'cn-hongkong-finance-pop': 'linkvisual.aliyuncs.com',
            'cn-huhehaote': 'linkvisual.aliyuncs.com',
            'cn-north-2-gov-1': 'linkvisual.aliyuncs.com',
            'cn-qingdao': 'linkvisual.aliyuncs.com',
            'cn-qingdao-nebula': 'linkvisual.aliyuncs.com',
            'cn-shanghai-et15-b01': 'linkvisual.aliyuncs.com',
            'cn-shanghai-et2-b01': 'linkvisual.aliyuncs.com',
            'cn-shanghai-finance-1': 'linkvisual.aliyuncs.com',
            'cn-shanghai-inner': 'linkvisual.aliyuncs.com',
            'cn-shanghai-internal-test-1': 'linkvisual.aliyuncs.com',
            'cn-shenzhen': 'linkvisual.aliyuncs.com',
            'cn-shenzhen-finance-1': 'linkvisual.aliyuncs.com',
            'cn-shenzhen-inner': 'linkvisual.aliyuncs.com',
            'cn-shenzhen-st4-d01': 'linkvisual.aliyuncs.com',
            'cn-shenzhen-su18-b01': 'linkvisual.aliyuncs.com',
            'cn-wuhan': 'linkvisual.aliyuncs.com',
            'cn-yushanfang': 'linkvisual.aliyuncs.com',
            'cn-zhangbei-na61-b01': 'linkvisual.aliyuncs.com',
            'cn-zhangjiakou': 'linkvisual.aliyuncs.com',
            'cn-zhangjiakou-na62-a01': 'linkvisual.aliyuncs.com',
            'cn-zhengzhou-nebula-1': 'linkvisual.aliyuncs.com',
            'eu-central-1': 'linkvisual.aliyuncs.com',
            'eu-west-1': 'linkvisual.aliyuncs.com',
            'eu-west-1-oxs': 'linkvisual.aliyuncs.com',
            'me-east-1': 'linkvisual.aliyuncs.com',
            'rus-west-1-pop': 'linkvisual.aliyuncs.com',
            'us-east-1': 'linkvisual.aliyuncs.com',
            'us-west-1': 'linkvisual.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('linkvisual', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def bind_storage_order_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.device_name):
            query['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.enable_default_plan):
            query['EnableDefaultPlan'] = request.enable_default_plan
        if not UtilClient.is_unset(request.event_record_duration):
            query['EventRecordDuration'] = request.event_record_duration
        if not UtilClient.is_unset(request.event_record_prolong):
            query['EventRecordProlong'] = request.event_record_prolong
        if not UtilClient.is_unset(request.iot_id):
            query['IotId'] = request.iot_id
        if not UtilClient.is_unset(request.max_record_file_duration):
            query['MaxRecordFileDuration'] = request.max_record_file_duration
        if not UtilClient.is_unset(request.order_id):
            query['OrderId'] = request.order_id
        if not UtilClient.is_unset(request.pre_record_duration):
            query['PreRecordDuration'] = request.pre_record_duration
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        if not UtilClient.is_unset(request.user_name):
            query['UserName'] = request.user_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BindStorageOrder',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20230630_models.BindStorageOrderResponse(),
            self.call_api(params, req, runtime)
        )

    def bind_storage_order(self, request):
        runtime = util_models.RuntimeOptions()
        return self.bind_storage_order_with_options(request, runtime)

    def check_free_storage_valid_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.device_name):
            query['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.iot_id):
            query['IotId'] = request.iot_id
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CheckFreeStorageValid',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20230630_models.CheckFreeStorageValidResponse(),
            self.call_api(params, req, runtime)
        )

    def check_free_storage_valid(self, request):
        runtime = util_models.RuntimeOptions()
        return self.check_free_storage_valid_with_options(request, runtime)

    def consume_free_storage_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.device_name):
            query['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.enable_default_plan):
            query['EnableDefaultPlan'] = request.enable_default_plan
        if not UtilClient.is_unset(request.event_record_duration):
            query['EventRecordDuration'] = request.event_record_duration
        if not UtilClient.is_unset(request.event_record_prolong):
            query['EventRecordProlong'] = request.event_record_prolong
        if not UtilClient.is_unset(request.immediate_use):
            query['ImmediateUse'] = request.immediate_use
        if not UtilClient.is_unset(request.iot_id):
            query['IotId'] = request.iot_id
        if not UtilClient.is_unset(request.pre_record_duration):
            query['PreRecordDuration'] = request.pre_record_duration
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        if not UtilClient.is_unset(request.quota):
            query['Quota'] = request.quota
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ConsumeFreeStorage',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20230630_models.ConsumeFreeStorageResponse(),
            self.call_api(params, req, runtime)
        )

    def consume_free_storage(self, request):
        runtime = util_models.RuntimeOptions()
        return self.consume_free_storage_with_options(request, runtime)

    def create_and_pay_storage_order_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.commodity_code):
            query['CommodityCode'] = request.commodity_code
        if not UtilClient.is_unset(request.copies):
            query['Copies'] = request.copies
        if not UtilClient.is_unset(request.device_name):
            query['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.device_no_owner):
            query['DeviceNoOwner'] = request.device_no_owner
        if not UtilClient.is_unset(request.enable_default_plan):
            query['EnableDefaultPlan'] = request.enable_default_plan
        if not UtilClient.is_unset(request.event_record_duration):
            query['EventRecordDuration'] = request.event_record_duration
        if not UtilClient.is_unset(request.event_record_prolong):
            query['EventRecordProlong'] = request.event_record_prolong
        if not UtilClient.is_unset(request.immediate_use):
            query['ImmediateUse'] = request.immediate_use
        if not UtilClient.is_unset(request.iot_id):
            query['IotId'] = request.iot_id
        if not UtilClient.is_unset(request.max_record_file_duration):
            query['MaxRecordFileDuration'] = request.max_record_file_duration
        if not UtilClient.is_unset(request.pre_record_duration):
            query['PreRecordDuration'] = request.pre_record_duration
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        if not UtilClient.is_unset(request.specification):
            query['Specification'] = request.specification
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        if not UtilClient.is_unset(request.user_name):
            query['UserName'] = request.user_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateAndPayStorageOrder',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20230630_models.CreateAndPayStorageOrderResponse(),
            self.call_api(params, req, runtime)
        )

    def create_and_pay_storage_order(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_and_pay_storage_order_with_options(request, runtime)

    def enable_free_storage_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.device_name):
            query['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.iot_id):
            query['IotId'] = request.iot_id
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnableFreeStorage',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20230630_models.EnableFreeStorageResponse(),
            self.call_api(params, req, runtime)
        )

    def enable_free_storage(self, request):
        runtime = util_models.RuntimeOptions()
        return self.enable_free_storage_with_options(request, runtime)

    def enable_storage_order_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.device_name):
            query['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.iot_id):
            query['IotId'] = request.iot_id
        if not UtilClient.is_unset(request.order_id):
            query['OrderId'] = request.order_id
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnableStorageOrder',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20230630_models.EnableStorageOrderResponse(),
            self.call_api(params, req, runtime)
        )

    def enable_storage_order(self, request):
        runtime = util_models.RuntimeOptions()
        return self.enable_storage_order_with_options(request, runtime)

    def freeze_free_storage_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.device_name):
            query['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.iot_id):
            query['IotId'] = request.iot_id
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='FreezeFreeStorage',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20230630_models.FreezeFreeStorageResponse(),
            self.call_api(params, req, runtime)
        )

    def freeze_free_storage(self, request):
        runtime = util_models.RuntimeOptions()
        return self.freeze_free_storage_with_options(request, runtime)

    def freeze_storage_order_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.device_name):
            query['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.device_no_owner):
            query['DeviceNoOwner'] = request.device_no_owner
        if not UtilClient.is_unset(request.iot_id):
            query['IotId'] = request.iot_id
        if not UtilClient.is_unset(request.order_id):
            query['OrderId'] = request.order_id
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='FreezeStorageOrder',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20230630_models.FreezeStorageOrderResponse(),
            self.call_api(params, req, runtime)
        )

    def freeze_storage_order(self, request):
        runtime = util_models.RuntimeOptions()
        return self.freeze_storage_order_with_options(request, runtime)

    def generate_device_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.amount):
            query['Amount'] = request.amount
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GenerateDevice',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20230630_models.GenerateDeviceResponse(),
            self.call_api(params, req, runtime)
        )

    def generate_device(self, request):
        runtime = util_models.RuntimeOptions()
        return self.generate_device_with_options(request, runtime)

    def generate_device_by_batch_id_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.batch_id):
            query['BatchId'] = request.batch_id
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GenerateDeviceByBatchId',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20230630_models.GenerateDeviceByBatchIdResponse(),
            self.call_api(params, req, runtime)
        )

    def generate_device_by_batch_id(self, request):
        runtime = util_models.RuntimeOptions()
        return self.generate_device_by_batch_id_with_options(request, runtime)

    def query_batch_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.batch_id):
            query['BatchId'] = request.batch_id
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryBatchStatus',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20230630_models.QueryBatchStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def query_batch_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_batch_status_with_options(request, runtime)

    def query_devices_download_url_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.batch_id):
            query['BatchId'] = request.batch_id
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryDevicesDownloadUrl',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20230630_models.QueryDevicesDownloadUrlResponse(),
            self.call_api(params, req, runtime)
        )

    def query_devices_download_url(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_devices_download_url_with_options(request, runtime)

    def query_free_storage_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.device_name):
            query['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.iot_id):
            query['IotId'] = request.iot_id
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryFreeStorage',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20230630_models.QueryFreeStorageResponse(),
            self.call_api(params, req, runtime)
        )

    def query_free_storage(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_free_storage_with_options(request, runtime)

    def query_generate_devices_info_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.batch_id):
            query['BatchId'] = request.batch_id
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryGenerateDevicesInfoList',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20230630_models.QueryGenerateDevicesInfoListResponse(),
            self.call_api(params, req, runtime)
        )

    def query_generate_devices_info_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_generate_devices_info_list_with_options(request, runtime)

    def query_generate_devices_record_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
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
            action='QueryGenerateDevicesRecord',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20230630_models.QueryGenerateDevicesRecordResponse(),
            self.call_api(params, req, runtime)
        )

    def query_generate_devices_record(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_generate_devices_record_with_options(request, runtime)

    def query_storage_commodity_list_with_options(self, runtime):
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='QueryStorageCommodityList',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20230630_models.QueryStorageCommodityListResponse(),
            self.call_api(params, req, runtime)
        )

    def query_storage_commodity_list(self):
        runtime = util_models.RuntimeOptions()
        return self.query_storage_commodity_list_with_options(runtime)

    def query_storage_order_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.device_name):
            query['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.device_no_owner):
            query['DeviceNoOwner'] = request.device_no_owner
        if not UtilClient.is_unset(request.iot_id):
            query['IotId'] = request.iot_id
        if not UtilClient.is_unset(request.order_id):
            query['OrderId'] = request.order_id
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryStorageOrder',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20230630_models.QueryStorageOrderResponse(),
            self.call_api(params, req, runtime)
        )

    def query_storage_order(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_storage_order_with_options(request, runtime)

    def query_storage_order_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.device_name):
            query['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.device_no_owner):
            query['DeviceNoOwner'] = request.device_no_owner
        if not UtilClient.is_unset(request.iot_id):
            query['IotId'] = request.iot_id
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
            action='QueryStorageOrderList',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20230630_models.QueryStorageOrderListResponse(),
            self.call_api(params, req, runtime)
        )

    def query_storage_order_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_storage_order_list_with_options(request, runtime)

    def transfer_storage_order_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dst_iot_id):
            query['DstIotId'] = request.dst_iot_id
        if not UtilClient.is_unset(request.enable_default_plan):
            query['EnableDefaultPlan'] = request.enable_default_plan
        if not UtilClient.is_unset(request.event_record_duration):
            query['EventRecordDuration'] = request.event_record_duration
        if not UtilClient.is_unset(request.event_record_prolong):
            query['EventRecordProlong'] = request.event_record_prolong
        if not UtilClient.is_unset(request.immediate_use):
            query['ImmediateUse'] = request.immediate_use
        if not UtilClient.is_unset(request.pre_record_duration):
            query['PreRecordDuration'] = request.pre_record_duration
        if not UtilClient.is_unset(request.src_iot_id):
            query['SrcIotId'] = request.src_iot_id
        if not UtilClient.is_unset(request.src_order_id):
            query['SrcOrderId'] = request.src_order_id
        if not UtilClient.is_unset(request.support_cross_identity_transfer):
            query['SupportCrossIdentityTransfer'] = request.support_cross_identity_transfer
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        if not UtilClient.is_unset(request.user_name):
            query['UserName'] = request.user_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TransferStorageOrder',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20230630_models.TransferStorageOrderResponse(),
            self.call_api(params, req, runtime)
        )

    def transfer_storage_order(self, request):
        runtime = util_models.RuntimeOptions()
        return self.transfer_storage_order_with_options(request, runtime)

    def upload_device_name_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        if not UtilClient.is_unset(request.project_id):
            query['ProjectId'] = request.project_id
        body = {}
        if not UtilClient.is_unset(request.device_names):
            body['DeviceNames'] = request.device_names
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UploadDeviceNameList',
            version='2023-06-30',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20230630_models.UploadDeviceNameListResponse(),
            self.call_api(params, req, runtime)
        )

    def upload_device_name_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.upload_device_name_list_with_options(request, runtime)
