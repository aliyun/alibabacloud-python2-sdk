# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_alikafka20190916 import models as alikafka_20190916_models
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
            'ap-northeast-2-pop': 'alikafka.aliyuncs.com',
            'ap-southeast-2': 'alikafka.aliyuncs.com',
            'cn-beijing-finance-1': 'alikafka.aliyuncs.com',
            'cn-beijing-finance-pop': 'alikafka.aliyuncs.com',
            'cn-beijing-gov-1': 'alikafka.aliyuncs.com',
            'cn-beijing-nu16-b01': 'alikafka.aliyuncs.com',
            'cn-edge-1': 'alikafka.aliyuncs.com',
            'cn-fujian': 'alikafka.aliyuncs.com',
            'cn-haidian-cm12-c01': 'alikafka.aliyuncs.com',
            'cn-hangzhou-bj-b01': 'alikafka.aliyuncs.com',
            'cn-hangzhou-internal-prod-1': 'alikafka.aliyuncs.com',
            'cn-hangzhou-internal-test-1': 'alikafka.aliyuncs.com',
            'cn-hangzhou-internal-test-2': 'alikafka.aliyuncs.com',
            'cn-hangzhou-internal-test-3': 'alikafka.aliyuncs.com',
            'cn-hangzhou-test-306': 'alikafka.aliyuncs.com',
            'cn-hongkong-finance-pop': 'alikafka.aliyuncs.com',
            'cn-huhehaote-nebula-1': 'alikafka.aliyuncs.com',
            'cn-qingdao-nebula': 'alikafka.aliyuncs.com',
            'cn-shanghai-et15-b01': 'alikafka.aliyuncs.com',
            'cn-shanghai-et2-b01': 'alikafka.aliyuncs.com',
            'cn-shanghai-inner': 'alikafka.aliyuncs.com',
            'cn-shanghai-internal-test-1': 'alikafka.aliyuncs.com',
            'cn-shenzhen-inner': 'alikafka.aliyuncs.com',
            'cn-shenzhen-st4-d01': 'alikafka.aliyuncs.com',
            'cn-shenzhen-su18-b01': 'alikafka.aliyuncs.com',
            'cn-wuhan': 'alikafka.aliyuncs.com',
            'cn-wulanchabu': 'alikafka.aliyuncs.com',
            'cn-yushanfang': 'alikafka.aliyuncs.com',
            'cn-zhangbei': 'alikafka.aliyuncs.com',
            'cn-zhangbei-na61-b01': 'alikafka.aliyuncs.com',
            'cn-zhangjiakou-na62-a01': 'alikafka.aliyuncs.com',
            'cn-zhengzhou-nebula-1': 'alikafka.aliyuncs.com',
            'eu-west-1-oxs': 'alikafka.aliyuncs.com',
            'me-east-1': 'alikafka.aliyuncs.com',
            'rus-west-1-pop': 'alikafka.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('alikafka', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def convert_post_pay_order_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.duration):
            query['Duration'] = request.duration
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ConvertPostPayOrder',
            version='2019-09-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alikafka_20190916_models.ConvertPostPayOrderResponse(),
            self.call_api(params, req, runtime)
        )

    def convert_post_pay_order(self, request):
        runtime = util_models.RuntimeOptions()
        return self.convert_post_pay_order_with_options(request, runtime)

    def create_acl_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.acl_operation_type):
            query['AclOperationType'] = request.acl_operation_type
        if not UtilClient.is_unset(request.acl_resource_name):
            query['AclResourceName'] = request.acl_resource_name
        if not UtilClient.is_unset(request.acl_resource_pattern_type):
            query['AclResourcePatternType'] = request.acl_resource_pattern_type
        if not UtilClient.is_unset(request.acl_resource_type):
            query['AclResourceType'] = request.acl_resource_type
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.username):
            query['Username'] = request.username
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateAcl',
            version='2019-09-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alikafka_20190916_models.CreateAclResponse(),
            self.call_api(params, req, runtime)
        )

    def create_acl(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_acl_with_options(request, runtime)

    def create_consumer_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.consumer_id):
            query['ConsumerId'] = request.consumer_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateConsumerGroup',
            version='2019-09-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alikafka_20190916_models.CreateConsumerGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def create_consumer_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_consumer_group_with_options(request, runtime)

    def create_post_pay_order_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.deploy_type):
            query['DeployType'] = request.deploy_type
        if not UtilClient.is_unset(request.disk_size):
            query['DiskSize'] = request.disk_size
        if not UtilClient.is_unset(request.disk_type):
            query['DiskType'] = request.disk_type
        if not UtilClient.is_unset(request.eip_max):
            query['EipMax'] = request.eip_max
        if not UtilClient.is_unset(request.io_max):
            query['IoMax'] = request.io_max
        if not UtilClient.is_unset(request.io_max_spec):
            query['IoMaxSpec'] = request.io_max_spec
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.spec_type):
            query['SpecType'] = request.spec_type
        if not UtilClient.is_unset(request.topic_quota):
            query['TopicQuota'] = request.topic_quota
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreatePostPayOrder',
            version='2019-09-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alikafka_20190916_models.CreatePostPayOrderResponse(),
            self.call_api(params, req, runtime)
        )

    def create_post_pay_order(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_post_pay_order_with_options(request, runtime)

    def create_pre_pay_order_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.deploy_type):
            query['DeployType'] = request.deploy_type
        if not UtilClient.is_unset(request.disk_size):
            query['DiskSize'] = request.disk_size
        if not UtilClient.is_unset(request.disk_type):
            query['DiskType'] = request.disk_type
        if not UtilClient.is_unset(request.eip_max):
            query['EipMax'] = request.eip_max
        if not UtilClient.is_unset(request.io_max):
            query['IoMax'] = request.io_max
        if not UtilClient.is_unset(request.io_max_spec):
            query['IoMaxSpec'] = request.io_max_spec
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.spec_type):
            query['SpecType'] = request.spec_type
        if not UtilClient.is_unset(request.topic_quota):
            query['TopicQuota'] = request.topic_quota
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreatePrePayOrder',
            version='2019-09-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alikafka_20190916_models.CreatePrePayOrderResponse(),
            self.call_api(params, req, runtime)
        )

    def create_pre_pay_order(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_pre_pay_order_with_options(request, runtime)

    def create_sasl_user_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.password):
            query['Password'] = request.password
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        if not UtilClient.is_unset(request.username):
            query['Username'] = request.username
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateSaslUser',
            version='2019-09-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alikafka_20190916_models.CreateSaslUserResponse(),
            self.call_api(params, req, runtime)
        )

    def create_sasl_user(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_sasl_user_with_options(request, runtime)

    def create_topic_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = alikafka_20190916_models.CreateTopicShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.config):
            request.config_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.config, 'Config', 'json')
        query = {}
        if not UtilClient.is_unset(request.compact_topic):
            query['CompactTopic'] = request.compact_topic
        if not UtilClient.is_unset(request.config_shrink):
            query['Config'] = request.config_shrink
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.local_topic):
            query['LocalTopic'] = request.local_topic
        if not UtilClient.is_unset(request.min_insync_replicas):
            query['MinInsyncReplicas'] = request.min_insync_replicas
        if not UtilClient.is_unset(request.partition_num):
            query['PartitionNum'] = request.partition_num
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        if not UtilClient.is_unset(request.replication_factor):
            query['ReplicationFactor'] = request.replication_factor
        if not UtilClient.is_unset(request.topic):
            query['Topic'] = request.topic
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateTopic',
            version='2019-09-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alikafka_20190916_models.CreateTopicResponse(),
            self.call_api(params, req, runtime)
        )

    def create_topic(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_topic_with_options(request, runtime)

    def delete_acl_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.acl_operation_type):
            query['AclOperationType'] = request.acl_operation_type
        if not UtilClient.is_unset(request.acl_resource_name):
            query['AclResourceName'] = request.acl_resource_name
        if not UtilClient.is_unset(request.acl_resource_pattern_type):
            query['AclResourcePatternType'] = request.acl_resource_pattern_type
        if not UtilClient.is_unset(request.acl_resource_type):
            query['AclResourceType'] = request.acl_resource_type
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.username):
            query['Username'] = request.username
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteAcl',
            version='2019-09-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alikafka_20190916_models.DeleteAclResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_acl(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_acl_with_options(request, runtime)

    def delete_consumer_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.consumer_id):
            query['ConsumerId'] = request.consumer_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteConsumerGroup',
            version='2019-09-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alikafka_20190916_models.DeleteConsumerGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_consumer_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_consumer_group_with_options(request, runtime)

    def delete_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteInstance',
            version='2019-09-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alikafka_20190916_models.DeleteInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_instance_with_options(request, runtime)

    def delete_sasl_user_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.type):
            query['Type'] = request.type
        if not UtilClient.is_unset(request.username):
            query['Username'] = request.username
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteSaslUser',
            version='2019-09-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alikafka_20190916_models.DeleteSaslUserResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_sasl_user(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_sasl_user_with_options(request, runtime)

    def delete_topic_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.topic):
            query['Topic'] = request.topic
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteTopic',
            version='2019-09-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alikafka_20190916_models.DeleteTopicResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_topic(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_topic_with_options(request, runtime)

    def describe_acls_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.acl_resource_name):
            query['AclResourceName'] = request.acl_resource_name
        if not UtilClient.is_unset(request.acl_resource_pattern_type):
            query['AclResourcePatternType'] = request.acl_resource_pattern_type
        if not UtilClient.is_unset(request.acl_resource_type):
            query['AclResourceType'] = request.acl_resource_type
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.username):
            query['Username'] = request.username
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAcls',
            version='2019-09-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alikafka_20190916_models.DescribeAclsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_acls(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_acls_with_options(request, runtime)

    def describe_node_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeNodeStatus',
            version='2019-09-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alikafka_20190916_models.DescribeNodeStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_node_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_node_status_with_options(request, runtime)

    def describe_sasl_users_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeSaslUsers',
            version='2019-09-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alikafka_20190916_models.DescribeSaslUsersResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_sasl_users(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_sasl_users_with_options(request, runtime)

    def get_all_instance_id_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAllInstanceIdList',
            version='2019-09-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alikafka_20190916_models.GetAllInstanceIdListResponse(),
            self.call_api(params, req, runtime)
        )

    def get_all_instance_id_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_all_instance_id_list_with_options(request, runtime)

    def get_allowed_ip_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAllowedIpList',
            version='2019-09-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alikafka_20190916_models.GetAllowedIpListResponse(),
            self.call_api(params, req, runtime)
        )

    def get_allowed_ip_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_allowed_ip_list_with_options(request, runtime)

    def get_consumer_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.consumer_id):
            query['ConsumerId'] = request.consumer_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetConsumerList',
            version='2019-09-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alikafka_20190916_models.GetConsumerListResponse(),
            self.call_api(params, req, runtime)
        )

    def get_consumer_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_consumer_list_with_options(request, runtime)

    def get_consumer_progress_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.consumer_id):
            query['ConsumerId'] = request.consumer_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetConsumerProgress',
            version='2019-09-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alikafka_20190916_models.GetConsumerProgressResponse(),
            self.call_api(params, req, runtime)
        )

    def get_consumer_progress(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_consumer_progress_with_options(request, runtime)

    def get_instance_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.order_id):
            query['OrderId'] = request.order_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetInstanceList',
            version='2019-09-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alikafka_20190916_models.GetInstanceListResponse(),
            self.call_api(params, req, runtime)
        )

    def get_instance_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_instance_list_with_options(request, runtime)

    def get_topic_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.current_page):
            query['CurrentPage'] = request.current_page
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.topic):
            query['Topic'] = request.topic
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetTopicList',
            version='2019-09-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alikafka_20190916_models.GetTopicListResponse(),
            self.call_api(params, req, runtime)
        )

    def get_topic_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_topic_list_with_options(request, runtime)

    def get_topic_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.topic):
            query['Topic'] = request.topic
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetTopicStatus',
            version='2019-09-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alikafka_20190916_models.GetTopicStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def get_topic_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_topic_status_with_options(request, runtime)

    def list_tag_resources_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
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
            action='ListTagResources',
            version='2019-09-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alikafka_20190916_models.ListTagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_tag_resources(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_tag_resources_with_options(request, runtime)

    def modify_instance_name_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_name):
            query['InstanceName'] = request.instance_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyInstanceName',
            version='2019-09-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alikafka_20190916_models.ModifyInstanceNameResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_instance_name(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_instance_name_with_options(request, runtime)

    def modify_partition_num_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.add_partition_num):
            query['AddPartitionNum'] = request.add_partition_num
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.topic):
            query['Topic'] = request.topic
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyPartitionNum',
            version='2019-09-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alikafka_20190916_models.ModifyPartitionNumResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_partition_num(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_partition_num_with_options(request, runtime)

    def modify_topic_remark_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.remark):
            query['Remark'] = request.remark
        if not UtilClient.is_unset(request.topic):
            query['Topic'] = request.topic
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyTopicRemark',
            version='2019-09-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alikafka_20190916_models.ModifyTopicRemarkResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_topic_remark(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_topic_remark_with_options(request, runtime)

    def release_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.force_delete_instance):
            query['ForceDeleteInstance'] = request.force_delete_instance
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ReleaseInstance',
            version='2019-09-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alikafka_20190916_models.ReleaseInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    def release_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.release_instance_with_options(request, runtime)

    def start_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.config):
            query['Config'] = request.config
        if not UtilClient.is_unset(request.deploy_module):
            query['DeployModule'] = request.deploy_module
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.is_eip_inner):
            query['IsEipInner'] = request.is_eip_inner
        if not UtilClient.is_unset(request.is_set_user_and_password):
            query['IsSetUserAndPassword'] = request.is_set_user_and_password
        if not UtilClient.is_unset(request.kmskey_id):
            query['KMSKeyId'] = request.kmskey_id
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.password):
            query['Password'] = request.password
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.security_group):
            query['SecurityGroup'] = request.security_group
        if not UtilClient.is_unset(request.service_version):
            query['ServiceVersion'] = request.service_version
        if not UtilClient.is_unset(request.username):
            query['Username'] = request.username
        if not UtilClient.is_unset(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        if not UtilClient.is_unset(request.zone_id):
            query['ZoneId'] = request.zone_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartInstance',
            version='2019-09-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alikafka_20190916_models.StartInstanceResponse(),
            self.call_api(params, req, runtime)
        )

    def start_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.start_instance_with_options(request, runtime)

    def tag_resources_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
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
            version='2019-09-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alikafka_20190916_models.TagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    def tag_resources(self, request):
        runtime = util_models.RuntimeOptions()
        return self.tag_resources_with_options(request, runtime)

    def untag_resources_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.all):
            query['All'] = request.all
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag_key):
            query['TagKey'] = request.tag_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UntagResources',
            version='2019-09-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alikafka_20190916_models.UntagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    def untag_resources(self, request):
        runtime = util_models.RuntimeOptions()
        return self.untag_resources_with_options(request, runtime)

    def update_allowed_ip_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.allowed_list_ip):
            query['AllowedListIp'] = request.allowed_list_ip
        if not UtilClient.is_unset(request.allowed_list_type):
            query['AllowedListType'] = request.allowed_list_type
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.port_range):
            query['PortRange'] = request.port_range
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.update_type):
            query['UpdateType'] = request.update_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateAllowedIp',
            version='2019-09-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alikafka_20190916_models.UpdateAllowedIpResponse(),
            self.call_api(params, req, runtime)
        )

    def update_allowed_ip(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_allowed_ip_with_options(request, runtime)

    def update_instance_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.config):
            query['Config'] = request.config
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateInstanceConfig',
            version='2019-09-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alikafka_20190916_models.UpdateInstanceConfigResponse(),
            self.call_api(params, req, runtime)
        )

    def update_instance_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_instance_config_with_options(request, runtime)

    def upgrade_instance_version_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.target_version):
            query['TargetVersion'] = request.target_version
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpgradeInstanceVersion',
            version='2019-09-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alikafka_20190916_models.UpgradeInstanceVersionResponse(),
            self.call_api(params, req, runtime)
        )

    def upgrade_instance_version(self, request):
        runtime = util_models.RuntimeOptions()
        return self.upgrade_instance_version_with_options(request, runtime)

    def upgrade_post_pay_order_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.disk_size):
            query['DiskSize'] = request.disk_size
        if not UtilClient.is_unset(request.eip_max):
            query['EipMax'] = request.eip_max
        if not UtilClient.is_unset(request.eip_model):
            query['EipModel'] = request.eip_model
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.io_max):
            query['IoMax'] = request.io_max
        if not UtilClient.is_unset(request.io_max_spec):
            query['IoMaxSpec'] = request.io_max_spec
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.spec_type):
            query['SpecType'] = request.spec_type
        if not UtilClient.is_unset(request.topic_quota):
            query['TopicQuota'] = request.topic_quota
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpgradePostPayOrder',
            version='2019-09-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alikafka_20190916_models.UpgradePostPayOrderResponse(),
            self.call_api(params, req, runtime)
        )

    def upgrade_post_pay_order(self, request):
        runtime = util_models.RuntimeOptions()
        return self.upgrade_post_pay_order_with_options(request, runtime)

    def upgrade_pre_pay_order_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.disk_size):
            query['DiskSize'] = request.disk_size
        if not UtilClient.is_unset(request.eip_max):
            query['EipMax'] = request.eip_max
        if not UtilClient.is_unset(request.eip_model):
            query['EipModel'] = request.eip_model
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.io_max):
            query['IoMax'] = request.io_max
        if not UtilClient.is_unset(request.io_max_spec):
            query['IoMaxSpec'] = request.io_max_spec
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.spec_type):
            query['SpecType'] = request.spec_type
        if not UtilClient.is_unset(request.topic_quota):
            query['TopicQuota'] = request.topic_quota
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpgradePrePayOrder',
            version='2019-09-16',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            alikafka_20190916_models.UpgradePrePayOrderResponse(),
            self.call_api(params, req, runtime)
        )

    def upgrade_pre_pay_order(self, request):
        runtime = util_models.RuntimeOptions()
        return self.upgrade_pre_pay_order_with_options(request, runtime)
