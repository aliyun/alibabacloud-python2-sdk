# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_mpaas20201028 import models as m_paa_s20201028_models
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
            'cn-hangzhou': 'mpaas.aliyuncs.com',
            'ap-northeast-1': 'mpaas.aliyuncs.com',
            'ap-northeast-2-pop': 'mpaas.aliyuncs.com',
            'ap-south-1': 'mpaas.aliyuncs.com',
            'ap-southeast-1': 'mpaas.aliyuncs.com',
            'ap-southeast-2': 'mpaas.aliyuncs.com',
            'ap-southeast-3': 'mpaas.aliyuncs.com',
            'ap-southeast-5': 'mpaas.aliyuncs.com',
            'cn-beijing': 'mpaas.aliyuncs.com',
            'cn-beijing-finance-1': 'mpaas.aliyuncs.com',
            'cn-beijing-finance-pop': 'mpaas.aliyuncs.com',
            'cn-beijing-gov-1': 'mpaas.aliyuncs.com',
            'cn-beijing-nu16-b01': 'mpaas.aliyuncs.com',
            'cn-chengdu': 'mpaas.aliyuncs.com',
            'cn-edge-1': 'mpaas.aliyuncs.com',
            'cn-fujian': 'mpaas.aliyuncs.com',
            'cn-haidian-cm12-c01': 'mpaas.aliyuncs.com',
            'cn-hangzhou-bj-b01': 'mpaas.aliyuncs.com',
            'cn-hangzhou-finance': 'mpaas.aliyuncs.com',
            'cn-hangzhou-internal-prod-1': 'mpaas.aliyuncs.com',
            'cn-hangzhou-internal-test-1': 'mpaas.aliyuncs.com',
            'cn-hangzhou-internal-test-2': 'mpaas.aliyuncs.com',
            'cn-hangzhou-internal-test-3': 'mpaas.aliyuncs.com',
            'cn-hangzhou-test-306': 'mpaas.aliyuncs.com',
            'cn-hongkong': 'mpaas.aliyuncs.com',
            'cn-hongkong-finance-pop': 'mpaas.aliyuncs.com',
            'cn-huhehaote': 'mpaas.aliyuncs.com',
            'cn-north-2-gov-1': 'mpaas.aliyuncs.com',
            'cn-qingdao': 'mpaas.aliyuncs.com',
            'cn-qingdao-nebula': 'mpaas.aliyuncs.com',
            'cn-shanghai': 'mpaas.aliyuncs.com',
            'cn-shanghai-et15-b01': 'mpaas.aliyuncs.com',
            'cn-shanghai-et2-b01': 'mpaas.aliyuncs.com',
            'cn-shanghai-finance-1': 'mpaas.aliyuncs.com',
            'cn-shanghai-inner': 'mpaas.aliyuncs.com',
            'cn-shanghai-internal-test-1': 'mpaas.aliyuncs.com',
            'cn-shenzhen': 'mpaas.aliyuncs.com',
            'cn-shenzhen-finance-1': 'mpaas.aliyuncs.com',
            'cn-shenzhen-inner': 'mpaas.aliyuncs.com',
            'cn-shenzhen-st4-d01': 'mpaas.aliyuncs.com',
            'cn-shenzhen-su18-b01': 'mpaas.aliyuncs.com',
            'cn-wuhan': 'mpaas.aliyuncs.com',
            'cn-yushanfang': 'mpaas.aliyuncs.com',
            'cn-zhangbei-na61-b01': 'mpaas.aliyuncs.com',
            'cn-zhangjiakou': 'mpaas.aliyuncs.com',
            'cn-zhangjiakou-na62-a01': 'mpaas.aliyuncs.com',
            'cn-zhengzhou-nebula-1': 'mpaas.aliyuncs.com',
            'eu-central-1': 'mpaas.aliyuncs.com',
            'eu-west-1': 'mpaas.aliyuncs.com',
            'eu-west-1-oxs': 'mpaas.aliyuncs.com',
            'me-east-1': 'mpaas.aliyuncs.com',
            'rus-west-1-pop': 'mpaas.aliyuncs.com',
            'us-east-1': 'mpaas.aliyuncs.com',
            'us-west-1': 'mpaas.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('mpaas', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def add_mds_mini_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.mpaas_mappcenter_mini_config_add_json_str):
            body['MpaasMappcenterMiniConfigAddJsonStr'] = request.mpaas_mappcenter_mini_config_add_json_str
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddMdsMiniConfig',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.AddMdsMiniConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def add_mds_mini_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_mds_mini_config_with_options(request, runtime)

    def cancel_push_scheduler_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        if not UtilClient.is_unset(request.unique_ids):
            body['UniqueIds'] = request.unique_ids
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CancelPushScheduler',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.CancelPushSchedulerResponse(),
            self.call_api(params, req, runtime)
        )

    def cancel_push_scheduler(self, request):
        runtime = util_models.RuntimeOptions()
        return self.cancel_push_scheduler_with_options(request, runtime)

    def change_mcube_mini_task_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.biz_type):
            body['BizType'] = request.biz_type
        if not UtilClient.is_unset(request.package_id):
            body['PackageId'] = request.package_id
        if not UtilClient.is_unset(request.task_id):
            body['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.task_status):
            body['TaskStatus'] = request.task_status
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ChangeMcubeMiniTaskStatus',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.ChangeMcubeMiniTaskStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def change_mcube_mini_task_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.change_mcube_mini_task_status_with_options(request, runtime)

    def change_mcube_nebula_task_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.biz_type):
            body['BizType'] = request.biz_type
        if not UtilClient.is_unset(request.package_id):
            body['PackageId'] = request.package_id
        if not UtilClient.is_unset(request.task_id):
            body['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.task_status):
            body['TaskStatus'] = request.task_status
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ChangeMcubeNebulaTaskStatus',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.ChangeMcubeNebulaTaskStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def change_mcube_nebula_task_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.change_mcube_nebula_task_status_with_options(request, runtime)

    def change_mcube_public_task_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.task_id):
            body['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.task_status):
            body['TaskStatus'] = request.task_status
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ChangeMcubePublicTaskStatus',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.ChangeMcubePublicTaskStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def change_mcube_public_task_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.change_mcube_public_task_status_with_options(request, runtime)

    def copy_mcdp_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.mpaas_mappcenter_mcdp_group_copy_json_str):
            body['MpaasMappcenterMcdpGroupCopyJsonStr'] = request.mpaas_mappcenter_mcdp_group_copy_json_str
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CopyMcdpGroup',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.CopyMcdpGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def copy_mcdp_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.copy_mcdp_group_with_options(request, runtime)

    def create_mas_crowd_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.mpaas_mappcenter_mcdp_mas_crowd_create_json_str):
            body['MpaasMappcenterMcdpMasCrowdCreateJsonStr'] = request.mpaas_mappcenter_mcdp_mas_crowd_create_json_str
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateMasCrowd',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.CreateMasCrowdResponse(),
            self.call_api(params, req, runtime)
        )

    def create_mas_crowd(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_mas_crowd_with_options(request, runtime)

    def create_mas_funnel_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.mpaas_mappcenter_mcdp_mas_funnel_create_json_str):
            body['MpaasMappcenterMcdpMasFunnelCreateJsonStr'] = request.mpaas_mappcenter_mcdp_mas_funnel_create_json_str
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateMasFunnel',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.CreateMasFunnelResponse(),
            self.call_api(params, req, runtime)
        )

    def create_mas_funnel(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_mas_funnel_with_options(request, runtime)

    def create_mcdp_event_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.mpaas_mappcenter_mcdp_event_create_json_str):
            body['MpaasMappcenterMcdpEventCreateJsonStr'] = request.mpaas_mappcenter_mcdp_event_create_json_str
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateMcdpEvent',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.CreateMcdpEventResponse(),
            self.call_api(params, req, runtime)
        )

    def create_mcdp_event(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_mcdp_event_with_options(request, runtime)

    def create_mcdp_event_attribute_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.mpaas_mappcenter_mcdp_event_attribute_create_json_str):
            body['MpaasMappcenterMcdpEventAttributeCreateJsonStr'] = request.mpaas_mappcenter_mcdp_event_attribute_create_json_str
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateMcdpEventAttribute',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.CreateMcdpEventAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    def create_mcdp_event_attribute(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_mcdp_event_attribute_with_options(request, runtime)

    def create_mcdp_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.mpaas_mappcenter_mcdp_group_create_json_str):
            body['MpaasMappcenterMcdpGroupCreateJsonStr'] = request.mpaas_mappcenter_mcdp_group_create_json_str
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateMcdpGroup',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.CreateMcdpGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def create_mcdp_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_mcdp_group_with_options(request, runtime)

    def create_mcdp_material_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.mpaas_mappcenter_mcdp_material_create_json_str):
            body['MpaasMappcenterMcdpMaterialCreateJsonStr'] = request.mpaas_mappcenter_mcdp_material_create_json_str
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateMcdpMaterial',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.CreateMcdpMaterialResponse(),
            self.call_api(params, req, runtime)
        )

    def create_mcdp_material(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_mcdp_material_with_options(request, runtime)

    def create_mcdp_zone_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.mpaas_mappcenter_mcdp_zone_create_json_str):
            body['MpaasMappcenterMcdpZoneCreateJsonStr'] = request.mpaas_mappcenter_mcdp_zone_create_json_str
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateMcdpZone',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.CreateMcdpZoneResponse(),
            self.call_api(params, req, runtime)
        )

    def create_mcdp_zone(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_mcdp_zone_with_options(request, runtime)

    def create_mcube_mini_app_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.h_5id):
            body['H5Id'] = request.h_5id
        if not UtilClient.is_unset(request.h_5name):
            body['H5Name'] = request.h_5name
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateMcubeMiniApp',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.CreateMcubeMiniAppResponse(),
            self.call_api(params, req, runtime)
        )

    def create_mcube_mini_app(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_mcube_mini_app_with_options(request, runtime)

    def create_mcube_mini_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.grey_config_info):
            body['GreyConfigInfo'] = request.grey_config_info
        if not UtilClient.is_unset(request.grey_endtime_data):
            body['GreyEndtimeData'] = request.grey_endtime_data
        if not UtilClient.is_unset(request.grey_num):
            body['GreyNum'] = request.grey_num
        if not UtilClient.is_unset(request.memo):
            body['Memo'] = request.memo
        if not UtilClient.is_unset(request.package_id):
            body['PackageId'] = request.package_id
        if not UtilClient.is_unset(request.publish_mode):
            body['PublishMode'] = request.publish_mode
        if not UtilClient.is_unset(request.publish_type):
            body['PublishType'] = request.publish_type
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.whitelist_ids):
            body['WhitelistIds'] = request.whitelist_ids
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateMcubeMiniTask',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.CreateMcubeMiniTaskResponse(),
            self.call_api(params, req, runtime)
        )

    def create_mcube_mini_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_mcube_mini_task_with_options(request, runtime)

    def create_mcube_nebula_app_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.h_5id):
            body['H5Id'] = request.h_5id
        if not UtilClient.is_unset(request.h_5name):
            body['H5Name'] = request.h_5name
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateMcubeNebulaApp',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.CreateMcubeNebulaAppResponse(),
            self.call_api(params, req, runtime)
        )

    def create_mcube_nebula_app(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_mcube_nebula_app_with_options(request, runtime)

    def create_mcube_nebula_resource_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.auto_install):
            body['AutoInstall'] = request.auto_install
        if not UtilClient.is_unset(request.client_version_max):
            body['ClientVersionMax'] = request.client_version_max
        if not UtilClient.is_unset(request.client_version_min):
            body['ClientVersionMin'] = request.client_version_min
        if not UtilClient.is_unset(request.custom_domain_name):
            body['CustomDomainName'] = request.custom_domain_name
        if not UtilClient.is_unset(request.extend_info):
            body['ExtendInfo'] = request.extend_info
        if not UtilClient.is_unset(request.file_url):
            body['FileUrl'] = request.file_url
        if not UtilClient.is_unset(request.h_5id):
            body['H5Id'] = request.h_5id
        if not UtilClient.is_unset(request.h_5name):
            body['H5Name'] = request.h_5name
        if not UtilClient.is_unset(request.h_5version):
            body['H5Version'] = request.h_5version
        if not UtilClient.is_unset(request.install_type):
            body['InstallType'] = request.install_type
        if not UtilClient.is_unset(request.main_url):
            body['MainUrl'] = request.main_url
        if not UtilClient.is_unset(request.onex_flag):
            body['OnexFlag'] = request.onex_flag
        if not UtilClient.is_unset(request.platform):
            body['Platform'] = request.platform
        if not UtilClient.is_unset(request.repeat_nebula):
            body['RepeatNebula'] = request.repeat_nebula
        if not UtilClient.is_unset(request.resource_type):
            body['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.sub_url):
            body['SubUrl'] = request.sub_url
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.vhost):
            body['Vhost'] = request.vhost
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateMcubeNebulaResource',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.CreateMcubeNebulaResourceResponse(),
            self.call_api(params, req, runtime)
        )

    def create_mcube_nebula_resource(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_mcube_nebula_resource_with_options(request, runtime)

    def create_mcube_nebula_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_code):
            body['AppCode'] = request.app_code
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.biz_type):
            body['BizType'] = request.biz_type
        if not UtilClient.is_unset(request.creator):
            body['Creator'] = request.creator
        if not UtilClient.is_unset(request.gmt_create):
            body['GmtCreate'] = request.gmt_create
        if not UtilClient.is_unset(request.gmt_modified):
            body['GmtModified'] = request.gmt_modified
        if not UtilClient.is_unset(request.gmt_modified_str):
            body['GmtModifiedStr'] = request.gmt_modified_str
        if not UtilClient.is_unset(request.grey_config_info):
            body['GreyConfigInfo'] = request.grey_config_info
        if not UtilClient.is_unset(request.grey_endtime):
            body['GreyEndtime'] = request.grey_endtime
        if not UtilClient.is_unset(request.grey_endtime_data):
            body['GreyEndtimeData'] = request.grey_endtime_data
        if not UtilClient.is_unset(request.grey_endtime_str):
            body['GreyEndtimeStr'] = request.grey_endtime_str
        if not UtilClient.is_unset(request.grey_num):
            body['GreyNum'] = request.grey_num
        if not UtilClient.is_unset(request.grey_url):
            body['GreyUrl'] = request.grey_url
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.memo):
            body['Memo'] = request.memo
        if not UtilClient.is_unset(request.modifier):
            body['Modifier'] = request.modifier
        if not UtilClient.is_unset(request.package_id):
            body['PackageId'] = request.package_id
        if not UtilClient.is_unset(request.percent):
            body['Percent'] = request.percent
        if not UtilClient.is_unset(request.platform):
            body['Platform'] = request.platform
        if not UtilClient.is_unset(request.product_id):
            body['ProductId'] = request.product_id
        if not UtilClient.is_unset(request.product_version):
            body['ProductVersion'] = request.product_version
        if not UtilClient.is_unset(request.publish_mode):
            body['PublishMode'] = request.publish_mode
        if not UtilClient.is_unset(request.publish_type):
            body['PublishType'] = request.publish_type
        if not UtilClient.is_unset(request.release_version):
            body['ReleaseVersion'] = request.release_version
        if not UtilClient.is_unset(request.res_ids):
            body['ResIds'] = request.res_ids
        if not UtilClient.is_unset(request.serial_version_uid):
            body['SerialVersionUID'] = request.serial_version_uid
        if not UtilClient.is_unset(request.status):
            body['Status'] = request.status
        if not UtilClient.is_unset(request.sync_mode):
            body['SyncMode'] = request.sync_mode
        if not UtilClient.is_unset(request.sync_result):
            body['SyncResult'] = request.sync_result
        if not UtilClient.is_unset(request.task_name):
            body['TaskName'] = request.task_name
        if not UtilClient.is_unset(request.task_status):
            body['TaskStatus'] = request.task_status
        if not UtilClient.is_unset(request.task_type):
            body['TaskType'] = request.task_type
        if not UtilClient.is_unset(request.task_version):
            body['TaskVersion'] = request.task_version
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.upgrade_notice_num):
            body['UpgradeNoticeNum'] = request.upgrade_notice_num
        if not UtilClient.is_unset(request.upgrade_progress):
            body['UpgradeProgress'] = request.upgrade_progress
        if not UtilClient.is_unset(request.whitelist_ids):
            body['WhitelistIds'] = request.whitelist_ids
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateMcubeNebulaTask',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.CreateMcubeNebulaTaskResponse(),
            self.call_api(params, req, runtime)
        )

    def create_mcube_nebula_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_mcube_nebula_task_with_options(request, runtime)

    def create_mcube_upgrade_package_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.app_version):
            body['AppVersion'] = request.app_version
        if not UtilClient.is_unset(request.appstore_url):
            body['AppstoreUrl'] = request.appstore_url
        if not UtilClient.is_unset(request.bundle_id):
            body['BundleId'] = request.bundle_id
        if not UtilClient.is_unset(request.custom_domain_name):
            body['CustomDomainName'] = request.custom_domain_name
        if not UtilClient.is_unset(request.desc):
            body['Desc'] = request.desc
        if not UtilClient.is_unset(request.download_url):
            body['DownloadUrl'] = request.download_url
        if not UtilClient.is_unset(request.file_url):
            body['FileUrl'] = request.file_url
        if not UtilClient.is_unset(request.icon_file_url):
            body['IconFileUrl'] = request.icon_file_url
        if not UtilClient.is_unset(request.install_amount):
            body['InstallAmount'] = request.install_amount
        if not UtilClient.is_unset(request.ios_symbolfile_url):
            body['IosSymbolfileUrl'] = request.ios_symbolfile_url
        if not UtilClient.is_unset(request.is_enterprise):
            body['IsEnterprise'] = request.is_enterprise
        if not UtilClient.is_unset(request.need_check):
            body['NeedCheck'] = request.need_check
        if not UtilClient.is_unset(request.onex_flag):
            body['OnexFlag'] = request.onex_flag
        if not UtilClient.is_unset(request.platform):
            body['Platform'] = request.platform
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.valid_days):
            body['ValidDays'] = request.valid_days
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateMcubeUpgradePackage',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.CreateMcubeUpgradePackageResponse(),
            self.call_api(params, req, runtime)
        )

    def create_mcube_upgrade_package(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_mcube_upgrade_package_with_options(request, runtime)

    def create_mcube_upgrade_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.grey_config_info):
            body['GreyConfigInfo'] = request.grey_config_info
        if not UtilClient.is_unset(request.grey_endtime_data):
            body['GreyEndtimeData'] = request.grey_endtime_data
        if not UtilClient.is_unset(request.grey_num):
            body['GreyNum'] = request.grey_num
        if not UtilClient.is_unset(request.history_force):
            body['HistoryForce'] = request.history_force
        if not UtilClient.is_unset(request.memo):
            body['Memo'] = request.memo
        if not UtilClient.is_unset(request.package_info_id):
            body['PackageInfoId'] = request.package_info_id
        if not UtilClient.is_unset(request.publish_mode):
            body['PublishMode'] = request.publish_mode
        if not UtilClient.is_unset(request.publish_type):
            body['PublishType'] = request.publish_type
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.upgrade_content):
            body['UpgradeContent'] = request.upgrade_content
        if not UtilClient.is_unset(request.upgrade_type):
            body['UpgradeType'] = request.upgrade_type
        if not UtilClient.is_unset(request.whitelist_ids):
            body['WhitelistIds'] = request.whitelist_ids
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateMcubeUpgradeTask',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.CreateMcubeUpgradeTaskResponse(),
            self.call_api(params, req, runtime)
        )

    def create_mcube_upgrade_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_mcube_upgrade_task_with_options(request, runtime)

    def create_mcube_vhost_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.vhost):
            body['Vhost'] = request.vhost
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateMcubeVhost',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.CreateMcubeVhostResponse(),
            self.call_api(params, req, runtime)
        )

    def create_mcube_vhost(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_mcube_vhost_with_options(request, runtime)

    def create_mcube_whitelist_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.white_list_name):
            body['WhiteListName'] = request.white_list_name
        if not UtilClient.is_unset(request.whitelist_type):
            body['WhitelistType'] = request.whitelist_type
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateMcubeWhitelist',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.CreateMcubeWhitelistResponse(),
            self.call_api(params, req, runtime)
        )

    def create_mcube_whitelist(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_mcube_whitelist_with_options(request, runtime)

    def create_mcube_whitelist_for_ide_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.user_id):
            body['UserId'] = request.user_id
        if not UtilClient.is_unset(request.whitelist_value):
            body['WhitelistValue'] = request.whitelist_value
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateMcubeWhitelistForIde',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.CreateMcubeWhitelistForIdeResponse(),
            self.call_api(params, req, runtime)
        )

    def create_mcube_whitelist_for_ide(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_mcube_whitelist_for_ide_with_options(request, runtime)

    def create_mds_miniprogram_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.grey_config_info):
            body['GreyConfigInfo'] = request.grey_config_info
        if not UtilClient.is_unset(request.grey_endtime_data):
            body['GreyEndtimeData'] = request.grey_endtime_data
        if not UtilClient.is_unset(request.grey_num):
            body['GreyNum'] = request.grey_num
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.memo):
            body['Memo'] = request.memo
        if not UtilClient.is_unset(request.package_id):
            body['PackageId'] = request.package_id
        if not UtilClient.is_unset(request.publish_mode):
            body['PublishMode'] = request.publish_mode
        if not UtilClient.is_unset(request.publish_type):
            body['PublishType'] = request.publish_type
        if not UtilClient.is_unset(request.sync_mode):
            body['SyncMode'] = request.sync_mode
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.whitelist_ids):
            body['WhitelistIds'] = request.whitelist_ids
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateMdsMiniprogramTask',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.CreateMdsMiniprogramTaskResponse(),
            self.call_api(params, req, runtime)
        )

    def create_mds_miniprogram_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_mds_miniprogram_task_with_options(request, runtime)

    def create_msa_enhance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.mpaas_mappcenter_msa_enhance_create_json_str):
            body['MpaasMappcenterMsaEnhanceCreateJsonStr'] = request.mpaas_mappcenter_msa_enhance_create_json_str
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateMsaEnhance',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.CreateMsaEnhanceResponse(),
            self.call_api(params, req, runtime)
        )

    def create_msa_enhance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_msa_enhance_with_options(request, runtime)

    def create_open_global_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.app_max_version):
            body['AppMaxVersion'] = request.app_max_version
        if not UtilClient.is_unset(request.app_min_version):
            body['AppMinVersion'] = request.app_min_version
        if not UtilClient.is_unset(request.biz_type):
            body['BizType'] = request.biz_type
        if not UtilClient.is_unset(request.ext_attr_str):
            body['ExtAttrStr'] = request.ext_attr_str
        if not UtilClient.is_unset(request.max_uid):
            body['MaxUid'] = request.max_uid
        if not UtilClient.is_unset(request.min_uid):
            body['MinUid'] = request.min_uid
        if not UtilClient.is_unset(request.os_type):
            body['OsType'] = request.os_type
        if not UtilClient.is_unset(request.payload):
            body['Payload'] = request.payload
        if not UtilClient.is_unset(request.third_msg_id):
            body['ThirdMsgId'] = request.third_msg_id
        if not UtilClient.is_unset(request.uids):
            body['Uids'] = request.uids
        if not UtilClient.is_unset(request.valid_time_end):
            body['ValidTimeEnd'] = request.valid_time_end
        if not UtilClient.is_unset(request.valid_time_start):
            body['ValidTimeStart'] = request.valid_time_start
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateOpenGlobalData',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.CreateOpenGlobalDataResponse(),
            self.call_api(params, req, runtime)
        )

    def create_open_global_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_open_global_data_with_options(request, runtime)

    def create_open_single_data_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.app_max_version):
            body['AppMaxVersion'] = request.app_max_version
        if not UtilClient.is_unset(request.app_min_version):
            body['AppMinVersion'] = request.app_min_version
        if not UtilClient.is_unset(request.biz_type):
            body['BizType'] = request.biz_type
        if not UtilClient.is_unset(request.check_online):
            body['CheckOnline'] = request.check_online
        if not UtilClient.is_unset(request.ext_attr_str):
            body['ExtAttrStr'] = request.ext_attr_str
        if not UtilClient.is_unset(request.link_token):
            body['LinkToken'] = request.link_token
        if not UtilClient.is_unset(request.os_type):
            body['OsType'] = request.os_type
        if not UtilClient.is_unset(request.payload):
            body['Payload'] = request.payload
        if not UtilClient.is_unset(request.third_msg_id):
            body['ThirdMsgId'] = request.third_msg_id
        if not UtilClient.is_unset(request.valid_time_end):
            body['ValidTimeEnd'] = request.valid_time_end
        if not UtilClient.is_unset(request.valid_time_start):
            body['ValidTimeStart'] = request.valid_time_start
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateOpenSingleData',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.CreateOpenSingleDataResponse(),
            self.call_api(params, req, runtime)
        )

    def create_open_single_data(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_open_single_data_with_options(request, runtime)

    def delete_cubecard_whitelist_content_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.whitelist_id):
            body['WhitelistId'] = request.whitelist_id
        if not UtilClient.is_unset(request.whitelist_value):
            body['WhitelistValue'] = request.whitelist_value
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteCubecardWhitelistContent',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.DeleteCubecardWhitelistContentResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_cubecard_whitelist_content(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_cubecard_whitelist_content_with_options(request, runtime)

    def delete_mcdp_aim_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.mpaas_mappcenter_mcdp_aim_delete_json_str):
            body['MpaasMappcenterMcdpAimDeleteJsonStr'] = request.mpaas_mappcenter_mcdp_aim_delete_json_str
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteMcdpAim',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.DeleteMcdpAimResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_mcdp_aim(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_mcdp_aim_with_options(request, runtime)

    def delete_mcdp_crowd_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.mpaas_mappcenter_mcdp_crowd_delete_json_str):
            body['MpaasMappcenterMcdpCrowdDeleteJsonStr'] = request.mpaas_mappcenter_mcdp_crowd_delete_json_str
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteMcdpCrowd',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.DeleteMcdpCrowdResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_mcdp_crowd(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_mcdp_crowd_with_options(request, runtime)

    def delete_mcdp_event_attribute_by_id_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.mpaas_mappcenter_mcdp_event_attribute_delete_json_str):
            body['MpaasMappcenterMcdpEventAttributeDeleteJsonStr'] = request.mpaas_mappcenter_mcdp_event_attribute_delete_json_str
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteMcdpEventAttributeById',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.DeleteMcdpEventAttributeByIdResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_mcdp_event_attribute_by_id(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_mcdp_event_attribute_by_id_with_options(request, runtime)

    def delete_mcdp_event_by_id_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.mpaas_mappcenter_mcdp_event_delete_json_str):
            body['MpaasMappcenterMcdpEventDeleteJsonStr'] = request.mpaas_mappcenter_mcdp_event_delete_json_str
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteMcdpEventById',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.DeleteMcdpEventByIdResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_mcdp_event_by_id(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_mcdp_event_by_id_with_options(request, runtime)

    def delete_mcdp_material_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.mpaas_mappcenter_mcdp_material_delete_json_str):
            body['MpaasMappcenterMcdpMaterialDeleteJsonStr'] = request.mpaas_mappcenter_mcdp_material_delete_json_str
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteMcdpMaterial',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.DeleteMcdpMaterialResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_mcdp_material(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_mcdp_material_with_options(request, runtime)

    def delete_mcdp_zone_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.mpaas_mappcenter_mcdp_zone_delete_json_str):
            body['MpaasMappcenterMcdpZoneDeleteJsonStr'] = request.mpaas_mappcenter_mcdp_zone_delete_json_str
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteMcdpZone',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.DeleteMcdpZoneResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_mcdp_zone(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_mcdp_zone_with_options(request, runtime)

    def delete_mcube_mini_app_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.h_5id):
            body['H5Id'] = request.h_5id
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteMcubeMiniApp',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.DeleteMcubeMiniAppResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_mcube_mini_app(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_mcube_mini_app_with_options(request, runtime)

    def delete_mcube_nebula_app_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.h_5id):
            body['H5Id'] = request.h_5id
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteMcubeNebulaApp',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.DeleteMcubeNebulaAppResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_mcube_nebula_app(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_mcube_nebula_app_with_options(request, runtime)

    def delete_mcube_upgrade_resource_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.platform):
            body['Platform'] = request.platform
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteMcubeUpgradeResource',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.DeleteMcubeUpgradeResourceResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_mcube_upgrade_resource(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_mcube_upgrade_resource_with_options(request, runtime)

    def delete_mcube_whitelist_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteMcubeWhitelist',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.DeleteMcubeWhitelistResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_mcube_whitelist(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_mcube_whitelist_with_options(request, runtime)

    def delete_mds_whitelist_content_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.whitelist_id):
            body['WhitelistId'] = request.whitelist_id
        if not UtilClient.is_unset(request.whitelist_value):
            body['WhitelistValue'] = request.whitelist_value
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteMdsWhitelistContent',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.DeleteMdsWhitelistContentResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_mds_whitelist_content(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_mds_whitelist_content_with_options(request, runtime)

    def exist_mcube_rsa_key_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ExistMcubeRsaKey',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.ExistMcubeRsaKeyResponse(),
            self.call_api(params, req, runtime)
        )

    def exist_mcube_rsa_key(self, request):
        runtime = util_models.RuntimeOptions()
        return self.exist_mcube_rsa_key_with_options(request, runtime)

    def export_mapp_center_app_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.apk_file_url):
            body['ApkFileUrl'] = request.apk_file_url
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.cert_rsa_base_64):
            body['CertRsaBase64'] = request.cert_rsa_base_64
        if not UtilClient.is_unset(request.identifier):
            body['Identifier'] = request.identifier
        if not UtilClient.is_unset(request.onex_flag):
            body['OnexFlag'] = request.onex_flag
        if not UtilClient.is_unset(request.system_type):
            body['SystemType'] = request.system_type
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ExportMappCenterAppConfig',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.ExportMappCenterAppConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def export_mapp_center_app_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.export_mapp_center_app_config_with_options(request, runtime)

    def get_file_token_for_upload_to_msa_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.onex_flag):
            body['OnexFlag'] = request.onex_flag
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetFileTokenForUploadToMsa',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.GetFileTokenForUploadToMsaResponse(),
            self.call_api(params, req, runtime)
        )

    def get_file_token_for_upload_to_msa(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_file_token_for_upload_to_msa_with_options(request, runtime)

    def get_log_url_in_msa_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetLogUrlInMsa',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.GetLogUrlInMsaResponse(),
            self.call_api(params, req, runtime)
        )

    def get_log_url_in_msa(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_log_url_in_msa_with_options(request, runtime)

    def get_mcube_file_token_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.onex_flag):
            body['OnexFlag'] = request.onex_flag
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetMcubeFileToken',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.GetMcubeFileTokenResponse(),
            self.call_api(params, req, runtime)
        )

    def get_mcube_file_token(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_mcube_file_token_with_options(request, runtime)

    def get_mcube_nebula_resource_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetMcubeNebulaResource',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.GetMcubeNebulaResourceResponse(),
            self.call_api(params, req, runtime)
        )

    def get_mcube_nebula_resource(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_mcube_nebula_resource_with_options(request, runtime)

    def get_mcube_nebula_task_detail_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.task_id):
            body['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetMcubeNebulaTaskDetail',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.GetMcubeNebulaTaskDetailResponse(),
            self.call_api(params, req, runtime)
        )

    def get_mcube_nebula_task_detail(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_mcube_nebula_task_detail_with_options(request, runtime)

    def get_mcube_upgrade_package_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.package_id):
            body['PackageId'] = request.package_id
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetMcubeUpgradePackageInfo',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.GetMcubeUpgradePackageInfoResponse(),
            self.call_api(params, req, runtime)
        )

    def get_mcube_upgrade_package_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_mcube_upgrade_package_info_with_options(request, runtime)

    def get_mcube_upgrade_task_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.task_id):
            body['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetMcubeUpgradeTaskInfo',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.GetMcubeUpgradeTaskInfoResponse(),
            self.call_api(params, req, runtime)
        )

    def get_mcube_upgrade_task_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_mcube_upgrade_task_info_with_options(request, runtime)

    def get_mds_mini_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.h_5id):
            body['H5Id'] = request.h_5id
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetMdsMiniConfig',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.GetMdsMiniConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def get_mds_mini_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_mds_mini_config_with_options(request, runtime)

    def get_user_app_donwload_url_in_msa_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetUserAppDonwloadUrlInMsa',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.GetUserAppDonwloadUrlInMsaResponse(),
            self.call_api(params, req, runtime)
        )

    def get_user_app_donwload_url_in_msa(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_user_app_donwload_url_in_msa_with_options(request, runtime)

    def get_user_app_enhance_process_in_msa_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetUserAppEnhanceProcessInMsa',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.GetUserAppEnhanceProcessInMsaResponse(),
            self.call_api(params, req, runtime)
        )

    def get_user_app_enhance_process_in_msa(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_user_app_enhance_process_in_msa_with_options(request, runtime)

    def get_user_app_upload_process_in_msa_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetUserAppUploadProcessInMsa',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.GetUserAppUploadProcessInMsaResponse(),
            self.call_api(params, req, runtime)
        )

    def get_user_app_upload_process_in_msa(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_user_app_upload_process_in_msa_with_options(request, runtime)

    def list_mapp_center_apps_with_options(self, runtime):
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='ListMappCenterApps',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.ListMappCenterAppsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_mapp_center_apps(self):
        runtime = util_models.RuntimeOptions()
        return self.list_mapp_center_apps_with_options(runtime)

    def list_mapp_center_workspaces_with_options(self, runtime):
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='ListMappCenterWorkspaces',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.ListMappCenterWorkspacesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_mapp_center_workspaces(self):
        runtime = util_models.RuntimeOptions()
        return self.list_mapp_center_workspaces_with_options(runtime)

    def list_mcdp_aim_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.empty_tag):
            body['EmptyTag'] = request.empty_tag
        if not UtilClient.is_unset(request.keyword):
            body['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.page_no):
            body['PageNo'] = request.page_no
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.sort):
            body['Sort'] = request.sort
        if not UtilClient.is_unset(request.sort_field):
            body['SortField'] = request.sort_field
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListMcdpAim',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.ListMcdpAimResponse(),
            self.call_api(params, req, runtime)
        )

    def list_mcdp_aim(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_mcdp_aim_with_options(request, runtime)

    def list_mcube_mini_apps_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.keyword):
            body['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.page_num):
            body['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListMcubeMiniApps',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.ListMcubeMiniAppsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_mcube_mini_apps(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_mcube_mini_apps_with_options(request, runtime)

    def list_mcube_mini_packages_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.h_5id):
            body['H5Id'] = request.h_5id
        if not UtilClient.is_unset(request.package_types):
            body['PackageTypes'] = request.package_types
        if not UtilClient.is_unset(request.page_num):
            body['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListMcubeMiniPackages',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.ListMcubeMiniPackagesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_mcube_mini_packages(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_mcube_mini_packages_with_options(request, runtime)

    def list_mcube_mini_tasks_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListMcubeMiniTasks',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.ListMcubeMiniTasksResponse(),
            self.call_api(params, req, runtime)
        )

    def list_mcube_mini_tasks(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_mcube_mini_tasks_with_options(request, runtime)

    def list_mcube_nebula_apps_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.keyword):
            body['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.page_num):
            body['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListMcubeNebulaApps',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.ListMcubeNebulaAppsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_mcube_nebula_apps(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_mcube_nebula_apps_with_options(request, runtime)

    def list_mcube_nebula_resources_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.h_5id):
            body['H5Id'] = request.h_5id
        if not UtilClient.is_unset(request.page_num):
            body['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListMcubeNebulaResources',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.ListMcubeNebulaResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_mcube_nebula_resources(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_mcube_nebula_resources_with_options(request, runtime)

    def list_mcube_nebula_tasks_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListMcubeNebulaTasks',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.ListMcubeNebulaTasksResponse(),
            self.call_api(params, req, runtime)
        )

    def list_mcube_nebula_tasks(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_mcube_nebula_tasks_with_options(request, runtime)

    def list_mcube_upgrade_packages_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.page_num):
            body['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListMcubeUpgradePackages',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.ListMcubeUpgradePackagesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_mcube_upgrade_packages(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_mcube_upgrade_packages_with_options(request, runtime)

    def list_mcube_upgrade_tasks_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.package_id):
            body['PackageId'] = request.package_id
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListMcubeUpgradeTasks',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.ListMcubeUpgradeTasksResponse(),
            self.call_api(params, req, runtime)
        )

    def list_mcube_upgrade_tasks(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_mcube_upgrade_tasks_with_options(request, runtime)

    def list_mcube_whitelists_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.page_num):
            body['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.whitelist_name):
            body['WhitelistName'] = request.whitelist_name
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListMcubeWhitelists',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.ListMcubeWhitelistsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_mcube_whitelists(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_mcube_whitelists_with_options(request, runtime)

    def list_mgs_api_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.api_status):
            body['ApiStatus'] = request.api_status
        if not UtilClient.is_unset(request.api_type):
            body['ApiType'] = request.api_type
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.format):
            body['Format'] = request.format
        if not UtilClient.is_unset(request.host):
            body['Host'] = request.host
        if not UtilClient.is_unset(request.need_encrypt):
            body['NeedEncrypt'] = request.need_encrypt
        if not UtilClient.is_unset(request.need_etag):
            body['NeedEtag'] = request.need_etag
        if not UtilClient.is_unset(request.need_sign):
            body['NeedSign'] = request.need_sign
        if not UtilClient.is_unset(request.operation_type):
            body['OperationType'] = request.operation_type
        if not UtilClient.is_unset(request.opt_fuzzy):
            body['OptFuzzy'] = request.opt_fuzzy
        if not UtilClient.is_unset(request.page_index):
            body['PageIndex'] = request.page_index
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.sys_id):
            body['SysId'] = request.sys_id
        if not UtilClient.is_unset(request.sys_name):
            body['SysName'] = request.sys_name
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListMgsApi',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.ListMgsApiResponse(),
            self.call_api(params, req, runtime)
        )

    def list_mgs_api(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_mgs_api_with_options(request, runtime)

    def log_msa_query_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.onex_flag):
            body['OnexFlag'] = request.onex_flag
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='LogMsaQuery',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.LogMsaQueryResponse(),
            self.call_api(params, req, runtime)
        )

    def log_msa_query(self, request):
        runtime = util_models.RuntimeOptions()
        return self.log_msa_query_with_options(request, runtime)

    def m_trsocrservice_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.image_raw):
            body['ImageRaw'] = request.image_raw
        if not UtilClient.is_unset(request.mask):
            body['Mask'] = request.mask
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='MTRSOCRService',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.MTRSOCRServiceResponse(),
            self.call_api(params, req, runtime)
        )

    def m_trsocrservice(self, request):
        runtime = util_models.RuntimeOptions()
        return self.m_trsocrservice_with_options(request, runtime)

    def open_api_add_active_code_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.mpaas_mqcp_open_api_add_active_code_req_json_str):
            body['MpaasMqcpOpenApiAddActiveCodeReqJsonStr'] = request.mpaas_mqcp_open_api_add_active_code_req_json_str
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='OpenApiAddActiveCode',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.OpenApiAddActiveCodeResponse(),
            self.call_api(params, req, runtime)
        )

    def open_api_add_active_code(self, request):
        runtime = util_models.RuntimeOptions()
        return self.open_api_add_active_code_with_options(request, runtime)

    def open_api_add_active_scene_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.mpaas_mqcp_open_api_add_active_scene_req_json_str):
            body['MpaasMqcpOpenApiAddActiveSceneReqJsonStr'] = request.mpaas_mqcp_open_api_add_active_scene_req_json_str
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='OpenApiAddActiveScene',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.OpenApiAddActiveSceneResponse(),
            self.call_api(params, req, runtime)
        )

    def open_api_add_active_scene(self, request):
        runtime = util_models.RuntimeOptions()
        return self.open_api_add_active_scene_with_options(request, runtime)

    def open_api_callback_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.mpaas_mqcp_open_api_callback_request_json_str):
            body['MpaasMqcpOpenApiCallbackRequestJsonStr'] = request.mpaas_mqcp_open_api_callback_request_json_str
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='OpenApiCallback',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.OpenApiCallbackResponse(),
            self.call_api(params, req, runtime)
        )

    def open_api_callback(self, request):
        runtime = util_models.RuntimeOptions()
        return self.open_api_callback_with_options(request, runtime)

    def open_api_decode_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.mpaas_mqcp_open_api_decode_request_json_str):
            body['MpaasMqcpOpenApiDecodeRequestJsonStr'] = request.mpaas_mqcp_open_api_decode_request_json_str
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='OpenApiDecode',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.OpenApiDecodeResponse(),
            self.call_api(params, req, runtime)
        )

    def open_api_decode(self, request):
        runtime = util_models.RuntimeOptions()
        return self.open_api_decode_with_options(request, runtime)

    def open_api_delete_active_code_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.mpaas_mqcp_open_api_delete_active_code_req_json_str):
            body['MpaasMqcpOpenApiDeleteActiveCodeReqJsonStr'] = request.mpaas_mqcp_open_api_delete_active_code_req_json_str
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='OpenApiDeleteActiveCode',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.OpenApiDeleteActiveCodeResponse(),
            self.call_api(params, req, runtime)
        )

    def open_api_delete_active_code(self, request):
        runtime = util_models.RuntimeOptions()
        return self.open_api_delete_active_code_with_options(request, runtime)

    def open_api_encode_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.mpaas_mqcp_open_api_encode_request_json_str):
            body['MpaasMqcpOpenApiEncodeRequestJsonStr'] = request.mpaas_mqcp_open_api_encode_request_json_str
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='OpenApiEncode',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.OpenApiEncodeResponse(),
            self.call_api(params, req, runtime)
        )

    def open_api_encode(self, request):
        runtime = util_models.RuntimeOptions()
        return self.open_api_encode_with_options(request, runtime)

    def open_api_query_active_code_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.mpaas_mqcp_open_api_query_active_code_req_json_str):
            body['MpaasMqcpOpenApiQueryActiveCodeReqJsonStr'] = request.mpaas_mqcp_open_api_query_active_code_req_json_str
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='OpenApiQueryActiveCode',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.OpenApiQueryActiveCodeResponse(),
            self.call_api(params, req, runtime)
        )

    def open_api_query_active_code(self, request):
        runtime = util_models.RuntimeOptions()
        return self.open_api_query_active_code_with_options(request, runtime)

    def open_api_query_active_scene_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.mpaas_mqcp_open_api_query_active_scene_req_json_str):
            body['MpaasMqcpOpenApiQueryActiveSceneReqJsonStr'] = request.mpaas_mqcp_open_api_query_active_scene_req_json_str
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='OpenApiQueryActiveScene',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.OpenApiQueryActiveSceneResponse(),
            self.call_api(params, req, runtime)
        )

    def open_api_query_active_scene(self, request):
        runtime = util_models.RuntimeOptions()
        return self.open_api_query_active_scene_with_options(request, runtime)

    def open_api_unique_encode_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.mpaas_mqcp_open_api_unique_encode_request_json_str):
            body['MpaasMqcpOpenApiUniqueEncodeRequestJsonStr'] = request.mpaas_mqcp_open_api_unique_encode_request_json_str
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='OpenApiUniqueEncode',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.OpenApiUniqueEncodeResponse(),
            self.call_api(params, req, runtime)
        )

    def open_api_unique_encode(self, request):
        runtime = util_models.RuntimeOptions()
        return self.open_api_unique_encode_with_options(request, runtime)

    def open_api_update_active_code_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.mpaas_mqcp_open_api_update_active_code_req_json_str):
            body['MpaasMqcpOpenApiUpdateActiveCodeReqJsonStr'] = request.mpaas_mqcp_open_api_update_active_code_req_json_str
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='OpenApiUpdateActiveCode',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.OpenApiUpdateActiveCodeResponse(),
            self.call_api(params, req, runtime)
        )

    def open_api_update_active_code(self, request):
        runtime = util_models.RuntimeOptions()
        return self.open_api_update_active_code_with_options(request, runtime)

    def open_api_update_active_scene_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.mpaas_mqcp_open_api_update_active_scene_req_json_str):
            body['MpaasMqcpOpenApiUpdateActiveSceneReqJsonStr'] = request.mpaas_mqcp_open_api_update_active_scene_req_json_str
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='OpenApiUpdateActiveScene',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.OpenApiUpdateActiveSceneResponse(),
            self.call_api(params, req, runtime)
        )

    def open_api_update_active_scene(self, request):
        runtime = util_models.RuntimeOptions()
        return self.open_api_update_active_scene_with_options(request, runtime)

    def push_bind_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.delivery_token):
            body['DeliveryToken'] = request.delivery_token
        if not UtilClient.is_unset(request.os_type):
            body['OsType'] = request.os_type
        if not UtilClient.is_unset(request.phone_number):
            body['PhoneNumber'] = request.phone_number
        if not UtilClient.is_unset(request.user_id):
            body['UserId'] = request.user_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PushBind',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.PushBindResponse(),
            self.call_api(params, req, runtime)
        )

    def push_bind(self, request):
        runtime = util_models.RuntimeOptions()
        return self.push_bind_with_options(request, runtime)

    def push_broadcast_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = m_paa_s20201028_models.PushBroadcastShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.third_channel_category):
            request.third_channel_category_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.third_channel_category, 'ThirdChannelCategory', 'json')
        body = {}
        if not UtilClient.is_unset(request.android_channel):
            body['AndroidChannel'] = request.android_channel
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.bind_period):
            body['BindPeriod'] = request.bind_period
        if not UtilClient.is_unset(request.channel_id):
            body['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.classification):
            body['Classification'] = request.classification
        if not UtilClient.is_unset(request.delivery_type):
            body['DeliveryType'] = request.delivery_type
        if not UtilClient.is_unset(request.expired_seconds):
            body['ExpiredSeconds'] = request.expired_seconds
        if not UtilClient.is_unset(request.extended_params):
            body['ExtendedParams'] = request.extended_params
        if not UtilClient.is_unset(request.mi_channel_id):
            body['MiChannelId'] = request.mi_channel_id
        if not UtilClient.is_unset(request.msgkey):
            body['Msgkey'] = request.msgkey
        if not UtilClient.is_unset(request.notify_type):
            body['NotifyType'] = request.notify_type
        if not UtilClient.is_unset(request.push_action):
            body['PushAction'] = request.push_action
        if not UtilClient.is_unset(request.push_status):
            body['PushStatus'] = request.push_status
        if not UtilClient.is_unset(request.silent):
            body['Silent'] = request.silent
        if not UtilClient.is_unset(request.strategy_content):
            body['StrategyContent'] = request.strategy_content
        if not UtilClient.is_unset(request.strategy_type):
            body['StrategyType'] = request.strategy_type
        if not UtilClient.is_unset(request.task_name):
            body['TaskName'] = request.task_name
        if not UtilClient.is_unset(request.template_key_value):
            body['TemplateKeyValue'] = request.template_key_value
        if not UtilClient.is_unset(request.template_name):
            body['TemplateName'] = request.template_name
        if not UtilClient.is_unset(request.third_channel_category_shrink):
            body['ThirdChannelCategory'] = request.third_channel_category_shrink
        if not UtilClient.is_unset(request.un_bind_period):
            body['UnBindPeriod'] = request.un_bind_period
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PushBroadcast',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.PushBroadcastResponse(),
            self.call_api(params, req, runtime)
        )

    def push_broadcast(self, request):
        runtime = util_models.RuntimeOptions()
        return self.push_broadcast_with_options(request, runtime)

    def push_multiple_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = m_paa_s20201028_models.PushMultipleShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.third_channel_category):
            request.third_channel_category_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.third_channel_category, 'ThirdChannelCategory', 'json')
        body = {}
        if not UtilClient.is_unset(request.activity_content_state):
            body['ActivityContentState'] = request.activity_content_state
        if not UtilClient.is_unset(request.activity_event):
            body['ActivityEvent'] = request.activity_event
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.channel_id):
            body['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.classification):
            body['Classification'] = request.classification
        if not UtilClient.is_unset(request.delivery_type):
            body['DeliveryType'] = request.delivery_type
        if not UtilClient.is_unset(request.dismissal_date):
            body['DismissalDate'] = request.dismissal_date
        if not UtilClient.is_unset(request.expired_seconds):
            body['ExpiredSeconds'] = request.expired_seconds
        if not UtilClient.is_unset(request.extended_params):
            body['ExtendedParams'] = request.extended_params
        if not UtilClient.is_unset(request.mi_channel_id):
            body['MiChannelId'] = request.mi_channel_id
        if not UtilClient.is_unset(request.notify_type):
            body['NotifyType'] = request.notify_type
        if not UtilClient.is_unset(request.push_action):
            body['PushAction'] = request.push_action
        if not UtilClient.is_unset(request.silent):
            body['Silent'] = request.silent
        if not UtilClient.is_unset(request.strategy_content):
            body['StrategyContent'] = request.strategy_content
        if not UtilClient.is_unset(request.strategy_type):
            body['StrategyType'] = request.strategy_type
        if not UtilClient.is_unset(request.target_msg):
            body['TargetMsg'] = request.target_msg
        if not UtilClient.is_unset(request.task_name):
            body['TaskName'] = request.task_name
        if not UtilClient.is_unset(request.template_name):
            body['TemplateName'] = request.template_name
        if not UtilClient.is_unset(request.third_channel_category_shrink):
            body['ThirdChannelCategory'] = request.third_channel_category_shrink
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PushMultiple',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.PushMultipleResponse(),
            self.call_api(params, req, runtime)
        )

    def push_multiple(self, request):
        runtime = util_models.RuntimeOptions()
        return self.push_multiple_with_options(request, runtime)

    def push_report_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.app_version):
            body['AppVersion'] = request.app_version
        if not UtilClient.is_unset(request.channel):
            body['Channel'] = request.channel
        if not UtilClient.is_unset(request.connect_type):
            body['ConnectType'] = request.connect_type
        if not UtilClient.is_unset(request.delivery_token):
            body['DeliveryToken'] = request.delivery_token
        if not UtilClient.is_unset(request.imei):
            body['Imei'] = request.imei
        if not UtilClient.is_unset(request.imsi):
            body['Imsi'] = request.imsi
        if not UtilClient.is_unset(request.model):
            body['Model'] = request.model
        if not UtilClient.is_unset(request.os_type):
            body['OsType'] = request.os_type
        if not UtilClient.is_unset(request.push_version):
            body['PushVersion'] = request.push_version
        if not UtilClient.is_unset(request.third_channel):
            body['ThirdChannel'] = request.third_channel
        if not UtilClient.is_unset(request.third_channel_device_token):
            body['ThirdChannelDeviceToken'] = request.third_channel_device_token
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PushReport',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.PushReportResponse(),
            self.call_api(params, req, runtime)
        )

    def push_report(self, request):
        runtime = util_models.RuntimeOptions()
        return self.push_report_with_options(request, runtime)

    def push_simple_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = m_paa_s20201028_models.PushSimpleShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.third_channel_category):
            request.third_channel_category_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.third_channel_category, 'ThirdChannelCategory', 'json')
        body = {}
        if not UtilClient.is_unset(request.activity_content_state):
            body['ActivityContentState'] = request.activity_content_state
        if not UtilClient.is_unset(request.activity_event):
            body['ActivityEvent'] = request.activity_event
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.channel_id):
            body['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.classification):
            body['Classification'] = request.classification
        if not UtilClient.is_unset(request.content):
            body['Content'] = request.content
        if not UtilClient.is_unset(request.delivery_type):
            body['DeliveryType'] = request.delivery_type
        if not UtilClient.is_unset(request.dismissal_date):
            body['DismissalDate'] = request.dismissal_date
        if not UtilClient.is_unset(request.expired_seconds):
            body['ExpiredSeconds'] = request.expired_seconds
        if not UtilClient.is_unset(request.extended_params):
            body['ExtendedParams'] = request.extended_params
        if not UtilClient.is_unset(request.icon_urls):
            body['IconUrls'] = request.icon_urls
        if not UtilClient.is_unset(request.image_urls):
            body['ImageUrls'] = request.image_urls
        if not UtilClient.is_unset(request.mi_channel_id):
            body['MiChannelId'] = request.mi_channel_id
        if not UtilClient.is_unset(request.notify_type):
            body['NotifyType'] = request.notify_type
        if not UtilClient.is_unset(request.push_action):
            body['PushAction'] = request.push_action
        if not UtilClient.is_unset(request.push_style):
            body['PushStyle'] = request.push_style
        if not UtilClient.is_unset(request.silent):
            body['Silent'] = request.silent
        if not UtilClient.is_unset(request.sms_sign_name):
            body['SmsSignName'] = request.sms_sign_name
        if not UtilClient.is_unset(request.sms_strategy):
            body['SmsStrategy'] = request.sms_strategy
        if not UtilClient.is_unset(request.sms_template_code):
            body['SmsTemplateCode'] = request.sms_template_code
        if not UtilClient.is_unset(request.sms_template_param):
            body['SmsTemplateParam'] = request.sms_template_param
        if not UtilClient.is_unset(request.strategy_content):
            body['StrategyContent'] = request.strategy_content
        if not UtilClient.is_unset(request.strategy_type):
            body['StrategyType'] = request.strategy_type
        if not UtilClient.is_unset(request.target_msgkey):
            body['TargetMsgkey'] = request.target_msgkey
        if not UtilClient.is_unset(request.task_name):
            body['TaskName'] = request.task_name
        if not UtilClient.is_unset(request.third_channel_category_shrink):
            body['ThirdChannelCategory'] = request.third_channel_category_shrink
        if not UtilClient.is_unset(request.title):
            body['Title'] = request.title
        if not UtilClient.is_unset(request.uri):
            body['Uri'] = request.uri
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PushSimple',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.PushSimpleResponse(),
            self.call_api(params, req, runtime)
        )

    def push_simple(self, request):
        runtime = util_models.RuntimeOptions()
        return self.push_simple_with_options(request, runtime)

    def push_template_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = m_paa_s20201028_models.PushTemplateShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.third_channel_category):
            request.third_channel_category_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.third_channel_category, 'ThirdChannelCategory', 'json')
        body = {}
        if not UtilClient.is_unset(request.activity_content_state):
            body['ActivityContentState'] = request.activity_content_state
        if not UtilClient.is_unset(request.activity_event):
            body['ActivityEvent'] = request.activity_event
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.channel_id):
            body['ChannelId'] = request.channel_id
        if not UtilClient.is_unset(request.classification):
            body['Classification'] = request.classification
        if not UtilClient.is_unset(request.delivery_type):
            body['DeliveryType'] = request.delivery_type
        if not UtilClient.is_unset(request.dismissal_date):
            body['DismissalDate'] = request.dismissal_date
        if not UtilClient.is_unset(request.expired_seconds):
            body['ExpiredSeconds'] = request.expired_seconds
        if not UtilClient.is_unset(request.extended_params):
            body['ExtendedParams'] = request.extended_params
        if not UtilClient.is_unset(request.mi_channel_id):
            body['MiChannelId'] = request.mi_channel_id
        if not UtilClient.is_unset(request.notify_type):
            body['NotifyType'] = request.notify_type
        if not UtilClient.is_unset(request.push_action):
            body['PushAction'] = request.push_action
        if not UtilClient.is_unset(request.silent):
            body['Silent'] = request.silent
        if not UtilClient.is_unset(request.sms_sign_name):
            body['SmsSignName'] = request.sms_sign_name
        if not UtilClient.is_unset(request.sms_strategy):
            body['SmsStrategy'] = request.sms_strategy
        if not UtilClient.is_unset(request.sms_template_code):
            body['SmsTemplateCode'] = request.sms_template_code
        if not UtilClient.is_unset(request.sms_template_param):
            body['SmsTemplateParam'] = request.sms_template_param
        if not UtilClient.is_unset(request.strategy_content):
            body['StrategyContent'] = request.strategy_content
        if not UtilClient.is_unset(request.strategy_type):
            body['StrategyType'] = request.strategy_type
        if not UtilClient.is_unset(request.target_msgkey):
            body['TargetMsgkey'] = request.target_msgkey
        if not UtilClient.is_unset(request.task_name):
            body['TaskName'] = request.task_name
        if not UtilClient.is_unset(request.template_key_value):
            body['TemplateKeyValue'] = request.template_key_value
        if not UtilClient.is_unset(request.template_name):
            body['TemplateName'] = request.template_name
        if not UtilClient.is_unset(request.third_channel_category_shrink):
            body['ThirdChannelCategory'] = request.third_channel_category_shrink
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PushTemplate',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.PushTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    def push_template(self, request):
        runtime = util_models.RuntimeOptions()
        return self.push_template_with_options(request, runtime)

    def push_un_bind_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.delivery_token):
            body['DeliveryToken'] = request.delivery_token
        if not UtilClient.is_unset(request.user_id):
            body['UserId'] = request.user_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='PushUnBind',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.PushUnBindResponse(),
            self.call_api(params, req, runtime)
        )

    def push_un_bind(self, request):
        runtime = util_models.RuntimeOptions()
        return self.push_un_bind_with_options(request, runtime)

    def query_info_from_mdp_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.mobile):
            body['Mobile'] = request.mobile
        if not UtilClient.is_unset(request.mobile_md_5):
            body['MobileMd5'] = request.mobile_md_5
        if not UtilClient.is_unset(request.mobile_sha_256):
            body['MobileSha256'] = request.mobile_sha_256
        if not UtilClient.is_unset(request.risk_scene):
            body['RiskScene'] = request.risk_scene
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryInfoFromMdp',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.QueryInfoFromMdpResponse(),
            self.call_api(params, req, runtime)
        )

    def query_info_from_mdp(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_info_from_mdp_with_options(request, runtime)

    def query_mapp_center_app_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryMappCenterApp',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.QueryMappCenterAppResponse(),
            self.call_api(params, req, runtime)
        )

    def query_mapp_center_app(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_mapp_center_app_with_options(request, runtime)

    def query_mcdp_aim_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryMcdpAim',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.QueryMcdpAimResponse(),
            self.call_api(params, req, runtime)
        )

    def query_mcdp_aim(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_mcdp_aim_with_options(request, runtime)

    def query_mcdp_zone_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryMcdpZone',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.QueryMcdpZoneResponse(),
            self.call_api(params, req, runtime)
        )

    def query_mcdp_zone(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_mcdp_zone_with_options(request, runtime)

    def query_mcube_mini_package_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.h_5id):
            body['H5Id'] = request.h_5id
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryMcubeMiniPackage',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.QueryMcubeMiniPackageResponse(),
            self.call_api(params, req, runtime)
        )

    def query_mcube_mini_package(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_mcube_mini_package_with_options(request, runtime)

    def query_mcube_mini_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.task_id):
            body['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryMcubeMiniTask',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.QueryMcubeMiniTaskResponse(),
            self.call_api(params, req, runtime)
        )

    def query_mcube_mini_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_mcube_mini_task_with_options(request, runtime)

    def query_mcube_vhost_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryMcubeVhost',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.QueryMcubeVhostResponse(),
            self.call_api(params, req, runtime)
        )

    def query_mcube_vhost(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_mcube_vhost_with_options(request, runtime)

    def query_mds_upgrade_task_detail_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.task_id):
            body['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryMdsUpgradeTaskDetail',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.QueryMdsUpgradeTaskDetailResponse(),
            self.call_api(params, req, runtime)
        )

    def query_mds_upgrade_task_detail(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_mds_upgrade_task_detail_with_options(request, runtime)

    def query_mgs_apipage_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.api_status):
            body['ApiStatus'] = request.api_status
        if not UtilClient.is_unset(request.api_type):
            body['ApiType'] = request.api_type
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.format):
            body['Format'] = request.format
        if not UtilClient.is_unset(request.host):
            body['Host'] = request.host
        if not UtilClient.is_unset(request.need_encrypt):
            body['NeedEncrypt'] = request.need_encrypt
        if not UtilClient.is_unset(request.need_etag):
            body['NeedEtag'] = request.need_etag
        if not UtilClient.is_unset(request.need_sign):
            body['NeedSign'] = request.need_sign
        if not UtilClient.is_unset(request.operation_type):
            body['OperationType'] = request.operation_type
        if not UtilClient.is_unset(request.opt_fuzzy):
            body['OptFuzzy'] = request.opt_fuzzy
        if not UtilClient.is_unset(request.page_index):
            body['PageIndex'] = request.page_index
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.sys_id):
            body['SysId'] = request.sys_id
        if not UtilClient.is_unset(request.sys_name):
            body['SysName'] = request.sys_name
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryMgsApipage',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.QueryMgsApipageResponse(),
            self.call_api(params, req, runtime)
        )

    def query_mgs_apipage(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_mgs_apipage_with_options(request, runtime)

    def query_mgs_apirest_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.format):
            body['Format'] = request.format
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryMgsApirest',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.QueryMgsApirestResponse(),
            self.call_api(params, req, runtime)
        )

    def query_mgs_apirest(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_mgs_apirest_with_options(request, runtime)

    def query_mgs_testreqbodyautogen_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.format):
            body['Format'] = request.format
        if not UtilClient.is_unset(request.mpaas_mappcenter_mgs_testreqbodyautogen_query_json_str):
            body['MpaasMappcenterMgsTestreqbodyautogenQueryJsonStr'] = request.mpaas_mappcenter_mgs_testreqbodyautogen_query_json_str
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryMgsTestreqbodyautogen',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.QueryMgsTestreqbodyautogenResponse(),
            self.call_api(params, req, runtime)
        )

    def query_mgs_testreqbodyautogen(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_mgs_testreqbodyautogen_with_options(request, runtime)

    def query_mps_scheduler_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.end_time):
            body['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.start_time):
            body['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        if not UtilClient.is_unset(request.unique_id):
            body['UniqueId'] = request.unique_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryMpsSchedulerList',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.QueryMpsSchedulerListResponse(),
            self.call_api(params, req, runtime)
        )

    def query_mps_scheduler_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_mps_scheduler_list_with_options(request, runtime)

    def query_push_analysis_core_index_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.channel):
            body['Channel'] = request.channel
        if not UtilClient.is_unset(request.end_time):
            body['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.platform):
            body['Platform'] = request.platform
        if not UtilClient.is_unset(request.start_time):
            body['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.task_id):
            body['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryPushAnalysisCoreIndex',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.QueryPushAnalysisCoreIndexResponse(),
            self.call_api(params, req, runtime)
        )

    def query_push_analysis_core_index(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_push_analysis_core_index_with_options(request, runtime)

    def query_push_analysis_task_detail_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.task_id):
            body['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryPushAnalysisTaskDetail',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.QueryPushAnalysisTaskDetailResponse(),
            self.call_api(params, req, runtime)
        )

    def query_push_analysis_task_detail(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_push_analysis_task_detail_with_options(request, runtime)

    def query_push_analysis_task_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.start_time):
            body['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.task_id):
            body['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.task_name):
            body['TaskName'] = request.task_name
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryPushAnalysisTaskList',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.QueryPushAnalysisTaskListResponse(),
            self.call_api(params, req, runtime)
        )

    def query_push_analysis_task_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_push_analysis_task_list_with_options(request, runtime)

    def query_push_scheduler_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.end_time):
            body['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.start_time):
            body['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        if not UtilClient.is_unset(request.unique_id):
            body['UniqueId'] = request.unique_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='QueryPushSchedulerList',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.QueryPushSchedulerListResponse(),
            self.call_api(params, req, runtime)
        )

    def query_push_scheduler_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_push_scheduler_list_with_options(request, runtime)

    def revoke_push_message_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.message_id):
            body['MessageId'] = request.message_id
        if not UtilClient.is_unset(request.target_id):
            body['TargetId'] = request.target_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RevokePushMessage',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.RevokePushMessageResponse(),
            self.call_api(params, req, runtime)
        )

    def revoke_push_message(self, request):
        runtime = util_models.RuntimeOptions()
        return self.revoke_push_message_with_options(request, runtime)

    def revoke_push_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.task_id):
            body['TaskId'] = request.task_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RevokePushTask',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.RevokePushTaskResponse(),
            self.call_api(params, req, runtime)
        )

    def revoke_push_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.revoke_push_task_with_options(request, runtime)

    def run_msa_diff_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.mpaas_mappcenter_msa_diff_run_json_str):
            body['MpaasMappcenterMsaDiffRunJsonStr'] = request.mpaas_mappcenter_msa_diff_run_json_str
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RunMsaDiff',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.RunMsaDiffResponse(),
            self.call_api(params, req, runtime)
        )

    def run_msa_diff(self, request):
        runtime = util_models.RuntimeOptions()
        return self.run_msa_diff_with_options(request, runtime)

    def save_mgs_apirest_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.mpaas_mappcenter_mgs_apirest_save_json_str):
            body['MpaasMappcenterMgsApirestSaveJsonStr'] = request.mpaas_mappcenter_mgs_apirest_save_json_str
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SaveMgsApirest',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.SaveMgsApirestResponse(),
            self.call_api(params, req, runtime)
        )

    def save_mgs_apirest(self, request):
        runtime = util_models.RuntimeOptions()
        return self.save_mgs_apirest_with_options(request, runtime)

    def start_user_app_async_enhance_in_msa_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.apk_protector):
            body['ApkProtector'] = request.apk_protector
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.assets_file_list):
            body['AssetsFileList'] = request.assets_file_list
        if not UtilClient.is_unset(request.classes):
            body['Classes'] = request.classes
        if not UtilClient.is_unset(request.dalvik_debugger):
            body['DalvikDebugger'] = request.dalvik_debugger
        if not UtilClient.is_unset(request.emulator_environment):
            body['EmulatorEnvironment'] = request.emulator_environment
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.java_hook):
            body['JavaHook'] = request.java_hook
        if not UtilClient.is_unset(request.memory_dump):
            body['MemoryDump'] = request.memory_dump
        if not UtilClient.is_unset(request.native_debugger):
            body['NativeDebugger'] = request.native_debugger
        if not UtilClient.is_unset(request.native_hook):
            body['NativeHook'] = request.native_hook
        if not UtilClient.is_unset(request.package_tampered):
            body['PackageTampered'] = request.package_tampered
        if not UtilClient.is_unset(request.root):
            body['Root'] = request.root
        if not UtilClient.is_unset(request.run_mode):
            body['RunMode'] = request.run_mode
        if not UtilClient.is_unset(request.so_file_list):
            body['SoFileList'] = request.so_file_list
        if not UtilClient.is_unset(request.task_type):
            body['TaskType'] = request.task_type
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.total_switch):
            body['TotalSwitch'] = request.total_switch
        if not UtilClient.is_unset(request.use_ashield):
            body['UseAShield'] = request.use_ashield
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='StartUserAppAsyncEnhanceInMsa',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.StartUserAppAsyncEnhanceInMsaResponse(),
            self.call_api(params, req, runtime)
        )

    def start_user_app_async_enhance_in_msa(self, request):
        runtime = util_models.RuntimeOptions()
        return self.start_user_app_async_enhance_in_msa_with_options(request, runtime)

    def update_mcube_whitelist_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.key_ids):
            body['KeyIds'] = request.key_ids
        if not UtilClient.is_unset(request.onex_flag):
            body['OnexFlag'] = request.onex_flag
        if not UtilClient.is_unset(request.oss_url):
            body['OssUrl'] = request.oss_url
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateMcubeWhitelist',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.UpdateMcubeWhitelistResponse(),
            self.call_api(params, req, runtime)
        )

    def update_mcube_whitelist(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_mcube_whitelist_with_options(request, runtime)

    def update_mpaas_app_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.app_name):
            body['AppName'] = request.app_name
        if not UtilClient.is_unset(request.icon_file_url):
            body['IconFileUrl'] = request.icon_file_url
        if not UtilClient.is_unset(request.identifier):
            body['Identifier'] = request.identifier
        if not UtilClient.is_unset(request.onex_flag):
            body['OnexFlag'] = request.onex_flag
        if not UtilClient.is_unset(request.system_type):
            body['SystemType'] = request.system_type
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateMpaasAppInfo',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.UpdateMpaasAppInfoResponse(),
            self.call_api(params, req, runtime)
        )

    def update_mpaas_app_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_mpaas_app_info_with_options(request, runtime)

    def upload_bitcode_to_msa_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.bitcode):
            body['Bitcode'] = request.bitcode
        if not UtilClient.is_unset(request.code_version):
            body['CodeVersion'] = request.code_version
        if not UtilClient.is_unset(request.license):
            body['License'] = request.license
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UploadBitcodeToMsa',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.UploadBitcodeToMsaResponse(),
            self.call_api(params, req, runtime)
        )

    def upload_bitcode_to_msa(self, request):
        runtime = util_models.RuntimeOptions()
        return self.upload_bitcode_to_msa_with_options(request, runtime)

    def upload_mcube_mini_package_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.auto_install):
            body['AutoInstall'] = request.auto_install
        if not UtilClient.is_unset(request.client_version_max):
            body['ClientVersionMax'] = request.client_version_max
        if not UtilClient.is_unset(request.client_version_min):
            body['ClientVersionMin'] = request.client_version_min
        if not UtilClient.is_unset(request.enable_keep_alive):
            body['EnableKeepAlive'] = request.enable_keep_alive
        if not UtilClient.is_unset(request.enable_option_menu):
            body['EnableOptionMenu'] = request.enable_option_menu
        if not UtilClient.is_unset(request.enable_tab_bar):
            body['EnableTabBar'] = request.enable_tab_bar
        if not UtilClient.is_unset(request.extend_info):
            body['ExtendInfo'] = request.extend_info
        if not UtilClient.is_unset(request.h_5id):
            body['H5Id'] = request.h_5id
        if not UtilClient.is_unset(request.h_5name):
            body['H5Name'] = request.h_5name
        if not UtilClient.is_unset(request.h_5version):
            body['H5Version'] = request.h_5version
        if not UtilClient.is_unset(request.icon_file_url):
            body['IconFileUrl'] = request.icon_file_url
        if not UtilClient.is_unset(request.icon_url):
            body['IconUrl'] = request.icon_url
        if not UtilClient.is_unset(request.install_type):
            body['InstallType'] = request.install_type
        if not UtilClient.is_unset(request.main_url):
            body['MainUrl'] = request.main_url
        if not UtilClient.is_unset(request.onex_flag):
            body['OnexFlag'] = request.onex_flag
        if not UtilClient.is_unset(request.package_type):
            body['PackageType'] = request.package_type
        if not UtilClient.is_unset(request.platform):
            body['Platform'] = request.platform
        if not UtilClient.is_unset(request.resource_file_url):
            body['ResourceFileUrl'] = request.resource_file_url
        if not UtilClient.is_unset(request.resource_type):
            body['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.user_id):
            body['UserId'] = request.user_id
        if not UtilClient.is_unset(request.uuid):
            body['Uuid'] = request.uuid
        if not UtilClient.is_unset(request.vhost):
            body['Vhost'] = request.vhost
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UploadMcubeMiniPackage',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.UploadMcubeMiniPackageResponse(),
            self.call_api(params, req, runtime)
        )

    def upload_mcube_mini_package(self, request):
        runtime = util_models.RuntimeOptions()
        return self.upload_mcube_mini_package_with_options(request, runtime)

    def upload_mcube_rsa_key_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.file_url):
            body['FileUrl'] = request.file_url
        if not UtilClient.is_unset(request.onex_flag):
            body['OnexFlag'] = request.onex_flag
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UploadMcubeRsaKey',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.UploadMcubeRsaKeyResponse(),
            self.call_api(params, req, runtime)
        )

    def upload_mcube_rsa_key(self, request):
        runtime = util_models.RuntimeOptions()
        return self.upload_mcube_rsa_key_with_options(request, runtime)

    def upload_user_app_to_msa_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.file_url):
            body['FileUrl'] = request.file_url
        if not UtilClient.is_unset(request.tenant_id):
            body['TenantId'] = request.tenant_id
        if not UtilClient.is_unset(request.workspace_id):
            body['WorkspaceId'] = request.workspace_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UploadUserAppToMsa',
            version='2020-10-28',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            m_paa_s20201028_models.UploadUserAppToMsaResponse(),
            self.call_api(params, req, runtime)
        )

    def upload_user_app_to_msa(self, request):
        runtime = util_models.RuntimeOptions()
        return self.upload_user_app_to_msa_with_options(request, runtime)
