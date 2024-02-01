# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_linkvisual20180120 import models as linkvisual_20180120_models
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

    def add_event_record_plan_device_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.device_name):
            query['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.iot_id):
            query['IotId'] = request.iot_id
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.plan_id):
            query['PlanId'] = request.plan_id
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        if not UtilClient.is_unset(request.stream_type):
            query['StreamType'] = request.stream_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddEventRecordPlanDevice',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.AddEventRecordPlanDeviceResponse(),
            self.call_api(params, req, runtime)
        )

    def add_event_record_plan_device(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_event_record_plan_device_with_options(request, runtime)

    def add_face_device_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.device_group_name):
            query['DeviceGroupName'] = request.device_group_name
        if not UtilClient.is_unset(request.isolation_id):
            query['IsolationId'] = request.isolation_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddFaceDeviceGroup',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.AddFaceDeviceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def add_face_device_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_face_device_group_with_options(request, runtime)

    def add_face_device_to_device_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.device_group_id):
            query['DeviceGroupId'] = request.device_group_id
        if not UtilClient.is_unset(request.device_name):
            query['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.isolation_id):
            query['IsolationId'] = request.isolation_id
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddFaceDeviceToDeviceGroup',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.AddFaceDeviceToDeviceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def add_face_device_to_device_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_face_device_to_device_group_with_options(request, runtime)

    def add_face_user_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.custom_user_id):
            query['CustomUserId'] = request.custom_user_id
        if not UtilClient.is_unset(request.face_pic_url):
            query['FacePicUrl'] = request.face_pic_url
        if not UtilClient.is_unset(request.isolation_id):
            query['IsolationId'] = request.isolation_id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.params):
            query['Params'] = request.params
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddFaceUser',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.AddFaceUserResponse(),
            self.call_api(params, req, runtime)
        )

    def add_face_user(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_face_user_with_options(request, runtime)

    def add_face_user_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.isolation_id):
            query['IsolationId'] = request.isolation_id
        if not UtilClient.is_unset(request.user_group_name):
            query['UserGroupName'] = request.user_group_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddFaceUserGroup',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.AddFaceUserGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def add_face_user_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_face_user_group_with_options(request, runtime)

    def add_face_user_group_and_device_group_relation_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.device_group_id):
            query['DeviceGroupId'] = request.device_group_id
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.isolation_id):
            query['IsolationId'] = request.isolation_id
        if not UtilClient.is_unset(request.relation):
            query['Relation'] = request.relation
        if not UtilClient.is_unset(request.user_group_id):
            query['UserGroupId'] = request.user_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddFaceUserGroupAndDeviceGroupRelation',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.AddFaceUserGroupAndDeviceGroupRelationResponse(),
            self.call_api(params, req, runtime)
        )

    def add_face_user_group_and_device_group_relation(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_face_user_group_and_device_group_relation_with_options(request, runtime)

    def add_face_user_picture_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.face_pic_url):
            query['FacePicUrl'] = request.face_pic_url
        if not UtilClient.is_unset(request.isolation_id):
            query['IsolationId'] = request.isolation_id
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddFaceUserPicture',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.AddFaceUserPictureResponse(),
            self.call_api(params, req, runtime)
        )

    def add_face_user_picture(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_face_user_picture_with_options(request, runtime)

    def add_face_user_to_user_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.isolation_id):
            query['IsolationId'] = request.isolation_id
        if not UtilClient.is_unset(request.user_group_id):
            query['UserGroupId'] = request.user_group_id
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddFaceUserToUserGroup',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.AddFaceUserToUserGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def add_face_user_to_user_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_face_user_to_user_group_with_options(request, runtime)

    def add_record_plan_device_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.device_name):
            query['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.iot_id):
            query['IotId'] = request.iot_id
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.plan_id):
            query['PlanId'] = request.plan_id
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        if not UtilClient.is_unset(request.stream_type):
            query['StreamType'] = request.stream_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddRecordPlanDevice',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.AddRecordPlanDeviceResponse(),
            self.call_api(params, req, runtime)
        )

    def add_record_plan_device(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_record_plan_device_with_options(request, runtime)

    def batch_query_vision_device_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.device_name_list):
            query['DeviceNameList'] = request.device_name_list
        if not UtilClient.is_unset(request.iot_id_list):
            query['IotIdList'] = request.iot_id_list
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BatchQueryVisionDeviceInfo',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.BatchQueryVisionDeviceInfoResponse(),
            self.call_api(params, req, runtime)
        )

    def batch_query_vision_device_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.batch_query_vision_device_info_with_options(request, runtime)

    def bind_picture_search_app_with_devices_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_instance_id):
            query['AppInstanceId'] = request.app_instance_id
        if not UtilClient.is_unset(request.device_iot_ids):
            query['DeviceIotIds'] = request.device_iot_ids
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BindPictureSearchAppWithDevices',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.BindPictureSearchAppWithDevicesResponse(),
            self.call_api(params, req, runtime)
        )

    def bind_picture_search_app_with_devices(self, request):
        runtime = util_models.RuntimeOptions()
        return self.bind_picture_search_app_with_devices_with_options(request, runtime)

    def check_face_user_do_exist_on_device_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.device_name):
            query['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.isolation_id):
            query['IsolationId'] = request.isolation_id
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CheckFaceUserDoExistOnDevice',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.CheckFaceUserDoExistOnDeviceResponse(),
            self.call_api(params, req, runtime)
        )

    def check_face_user_do_exist_on_device(self, request):
        runtime = util_models.RuntimeOptions()
        return self.check_face_user_do_exist_on_device_with_options(request, runtime)

    def clear_face_device_dbwith_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.device_name):
            query['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.isolation_id):
            query['IsolationId'] = request.isolation_id
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ClearFaceDeviceDB',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.ClearFaceDeviceDBResponse(),
            self.call_api(params, req, runtime)
        )

    def clear_face_device_db(self, request):
        runtime = util_models.RuntimeOptions()
        return self.clear_face_device_dbwith_options(request, runtime)

    def create_event_record_plan_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.event_types):
            query['EventTypes'] = request.event_types
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.pre_record_duration):
            query['PreRecordDuration'] = request.pre_record_duration
        if not UtilClient.is_unset(request.record_duration):
            query['RecordDuration'] = request.record_duration
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateEventRecordPlan',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.CreateEventRecordPlanResponse(),
            self.call_api(params, req, runtime)
        )

    def create_event_record_plan(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_event_record_plan_with_options(request, runtime)

    def create_gb_device_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.device_name):
            query['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.device_type):
            query['DeviceType'] = request.device_type
        if not UtilClient.is_unset(request.gb_id):
            query['GbId'] = request.gb_id
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.media_net_protocol):
            query['MediaNetProtocol'] = request.media_net_protocol
        if not UtilClient.is_unset(request.password):
            query['Password'] = request.password
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        if not UtilClient.is_unset(request.sub_product_key):
            query['SubProductKey'] = request.sub_product_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateGbDevice',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.CreateGbDeviceResponse(),
            self.call_api(params, req, runtime)
        )

    def create_gb_device(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_gb_device_with_options(request, runtime)

    def create_local_file_upload_job_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.time_slot):
            query['TimeSlot'] = request.time_slot
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateLocalFileUploadJob',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.CreateLocalFileUploadJobResponse(),
            self.call_api(params, req, runtime)
        )

    def create_local_file_upload_job(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_local_file_upload_job_with_options(request, runtime)

    def create_local_record_download_by_time_job_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.begin_time):
            query['BeginTime'] = request.begin_time
        if not UtilClient.is_unset(request.device_name):
            query['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.iot_id):
            query['IotId'] = request.iot_id
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        if not UtilClient.is_unset(request.speed):
            query['Speed'] = request.speed
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateLocalRecordDownloadByTimeJob',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.CreateLocalRecordDownloadByTimeJobResponse(),
            self.call_api(params, req, runtime)
        )

    def create_local_record_download_by_time_job(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_local_record_download_by_time_job_with_options(request, runtime)

    def create_picture_search_app_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.desc):
            query['Desc'] = request.desc
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreatePictureSearchApp',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.CreatePictureSearchAppResponse(),
            self.call_api(params, req, runtime)
        )

    def create_picture_search_app(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_picture_search_app_with_options(request, runtime)

    def create_picture_search_job_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_instance_id):
            query['AppInstanceId'] = request.app_instance_id
        if not UtilClient.is_unset(request.body_threshold):
            query['BodyThreshold'] = request.body_threshold
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.picture_search_type):
            query['PictureSearchType'] = request.picture_search_type
        if not UtilClient.is_unset(request.search_pic_url):
            query['SearchPicUrl'] = request.search_pic_url
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.threshold):
            query['Threshold'] = request.threshold
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreatePictureSearchJob',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.CreatePictureSearchJobResponse(),
            self.call_api(params, req, runtime)
        )

    def create_picture_search_job(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_picture_search_job_with_options(request, runtime)

    def create_record_download_by_time_job_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.begin_time):
            query['BeginTime'] = request.begin_time
        if not UtilClient.is_unset(request.device_name):
            query['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.iot_id):
            query['IotId'] = request.iot_id
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        if not UtilClient.is_unset(request.record_type):
            query['RecordType'] = request.record_type
        if not UtilClient.is_unset(request.stream_type):
            query['StreamType'] = request.stream_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateRecordDownloadByTimeJob',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.CreateRecordDownloadByTimeJobResponse(),
            self.call_api(params, req, runtime)
        )

    def create_record_download_by_time_job(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_record_download_by_time_job_with_options(request, runtime)

    def create_record_plan_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateRecordPlan',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.CreateRecordPlanResponse(),
            self.call_api(params, req, runtime)
        )

    def create_record_plan(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_record_plan_with_options(request, runtime)

    def create_rtmp_device_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.device_name):
            query['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        if not UtilClient.is_unset(request.pull_auth_key):
            query['PullAuthKey'] = request.pull_auth_key
        if not UtilClient.is_unset(request.pull_key_expire_time):
            query['PullKeyExpireTime'] = request.pull_key_expire_time
        if not UtilClient.is_unset(request.push_auth_key):
            query['PushAuthKey'] = request.push_auth_key
        if not UtilClient.is_unset(request.push_key_expire_time):
            query['PushKeyExpireTime'] = request.push_key_expire_time
        if not UtilClient.is_unset(request.sub_stream_name):
            query['SubStreamName'] = request.sub_stream_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateRtmpDevice',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.CreateRtmpDeviceResponse(),
            self.call_api(params, req, runtime)
        )

    def create_rtmp_device(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_rtmp_device_with_options(request, runtime)

    def create_stream_push_job_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.device_name):
            query['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.iot_id):
            query['IotId'] = request.iot_id
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.job_type):
            query['JobType'] = request.job_type
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        if not UtilClient.is_unset(request.push_url):
            query['PushUrl'] = request.push_url
        if not UtilClient.is_unset(request.stream_type):
            query['StreamType'] = request.stream_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateStreamPushJob',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.CreateStreamPushJobResponse(),
            self.call_api(params, req, runtime)
        )

    def create_stream_push_job(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_stream_push_job_with_options(request, runtime)

    def create_stream_snapshot_job_with_options(self, request, runtime):
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
        if not UtilClient.is_unset(request.snapshot_interval):
            query['SnapshotInterval'] = request.snapshot_interval
        if not UtilClient.is_unset(request.stream_type):
            query['StreamType'] = request.stream_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateStreamSnapshotJob',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.CreateStreamSnapshotJobResponse(),
            self.call_api(params, req, runtime)
        )

    def create_stream_snapshot_job(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_stream_snapshot_job_with_options(request, runtime)

    def create_time_template_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.all_day):
            query['AllDay'] = request.all_day
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.time_sections):
            query['TimeSections'] = request.time_sections
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateTimeTemplate',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.CreateTimeTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    def create_time_template(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_time_template_with_options(request, runtime)

    def delete_event_record_plan_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.plan_id):
            query['PlanId'] = request.plan_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteEventRecordPlan',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.DeleteEventRecordPlanResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_event_record_plan(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_event_record_plan_with_options(request, runtime)

    def delete_event_record_plan_device_with_options(self, request, runtime):
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
        if not UtilClient.is_unset(request.stream_type):
            query['StreamType'] = request.stream_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteEventRecordPlanDevice',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.DeleteEventRecordPlanDeviceResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_event_record_plan_device(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_event_record_plan_device_with_options(request, runtime)

    def delete_face_device_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.device_group_id):
            query['DeviceGroupId'] = request.device_group_id
        if not UtilClient.is_unset(request.isolation_id):
            query['IsolationId'] = request.isolation_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteFaceDeviceGroup',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.DeleteFaceDeviceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_face_device_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_face_device_group_with_options(request, runtime)

    def delete_face_user_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.isolation_id):
            query['IsolationId'] = request.isolation_id
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteFaceUser',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.DeleteFaceUserResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_face_user(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_face_user_with_options(request, runtime)

    def delete_face_user_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.isolation_id):
            query['IsolationId'] = request.isolation_id
        if not UtilClient.is_unset(request.user_group_id):
            query['UserGroupId'] = request.user_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteFaceUserGroup',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.DeleteFaceUserGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_face_user_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_face_user_group_with_options(request, runtime)

    def delete_face_user_group_and_device_group_relation_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.control_id):
            query['ControlId'] = request.control_id
        if not UtilClient.is_unset(request.isolation_id):
            query['IsolationId'] = request.isolation_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteFaceUserGroupAndDeviceGroupRelation',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.DeleteFaceUserGroupAndDeviceGroupRelationResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_face_user_group_and_device_group_relation(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_face_user_group_and_device_group_relation_with_options(request, runtime)

    def delete_face_user_picture_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.face_pic_md_5):
            query['FacePicMd5'] = request.face_pic_md_5
        if not UtilClient.is_unset(request.isolation_id):
            query['IsolationId'] = request.isolation_id
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteFaceUserPicture',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.DeleteFaceUserPictureResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_face_user_picture(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_face_user_picture_with_options(request, runtime)

    def delete_gb_device_with_options(self, request, runtime):
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
            action='DeleteGbDevice',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.DeleteGbDeviceResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_gb_device(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_gb_device_with_options(request, runtime)

    def delete_local_file_upload_job_with_options(self, request, runtime):
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
            action='DeleteLocalFileUploadJob',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.DeleteLocalFileUploadJobResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_local_file_upload_job(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_local_file_upload_job_with_options(request, runtime)

    def delete_picture_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.device_name):
            query['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.iot_id):
            query['IotId'] = request.iot_id
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.picture_id_list):
            query['PictureIdList'] = request.picture_id_list
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeletePicture',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.DeletePictureResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_picture(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_picture_with_options(request, runtime)

    def delete_record_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.device_name):
            query['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.file_name_list):
            query['FileNameList'] = request.file_name_list
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
            action='DeleteRecord',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.DeleteRecordResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_record(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_record_with_options(request, runtime)

    def delete_record_plan_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.plan_id):
            query['PlanId'] = request.plan_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteRecordPlan',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.DeleteRecordPlanResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_record_plan(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_record_plan_with_options(request, runtime)

    def delete_record_plan_device_with_options(self, request, runtime):
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
        if not UtilClient.is_unset(request.stream_type):
            query['StreamType'] = request.stream_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteRecordPlanDevice',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.DeleteRecordPlanDeviceResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_record_plan_device(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_record_plan_device_with_options(request, runtime)

    def delete_rtmp_device_with_options(self, request, runtime):
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
            action='DeleteRtmpDevice',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.DeleteRtmpDeviceResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_rtmp_device(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_rtmp_device_with_options(request, runtime)

    def delete_rtmp_key_with_options(self, request, runtime):
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
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteRtmpKey',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.DeleteRtmpKeyResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_rtmp_key(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_rtmp_key_with_options(request, runtime)

    def delete_stream_push_job_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.device_name):
            query['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.iot_id):
            query['IotId'] = request.iot_id
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
            action='DeleteStreamPushJob',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.DeleteStreamPushJobResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_stream_push_job(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_stream_push_job_with_options(request, runtime)

    def delete_stream_snapshot_job_with_options(self, request, runtime):
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
        if not UtilClient.is_unset(request.stream_type):
            query['StreamType'] = request.stream_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteStreamSnapshotJob',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.DeleteStreamSnapshotJobResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_stream_snapshot_job(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_stream_snapshot_job_with_options(request, runtime)

    def delete_time_template_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteTimeTemplate',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.DeleteTimeTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_time_template(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_time_template_with_options(request, runtime)

    def detect_user_face_by_url_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.face_pic_url):
            query['FacePicUrl'] = request.face_pic_url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DetectUserFaceByUrl',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.DetectUserFaceByUrlResponse(),
            self.call_api(params, req, runtime)
        )

    def detect_user_face_by_url(self, request):
        runtime = util_models.RuntimeOptions()
        return self.detect_user_face_by_url_with_options(request, runtime)

    def enable_gb_sub_device_with_options(self, request, runtime):
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
        if not UtilClient.is_unset(request.sub_device_id):
            query['SubDeviceId'] = request.sub_device_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnableGbSubDevice',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.EnableGbSubDeviceResponse(),
            self.call_api(params, req, runtime)
        )

    def enable_gb_sub_device(self, request):
        runtime = util_models.RuntimeOptions()
        return self.enable_gb_sub_device_with_options(request, runtime)

    def get_picture_search_job_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_instance_id):
            query['AppInstanceId'] = request.app_instance_id
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetPictureSearchJobStatus',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.GetPictureSearchJobStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def get_picture_search_job_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_picture_search_job_status_with_options(request, runtime)

    def picture_search_picture_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_instance_id):
            query['AppInstanceId'] = request.app_instance_id
        if not UtilClient.is_unset(request.contain_pic_url):
            query['ContainPicUrl'] = request.contain_pic_url
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.picture_search_type):
            query['PictureSearchType'] = request.picture_search_type
        if not UtilClient.is_unset(request.search_pic_url):
            query['SearchPicUrl'] = request.search_pic_url
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.threshold):
            query['Threshold'] = request.threshold
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PictureSearchPicture',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.PictureSearchPictureResponse(),
            self.call_api(params, req, runtime)
        )

    def picture_search_picture(self, request):
        runtime = util_models.RuntimeOptions()
        return self.picture_search_picture_with_options(request, runtime)

    def query_car_process_events_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.action_type):
            query['ActionType'] = request.action_type
        if not UtilClient.is_unset(request.area_index):
            query['AreaIndex'] = request.area_index
        if not UtilClient.is_unset(request.begin_time):
            query['BeginTime'] = request.begin_time
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.plate_no):
            query['PlateNo'] = request.plate_no
        if not UtilClient.is_unset(request.sub_device_name):
            query['SubDeviceName'] = request.sub_device_name
        if not UtilClient.is_unset(request.sub_iot_id):
            query['SubIotId'] = request.sub_iot_id
        if not UtilClient.is_unset(request.sub_product_key):
            query['SubProductKey'] = request.sub_product_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryCarProcessEvents',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.QueryCarProcessEventsResponse(),
            self.call_api(params, req, runtime)
        )

    def query_car_process_events(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_car_process_events_with_options(request, runtime)

    def query_device_event_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.begin_time):
            query['BeginTime'] = request.begin_time
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.device_name):
            query['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.event_type):
            query['EventType'] = request.event_type
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
            action='QueryDeviceEvent',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.QueryDeviceEventResponse(),
            self.call_api(params, req, runtime)
        )

    def query_device_event(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_device_event_with_options(request, runtime)

    def query_device_event_picture_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.device_name):
            query['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.event_id):
            query['EventId'] = request.event_id
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
            action='QueryDeviceEventPicture',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.QueryDeviceEventPictureResponse(),
            self.call_api(params, req, runtime)
        )

    def query_device_event_picture(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_device_event_picture_with_options(request, runtime)

    def query_device_event_record_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.device_name):
            query['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.event_id):
            query['EventId'] = request.event_id
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
            action='QueryDeviceEventRecord',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.QueryDeviceEventRecordResponse(),
            self.call_api(params, req, runtime)
        )

    def query_device_event_record(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_device_event_record_with_options(request, runtime)

    def query_device_picture_by_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.device_name):
            query['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.expire_time):
            query['ExpireTime'] = request.expire_time
        if not UtilClient.is_unset(request.iot_id):
            query['IotId'] = request.iot_id
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.picture_id_list):
            query['PictureIdList'] = request.picture_id_list
        if not UtilClient.is_unset(request.picture_type):
            query['PictureType'] = request.picture_type
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        if not UtilClient.is_unset(request.thumb_width):
            query['ThumbWidth'] = request.thumb_width
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryDevicePictureByList',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.QueryDevicePictureByListResponse(),
            self.call_api(params, req, runtime)
        )

    def query_device_picture_by_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_device_picture_by_list_with_options(request, runtime)

    def query_device_picture_file_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.capture_id):
            query['CaptureId'] = request.capture_id
        if not UtilClient.is_unset(request.device_name):
            query['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.expire_time):
            query['ExpireTime'] = request.expire_time
        if not UtilClient.is_unset(request.iot_id):
            query['IotId'] = request.iot_id
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.picture_type):
            query['PictureType'] = request.picture_type
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        if not UtilClient.is_unset(request.thumb_width):
            query['ThumbWidth'] = request.thumb_width
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryDevicePictureFile',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.QueryDevicePictureFileResponse(),
            self.call_api(params, req, runtime)
        )

    def query_device_picture_file(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_device_picture_file_with_options(request, runtime)

    def query_device_picture_life_cycle_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.iot_id):
            query['IotId'] = request.iot_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryDevicePictureLifeCycle',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.QueryDevicePictureLifeCycleResponse(),
            self.call_api(params, req, runtime)
        )

    def query_device_picture_life_cycle(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_device_picture_life_cycle_with_options(request, runtime)

    def query_device_record_life_cycle_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.device_list):
            query['DeviceList'] = request.device_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryDeviceRecordLifeCycle',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.QueryDeviceRecordLifeCycleResponse(),
            self.call_api(params, req, runtime)
        )

    def query_device_record_life_cycle(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_device_record_life_cycle_with_options(request, runtime)

    def query_device_vod_url_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.device_name):
            query['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.enable_stun):
            query['EnableStun'] = request.enable_stun
        if not UtilClient.is_unset(request.encrypt_type):
            query['EncryptType'] = request.encrypt_type
        if not UtilClient.is_unset(request.file_name):
            query['FileName'] = request.file_name
        if not UtilClient.is_unset(request.iot_id):
            query['IotId'] = request.iot_id
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.play_un_limited):
            query['PlayUnLimited'] = request.play_un_limited
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        if not UtilClient.is_unset(request.scheme):
            query['Scheme'] = request.scheme
        if not UtilClient.is_unset(request.seek_time):
            query['SeekTime'] = request.seek_time
        if not UtilClient.is_unset(request.should_encrypt):
            query['ShouldEncrypt'] = request.should_encrypt
        if not UtilClient.is_unset(request.url_valid_duration):
            query['UrlValidDuration'] = request.url_valid_duration
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryDeviceVodUrl',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.QueryDeviceVodUrlResponse(),
            self.call_api(params, req, runtime)
        )

    def query_device_vod_url(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_device_vod_url_with_options(request, runtime)

    def query_device_vod_url_by_time_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.begin_time):
            query['BeginTime'] = request.begin_time
        if not UtilClient.is_unset(request.device_name):
            query['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.enable_stun):
            query['EnableStun'] = request.enable_stun
        if not UtilClient.is_unset(request.encrypt_type):
            query['EncryptType'] = request.encrypt_type
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.iot_id):
            query['IotId'] = request.iot_id
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.play_un_limited):
            query['PlayUnLimited'] = request.play_un_limited
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        if not UtilClient.is_unset(request.scheme):
            query['Scheme'] = request.scheme
        if not UtilClient.is_unset(request.seek_time):
            query['SeekTime'] = request.seek_time
        if not UtilClient.is_unset(request.should_encrypt):
            query['ShouldEncrypt'] = request.should_encrypt
        if not UtilClient.is_unset(request.url_valid_duration):
            query['UrlValidDuration'] = request.url_valid_duration
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryDeviceVodUrlByTime',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.QueryDeviceVodUrlByTimeResponse(),
            self.call_api(params, req, runtime)
        )

    def query_device_vod_url_by_time(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_device_vod_url_by_time_with_options(request, runtime)

    def query_event_record_plan_detail_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.plan_id):
            query['PlanId'] = request.plan_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryEventRecordPlanDetail',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.QueryEventRecordPlanDetailResponse(),
            self.call_api(params, req, runtime)
        )

    def query_event_record_plan_detail(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_event_record_plan_detail_with_options(request, runtime)

    def query_event_record_plan_device_by_device_with_options(self, request, runtime):
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
        if not UtilClient.is_unset(request.stream_type):
            query['StreamType'] = request.stream_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryEventRecordPlanDeviceByDevice',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.QueryEventRecordPlanDeviceByDeviceResponse(),
            self.call_api(params, req, runtime)
        )

    def query_event_record_plan_device_by_device(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_event_record_plan_device_by_device_with_options(request, runtime)

    def query_event_record_plan_device_by_plan_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.plan_id):
            query['PlanId'] = request.plan_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryEventRecordPlanDeviceByPlan',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.QueryEventRecordPlanDeviceByPlanResponse(),
            self.call_api(params, req, runtime)
        )

    def query_event_record_plan_device_by_plan(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_event_record_plan_device_by_plan_with_options(request, runtime)

    def query_event_record_plans_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryEventRecordPlans',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.QueryEventRecordPlansResponse(),
            self.call_api(params, req, runtime)
        )

    def query_event_record_plans(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_event_record_plans_with_options(request, runtime)

    def query_face_all_device_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.isolation_id):
            query['IsolationId'] = request.isolation_id
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryFaceAllDeviceGroup',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.QueryFaceAllDeviceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def query_face_all_device_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_face_all_device_group_with_options(request, runtime)

    def query_face_all_user_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.isolation_id):
            query['IsolationId'] = request.isolation_id
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryFaceAllUserGroup',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.QueryFaceAllUserGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def query_face_all_user_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_face_all_user_group_with_options(request, runtime)

    def query_face_all_user_group_and_device_group_relation_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.isolation_id):
            query['IsolationId'] = request.isolation_id
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryFaceAllUserGroupAndDeviceGroupRelation',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.QueryFaceAllUserGroupAndDeviceGroupRelationResponse(),
            self.call_api(params, req, runtime)
        )

    def query_face_all_user_group_and_device_group_relation(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_face_all_user_group_and_device_group_relation_with_options(request, runtime)

    def query_face_all_user_ids_by_group_id_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.isolation_id):
            query['IsolationId'] = request.isolation_id
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.user_group_id):
            query['UserGroupId'] = request.user_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryFaceAllUserIdsByGroupId',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.QueryFaceAllUserIdsByGroupIdResponse(),
            self.call_api(params, req, runtime)
        )

    def query_face_all_user_ids_by_group_id(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_face_all_user_ids_by_group_id_with_options(request, runtime)

    def query_face_custom_user_id_by_user_id_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.isolation_id):
            query['IsolationId'] = request.isolation_id
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryFaceCustomUserIdByUserId',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.QueryFaceCustomUserIdByUserIdResponse(),
            self.call_api(params, req, runtime)
        )

    def query_face_custom_user_id_by_user_id(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_face_custom_user_id_by_user_id_with_options(request, runtime)

    def query_face_device_groups_by_device_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.device_name):
            query['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.isolation_id):
            query['IsolationId'] = request.isolation_id
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
            action='QueryFaceDeviceGroupsByDevice',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.QueryFaceDeviceGroupsByDeviceResponse(),
            self.call_api(params, req, runtime)
        )

    def query_face_device_groups_by_device(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_face_device_groups_by_device_with_options(request, runtime)

    def query_face_user_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.isolation_id):
            query['IsolationId'] = request.isolation_id
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryFaceUser',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.QueryFaceUserResponse(),
            self.call_api(params, req, runtime)
        )

    def query_face_user(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_face_user_with_options(request, runtime)

    def query_face_user_batch_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.isolation_id):
            query['IsolationId'] = request.isolation_id
        if not UtilClient.is_unset(request.user_id_list):
            query['UserIdList'] = request.user_id_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryFaceUserBatch',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.QueryFaceUserBatchResponse(),
            self.call_api(params, req, runtime)
        )

    def query_face_user_batch(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_face_user_batch_with_options(request, runtime)

    def query_face_user_by_name_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.isolation_id):
            query['IsolationId'] = request.isolation_id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.params):
            query['Params'] = request.params
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryFaceUserByName',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.QueryFaceUserByNameResponse(),
            self.call_api(params, req, runtime)
        )

    def query_face_user_by_name(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_face_user_by_name_with_options(request, runtime)

    def query_face_user_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.isolation_id):
            query['IsolationId'] = request.isolation_id
        if not UtilClient.is_unset(request.page_no):
            query['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryFaceUserGroup',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.QueryFaceUserGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def query_face_user_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_face_user_group_with_options(request, runtime)

    def query_face_user_group_and_device_group_relation_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.control_id):
            query['ControlId'] = request.control_id
        if not UtilClient.is_unset(request.isolation_id):
            query['IsolationId'] = request.isolation_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryFaceUserGroupAndDeviceGroupRelation',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.QueryFaceUserGroupAndDeviceGroupRelationResponse(),
            self.call_api(params, req, runtime)
        )

    def query_face_user_group_and_device_group_relation(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_face_user_group_and_device_group_relation_with_options(request, runtime)

    def query_face_user_id_by_custom_user_id_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.custom_user_id):
            query['CustomUserId'] = request.custom_user_id
        if not UtilClient.is_unset(request.isolation_id):
            query['IsolationId'] = request.isolation_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryFaceUserIdByCustomUserId',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.QueryFaceUserIdByCustomUserIdResponse(),
            self.call_api(params, req, runtime)
        )

    def query_face_user_id_by_custom_user_id(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_face_user_id_by_custom_user_id_with_options(request, runtime)

    def query_gb_sub_device_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.device_name):
            query['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.iot_id):
            query['IotId'] = request.iot_id
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.page_start):
            query['PageStart'] = request.page_start
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryGbSubDeviceList',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.QueryGbSubDeviceListResponse(),
            self.call_api(params, req, runtime)
        )

    def query_gb_sub_device_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_gb_sub_device_list_with_options(request, runtime)

    def query_live_streaming_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cache_duration):
            query['CacheDuration'] = request.cache_duration
        if not UtilClient.is_unset(request.device_name):
            query['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.enable_stun):
            query['EnableStun'] = request.enable_stun
        if not UtilClient.is_unset(request.encrypt_type):
            query['EncryptType'] = request.encrypt_type
        if not UtilClient.is_unset(request.force_iframe):
            query['ForceIFrame'] = request.force_iframe
        if not UtilClient.is_unset(request.iot_id):
            query['IotId'] = request.iot_id
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.play_un_limited):
            query['PlayUnLimited'] = request.play_un_limited
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        if not UtilClient.is_unset(request.scheme):
            query['Scheme'] = request.scheme
        if not UtilClient.is_unset(request.should_encrypt):
            query['ShouldEncrypt'] = request.should_encrypt
        if not UtilClient.is_unset(request.stream_type):
            query['StreamType'] = request.stream_type
        if not UtilClient.is_unset(request.url_valid_duration):
            query['UrlValidDuration'] = request.url_valid_duration
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryLiveStreaming',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.QueryLiveStreamingResponse(),
            self.call_api(params, req, runtime)
        )

    def query_live_streaming(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_live_streaming_with_options(request, runtime)

    def query_local_file_upload_job_with_options(self, request, runtime):
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
            action='QueryLocalFileUploadJob',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.QueryLocalFileUploadJobResponse(),
            self.call_api(params, req, runtime)
        )

    def query_local_file_upload_job(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_local_file_upload_job_with_options(request, runtime)

    def query_month_record_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.device_name):
            query['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.iot_id):
            query['IotId'] = request.iot_id
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.month):
            query['Month'] = request.month
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryMonthRecord',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.QueryMonthRecordResponse(),
            self.call_api(params, req, runtime)
        )

    def query_month_record(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_month_record_with_options(request, runtime)

    def query_picture_files_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.begin_time):
            query['BeginTime'] = request.begin_time
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.device_name):
            query['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.iot_id):
            query['IotId'] = request.iot_id
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.picture_source):
            query['PictureSource'] = request.picture_source
        if not UtilClient.is_unset(request.picture_type):
            query['PictureType'] = request.picture_type
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryPictureFiles',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.QueryPictureFilesResponse(),
            self.call_api(params, req, runtime)
        )

    def query_picture_files(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_picture_files_with_options(request, runtime)

    def query_picture_search_aiboxes_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_instance_id):
            query['AppInstanceId'] = request.app_instance_id
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
            action='QueryPictureSearchAiboxes',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.QueryPictureSearchAiboxesResponse(),
            self.call_api(params, req, runtime)
        )

    def query_picture_search_aiboxes(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_picture_search_aiboxes_with_options(request, runtime)

    def query_picture_search_apps_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
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
            action='QueryPictureSearchApps',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.QueryPictureSearchAppsResponse(),
            self.call_api(params, req, runtime)
        )

    def query_picture_search_apps(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_picture_search_apps_with_options(request, runtime)

    def query_picture_search_devices_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_instance_id):
            query['AppInstanceId'] = request.app_instance_id
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryPictureSearchDevices',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.QueryPictureSearchDevicesResponse(),
            self.call_api(params, req, runtime)
        )

    def query_picture_search_devices(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_picture_search_devices_with_options(request, runtime)

    def query_picture_search_job_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_instance_id):
            query['AppInstanceId'] = request.app_instance_id
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.job_status):
            query['JobStatus'] = request.job_status
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryPictureSearchJob',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.QueryPictureSearchJobResponse(),
            self.call_api(params, req, runtime)
        )

    def query_picture_search_job(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_picture_search_job_with_options(request, runtime)

    def query_picture_search_job_result_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_instance_id):
            query['AppInstanceId'] = request.app_instance_id
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.job_id):
            query['JobId'] = request.job_id
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryPictureSearchJobResult',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.QueryPictureSearchJobResultResponse(),
            self.call_api(params, req, runtime)
        )

    def query_picture_search_job_result(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_picture_search_job_result_with_options(request, runtime)

    def query_record_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.begin_time):
            query['BeginTime'] = request.begin_time
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.device_name):
            query['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.iot_id):
            query['IotId'] = request.iot_id
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.need_snapshot):
            query['NeedSnapshot'] = request.need_snapshot
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        if not UtilClient.is_unset(request.record_type):
            query['RecordType'] = request.record_type
        if not UtilClient.is_unset(request.stream_type):
            query['StreamType'] = request.stream_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryRecord',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.QueryRecordResponse(),
            self.call_api(params, req, runtime)
        )

    def query_record(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_record_with_options(request, runtime)

    def query_record_by_record_id_with_options(self, request, runtime):
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
        if not UtilClient.is_unset(request.record_id):
            query['RecordId'] = request.record_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryRecordByRecordId',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.QueryRecordByRecordIdResponse(),
            self.call_api(params, req, runtime)
        )

    def query_record_by_record_id(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_record_by_record_id_with_options(request, runtime)

    def query_record_download_job_by_id_with_options(self, request, runtime):
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
            action='QueryRecordDownloadJobById',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.QueryRecordDownloadJobByIdResponse(),
            self.call_api(params, req, runtime)
        )

    def query_record_download_job_by_id(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_record_download_job_by_id_with_options(request, runtime)

    def query_record_download_job_list_with_options(self, request, runtime):
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
            action='QueryRecordDownloadJobList',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.QueryRecordDownloadJobListResponse(),
            self.call_api(params, req, runtime)
        )

    def query_record_download_job_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_record_download_job_list_with_options(request, runtime)

    def query_record_download_url_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.device_name):
            query['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.file_name):
            query['FileName'] = request.file_name
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
            action='QueryRecordDownloadUrl',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.QueryRecordDownloadUrlResponse(),
            self.call_api(params, req, runtime)
        )

    def query_record_download_url(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_record_download_url_with_options(request, runtime)

    def query_record_plan_detail_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.plan_id):
            query['PlanId'] = request.plan_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryRecordPlanDetail',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.QueryRecordPlanDetailResponse(),
            self.call_api(params, req, runtime)
        )

    def query_record_plan_detail(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_record_plan_detail_with_options(request, runtime)

    def query_record_plan_device_by_device_with_options(self, request, runtime):
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
        if not UtilClient.is_unset(request.stream_type):
            query['StreamType'] = request.stream_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryRecordPlanDeviceByDevice',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.QueryRecordPlanDeviceByDeviceResponse(),
            self.call_api(params, req, runtime)
        )

    def query_record_plan_device_by_device(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_record_plan_device_by_device_with_options(request, runtime)

    def query_record_plan_device_by_plan_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.plan_id):
            query['PlanId'] = request.plan_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryRecordPlanDeviceByPlan',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.QueryRecordPlanDeviceByPlanResponse(),
            self.call_api(params, req, runtime)
        )

    def query_record_plan_device_by_plan(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_record_plan_device_by_plan_with_options(request, runtime)

    def query_record_plans_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryRecordPlans',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.QueryRecordPlansResponse(),
            self.call_api(params, req, runtime)
        )

    def query_record_plans(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_record_plans_with_options(request, runtime)

    def query_record_url_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.device_name):
            query['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.file_name):
            query['FileName'] = request.file_name
        if not UtilClient.is_unset(request.iot_id):
            query['IotId'] = request.iot_id
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        if not UtilClient.is_unset(request.seek_time):
            query['SeekTime'] = request.seek_time
        if not UtilClient.is_unset(request.url_valid_duration):
            query['UrlValidDuration'] = request.url_valid_duration
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryRecordUrl',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.QueryRecordUrlResponse(),
            self.call_api(params, req, runtime)
        )

    def query_record_url(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_record_url_with_options(request, runtime)

    def query_record_url_by_time_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.begin_time):
            query['BeginTime'] = request.begin_time
        if not UtilClient.is_unset(request.device_name):
            query['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.iot_id):
            query['IotId'] = request.iot_id
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        if not UtilClient.is_unset(request.stream_type):
            query['StreamType'] = request.stream_type
        if not UtilClient.is_unset(request.url_valid_duration):
            query['UrlValidDuration'] = request.url_valid_duration
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryRecordUrlByTime',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.QueryRecordUrlByTimeResponse(),
            self.call_api(params, req, runtime)
        )

    def query_record_url_by_time(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_record_url_by_time_with_options(request, runtime)

    def query_rtmp_key_with_options(self, request, runtime):
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
            action='QueryRtmpKey',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.QueryRtmpKeyResponse(),
            self.call_api(params, req, runtime)
        )

    def query_rtmp_key(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_rtmp_key_with_options(request, runtime)

    def query_stream_push_job_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.device_name):
            query['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.iot_id):
            query['IotId'] = request.iot_id
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
            action='QueryStreamPushJob',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.QueryStreamPushJobResponse(),
            self.call_api(params, req, runtime)
        )

    def query_stream_push_job(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_stream_push_job_with_options(request, runtime)

    def query_stream_push_job_list_with_options(self, request, runtime):
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
        if not UtilClient.is_unset(request.job_type):
            query['JobType'] = request.job_type
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryStreamPushJobList',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.QueryStreamPushJobListResponse(),
            self.call_api(params, req, runtime)
        )

    def query_stream_push_job_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_stream_push_job_list_with_options(request, runtime)

    def query_stream_snapshot_job_with_options(self, request, runtime):
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
            action='QueryStreamSnapshotJob',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.QueryStreamSnapshotJobResponse(),
            self.call_api(params, req, runtime)
        )

    def query_stream_snapshot_job(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_stream_snapshot_job_with_options(request, runtime)

    def query_time_template_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryTimeTemplate',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.QueryTimeTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    def query_time_template(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_time_template_with_options(request, runtime)

    def query_time_template_detail_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryTimeTemplateDetail',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.QueryTimeTemplateDetailResponse(),
            self.call_api(params, req, runtime)
        )

    def query_time_template_detail(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_time_template_detail_with_options(request, runtime)

    def query_vision_device_info_with_options(self, request, runtime):
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
            action='QueryVisionDeviceInfo',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.QueryVisionDeviceInfoResponse(),
            self.call_api(params, req, runtime)
        )

    def query_vision_device_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_vision_device_info_with_options(request, runtime)

    def query_voice_intercom_with_options(self, request, runtime):
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
        if not UtilClient.is_unset(request.scheme):
            query['Scheme'] = request.scheme
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryVoiceIntercom',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.QueryVoiceIntercomResponse(),
            self.call_api(params, req, runtime)
        )

    def query_voice_intercom(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_voice_intercom_with_options(request, runtime)

    def refresh_gb_sub_device_list_with_options(self, request, runtime):
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
            action='RefreshGbSubDeviceList',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.RefreshGbSubDeviceListResponse(),
            self.call_api(params, req, runtime)
        )

    def refresh_gb_sub_device_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.refresh_gb_sub_device_list_with_options(request, runtime)

    def remove_face_device_from_device_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.device_group_id):
            query['DeviceGroupId'] = request.device_group_id
        if not UtilClient.is_unset(request.device_name):
            query['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.isolation_id):
            query['IsolationId'] = request.isolation_id
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemoveFaceDeviceFromDeviceGroup',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.RemoveFaceDeviceFromDeviceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def remove_face_device_from_device_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.remove_face_device_from_device_group_with_options(request, runtime)

    def remove_face_user_from_user_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.isolation_id):
            query['IsolationId'] = request.isolation_id
        if not UtilClient.is_unset(request.user_group_id):
            query['UserGroupId'] = request.user_group_id
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemoveFaceUserFromUserGroup',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.RemoveFaceUserFromUserGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def remove_face_user_from_user_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.remove_face_user_from_user_group_with_options(request, runtime)

    def set_device_picture_life_cycle_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.day):
            query['Day'] = request.day
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
            action='SetDevicePictureLifeCycle',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.SetDevicePictureLifeCycleResponse(),
            self.call_api(params, req, runtime)
        )

    def set_device_picture_life_cycle(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_device_picture_life_cycle_with_options(request, runtime)

    def set_device_record_life_cycle_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.day):
            query['Day'] = request.day
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
            action='SetDeviceRecordLifeCycle',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.SetDeviceRecordLifeCycleResponse(),
            self.call_api(params, req, runtime)
        )

    def set_device_record_life_cycle(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_device_record_life_cycle_with_options(request, runtime)

    def stop_live_streaming_with_options(self, request, runtime):
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
        if not UtilClient.is_unset(request.stream_type):
            query['StreamType'] = request.stream_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopLiveStreaming',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.StopLiveStreamingResponse(),
            self.call_api(params, req, runtime)
        )

    def stop_live_streaming(self, request):
        runtime = util_models.RuntimeOptions()
        return self.stop_live_streaming_with_options(request, runtime)

    def stop_triggered_record_with_options(self, request, runtime):
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
        if not UtilClient.is_unset(request.record_id):
            query['RecordId'] = request.record_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopTriggeredRecord',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.StopTriggeredRecordResponse(),
            self.call_api(params, req, runtime)
        )

    def stop_triggered_record(self, request):
        runtime = util_models.RuntimeOptions()
        return self.stop_triggered_record_with_options(request, runtime)

    def transfer_device_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.device_name_list):
            query['DeviceNameList'] = request.device_name_list
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        if not UtilClient.is_unset(request.source_instance_id):
            query['SourceInstanceId'] = request.source_instance_id
        if not UtilClient.is_unset(request.target_instance_id):
            query['TargetInstanceId'] = request.target_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TransferDeviceInstance',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.TransferDeviceInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    def transfer_device_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.transfer_device_instance_with_options(request, runtime)

    def trigger_capture_picture_with_options(self, request, runtime):
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
            action='TriggerCapturePicture',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.TriggerCapturePictureResponse(),
            self.call_api(params, req, runtime)
        )

    def trigger_capture_picture(self, request):
        runtime = util_models.RuntimeOptions()
        return self.trigger_capture_picture_with_options(request, runtime)

    def trigger_record_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.device_name):
            query['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.iot_id):
            query['IotId'] = request.iot_id
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.pre_record_duration):
            query['PreRecordDuration'] = request.pre_record_duration
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        if not UtilClient.is_unset(request.record_duration):
            query['RecordDuration'] = request.record_duration
        if not UtilClient.is_unset(request.stream_type):
            query['StreamType'] = request.stream_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TriggerRecord',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.TriggerRecordResponse(),
            self.call_api(params, req, runtime)
        )

    def trigger_record(self, request):
        runtime = util_models.RuntimeOptions()
        return self.trigger_record_with_options(request, runtime)

    def unbind_picture_search_app_with_devices_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_instance_id):
            query['AppInstanceId'] = request.app_instance_id
        if not UtilClient.is_unset(request.device_iot_ids):
            query['DeviceIotIds'] = request.device_iot_ids
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UnbindPictureSearchAppWithDevices',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.UnbindPictureSearchAppWithDevicesResponse(),
            self.call_api(params, req, runtime)
        )

    def unbind_picture_search_app_with_devices(self, request):
        runtime = util_models.RuntimeOptions()
        return self.unbind_picture_search_app_with_devices_with_options(request, runtime)

    def update_event_record_plan_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.event_types):
            query['EventTypes'] = request.event_types
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.plan_id):
            query['PlanId'] = request.plan_id
        if not UtilClient.is_unset(request.pre_record_duration):
            query['PreRecordDuration'] = request.pre_record_duration
        if not UtilClient.is_unset(request.record_duration):
            query['RecordDuration'] = request.record_duration
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateEventRecordPlan',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.UpdateEventRecordPlanResponse(),
            self.call_api(params, req, runtime)
        )

    def update_event_record_plan(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_event_record_plan_with_options(request, runtime)

    def update_face_user_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.custom_user_id):
            query['CustomUserId'] = request.custom_user_id
        if not UtilClient.is_unset(request.face_pic_url):
            query['FacePicUrl'] = request.face_pic_url
        if not UtilClient.is_unset(request.isolation_id):
            query['IsolationId'] = request.isolation_id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.params):
            query['Params'] = request.params
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateFaceUser',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.UpdateFaceUserResponse(),
            self.call_api(params, req, runtime)
        )

    def update_face_user(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_face_user_with_options(request, runtime)

    def update_face_user_group_and_device_group_relation_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.control_id):
            query['ControlId'] = request.control_id
        if not UtilClient.is_unset(request.isolation_id):
            query['IsolationId'] = request.isolation_id
        if not UtilClient.is_unset(request.relation):
            query['Relation'] = request.relation
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateFaceUserGroupAndDeviceGroupRelation',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.UpdateFaceUserGroupAndDeviceGroupRelationResponse(),
            self.call_api(params, req, runtime)
        )

    def update_face_user_group_and_device_group_relation(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_face_user_group_and_device_group_relation_with_options(request, runtime)

    def update_gb_device_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.device_name):
            query['DeviceName'] = request.device_name
        if not UtilClient.is_unset(request.gb_id):
            query['GbId'] = request.gb_id
        if not UtilClient.is_unset(request.iot_id):
            query['IotId'] = request.iot_id
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.password):
            query['Password'] = request.password
        if not UtilClient.is_unset(request.product_key):
            query['ProductKey'] = request.product_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateGbDevice',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.UpdateGbDeviceResponse(),
            self.call_api(params, req, runtime)
        )

    def update_gb_device(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_gb_device_with_options(request, runtime)

    def update_instance_internet_protocol_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.iot_instance_id):
            query['IotInstanceId'] = request.iot_instance_id
        if not UtilClient.is_unset(request.ip_version):
            query['IpVersion'] = request.ip_version
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateInstanceInternetProtocol',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.UpdateInstanceInternetProtocolResponse(),
            self.call_api(params, req, runtime)
        )

    def update_instance_internet_protocol(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_instance_internet_protocol_with_options(request, runtime)

    def update_picture_search_app_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_instance_id):
            query['AppInstanceId'] = request.app_instance_id
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdatePictureSearchApp',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.UpdatePictureSearchAppResponse(),
            self.call_api(params, req, runtime)
        )

    def update_picture_search_app(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_picture_search_app_with_options(request, runtime)

    def update_record_plan_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.plan_id):
            query['PlanId'] = request.plan_id
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateRecordPlan',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.UpdateRecordPlanResponse(),
            self.call_api(params, req, runtime)
        )

    def update_record_plan(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_record_plan_with_options(request, runtime)

    def update_rtmp_key_with_options(self, request, runtime):
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
        if not UtilClient.is_unset(request.pull_auth_key):
            query['PullAuthKey'] = request.pull_auth_key
        if not UtilClient.is_unset(request.pull_key_expire_time):
            query['PullKeyExpireTime'] = request.pull_key_expire_time
        if not UtilClient.is_unset(request.push_auth_key):
            query['PushAuthKey'] = request.push_auth_key
        if not UtilClient.is_unset(request.push_key_expire_time):
            query['PushKeyExpireTime'] = request.push_key_expire_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateRtmpKey',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.UpdateRtmpKeyResponse(),
            self.call_api(params, req, runtime)
        )

    def update_rtmp_key(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_rtmp_key_with_options(request, runtime)

    def update_time_template_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.all_day):
            query['AllDay'] = request.all_day
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.template_id):
            query['TemplateId'] = request.template_id
        if not UtilClient.is_unset(request.time_sections):
            query['TimeSections'] = request.time_sections
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateTimeTemplate',
            version='2018-01-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            linkvisual_20180120_models.UpdateTimeTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    def update_time_template(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_time_template_with_options(request, runtime)
