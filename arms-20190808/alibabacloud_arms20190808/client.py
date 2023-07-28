# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_arms20190808 import models as arms20190808_models
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
        self._endpoint_map = {
            'ap-northeast-2-pop': 'arms.aliyuncs.com',
            'cn-beijing-finance-1': 'arms.aliyuncs.com',
            'cn-beijing-finance-pop': 'arms.aliyuncs.com',
            'cn-beijing-gov-1': 'arms.aliyuncs.com',
            'cn-beijing-nu16-b01': 'arms.aliyuncs.com',
            'cn-edge-1': 'arms.aliyuncs.com',
            'cn-fujian': 'arms.aliyuncs.com',
            'cn-haidian-cm12-c01': 'arms.aliyuncs.com',
            'cn-hangzhou-bj-b01': 'arms.aliyuncs.com',
            'cn-hangzhou-internal-prod-1': 'arms.aliyuncs.com',
            'cn-hangzhou-internal-test-1': 'arms.aliyuncs.com',
            'cn-hangzhou-internal-test-2': 'arms.aliyuncs.com',
            'cn-hangzhou-internal-test-3': 'arms.aliyuncs.com',
            'cn-hangzhou-test-306': 'arms.aliyuncs.com',
            'cn-hongkong-finance-pop': 'arms.aliyuncs.com',
            'cn-huhehaote-nebula-1': 'arms.aliyuncs.com',
            'cn-qingdao-nebula': 'arms.aliyuncs.com',
            'cn-shanghai-et15-b01': 'arms.aliyuncs.com',
            'cn-shanghai-et2-b01': 'arms.aliyuncs.com',
            'cn-shanghai-inner': 'arms.aliyuncs.com',
            'cn-shanghai-internal-test-1': 'arms.aliyuncs.com',
            'cn-shenzhen-inner': 'arms.aliyuncs.com',
            'cn-shenzhen-st4-d01': 'arms.aliyuncs.com',
            'cn-shenzhen-su18-b01': 'arms.aliyuncs.com',
            'cn-wuhan': 'arms.aliyuncs.com',
            'cn-yushanfang': 'arms.aliyuncs.com',
            'cn-zhangbei': 'arms.aliyuncs.com',
            'cn-zhangbei-na61-b01': 'arms.aliyuncs.com',
            'cn-zhangjiakou-na62-a01': 'arms.aliyuncs.com',
            'cn-zhengzhou-nebula-1': 'arms.aliyuncs.com',
            'eu-west-1-oxs': 'arms.aliyuncs.com',
            'me-east-1': 'arms.aliyuncs.com',
            'rus-west-1-pop': 'arms.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('arms', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def add_ali_cluster_ids_to_prometheus_global_view_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_ids):
            query['ClusterIds'] = request.cluster_ids
        if not UtilClient.is_unset(request.global_view_cluster_id):
            query['GlobalViewClusterId'] = request.global_view_cluster_id
        if not UtilClient.is_unset(request.group_name):
            query['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddAliClusterIdsToPrometheusGlobalView',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.AddAliClusterIdsToPrometheusGlobalViewResponse(),
            self.call_api(params, req, runtime)
        )

    def add_ali_cluster_ids_to_prometheus_global_view(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_ali_cluster_ids_to_prometheus_global_view_with_options(request, runtime)

    def add_grafana_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.integration):
            query['Integration'] = request.integration
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddGrafana',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.AddGrafanaResponse(),
            self.call_api(params, req, runtime)
        )

    def add_grafana(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_grafana_with_options(request, runtime)

    def add_integration_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.integration):
            query['Integration'] = request.integration
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddIntegration',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.AddIntegrationResponse(),
            self.call_api(params, req, runtime)
        )

    def add_integration(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_integration_with_options(request, runtime)

    def add_prometheus_global_view_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.clusters):
            query['Clusters'] = request.clusters
        if not UtilClient.is_unset(request.group_name):
            query['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddPrometheusGlobalView',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.AddPrometheusGlobalViewResponse(),
            self.call_api(params, req, runtime)
        )

    def add_prometheus_global_view(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_prometheus_global_view_with_options(request, runtime)

    def add_prometheus_global_view_by_ali_cluster_ids_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_ids):
            query['ClusterIds'] = request.cluster_ids
        if not UtilClient.is_unset(request.group_name):
            query['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.product_code):
            query['ProductCode'] = request.product_code
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddPrometheusGlobalViewByAliClusterIds',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.AddPrometheusGlobalViewByAliClusterIdsResponse(),
            self.call_api(params, req, runtime)
        )

    def add_prometheus_global_view_by_ali_cluster_ids(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_prometheus_global_view_by_ali_cluster_ids_with_options(request, runtime)

    def add_prometheus_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddPrometheusInstance',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.AddPrometheusInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    def add_prometheus_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_prometheus_instance_with_options(request, runtime)

    def add_prometheus_integration_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.integration_type):
            query['IntegrationType'] = request.integration_type
        if not UtilClient.is_unset(request.param):
            query['Param'] = request.param
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddPrometheusIntegration',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.AddPrometheusIntegrationResponse(),
            self.call_api(params, req, runtime)
        )

    def add_prometheus_integration(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_prometheus_integration_with_options(request, runtime)

    def add_prometheus_remote_write_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not UtilClient.is_unset(request.remote_write_yaml):
            body['RemoteWriteYaml'] = request.remote_write_yaml
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AddPrometheusRemoteWrite',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.AddPrometheusRemoteWriteResponse(),
            self.call_api(params, req, runtime)
        )

    def add_prometheus_remote_write(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_prometheus_remote_write_with_options(request, runtime)

    def add_recording_rule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.rule_yaml):
            query['RuleYaml'] = request.rule_yaml
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddRecordingRule',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.AddRecordingRuleResponse(),
            self.call_api(params, req, runtime)
        )

    def add_recording_rule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_recording_rule_with_options(request, runtime)

    def append_instances_to_prometheus_global_view_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.clusters):
            query['Clusters'] = request.clusters
        if not UtilClient.is_unset(request.global_view_cluster_id):
            query['GlobalViewClusterId'] = request.global_view_cluster_id
        if not UtilClient.is_unset(request.group_name):
            query['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AppendInstancesToPrometheusGlobalView',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.AppendInstancesToPrometheusGlobalViewResponse(),
            self.call_api(params, req, runtime)
        )

    def append_instances_to_prometheus_global_view(self, request):
        runtime = util_models.RuntimeOptions()
        return self.append_instances_to_prometheus_global_view_with_options(request, runtime)

    def apply_scenario_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = arms20190808_models.ApplyScenarioShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.config):
            request.config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.config, 'Config', 'json')
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.config_shrink):
            query['Config'] = request.config_shrink
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.scenario):
            query['Scenario'] = request.scenario
        if not UtilClient.is_unset(request.sign):
            query['Sign'] = request.sign
        if not UtilClient.is_unset(request.sn_dump):
            query['SnDump'] = request.sn_dump
        if not UtilClient.is_unset(request.sn_force):
            query['SnForce'] = request.sn_force
        if not UtilClient.is_unset(request.sn_stat):
            query['SnStat'] = request.sn_stat
        if not UtilClient.is_unset(request.sn_transfer):
            query['SnTransfer'] = request.sn_transfer
        if not UtilClient.is_unset(request.update_option):
            query['UpdateOption'] = request.update_option
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ApplyScenario',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.ApplyScenarioResponse(),
            self.call_api(params, req, runtime)
        )

    def apply_scenario(self, request):
        runtime = util_models.RuntimeOptions()
        return self.apply_scenario_with_options(request, runtime)

    def bind_prometheus_grafana_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.grafana_instance_id):
            query['GrafanaInstanceId'] = request.grafana_instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BindPrometheusGrafanaInstance',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.BindPrometheusGrafanaInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    def bind_prometheus_grafana_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.bind_prometheus_grafana_instance_with_options(request, runtime)

    def change_resource_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.new_resource_group_id):
            query['NewResourceGroupId'] = request.new_resource_group_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ChangeResourceGroup',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.ChangeResourceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def change_resource_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.change_resource_group_with_options(request, runtime)

    def check_service_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.svc_code):
            query['SvcCode'] = request.svc_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CheckServiceStatus',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.CheckServiceStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def check_service_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.check_service_status_with_options(request, runtime)

    def config_app_with_options(self, request, runtime):
        """
        ***\
        

        @param request: ConfigAppRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ConfigAppResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_ids):
            query['AppIds'] = request.app_ids
        if not UtilClient.is_unset(request.enable):
            query['Enable'] = request.enable
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ConfigApp',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.ConfigAppResponse(),
            self.call_api(params, req, runtime)
        )

    def config_app(self, request):
        """
        ***\
        

        @param request: ConfigAppRequest

        @return: ConfigAppResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.config_app_with_options(request, runtime)

    def create_alert_contact_with_options(self, request, runtime):
        """
        The ID of the request.
        

        @param request: CreateAlertContactRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateAlertContactResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.contact_name):
            query['ContactName'] = request.contact_name
        if not UtilClient.is_unset(request.ding_robot_webhook_url):
            query['DingRobotWebhookUrl'] = request.ding_robot_webhook_url
        if not UtilClient.is_unset(request.email):
            query['Email'] = request.email
        if not UtilClient.is_unset(request.phone_num):
            query['PhoneNum'] = request.phone_num
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.system_noc):
            query['SystemNoc'] = request.system_noc
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateAlertContact',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.CreateAlertContactResponse(),
            self.call_api(params, req, runtime)
        )

    def create_alert_contact(self, request):
        """
        The ID of the request.
        

        @param request: CreateAlertContactRequest

        @return: CreateAlertContactResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_alert_contact_with_options(request, runtime)

    def create_alert_contact_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.contact_group_name):
            query['ContactGroupName'] = request.contact_group_name
        if not UtilClient.is_unset(request.contact_ids):
            query['ContactIds'] = request.contact_ids
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateAlertContactGroup',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.CreateAlertContactGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def create_alert_contact_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_alert_contact_group_with_options(request, runtime)

    def create_dispatch_rule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dispatch_rule):
            query['DispatchRule'] = request.dispatch_rule
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDispatchRule',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.CreateDispatchRuleResponse(),
            self.call_api(params, req, runtime)
        )

    def create_dispatch_rule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_dispatch_rule_with_options(request, runtime)

    def create_integration_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.auto_recover):
            body['AutoRecover'] = request.auto_recover
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.integration_name):
            body['IntegrationName'] = request.integration_name
        if not UtilClient.is_unset(request.integration_product_type):
            body['IntegrationProductType'] = request.integration_product_type
        if not UtilClient.is_unset(request.recover_time):
            body['RecoverTime'] = request.recover_time
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateIntegration',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.CreateIntegrationResponse(),
            self.call_api(params, req, runtime)
        )

    def create_integration(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_integration_with_options(request, runtime)

    def create_or_update_alert_rule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.alert_check_type):
            body['AlertCheckType'] = request.alert_check_type
        if not UtilClient.is_unset(request.alert_group):
            body['AlertGroup'] = request.alert_group
        if not UtilClient.is_unset(request.alert_id):
            body['AlertId'] = request.alert_id
        if not UtilClient.is_unset(request.alert_name):
            body['AlertName'] = request.alert_name
        if not UtilClient.is_unset(request.alert_rule_content):
            body['AlertRuleContent'] = request.alert_rule_content
        if not UtilClient.is_unset(request.alert_status):
            body['AlertStatus'] = request.alert_status
        if not UtilClient.is_unset(request.alert_type):
            body['AlertType'] = request.alert_type
        if not UtilClient.is_unset(request.annotations):
            body['Annotations'] = request.annotations
        if not UtilClient.is_unset(request.auto_add_new_application):
            body['AutoAddNewApplication'] = request.auto_add_new_application
        if not UtilClient.is_unset(request.cluster_id):
            body['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.duration):
            body['Duration'] = request.duration
        if not UtilClient.is_unset(request.filters):
            body['Filters'] = request.filters
        if not UtilClient.is_unset(request.labels):
            body['Labels'] = request.labels
        if not UtilClient.is_unset(request.level):
            body['Level'] = request.level
        if not UtilClient.is_unset(request.message):
            body['Message'] = request.message
        if not UtilClient.is_unset(request.metrics_key):
            body['MetricsKey'] = request.metrics_key
        if not UtilClient.is_unset(request.metrics_type):
            body['MetricsType'] = request.metrics_type
        if not UtilClient.is_unset(request.notify_strategy):
            body['NotifyStrategy'] = request.notify_strategy
        if not UtilClient.is_unset(request.pids):
            body['Pids'] = request.pids
        if not UtilClient.is_unset(request.prom_ql):
            body['PromQL'] = request.prom_ql
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.tags):
            body['Tags'] = request.tags
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateOrUpdateAlertRule',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.CreateOrUpdateAlertRuleResponse(),
            self.call_api(params, req, runtime)
        )

    def create_or_update_alert_rule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_or_update_alert_rule_with_options(request, runtime)

    def create_or_update_contact_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ding_robot_url):
            query['DingRobotUrl'] = request.ding_robot_url
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        body = {}
        if not UtilClient.is_unset(request.contact_id):
            body['ContactId'] = request.contact_id
        if not UtilClient.is_unset(request.contact_name):
            body['ContactName'] = request.contact_name
        if not UtilClient.is_unset(request.email):
            body['Email'] = request.email
        if not UtilClient.is_unset(request.is_email_verify):
            body['IsEmailVerify'] = request.is_email_verify
        if not UtilClient.is_unset(request.phone):
            body['Phone'] = request.phone
        if not UtilClient.is_unset(request.reissue_send_notice):
            body['ReissueSendNotice'] = request.reissue_send_notice
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateOrUpdateContact',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.CreateOrUpdateContactResponse(),
            self.call_api(params, req, runtime)
        )

    def create_or_update_contact(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_or_update_contact_with_options(request, runtime)

    def create_or_update_contact_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.contact_group_id):
            body['ContactGroupId'] = request.contact_group_id
        if not UtilClient.is_unset(request.contact_group_name):
            body['ContactGroupName'] = request.contact_group_name
        if not UtilClient.is_unset(request.contact_ids):
            body['ContactIds'] = request.contact_ids
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateOrUpdateContactGroup',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.CreateOrUpdateContactGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def create_or_update_contact_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_or_update_contact_group_with_options(request, runtime)

    def create_or_update_event_bridge_integration_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.access_key):
            body['AccessKey'] = request.access_key
        if not UtilClient.is_unset(request.access_secret):
            body['AccessSecret'] = request.access_secret
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.endpoint):
            body['Endpoint'] = request.endpoint
        if not UtilClient.is_unset(request.event_bus_name):
            body['EventBusName'] = request.event_bus_name
        if not UtilClient.is_unset(request.event_bus_region_id):
            body['EventBusRegionId'] = request.event_bus_region_id
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.source):
            body['Source'] = request.source
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateOrUpdateEventBridgeIntegration',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.CreateOrUpdateEventBridgeIntegrationResponse(),
            self.call_api(params, req, runtime)
        )

    def create_or_update_event_bridge_integration(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_or_update_event_bridge_integration_with_options(request, runtime)

    def create_or_update_imrobot_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.card_template):
            body['CardTemplate'] = request.card_template
        if not UtilClient.is_unset(request.daily_noc):
            body['DailyNoc'] = request.daily_noc
        if not UtilClient.is_unset(request.daily_noc_time):
            body['DailyNocTime'] = request.daily_noc_time
        if not UtilClient.is_unset(request.ding_sign_key):
            body['DingSignKey'] = request.ding_sign_key
        if not UtilClient.is_unset(request.enable_outgoing):
            body['EnableOutgoing'] = request.enable_outgoing
        if not UtilClient.is_unset(request.robot_address):
            body['RobotAddress'] = request.robot_address
        if not UtilClient.is_unset(request.robot_id):
            body['RobotId'] = request.robot_id
        if not UtilClient.is_unset(request.robot_name):
            body['RobotName'] = request.robot_name
        if not UtilClient.is_unset(request.token):
            body['Token'] = request.token
        if not UtilClient.is_unset(request.type):
            body['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateOrUpdateIMRobot',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.CreateOrUpdateIMRobotResponse(),
            self.call_api(params, req, runtime)
        )

    def create_or_update_imrobot(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_or_update_imrobot_with_options(request, runtime)

    def create_or_update_notification_policy_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.escalation_policy_id):
            body['EscalationPolicyId'] = request.escalation_policy_id
        if not UtilClient.is_unset(request.group_rule):
            body['GroupRule'] = request.group_rule
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.integration_id):
            body['IntegrationId'] = request.integration_id
        if not UtilClient.is_unset(request.matching_rules):
            body['MatchingRules'] = request.matching_rules
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.notify_rule):
            body['NotifyRule'] = request.notify_rule
        if not UtilClient.is_unset(request.notify_template):
            body['NotifyTemplate'] = request.notify_template
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.repeat):
            body['Repeat'] = request.repeat
        if not UtilClient.is_unset(request.repeat_interval):
            body['RepeatInterval'] = request.repeat_interval
        if not UtilClient.is_unset(request.send_recover_message):
            body['SendRecoverMessage'] = request.send_recover_message
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateOrUpdateNotificationPolicy',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.CreateOrUpdateNotificationPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    def create_or_update_notification_policy(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_or_update_notification_policy_with_options(request, runtime)

    def create_or_update_silence_policy_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        if not UtilClient.is_unset(request.matching_rules):
            body['MatchingRules'] = request.matching_rules
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateOrUpdateSilencePolicy',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.CreateOrUpdateSilencePolicyResponse(),
            self.call_api(params, req, runtime)
        )

    def create_or_update_silence_policy(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_or_update_silence_policy_with_options(request, runtime)

    def create_or_update_webhook_contact_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.biz_headers):
            body['BizHeaders'] = request.biz_headers
        if not UtilClient.is_unset(request.biz_params):
            body['BizParams'] = request.biz_params
        if not UtilClient.is_unset(request.body):
            body['Body'] = request.body
        if not UtilClient.is_unset(request.method):
            body['Method'] = request.method
        if not UtilClient.is_unset(request.recover_body):
            body['RecoverBody'] = request.recover_body
        if not UtilClient.is_unset(request.url):
            body['Url'] = request.url
        if not UtilClient.is_unset(request.webhook_id):
            body['WebhookId'] = request.webhook_id
        if not UtilClient.is_unset(request.webhook_name):
            body['WebhookName'] = request.webhook_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateOrUpdateWebhookContact',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.CreateOrUpdateWebhookContactResponse(),
            self.call_api(params, req, runtime)
        )

    def create_or_update_webhook_contact(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_or_update_webhook_contact_with_options(request, runtime)

    def create_prometheus_alert_rule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alert_name):
            query['AlertName'] = request.alert_name
        if not UtilClient.is_unset(request.annotations):
            query['Annotations'] = request.annotations
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.dispatch_rule_id):
            query['DispatchRuleId'] = request.dispatch_rule_id
        if not UtilClient.is_unset(request.duration):
            query['Duration'] = request.duration
        if not UtilClient.is_unset(request.expression):
            query['Expression'] = request.expression
        if not UtilClient.is_unset(request.labels):
            query['Labels'] = request.labels
        if not UtilClient.is_unset(request.message):
            query['Message'] = request.message
        if not UtilClient.is_unset(request.notify_type):
            query['NotifyType'] = request.notify_type
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreatePrometheusAlertRule',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.CreatePrometheusAlertRuleResponse(),
            self.call_api(params, req, runtime)
        )

    def create_prometheus_alert_rule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_prometheus_alert_rule_with_options(request, runtime)

    def create_prometheus_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.all_sub_clusters_success):
            query['AllSubClustersSuccess'] = request.all_sub_clusters_success
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.cluster_name):
            query['ClusterName'] = request.cluster_name
        if not UtilClient.is_unset(request.cluster_type):
            query['ClusterType'] = request.cluster_type
        if not UtilClient.is_unset(request.grafana_instance_id):
            query['GrafanaInstanceId'] = request.grafana_instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.security_group_id):
            query['SecurityGroupId'] = request.security_group_id
        if not UtilClient.is_unset(request.sub_clusters_json):
            query['SubClustersJson'] = request.sub_clusters_json
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
        if not UtilClient.is_unset(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreatePrometheusInstance',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.CreatePrometheusInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    def create_prometheus_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_prometheus_instance_with_options(request, runtime)

    def create_prometheus_monitoring_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        body = {}
        if not UtilClient.is_unset(request.config_yaml):
            body['ConfigYaml'] = request.config_yaml
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreatePrometheusMonitoring',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.CreatePrometheusMonitoringResponse(),
            self.call_api(params, req, runtime)
        )

    def create_prometheus_monitoring(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_prometheus_monitoring_with_options(request, runtime)

    def create_retcode_app_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.retcode_app_name):
            query['RetcodeAppName'] = request.retcode_app_name
        if not UtilClient.is_unset(request.retcode_app_type):
            query['RetcodeAppType'] = request.retcode_app_type
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateRetcodeApp',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.CreateRetcodeAppResponse(),
            self.call_api(params, req, runtime)
        )

    def create_retcode_app(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_retcode_app_with_options(request, runtime)

    def create_synthetic_task_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = arms20190808_models.CreateSyntheticTaskShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.common_param):
            request.common_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.common_param, 'CommonParam', 'json')
        if not UtilClient.is_unset(tmp_req.download):
            request.download_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.download, 'Download', 'json')
        if not UtilClient.is_unset(tmp_req.extend_interval):
            request.extend_interval_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.extend_interval, 'ExtendInterval', 'json')
        if not UtilClient.is_unset(tmp_req.monitor_list):
            request.monitor_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.monitor_list, 'MonitorList', 'json')
        if not UtilClient.is_unset(tmp_req.navigation):
            request.navigation_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.navigation, 'Navigation', 'json')
        if not UtilClient.is_unset(tmp_req.net):
            request.net_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.net, 'Net', 'json')
        if not UtilClient.is_unset(tmp_req.protocol):
            request.protocol_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.protocol, 'Protocol', 'json')
        query = {}
        if not UtilClient.is_unset(request.common_param_shrink):
            query['CommonParam'] = request.common_param_shrink
        if not UtilClient.is_unset(request.download_shrink):
            query['Download'] = request.download_shrink
        if not UtilClient.is_unset(request.extend_interval_shrink):
            query['ExtendInterval'] = request.extend_interval_shrink
        if not UtilClient.is_unset(request.interval_time):
            query['IntervalTime'] = request.interval_time
        if not UtilClient.is_unset(request.interval_type):
            query['IntervalType'] = request.interval_type
        if not UtilClient.is_unset(request.ip_type):
            query['IpType'] = request.ip_type
        if not UtilClient.is_unset(request.monitor_list_shrink):
            query['MonitorList'] = request.monitor_list_shrink
        if not UtilClient.is_unset(request.navigation_shrink):
            query['Navigation'] = request.navigation_shrink
        if not UtilClient.is_unset(request.net_shrink):
            query['Net'] = request.net_shrink
        if not UtilClient.is_unset(request.protocol_shrink):
            query['Protocol'] = request.protocol_shrink
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.task_name):
            query['TaskName'] = request.task_name
        if not UtilClient.is_unset(request.task_type):
            query['TaskType'] = request.task_type
        if not UtilClient.is_unset(request.update_task):
            query['UpdateTask'] = request.update_task
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateSyntheticTask',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.CreateSyntheticTaskResponse(),
            self.call_api(params, req, runtime)
        )

    def create_synthetic_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_synthetic_task_with_options(request, runtime)

    def create_webhook_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.body):
            query['Body'] = request.body
        if not UtilClient.is_unset(request.contact_name):
            query['ContactName'] = request.contact_name
        if not UtilClient.is_unset(request.http_headers):
            query['HttpHeaders'] = request.http_headers
        if not UtilClient.is_unset(request.http_params):
            query['HttpParams'] = request.http_params
        if not UtilClient.is_unset(request.method):
            query['Method'] = request.method
        if not UtilClient.is_unset(request.recover_body):
            query['RecoverBody'] = request.recover_body
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateWebhook',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.CreateWebhookResponse(),
            self.call_api(params, req, runtime)
        )

    def create_webhook(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_webhook_with_options(request, runtime)

    def del_auth_token_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DelAuthToken',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.DelAuthTokenResponse(),
            self.call_api(params, req, runtime)
        )

    def del_auth_token(self, request):
        runtime = util_models.RuntimeOptions()
        return self.del_auth_token_with_options(request, runtime)

    def delete_alert_contact_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.contact_id):
            query['ContactId'] = request.contact_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteAlertContact',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.DeleteAlertContactResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_alert_contact(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_alert_contact_with_options(request, runtime)

    def delete_alert_contact_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.contact_group_id):
            query['ContactGroupId'] = request.contact_group_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteAlertContactGroup',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.DeleteAlertContactGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_alert_contact_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_alert_contact_group_with_options(request, runtime)

    def delete_alert_rule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alert_id):
            query['AlertId'] = request.alert_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteAlertRule',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.DeleteAlertRuleResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_alert_rule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_alert_rule_with_options(request, runtime)

    def delete_alert_rules_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alert_ids):
            query['AlertIds'] = request.alert_ids
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteAlertRules',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.DeleteAlertRulesResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_alert_rules(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_alert_rules_with_options(request, runtime)

    def delete_cms_exporter_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteCmsExporter',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.DeleteCmsExporterResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_cms_exporter(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_cms_exporter_with_options(request, runtime)

    def delete_contact_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.contact_id):
            query['ContactId'] = request.contact_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteContact',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.DeleteContactResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_contact(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_contact_with_options(request, runtime)

    def delete_contact_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.contact_group_id):
            query['ContactGroupId'] = request.contact_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteContactGroup',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.DeleteContactGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_contact_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_contact_group_with_options(request, runtime)

    def delete_dispatch_rule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDispatchRule',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.DeleteDispatchRuleResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_dispatch_rule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_dispatch_rule_with_options(request, runtime)

    def delete_event_bridge_integration_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.id):
            body['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteEventBridgeIntegration',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.DeleteEventBridgeIntegrationResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_event_bridge_integration(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_event_bridge_integration_with_options(request, runtime)

    def delete_grafana_resource_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        body = {}
        if not UtilClient.is_unset(request.cluster_id):
            body['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.cluster_name):
            body['ClusterName'] = request.cluster_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteGrafanaResource',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.DeleteGrafanaResourceResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_grafana_resource(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_grafana_resource_with_options(request, runtime)

    def delete_imrobot_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.robot_id):
            query['RobotId'] = request.robot_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteIMRobot',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.DeleteIMRobotResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_imrobot(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_imrobot_with_options(request, runtime)

    def delete_integration_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.integration):
            query['Integration'] = request.integration
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteIntegration',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.DeleteIntegrationResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_integration(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_integration_with_options(request, runtime)

    def delete_integrations_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteIntegrations',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.DeleteIntegrationsResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_integrations(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_integrations_with_options(request, runtime)

    def delete_notification_policy_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteNotificationPolicy',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.DeleteNotificationPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_notification_policy(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_notification_policy_with_options(request, runtime)

    def delete_prometheus_alert_rule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alert_id):
            query['AlertId'] = request.alert_id
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeletePrometheusAlertRule',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.DeletePrometheusAlertRuleResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_prometheus_alert_rule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_prometheus_alert_rule_with_options(request, runtime)

    def delete_prometheus_global_view_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.global_view_cluster_id):
            query['GlobalViewClusterId'] = request.global_view_cluster_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeletePrometheusGlobalView',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.DeletePrometheusGlobalViewResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_prometheus_global_view(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_prometheus_global_view_with_options(request, runtime)

    def delete_prometheus_integration_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.integration_type):
            query['IntegrationType'] = request.integration_type
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeletePrometheusIntegration',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.DeletePrometheusIntegrationResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_prometheus_integration(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_prometheus_integration_with_options(request, runtime)

    def delete_prometheus_monitoring_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.monitoring_name):
            query['MonitoringName'] = request.monitoring_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeletePrometheusMonitoring',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.DeletePrometheusMonitoringResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_prometheus_monitoring(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_prometheus_monitoring_with_options(request, runtime)

    def delete_prometheus_remote_write_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.remote_write_names):
            query['RemoteWriteNames'] = request.remote_write_names
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeletePrometheusRemoteWrite',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.DeletePrometheusRemoteWriteResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_prometheus_remote_write(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_prometheus_remote_write_with_options(request, runtime)

    def delete_retcode_app_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.pid):
            query['Pid'] = request.pid
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteRetcodeApp',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.DeleteRetcodeAppResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_retcode_app(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_retcode_app_with_options(request, runtime)

    def delete_scenario_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.scenario_id):
            query['ScenarioId'] = request.scenario_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteScenario',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.DeleteScenarioResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_scenario(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_scenario_with_options(request, runtime)

    def delete_silence_policy_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteSilencePolicy',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.DeleteSilencePolicyResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_silence_policy(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_silence_policy_with_options(request, runtime)

    def delete_source_map_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = arms20190808_models.DeleteSourceMapShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.fid_list):
            request.fid_list_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.fid_list, 'FidList', 'json')
        query = {}
        if not UtilClient.is_unset(request.fid_list_shrink):
            query['FidList'] = request.fid_list_shrink
        if not UtilClient.is_unset(request.pid):
            query['Pid'] = request.pid
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteSourceMap',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.DeleteSourceMapResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_source_map(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_source_map_with_options(request, runtime)

    def delete_synthetic_task_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.task_ids):
            query['TaskIds'] = request.task_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteSyntheticTask',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.DeleteSyntheticTaskResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_synthetic_task(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_synthetic_task_with_options(request, runtime)

    def delete_trace_app_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.pid):
            query['Pid'] = request.pid
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteTraceApp',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.DeleteTraceAppResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_trace_app(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_trace_app_with_options(request, runtime)

    def delete_webhook_contact_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.webhook_id):
            query['WebhookId'] = request.webhook_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteWebhookContact',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.DeleteWebhookContactResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_webhook_contact(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_webhook_contact_with_options(request, runtime)

    def describe_contact_groups_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.contact_group_name):
            query['ContactGroupName'] = request.contact_group_name
        if not UtilClient.is_unset(request.group_ids):
            query['GroupIds'] = request.group_ids
        if not UtilClient.is_unset(request.is_detail):
            query['IsDetail'] = request.is_detail
        if not UtilClient.is_unset(request.page):
            query['Page'] = request.page
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.size):
            query['Size'] = request.size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeContactGroups',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.DescribeContactGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_contact_groups(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_contact_groups_with_options(request, runtime)

    def describe_contacts_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.contact_ids):
            query['ContactIds'] = request.contact_ids
        if not UtilClient.is_unset(request.contact_name):
            query['ContactName'] = request.contact_name
        if not UtilClient.is_unset(request.email):
            query['Email'] = request.email
        if not UtilClient.is_unset(request.page):
            query['Page'] = request.page
        if not UtilClient.is_unset(request.phone):
            query['Phone'] = request.phone
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.size):
            query['Size'] = request.size
        if not UtilClient.is_unset(request.verbose):
            query['Verbose'] = request.verbose
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeContacts',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.DescribeContactsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_contacts(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_contacts_with_options(request, runtime)

    def describe_dispatch_rule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDispatchRule',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.DescribeDispatchRuleResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_dispatch_rule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dispatch_rule_with_options(request, runtime)

    def describe_imrobots_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page):
            query['Page'] = request.page
        if not UtilClient.is_unset(request.robot_ids):
            query['RobotIds'] = request.robot_ids
        if not UtilClient.is_unset(request.robot_name):
            query['RobotName'] = request.robot_name
        if not UtilClient.is_unset(request.size):
            query['Size'] = request.size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeIMRobots',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.DescribeIMRobotsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_imrobots(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_imrobots_with_options(request, runtime)

    def describe_prometheus_alert_rule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alert_id):
            query['AlertId'] = request.alert_id
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePrometheusAlertRule',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.DescribePrometheusAlertRuleResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_prometheus_alert_rule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_prometheus_alert_rule_with_options(request, runtime)

    def describe_trace_license_key_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeTraceLicenseKey',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.DescribeTraceLicenseKeyResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_trace_license_key(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_trace_license_key_with_options(request, runtime)

    def describe_webhook_contacts_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeWebhookContacts',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.DescribeWebhookContactsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_webhook_contacts(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_webhook_contacts_with_options(request, runtime)

    def enable_metric_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.drop_metric):
            query['DropMetric'] = request.drop_metric
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnableMetric',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.EnableMetricResponse(),
            self.call_api(params, req, runtime)
        )

    def enable_metric(self, request):
        runtime = util_models.RuntimeOptions()
        return self.enable_metric_with_options(request, runtime)

    def get_agent_download_url_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAgentDownloadUrl',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.GetAgentDownloadUrlResponse(),
            self.call_api(params, req, runtime)
        )

    def get_agent_download_url(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_agent_download_url_with_options(request, runtime)

    def get_alert_rules_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alert_ids):
            query['AlertIds'] = request.alert_ids
        if not UtilClient.is_unset(request.alert_names):
            query['AlertNames'] = request.alert_names
        if not UtilClient.is_unset(request.alert_status):
            query['AlertStatus'] = request.alert_status
        if not UtilClient.is_unset(request.alert_type):
            query['AlertType'] = request.alert_type
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.page):
            query['Page'] = request.page
        if not UtilClient.is_unset(request.product_code):
            query['ProductCode'] = request.product_code
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.size):
            query['Size'] = request.size
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAlertRules',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.GetAlertRulesResponse(),
            self.call_api(params, req, runtime)
        )

    def get_alert_rules(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_alert_rules_with_options(request, runtime)

    def get_app_api_by_page_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.interval_mills):
            query['IntervalMills'] = request.interval_mills
        if not UtilClient.is_unset(request.pid):
            query['PId'] = request.pid
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAppApiByPage',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.GetAppApiByPageResponse(),
            self.call_api(params, req, runtime)
        )

    def get_app_api_by_page(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_app_api_by_page_with_options(request, runtime)

    def get_auth_token_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAuthToken',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.GetAuthTokenResponse(),
            self.call_api(params, req, runtime)
        )

    def get_auth_token(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_auth_token_with_options(request, runtime)

    def get_cloud_cluster_all_url_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetCloudClusterAllUrl',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.GetCloudClusterAllUrlResponse(),
            self.call_api(params, req, runtime)
        )

    def get_cloud_cluster_all_url(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_cloud_cluster_all_url_with_options(request, runtime)

    def get_cluster_all_url_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetClusterAllUrl',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.GetClusterAllUrlResponse(),
            self.call_api(params, req, runtime)
        )

    def get_cluster_all_url(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_cluster_all_url_with_options(request, runtime)

    def get_explore_url_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.expression):
            query['Expression'] = request.expression
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetExploreUrl',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.GetExploreUrlResponse(),
            self.call_api(params, req, runtime)
        )

    def get_explore_url(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_explore_url_with_options(request, runtime)

    def get_integration_state_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.integration):
            query['Integration'] = request.integration
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetIntegrationState',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.GetIntegrationStateResponse(),
            self.call_api(params, req, runtime)
        )

    def get_integration_state(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_integration_state_with_options(request, runtime)

    def get_managed_prometheus_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.cluster_type):
            query['ClusterType'] = request.cluster_type
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetManagedPrometheusStatus',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.GetManagedPrometheusStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def get_managed_prometheus_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_managed_prometheus_status_with_options(request, runtime)

    def get_multiple_trace_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.trace_ids):
            query['TraceIDs'] = request.trace_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetMultipleTrace',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.GetMultipleTraceResponse(),
            self.call_api(params, req, runtime)
        )

    def get_multiple_trace(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_multiple_trace_with_options(request, runtime)

    def get_on_call_schedules_detail_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetOnCallSchedulesDetail',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.GetOnCallSchedulesDetailResponse(),
            self.call_api(params, req, runtime)
        )

    def get_on_call_schedules_detail(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_on_call_schedules_detail_with_options(request, runtime)

    def get_prometheus_api_token_with_options(self, request, runtime):
        """
        The ID of the request.
        

        @param request: GetPrometheusApiTokenRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: GetPrometheusApiTokenResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetPrometheusApiToken',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.GetPrometheusApiTokenResponse(),
            self.call_api(params, req, runtime)
        )

    def get_prometheus_api_token(self, request):
        """
        The ID of the request.
        

        @param request: GetPrometheusApiTokenRequest

        @return: GetPrometheusApiTokenResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_prometheus_api_token_with_options(request, runtime)

    def get_prometheus_global_view_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.global_view_cluster_id):
            query['GlobalViewClusterId'] = request.global_view_cluster_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetPrometheusGlobalView',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.GetPrometheusGlobalViewResponse(),
            self.call_api(params, req, runtime)
        )

    def get_prometheus_global_view(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_prometheus_global_view_with_options(request, runtime)

    def get_prometheus_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetPrometheusInstance',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.GetPrometheusInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    def get_prometheus_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_prometheus_instance_with_options(request, runtime)

    def get_prometheus_integration_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.integration_type):
            query['IntegrationType'] = request.integration_type
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetPrometheusIntegration',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.GetPrometheusIntegrationResponse(),
            self.call_api(params, req, runtime)
        )

    def get_prometheus_integration(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_prometheus_integration_with_options(request, runtime)

    def get_prometheus_monitoring_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.monitoring_name):
            query['MonitoringName'] = request.monitoring_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetPrometheusMonitoring',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.GetPrometheusMonitoringResponse(),
            self.call_api(params, req, runtime)
        )

    def get_prometheus_monitoring(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_prometheus_monitoring_with_options(request, runtime)

    def get_prometheus_remote_write_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.remote_write_name):
            query['RemoteWriteName'] = request.remote_write_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetPrometheusRemoteWrite',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.GetPrometheusRemoteWriteResponse(),
            self.call_api(params, req, runtime)
        )

    def get_prometheus_remote_write(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_prometheus_remote_write_with_options(request, runtime)

    def get_recording_rule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetRecordingRule',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.GetRecordingRuleResponse(),
            self.call_api(params, req, runtime)
        )

    def get_recording_rule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_recording_rule_with_options(request, runtime)

    def get_retcode_app_by_pid_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetRetcodeAppByPid',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.GetRetcodeAppByPidResponse(),
            self.call_api(params, req, runtime)
        )

    def get_retcode_app_by_pid(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_retcode_app_by_pid_with_options(request, runtime)

    def get_retcode_data_by_query_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.from_):
            query['From'] = request.from_
        if not UtilClient.is_unset(request.pid):
            query['Pid'] = request.pid
        if not UtilClient.is_unset(request.query):
            query['Query'] = request.query
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.to):
            query['To'] = request.to
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetRetcodeDataByQuery',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.GetRetcodeDataByQueryResponse(),
            self.call_api(params, req, runtime)
        )

    def get_retcode_data_by_query(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_retcode_data_by_query_with_options(request, runtime)

    def get_retcode_logstore_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.pid):
            query['Pid'] = request.pid
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetRetcodeLogstore',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.GetRetcodeLogstoreResponse(),
            self.call_api(params, req, runtime)
        )

    def get_retcode_logstore(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_retcode_logstore_with_options(request, runtime)

    def get_retcode_share_url_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.pid):
            query['Pid'] = request.pid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetRetcodeShareUrl',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.GetRetcodeShareUrlResponse(),
            self.call_api(params, req, runtime)
        )

    def get_retcode_share_url(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_retcode_share_url_with_options(request, runtime)

    def get_source_map_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ascending_sequence):
            query['AscendingSequence'] = request.ascending_sequence
        if not UtilClient.is_unset(request.edition):
            query['Edition'] = request.edition
        if not UtilClient.is_unset(request.id):
            query['ID'] = request.id
        if not UtilClient.is_unset(request.keyword):
            query['Keyword'] = request.keyword
        if not UtilClient.is_unset(request.order_field):
            query['OrderField'] = request.order_field
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSourceMapInfo',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.GetSourceMapInfoResponse(),
            self.call_api(params, req, runtime)
        )

    def get_source_map_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_source_map_info_with_options(request, runtime)

    def get_stack_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.pid):
            query['Pid'] = request.pid
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.rpc_id):
            query['RpcID'] = request.rpc_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.trace_id):
            query['TraceID'] = request.trace_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetStack',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.GetStackResponse(),
            self.call_api(params, req, runtime)
        )

    def get_stack(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_stack_with_options(request, runtime)

    def get_synthetic_task_detail_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSyntheticTaskDetail',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.GetSyntheticTaskDetailResponse(),
            self.call_api(params, req, runtime)
        )

    def get_synthetic_task_detail(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_synthetic_task_detail_with_options(request, runtime)

    def get_synthetic_task_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.direction):
            query['Direction'] = request.direction
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.task_name):
            query['TaskName'] = request.task_name
        if not UtilClient.is_unset(request.task_status):
            query['TaskStatus'] = request.task_status
        if not UtilClient.is_unset(request.task_type):
            query['TaskType'] = request.task_type
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSyntheticTaskList',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.GetSyntheticTaskListResponse(),
            self.call_api(params, req, runtime)
        )

    def get_synthetic_task_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_synthetic_task_list_with_options(request, runtime)

    def get_synthetic_task_monitors_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetSyntheticTaskMonitors',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.GetSyntheticTaskMonitorsResponse(),
            self.call_api(params, req, runtime)
        )

    def get_synthetic_task_monitors(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_synthetic_task_monitors_with_options(request, runtime)

    def get_trace_with_options(self, request, runtime):
        """
        > You must use Application Real-Time Monitoring Service (ARMS) SDK for Java V2.7.24.
        

        @param request: GetTraceRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: GetTraceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.trace_id):
            query['TraceID'] = request.trace_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetTrace',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.GetTraceResponse(),
            self.call_api(params, req, runtime)
        )

    def get_trace(self, request):
        """
        > You must use Application Real-Time Monitoring Service (ARMS) SDK for Java V2.7.24.
        

        @param request: GetTraceRequest

        @return: GetTraceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_trace_with_options(request, runtime)

    def get_trace_app_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.pid):
            query['Pid'] = request.pid
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetTraceApp',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.GetTraceAppResponse(),
            self.call_api(params, req, runtime)
        )

    def get_trace_app(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_trace_app_with_options(request, runtime)

    def import_app_alert_rules_with_options(self, request, runtime):
        """
        The ID of the region where the associated applications reside.
        

        @param request: ImportAppAlertRulesRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ImportAppAlertRulesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.contact_group_ids):
            query['ContactGroupIds'] = request.contact_group_ids
        if not UtilClient.is_unset(request.is_auto_start):
            query['IsAutoStart'] = request.is_auto_start
        if not UtilClient.is_unset(request.pids):
            query['Pids'] = request.pids
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
        if not UtilClient.is_unset(request.templage_alert_config):
            query['TemplageAlertConfig'] = request.templage_alert_config
        if not UtilClient.is_unset(request.template_alert_id):
            query['TemplateAlertId'] = request.template_alert_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ImportAppAlertRules',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.ImportAppAlertRulesResponse(),
            self.call_api(params, req, runtime)
        )

    def import_app_alert_rules(self, request):
        """
        The ID of the region where the associated applications reside.
        

        @param request: ImportAppAlertRulesRequest

        @return: ImportAppAlertRulesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.import_app_alert_rules_with_options(request, runtime)

    def install_cms_exporter_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.cms_args):
            query['CmsArgs'] = request.cms_args
        if not UtilClient.is_unset(request.direct_args):
            query['DirectArgs'] = request.direct_args
        if not UtilClient.is_unset(request.enable_tag):
            query['EnableTag'] = request.enable_tag
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='InstallCmsExporter',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.InstallCmsExporterResponse(),
            self.call_api(params, req, runtime)
        )

    def install_cms_exporter(self, request):
        runtime = util_models.RuntimeOptions()
        return self.install_cms_exporter_with_options(request, runtime)

    def install_managed_prometheus_with_options(self, request, runtime):
        """
        $.parameters[5].schema.example
        

        @param request: InstallManagedPrometheusRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: InstallManagedPrometheusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.cluster_name):
            query['ClusterName'] = request.cluster_name
        if not UtilClient.is_unset(request.cluster_type):
            query['ClusterType'] = request.cluster_type
        if not UtilClient.is_unset(request.grafana_instance_id):
            query['GrafanaInstanceId'] = request.grafana_instance_id
        if not UtilClient.is_unset(request.kube_config):
            query['KubeConfig'] = request.kube_config
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.security_group_id):
            query['SecurityGroupId'] = request.security_group_id
        if not UtilClient.is_unset(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='InstallManagedPrometheus',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.InstallManagedPrometheusResponse(),
            self.call_api(params, req, runtime)
        )

    def install_managed_prometheus(self, request):
        """
        $.parameters[5].schema.example
        

        @param request: InstallManagedPrometheusRequest

        @return: InstallManagedPrometheusResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.install_managed_prometheus_with_options(request, runtime)

    def list_activated_alerts_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.filter):
            query['Filter'] = request.filter
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListActivatedAlerts',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.ListActivatedAlertsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_activated_alerts(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_activated_alerts_with_options(request, runtime)

    def list_alert_events_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alert_name):
            query['AlertName'] = request.alert_name
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.matching_conditions):
            query['MatchingConditions'] = request.matching_conditions
        if not UtilClient.is_unset(request.page):
            query['Page'] = request.page
        if not UtilClient.is_unset(request.size):
            query['Size'] = request.size
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAlertEvents',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.ListAlertEventsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_alert_events(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_alert_events_with_options(request, runtime)

    def list_alerts_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alert_name):
            query['AlertName'] = request.alert_name
        if not UtilClient.is_unset(request.dispatch_rule_id):
            query['DispatchRuleId'] = request.dispatch_rule_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.integration_type):
            query['IntegrationType'] = request.integration_type
        if not UtilClient.is_unset(request.page):
            query['Page'] = request.page
        if not UtilClient.is_unset(request.severity):
            query['Severity'] = request.severity
        if not UtilClient.is_unset(request.show_activities):
            query['ShowActivities'] = request.show_activities
        if not UtilClient.is_unset(request.show_events):
            query['ShowEvents'] = request.show_events
        if not UtilClient.is_unset(request.size):
            query['Size'] = request.size
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.state):
            query['State'] = request.state
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAlerts',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.ListAlertsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_alerts(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_alerts_with_options(request, runtime)

    def list_cluster_from_grafana_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListClusterFromGrafana',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.ListClusterFromGrafanaResponse(),
            self.call_api(params, req, runtime)
        )

    def list_cluster_from_grafana(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_cluster_from_grafana_with_options(request, runtime)

    def list_cms_instances_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.type_filter):
            query['TypeFilter'] = request.type_filter
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListCmsInstances',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.ListCmsInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_cms_instances(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_cms_instances_with_options(request, runtime)

    def list_dashboards_with_options(self, request, runtime):
        """
        None.
        

        @param request: ListDashboardsRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListDashboardsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.cluster_type):
            query['ClusterType'] = request.cluster_type
        if not UtilClient.is_unset(request.dashboard_name):
            query['DashboardName'] = request.dashboard_name
        if not UtilClient.is_unset(request.language):
            query['Language'] = request.language
        if not UtilClient.is_unset(request.product):
            query['Product'] = request.product
        if not UtilClient.is_unset(request.recreate_switch):
            query['RecreateSwitch'] = request.recreate_switch
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.title):
            query['Title'] = request.title
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDashboards',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.ListDashboardsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_dashboards(self, request):
        """
        None.
        

        @param request: ListDashboardsRequest

        @return: ListDashboardsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_dashboards_with_options(request, runtime)

    def list_dashboards_by_name_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.cluster_type):
            query['ClusterType'] = request.cluster_type
        if not UtilClient.is_unset(request.dash_board_name):
            query['DashBoardName'] = request.dash_board_name
        if not UtilClient.is_unset(request.dash_board_version):
            query['DashBoardVersion'] = request.dash_board_version
        if not UtilClient.is_unset(request.data_source_type):
            query['DataSourceType'] = request.data_source_type
        if not UtilClient.is_unset(request.group_name):
            query['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.only_query):
            query['OnlyQuery'] = request.only_query
        if not UtilClient.is_unset(request.product_code):
            query['ProductCode'] = request.product_code
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDashboardsByName',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.ListDashboardsByNameResponse(),
            self.call_api(params, req, runtime)
        )

    def list_dashboards_by_name(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_dashboards_by_name_with_options(request, runtime)

    def list_dispatch_rule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.system):
            query['System'] = request.system
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDispatchRule',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.ListDispatchRuleResponse(),
            self.call_api(params, req, runtime)
        )

    def list_dispatch_rule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_dispatch_rule_with_options(request, runtime)

    def list_escalation_policies_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListEscalationPolicies',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.ListEscalationPoliciesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_escalation_policies(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_escalation_policies_with_options(request, runtime)

    def list_event_bridge_integrations_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListEventBridgeIntegrations',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.ListEventBridgeIntegrationsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_event_bridge_integrations(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_event_bridge_integrations_with_options(request, runtime)

    def list_insights_events_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.insights_types):
            query['InsightsTypes'] = request.insights_types
        if not UtilClient.is_unset(request.pid):
            query['Pid'] = request.pid
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListInsightsEvents',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.ListInsightsEventsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_insights_events(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_insights_events_with_options(request, runtime)

    def list_integration_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListIntegration',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.ListIntegrationResponse(),
            self.call_api(params, req, runtime)
        )

    def list_integration(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_integration_with_options(request, runtime)

    def list_notification_policies_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ids):
            query['Ids'] = request.ids
        if not UtilClient.is_unset(request.is_detail):
            query['IsDetail'] = request.is_detail
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.page):
            query['Page'] = request.page
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.size):
            query['Size'] = request.size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListNotificationPolicies',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.ListNotificationPoliciesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_notification_policies(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_notification_policies_with_options(request, runtime)

    def list_on_call_schedules_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListOnCallSchedules',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.ListOnCallSchedulesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_on_call_schedules(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_on_call_schedules_with_options(request, runtime)

    def list_prometheus_alert_rules_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.match_expressions):
            query['MatchExpressions'] = request.match_expressions
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPrometheusAlertRules',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.ListPrometheusAlertRulesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_prometheus_alert_rules(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_prometheus_alert_rules_with_options(request, runtime)

    def list_prometheus_alert_templates_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPrometheusAlertTemplates',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.ListPrometheusAlertTemplatesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_prometheus_alert_templates(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_prometheus_alert_templates_with_options(request, runtime)

    def list_prometheus_global_view_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPrometheusGlobalView',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.ListPrometheusGlobalViewResponse(),
            self.call_api(params, req, runtime)
        )

    def list_prometheus_global_view(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_prometheus_global_view_with_options(request, runtime)

    def list_prometheus_instance_by_tag_and_resource_group_id_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPrometheusInstanceByTagAndResourceGroupId',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.ListPrometheusInstanceByTagAndResourceGroupIdResponse(),
            self.call_api(params, req, runtime)
        )

    def list_prometheus_instance_by_tag_and_resource_group_id(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_prometheus_instance_by_tag_and_resource_group_id_with_options(request, runtime)

    def list_prometheus_instances_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_type):
            query['ClusterType'] = request.cluster_type
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.show_global_view):
            query['ShowGlobalView'] = request.show_global_view
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPrometheusInstances',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.ListPrometheusInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_prometheus_instances(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_prometheus_instances_with_options(request, runtime)

    def list_prometheus_integration_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.integration_type):
            query['IntegrationType'] = request.integration_type
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPrometheusIntegration',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.ListPrometheusIntegrationResponse(),
            self.call_api(params, req, runtime)
        )

    def list_prometheus_integration(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_prometheus_integration_with_options(request, runtime)

    def list_prometheus_monitoring_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPrometheusMonitoring',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.ListPrometheusMonitoringResponse(),
            self.call_api(params, req, runtime)
        )

    def list_prometheus_monitoring(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_prometheus_monitoring_with_options(request, runtime)

    def list_prometheus_remote_writes_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPrometheusRemoteWrites',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.ListPrometheusRemoteWritesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_prometheus_remote_writes(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_prometheus_remote_writes_with_options(request, runtime)

    def list_retcode_apps_with_options(self, request, runtime):
        """
        ***\
        

        @param request: ListRetcodeAppsRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListRetcodeAppsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListRetcodeApps',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.ListRetcodeAppsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_retcode_apps(self, request):
        """
        ***\
        

        @param request: ListRetcodeAppsRequest

        @return: ListRetcodeAppsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_retcode_apps_with_options(request, runtime)

    def list_scenario_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.scenario):
            query['Scenario'] = request.scenario
        if not UtilClient.is_unset(request.sign):
            query['Sign'] = request.sign
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListScenario',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.ListScenarioResponse(),
            self.call_api(params, req, runtime)
        )

    def list_scenario(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_scenario_with_options(request, runtime)

    def list_silence_policies_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.is_detail):
            query['IsDetail'] = request.is_detail
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.page):
            query['Page'] = request.page
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.size):
            query['Size'] = request.size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSilencePolicies',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.ListSilencePoliciesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_silence_policies(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_silence_policies_with_options(request, runtime)

    def list_trace_apps_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTraceApps',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.ListTraceAppsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_trace_apps(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_trace_apps_with_options(request, runtime)

    def manage_get_recording_rule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.query_user_id):
            query['QueryUserId'] = request.query_user_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ManageGetRecordingRule',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.ManageGetRecordingRuleResponse(),
            self.call_api(params, req, runtime)
        )

    def manage_get_recording_rule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.manage_get_recording_rule_with_options(request, runtime)

    def manage_recording_rule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.query_user_id):
            query['QueryUserId'] = request.query_user_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.rule_yaml):
            query['RuleYaml'] = request.rule_yaml
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ManageRecordingRule',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.ManageRecordingRuleResponse(),
            self.call_api(params, req, runtime)
        )

    def manage_recording_rule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.manage_recording_rule_with_options(request, runtime)

    def open_arms_default_slrwith_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='OpenArmsDefaultSLR',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.OpenArmsDefaultSLRResponse(),
            self.call_api(params, req, runtime)
        )

    def open_arms_default_slr(self, request):
        runtime = util_models.RuntimeOptions()
        return self.open_arms_default_slrwith_options(request, runtime)

    def open_arms_service_second_version_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='OpenArmsServiceSecondVersion',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.OpenArmsServiceSecondVersionResponse(),
            self.call_api(params, req, runtime)
        )

    def open_arms_service_second_version(self, request):
        runtime = util_models.RuntimeOptions()
        return self.open_arms_service_second_version_with_options(request, runtime)

    def open_vcluster_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_type):
            query['ClusterType'] = request.cluster_type
        if not UtilClient.is_unset(request.length):
            query['Length'] = request.length
        if not UtilClient.is_unset(request.product):
            query['Product'] = request.product
        if not UtilClient.is_unset(request.recreate_switch):
            query['RecreateSwitch'] = request.recreate_switch
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='OpenVCluster',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.OpenVClusterResponse(),
            self.call_api(params, req, runtime)
        )

    def open_vcluster(self, request):
        runtime = util_models.RuntimeOptions()
        return self.open_vcluster_with_options(request, runtime)

    def open_xtrace_default_slrwith_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='OpenXtraceDefaultSLR',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.OpenXtraceDefaultSLRResponse(),
            self.call_api(params, req, runtime)
        )

    def open_xtrace_default_slr(self, request):
        runtime = util_models.RuntimeOptions()
        return self.open_xtrace_default_slrwith_options(request, runtime)

    def query_metric_by_page_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.custom_filters):
            query['CustomFilters'] = request.custom_filters
        if not UtilClient.is_unset(request.dimensions):
            query['Dimensions'] = request.dimensions
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.filters):
            query['Filters'] = request.filters
        if not UtilClient.is_unset(request.interval_in_sec):
            query['IntervalInSec'] = request.interval_in_sec
        if not UtilClient.is_unset(request.measures):
            query['Measures'] = request.measures
        if not UtilClient.is_unset(request.metric):
            query['Metric'] = request.metric
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.order_by):
            query['OrderBy'] = request.order_by
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryMetricByPage',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.QueryMetricByPageResponse(),
            self.call_api(params, req, runtime)
        )

    def query_metric_by_page(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_metric_by_page_with_options(request, runtime)

    def query_prom_install_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryPromInstallStatus',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.QueryPromInstallStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def query_prom_install_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_prom_install_status_with_options(request, runtime)

    def query_release_metric_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.change_order_id):
            query['ChangeOrderId'] = request.change_order_id
        if not UtilClient.is_unset(request.create_time):
            query['CreateTime'] = request.create_time
        if not UtilClient.is_unset(request.metric_type):
            query['MetricType'] = request.metric_type
        if not UtilClient.is_unset(request.pid):
            query['Pid'] = request.pid
        if not UtilClient.is_unset(request.proxy_user_id):
            query['ProxyUserId'] = request.proxy_user_id
        if not UtilClient.is_unset(request.release_end_time):
            query['ReleaseEndTime'] = request.release_end_time
        if not UtilClient.is_unset(request.release_start_time):
            query['ReleaseStartTime'] = request.release_start_time
        if not UtilClient.is_unset(request.service):
            query['Service'] = request.service
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryReleaseMetric',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.QueryReleaseMetricResponse(),
            self.call_api(params, req, runtime)
        )

    def query_release_metric(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_release_metric_with_options(request, runtime)

    def remove_ali_cluster_ids_from_prometheus_global_view_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_ids):
            query['ClusterIds'] = request.cluster_ids
        if not UtilClient.is_unset(request.global_view_cluster_id):
            query['GlobalViewClusterId'] = request.global_view_cluster_id
        if not UtilClient.is_unset(request.group_name):
            query['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemoveAliClusterIdsFromPrometheusGlobalView',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.RemoveAliClusterIdsFromPrometheusGlobalViewResponse(),
            self.call_api(params, req, runtime)
        )

    def remove_ali_cluster_ids_from_prometheus_global_view(self, request):
        runtime = util_models.RuntimeOptions()
        return self.remove_ali_cluster_ids_from_prometheus_global_view_with_options(request, runtime)

    def remove_sources_from_prometheus_global_view_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.global_view_cluster_id):
            query['GlobalViewClusterId'] = request.global_view_cluster_id
        if not UtilClient.is_unset(request.group_name):
            query['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.source_names):
            query['SourceNames'] = request.source_names
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemoveSourcesFromPrometheusGlobalView',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.RemoveSourcesFromPrometheusGlobalViewResponse(),
            self.call_api(params, req, runtime)
        )

    def remove_sources_from_prometheus_global_view(self, request):
        runtime = util_models.RuntimeOptions()
        return self.remove_sources_from_prometheus_global_view_with_options(request, runtime)

    def save_trace_app_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.pid):
            query['Pid'] = request.pid
        if not UtilClient.is_unset(request.settings):
            query['Settings'] = request.settings
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SaveTraceAppConfig',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.SaveTraceAppConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def save_trace_app_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.save_trace_app_config_with_options(request, runtime)

    def search_alert_contact_with_options(self, request, runtime):
        """
        The ID of the resource group.
        

        @param request: SearchAlertContactRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: SearchAlertContactResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.contact_ids):
            query['ContactIds'] = request.contact_ids
        if not UtilClient.is_unset(request.contact_name):
            query['ContactName'] = request.contact_name
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.email):
            query['Email'] = request.email
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.phone):
            query['Phone'] = request.phone
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SearchAlertContact',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.SearchAlertContactResponse(),
            self.call_api(params, req, runtime)
        )

    def search_alert_contact(self, request):
        """
        The ID of the resource group.
        

        @param request: SearchAlertContactRequest

        @return: SearchAlertContactResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.search_alert_contact_with_options(request, runtime)

    def search_alert_contact_group_with_options(self, request, runtime):
        """
        The mobile number of the alert contact.
        

        @param request: SearchAlertContactGroupRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: SearchAlertContactGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.contact_group_ids):
            query['ContactGroupIds'] = request.contact_group_ids
        if not UtilClient.is_unset(request.contact_group_name):
            query['ContactGroupName'] = request.contact_group_name
        if not UtilClient.is_unset(request.contact_id):
            query['ContactId'] = request.contact_id
        if not UtilClient.is_unset(request.contact_name):
            query['ContactName'] = request.contact_name
        if not UtilClient.is_unset(request.is_detail):
            query['IsDetail'] = request.is_detail
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SearchAlertContactGroup',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.SearchAlertContactGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def search_alert_contact_group(self, request):
        """
        The mobile number of the alert contact.
        

        @param request: SearchAlertContactGroupRequest

        @return: SearchAlertContactGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.search_alert_contact_group_with_options(request, runtime)

    def search_alert_histories_with_options(self, request, runtime):
        """
        This operation is no longer maintained. To query alert records, call the ListAlerts operation provided by the new version of Alert Management.
        

        @param request: SearchAlertHistoriesRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: SearchAlertHistoriesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alert_id):
            query['AlertId'] = request.alert_id
        if not UtilClient.is_unset(request.alert_type):
            query['AlertType'] = request.alert_type
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SearchAlertHistories',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.SearchAlertHistoriesResponse(),
            self.call_api(params, req, runtime)
        )

    def search_alert_histories(self, request):
        """
        This operation is no longer maintained. To query alert records, call the ListAlerts operation provided by the new version of Alert Management.
        

        @param request: SearchAlertHistoriesRequest

        @return: SearchAlertHistoriesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.search_alert_histories_with_options(request, runtime)

    def search_alert_rules_with_options(self, request, runtime):
        """
        The current operation is no longer maintained. You can call the GetAlertRules operation of Alert Management (New) to query existing alert rules.
        

        @param request: SearchAlertRulesRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: SearchAlertRulesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alert_rule_id):
            query['AlertRuleId'] = request.alert_rule_id
        if not UtilClient.is_unset(request.app_type):
            query['AppType'] = request.app_type
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.pid):
            query['Pid'] = request.pid
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.system_region_id):
            query['SystemRegionId'] = request.system_region_id
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
        if not UtilClient.is_unset(request.title):
            query['Title'] = request.title
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SearchAlertRules',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.SearchAlertRulesResponse(),
            self.call_api(params, req, runtime)
        )

    def search_alert_rules(self, request):
        """
        The current operation is no longer maintained. You can call the GetAlertRules operation of Alert Management (New) to query existing alert rules.
        

        @param request: SearchAlertRulesRequest

        @return: SearchAlertRulesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.search_alert_rules_with_options(request, runtime)

    def search_events_with_options(self, request, runtime):
        """
        The operation that you want to perform. Set the value to `SearchEvents`.
        

        @param request: SearchEventsRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: SearchEventsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alert_id):
            query['AlertId'] = request.alert_id
        if not UtilClient.is_unset(request.alert_type):
            query['AlertType'] = request.alert_type
        if not UtilClient.is_unset(request.app_type):
            query['AppType'] = request.app_type
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.is_trigger):
            query['IsTrigger'] = request.is_trigger
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.pid):
            query['Pid'] = request.pid
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SearchEvents',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.SearchEventsResponse(),
            self.call_api(params, req, runtime)
        )

    def search_events(self, request):
        """
        The operation that you want to perform. Set the value to `SearchEvents`.
        

        @param request: SearchEventsRequest

        @return: SearchEventsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.search_events_with_options(request, runtime)

    def search_retcode_app_by_page_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.retcode_app_id):
            query['RetcodeAppId'] = request.retcode_app_id
        if not UtilClient.is_unset(request.retcode_app_name):
            query['RetcodeAppName'] = request.retcode_app_name
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SearchRetcodeAppByPage',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.SearchRetcodeAppByPageResponse(),
            self.call_api(params, req, runtime)
        )

    def search_retcode_app_by_page(self, request):
        runtime = util_models.RuntimeOptions()
        return self.search_retcode_app_by_page_with_options(request, runtime)

    def search_trace_app_by_name_with_options(self, request, runtime):
        """
        **\
        

        @param request: SearchTraceAppByNameRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: SearchTraceAppByNameResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
        if not UtilClient.is_unset(request.trace_app_name):
            query['TraceAppName'] = request.trace_app_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SearchTraceAppByName',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.SearchTraceAppByNameResponse(),
            self.call_api(params, req, runtime)
        )

    def search_trace_app_by_name(self, request):
        """
        **\
        

        @param request: SearchTraceAppByNameRequest

        @return: SearchTraceAppByNameResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.search_trace_app_by_name_with_options(request, runtime)

    def search_trace_app_by_page_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
        if not UtilClient.is_unset(request.trace_app_name):
            query['TraceAppName'] = request.trace_app_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SearchTraceAppByPage',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.SearchTraceAppByPageResponse(),
            self.call_api(params, req, runtime)
        )

    def search_trace_app_by_page(self, request):
        runtime = util_models.RuntimeOptions()
        return self.search_trace_app_by_page_with_options(request, runtime)

    def search_traces_with_options(self, request, runtime):
        """
        > A maximum of 100 data entries can be returned each time this operation is called. If you want to query all existing traces, we recommend that you call the SearchTracesByPage operation. For more information, see [SearchTracesByPage](~~175866~~).
        

        @param request: SearchTracesRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: SearchTracesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.exclusion_filters):
            query['ExclusionFilters'] = request.exclusion_filters
        if not UtilClient.is_unset(request.min_duration):
            query['MinDuration'] = request.min_duration
        if not UtilClient.is_unset(request.operation_name):
            query['OperationName'] = request.operation_name
        if not UtilClient.is_unset(request.pid):
            query['Pid'] = request.pid
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.reverse):
            query['Reverse'] = request.reverse
        if not UtilClient.is_unset(request.service_ip):
            query['ServiceIp'] = request.service_ip
        if not UtilClient.is_unset(request.service_name):
            query['ServiceName'] = request.service_name
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SearchTraces',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.SearchTracesResponse(),
            self.call_api(params, req, runtime)
        )

    def search_traces(self, request):
        """
        > A maximum of 100 data entries can be returned each time this operation is called. If you want to query all existing traces, we recommend that you call the SearchTracesByPage operation. For more information, see [SearchTracesByPage](~~175866~~).
        

        @param request: SearchTracesRequest

        @return: SearchTracesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.search_traces_with_options(request, runtime)

    def search_traces_by_page_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.exclusion_filters):
            query['ExclusionFilters'] = request.exclusion_filters
        if not UtilClient.is_unset(request.is_error):
            query['IsError'] = request.is_error
        if not UtilClient.is_unset(request.min_duration):
            query['MinDuration'] = request.min_duration
        if not UtilClient.is_unset(request.operation_name):
            query['OperationName'] = request.operation_name
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.pid):
            query['Pid'] = request.pid
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.reverse):
            query['Reverse'] = request.reverse
        if not UtilClient.is_unset(request.service_ip):
            query['ServiceIp'] = request.service_ip
        if not UtilClient.is_unset(request.service_name):
            query['ServiceName'] = request.service_name
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SearchTracesByPage',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.SearchTracesByPageResponse(),
            self.call_api(params, req, runtime)
        )

    def search_traces_by_page(self, request):
        runtime = util_models.RuntimeOptions()
        return self.search_traces_by_page_with_options(request, runtime)

    def send_ttsverify_link_with_options(self, request, runtime):
        """
        After you receive the text message, verify the mobile number as prompted. Before you can specify a mobile phone number in a notification policy, you must verify the mobile phone number.
        

        @param request: SendTTSVerifyLinkRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: SendTTSVerifyLinkResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.contact_id):
            body['ContactId'] = request.contact_id
        if not UtilClient.is_unset(request.phone):
            body['Phone'] = request.phone
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SendTTSVerifyLink',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.SendTTSVerifyLinkResponse(),
            self.call_api(params, req, runtime)
        )

    def send_ttsverify_link(self, request):
        """
        After you receive the text message, verify the mobile number as prompted. Before you can specify a mobile phone number in a notification policy, you must verify the mobile phone number.
        

        @param request: SendTTSVerifyLinkRequest

        @return: SendTTSVerifyLinkResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.send_ttsverify_link_with_options(request, runtime)

    def set_retcode_share_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_name):
            query['AppName'] = request.app_name
        if not UtilClient.is_unset(request.pid):
            query['Pid'] = request.pid
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetRetcodeShareStatus',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.SetRetcodeShareStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def set_retcode_share_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_retcode_share_status_with_options(request, runtime)

    def start_alert_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alert_id):
            query['AlertId'] = request.alert_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartAlert',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.StartAlertResponse(),
            self.call_api(params, req, runtime)
        )

    def start_alert(self, request):
        runtime = util_models.RuntimeOptions()
        return self.start_alert_with_options(request, runtime)

    def stop_alert_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alert_id):
            query['AlertId'] = request.alert_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopAlert',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.StopAlertResponse(),
            self.call_api(params, req, runtime)
        )

    def stop_alert(self, request):
        runtime = util_models.RuntimeOptions()
        return self.stop_alert_with_options(request, runtime)

    def switch_synthetic_task_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.switch_status):
            query['SwitchStatus'] = request.switch_status
        if not UtilClient.is_unset(request.task_ids):
            query['TaskIds'] = request.task_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SwitchSyntheticTaskStatus',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.SwitchSyntheticTaskStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def switch_synthetic_task_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.switch_synthetic_task_status_with_options(request, runtime)

    def sync_recording_rules_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.target_clusters):
            query['TargetClusters'] = request.target_clusters
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SyncRecordingRules',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.SyncRecordingRulesResponse(),
            self.call_api(params, req, runtime)
        )

    def sync_recording_rules(self, request):
        runtime = util_models.RuntimeOptions()
        return self.sync_recording_rules_with_options(request, runtime)

    def tag_resources_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TagResources',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.TagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    def tag_resources(self, request):
        runtime = util_models.RuntimeOptions()
        return self.tag_resources_with_options(request, runtime)

    def uninstall_managed_prometheus_with_options(self, request, runtime):
        """
        The status code. The status code 200 indicates that the request was successful. If another status code is returned, the request failed.
        

        @param request: UninstallManagedPrometheusRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: UninstallManagedPrometheusResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.cluster_type):
            query['ClusterType'] = request.cluster_type
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UninstallManagedPrometheus',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.UninstallManagedPrometheusResponse(),
            self.call_api(params, req, runtime)
        )

    def uninstall_managed_prometheus(self, request):
        """
        The status code. The status code 200 indicates that the request was successful. If another status code is returned, the request failed.
        

        @param request: UninstallManagedPrometheusRequest

        @return: UninstallManagedPrometheusResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.uninstall_managed_prometheus_with_options(request, runtime)

    def uninstall_prom_cluster_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UninstallPromCluster',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.UninstallPromClusterResponse(),
            self.call_api(params, req, runtime)
        )

    def uninstall_prom_cluster(self, request):
        runtime = util_models.RuntimeOptions()
        return self.uninstall_prom_cluster_with_options(request, runtime)

    def untag_resources_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.all):
            query['All'] = request.all
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag_key):
            query['TagKey'] = request.tag_key
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UntagResources',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.UntagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    def untag_resources(self, request):
        runtime = util_models.RuntimeOptions()
        return self.untag_resources_with_options(request, runtime)

    def update_alert_contact_with_options(self, request, runtime):
        """
        The ID of the request.
        

        @param request: UpdateAlertContactRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: UpdateAlertContactResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.contact_id):
            query['ContactId'] = request.contact_id
        if not UtilClient.is_unset(request.contact_name):
            query['ContactName'] = request.contact_name
        if not UtilClient.is_unset(request.ding_robot_webhook_url):
            query['DingRobotWebhookUrl'] = request.ding_robot_webhook_url
        if not UtilClient.is_unset(request.email):
            query['Email'] = request.email
        if not UtilClient.is_unset(request.phone_num):
            query['PhoneNum'] = request.phone_num
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.system_noc):
            query['SystemNoc'] = request.system_noc
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateAlertContact',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.UpdateAlertContactResponse(),
            self.call_api(params, req, runtime)
        )

    def update_alert_contact(self, request):
        """
        The ID of the request.
        

        @param request: UpdateAlertContactRequest

        @return: UpdateAlertContactResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_alert_contact_with_options(request, runtime)

    def update_alert_contact_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.contact_group_id):
            query['ContactGroupId'] = request.contact_group_id
        if not UtilClient.is_unset(request.contact_group_name):
            query['ContactGroupName'] = request.contact_group_name
        if not UtilClient.is_unset(request.contact_ids):
            query['ContactIds'] = request.contact_ids
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateAlertContactGroup',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.UpdateAlertContactGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def update_alert_contact_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_alert_contact_group_with_options(request, runtime)

    def update_alert_rule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alert_id):
            query['AlertId'] = request.alert_id
        if not UtilClient.is_unset(request.contact_group_ids):
            query['ContactGroupIds'] = request.contact_group_ids
        if not UtilClient.is_unset(request.is_auto_start):
            query['IsAutoStart'] = request.is_auto_start
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.templage_alert_config):
            query['TemplageAlertConfig'] = request.templage_alert_config
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateAlertRule',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.UpdateAlertRuleResponse(),
            self.call_api(params, req, runtime)
        )

    def update_alert_rule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_alert_rule_with_options(request, runtime)

    def update_dispatch_rule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dispatch_rule):
            query['DispatchRule'] = request.dispatch_rule
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateDispatchRule',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.UpdateDispatchRuleResponse(),
            self.call_api(params, req, runtime)
        )

    def update_dispatch_rule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_dispatch_rule_with_options(request, runtime)

    def update_integration_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.auto_recover):
            body['AutoRecover'] = request.auto_recover
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.duplicate_key):
            body['DuplicateKey'] = request.duplicate_key
        if not UtilClient.is_unset(request.extended_field_redefine_rules):
            body['ExtendedFieldRedefineRules'] = request.extended_field_redefine_rules
        if not UtilClient.is_unset(request.field_redefine_rules):
            body['FieldRedefineRules'] = request.field_redefine_rules
        if not UtilClient.is_unset(request.initiative_recover_field):
            body['InitiativeRecoverField'] = request.initiative_recover_field
        if not UtilClient.is_unset(request.initiative_recover_value):
            body['InitiativeRecoverValue'] = request.initiative_recover_value
        if not UtilClient.is_unset(request.integration_id):
            body['IntegrationId'] = request.integration_id
        if not UtilClient.is_unset(request.integration_name):
            body['IntegrationName'] = request.integration_name
        if not UtilClient.is_unset(request.integration_product_type):
            body['IntegrationProductType'] = request.integration_product_type
        if not UtilClient.is_unset(request.liveness):
            body['Liveness'] = request.liveness
        if not UtilClient.is_unset(request.recover_time):
            body['RecoverTime'] = request.recover_time
        if not UtilClient.is_unset(request.stat):
            body['Stat'] = request.stat
        if not UtilClient.is_unset(request.state):
            body['State'] = request.state
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateIntegration',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.UpdateIntegrationResponse(),
            self.call_api(params, req, runtime)
        )

    def update_integration(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_integration_with_options(request, runtime)

    def update_prometheus_alert_rule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alert_id):
            query['AlertId'] = request.alert_id
        if not UtilClient.is_unset(request.alert_name):
            query['AlertName'] = request.alert_name
        if not UtilClient.is_unset(request.annotations):
            query['Annotations'] = request.annotations
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.dispatch_rule_id):
            query['DispatchRuleId'] = request.dispatch_rule_id
        if not UtilClient.is_unset(request.duration):
            query['Duration'] = request.duration
        if not UtilClient.is_unset(request.expression):
            query['Expression'] = request.expression
        if not UtilClient.is_unset(request.labels):
            query['Labels'] = request.labels
        if not UtilClient.is_unset(request.message):
            query['Message'] = request.message
        if not UtilClient.is_unset(request.notify_type):
            query['NotifyType'] = request.notify_type
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdatePrometheusAlertRule',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.UpdatePrometheusAlertRuleResponse(),
            self.call_api(params, req, runtime)
        )

    def update_prometheus_alert_rule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_prometheus_alert_rule_with_options(request, runtime)

    def update_prometheus_global_view_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.all_sub_clusters_success):
            query['AllSubClustersSuccess'] = request.all_sub_clusters_success
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.sub_clusters_json):
            query['SubClustersJson'] = request.sub_clusters_json
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdatePrometheusGlobalView',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.UpdatePrometheusGlobalViewResponse(),
            self.call_api(params, req, runtime)
        )

    def update_prometheus_global_view(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_prometheus_global_view_with_options(request, runtime)

    def update_prometheus_integration_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.integration_type):
            query['IntegrationType'] = request.integration_type
        if not UtilClient.is_unset(request.param):
            query['Param'] = request.param
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdatePrometheusIntegration',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.UpdatePrometheusIntegrationResponse(),
            self.call_api(params, req, runtime)
        )

    def update_prometheus_integration(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_prometheus_integration_with_options(request, runtime)

    def update_prometheus_monitoring_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.monitoring_name):
            query['MonitoringName'] = request.monitoring_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        body = {}
        if not UtilClient.is_unset(request.config_yaml):
            body['ConfigYaml'] = request.config_yaml
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdatePrometheusMonitoring',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.UpdatePrometheusMonitoringResponse(),
            self.call_api(params, req, runtime)
        )

    def update_prometheus_monitoring(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_prometheus_monitoring_with_options(request, runtime)

    def update_prometheus_monitoring_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.monitoring_name):
            query['MonitoringName'] = request.monitoring_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdatePrometheusMonitoringStatus',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.UpdatePrometheusMonitoringStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def update_prometheus_monitoring_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_prometheus_monitoring_status_with_options(request, runtime)

    def update_prometheus_remote_write_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.remote_write_name):
            query['RemoteWriteName'] = request.remote_write_name
        body = {}
        if not UtilClient.is_unset(request.remote_write_yaml):
            body['RemoteWriteYaml'] = request.remote_write_yaml
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdatePrometheusRemoteWrite',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.UpdatePrometheusRemoteWriteResponse(),
            self.call_api(params, req, runtime)
        )

    def update_prometheus_remote_write(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_prometheus_remote_write_with_options(request, runtime)

    def update_webhook_with_options(self, request, runtime):
        """
        The ID of the request.
        

        @param request: UpdateWebhookRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: UpdateWebhookResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.body):
            query['Body'] = request.body
        if not UtilClient.is_unset(request.contact_id):
            query['ContactId'] = request.contact_id
        if not UtilClient.is_unset(request.contact_name):
            query['ContactName'] = request.contact_name
        if not UtilClient.is_unset(request.http_headers):
            query['HttpHeaders'] = request.http_headers
        if not UtilClient.is_unset(request.http_params):
            query['HttpParams'] = request.http_params
        if not UtilClient.is_unset(request.method):
            query['Method'] = request.method
        if not UtilClient.is_unset(request.recover_body):
            query['RecoverBody'] = request.recover_body
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateWebhook',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.UpdateWebhookResponse(),
            self.call_api(params, req, runtime)
        )

    def update_webhook(self, request):
        """
        The ID of the request.
        

        @param request: UpdateWebhookRequest

        @return: UpdateWebhookResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_webhook_with_options(request, runtime)

    def upload_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.edition):
            query['Edition'] = request.edition
        if not UtilClient.is_unset(request.file_name):
            query['FileName'] = request.file_name
        if not UtilClient.is_unset(request.pid):
            query['Pid'] = request.pid
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.version):
            query['Version'] = request.version
        body = {}
        if not UtilClient.is_unset(request.file):
            body['File'] = request.file
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='Upload',
            version='2019-08-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20190808_models.UploadResponse(),
            self.call_api(params, req, runtime)
        )

    def upload(self, request):
        runtime = util_models.RuntimeOptions()
        return self.upload_with_options(request, runtime)
