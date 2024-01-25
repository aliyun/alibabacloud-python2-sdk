# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_cloudesl20200201 import models as cloudesl_20200201_models
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
            'ap-northeast-1': 'cloudesl.aliyuncs.com',
            'ap-northeast-2-pop': 'cloudesl.aliyuncs.com',
            'ap-south-1': 'cloudesl.aliyuncs.com',
            'ap-southeast-1': 'cloudesl.aliyuncs.com',
            'ap-southeast-2': 'cloudesl.aliyuncs.com',
            'ap-southeast-3': 'cloudesl.aliyuncs.com',
            'ap-southeast-5': 'cloudesl.aliyuncs.com',
            'cn-beijing': 'cloudesl.aliyuncs.com',
            'cn-beijing-finance-1': 'cloudesl.aliyuncs.com',
            'cn-beijing-finance-pop': 'cloudesl.aliyuncs.com',
            'cn-beijing-gov-1': 'cloudesl.aliyuncs.com',
            'cn-beijing-nu16-b01': 'cloudesl.aliyuncs.com',
            'cn-chengdu': 'cloudesl.aliyuncs.com',
            'cn-edge-1': 'cloudesl.aliyuncs.com',
            'cn-fujian': 'cloudesl.aliyuncs.com',
            'cn-haidian-cm12-c01': 'cloudesl.aliyuncs.com',
            'cn-hangzhou-bj-b01': 'cloudesl.aliyuncs.com',
            'cn-hangzhou-finance': 'cloudesl.aliyuncs.com',
            'cn-hangzhou-internal-prod-1': 'cloudesl.aliyuncs.com',
            'cn-hangzhou-internal-test-1': 'cloudesl.aliyuncs.com',
            'cn-hangzhou-internal-test-2': 'cloudesl.aliyuncs.com',
            'cn-hangzhou-internal-test-3': 'cloudesl.aliyuncs.com',
            'cn-hangzhou-test-306': 'cloudesl.aliyuncs.com',
            'cn-hongkong': 'cloudesl.aliyuncs.com',
            'cn-hongkong-finance-pop': 'cloudesl.aliyuncs.com',
            'cn-huhehaote': 'cloudesl.aliyuncs.com',
            'cn-north-2-gov-1': 'cloudesl.aliyuncs.com',
            'cn-qingdao': 'cloudesl.aliyuncs.com',
            'cn-qingdao-nebula': 'cloudesl.aliyuncs.com',
            'cn-shanghai': 'cloudesl.aliyuncs.com',
            'cn-shanghai-et15-b01': 'cloudesl.aliyuncs.com',
            'cn-shanghai-et2-b01': 'cloudesl.aliyuncs.com',
            'cn-shanghai-finance-1': 'cloudesl.aliyuncs.com',
            'cn-shanghai-inner': 'cloudesl.aliyuncs.com',
            'cn-shanghai-internal-test-1': 'cloudesl.aliyuncs.com',
            'cn-shenzhen': 'cloudesl.aliyuncs.com',
            'cn-shenzhen-finance-1': 'cloudesl.aliyuncs.com',
            'cn-shenzhen-inner': 'cloudesl.aliyuncs.com',
            'cn-shenzhen-st4-d01': 'cloudesl.aliyuncs.com',
            'cn-shenzhen-su18-b01': 'cloudesl.aliyuncs.com',
            'cn-wuhan': 'cloudesl.aliyuncs.com',
            'cn-yushanfang': 'cloudesl.aliyuncs.com',
            'cn-zhangbei-na61-b01': 'cloudesl.aliyuncs.com',
            'cn-zhangjiakou': 'cloudesl.aliyuncs.com',
            'cn-zhangjiakou-na62-a01': 'cloudesl.aliyuncs.com',
            'cn-zhengzhou-nebula-1': 'cloudesl.aliyuncs.com',
            'eu-central-1': 'cloudesl.aliyuncs.com',
            'eu-west-1': 'cloudesl.aliyuncs.com',
            'eu-west-1-oxs': 'cloudesl.aliyuncs.com',
            'me-east-1': 'cloudesl.aliyuncs.com',
            'rus-west-1-pop': 'cloudesl.aliyuncs.com',
            'us-east-1': 'cloudesl.aliyuncs.com',
            'us-west-1': 'cloudesl.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('cloudesl', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def activate_ap_device_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ap_mac):
            body['ApMac'] = request.ap_mac
        if not UtilClient.is_unset(request.extra_params):
            body['ExtraParams'] = request.extra_params
        if not UtilClient.is_unset(request.store_id):
            body['StoreId'] = request.store_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ActivateApDevice',
            version='2020-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudesl_20200201_models.ActivateApDeviceResponse(),
            self.call_api(params, req, runtime)
        )

    def activate_ap_device(self, request):
        runtime = util_models.RuntimeOptions()
        return self.activate_ap_device_with_options(request, runtime)

    def add_ap_device_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ap_mac):
            body['ApMac'] = request.ap_mac
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.extra_params):
            body['ExtraParams'] = request.extra_params
        if not UtilClient.is_unset(request.remark):
            body['Remark'] = request.remark
        if not UtilClient.is_unset(request.serial_number):
            body['SerialNumber'] = request.serial_number
        if not UtilClient.is_unset(request.store_id):
            body['StoreId'] = request.store_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddApDevice',
            version='2020-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudesl_20200201_models.AddApDeviceResponse(),
            self.call_api(params, req, runtime)
        )

    def add_ap_device(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_ap_device_with_options(request, runtime)

    def add_company_template_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.device_type):
            body['DeviceType'] = request.device_type
        if not UtilClient.is_unset(request.esl_size):
            body['EslSize'] = request.esl_size
        if not UtilClient.is_unset(request.extra_params):
            body['ExtraParams'] = request.extra_params
        if not UtilClient.is_unset(request.group_id):
            body['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.if_default):
            body['IfDefault'] = request.if_default
        if not UtilClient.is_unset(request.if_member):
            body['IfMember'] = request.if_member
        if not UtilClient.is_unset(request.if_out_of_inventory):
            body['IfOutOfInventory'] = request.if_out_of_inventory
        if not UtilClient.is_unset(request.if_promotion):
            body['IfPromotion'] = request.if_promotion
        if not UtilClient.is_unset(request.if_source_code):
            body['IfSourceCode'] = request.if_source_code
        if not UtilClient.is_unset(request.layout):
            body['Layout'] = request.layout
        if not UtilClient.is_unset(request.scene):
            body['Scene'] = request.scene
        if not UtilClient.is_unset(request.template_name):
            body['TemplateName'] = request.template_name
        if not UtilClient.is_unset(request.template_scene_id):
            body['TemplateSceneId'] = request.template_scene_id
        if not UtilClient.is_unset(request.template_type):
            body['TemplateType'] = request.template_type
        if not UtilClient.is_unset(request.template_version):
            body['TemplateVersion'] = request.template_version
        if not UtilClient.is_unset(request.vendor):
            body['Vendor'] = request.vendor
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddCompanyTemplate',
            version='2020-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudesl_20200201_models.AddCompanyTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    def add_company_template(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_company_template_with_options(request, runtime)

    def add_user_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.extra_params):
            body['ExtraParams'] = request.extra_params
        if not UtilClient.is_unset(request.user_id):
            body['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddUser',
            version='2020-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudesl_20200201_models.AddUserResponse(),
            self.call_api(params, req, runtime)
        )

    def add_user(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_user_with_options(request, runtime)

    def apply_company_template_version_to_stores_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.stores):
            body['Stores'] = request.stores
        if not UtilClient.is_unset(request.template_version):
            body['TemplateVersion'] = request.template_version
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ApplyCompanyTemplateVersionToStores',
            version='2020-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudesl_20200201_models.ApplyCompanyTemplateVersionToStoresResponse(),
            self.call_api(params, req, runtime)
        )

    def apply_company_template_version_to_stores(self, request):
        runtime = util_models.RuntimeOptions()
        return self.apply_company_template_version_to_stores_with_options(request, runtime)

    def assign_user_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.extra_params):
            body['ExtraParams'] = request.extra_params
        if not UtilClient.is_unset(request.stores):
            body['Stores'] = request.stores
        if not UtilClient.is_unset(request.user_id):
            body['UserId'] = request.user_id
        if not UtilClient.is_unset(request.user_type):
            body['UserType'] = request.user_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AssignUser',
            version='2020-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudesl_20200201_models.AssignUserResponse(),
            self.call_api(params, req, runtime)
        )

    def assign_user(self, request):
        runtime = util_models.RuntimeOptions()
        return self.assign_user_with_options(request, runtime)

    def batch_insert_items_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.extra_params):
            body['ExtraParams'] = request.extra_params
        if not UtilClient.is_unset(request.item_info):
            body['ItemInfo'] = request.item_info
        if not UtilClient.is_unset(request.store_id):
            body['StoreId'] = request.store_id
        if not UtilClient.is_unset(request.sync_by_item_id):
            body['SyncByItemId'] = request.sync_by_item_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='BatchInsertItems',
            version='2020-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudesl_20200201_models.BatchInsertItemsResponse(),
            self.call_api(params, req, runtime)
        )

    def batch_insert_items(self, request):
        runtime = util_models.RuntimeOptions()
        return self.batch_insert_items_with_options(request, runtime)

    def bind_esl_device_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.column):
            body['Column'] = request.column
        if not UtilClient.is_unset(request.container_id):
            body['ContainerId'] = request.container_id
        if not UtilClient.is_unset(request.container_name):
            body['ContainerName'] = request.container_name
        if not UtilClient.is_unset(request.esl_bar_code):
            body['EslBarCode'] = request.esl_bar_code
        if not UtilClient.is_unset(request.extra_params):
            body['ExtraParams'] = request.extra_params
        if not UtilClient.is_unset(request.item_bar_code):
            body['ItemBarCode'] = request.item_bar_code
        if not UtilClient.is_unset(request.layer):
            body['Layer'] = request.layer
        if not UtilClient.is_unset(request.layout_id):
            body['LayoutId'] = request.layout_id
        if not UtilClient.is_unset(request.layout_name):
            body['LayoutName'] = request.layout_name
        if not UtilClient.is_unset(request.shelf):
            body['Shelf'] = request.shelf
        if not UtilClient.is_unset(request.store_id):
            body['StoreId'] = request.store_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='BindEslDevice',
            version='2020-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudesl_20200201_models.BindEslDeviceResponse(),
            self.call_api(params, req, runtime)
        )

    def bind_esl_device(self, request):
        runtime = util_models.RuntimeOptions()
        return self.bind_esl_device_with_options(request, runtime)

    def create_store_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.auto_unbind_days):
            body['AutoUnbindDays'] = request.auto_unbind_days
        if not UtilClient.is_unset(request.auto_unbind_offline_esl):
            body['AutoUnbindOfflineEsl'] = request.auto_unbind_offline_esl
        if not UtilClient.is_unset(request.bar_code_encode):
            body['BarCodeEncode'] = request.bar_code_encode
        if not UtilClient.is_unset(request.client_token):
            body['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.extra_params):
            body['ExtraParams'] = request.extra_params
        if not UtilClient.is_unset(request.parent_id):
            body['ParentId'] = request.parent_id
        if not UtilClient.is_unset(request.phone):
            body['Phone'] = request.phone
        if not UtilClient.is_unset(request.store_name):
            body['StoreName'] = request.store_name
        if not UtilClient.is_unset(request.time_zone):
            body['TimeZone'] = request.time_zone
        if not UtilClient.is_unset(request.user_store_code):
            body['UserStoreCode'] = request.user_store_code
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateStore',
            version='2020-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudesl_20200201_models.CreateStoreResponse(),
            self.call_api(params, req, runtime)
        )

    def create_store(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_store_with_options(request, runtime)

    def delete_ap_device_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ap_mac):
            body['ApMac'] = request.ap_mac
        if not UtilClient.is_unset(request.extra_params):
            body['ExtraParams'] = request.extra_params
        if not UtilClient.is_unset(request.store_id):
            body['StoreId'] = request.store_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteApDevice',
            version='2020-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudesl_20200201_models.DeleteApDeviceResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_ap_device(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_ap_device_with_options(request, runtime)

    def delete_company_template_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.extra_params):
            body['ExtraParams'] = request.extra_params
        if not UtilClient.is_unset(request.template_id):
            body['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteCompanyTemplate',
            version='2020-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudesl_20200201_models.DeleteCompanyTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_company_template(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_company_template_with_options(request, runtime)

    def delete_item_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.item_bar_code):
            body['ItemBarCode'] = request.item_bar_code
        if not UtilClient.is_unset(request.store_id):
            body['StoreId'] = request.store_id
        if not UtilClient.is_unset(request.unbind_esl_device):
            body['UnbindEslDevice'] = request.unbind_esl_device
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteItem',
            version='2020-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudesl_20200201_models.DeleteItemResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_item(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_item_with_options(request, runtime)

    def delete_store_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.extra_params):
            body['ExtraParams'] = request.extra_params
        if not UtilClient.is_unset(request.store_id):
            body['StoreId'] = request.store_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteStore',
            version='2020-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudesl_20200201_models.DeleteStoreResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_store(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_store_with_options(request, runtime)

    def delete_user_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.extra_params):
            body['ExtraParams'] = request.extra_params
        if not UtilClient.is_unset(request.user_id):
            body['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteUser',
            version='2020-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudesl_20200201_models.DeleteUserResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_user(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_user_with_options(request, runtime)

    def describe_ap_devices_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.ap_mac):
            body['ApMac'] = request.ap_mac
        if not UtilClient.is_unset(request.be_activate):
            body['BeActivate'] = request.be_activate
        if not UtilClient.is_unset(request.extra_params):
            body['ExtraParams'] = request.extra_params
        if not UtilClient.is_unset(request.model):
            body['Model'] = request.model
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        if not UtilClient.is_unset(request.store_id):
            body['StoreId'] = request.store_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeApDevices',
            version='2020-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudesl_20200201_models.DescribeApDevicesResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_ap_devices(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_ap_devices_with_options(request, runtime)

    def describe_available_esl_models_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.model_id):
            body['ModelId'] = request.model_id
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeAvailableEslModels',
            version='2020-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudesl_20200201_models.DescribeAvailableEslModelsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_available_esl_models(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_available_esl_models_with_options(request, runtime)

    def describe_binders_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.esl_bar_code):
            body['EslBarCode'] = request.esl_bar_code
        if not UtilClient.is_unset(request.extra_params):
            body['ExtraParams'] = request.extra_params
        if not UtilClient.is_unset(request.item_bar_code):
            body['ItemBarCode'] = request.item_bar_code
        if not UtilClient.is_unset(request.item_title):
            body['ItemTitle'] = request.item_title
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.store_id):
            body['StoreId'] = request.store_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeBinders',
            version='2020-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudesl_20200201_models.DescribeBindersResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_binders(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_binders_with_options(request, runtime)

    def describe_company_template_versions_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeCompanyTemplateVersions',
            version='2020-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudesl_20200201_models.DescribeCompanyTemplateVersionsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_company_template_versions(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_company_template_versions_with_options(request, runtime)

    def describe_esl_device_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.from_date):
            body['FromDate'] = request.from_date
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.store_id):
            body['StoreId'] = request.store_id
        if not UtilClient.is_unset(request.to_date):
            body['ToDate'] = request.to_date
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeEslDevice',
            version='2020-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudesl_20200201_models.DescribeEslDeviceResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_esl_device(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_esl_device_with_options(request, runtime)

    def describe_esl_devices_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.esl_bar_code):
            body['EslBarCode'] = request.esl_bar_code
        if not UtilClient.is_unset(request.esl_status):
            body['EslStatus'] = request.esl_status
        if not UtilClient.is_unset(request.extra_params):
            body['ExtraParams'] = request.extra_params
        if not UtilClient.is_unset(request.from_battery_level):
            body['FromBatteryLevel'] = request.from_battery_level
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.store_id):
            body['StoreId'] = request.store_id
        if not UtilClient.is_unset(request.to_battery_level):
            body['ToBatteryLevel'] = request.to_battery_level
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        if not UtilClient.is_unset(request.type_encode):
            body['TypeEncode'] = request.type_encode
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeEslDevices',
            version='2020-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudesl_20200201_models.DescribeEslDevicesResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_esl_devices(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_esl_devices_with_options(request, runtime)

    def describe_esl_model_by_template_version_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.template_version):
            body['TemplateVersion'] = request.template_version
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeEslModelByTemplateVersion',
            version='2020-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudesl_20200201_models.DescribeEslModelByTemplateVersionResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_esl_model_by_template_version(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_esl_model_by_template_version_with_options(request, runtime)

    def describe_items_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.be_promotion):
            body['BePromotion'] = request.be_promotion
        if not UtilClient.is_unset(request.extra_params):
            body['ExtraParams'] = request.extra_params
        if not UtilClient.is_unset(request.item_bar_code):
            body['ItemBarCode'] = request.item_bar_code
        if not UtilClient.is_unset(request.item_id):
            body['ItemId'] = request.item_id
        if not UtilClient.is_unset(request.item_title):
            body['ItemTitle'] = request.item_title
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.sku_id):
            body['SkuId'] = request.sku_id
        if not UtilClient.is_unset(request.store_id):
            body['StoreId'] = request.store_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeItems',
            version='2020-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudesl_20200201_models.DescribeItemsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_items(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_items_with_options(request, runtime)

    def describe_store_by_template_version_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.template_version):
            body['TemplateVersion'] = request.template_version
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeStoreByTemplateVersion',
            version='2020-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudesl_20200201_models.DescribeStoreByTemplateVersionResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_store_by_template_version(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_store_by_template_version_with_options(request, runtime)

    def describe_store_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.extra_params):
            body['ExtraParams'] = request.extra_params
        if not UtilClient.is_unset(request.store_id):
            body['StoreId'] = request.store_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeStoreConfig',
            version='2020-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudesl_20200201_models.DescribeStoreConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_store_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_store_config_with_options(request, runtime)

    def describe_stores_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.extra_params):
            body['ExtraParams'] = request.extra_params
        if not UtilClient.is_unset(request.from_date):
            body['FromDate'] = request.from_date
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.store_id):
            body['StoreId'] = request.store_id
        if not UtilClient.is_unset(request.store_name):
            body['StoreName'] = request.store_name
        if not UtilClient.is_unset(request.template_version):
            body['TemplateVersion'] = request.template_version
        if not UtilClient.is_unset(request.to_date):
            body['ToDate'] = request.to_date
        if not UtilClient.is_unset(request.user_store_code):
            body['UserStoreCode'] = request.user_store_code
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeStores',
            version='2020-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudesl_20200201_models.DescribeStoresResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_stores(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_stores_with_options(request, runtime)

    def describe_template_by_model_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.device_type):
            body['DeviceType'] = request.device_type
        if not UtilClient.is_unset(request.esl_size):
            body['EslSize'] = request.esl_size
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.template_version):
            body['TemplateVersion'] = request.template_version
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeTemplateByModel',
            version='2020-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudesl_20200201_models.DescribeTemplateByModelResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_template_by_model(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_template_by_model_with_options(request, runtime)

    def describe_user_log_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.esl_bar_code):
            body['EslBarCode'] = request.esl_bar_code
        if not UtilClient.is_unset(request.extra_params):
            body['ExtraParams'] = request.extra_params
        if not UtilClient.is_unset(request.from_date):
            body['FromDate'] = request.from_date
        if not UtilClient.is_unset(request.item_bar_code):
            body['ItemBarCode'] = request.item_bar_code
        if not UtilClient.is_unset(request.item_short_title):
            body['ItemShortTitle'] = request.item_short_title
        if not UtilClient.is_unset(request.log_id):
            body['LogId'] = request.log_id
        if not UtilClient.is_unset(request.operation_status):
            body['OperationStatus'] = request.operation_status
        if not UtilClient.is_unset(request.operation_type):
            body['OperationType'] = request.operation_type
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.store_id):
            body['StoreId'] = request.store_id
        if not UtilClient.is_unset(request.to_date):
            body['ToDate'] = request.to_date
        if not UtilClient.is_unset(request.user_id):
            body['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeUserLog',
            version='2020-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudesl_20200201_models.DescribeUserLogResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_user_log(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_user_log_with_options(request, runtime)

    def describe_users_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.extra_params):
            body['ExtraParams'] = request.extra_params
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.user_id):
            body['UserId'] = request.user_id
        if not UtilClient.is_unset(request.user_name):
            body['UserName'] = request.user_name
        if not UtilClient.is_unset(request.user_type):
            body['UserType'] = request.user_type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeUsers',
            version='2020-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudesl_20200201_models.DescribeUsersResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_users(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_users_with_options(request, runtime)

    def get_user_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.extra_params):
            body['ExtraParams'] = request.extra_params
        if not UtilClient.is_unset(request.user_id):
            body['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetUser',
            version='2020-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudesl_20200201_models.GetUserResponse(),
            self.call_api(params, req, runtime)
        )

    def get_user(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_user_with_options(request, runtime)

    def query_template_list_by_group_id_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.group_id):
            body['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryTemplateListByGroupId',
            version='2020-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudesl_20200201_models.QueryTemplateListByGroupIdResponse(),
            self.call_api(params, req, runtime)
        )

    def query_template_list_by_group_id(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_template_list_by_group_id_with_options(request, runtime)

    def sync_add_material_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.content):
            body['Content'] = request.content
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SyncAddMaterial',
            version='2020-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudesl_20200201_models.SyncAddMaterialResponse(),
            self.call_api(params, req, runtime)
        )

    def sync_add_material(self, request):
        runtime = util_models.RuntimeOptions()
        return self.sync_add_material_with_options(request, runtime)

    def unassign_user_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.extra_params):
            body['ExtraParams'] = request.extra_params
        if not UtilClient.is_unset(request.user_id):
            body['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UnassignUser',
            version='2020-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudesl_20200201_models.UnassignUserResponse(),
            self.call_api(params, req, runtime)
        )

    def unassign_user(self, request):
        runtime = util_models.RuntimeOptions()
        return self.unassign_user_with_options(request, runtime)

    def unbind_esl_device_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.column):
            body['Column'] = request.column
        if not UtilClient.is_unset(request.container_name):
            body['ContainerName'] = request.container_name
        if not UtilClient.is_unset(request.esl_bar_code):
            body['EslBarCode'] = request.esl_bar_code
        if not UtilClient.is_unset(request.extra_params):
            body['ExtraParams'] = request.extra_params
        if not UtilClient.is_unset(request.item_bar_code):
            body['ItemBarCode'] = request.item_bar_code
        if not UtilClient.is_unset(request.layer):
            body['Layer'] = request.layer
        if not UtilClient.is_unset(request.shelf):
            body['Shelf'] = request.shelf
        if not UtilClient.is_unset(request.store_id):
            body['StoreId'] = request.store_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UnbindEslDevice',
            version='2020-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudesl_20200201_models.UnbindEslDeviceResponse(),
            self.call_api(params, req, runtime)
        )

    def unbind_esl_device(self, request):
        runtime = util_models.RuntimeOptions()
        return self.unbind_esl_device_with_options(request, runtime)

    def update_esl_device_light_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.esl_bar_code):
            body['EslBarCode'] = request.esl_bar_code
        if not UtilClient.is_unset(request.extra_params):
            body['ExtraParams'] = request.extra_params
        if not UtilClient.is_unset(request.frequency):
            body['Frequency'] = request.frequency
        if not UtilClient.is_unset(request.item_bar_code):
            body['ItemBarCode'] = request.item_bar_code
        if not UtilClient.is_unset(request.led_color):
            body['LedColor'] = request.led_color
        if not UtilClient.is_unset(request.light_up_time):
            body['LightUpTime'] = request.light_up_time
        if not UtilClient.is_unset(request.store_id):
            body['StoreId'] = request.store_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateEslDeviceLight',
            version='2020-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudesl_20200201_models.UpdateEslDeviceLightResponse(),
            self.call_api(params, req, runtime)
        )

    def update_esl_device_light(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_esl_device_light_with_options(request, runtime)

    def update_store_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.auto_unbind_days):
            body['AutoUnbindDays'] = request.auto_unbind_days
        if not UtilClient.is_unset(request.auto_unbind_offline_esl):
            body['AutoUnbindOfflineEsl'] = request.auto_unbind_offline_esl
        if not UtilClient.is_unset(request.bar_code_encode):
            body['BarCodeEncode'] = request.bar_code_encode
        if not UtilClient.is_unset(request.extra_params):
            body['ExtraParams'] = request.extra_params
        if not UtilClient.is_unset(request.phone):
            body['Phone'] = request.phone
        if not UtilClient.is_unset(request.store_id):
            body['StoreId'] = request.store_id
        if not UtilClient.is_unset(request.store_name):
            body['StoreName'] = request.store_name
        if not UtilClient.is_unset(request.template_version):
            body['TemplateVersion'] = request.template_version
        if not UtilClient.is_unset(request.timezone):
            body['Timezone'] = request.timezone
        if not UtilClient.is_unset(request.user_store_code):
            body['UserStoreCode'] = request.user_store_code
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateStore',
            version='2020-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudesl_20200201_models.UpdateStoreResponse(),
            self.call_api(params, req, runtime)
        )

    def update_store(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_store_with_options(request, runtime)

    def update_store_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.enable_notification):
            body['EnableNotification'] = request.enable_notification
        if not UtilClient.is_unset(request.extra_params):
            body['ExtraParams'] = request.extra_params
        if not UtilClient.is_unset(request.notification_silent_times):
            body['NotificationSilentTimes'] = request.notification_silent_times
        if not UtilClient.is_unset(request.notification_web_hook):
            body['NotificationWebHook'] = request.notification_web_hook
        if not UtilClient.is_unset(request.store_id):
            body['StoreId'] = request.store_id
        if not UtilClient.is_unset(request.subscribe_contents):
            body['SubscribeContents'] = request.subscribe_contents
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateStoreConfig',
            version='2020-02-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            cloudesl_20200201_models.UpdateStoreConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def update_store_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_store_config_with_options(request, runtime)
