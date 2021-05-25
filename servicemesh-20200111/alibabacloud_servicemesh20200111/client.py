# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_servicemesh20200111 import models as servicemesh_20200111_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_openapi_util.client import Client as OpenApiUtilClient


class Client(OpenApiClient):
    """
    *\
    """
    def __init__(self, config):
        super(Client, self).__init__(config)
        self._endpoint_rule = 'central'
        self.check_config(config)
        self._endpoint = self.get_endpoint('servicemesh', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def run_diagnosis_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.RunDiagnosisResponse(),
            self.do_rpcrequest('RunDiagnosis', '2020-01-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def run_diagnosis(self, request):
        runtime = util_models.RuntimeOptions()
        return self.run_diagnosis_with_options(request, runtime)

    def describe_guest_cluster_access_log_dashboards_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.DescribeGuestClusterAccessLogDashboardsResponse(),
            self.do_rpcrequest('DescribeGuestClusterAccessLogDashboards', '2020-01-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_guest_cluster_access_log_dashboards(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_guest_cluster_access_log_dashboards_with_options(request, runtime)

    def list_builtin_envoy_filter_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.ListBuiltinEnvoyFilterResponse(),
            self.do_rpcrequest('ListBuiltinEnvoyFilter', '2020-01-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_builtin_envoy_filter(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_builtin_envoy_filter_with_options(request, runtime)

    def describe_service_meshes_with_options(self, runtime):
        req = open_api_models.OpenApiRequest()
        return TeaCore.from_map(
            servicemesh_20200111_models.DescribeServiceMeshesResponse(),
            self.do_rpcrequest('DescribeServiceMeshes', '2020-01-11', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def describe_service_meshes(self):
        runtime = util_models.RuntimeOptions()
        return self.describe_service_meshes_with_options(runtime)

    def modify_builtin_envoy_filter_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.ModifyBuiltinEnvoyFilterResponse(),
            self.do_rpcrequest('ModifyBuiltinEnvoyFilter', '2020-01-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_builtin_envoy_filter(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_builtin_envoy_filter_with_options(request, runtime)

    def describe_available_nacos_instances_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.DescribeAvailableNacosInstancesResponse(),
            self.do_rpcrequest('DescribeAvailableNacosInstances', '2020-01-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_available_nacos_instances(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_available_nacos_instances_with_options(request, runtime)

    def describe_ingress_gateways_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.DescribeIngressGatewaysResponse(),
            self.do_rpcrequest('DescribeIngressGateways', '2020-01-11', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def describe_ingress_gateways(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_ingress_gateways_with_options(request, runtime)

    def describe_service_mesh_detail_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.DescribeServiceMeshDetailResponse(),
            self.do_rpcrequest('DescribeServiceMeshDetail', '2020-01-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_service_mesh_detail(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_service_mesh_detail_with_options(request, runtime)

    def upgrade_mesh_version_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.UpgradeMeshVersionResponse(),
            self.do_rpcrequest('UpgradeMeshVersion', '2020-01-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def upgrade_mesh_version(self, request):
        runtime = util_models.RuntimeOptions()
        return self.upgrade_mesh_version_with_options(request, runtime)

    def describe_service_mesh_kubeconfig_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.DescribeServiceMeshKubeconfigResponse(),
            self.do_rpcrequest('DescribeServiceMeshKubeconfig', '2020-01-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_service_mesh_kubeconfig(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_service_mesh_kubeconfig_with_options(request, runtime)

    def get_ca_cert_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.GetCaCertResponse(),
            self.do_rpcrequest('GetCaCert', '2020-01-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_ca_cert(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_ca_cert_with_options(request, runtime)

    def get_service_mesh_slb_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.GetServiceMeshSlbResponse(),
            self.do_rpcrequest('GetServiceMeshSlb', '2020-01-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_service_mesh_slb(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_service_mesh_slb_with_options(request, runtime)

    def get_registered_service_endpoints_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.GetRegisteredServiceEndpointsResponse(),
            self.do_rpcrequest('GetRegisteredServiceEndpoints', '2020-01-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_registered_service_endpoints(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_registered_service_endpoints_with_options(request, runtime)

    def get_auto_injection_label_sync_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.GetAutoInjectionLabelSyncStatusResponse(),
            self.do_rpcrequest('GetAutoInjectionLabelSyncStatus', '2020-01-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_auto_injection_label_sync_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_auto_injection_label_sync_status_with_options(request, runtime)

    def get_registered_service_namespaces_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.GetRegisteredServiceNamespacesResponse(),
            self.do_rpcrequest('GetRegisteredServiceNamespaces', '2020-01-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_registered_service_namespaces(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_registered_service_namespaces_with_options(request, runtime)

    def describe_vswitches_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.DescribeVSwitchesResponse(),
            self.do_rpcrequest('DescribeVSwitches', '2020-01-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_vswitches(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_vswitches_with_options(request, runtime)

    def describe_vpcs_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.DescribeVpcsResponse(),
            self.do_rpcrequest('DescribeVpcs', '2020-01-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_vpcs(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_vpcs_with_options(request, runtime)

    def remove_vm_app_from_mesh_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.RemoveVmAppFromMeshResponse(),
            self.do_rpcrequest('RemoveVmAppFromMesh', '2020-01-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def remove_vm_app_from_mesh(self, request):
        runtime = util_models.RuntimeOptions()
        return self.remove_vm_app_from_mesh_with_options(request, runtime)

    def describe_cluster_prometheus_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.DescribeClusterPrometheusResponse(),
            self.do_rpcrequest('DescribeClusterPrometheus', '2020-01-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_cluster_prometheus(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_cluster_prometheus_with_options(request, runtime)

    def update_istio_injection_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.UpdateIstioInjectionConfigResponse(),
            self.do_rpcrequest('UpdateIstioInjectionConfig', '2020-01-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_istio_injection_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_istio_injection_config_with_options(request, runtime)

    def get_vm_meta_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.GetVmMetaResponse(),
            self.do_rpcrequest('GetVmMeta', '2020-01-11', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def get_vm_meta(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_vm_meta_with_options(request, runtime)

    def describe_upgrade_version_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.DescribeUpgradeVersionResponse(),
            self.do_rpcrequest('DescribeUpgradeVersion', '2020-01-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_upgrade_version(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_upgrade_version_with_options(request, runtime)

    def describe_clusters_in_service_mesh_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.DescribeClustersInServiceMeshResponse(),
            self.do_rpcrequest('DescribeClustersInServiceMesh', '2020-01-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_clusters_in_service_mesh(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_clusters_in_service_mesh_with_options(request, runtime)

    def get_builtin_envoy_filter_catalog_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.GetBuiltinEnvoyFilterCatalogResponse(),
            self.do_rpcrequest('GetBuiltinEnvoyFilterCatalog', '2020-01-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_builtin_envoy_filter_catalog(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_builtin_envoy_filter_catalog_with_options(request, runtime)

    def describe_cluster_grafana_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.DescribeClusterGrafanaResponse(),
            self.do_rpcrequest('DescribeClusterGrafana', '2020-01-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_cluster_grafana(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_cluster_grafana_with_options(request, runtime)

    def get_diagnosis_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.GetDiagnosisResponse(),
            self.do_rpcrequest('GetDiagnosis', '2020-01-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_diagnosis(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_diagnosis_with_options(request, runtime)

    def get_registered_services_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.GetRegisteredServicesResponse(),
            self.do_rpcrequest('GetRegisteredServices', '2020-01-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_registered_services(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_registered_services_with_options(request, runtime)

    def describe_cens_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.DescribeCensResponse(),
            self.do_rpcrequest('DescribeCens', '2020-01-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_cens(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_cens_with_options(request, runtime)

    def delete_service_mesh_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.DeleteServiceMeshResponse(),
            self.do_rpcrequest('DeleteServiceMesh', '2020-01-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_service_mesh(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_service_mesh_with_options(request, runtime)

    def get_sa_token_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.GetSaTokenResponse(),
            self.do_rpcrequest('GetSaToken', '2020-01-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_sa_token(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_sa_token_with_options(request, runtime)

    def get_vm_app_mesh_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.GetVmAppMeshInfoResponse(),
            self.do_rpcrequest('GetVmAppMeshInfo', '2020-01-11', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def get_vm_app_mesh_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_vm_app_mesh_info_with_options(request, runtime)

    def remove_cluster_from_service_mesh_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.RemoveClusterFromServiceMeshResponse(),
            self.do_rpcrequest('RemoveClusterFromServiceMesh', '2020-01-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def remove_cluster_from_service_mesh(self, request):
        runtime = util_models.RuntimeOptions()
        return self.remove_cluster_from_service_mesh_with_options(request, runtime)

    def describe_regions_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.DescribeRegionsResponse(),
            self.do_rpcrequest('DescribeRegions', '2020-01-11', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def describe_regions(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_regions_with_options(request, runtime)

    def set_service_registry_source_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = servicemesh_20200111_models.SetServiceRegistrySourceShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.config):
            request.config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.config, 'Config', 'json')
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.SetServiceRegistrySourceResponse(),
            self.do_rpcrequest('SetServiceRegistrySource', '2020-01-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def set_service_registry_source(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_service_registry_source_with_options(request, runtime)

    def add_cluster_into_service_mesh_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.AddClusterIntoServiceMeshResponse(),
            self.do_rpcrequest('AddClusterIntoServiceMesh', '2020-01-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def add_cluster_into_service_mesh(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_cluster_into_service_mesh_with_options(request, runtime)

    def add_builtin_envoy_filter_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.AddBuiltinEnvoyFilterResponse(),
            self.do_rpcrequest('AddBuiltinEnvoyFilter', '2020-01-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def add_builtin_envoy_filter(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_builtin_envoy_filter_with_options(request, runtime)

    def get_ecs_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=query
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.GetEcsListResponse(),
            self.do_rpcrequest('GetEcsList', '2020-01-11', 'HTTPS', 'GET', 'AK', 'json', req, runtime)
        )

    def get_ecs_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_ecs_list_with_options(request, runtime)

    def update_mesh_feature_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.UpdateMeshFeatureResponse(),
            self.do_rpcrequest('UpdateMeshFeature', '2020-01-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_mesh_feature(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_mesh_feature_with_options(request, runtime)

    def add_vm_app_to_mesh_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.AddVmAppToMeshResponse(),
            self.do_rpcrequest('AddVmAppToMesh', '2020-01-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def add_vm_app_to_mesh(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_vm_app_to_mesh_with_options(request, runtime)

    def create_service_mesh_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.CreateServiceMeshResponse(),
            self.do_rpcrequest('CreateServiceMesh', '2020-01-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_service_mesh(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_service_mesh_with_options(request, runtime)

    def get_service_registry_source_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.GetServiceRegistrySourceResponse(),
            self.do_rpcrequest('GetServiceRegistrySource', '2020-01-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_service_registry_source(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_service_registry_source_with_options(request, runtime)

    def remove_builtin_envoy_filter_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.RemoveBuiltinEnvoyFilterResponse(),
            self.do_rpcrequest('RemoveBuiltinEnvoyFilter', '2020-01-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def remove_builtin_envoy_filter(self, request):
        runtime = util_models.RuntimeOptions()
        return self.remove_builtin_envoy_filter_with_options(request, runtime)

    def get_builtin_envoy_filter_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.GetBuiltinEnvoyFilterResponse(),
            self.do_rpcrequest('GetBuiltinEnvoyFilter', '2020-01-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_builtin_envoy_filter(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_builtin_envoy_filter_with_options(request, runtime)

    def initialize_asmrole_with_options(self, runtime):
        req = open_api_models.OpenApiRequest()
        return TeaCore.from_map(
            servicemesh_20200111_models.InitializeASMRoleResponse(),
            self.do_rpcrequest('InitializeASMRole', '2020-01-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def initialize_asmrole(self):
        runtime = util_models.RuntimeOptions()
        return self.initialize_asmrole_with_options(runtime)

    def add_mesh_tag_to_ecs_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            servicemesh_20200111_models.AddMeshTagToEcsResponse(),
            self.do_rpcrequest('AddMeshTagToEcs', '2020-01-11', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def add_mesh_tag_to_ecs(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_mesh_tag_to_ecs_with_options(request, runtime)
