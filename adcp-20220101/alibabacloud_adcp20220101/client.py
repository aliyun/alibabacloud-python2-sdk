# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_adcp20220101 import models as adcp_20220101_models
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
        self._endpoint = self.get_endpoint('adcp', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def attach_cluster_to_hub_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        body = {}
        if not UtilClient.is_unset(request.cluster_ids):
            body['ClusterIds'] = request.cluster_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='AttachClusterToHub',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adcp_20220101_models.AttachClusterToHubResponse(),
            self.call_api(params, req, runtime)
        )

    def attach_cluster_to_hub(self, request):
        runtime = util_models.RuntimeOptions()
        return self.attach_cluster_to_hub_with_options(request, runtime)

    def create_hub_cluster_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.api_server_public_eip):
            body['ApiServerPublicEip'] = request.api_server_public_eip
        if not UtilClient.is_unset(request.audit_log_enabled):
            body['AuditLogEnabled'] = request.audit_log_enabled
        if not UtilClient.is_unset(request.audit_log_project):
            body['AuditLogProject'] = request.audit_log_project
        if not UtilClient.is_unset(request.audit_log_store_ttl):
            body['AuditLogStoreTTL'] = request.audit_log_store_ttl
        if not UtilClient.is_unset(request.control_plane_log_enabled):
            body['ControlPlaneLogEnabled'] = request.control_plane_log_enabled
        if not UtilClient.is_unset(request.control_plane_log_project):
            body['ControlPlaneLogProject'] = request.control_plane_log_project
        if not UtilClient.is_unset(request.control_plane_log_ttl):
            body['ControlPlaneLogTTL'] = request.control_plane_log_ttl
        if not UtilClient.is_unset(request.is_enterprise_security_group):
            body['IsEnterpriseSecurityGroup'] = request.is_enterprise_security_group
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.region_id):
            body['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.v_switches):
            body['VSwitches'] = request.v_switches
        if not UtilClient.is_unset(request.vpc_id):
            body['VpcId'] = request.vpc_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateHubCluster',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adcp_20220101_models.CreateHubClusterResponse(),
            self.call_api(params, req, runtime)
        )

    def create_hub_cluster(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_hub_cluster_with_options(request, runtime)

    def delete_hub_cluster_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.force):
            query['Force'] = request.force
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteHubCluster',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adcp_20220101_models.DeleteHubClusterResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_hub_cluster(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_hub_cluster_with_options(request, runtime)

    def describe_hub_cluster_details_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeHubClusterDetails',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adcp_20220101_models.DescribeHubClusterDetailsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_hub_cluster_details(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_hub_cluster_details_with_options(request, runtime)

    def describe_hub_cluster_kubeconfig_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.private_ip_address):
            query['PrivateIpAddress'] = request.private_ip_address
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeHubClusterKubeconfig',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adcp_20220101_models.DescribeHubClusterKubeconfigResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_hub_cluster_kubeconfig(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_hub_cluster_kubeconfig_with_options(request, runtime)

    def describe_hub_cluster_logs_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeHubClusterLogs',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adcp_20220101_models.DescribeHubClusterLogsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_hub_cluster_logs(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_hub_cluster_logs_with_options(request, runtime)

    def describe_hub_clusters_with_options(self, runtime):
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeHubClusters',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adcp_20220101_models.DescribeHubClustersResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_hub_clusters(self):
        runtime = util_models.RuntimeOptions()
        return self.describe_hub_clusters_with_options(runtime)

    def describe_managed_clusters_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeManagedClusters',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adcp_20220101_models.DescribeManagedClustersResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_managed_clusters(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_managed_clusters_with_options(request, runtime)

    def describe_regions_with_options(self, runtime):
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DescribeRegions',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adcp_20220101_models.DescribeRegionsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_regions(self):
        runtime = util_models.RuntimeOptions()
        return self.describe_regions_with_options(runtime)

    def detach_cluster_from_hub_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        body = {}
        if not UtilClient.is_unset(request.cluster_ids):
            body['ClusterIds'] = request.cluster_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DetachClusterFromHub',
            version='2022-01-01',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            adcp_20220101_models.DetachClusterFromHubResponse(),
            self.call_api(params, req, runtime)
        )

    def detach_cluster_from_hub(self, request):
        runtime = util_models.RuntimeOptions()
        return self.detach_cluster_from_hub_with_options(request, runtime)
