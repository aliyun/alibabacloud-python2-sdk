# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_mse20190531 import models as mse_20190531_models
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
            'cn-chengdu': 'mse.cn-chegndu.aliyuncs.com',
            'ap-northeast-1': 'mse. ap-northeast-1.aliyuncs.com',
            'cn-shanghai-finance-1': 'msefinance-share.cn-shanghai-finance-1.aliyuncs.com',
            'cn-shenzhen-finance-1': 'msefinance-share.cn-shenzhen-finance-1.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('mse', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def add_mock_rule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mse_20190531_models.AddMockRuleResponse(),
            self.do_rpcrequest('AddMockRule', '2019-05-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def add_mock_rule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_mock_rule_with_options(request, runtime)

    def clone_nacos_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mse_20190531_models.CloneNacosConfigResponse(),
            self.do_rpcrequest('CloneNacosConfig', '2019-05-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def clone_nacos_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.clone_nacos_config_with_options(request, runtime)

    def create_alarm_rule_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = mse_20190531_models.CreateAlarmRuleShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.alert_way):
            request.alert_way_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.alert_way, 'AlertWay', 'json')
        if not UtilClient.is_unset(tmp_req.contact_group_ids):
            request.contact_group_ids_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.contact_group_ids, 'ContactGroupIds', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mse_20190531_models.CreateAlarmRuleResponse(),
            self.do_rpcrequest('CreateAlarmRule', '2019-05-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_alarm_rule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_alarm_rule_with_options(request, runtime)

    def create_application_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mse_20190531_models.CreateApplicationResponse(),
            self.do_rpcrequest('CreateApplication', '2019-05-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_application(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_application_with_options(request, runtime)

    def create_cluster_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mse_20190531_models.CreateClusterResponse(),
            self.do_rpcrequest('CreateCluster', '2019-05-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_cluster(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_cluster_with_options(request, runtime)

    def create_engine_namespace_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mse_20190531_models.CreateEngineNamespaceResponse(),
            self.do_rpcrequest('CreateEngineNamespace', '2019-05-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_engine_namespace(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_engine_namespace_with_options(request, runtime)

    def create_nacos_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mse_20190531_models.CreateNacosConfigResponse(),
            self.do_rpcrequest('CreateNacosConfig', '2019-05-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_nacos_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_nacos_config_with_options(request, runtime)

    def create_znode_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mse_20190531_models.CreateZnodeResponse(),
            self.do_rpcrequest('CreateZnode', '2019-05-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_znode(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_znode_with_options(request, runtime)

    def delete_alarm_rule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mse_20190531_models.DeleteAlarmRuleResponse(),
            self.do_rpcrequest('DeleteAlarmRule', '2019-05-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_alarm_rule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_alarm_rule_with_options(request, runtime)

    def delete_cluster_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mse_20190531_models.DeleteClusterResponse(),
            self.do_rpcrequest('DeleteCluster', '2019-05-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_cluster(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_cluster_with_options(request, runtime)

    def delete_engine_namespace_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mse_20190531_models.DeleteEngineNamespaceResponse(),
            self.do_rpcrequest('DeleteEngineNamespace', '2019-05-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_engine_namespace(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_engine_namespace_with_options(request, runtime)

    def delete_nacos_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mse_20190531_models.DeleteNacosConfigResponse(),
            self.do_rpcrequest('DeleteNacosConfig', '2019-05-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_nacos_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_nacos_config_with_options(request, runtime)

    def delete_nacos_configs_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mse_20190531_models.DeleteNacosConfigsResponse(),
            self.do_rpcrequest('DeleteNacosConfigs', '2019-05-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_nacos_configs(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_nacos_configs_with_options(request, runtime)

    def delete_nacos_service_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mse_20190531_models.DeleteNacosServiceResponse(),
            self.do_rpcrequest('DeleteNacosService', '2019-05-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_nacos_service(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_nacos_service_with_options(request, runtime)

    def delete_znode_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mse_20190531_models.DeleteZnodeResponse(),
            self.do_rpcrequest('DeleteZnode', '2019-05-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_znode(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_znode_with_options(request, runtime)

    def export_nacos_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mse_20190531_models.ExportNacosConfigResponse(),
            self.do_rpcrequest('ExportNacosConfig', '2019-05-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def export_nacos_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.export_nacos_config_with_options(request, runtime)

    def get_engine_namepace_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mse_20190531_models.GetEngineNamepaceResponse(),
            self.do_rpcrequest('GetEngineNamepace', '2019-05-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_engine_namepace(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_engine_namepace_with_options(request, runtime)

    def get_import_file_url_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mse_20190531_models.GetImportFileUrlResponse(),
            self.do_rpcrequest('GetImportFileUrl', '2019-05-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_import_file_url(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_import_file_url_with_options(request, runtime)

    def get_nacos_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mse_20190531_models.GetNacosConfigResponse(),
            self.do_rpcrequest('GetNacosConfig', '2019-05-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_nacos_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_nacos_config_with_options(request, runtime)

    def get_nacos_history_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mse_20190531_models.GetNacosHistoryConfigResponse(),
            self.do_rpcrequest('GetNacosHistoryConfig', '2019-05-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_nacos_history_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_nacos_history_config_with_options(request, runtime)

    def get_overview_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mse_20190531_models.GetOverviewResponse(),
            self.do_rpcrequest('GetOverview', '2019-05-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_overview(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_overview_with_options(request, runtime)

    def import_nacos_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mse_20190531_models.ImportNacosConfigResponse(),
            self.do_rpcrequest('ImportNacosConfig', '2019-05-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def import_nacos_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.import_nacos_config_with_options(request, runtime)

    def list_alarm_contact_groups_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            mse_20190531_models.ListAlarmContactGroupsResponse(),
            self.do_rpcrequest('ListAlarmContactGroups', '2019-05-31', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def list_alarm_contact_groups(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_alarm_contact_groups_with_options(request, runtime)

    def list_alarm_histories_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            mse_20190531_models.ListAlarmHistoriesResponse(),
            self.do_rpcrequest('ListAlarmHistories', '2019-05-31', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def list_alarm_histories(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_alarm_histories_with_options(request, runtime)

    def list_alarm_items_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            mse_20190531_models.ListAlarmItemsResponse(),
            self.do_rpcrequest('ListAlarmItems', '2019-05-31', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def list_alarm_items(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_alarm_items_with_options(request, runtime)

    def list_alarm_rules_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            mse_20190531_models.ListAlarmRulesResponse(),
            self.do_rpcrequest('ListAlarmRules', '2019-05-31', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def list_alarm_rules(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_alarm_rules_with_options(request, runtime)

    def list_ans_instances_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            mse_20190531_models.ListAnsInstancesResponse(),
            self.do_rpcrequest('ListAnsInstances', '2019-05-31', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def list_ans_instances(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_ans_instances_with_options(request, runtime)

    def list_ans_service_clusters_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            mse_20190531_models.ListAnsServiceClustersResponse(),
            self.do_rpcrequest('ListAnsServiceClusters', '2019-05-31', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def list_ans_service_clusters(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_ans_service_clusters_with_options(request, runtime)

    def list_ans_services_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            mse_20190531_models.ListAnsServicesResponse(),
            self.do_rpcrequest('ListAnsServices', '2019-05-31', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def list_ans_services(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_ans_services_with_options(request, runtime)

    def list_cluster_connection_types_with_options(self, runtime):
        req = open_api_models.OpenApiRequest()
        return TeaCore.from_map(
            mse_20190531_models.ListClusterConnectionTypesResponse(),
            self.do_rpcrequest('ListClusterConnectionTypes', '2019-05-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_cluster_connection_types(self):
        runtime = util_models.RuntimeOptions()
        return self.list_cluster_connection_types_with_options(runtime)

    def list_clusters_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            mse_20190531_models.ListClustersResponse(),
            self.do_rpcrequest('ListClusters', '2019-05-31', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def list_clusters(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_clusters_with_options(request, runtime)

    def list_cluster_types_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mse_20190531_models.ListClusterTypesResponse(),
            self.do_rpcrequest('ListClusterTypes', '2019-05-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_cluster_types(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_cluster_types_with_options(request, runtime)

    def list_cluster_versions_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mse_20190531_models.ListClusterVersionsResponse(),
            self.do_rpcrequest('ListClusterVersions', '2019-05-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_cluster_versions(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_cluster_versions_with_options(request, runtime)

    def list_engine_namespaces_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            mse_20190531_models.ListEngineNamespacesResponse(),
            self.do_rpcrequest('ListEngineNamespaces', '2019-05-31', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def list_engine_namespaces(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_engine_namespaces_with_options(request, runtime)

    def list_eureka_instances_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            mse_20190531_models.ListEurekaInstancesResponse(),
            self.do_rpcrequest('ListEurekaInstances', '2019-05-31', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def list_eureka_instances(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_eureka_instances_with_options(request, runtime)

    def list_eureka_services_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            mse_20190531_models.ListEurekaServicesResponse(),
            self.do_rpcrequest('ListEurekaServices', '2019-05-31', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def list_eureka_services(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_eureka_services_with_options(request, runtime)

    def list_listeners_by_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mse_20190531_models.ListListenersByConfigResponse(),
            self.do_rpcrequest('ListListenersByConfig', '2019-05-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_listeners_by_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_listeners_by_config_with_options(request, runtime)

    def list_listeners_by_ip_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mse_20190531_models.ListListenersByIpResponse(),
            self.do_rpcrequest('ListListenersByIp', '2019-05-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_listeners_by_ip(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_listeners_by_ip_with_options(request, runtime)

    def list_nacos_configs_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mse_20190531_models.ListNacosConfigsResponse(),
            self.do_rpcrequest('ListNacosConfigs', '2019-05-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_nacos_configs(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_nacos_configs_with_options(request, runtime)

    def list_nacos_history_configs_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mse_20190531_models.ListNacosHistoryConfigsResponse(),
            self.do_rpcrequest('ListNacosHistoryConfigs', '2019-05-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_nacos_history_configs(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_nacos_history_configs_with_options(request, runtime)

    def list_znode_children_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            mse_20190531_models.ListZnodeChildrenResponse(),
            self.do_rpcrequest('ListZnodeChildren', '2019-05-31', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def list_znode_children(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_znode_children_with_options(request, runtime)

    def query_business_locations_with_options(self, runtime):
        req = open_api_models.OpenApiRequest()
        return TeaCore.from_map(
            mse_20190531_models.QueryBusinessLocationsResponse(),
            self.do_rpcrequest('QueryBusinessLocations', '2019-05-31', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def query_business_locations(self):
        runtime = util_models.RuntimeOptions()
        return self.query_business_locations_with_options(runtime)

    def query_cluster_detail_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mse_20190531_models.QueryClusterDetailResponse(),
            self.do_rpcrequest('QueryClusterDetail', '2019-05-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_cluster_detail(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_cluster_detail_with_options(request, runtime)

    def query_cluster_disk_specification_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mse_20190531_models.QueryClusterDiskSpecificationResponse(),
            self.do_rpcrequest('QueryClusterDiskSpecification', '2019-05-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_cluster_disk_specification(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_cluster_disk_specification_with_options(request, runtime)

    def query_cluster_specification_with_options(self, runtime):
        req = open_api_models.OpenApiRequest()
        return TeaCore.from_map(
            mse_20190531_models.QueryClusterSpecificationResponse(),
            self.do_rpcrequest('QueryClusterSpecification', '2019-05-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def query_cluster_specification(self):
        runtime = util_models.RuntimeOptions()
        return self.query_cluster_specification_with_options(runtime)

    def query_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            mse_20190531_models.QueryConfigResponse(),
            self.do_rpcrequest('QueryConfig', '2019-05-31', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def query_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_config_with_options(request, runtime)

    def query_monitor_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            mse_20190531_models.QueryMonitorResponse(),
            self.do_rpcrequest('QueryMonitor', '2019-05-31', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def query_monitor(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_monitor_with_options(request, runtime)

    def query_znode_detail_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            mse_20190531_models.QueryZnodeDetailResponse(),
            self.do_rpcrequest('QueryZnodeDetail', '2019-05-31', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def query_znode_detail(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_znode_detail_with_options(request, runtime)

    def restart_cluster_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mse_20190531_models.RestartClusterResponse(),
            self.do_rpcrequest('RestartCluster', '2019-05-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def restart_cluster(self, request):
        runtime = util_models.RuntimeOptions()
        return self.restart_cluster_with_options(request, runtime)

    def retry_cluster_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mse_20190531_models.RetryClusterResponse(),
            self.do_rpcrequest('RetryCluster', '2019-05-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def retry_cluster(self, request):
        runtime = util_models.RuntimeOptions()
        return self.retry_cluster_with_options(request, runtime)

    def scaling_cluster_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mse_20190531_models.ScalingClusterResponse(),
            self.do_rpcrequest('ScalingCluster', '2019-05-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def scaling_cluster(self, request):
        runtime = util_models.RuntimeOptions()
        return self.scaling_cluster_with_options(request, runtime)

    def update_acl_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mse_20190531_models.UpdateAclResponse(),
            self.do_rpcrequest('UpdateAcl', '2019-05-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_acl(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_acl_with_options(request, runtime)

    def update_cluster_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mse_20190531_models.UpdateClusterResponse(),
            self.do_rpcrequest('UpdateCluster', '2019-05-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_cluster(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_cluster_with_options(request, runtime)

    def update_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mse_20190531_models.UpdateConfigResponse(),
            self.do_rpcrequest('UpdateConfig', '2019-05-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_config_with_options(request, runtime)

    def update_engine_namespace_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mse_20190531_models.UpdateEngineNamespaceResponse(),
            self.do_rpcrequest('UpdateEngineNamespace', '2019-05-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_engine_namespace(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_engine_namespace_with_options(request, runtime)

    def update_nacos_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mse_20190531_models.UpdateNacosConfigResponse(),
            self.do_rpcrequest('UpdateNacosConfig', '2019-05-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_nacos_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_nacos_config_with_options(request, runtime)

    def update_nacos_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mse_20190531_models.UpdateNacosInstanceResponse(),
            self.do_rpcrequest('UpdateNacosInstance', '2019-05-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_nacos_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_nacos_instance_with_options(request, runtime)

    def update_znode_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mse_20190531_models.UpdateZnodeResponse(),
            self.do_rpcrequest('UpdateZnode', '2019-05-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_znode(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_znode_with_options(request, runtime)

    def upgrade_cluster_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            mse_20190531_models.UpgradeClusterResponse(),
            self.do_rpcrequest('UpgradeCluster', '2019-05-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def upgrade_cluster(self, request):
        runtime = util_models.RuntimeOptions()
        return self.upgrade_cluster_with_options(request, runtime)
