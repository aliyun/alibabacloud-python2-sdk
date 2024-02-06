# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_arms20210422 import models as arms20210422_models
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
            version='2021-04-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20210422_models.AddGrafanaResponse(),
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
            version='2021-04-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20210422_models.AddIntegrationResponse(),
            self.call_api(params, req, runtime)
        )

    def add_integration(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_integration_with_options(request, runtime)

    def apply_scenario_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = arms20210422_models.ApplyScenarioShrinkRequest()
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
            version='2021-04-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20210422_models.ApplyScenarioResponse(),
            self.call_api(params, req, runtime)
        )

    def apply_scenario(self, request):
        runtime = util_models.RuntimeOptions()
        return self.apply_scenario_with_options(request, runtime)

    def check_data_consistency_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_type):
            query['AppType'] = request.app_type
        if not UtilClient.is_unset(request.current_timestamp):
            query['CurrentTimestamp'] = request.current_timestamp
        if not UtilClient.is_unset(request.pid):
            query['Pid'] = request.pid
        if not UtilClient.is_unset(request.proxy_user_id):
            query['ProxyUserId'] = request.proxy_user_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CheckDataConsistency',
            version='2021-04-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20210422_models.CheckDataConsistencyResponse(),
            self.call_api(params, req, runtime)
        )

    def check_data_consistency(self, request):
        runtime = util_models.RuntimeOptions()
        return self.check_data_consistency_with_options(request, runtime)

    def check_service_linked_role_for_deleting_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.deletion_task_id):
            query['DeletionTaskId'] = request.deletion_task_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.role_arn):
            query['RoleArn'] = request.role_arn
        if not UtilClient.is_unset(request.spiregion_id):
            query['SPIRegionId'] = request.spiregion_id
        if not UtilClient.is_unset(request.service_name):
            query['ServiceName'] = request.service_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CheckServiceLinkedRoleForDeleting',
            version='2021-04-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20210422_models.CheckServiceLinkedRoleForDeletingResponse(),
            self.call_api(params, req, runtime)
        )

    def check_service_linked_role_for_deleting(self, request):
        runtime = util_models.RuntimeOptions()
        return self.check_service_linked_role_for_deleting_with_options(request, runtime)

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
            version='2021-04-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20210422_models.CheckServiceStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def check_service_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.check_service_status_with_options(request, runtime)

    def config_app_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_ids):
            query['AppIds'] = request.app_ids
        if not UtilClient.is_unset(request.enable):
            query['Enable'] = request.enable
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ConfigApp',
            version='2021-04-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20210422_models.ConfigAppResponse(),
            self.call_api(params, req, runtime)
        )

    def config_app(self, request):
        runtime = util_models.RuntimeOptions()
        return self.config_app_with_options(request, runtime)

    def create_alert_contact_with_options(self, request, runtime):
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
        if not UtilClient.is_unset(request.system_noc):
            query['SystemNoc'] = request.system_noc
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateAlertContact',
            version='2021-04-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20210422_models.CreateAlertContactResponse(),
            self.call_api(params, req, runtime)
        )

    def create_alert_contact(self, request):
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
            version='2021-04-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20210422_models.CreateAlertContactGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def create_alert_contact_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_alert_contact_group_with_options(request, runtime)

    def create_alert_template_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.annotations):
            query['Annotations'] = request.annotations
        if not UtilClient.is_unset(request.labels):
            query['Labels'] = request.labels
        if not UtilClient.is_unset(request.match_expressions):
            query['MatchExpressions'] = request.match_expressions
        if not UtilClient.is_unset(request.message):
            query['Message'] = request.message
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.parent_id):
            query['ParentId'] = request.parent_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.rule):
            query['Rule'] = request.rule
        if not UtilClient.is_unset(request.template_provider):
            query['TemplateProvider'] = request.template_provider
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateAlertTemplate',
            version='2021-04-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20210422_models.CreateAlertTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    def create_alert_template(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_alert_template_with_options(request, runtime)

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
            version='2021-04-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20210422_models.CreateDispatchRuleResponse(),
            self.call_api(params, req, runtime)
        )

    def create_dispatch_rule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_dispatch_rule_with_options(request, runtime)

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
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreatePrometheusAlertRule',
            version='2021-04-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20210422_models.CreatePrometheusAlertRuleResponse(),
            self.call_api(params, req, runtime)
        )

    def create_prometheus_alert_rule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_prometheus_alert_rule_with_options(request, runtime)

    def create_retcode_app_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.retcode_app_name):
            query['RetcodeAppName'] = request.retcode_app_name
        if not UtilClient.is_unset(request.retcode_app_type):
            query['RetcodeAppType'] = request.retcode_app_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateRetcodeApp',
            version='2021-04-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20210422_models.CreateRetcodeAppResponse(),
            self.call_api(params, req, runtime)
        )

    def create_retcode_app(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_retcode_app_with_options(request, runtime)

    def create_wehook_with_options(self, request, runtime):
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
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateWehook',
            version='2021-04-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20210422_models.CreateWehookResponse(),
            self.call_api(params, req, runtime)
        )

    def create_wehook(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_wehook_with_options(request, runtime)

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
            version='2021-04-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20210422_models.DeleteAlertContactResponse(),
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
            version='2021-04-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20210422_models.DeleteAlertContactGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_alert_contact_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_alert_contact_group_with_options(request, runtime)

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
            version='2021-04-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20210422_models.DeleteAlertRulesResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_alert_rules(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_alert_rules_with_options(request, runtime)

    def delete_alert_template_with_options(self, request, runtime):
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
            action='DeleteAlertTemplate',
            version='2021-04-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20210422_models.DeleteAlertTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_alert_template(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_alert_template_with_options(request, runtime)

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
            version='2021-04-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20210422_models.DeleteDispatchRuleResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_dispatch_rule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_dispatch_rule_with_options(request, runtime)

    def delete_grafana_resource_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.cluster_id):
            body['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.cluster_name):
            body['ClusterName'] = request.cluster_name
        if not UtilClient.is_unset(request.user_id):
            body['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteGrafanaResource',
            version='2021-04-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20210422_models.DeleteGrafanaResourceResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_grafana_resource(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_grafana_resource_with_options(request, runtime)

    def delete_prometheus_alert_rule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alert_id):
            query['AlertId'] = request.alert_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeletePrometheusAlertRule',
            version='2021-04-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20210422_models.DeletePrometheusAlertRuleResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_prometheus_alert_rule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_prometheus_alert_rule_with_options(request, runtime)

    def delete_retcode_app_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteRetcodeApp',
            version='2021-04-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20210422_models.DeleteRetcodeAppResponse(),
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
            version='2021-04-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20210422_models.DeleteScenarioResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_scenario(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_scenario_with_options(request, runtime)

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
            version='2021-04-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20210422_models.DeleteTraceAppResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_trace_app(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_trace_app_with_options(request, runtime)

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
            version='2021-04-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20210422_models.DescribeDispatchRuleResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_dispatch_rule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_dispatch_rule_with_options(request, runtime)

    def describe_prometheus_alert_rule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alert_id):
            query['AlertId'] = request.alert_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePrometheusAlertRule',
            version='2021-04-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20210422_models.DescribePrometheusAlertRuleResponse(),
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
            version='2021-04-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20210422_models.DescribeTraceLicenseKeyResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_trace_license_key(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_trace_license_key_with_options(request, runtime)

    def describe_trace_location_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeTraceLocation',
            version='2021-04-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20210422_models.DescribeTraceLocationResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_trace_location(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_trace_location_with_options(request, runtime)

    def disable_alert_template_with_options(self, request, runtime):
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
            action='DisableAlertTemplate',
            version='2021-04-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20210422_models.DisableAlertTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    def disable_alert_template(self, request):
        runtime = util_models.RuntimeOptions()
        return self.disable_alert_template_with_options(request, runtime)

    def enable_alert_template_with_options(self, request, runtime):
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
            action='EnableAlertTemplate',
            version='2021-04-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20210422_models.EnableAlertTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    def enable_alert_template(self, request):
        runtime = util_models.RuntimeOptions()
        return self.enable_alert_template_with_options(request, runtime)

    def export_prometheus_rules_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.name_space):
            query['NameSpace'] = request.name_space
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ExportPrometheusRules',
            version='2021-04-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20210422_models.ExportPrometheusRulesResponse(),
            self.call_api(params, req, runtime)
        )

    def export_prometheus_rules(self, request):
        runtime = util_models.RuntimeOptions()
        return self.export_prometheus_rules_with_options(request, runtime)

    def get_agent_download_url_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAgentDownloadUrl',
            version='2021-04-22',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20210422_models.GetAgentDownloadUrlResponse(),
            self.call_api(params, req, runtime)
        )

    def get_agent_download_url(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_agent_download_url_with_options(request, runtime)

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
            version='2021-04-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20210422_models.GetAppApiByPageResponse(),
            self.call_api(params, req, runtime)
        )

    def get_app_api_by_page(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_app_api_by_page_with_options(request, runtime)

    def get_consistency_snapshot_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_type):
            query['AppType'] = request.app_type
        if not UtilClient.is_unset(request.current_timestamp):
            query['CurrentTimestamp'] = request.current_timestamp
        if not UtilClient.is_unset(request.pid):
            query['Pid'] = request.pid
        if not UtilClient.is_unset(request.proxy_user_id):
            query['ProxyUserId'] = request.proxy_user_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetConsistencySnapshot',
            version='2021-04-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20210422_models.GetConsistencySnapshotResponse(),
            self.call_api(params, req, runtime)
        )

    def get_consistency_snapshot(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_consistency_snapshot_with_options(request, runtime)

    def get_integration_token_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.product_type):
            query['ProductType'] = request.product_type
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetIntegrationToken',
            version='2021-04-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20210422_models.GetIntegrationTokenResponse(),
            self.call_api(params, req, runtime)
        )

    def get_integration_token(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_integration_token_with_options(request, runtime)

    def get_multiple_trace_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.trace_ids):
            query['TraceIDs'] = request.trace_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetMultipleTrace',
            version='2021-04-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20210422_models.GetMultipleTraceResponse(),
            self.call_api(params, req, runtime)
        )

    def get_multiple_trace(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_multiple_trace_with_options(request, runtime)

    def get_prometheus_api_token_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetPrometheusApiToken',
            version='2021-04-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20210422_models.GetPrometheusApiTokenResponse(),
            self.call_api(params, req, runtime)
        )

    def get_prometheus_api_token(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_prometheus_api_token_with_options(request, runtime)

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
            version='2021-04-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20210422_models.GetRetcodeShareUrlResponse(),
            self.call_api(params, req, runtime)
        )

    def get_retcode_share_url(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_retcode_share_url_with_options(request, runtime)

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
            version='2021-04-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20210422_models.GetStackResponse(),
            self.call_api(params, req, runtime)
        )

    def get_stack(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_stack_with_options(request, runtime)

    def get_trace_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.trace_id):
            query['TraceID'] = request.trace_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetTrace',
            version='2021-04-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20210422_models.GetTraceResponse(),
            self.call_api(params, req, runtime)
        )

    def get_trace(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_trace_with_options(request, runtime)

    def get_trace_app_with_options(self, request, runtime):
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
            action='GetTraceApp',
            version='2021-04-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20210422_models.GetTraceAppResponse(),
            self.call_api(params, req, runtime)
        )

    def get_trace_app(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_trace_app_with_options(request, runtime)

    def import_app_alert_rules_with_options(self, request, runtime):
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
        if not UtilClient.is_unset(request.templage_alert_config):
            query['TemplageAlertConfig'] = request.templage_alert_config
        if not UtilClient.is_unset(request.template_alert_id):
            query['TemplateAlertId'] = request.template_alert_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ImportAppAlertRules',
            version='2021-04-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20210422_models.ImportAppAlertRulesResponse(),
            self.call_api(params, req, runtime)
        )

    def import_app_alert_rules(self, request):
        runtime = util_models.RuntimeOptions()
        return self.import_app_alert_rules_with_options(request, runtime)

    def import_custom_alert_rules_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.contact_group_ids):
            query['ContactGroupIds'] = request.contact_group_ids
        if not UtilClient.is_unset(request.is_auto_start):
            query['IsAutoStart'] = request.is_auto_start
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.templage_alert_config):
            query['TemplageAlertConfig'] = request.templage_alert_config
        if not UtilClient.is_unset(request.template_alert_config):
            query['TemplateAlertConfig'] = request.template_alert_config
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ImportCustomAlertRules',
            version='2021-04-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20210422_models.ImportCustomAlertRulesResponse(),
            self.call_api(params, req, runtime)
        )

    def import_custom_alert_rules(self, request):
        runtime = util_models.RuntimeOptions()
        return self.import_custom_alert_rules_with_options(request, runtime)

    def import_prometheus_rules_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.content):
            query['Content'] = request.content
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.name_space):
            query['NameSpace'] = request.name_space
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ImportPrometheusRules',
            version='2021-04-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20210422_models.ImportPrometheusRulesResponse(),
            self.call_api(params, req, runtime)
        )

    def import_prometheus_rules(self, request):
        runtime = util_models.RuntimeOptions()
        return self.import_prometheus_rules_with_options(request, runtime)

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
            version='2021-04-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20210422_models.ListActivatedAlertsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_activated_alerts(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_activated_alerts_with_options(request, runtime)

    def list_alert_templates_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alert_provider):
            query['AlertProvider'] = request.alert_provider
        if not UtilClient.is_unset(request.labels):
            query['Labels'] = request.labels
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.template_provider):
            query['TemplateProvider'] = request.template_provider
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAlertTemplates',
            version='2021-04-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20210422_models.ListAlertTemplatesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_alert_templates(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_alert_templates_with_options(request, runtime)

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
            version='2021-04-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20210422_models.ListClusterFromGrafanaResponse(),
            self.call_api(params, req, runtime)
        )

    def list_cluster_from_grafana(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_cluster_from_grafana_with_options(request, runtime)

    def list_dashboards_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.cluster_type):
            query['ClusterType'] = request.cluster_type
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
            version='2021-04-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20210422_models.ListDashboardsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_dashboards(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_dashboards_with_options(request, runtime)

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
            version='2021-04-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20210422_models.ListDispatchRuleResponse(),
            self.call_api(params, req, runtime)
        )

    def list_dispatch_rule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_dispatch_rule_with_options(request, runtime)

    def list_prom_clusters_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPromClusters',
            version='2021-04-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20210422_models.ListPromClustersResponse(),
            self.call_api(params, req, runtime)
        )

    def list_prom_clusters(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_prom_clusters_with_options(request, runtime)

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
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPrometheusAlertRules',
            version='2021-04-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20210422_models.ListPrometheusAlertRulesResponse(),
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
            version='2021-04-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20210422_models.ListPrometheusAlertTemplatesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_prometheus_alert_templates(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_prometheus_alert_templates_with_options(request, runtime)

    def list_retcode_apps_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.security_token):
            query['SecurityToken'] = request.security_token
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListRetcodeApps',
            version='2021-04-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20210422_models.ListRetcodeAppsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_retcode_apps(self, request):
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
            version='2021-04-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20210422_models.ListScenarioResponse(),
            self.call_api(params, req, runtime)
        )

    def list_scenario(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_scenario_with_options(request, runtime)

    def list_serverless_top_napps_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.limit):
            query['Limit'] = request.limit
        if not UtilClient.is_unset(request.order_by):
            query['OrderBy'] = request.order_by
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListServerlessTopNApps',
            version='2021-04-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20210422_models.ListServerlessTopNAppsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_serverless_top_napps(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_serverless_top_napps_with_options(request, runtime)

    def list_trace_apps_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTraceApps',
            version='2021-04-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20210422_models.ListTraceAppsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_trace_apps(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_trace_apps_with_options(request, runtime)

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
            version='2021-04-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20210422_models.OpenArmsDefaultSLRResponse(),
            self.call_api(params, req, runtime)
        )

    def open_arms_default_slr(self, request):
        runtime = util_models.RuntimeOptions()
        return self.open_arms_default_slrwith_options(request, runtime)

    def open_arms_service_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='OpenArmsService',
            version='2021-04-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20210422_models.OpenArmsServiceResponse(),
            self.call_api(params, req, runtime)
        )

    def open_arms_service(self, request):
        runtime = util_models.RuntimeOptions()
        return self.open_arms_service_with_options(request, runtime)

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
            version='2021-04-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20210422_models.OpenVClusterResponse(),
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
            version='2021-04-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20210422_models.OpenXtraceDefaultSLRResponse(),
            self.call_api(params, req, runtime)
        )

    def open_xtrace_default_slr(self, request):
        runtime = util_models.RuntimeOptions()
        return self.open_xtrace_default_slrwith_options(request, runtime)

    def query_dataset_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.dataset_id):
            query['DatasetId'] = request.dataset_id
        if not UtilClient.is_unset(request.date_str):
            query['DateStr'] = request.date_str
        if not UtilClient.is_unset(request.dimensions):
            query['Dimensions'] = request.dimensions
        if not UtilClient.is_unset(request.hungry_mode):
            query['HungryMode'] = request.hungry_mode
        if not UtilClient.is_unset(request.interval_in_sec):
            query['IntervalInSec'] = request.interval_in_sec
        if not UtilClient.is_unset(request.is_drill_down):
            query['IsDrillDown'] = request.is_drill_down
        if not UtilClient.is_unset(request.limit):
            query['Limit'] = request.limit
        if not UtilClient.is_unset(request.max_time):
            query['MaxTime'] = request.max_time
        if not UtilClient.is_unset(request.measures):
            query['Measures'] = request.measures
        if not UtilClient.is_unset(request.min_time):
            query['MinTime'] = request.min_time
        if not UtilClient.is_unset(request.optional_dims):
            query['OptionalDims'] = request.optional_dims
        if not UtilClient.is_unset(request.order_by_key):
            query['OrderByKey'] = request.order_by_key
        if not UtilClient.is_unset(request.proxy_user_id):
            query['ProxyUserId'] = request.proxy_user_id
        if not UtilClient.is_unset(request.reduce_tail):
            query['ReduceTail'] = request.reduce_tail
        if not UtilClient.is_unset(request.required_dims):
            query['RequiredDims'] = request.required_dims
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryDataset',
            version='2021-04-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20210422_models.QueryDatasetResponse(),
            self.call_api(params, req, runtime)
        )

    def query_dataset(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_dataset_with_options(request, runtime)

    def query_metric_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.consistency_data_key):
            query['ConsistencyDataKey'] = request.consistency_data_key
        if not UtilClient.is_unset(request.consistency_query_strategy):
            query['ConsistencyQueryStrategy'] = request.consistency_query_strategy
        if not UtilClient.is_unset(request.dimensions):
            query['Dimensions'] = request.dimensions
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.filters):
            query['Filters'] = request.filters
        if not UtilClient.is_unset(request.interval_in_sec):
            query['IntervalInSec'] = request.interval_in_sec
        if not UtilClient.is_unset(request.limit):
            query['Limit'] = request.limit
        if not UtilClient.is_unset(request.measures):
            query['Measures'] = request.measures
        if not UtilClient.is_unset(request.metric):
            query['Metric'] = request.metric
        if not UtilClient.is_unset(request.order):
            query['Order'] = request.order
        if not UtilClient.is_unset(request.order_by):
            query['OrderBy'] = request.order_by
        if not UtilClient.is_unset(request.proxy_user_id):
            query['ProxyUserId'] = request.proxy_user_id
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryMetric',
            version='2021-04-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20210422_models.QueryMetricResponse(),
            self.call_api(params, req, runtime)
        )

    def query_metric(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_metric_with_options(request, runtime)

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
            version='2021-04-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20210422_models.QueryMetricByPageResponse(),
            self.call_api(params, req, runtime)
        )

    def query_metric_by_page(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_metric_by_page_with_options(request, runtime)

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
            version='2021-04-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20210422_models.SaveTraceAppConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def save_trace_app_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.save_trace_app_config_with_options(request, runtime)

    def search_alert_contact_with_options(self, request, runtime):
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
            version='2021-04-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20210422_models.SearchAlertContactResponse(),
            self.call_api(params, req, runtime)
        )

    def search_alert_contact(self, request):
        runtime = util_models.RuntimeOptions()
        return self.search_alert_contact_with_options(request, runtime)

    def search_alert_contact_group_with_options(self, request, runtime):
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
            version='2021-04-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20210422_models.SearchAlertContactGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def search_alert_contact_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.search_alert_contact_group_with_options(request, runtime)

    def search_alert_histories_with_options(self, request, runtime):
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
            version='2021-04-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20210422_models.SearchAlertHistoriesResponse(),
            self.call_api(params, req, runtime)
        )

    def search_alert_histories(self, request):
        runtime = util_models.RuntimeOptions()
        return self.search_alert_histories_with_options(request, runtime)

    def search_alert_rules_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
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
        if not UtilClient.is_unset(request.title):
            query['Title'] = request.title
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SearchAlertRules',
            version='2021-04-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20210422_models.SearchAlertRulesResponse(),
            self.call_api(params, req, runtime)
        )

    def search_alert_rules(self, request):
        runtime = util_models.RuntimeOptions()
        return self.search_alert_rules_with_options(request, runtime)

    def search_events_with_options(self, request, runtime):
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
            version='2021-04-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20210422_models.SearchEventsResponse(),
            self.call_api(params, req, runtime)
        )

    def search_events(self, request):
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
        if not UtilClient.is_unset(request.retcode_app_name):
            query['RetcodeAppName'] = request.retcode_app_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SearchRetcodeAppByPage',
            version='2021-04-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20210422_models.SearchRetcodeAppByPageResponse(),
            self.call_api(params, req, runtime)
        )

    def search_retcode_app_by_page(self, request):
        runtime = util_models.RuntimeOptions()
        return self.search_retcode_app_by_page_with_options(request, runtime)

    def search_trace_app_by_name_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.trace_app_name):
            query['TraceAppName'] = request.trace_app_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SearchTraceAppByName',
            version='2021-04-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20210422_models.SearchTraceAppByNameResponse(),
            self.call_api(params, req, runtime)
        )

    def search_trace_app_by_name(self, request):
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
        if not UtilClient.is_unset(request.trace_app_name):
            query['TraceAppName'] = request.trace_app_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SearchTraceAppByPage',
            version='2021-04-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20210422_models.SearchTraceAppByPageResponse(),
            self.call_api(params, req, runtime)
        )

    def search_trace_app_by_page(self, request):
        runtime = util_models.RuntimeOptions()
        return self.search_trace_app_by_page_with_options(request, runtime)

    def search_traces_with_options(self, request, runtime):
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
            version='2021-04-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20210422_models.SearchTracesResponse(),
            self.call_api(params, req, runtime)
        )

    def search_traces(self, request):
        runtime = util_models.RuntimeOptions()
        return self.search_traces_with_options(request, runtime)

    def search_traces_by_page_with_options(self, request, runtime):
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
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
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
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SearchTracesByPage',
            version='2021-04-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20210422_models.SearchTracesByPageResponse(),
            self.call_api(params, req, runtime)
        )

    def search_traces_by_page(self, request):
        runtime = util_models.RuntimeOptions()
        return self.search_traces_by_page_with_options(request, runtime)

    def send_custom_incidents_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.incidents):
            query['Incidents'] = request.incidents
        if not UtilClient.is_unset(request.product_type):
            query['ProductType'] = request.product_type
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SendCustomIncidents',
            version='2021-04-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20210422_models.SendCustomIncidentsResponse(),
            self.call_api(params, req, runtime)
        )

    def send_custom_incidents(self, request):
        runtime = util_models.RuntimeOptions()
        return self.send_custom_incidents_with_options(request, runtime)

    def send_mse_incident_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.incidents):
            query['Incidents'] = request.incidents
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SendMseIncident',
            version='2021-04-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20210422_models.SendMseIncidentResponse(),
            self.call_api(params, req, runtime)
        )

    def send_mse_incident(self, request):
        runtime = util_models.RuntimeOptions()
        return self.send_mse_incident_with_options(request, runtime)

    def set_retcode_share_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.pid):
            query['Pid'] = request.pid
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetRetcodeShareStatus',
            version='2021-04-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20210422_models.SetRetcodeShareStatusResponse(),
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
            version='2021-04-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20210422_models.StartAlertResponse(),
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
            version='2021-04-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20210422_models.StopAlertResponse(),
            self.call_api(params, req, runtime)
        )

    def stop_alert(self, request):
        runtime = util_models.RuntimeOptions()
        return self.stop_alert_with_options(request, runtime)

    def update_alert_contact_with_options(self, request, runtime):
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
            version='2021-04-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20210422_models.UpdateAlertContactResponse(),
            self.call_api(params, req, runtime)
        )

    def update_alert_contact(self, request):
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
            version='2021-04-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20210422_models.UpdateAlertContactGroupResponse(),
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
            version='2021-04-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20210422_models.UpdateAlertRuleResponse(),
            self.call_api(params, req, runtime)
        )

    def update_alert_rule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_alert_rule_with_options(request, runtime)

    def update_alert_template_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.annotations):
            query['Annotations'] = request.annotations
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.labels):
            query['Labels'] = request.labels
        if not UtilClient.is_unset(request.match_expressions):
            query['MatchExpressions'] = request.match_expressions
        if not UtilClient.is_unset(request.message):
            query['Message'] = request.message
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.rule):
            query['Rule'] = request.rule
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateAlertTemplate',
            version='2021-04-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20210422_models.UpdateAlertTemplateResponse(),
            self.call_api(params, req, runtime)
        )

    def update_alert_template(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_alert_template_with_options(request, runtime)

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
            version='2021-04-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20210422_models.UpdateDispatchRuleResponse(),
            self.call_api(params, req, runtime)
        )

    def update_dispatch_rule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_dispatch_rule_with_options(request, runtime)

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
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdatePrometheusAlertRule',
            version='2021-04-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20210422_models.UpdatePrometheusAlertRuleResponse(),
            self.call_api(params, req, runtime)
        )

    def update_prometheus_alert_rule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_prometheus_alert_rule_with_options(request, runtime)

    def update_webhook_with_options(self, request, runtime):
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
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.url):
            query['Url'] = request.url
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateWebhook',
            version='2021-04-22',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            arms20210422_models.UpdateWebhookResponse(),
            self.call_api(params, req, runtime)
        )

    def update_webhook(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_webhook_with_options(request, runtime)
