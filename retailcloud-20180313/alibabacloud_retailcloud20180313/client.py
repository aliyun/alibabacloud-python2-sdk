# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_retailcloud20180313 import models as retailcloud_20180313_models
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
            'ap-northeast-1': 'retailcloud.aliyuncs.com',
            'ap-northeast-2-pop': 'retailcloud.aliyuncs.com',
            'ap-south-1': 'retailcloud.aliyuncs.com',
            'ap-southeast-1': 'retailcloud.aliyuncs.com',
            'ap-southeast-2': 'retailcloud.aliyuncs.com',
            'ap-southeast-3': 'retailcloud.aliyuncs.com',
            'ap-southeast-5': 'retailcloud.aliyuncs.com',
            'cn-beijing': 'retailcloud.aliyuncs.com',
            'cn-beijing-finance-1': 'retailcloud.aliyuncs.com',
            'cn-beijing-finance-pop': 'retailcloud.aliyuncs.com',
            'cn-beijing-gov-1': 'retailcloud.aliyuncs.com',
            'cn-beijing-nu16-b01': 'retailcloud.aliyuncs.com',
            'cn-chengdu': 'retailcloud.aliyuncs.com',
            'cn-edge-1': 'retailcloud.aliyuncs.com',
            'cn-fujian': 'retailcloud.aliyuncs.com',
            'cn-haidian-cm12-c01': 'retailcloud.aliyuncs.com',
            'cn-hangzhou': 'retailcloud.aliyuncs.com',
            'cn-hangzhou-bj-b01': 'retailcloud.aliyuncs.com',
            'cn-hangzhou-finance': 'retailcloud.aliyuncs.com',
            'cn-hangzhou-internal-prod-1': 'retailcloud.aliyuncs.com',
            'cn-hangzhou-internal-test-1': 'retailcloud.aliyuncs.com',
            'cn-hangzhou-internal-test-2': 'retailcloud.aliyuncs.com',
            'cn-hangzhou-internal-test-3': 'retailcloud.aliyuncs.com',
            'cn-hangzhou-test-306': 'retailcloud.aliyuncs.com',
            'cn-hongkong': 'retailcloud.aliyuncs.com',
            'cn-hongkong-finance-pop': 'retailcloud.aliyuncs.com',
            'cn-huhehaote': 'retailcloud.aliyuncs.com',
            'cn-north-2-gov-1': 'retailcloud.aliyuncs.com',
            'cn-qingdao': 'retailcloud.aliyuncs.com',
            'cn-qingdao-nebula': 'retailcloud.aliyuncs.com',
            'cn-shanghai': 'retailcloud.aliyuncs.com',
            'cn-shanghai-et15-b01': 'retailcloud.aliyuncs.com',
            'cn-shanghai-et2-b01': 'retailcloud.aliyuncs.com',
            'cn-shanghai-finance-1': 'retailcloud.aliyuncs.com',
            'cn-shanghai-inner': 'retailcloud.aliyuncs.com',
            'cn-shanghai-internal-test-1': 'retailcloud.aliyuncs.com',
            'cn-shenzhen': 'retailcloud.aliyuncs.com',
            'cn-shenzhen-finance-1': 'retailcloud.aliyuncs.com',
            'cn-shenzhen-inner': 'retailcloud.aliyuncs.com',
            'cn-shenzhen-st4-d01': 'retailcloud.aliyuncs.com',
            'cn-shenzhen-su18-b01': 'retailcloud.aliyuncs.com',
            'cn-wuhan': 'retailcloud.aliyuncs.com',
            'cn-yushanfang': 'retailcloud.aliyuncs.com',
            'cn-zhangbei-na61-b01': 'retailcloud.aliyuncs.com',
            'cn-zhangjiakou': 'retailcloud.aliyuncs.com',
            'cn-zhangjiakou-na62-a01': 'retailcloud.aliyuncs.com',
            'cn-zhengzhou-nebula-1': 'retailcloud.aliyuncs.com',
            'eu-central-1': 'retailcloud.aliyuncs.com',
            'eu-west-1': 'retailcloud.aliyuncs.com',
            'eu-west-1-oxs': 'retailcloud.aliyuncs.com',
            'me-east-1': 'retailcloud.aliyuncs.com',
            'rus-west-1-pop': 'retailcloud.aliyuncs.com',
            'us-east-1': 'retailcloud.aliyuncs.com',
            'us-west-1': 'retailcloud.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('retailcloud', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def add_cluster_node_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_instance_id):
            query['ClusterInstanceId'] = request.cluster_instance_id
        if not UtilClient.is_unset(request.ecs_instance_id_list):
            query['EcsInstanceIdList'] = request.ecs_instance_id_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddClusterNode',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.AddClusterNodeResponse(),
            self.call_api(params, req, runtime)
        )

    def add_cluster_node(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_cluster_node_with_options(request, runtime)

    def allocate_pod_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.env_id):
            query['EnvId'] = request.env_id
        if not UtilClient.is_unset(request.request_id):
            query['RequestId'] = request.request_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AllocatePodConfig',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.AllocatePodConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def allocate_pod_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.allocate_pod_config_with_options(request, runtime)

    def batch_add_servers_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.sign):
            query['Sign'] = request.sign
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BatchAddServers',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.BatchAddServersResponse(),
            self.call_api(params, req, runtime)
        )

    def batch_add_servers(self, request):
        runtime = util_models.RuntimeOptions()
        return self.batch_add_servers_with_options(request, runtime)

    def bind_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.biz_code):
            query['BizCode'] = request.biz_code
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BindGroup',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.BindGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def bind_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.bind_group_with_options(request, runtime)

    def bind_node_label_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.label_key):
            query['LabelKey'] = request.label_key
        if not UtilClient.is_unset(request.label_value):
            query['LabelValue'] = request.label_value
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BindNodeLabel',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.BindNodeLabelResponse(),
            self.call_api(params, req, runtime)
        )

    def bind_node_label(self, request):
        runtime = util_models.RuntimeOptions()
        return self.bind_node_label_with_options(request, runtime)

    def close_deploy_order_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.deploy_order_id):
            query['DeployOrderId'] = request.deploy_order_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CloseDeployOrder',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.CloseDeployOrderResponse(),
            self.call_api(params, req, runtime)
        )

    def close_deploy_order(self, request):
        runtime = util_models.RuntimeOptions()
        return self.close_deploy_order_with_options(request, runtime)

    def create_account_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.account_name):
            body['AccountName'] = request.account_name
        if not UtilClient.is_unset(request.account_password):
            body['AccountPassword'] = request.account_password
        if not UtilClient.is_unset(request.account_type):
            body['AccountType'] = request.account_type
        if not UtilClient.is_unset(request.db_instance_id):
            body['DbInstanceId'] = request.db_instance_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateAccount',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.CreateAccountResponse(),
            self.call_api(params, req, runtime)
        )

    def create_account(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_account_with_options(request, runtime)

    def create_app_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.biz_code):
            body['BizCode'] = request.biz_code
        if not UtilClient.is_unset(request.biz_title):
            body['BizTitle'] = request.biz_title
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.group_name):
            body['GroupName'] = request.group_name
        if not UtilClient.is_unset(request.language):
            body['Language'] = request.language
        if not UtilClient.is_unset(request.middle_ware_id_list):
            body['MiddleWareIdList'] = request.middle_ware_id_list
        if not UtilClient.is_unset(request.namespace):
            body['Namespace'] = request.namespace
        if not UtilClient.is_unset(request.operating_system):
            body['OperatingSystem'] = request.operating_system
        if not UtilClient.is_unset(request.service_type):
            body['ServiceType'] = request.service_type
        if not UtilClient.is_unset(request.state_type):
            body['StateType'] = request.state_type
        if not UtilClient.is_unset(request.title):
            body['Title'] = request.title
        if not UtilClient.is_unset(request.user_roles):
            body['UserRoles'] = request.user_roles
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateApp',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.CreateAppResponse(),
            self.call_api(params, req, runtime)
        )

    def create_app(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_app_with_options(request, runtime)

    def create_app_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.biz_code):
            body['BizCode'] = request.biz_code
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateAppGroup',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.CreateAppGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def create_app_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_app_group_with_options(request, runtime)

    def create_app_monitors_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.alarm_template_id):
            query['AlarmTemplateId'] = request.alarm_template_id
        if not UtilClient.is_unset(request.env_type):
            query['EnvType'] = request.env_type
        if not UtilClient.is_unset(request.main_user_id):
            query['MainUserId'] = request.main_user_id
        if not UtilClient.is_unset(request.silence_time):
            query['SilenceTime'] = request.silence_time
        body = {}
        if not UtilClient.is_unset(request.app_ids):
            body['AppIds'] = request.app_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateAppMonitors',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.CreateAppMonitorsResponse(),
            self.call_api(params, req, runtime)
        )

    def create_app_monitors(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_app_monitors_with_options(request, runtime)

    def create_app_resource_alloc_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_env_id):
            query['AppEnvId'] = request.app_env_id
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateAppResourceAlloc',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.CreateAppResourceAllocResponse(),
            self.call_api(params, req, runtime)
        )

    def create_app_resource_alloc(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_app_resource_alloc_with_options(request, runtime)

    def create_cluster_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.business_code):
            query['BusinessCode'] = request.business_code
        if not UtilClient.is_unset(request.cloud_monitor_flags):
            query['CloudMonitorFlags'] = request.cloud_monitor_flags
        if not UtilClient.is_unset(request.cluster_env_type):
            query['ClusterEnvType'] = request.cluster_env_type
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.cluster_title):
            query['ClusterTitle'] = request.cluster_title
        if not UtilClient.is_unset(request.cluster_type):
            query['ClusterType'] = request.cluster_type
        if not UtilClient.is_unset(request.create_with_arms_integration):
            query['CreateWithArmsIntegration'] = request.create_with_arms_integration
        if not UtilClient.is_unset(request.create_with_log_integration):
            query['CreateWithLogIntegration'] = request.create_with_log_integration
        if not UtilClient.is_unset(request.key_pair):
            query['KeyPair'] = request.key_pair
        if not UtilClient.is_unset(request.net_plug):
            query['NetPlug'] = request.net_plug
        if not UtilClient.is_unset(request.password):
            query['Password'] = request.password
        if not UtilClient.is_unset(request.pod_cidr):
            query['PodCIDR'] = request.pod_cidr
        if not UtilClient.is_unset(request.private_zone):
            query['PrivateZone'] = request.private_zone
        if not UtilClient.is_unset(request.public_slb):
            query['PublicSlb'] = request.public_slb
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.region_name):
            query['RegionName'] = request.region_name
        if not UtilClient.is_unset(request.service_cidr):
            query['ServiceCIDR'] = request.service_cidr
        if not UtilClient.is_unset(request.snat_entry):
            query['SnatEntry'] = request.snat_entry
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        if not UtilClient.is_unset(request.vswitchids):
            query['Vswitchids'] = request.vswitchids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateCluster',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.CreateClusterResponse(),
            self.call_api(params, req, runtime)
        )

    def create_cluster(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_cluster_with_options(request, runtime)

    def create_db_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.character_set_name):
            body['CharacterSetName'] = request.character_set_name
        if not UtilClient.is_unset(request.db_description):
            body['DbDescription'] = request.db_description
        if not UtilClient.is_unset(request.db_instance_id):
            body['DbInstanceId'] = request.db_instance_id
        if not UtilClient.is_unset(request.db_name):
            body['DbName'] = request.db_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateDb',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.CreateDbResponse(),
            self.call_api(params, req, runtime)
        )

    def create_db(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_db_with_options(request, runtime)

    def create_deploy_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.code_path):
            query['CodePath'] = request.code_path
        if not UtilClient.is_unset(request.config_map):
            query['ConfigMap'] = request.config_map
        if not UtilClient.is_unset(request.config_map_list):
            query['ConfigMapList'] = request.config_map_list
        if not UtilClient.is_unset(request.cron_job):
            query['CronJob'] = request.cron_job
        if not UtilClient.is_unset(request.deployment):
            query['Deployment'] = request.deployment
        if not UtilClient.is_unset(request.env_type):
            query['EnvType'] = request.env_type
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.secret_list):
            query['SecretList'] = request.secret_list
        if not UtilClient.is_unset(request.stateful_set):
            query['StatefulSet'] = request.stateful_set
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDeployConfig',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.CreateDeployConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def create_deploy_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_deploy_config_with_options(request, runtime)

    def create_eci_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_env_id):
            query['AppEnvId'] = request.app_env_id
        if not UtilClient.is_unset(request.eip_bandwidth):
            query['EipBandwidth'] = request.eip_bandwidth
        if not UtilClient.is_unset(request.enable_eci_schedule_policy):
            query['EnableEciSchedulePolicy'] = request.enable_eci_schedule_policy
        if not UtilClient.is_unset(request.mirror_cache):
            query['MirrorCache'] = request.mirror_cache
        if not UtilClient.is_unset(request.normal_instance_limit):
            query['NormalInstanceLimit'] = request.normal_instance_limit
        if not UtilClient.is_unset(request.schedule_virtual_node):
            query['ScheduleVirtualNode'] = request.schedule_virtual_node
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateEciConfig',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.CreateEciConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def create_eci_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_eci_config_with_options(request, runtime)

    def create_environment_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.app_schema_id):
            query['AppSchemaId'] = request.app_schema_id
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.env_name):
            query['EnvName'] = request.env_name
        if not UtilClient.is_unset(request.env_type):
            query['EnvType'] = request.env_type
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        if not UtilClient.is_unset(request.replicas):
            query['Replicas'] = request.replicas
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateEnvironment',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.CreateEnvironmentResponse(),
            self.call_api(params, req, runtime)
        )

    def create_environment(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_environment_with_options(request, runtime)

    def create_node_label_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.label_key):
            query['LabelKey'] = request.label_key
        if not UtilClient.is_unset(request.label_value):
            query['LabelValue'] = request.label_value
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateNodeLabel',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.CreateNodeLabelResponse(),
            self.call_api(params, req, runtime)
        )

    def create_node_label(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_node_label_with_options(request, runtime)

    def create_persistent_volume_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.access_modes):
            body['AccessModes'] = request.access_modes
        if not UtilClient.is_unset(request.capacity):
            body['Capacity'] = request.capacity
        if not UtilClient.is_unset(request.cluster_instance_id):
            body['ClusterInstanceId'] = request.cluster_instance_id
        if not UtilClient.is_unset(request.mount_dir):
            body['MountDir'] = request.mount_dir
        if not UtilClient.is_unset(request.mount_target_domain):
            body['MountTargetDomain'] = request.mount_target_domain
        if not UtilClient.is_unset(request.nfsversion):
            body['NFSVersion'] = request.nfsversion
        if not UtilClient.is_unset(request.name):
            body['Name'] = request.name
        if not UtilClient.is_unset(request.nas_type):
            body['NasType'] = request.nas_type
        if not UtilClient.is_unset(request.reclaim_policy):
            body['ReclaimPolicy'] = request.reclaim_policy
        if not UtilClient.is_unset(request.storage_class):
            body['StorageClass'] = request.storage_class
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreatePersistentVolume',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.CreatePersistentVolumeResponse(),
            self.call_api(params, req, runtime)
        )

    def create_persistent_volume(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_persistent_volume_with_options(request, runtime)

    def create_persistent_volume_claim_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_modes):
            query['AccessModes'] = request.access_modes
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.capacity):
            query['Capacity'] = request.capacity
        if not UtilClient.is_unset(request.env_id):
            query['EnvId'] = request.env_id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.storage_class):
            query['StorageClass'] = request.storage_class
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreatePersistentVolumeClaim',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.CreatePersistentVolumeClaimResponse(),
            self.call_api(params, req, runtime)
        )

    def create_persistent_volume_claim(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_persistent_volume_claim_with_options(request, runtime)

    def create_service_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.env_id):
            query['EnvId'] = request.env_id
        if not UtilClient.is_unset(request.headless):
            query['Headless'] = request.headless
        if not UtilClient.is_unset(request.k_8s_service_id):
            query['K8sServiceId'] = request.k_8s_service_id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.service_type):
            query['ServiceType'] = request.service_type
        body = {}
        if not UtilClient.is_unset(request.port_mappings):
            body['PortMappings'] = request.port_mappings
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateService',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.CreateServiceResponse(),
            self.call_api(params, req, runtime)
        )

    def create_service(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_service_with_options(request, runtime)

    def create_slb_apwith_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cookie_timeout):
            query['CookieTimeout'] = request.cookie_timeout
        if not UtilClient.is_unset(request.env_id):
            query['EnvId'] = request.env_id
        if not UtilClient.is_unset(request.established_timeout):
            query['EstablishedTimeout'] = request.established_timeout
        if not UtilClient.is_unset(request.listener_port):
            query['ListenerPort'] = request.listener_port
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.protocol):
            query['Protocol'] = request.protocol
        if not UtilClient.is_unset(request.real_server_port):
            query['RealServerPort'] = request.real_server_port
        if not UtilClient.is_unset(request.slb_id):
            query['SlbId'] = request.slb_id
        if not UtilClient.is_unset(request.ssl_cert_id):
            query['SslCertId'] = request.ssl_cert_id
        if not UtilClient.is_unset(request.sticky_session):
            query['StickySession'] = request.sticky_session
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateSlbAP',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.CreateSlbAPResponse(),
            self.call_api(params, req, runtime)
        )

    def create_slb_ap(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_slb_apwith_options(request, runtime)

    def delete_app_detail_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteAppDetail',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.DeleteAppDetailResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_app_detail(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_app_detail_with_options(request, runtime)

    def delete_app_environment_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.env_id):
            query['EnvId'] = request.env_id
        if not UtilClient.is_unset(request.force):
            query['Force'] = request.force
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteAppEnvironment',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.DeleteAppEnvironmentResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_app_environment(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_app_environment_with_options(request, runtime)

    def delete_app_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.force):
            query['Force'] = request.force
        if not UtilClient.is_unset(request.group_id):
            query['GroupId'] = request.group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteAppGroup',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.DeleteAppGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_app_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_app_group_with_options(request, runtime)

    def delete_app_resource_alloc_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_env_id):
            query['AppEnvId'] = request.app_env_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteAppResourceAlloc',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.DeleteAppResourceAllocResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_app_resource_alloc(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_app_resource_alloc_with_options(request, runtime)

    def delete_cluster_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_instance_id):
            query['ClusterInstanceId'] = request.cluster_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteCluster',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.DeleteClusterResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_cluster(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_cluster_with_options(request, runtime)

    def delete_database_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.dbinstance_id):
            body['DBInstanceId'] = request.dbinstance_id
        if not UtilClient.is_unset(request.dbname):
            body['DBName'] = request.dbname
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteDatabase',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.DeleteDatabaseResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_database(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_database_with_options(request, runtime)

    def delete_deploy_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.schema_id):
            query['SchemaId'] = request.schema_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDeployConfig',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.DeleteDeployConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_deploy_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_deploy_config_with_options(request, runtime)

    def delete_node_label_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.force):
            query['Force'] = request.force
        if not UtilClient.is_unset(request.label_key):
            query['LabelKey'] = request.label_key
        if not UtilClient.is_unset(request.label_value):
            query['LabelValue'] = request.label_value
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteNodeLabel',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.DeleteNodeLabelResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_node_label(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_node_label_with_options(request, runtime)

    def delete_persistent_volume_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.cluster_instance_id):
            body['ClusterInstanceId'] = request.cluster_instance_id
        if not UtilClient.is_unset(request.persistent_volume_name):
            body['PersistentVolumeName'] = request.persistent_volume_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeletePersistentVolume',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.DeletePersistentVolumeResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_persistent_volume(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_persistent_volume_with_options(request, runtime)

    def delete_persistent_volume_claim_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.env_id):
            query['EnvId'] = request.env_id
        if not UtilClient.is_unset(request.persistent_volume_claim_name):
            query['PersistentVolumeClaimName'] = request.persistent_volume_claim_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeletePersistentVolumeClaim',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.DeletePersistentVolumeClaimResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_persistent_volume_claim(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_persistent_volume_claim_with_options(request, runtime)

    def delete_rds_account_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.account_name):
            body['AccountName'] = request.account_name
        if not UtilClient.is_unset(request.db_instance_id):
            body['DbInstanceId'] = request.db_instance_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteRdsAccount',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.DeleteRdsAccountResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_rds_account(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_rds_account_with_options(request, runtime)

    def delete_service_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.service_id):
            query['ServiceId'] = request.service_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteService',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.DeleteServiceResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_service(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_service_with_options(request, runtime)

    def delete_slb_apwith_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.slb_apid):
            query['SlbAPId'] = request.slb_apid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteSlbAP',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.DeleteSlbAPResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_slb_ap(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_slb_apwith_options(request, runtime)

    def deploy_app_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.arms_flag):
            query['ArmsFlag'] = request.arms_flag
        if not UtilClient.is_unset(request.container_image_list):
            query['ContainerImageList'] = request.container_image_list
        if not UtilClient.is_unset(request.default_packet_of_app_group):
            query['DefaultPacketOfAppGroup'] = request.default_packet_of_app_group
        if not UtilClient.is_unset(request.deploy_packet_id):
            query['DeployPacketId'] = request.deploy_packet_id
        if not UtilClient.is_unset(request.deploy_packet_url):
            query['DeployPacketUrl'] = request.deploy_packet_url
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.env_id):
            query['EnvId'] = request.env_id
        if not UtilClient.is_unset(request.init_container_image_list):
            query['InitContainerImageList'] = request.init_container_image_list
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.pause_type):
            query['PauseType'] = request.pause_type
        if not UtilClient.is_unset(request.total_partitions):
            query['TotalPartitions'] = request.total_partitions
        if not UtilClient.is_unset(request.update_strategy_type):
            query['UpdateStrategyType'] = request.update_strategy_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeployApp',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.DeployAppResponse(),
            self.call_api(params, req, runtime)
        )

    def deploy_app(self, request):
        runtime = util_models.RuntimeOptions()
        return self.deploy_app_with_options(request, runtime)

    def describe_app_detail_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAppDetail',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.DescribeAppDetailResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_app_detail(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_app_detail_with_options(request, runtime)

    def describe_app_env_deploy_baseline_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.env_id):
            query['EnvId'] = request.env_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAppEnvDeployBaseline',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.DescribeAppEnvDeployBaselineResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_app_env_deploy_baseline(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_app_env_deploy_baseline_with_options(request, runtime)

    def describe_app_environment_detail_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAppEnvironmentDetail',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.DescribeAppEnvironmentDetailResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_app_environment_detail(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_app_environment_detail_with_options(request, runtime)

    def describe_app_group_deploy_setting_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_group_id):
            query['AppGroupId'] = request.app_group_id
        if not UtilClient.is_unset(request.env_type):
            query['EnvType'] = request.env_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAppGroupDeploySetting',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.DescribeAppGroupDeploySettingResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_app_group_deploy_setting(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_app_group_deploy_setting_with_options(request, runtime)

    def describe_app_monitor_metric_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.deploy_order_id):
            query['DeployOrderId'] = request.deploy_order_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.env_id):
            query['EnvId'] = request.env_id
        if not UtilClient.is_unset(request.metric):
            query['Metric'] = request.metric
        if not UtilClient.is_unset(request.pod_name):
            query['PodName'] = request.pod_name
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAppMonitorMetric',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.DescribeAppMonitorMetricResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_app_monitor_metric(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_app_monitor_metric_with_options(request, runtime)

    def describe_app_resource_alloc_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAppResourceAlloc',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.DescribeAppResourceAllocResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_app_resource_alloc(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_app_resource_alloc_with_options(request, runtime)

    def describe_cluster_detail_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_instance_id):
            query['ClusterInstanceId'] = request.cluster_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeClusterDetail',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.DescribeClusterDetailResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_cluster_detail(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_cluster_detail_with_options(request, runtime)

    def describe_databases_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDatabases',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.DescribeDatabasesResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_databases(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_databases_with_options(request, runtime)

    def describe_deploy_order_detail_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.deploy_order_id):
            query['DeployOrderId'] = request.deploy_order_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDeployOrderDetail',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.DescribeDeployOrderDetailResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_deploy_order_detail(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_deploy_order_detail_with_options(request, runtime)

    def describe_eci_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeEciConfig',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.DescribeEciConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_eci_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_eci_config_with_options(request, runtime)

    def describe_event_monitor_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.end_time):
            query['EndTime'] = request.end_time
        if not UtilClient.is_unset(request.env_id):
            query['EnvId'] = request.env_id
        if not UtilClient.is_unset(request.event_level):
            query['EventLevel'] = request.event_level
        if not UtilClient.is_unset(request.event_type):
            query['EventType'] = request.event_type
        if not UtilClient.is_unset(request.page_num):
            query['PageNum'] = request.page_num
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.pod_name):
            query['PodName'] = request.pod_name
        if not UtilClient.is_unset(request.start_time):
            query['StartTime'] = request.start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeEventMonitorList',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.DescribeEventMonitorListResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_event_monitor_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_event_monitor_list_with_options(request, runtime)

    def describe_job_log_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeJobLog',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.DescribeJobLogResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_job_log(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_job_log_with_options(request, runtime)

    def describe_pod_container_log_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.env_id):
            query['EnvId'] = request.env_id
        if not UtilClient.is_unset(request.line):
            query['Line'] = request.line
        if not UtilClient.is_unset(request.pod_name):
            query['PodName'] = request.pod_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePodContainerLogList',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.DescribePodContainerLogListResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_pod_container_log_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_pod_container_log_list_with_options(request, runtime)

    def describe_pod_events_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_inst_id):
            query['AppInstId'] = request.app_inst_id
        if not UtilClient.is_unset(request.deploy_order_id):
            query['DeployOrderId'] = request.deploy_order_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribePodEvents',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.DescribePodEventsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_pod_events(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_pod_events_with_options(request, runtime)

    def describe_pod_log_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_inst_id):
            body['AppInstId'] = request.app_inst_id
        if not UtilClient.is_unset(request.deploy_order_id):
            body['DeployOrderId'] = request.deploy_order_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribePodLog',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.DescribePodLogResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_pod_log(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_pod_log_with_options(request, runtime)

    def describe_rds_accounts_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRdsAccounts',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.DescribeRdsAccountsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_rds_accounts(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_rds_accounts_with_options(request, runtime)

    def describe_service_detail_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.service_id):
            query['ServiceId'] = request.service_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeServiceDetail',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.DescribeServiceDetailResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_service_detail(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_service_detail_with_options(request, runtime)

    def describe_slb_apdetail_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.slb_apid):
            query['SlbAPId'] = request.slb_apid
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSlbAPDetail',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.DescribeSlbAPDetailResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_slb_apdetail(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_slb_apdetail_with_options(request, runtime)

    def get_inst_trans_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.aliyun_commodity_code):
            body['aliyunCommodityCode'] = request.aliyun_commodity_code
        if not UtilClient.is_unset(request.aliyun_equip_id):
            body['aliyunEquipId'] = request.aliyun_equip_id
        if not UtilClient.is_unset(request.aliyun_uid):
            body['aliyunUid'] = request.aliyun_uid
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetInstTransInfo',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.GetInstTransInfoResponse(),
            self.call_api(params, req, runtime)
        )

    def get_inst_trans_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_inst_trans_info_with_options(request, runtime)

    def get_rds_back_up_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.backup_id):
            body['BackupId'] = request.backup_id
        if not UtilClient.is_unset(request.backup_type):
            body['BackupType'] = request.backup_type
        if not UtilClient.is_unset(request.db_instance_id):
            body['DbInstanceId'] = request.db_instance_id
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GetRdsBackUp',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.GetRdsBackUpResponse(),
            self.call_api(params, req, runtime)
        )

    def get_rds_back_up(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_rds_back_up_with_options(request, runtime)

    def grant_db_to_account_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.account_name):
            body['AccountName'] = request.account_name
        if not UtilClient.is_unset(request.account_privilege):
            body['AccountPrivilege'] = request.account_privilege
        if not UtilClient.is_unset(request.db_instance_id):
            body['DbInstanceId'] = request.db_instance_id
        if not UtilClient.is_unset(request.db_name):
            body['DbName'] = request.db_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='GrantDbToAccount',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.GrantDbToAccountResponse(),
            self.call_api(params, req, runtime)
        )

    def grant_db_to_account(self, request):
        runtime = util_models.RuntimeOptions()
        return self.grant_db_to_account_with_options(request, runtime)

    def list_app_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListApp',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.ListAppResponse(),
            self.call_api(params, req, runtime)
        )

    def list_app(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_app_with_options(request, runtime)

    def list_app_cms_groups_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAppCmsGroups',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.ListAppCmsGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_app_cms_groups(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_app_cms_groups_with_options(request, runtime)

    def list_app_environment_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAppEnvironment',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.ListAppEnvironmentResponse(),
            self.call_api(params, req, runtime)
        )

    def list_app_environment(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_app_environment_with_options(request, runtime)

    def list_app_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_code):
            query['BizCode'] = request.biz_code
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAppGroup',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.ListAppGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def list_app_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_app_group_with_options(request, runtime)

    def list_app_group_mapping_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.biz_code):
            query['BizCode'] = request.biz_code
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAppGroupMapping',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.ListAppGroupMappingResponse(),
            self.call_api(params, req, runtime)
        )

    def list_app_group_mapping(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_app_group_mapping_with_options(request, runtime)

    def list_app_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.env_id):
            body['EnvId'] = request.env_id
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListAppInstance',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.ListAppInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    def list_app_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_app_instance_with_options(request, runtime)

    def list_app_resource_allocs_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAppResourceAllocs',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.ListAppResourceAllocsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_app_resource_allocs(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_app_resource_allocs_with_options(request, runtime)

    def list_available_cluster_node_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAvailableClusterNode',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.ListAvailableClusterNodeResponse(),
            self.call_api(params, req, runtime)
        )

    def list_available_cluster_node(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_available_cluster_node_with_options(request, runtime)

    def list_cluster_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListCluster',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.ListClusterResponse(),
            self.call_api(params, req, runtime)
        )

    def list_cluster(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_cluster_with_options(request, runtime)

    def list_cluster_node_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListClusterNode',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.ListClusterNodeResponse(),
            self.call_api(params, req, runtime)
        )

    def list_cluster_node(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_cluster_node_with_options(request, runtime)

    def list_deploy_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.env_type):
            query['EnvType'] = request.env_type
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDeployConfig',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.ListDeployConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def list_deploy_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_deploy_config_with_options(request, runtime)

    def list_deploy_orders_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.deploy_category):
            query['DeployCategory'] = request.deploy_category
        if not UtilClient.is_unset(request.deploy_type):
            query['DeployType'] = request.deploy_type
        if not UtilClient.is_unset(request.end_time_greater_than):
            query['EndTimeGreaterThan'] = request.end_time_greater_than
        if not UtilClient.is_unset(request.end_time_greater_than_or_equal_to):
            query['EndTimeGreaterThanOrEqualTo'] = request.end_time_greater_than_or_equal_to
        if not UtilClient.is_unset(request.end_time_less_than):
            query['EndTimeLessThan'] = request.end_time_less_than
        if not UtilClient.is_unset(request.end_time_less_than_or_equal_to):
            query['EndTimeLessThanOrEqualTo'] = request.end_time_less_than_or_equal_to
        if not UtilClient.is_unset(request.env_id):
            query['EnvId'] = request.env_id
        if not UtilClient.is_unset(request.env_type):
            query['EnvType'] = request.env_type
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.partition_type):
            query['PartitionType'] = request.partition_type
        if not UtilClient.is_unset(request.pause_type):
            query['PauseType'] = request.pause_type
        if not UtilClient.is_unset(request.start_time_greater_than):
            query['StartTimeGreaterThan'] = request.start_time_greater_than
        if not UtilClient.is_unset(request.start_time_greater_than_or_equal_to):
            query['StartTimeGreaterThanOrEqualTo'] = request.start_time_greater_than_or_equal_to
        if not UtilClient.is_unset(request.start_time_less_than):
            query['StartTimeLessThan'] = request.start_time_less_than
        if not UtilClient.is_unset(request.start_time_less_than_or_equal_to):
            query['StartTimeLessThanOrEqualTo'] = request.start_time_less_than_or_equal_to
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        body = {}
        if not UtilClient.is_unset(request.result_list):
            body['ResultList'] = request.result_list
        if not UtilClient.is_unset(request.status_list):
            body['StatusList'] = request.status_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListDeployOrders',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.ListDeployOrdersResponse(),
            self.call_api(params, req, runtime)
        )

    def list_deploy_orders(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_deploy_orders_with_options(request, runtime)

    def list_job_histories_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListJobHistories',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.ListJobHistoriesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_job_histories(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_job_histories_with_options(request, runtime)

    def list_node_label_bindings_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListNodeLabelBindings',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.ListNodeLabelBindingsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_node_label_bindings(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_node_label_bindings_with_options(request, runtime)

    def list_node_labels_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.label_key):
            query['LabelKey'] = request.label_key
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListNodeLabels',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.ListNodeLabelsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_node_labels(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_node_labels_with_options(request, runtime)

    def list_persistent_volume_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.cluster_instance_id):
            body['ClusterInstanceId'] = request.cluster_instance_id
        if not UtilClient.is_unset(request.page_number):
            body['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            body['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListPersistentVolume',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.ListPersistentVolumeResponse(),
            self.call_api(params, req, runtime)
        )

    def list_persistent_volume(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_persistent_volume_with_options(request, runtime)

    def list_persistent_volume_claim_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.env_id):
            query['EnvId'] = request.env_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPersistentVolumeClaim',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.ListPersistentVolumeClaimResponse(),
            self.call_api(params, req, runtime)
        )

    def list_persistent_volume_claim(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_persistent_volume_claim_with_options(request, runtime)

    def list_pods_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.deploy_order_id):
            query['DeployOrderId'] = request.deploy_order_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        body = {}
        if not UtilClient.is_unset(request.result_list):
            body['ResultList'] = request.result_list
        if not UtilClient.is_unset(request.status_list):
            body['StatusList'] = request.status_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListPods',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.ListPodsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_pods(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_pods_with_options(request, runtime)

    def list_services_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.env_id):
            query['EnvId'] = request.env_id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.service_type):
            query['ServiceType'] = request.service_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListServices',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.ListServicesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_services(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_services_with_options(request, runtime)

    def list_slb_aps_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.env_id):
            query['EnvId'] = request.env_id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.network_mode):
            query['NetworkMode'] = request.network_mode
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.slb_id):
            query['SlbId'] = request.slb_id
        body = {}
        if not UtilClient.is_unset(request.protocol_list):
            body['ProtocolList'] = request.protocol_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ListSlbAPs',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.ListSlbAPsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_slb_aps(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_slb_aps_with_options(request, runtime)

    def list_users_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListUsers',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.ListUsersResponse(),
            self.call_api(params, req, runtime)
        )

    def list_users(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_users_with_options(request, runtime)

    def modify_service_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.service_id):
            query['ServiceId'] = request.service_id
        body = {}
        if not UtilClient.is_unset(request.port_mappings):
            body['PortMappings'] = request.port_mappings
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ModifyService',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.ModifyServiceResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_service(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_service_with_options(request, runtime)

    def modify_slb_apwith_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cookie_timeout):
            query['CookieTimeout'] = request.cookie_timeout
        if not UtilClient.is_unset(request.established_timeout):
            query['EstablishedTimeout'] = request.established_timeout
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.real_server_port):
            query['RealServerPort'] = request.real_server_port
        if not UtilClient.is_unset(request.slb_apid):
            query['SlbAPId'] = request.slb_apid
        if not UtilClient.is_unset(request.ssl_cert_id):
            query['SslCertId'] = request.ssl_cert_id
        if not UtilClient.is_unset(request.sticky_session):
            query['StickySession'] = request.sticky_session
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifySlbAP',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.ModifySlbAPResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_slb_ap(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_slb_apwith_options(request, runtime)

    def offline_app_environment_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.delete_pvc):
            query['DeletePvc'] = request.delete_pvc
        if not UtilClient.is_unset(request.env_id):
            query['EnvId'] = request.env_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='OfflineAppEnvironment',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.OfflineAppEnvironmentResponse(),
            self.call_api(params, req, runtime)
        )

    def offline_app_environment(self, request):
        runtime = util_models.RuntimeOptions()
        return self.offline_app_environment_with_options(request, runtime)

    def query_cluster_detail_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = OpenApiUtilClient.query(UtilClient.to_map(request))
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='QueryClusterDetail',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='GET',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.QueryClusterDetailResponse(),
            self.call_api(params, req, runtime)
        )

    def query_cluster_detail(self, request):
        runtime = util_models.RuntimeOptions()
        return self.query_cluster_detail_with_options(request, runtime)

    def rebuild_app_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.app_instance_id):
            query['AppInstanceId'] = request.app_instance_id
        if not UtilClient.is_unset(request.env_id):
            query['EnvId'] = request.env_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RebuildAppInstance',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.RebuildAppInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    def rebuild_app_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.rebuild_app_instance_with_options(request, runtime)

    def remove_cluster_node_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_instance_id):
            query['ClusterInstanceId'] = request.cluster_instance_id
        if not UtilClient.is_unset(request.ecs_instance_id_list):
            query['EcsInstanceIdList'] = request.ecs_instance_id_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemoveClusterNode',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.RemoveClusterNodeResponse(),
            self.call_api(params, req, runtime)
        )

    def remove_cluster_node(self, request):
        runtime = util_models.RuntimeOptions()
        return self.remove_cluster_node_with_options(request, runtime)

    def reset_account_password_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.account_name):
            body['AccountName'] = request.account_name
        if not UtilClient.is_unset(request.account_password):
            body['AccountPassword'] = request.account_password
        if not UtilClient.is_unset(request.db_instance_id):
            body['DbInstanceId'] = request.db_instance_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ResetAccountPassword',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.ResetAccountPasswordResponse(),
            self.call_api(params, req, runtime)
        )

    def reset_account_password(self, request):
        runtime = util_models.RuntimeOptions()
        return self.reset_account_password_with_options(request, runtime)

    def resource_status_notify_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.data):
            body['data'] = request.data
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ResourceStatusNotify',
            version='2018-03-13',
            protocol='HTTP',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='none'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.ResourceStatusNotifyResponse(),
            self.call_api(params, req, runtime)
        )

    def resource_status_notify(self, request):
        runtime = util_models.RuntimeOptions()
        return self.resource_status_notify_with_options(request, runtime)

    def restart_app_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.app_instance_id_list):
            query['AppInstanceIdList'] = request.app_instance_id_list
        if not UtilClient.is_unset(request.env_id):
            query['EnvId'] = request.env_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RestartAppInstance',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.RestartAppInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    def restart_app_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.restart_app_instance_with_options(request, runtime)

    def resume_deploy_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.deploy_order_id):
            query['DeployOrderId'] = request.deploy_order_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ResumeDeploy',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.ResumeDeployResponse(),
            self.call_api(params, req, runtime)
        )

    def resume_deploy(self, request):
        runtime = util_models.RuntimeOptions()
        return self.resume_deploy_with_options(request, runtime)

    def scale_app_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.env_id):
            query['EnvId'] = request.env_id
        if not UtilClient.is_unset(request.replicas):
            query['Replicas'] = request.replicas
        if not UtilClient.is_unset(request.total_partitions):
            query['TotalPartitions'] = request.total_partitions
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ScaleApp',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.ScaleAppResponse(),
            self.call_api(params, req, runtime)
        )

    def scale_app(self, request):
        runtime = util_models.RuntimeOptions()
        return self.scale_app_with_options(request, runtime)

    def set_deploy_pause_type_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.deploy_order_id):
            query['DeployOrderId'] = request.deploy_order_id
        if not UtilClient.is_unset(request.deploy_pause_type):
            query['DeployPauseType'] = request.deploy_pause_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetDeployPauseType',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.SetDeployPauseTypeResponse(),
            self.call_api(params, req, runtime)
        )

    def set_deploy_pause_type(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_deploy_pause_type_with_options(request, runtime)

    def submit_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.caller_uid):
            query['CallerUid'] = request.caller_uid
        if not UtilClient.is_unset(request.main_user_id):
            query['MainUserId'] = request.main_user_id
        if not UtilClient.is_unset(request.request_id):
            query['RequestId'] = request.request_id
        body = {}
        if not UtilClient.is_unset(request.ecs_desc_list):
            body['EcsDescList'] = request.ecs_desc_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SubmitInfo',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.SubmitInfoResponse(),
            self.call_api(params, req, runtime)
        )

    def submit_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.submit_info_with_options(request, runtime)

    def sync_pod_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.pod_name):
            query['PodName'] = request.pod_name
        if not UtilClient.is_unset(request.reason):
            query['Reason'] = request.reason
        if not UtilClient.is_unset(request.request_id):
            query['RequestId'] = request.request_id
        if not UtilClient.is_unset(request.side_car_type):
            query['SideCarType'] = request.side_car_type
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.task_id):
            query['TaskId'] = request.task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SyncPodInfo',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.SyncPodInfoResponse(),
            self.call_api(params, req, runtime)
        )

    def sync_pod_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.sync_pod_info_with_options(request, runtime)

    def unbind_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.biz_code):
            query['BizCode'] = request.biz_code
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UnbindGroup',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.UnbindGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def unbind_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.unbind_group_with_options(request, runtime)

    def unbind_node_label_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cluster_id):
            query['ClusterId'] = request.cluster_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.label_key):
            query['LabelKey'] = request.label_key
        if not UtilClient.is_unset(request.label_value):
            query['LabelValue'] = request.label_value
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UnbindNodeLabel',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.UnbindNodeLabelResponse(),
            self.call_api(params, req, runtime)
        )

    def unbind_node_label(self, request):
        runtime = util_models.RuntimeOptions()
        return self.unbind_node_label_with_options(request, runtime)

    def update_app_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.app_id):
            body['AppId'] = request.app_id
        if not UtilClient.is_unset(request.biz_title):
            body['BizTitle'] = request.biz_title
        if not UtilClient.is_unset(request.description):
            body['Description'] = request.description
        if not UtilClient.is_unset(request.language):
            body['Language'] = request.language
        if not UtilClient.is_unset(request.middle_ware_id_list):
            body['MiddleWareIdList'] = request.middle_ware_id_list
        if not UtilClient.is_unset(request.operating_system):
            body['OperatingSystem'] = request.operating_system
        if not UtilClient.is_unset(request.service_type):
            body['ServiceType'] = request.service_type
        if not UtilClient.is_unset(request.user_roles):
            body['UserRoles'] = request.user_roles
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateApp',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.UpdateAppResponse(),
            self.call_api(params, req, runtime)
        )

    def update_app(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_app_with_options(request, runtime)

    def update_app_monitors_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.main_user_id):
            body['MainUserId'] = request.main_user_id
        if not UtilClient.is_unset(request.monitor_ids):
            body['MonitorIds'] = request.monitor_ids
        if not UtilClient.is_unset(request.silence_time):
            body['SilenceTime'] = request.silence_time
        if not UtilClient.is_unset(request.template_id):
            body['TemplateId'] = request.template_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateAppMonitors',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.UpdateAppMonitorsResponse(),
            self.call_api(params, req, runtime)
        )

    def update_app_monitors(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_app_monitors_with_options(request, runtime)

    def update_deploy_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.code_path):
            query['CodePath'] = request.code_path
        if not UtilClient.is_unset(request.config_map):
            query['ConfigMap'] = request.config_map
        if not UtilClient.is_unset(request.config_map_list):
            query['ConfigMapList'] = request.config_map_list
        if not UtilClient.is_unset(request.cron_job):
            query['CronJob'] = request.cron_job
        if not UtilClient.is_unset(request.deployment):
            query['Deployment'] = request.deployment
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        if not UtilClient.is_unset(request.secret_list):
            query['SecretList'] = request.secret_list
        if not UtilClient.is_unset(request.stateful_set):
            query['StatefulSet'] = request.stateful_set
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateDeployConfig',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.UpdateDeployConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def update_deploy_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_deploy_config_with_options(request, runtime)

    def update_eci_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_env_id):
            query['AppEnvId'] = request.app_env_id
        if not UtilClient.is_unset(request.eip_bandwidth):
            query['EipBandwidth'] = request.eip_bandwidth
        if not UtilClient.is_unset(request.enable_eci_schedule_policy):
            query['EnableEciSchedulePolicy'] = request.enable_eci_schedule_policy
        if not UtilClient.is_unset(request.mirror_cache):
            query['MirrorCache'] = request.mirror_cache
        if not UtilClient.is_unset(request.normal_instance_limit):
            query['NormalInstanceLimit'] = request.normal_instance_limit
        if not UtilClient.is_unset(request.schedule_virtual_node):
            query['ScheduleVirtualNode'] = request.schedule_virtual_node
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateEciConfig',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.UpdateEciConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def update_eci_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_eci_config_with_options(request, runtime)

    def update_environment_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.app_env_id):
            query['AppEnvId'] = request.app_env_id
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.app_schema_id):
            query['AppSchemaId'] = request.app_schema_id
        if not UtilClient.is_unset(request.replicas):
            query['Replicas'] = request.replicas
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateEnvironment',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.UpdateEnvironmentResponse(),
            self.call_api(params, req, runtime)
        )

    def update_environment(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_environment_with_options(request, runtime)

    def update_normal_deploy_config_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = retailcloud_20180313_models.UpdateNormalDeployConfigShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.container_resource_limit):
            request.container_resource_limit_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.container_resource_limit, 'ContainerResourceLimit', 'json')
        if not UtilClient.is_unset(tmp_req.container_resource_request):
            request.container_resource_request_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.container_resource_request, 'ContainerResourceRequest', 'json')
        query = {}
        if not UtilClient.is_unset(request.app_id):
            query['AppId'] = request.app_id
        if not UtilClient.is_unset(request.container_resource_limit_shrink):
            query['ContainerResourceLimit'] = request.container_resource_limit_shrink
        if not UtilClient.is_unset(request.container_resource_request_shrink):
            query['ContainerResourceRequest'] = request.container_resource_request_shrink
        if not UtilClient.is_unset(request.id):
            query['Id'] = request.id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateNormalDeployConfig',
            version='2018-03-13',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            retailcloud_20180313_models.UpdateNormalDeployConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def update_normal_deploy_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_normal_deploy_config_with_options(request, runtime)
