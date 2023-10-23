# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_emr20210320 import models as emr_20210320_models
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
            'cn-beijing': 'emr.aliyuncs.com',
            'cn-hangzhou': 'emr.aliyuncs.com',
            'cn-shanghai': 'emr.aliyuncs.com',
            'cn-shenzhen': 'emr.aliyuncs.com',
            'ap-southeast-1': 'emr.aliyuncs.com',
            'us-west-1': 'emr.aliyuncs.com',
            'cn-hangzhou-finance': 'emr.aliyuncs.com',
            'cn-shenzhen-finance-1': 'emr.aliyuncs.com',
            'cn-shanghai-finance-1': 'emr.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('emr', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def create_cluster_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_configs):
            query['ApplicationConfigs'] = request.application_configs
        if not UtilClient.is_unset(request.applications):
            query['Applications'] = request.applications
        if not UtilClient.is_unset(request.bootstrap_scripts):
            query['BootstrapScripts'] = request.bootstrap_scripts
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.cluster_name):
            query['ClusterName'] = request.cluster_name
        if not UtilClient.is_unset(request.cluster_type):
            query['ClusterType'] = request.cluster_type
        if not UtilClient.is_unset(request.deploy_mode):
            query['DeployMode'] = request.deploy_mode
        if not UtilClient.is_unset(request.node_attributes):
            query['NodeAttributes'] = request.node_attributes
        if not UtilClient.is_unset(request.node_groups):
            query['NodeGroups'] = request.node_groups
        if not UtilClient.is_unset(request.payment_type):
            query['PaymentType'] = request.payment_type
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.release_version):
            query['ReleaseVersion'] = request.release_version
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.security_mode):
            query['SecurityMode'] = request.security_mode
        if not UtilClient.is_unset(request.subscription_config):
            query['SubscriptionConfig'] = request.subscription_config
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateCluster',
            version='2021-03-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20210320_models.CreateClusterResponse(),
            self.call_api(params, req, runtime)
        )

    def create_cluster(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_cluster_with_options(request, runtime)

    def create_node_group_with_options(self, request, runtime):
        """
        创建节点组。
        

        @param request: CreateNodeGroupRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateNodeGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.node_group):
            query['NodeGroup'] = request.node_group
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateNodeGroup',
            version='2021-03-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20210320_models.CreateNodeGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def create_node_group(self, request):
        """
        创建节点组。
        

        @param request: CreateNodeGroupRequest

        @return: CreateNodeGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_node_group_with_options(request, runtime)

    def decrease_nodes_with_options(self, request, runtime):
        """
        缩容节点。
        

        @param request: DecreaseNodesRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DecreaseNodesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.decrease_node_count):
            query['DecreaseNodeCount'] = request.decrease_node_count
        if not UtilClient.is_unset(request.node_group_id):
            query['NodeGroupId'] = request.node_group_id
        if not UtilClient.is_unset(request.node_ids):
            query['NodeIds'] = request.node_ids
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DecreaseNodes',
            version='2021-03-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20210320_models.DecreaseNodesResponse(),
            self.call_api(params, req, runtime)
        )

    def decrease_nodes(self, request):
        """
        缩容节点。
        

        @param request: DecreaseNodesRequest

        @return: DecreaseNodesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.decrease_nodes_with_options(request, runtime)

    def delete_cluster_with_options(self, request, runtime):
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
            action='DeleteCluster',
            version='2021-03-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20210320_models.DeleteClusterResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_cluster(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_cluster_with_options(request, runtime)

    def get_auto_scaling_activity_with_options(self, request, runtime):
        """
        获取弹性伸缩活动详情。
        

        @param request: GetAutoScalingActivityRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: GetAutoScalingActivityResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.scaling_activity_id):
            query['ScalingActivityId'] = request.scaling_activity_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAutoScalingActivity',
            version='2021-03-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20210320_models.GetAutoScalingActivityResponse(),
            self.call_api(params, req, runtime)
        )

    def get_auto_scaling_activity(self, request):
        """
        获取弹性伸缩活动详情。
        

        @param request: GetAutoScalingActivityRequest

        @return: GetAutoScalingActivityResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_auto_scaling_activity_with_options(request, runtime)

    def get_auto_scaling_policy_with_options(self, request, runtime):
        """
        获取弹性伸缩策略信息。
        

        @param request: GetAutoScalingPolicyRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: GetAutoScalingPolicyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.node_group_id):
            query['NodeGroupId'] = request.node_group_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAutoScalingPolicy',
            version='2021-03-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20210320_models.GetAutoScalingPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    def get_auto_scaling_policy(self, request):
        """
        获取弹性伸缩策略信息。
        

        @param request: GetAutoScalingPolicyRequest

        @return: GetAutoScalingPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_auto_scaling_policy_with_options(request, runtime)

    def get_cluster_with_options(self, request, runtime):
        """
        调用GetCluster获取集群详情。
        

        @param request: GetClusterRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: GetClusterResponse
        """
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
            action='GetCluster',
            version='2021-03-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20210320_models.GetClusterResponse(),
            self.call_api(params, req, runtime)
        )

    def get_cluster(self, request):
        """
        调用GetCluster获取集群详情。
        

        @param request: GetClusterRequest

        @return: GetClusterResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_cluster_with_options(request, runtime)

    def get_doctor_application_with_options(self, request, runtime):
        """
        get one doctor analysis app
        

        @param request: GetDoctorApplicationRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: GetDoctorApplicationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.date_time):
            query['DateTime'] = request.date_time
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDoctorApplication',
            version='2021-03-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20210320_models.GetDoctorApplicationResponse(),
            self.call_api(params, req, runtime)
        )

    def get_doctor_application(self, request):
        """
        get one doctor analysis app
        

        @param request: GetDoctorApplicationRequest

        @return: GetDoctorApplicationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_doctor_application_with_options(request, runtime)

    def get_doctor_compute_summary_with_options(self, request, runtime):
        """
        get one specific luster engine queue by <type, name>
        

        @param request: GetDoctorComputeSummaryRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: GetDoctorComputeSummaryResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.component_info):
            query['ComponentInfo'] = request.component_info
        if not UtilClient.is_unset(request.date_time):
            query['DateTime'] = request.date_time
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDoctorComputeSummary',
            version='2021-03-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20210320_models.GetDoctorComputeSummaryResponse(),
            self.call_api(params, req, runtime)
        )

    def get_doctor_compute_summary(self, request):
        """
        get one specific luster engine queue by <type, name>
        

        @param request: GetDoctorComputeSummaryRequest

        @return: GetDoctorComputeSummaryResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_doctor_compute_summary_with_options(request, runtime)

    def get_doctor_hbase_cluster_with_options(self, request, runtime):
        """
        get Doctor HBaseCluster
        

        @param request: GetDoctorHBaseClusterRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: GetDoctorHBaseClusterResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.date_time):
            query['DateTime'] = request.date_time
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDoctorHBaseCluster',
            version='2021-03-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20210320_models.GetDoctorHBaseClusterResponse(),
            self.call_api(params, req, runtime)
        )

    def get_doctor_hbase_cluster(self, request):
        """
        get Doctor HBaseCluster
        

        @param request: GetDoctorHBaseClusterRequest

        @return: GetDoctorHBaseClusterResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_doctor_hbase_cluster_with_options(request, runtime)

    def get_doctor_hbase_region_with_options(self, request, runtime):
        """
        list Doctor HBaseRegions
        

        @param request: GetDoctorHBaseRegionRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: GetDoctorHBaseRegionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.date_time):
            query['DateTime'] = request.date_time
        if not UtilClient.is_unset(request.hbase_region_id):
            query['HbaseRegionId'] = request.hbase_region_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDoctorHBaseRegion',
            version='2021-03-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20210320_models.GetDoctorHBaseRegionResponse(),
            self.call_api(params, req, runtime)
        )

    def get_doctor_hbase_region(self, request):
        """
        list Doctor HBaseRegions
        

        @param request: GetDoctorHBaseRegionRequest

        @return: GetDoctorHBaseRegionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_doctor_hbase_region_with_options(request, runtime)

    def get_doctor_hbase_region_server_with_options(self, request, runtime):
        """
        get Doctor HBaseRegionServer
        

        @param request: GetDoctorHBaseRegionServerRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: GetDoctorHBaseRegionServerResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.date_time):
            query['DateTime'] = request.date_time
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.region_server_host):
            query['RegionServerHost'] = request.region_server_host
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDoctorHBaseRegionServer',
            version='2021-03-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20210320_models.GetDoctorHBaseRegionServerResponse(),
            self.call_api(params, req, runtime)
        )

    def get_doctor_hbase_region_server(self, request):
        """
        get Doctor HBaseRegionServer
        

        @param request: GetDoctorHBaseRegionServerRequest

        @return: GetDoctorHBaseRegionServerResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_doctor_hbase_region_server_with_options(request, runtime)

    def get_doctor_hbase_table_with_options(self, request, runtime):
        """
        get Doctor HBaseTable
        

        @param request: GetDoctorHBaseTableRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: GetDoctorHBaseTableResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.date_time):
            query['DateTime'] = request.date_time
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.table_name):
            query['TableName'] = request.table_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDoctorHBaseTable',
            version='2021-03-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20210320_models.GetDoctorHBaseTableResponse(),
            self.call_api(params, req, runtime)
        )

    def get_doctor_hbase_table(self, request):
        """
        get Doctor HBaseTable
        

        @param request: GetDoctorHBaseTableRequest

        @return: GetDoctorHBaseTableResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_doctor_hbase_table_with_options(request, runtime)

    def get_doctor_hdfscluster_with_options(self, request, runtime):
        """
        list Doctor HBaseTableRegions
        

        @param request: GetDoctorHDFSClusterRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: GetDoctorHDFSClusterResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.date_time):
            query['DateTime'] = request.date_time
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDoctorHDFSCluster',
            version='2021-03-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20210320_models.GetDoctorHDFSClusterResponse(),
            self.call_api(params, req, runtime)
        )

    def get_doctor_hdfscluster(self, request):
        """
        list Doctor HBaseTableRegions
        

        @param request: GetDoctorHDFSClusterRequest

        @return: GetDoctorHDFSClusterResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_doctor_hdfscluster_with_options(request, runtime)

    def get_doctor_hdfsdirectory_with_options(self, request, runtime):
        """
        get Doctor HDFSNode
        

        @param request: GetDoctorHDFSDirectoryRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: GetDoctorHDFSDirectoryResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.date_time):
            query['DateTime'] = request.date_time
        if not UtilClient.is_unset(request.dir_path):
            query['DirPath'] = request.dir_path
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDoctorHDFSDirectory',
            version='2021-03-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20210320_models.GetDoctorHDFSDirectoryResponse(),
            self.call_api(params, req, runtime)
        )

    def get_doctor_hdfsdirectory(self, request):
        """
        get Doctor HDFSNode
        

        @param request: GetDoctorHDFSDirectoryRequest

        @return: GetDoctorHDFSDirectoryResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_doctor_hdfsdirectory_with_options(request, runtime)

    def get_doctor_hdfsugiwith_options(self, request, runtime):
        """
        get Doctor HDFS UGI
        

        @param request: GetDoctorHDFSUGIRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: GetDoctorHDFSUGIResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.date_time):
            query['DateTime'] = request.date_time
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
            action='GetDoctorHDFSUGI',
            version='2021-03-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20210320_models.GetDoctorHDFSUGIResponse(),
            self.call_api(params, req, runtime)
        )

    def get_doctor_hdfsugi(self, request):
        """
        get Doctor HDFS UGI
        

        @param request: GetDoctorHDFSUGIRequest

        @return: GetDoctorHDFSUGIResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_doctor_hdfsugiwith_options(request, runtime)

    def get_doctor_hive_cluster_with_options(self, request, runtime):
        """
        list Doctor Hive Cluster
        

        @param request: GetDoctorHiveClusterRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: GetDoctorHiveClusterResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.date_time):
            query['DateTime'] = request.date_time
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDoctorHiveCluster',
            version='2021-03-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20210320_models.GetDoctorHiveClusterResponse(),
            self.call_api(params, req, runtime)
        )

    def get_doctor_hive_cluster(self, request):
        """
        list Doctor Hive Cluster
        

        @param request: GetDoctorHiveClusterRequest

        @return: GetDoctorHiveClusterResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_doctor_hive_cluster_with_options(request, runtime)

    def get_doctor_hive_database_with_options(self, request, runtime):
        """
        get Doctor Hive Database
        

        @param request: GetDoctorHiveDatabaseRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: GetDoctorHiveDatabaseResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.database_name):
            query['DatabaseName'] = request.database_name
        if not UtilClient.is_unset(request.date_time):
            query['DateTime'] = request.date_time
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDoctorHiveDatabase',
            version='2021-03-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20210320_models.GetDoctorHiveDatabaseResponse(),
            self.call_api(params, req, runtime)
        )

    def get_doctor_hive_database(self, request):
        """
        get Doctor Hive Database
        

        @param request: GetDoctorHiveDatabaseRequest

        @return: GetDoctorHiveDatabaseResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_doctor_hive_database_with_options(request, runtime)

    def get_doctor_hive_table_with_options(self, request, runtime):
        """
        get Doctor Hive Table
        

        @param request: GetDoctorHiveTableRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: GetDoctorHiveTableResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.date_time):
            query['DateTime'] = request.date_time
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.table_name):
            query['TableName'] = request.table_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDoctorHiveTable',
            version='2021-03-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20210320_models.GetDoctorHiveTableResponse(),
            self.call_api(params, req, runtime)
        )

    def get_doctor_hive_table(self, request):
        """
        get Doctor Hive Table
        

        @param request: GetDoctorHiveTableRequest

        @return: GetDoctorHiveTableResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_doctor_hive_table_with_options(request, runtime)

    def get_doctor_job_with_options(self, request, runtime):
        """
        Get realtime job by yarn
        

        @param request: GetDoctorJobRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: GetDoctorJobResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDoctorJob',
            version='2021-03-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20210320_models.GetDoctorJobResponse(),
            self.call_api(params, req, runtime)
        )

    def get_doctor_job(self, request):
        """
        Get realtime job by yarn
        

        @param request: GetDoctorJobRequest

        @return: GetDoctorJobResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_doctor_job_with_options(request, runtime)

    def get_doctor_report_component_summary_with_options(self, request, runtime):
        """
        get specify component's report analysis by emr doctor
        

        @param request: GetDoctorReportComponentSummaryRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: GetDoctorReportComponentSummaryResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.component_type):
            query['ComponentType'] = request.component_type
        if not UtilClient.is_unset(request.date_time):
            query['DateTime'] = request.date_time
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetDoctorReportComponentSummary',
            version='2021-03-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20210320_models.GetDoctorReportComponentSummaryResponse(),
            self.call_api(params, req, runtime)
        )

    def get_doctor_report_component_summary(self, request):
        """
        get specify component's report analysis by emr doctor
        

        @param request: GetDoctorReportComponentSummaryRequest

        @return: GetDoctorReportComponentSummaryResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_doctor_report_component_summary_with_options(request, runtime)

    def get_node_group_with_options(self, request, runtime):
        """
        获取节点组详情。
        

        @param request: GetNodeGroupRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: GetNodeGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.node_group_id):
            query['NodeGroupId'] = request.node_group_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetNodeGroup',
            version='2021-03-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20210320_models.GetNodeGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def get_node_group(self, request):
        """
        获取节点组详情。
        

        @param request: GetNodeGroupRequest

        @return: GetNodeGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_node_group_with_options(request, runtime)

    def get_operation_with_options(self, request, runtime):
        """
        获取操作详情。
        

        @param request: GetOperationRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: GetOperationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.operation_id):
            query['OperationId'] = request.operation_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetOperation',
            version='2021-03-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20210320_models.GetOperationResponse(),
            self.call_api(params, req, runtime)
        )

    def get_operation(self, request):
        """
        获取操作详情。
        

        @param request: GetOperationRequest

        @return: GetOperationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_operation_with_options(request, runtime)

    def increase_nodes_with_options(self, request, runtime):
        """
        扩容节点。
        

        @param request: IncreaseNodesRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: IncreaseNodesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_configs):
            query['ApplicationConfigs'] = request.application_configs
        if not UtilClient.is_unset(request.auto_pay_order):
            query['AutoPayOrder'] = request.auto_pay_order
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.increase_node_count):
            query['IncreaseNodeCount'] = request.increase_node_count
        if not UtilClient.is_unset(request.node_group_id):
            query['NodeGroupId'] = request.node_group_id
        if not UtilClient.is_unset(request.payment_duration):
            query['PaymentDuration'] = request.payment_duration
        if not UtilClient.is_unset(request.payment_duration_unit):
            query['PaymentDurationUnit'] = request.payment_duration_unit
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='IncreaseNodes',
            version='2021-03-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20210320_models.IncreaseNodesResponse(),
            self.call_api(params, req, runtime)
        )

    def increase_nodes(self, request):
        """
        扩容节点。
        

        @param request: IncreaseNodesRequest

        @return: IncreaseNodesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.increase_nodes_with_options(request, runtime)

    def join_resource_group_with_options(self, request, runtime):
        """
        加入资源组。
        

        @param request: JoinResourceGroupRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: JoinResourceGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='JoinResourceGroup',
            version='2021-03-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20210320_models.JoinResourceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def join_resource_group(self, request):
        """
        加入资源组。
        

        @param request: JoinResourceGroupRequest

        @return: JoinResourceGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.join_resource_group_with_options(request, runtime)

    def list_application_configs_with_options(self, request, runtime):
        """
        查询应用配置。
        

        @param request: ListApplicationConfigsRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListApplicationConfigsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_name):
            query['ApplicationName'] = request.application_name
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.config_file_name):
            query['ConfigFileName'] = request.config_file_name
        if not UtilClient.is_unset(request.config_item_key):
            query['ConfigItemKey'] = request.config_item_key
        if not UtilClient.is_unset(request.config_item_value):
            query['ConfigItemValue'] = request.config_item_value
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.node_group_id):
            query['NodeGroupId'] = request.node_group_id
        if not UtilClient.is_unset(request.node_id):
            query['NodeId'] = request.node_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListApplicationConfigs',
            version='2021-03-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20210320_models.ListApplicationConfigsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_application_configs(self, request):
        """
        查询应用配置。
        

        @param request: ListApplicationConfigsRequest

        @return: ListApplicationConfigsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_application_configs_with_options(request, runtime)

    def list_applications_with_options(self, request, runtime):
        """
        查询应用列表。
        

        @param request: ListApplicationsRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListApplicationsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_names):
            query['ApplicationNames'] = request.application_names
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListApplications',
            version='2021-03-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20210320_models.ListApplicationsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_applications(self, request):
        """
        查询应用列表。
        

        @param request: ListApplicationsRequest

        @return: ListApplicationsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_applications_with_options(request, runtime)

    def list_auto_scaling_activities_with_options(self, request, runtime):
        """
        查询弹性伸缩活动列表。
        

        @param request: ListAutoScalingActivitiesRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListAutoScalingActivitiesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.node_group_id):
            query['NodeGroupId'] = request.node_group_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.scaling_activity_states):
            query['ScalingActivityStates'] = request.scaling_activity_states
        if not UtilClient.is_unset(request.scaling_activity_type):
            query['ScalingActivityType'] = request.scaling_activity_type
        if not UtilClient.is_unset(request.scaling_rule_name):
            query['ScalingRuleName'] = request.scaling_rule_name
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAutoScalingActivities',
            version='2021-03-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20210320_models.ListAutoScalingActivitiesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_auto_scaling_activities(self, request):
        """
        查询弹性伸缩活动列表。
        

        @param request: ListAutoScalingActivitiesRequest

        @return: ListAutoScalingActivitiesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_auto_scaling_activities_with_options(request, runtime)

    def list_clusters_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_ids):
            query['ClusterIds'] = request.cluster_ids
        if not UtilClient.is_unset(request.cluster_name):
            query['ClusterName'] = request.cluster_name
        if not UtilClient.is_unset(request.cluster_states):
            query['ClusterStates'] = request.cluster_states
        if not UtilClient.is_unset(request.cluster_types):
            query['ClusterTypes'] = request.cluster_types
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.payment_types):
            query['PaymentTypes'] = request.payment_types
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
            action='ListClusters',
            version='2021-03-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20210320_models.ListClustersResponse(),
            self.call_api(params, req, runtime)
        )

    def list_clusters(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_clusters_with_options(request, runtime)

    def list_doctor_applications_with_options(self, request, runtime):
        """
        list all doctor analysis apps
        

        @param request: ListDoctorApplicationsRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListDoctorApplicationsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_ids):
            query['AppIds'] = request.app_ids
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.date_time):
            query['DateTime'] = request.date_time
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.order_by):
            query['OrderBy'] = request.order_by
        if not UtilClient.is_unset(request.order_type):
            query['OrderType'] = request.order_type
        if not UtilClient.is_unset(request.queues):
            query['Queues'] = request.queues
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.types):
            query['Types'] = request.types
        if not UtilClient.is_unset(request.users):
            query['Users'] = request.users
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDoctorApplications',
            version='2021-03-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20210320_models.ListDoctorApplicationsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_doctor_applications(self, request):
        """
        list all doctor analysis apps
        

        @param request: ListDoctorApplicationsRequest

        @return: ListDoctorApplicationsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_doctor_applications_with_options(request, runtime)

    def list_doctor_compute_summary_with_options(self, request, runtime):
        """
        list Doctor analysis result of cluster engine queue view
        

        @param request: ListDoctorComputeSummaryRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListDoctorComputeSummaryResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.component_types):
            query['ComponentTypes'] = request.component_types
        if not UtilClient.is_unset(request.date_time):
            query['DateTime'] = request.date_time
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.order_by):
            query['OrderBy'] = request.order_by
        if not UtilClient.is_unset(request.order_type):
            query['OrderType'] = request.order_type
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDoctorComputeSummary',
            version='2021-03-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20210320_models.ListDoctorComputeSummaryResponse(),
            self.call_api(params, req, runtime)
        )

    def list_doctor_compute_summary(self, request):
        """
        list Doctor analysis result of cluster engine queue view
        

        @param request: ListDoctorComputeSummaryRequest

        @return: ListDoctorComputeSummaryResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_doctor_compute_summary_with_options(request, runtime)

    def list_doctor_hbase_region_servers_with_options(self, request, runtime):
        """
        list Doctor HBaseRegionServers
        

        @param request: ListDoctorHBaseRegionServersRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListDoctorHBaseRegionServersResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.date_time):
            query['DateTime'] = request.date_time
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.order_by):
            query['OrderBy'] = request.order_by
        if not UtilClient.is_unset(request.order_type):
            query['OrderType'] = request.order_type
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.region_server_hosts):
            query['RegionServerHosts'] = request.region_server_hosts
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDoctorHBaseRegionServers',
            version='2021-03-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20210320_models.ListDoctorHBaseRegionServersResponse(),
            self.call_api(params, req, runtime)
        )

    def list_doctor_hbase_region_servers(self, request):
        """
        list Doctor HBaseRegionServers
        

        @param request: ListDoctorHBaseRegionServersRequest

        @return: ListDoctorHBaseRegionServersResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_doctor_hbase_region_servers_with_options(request, runtime)

    def list_doctor_hbase_tables_with_options(self, request, runtime):
        """
        list Doctor HBaseTables
        

        @param request: ListDoctorHBaseTablesRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListDoctorHBaseTablesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.date_time):
            query['DateTime'] = request.date_time
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.order_by):
            query['OrderBy'] = request.order_by
        if not UtilClient.is_unset(request.order_type):
            query['OrderType'] = request.order_type
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.table_names):
            query['TableNames'] = request.table_names
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDoctorHBaseTables',
            version='2021-03-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20210320_models.ListDoctorHBaseTablesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_doctor_hbase_tables(self, request):
        """
        list Doctor HBaseTables
        

        @param request: ListDoctorHBaseTablesRequest

        @return: ListDoctorHBaseTablesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_doctor_hbase_tables_with_options(request, runtime)

    def list_doctor_hdfsdirectories_with_options(self, request, runtime):
        """
        list Doctor HDFSNodes
        

        @param request: ListDoctorHDFSDirectoriesRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListDoctorHDFSDirectoriesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.date_time):
            query['DateTime'] = request.date_time
        if not UtilClient.is_unset(request.dir_path):
            query['DirPath'] = request.dir_path
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.order_by):
            query['OrderBy'] = request.order_by
        if not UtilClient.is_unset(request.order_type):
            query['OrderType'] = request.order_type
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDoctorHDFSDirectories',
            version='2021-03-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20210320_models.ListDoctorHDFSDirectoriesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_doctor_hdfsdirectories(self, request):
        """
        list Doctor HDFSNodes
        

        @param request: ListDoctorHDFSDirectoriesRequest

        @return: ListDoctorHDFSDirectoriesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_doctor_hdfsdirectories_with_options(request, runtime)

    def list_doctor_hdfsugiwith_options(self, request, runtime):
        """
        list Doctor HDFS UGIs
        

        @param request: ListDoctorHDFSUGIRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListDoctorHDFSUGIResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.date_time):
            query['DateTime'] = request.date_time
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.order_by):
            query['OrderBy'] = request.order_by
        if not UtilClient.is_unset(request.order_type):
            query['OrderType'] = request.order_type
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDoctorHDFSUGI',
            version='2021-03-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20210320_models.ListDoctorHDFSUGIResponse(),
            self.call_api(params, req, runtime)
        )

    def list_doctor_hdfsugi(self, request):
        """
        list Doctor HDFS UGIs
        

        @param request: ListDoctorHDFSUGIRequest

        @return: ListDoctorHDFSUGIResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_doctor_hdfsugiwith_options(request, runtime)

    def list_doctor_hive_databases_with_options(self, request, runtime):
        """
        list Doctor Hive Databases
        

        @param request: ListDoctorHiveDatabasesRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListDoctorHiveDatabasesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.database_names):
            query['DatabaseNames'] = request.database_names
        if not UtilClient.is_unset(request.date_time):
            query['DateTime'] = request.date_time
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.order_by):
            query['OrderBy'] = request.order_by
        if not UtilClient.is_unset(request.order_type):
            query['OrderType'] = request.order_type
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDoctorHiveDatabases',
            version='2021-03-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20210320_models.ListDoctorHiveDatabasesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_doctor_hive_databases(self, request):
        """
        list Doctor Hive Databases
        

        @param request: ListDoctorHiveDatabasesRequest

        @return: ListDoctorHiveDatabasesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_doctor_hive_databases_with_options(request, runtime)

    def list_doctor_hive_tables_with_options(self, request, runtime):
        """
        list Doctor Hive Tables
        

        @param request: ListDoctorHiveTablesRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListDoctorHiveTablesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.date_time):
            query['DateTime'] = request.date_time
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.order_by):
            query['OrderBy'] = request.order_by
        if not UtilClient.is_unset(request.order_type):
            query['OrderType'] = request.order_type
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.table_names):
            query['TableNames'] = request.table_names
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDoctorHiveTables',
            version='2021-03-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20210320_models.ListDoctorHiveTablesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_doctor_hive_tables(self, request):
        """
        list Doctor Hive Tables
        

        @param request: ListDoctorHiveTablesRequest

        @return: ListDoctorHiveTablesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_doctor_hive_tables_with_options(request, runtime)

    def list_doctor_jobs_with_options(self, request, runtime):
        """
        list realtime jobs by yarn
        

        @param request: ListDoctorJobsRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListDoctorJobsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_ids):
            query['AppIds'] = request.app_ids
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.end_range):
            query['EndRange'] = request.end_range
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.order_by):
            query['OrderBy'] = request.order_by
        if not UtilClient.is_unset(request.order_type):
            query['OrderType'] = request.order_type
        if not UtilClient.is_unset(request.queues):
            query['Queues'] = request.queues
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.start_range):
            query['StartRange'] = request.start_range
        if not UtilClient.is_unset(request.types):
            query['Types'] = request.types
        if not UtilClient.is_unset(request.users):
            query['Users'] = request.users
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDoctorJobs',
            version='2021-03-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20210320_models.ListDoctorJobsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_doctor_jobs(self, request):
        """
        list realtime jobs by yarn
        

        @param request: ListDoctorJobsRequest

        @return: ListDoctorJobsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_doctor_jobs_with_options(request, runtime)

    def list_doctor_jobs_stats_with_options(self, request, runtime):
        """
        list stats groupBy jobs by yarn
        

        @param request: ListDoctorJobsStatsRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListDoctorJobsStatsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.end_range):
            query['EndRange'] = request.end_range
        if not UtilClient.is_unset(request.group_by):
            query['GroupBy'] = request.group_by
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.order_by):
            query['OrderBy'] = request.order_by
        if not UtilClient.is_unset(request.order_type):
            query['OrderType'] = request.order_type
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.start_range):
            query['StartRange'] = request.start_range
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDoctorJobsStats',
            version='2021-03-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20210320_models.ListDoctorJobsStatsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_doctor_jobs_stats(self, request):
        """
        list stats groupBy jobs by yarn
        

        @param request: ListDoctorJobsStatsRequest

        @return: ListDoctorJobsStatsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_doctor_jobs_stats_with_options(request, runtime)

    def list_doctor_reports_with_options(self, request, runtime):
        """
        list all reports analysis by emr doctor
        

        @param request: ListDoctorReportsRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListDoctorReportsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDoctorReports',
            version='2021-03-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20210320_models.ListDoctorReportsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_doctor_reports(self, request):
        """
        list all reports analysis by emr doctor
        

        @param request: ListDoctorReportsRequest

        @return: ListDoctorReportsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_doctor_reports_with_options(request, runtime)

    def list_instance_types_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.cluster_type):
            query['ClusterType'] = request.cluster_type
        if not UtilClient.is_unset(request.deploy_mode):
            query['DeployMode'] = request.deploy_mode
        if not UtilClient.is_unset(request.instance_type):
            query['InstanceType'] = request.instance_type
        if not UtilClient.is_unset(request.is_modification):
            query['IsModification'] = request.is_modification
        if not UtilClient.is_unset(request.node_group_id):
            query['NodeGroupId'] = request.node_group_id
        if not UtilClient.is_unset(request.node_group_type):
            query['NodeGroupType'] = request.node_group_type
        if not UtilClient.is_unset(request.payment_type):
            query['PaymentType'] = request.payment_type
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.release_version):
            query['ReleaseVersion'] = request.release_version
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListInstanceTypes',
            version='2021-03-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20210320_models.ListInstanceTypesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_instance_types(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_instance_types_with_options(request, runtime)

    def list_node_groups_with_options(self, request, runtime):
        """
        查询节点组。
        

        @param request: ListNodeGroupsRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListNodeGroupsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.node_group_ids):
            query['NodeGroupIds'] = request.node_group_ids
        if not UtilClient.is_unset(request.node_group_names):
            query['NodeGroupNames'] = request.node_group_names
        if not UtilClient.is_unset(request.node_group_states):
            query['NodeGroupStates'] = request.node_group_states
        if not UtilClient.is_unset(request.node_group_types):
            query['NodeGroupTypes'] = request.node_group_types
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListNodeGroups',
            version='2021-03-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20210320_models.ListNodeGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_node_groups(self, request):
        """
        查询节点组。
        

        @param request: ListNodeGroupsRequest

        @return: ListNodeGroupsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_node_groups_with_options(request, runtime)

    def list_nodes_with_options(self, request, runtime):
        """
        查询节点。
        

        @param request: ListNodesRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListNodesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.node_group_ids):
            query['NodeGroupIds'] = request.node_group_ids
        if not UtilClient.is_unset(request.node_ids):
            query['NodeIds'] = request.node_ids
        if not UtilClient.is_unset(request.node_names):
            query['NodeNames'] = request.node_names
        if not UtilClient.is_unset(request.node_states):
            query['NodeStates'] = request.node_states
        if not UtilClient.is_unset(request.private_ips):
            query['PrivateIps'] = request.private_ips
        if not UtilClient.is_unset(request.public_ips):
            query['PublicIps'] = request.public_ips
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListNodes',
            version='2021-03-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20210320_models.ListNodesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_nodes(self, request):
        """
        查询节点。
        

        @param request: ListNodesRequest

        @return: ListNodesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_nodes_with_options(request, runtime)

    def list_release_versions_with_options(self, request, runtime):
        """
        查询主版本。
        

        @param request: ListReleaseVersionsRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListReleaseVersionsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_type):
            query['ClusterType'] = request.cluster_type
        if not UtilClient.is_unset(request.iaas_type):
            query['IaasType'] = request.iaas_type
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListReleaseVersions',
            version='2021-03-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20210320_models.ListReleaseVersionsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_release_versions(self, request):
        """
        查询主版本。
        

        @param request: ListReleaseVersionsRequest

        @return: ListReleaseVersionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_release_versions_with_options(request, runtime)

    def list_tag_resources_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_ids):
            query['ResourceIds'] = request.resource_ids
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTagResources',
            version='2021-03-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20210320_models.ListTagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_tag_resources(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_tag_resources_with_options(request, runtime)

    def put_auto_scaling_policy_with_options(self, request, runtime):
        """
        设置弹性伸缩规则。
        

        @param request: PutAutoScalingPolicyRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: PutAutoScalingPolicyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.constraints):
            query['Constraints'] = request.constraints
        if not UtilClient.is_unset(request.node_group_id):
            query['NodeGroupId'] = request.node_group_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.scaling_rules):
            query['ScalingRules'] = request.scaling_rules
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PutAutoScalingPolicy',
            version='2021-03-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20210320_models.PutAutoScalingPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    def put_auto_scaling_policy(self, request):
        """
        设置弹性伸缩规则。
        

        @param request: PutAutoScalingPolicyRequest

        @return: PutAutoScalingPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.put_auto_scaling_policy_with_options(request, runtime)

    def remove_auto_scaling_policy_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.node_group_id):
            query['NodeGroupId'] = request.node_group_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemoveAutoScalingPolicy',
            version='2021-03-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20210320_models.RemoveAutoScalingPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    def remove_auto_scaling_policy(self, request):
        runtime = util_models.RuntimeOptions()
        return self.remove_auto_scaling_policy_with_options(request, runtime)

    def run_application_action_with_options(self, request, runtime):
        """
        执行应用操作。
        

        @param request: RunApplicationActionRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: RunApplicationActionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.action_name):
            query['ActionName'] = request.action_name
        if not UtilClient.is_unset(request.batch_size):
            query['BatchSize'] = request.batch_size
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.component_instance_selector):
            query['ComponentInstanceSelector'] = request.component_instance_selector
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.execute_strategy):
            query['ExecuteStrategy'] = request.execute_strategy
        if not UtilClient.is_unset(request.interval):
            query['Interval'] = request.interval
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.rolling_execute):
            query['RollingExecute'] = request.rolling_execute
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RunApplicationAction',
            version='2021-03-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20210320_models.RunApplicationActionResponse(),
            self.call_api(params, req, runtime)
        )

    def run_application_action(self, request):
        """
        执行应用操作。
        

        @param request: RunApplicationActionRequest

        @return: RunApplicationActionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.run_application_action_with_options(request, runtime)

    def tag_resources_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_ids):
            query['ResourceIds'] = request.resource_ids
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TagResources',
            version='2021-03-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20210320_models.TagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    def tag_resources(self, request):
        runtime = util_models.RuntimeOptions()
        return self.tag_resources_with_options(request, runtime)

    def untag_resources_with_options(self, request, runtime):
        """
        删除指定资源标签。
        

        @param request: UntagResourcesRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: UntagResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.all):
            query['All'] = request.all
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_ids):
            query['ResourceIds'] = request.resource_ids
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag_keys):
            query['TagKeys'] = request.tag_keys
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UntagResources',
            version='2021-03-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20210320_models.UntagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    def untag_resources(self, request):
        """
        删除指定资源标签。
        

        @param request: UntagResourcesRequest

        @return: UntagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.untag_resources_with_options(request, runtime)

    def update_application_configs_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.application_configs):
            query['ApplicationConfigs'] = request.application_configs
        if not UtilClient.is_unset(request.application_name):
            query['ApplicationName'] = request.application_name
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.config_action):
            query['ConfigAction'] = request.config_action
        if not UtilClient.is_unset(request.config_scope):
            query['ConfigScope'] = request.config_scope
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.node_group_id):
            query['NodeGroupId'] = request.node_group_id
        if not UtilClient.is_unset(request.node_id):
            query['NodeId'] = request.node_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateApplicationConfigs',
            version='2021-03-20',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            emr_20210320_models.UpdateApplicationConfigsResponse(),
            self.call_api(params, req, runtime)
        )

    def update_application_configs(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_application_configs_with_options(request, runtime)
