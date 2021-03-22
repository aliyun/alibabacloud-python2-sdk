# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_alikafka20190916 import models as alikafka_20190916_models
from alibabacloud_tea_util import models as util_models


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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alikafka_20190916_models.ConvertPostPayOrderResponse().from_map(
            self.do_rpcrequest('ConvertPostPayOrder', '2019-09-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def convert_post_pay_order(self, request):
        runtime = util_models.RuntimeOptions()
        return self.convert_post_pay_order_with_options(request, runtime)

    def create_acl_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alikafka_20190916_models.CreateAclResponse().from_map(
            self.do_rpcrequest('CreateAcl', '2019-09-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_acl(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_acl_with_options(request, runtime)

    def create_consumer_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alikafka_20190916_models.CreateConsumerGroupResponse().from_map(
            self.do_rpcrequest('CreateConsumerGroup', '2019-09-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_consumer_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_consumer_group_with_options(request, runtime)

    def create_post_pay_order_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alikafka_20190916_models.CreatePostPayOrderResponse().from_map(
            self.do_rpcrequest('CreatePostPayOrder', '2019-09-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_post_pay_order(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_post_pay_order_with_options(request, runtime)

    def create_pre_pay_order_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alikafka_20190916_models.CreatePrePayOrderResponse().from_map(
            self.do_rpcrequest('CreatePrePayOrder', '2019-09-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_pre_pay_order(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_pre_pay_order_with_options(request, runtime)

    def create_sasl_user_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alikafka_20190916_models.CreateSaslUserResponse().from_map(
            self.do_rpcrequest('CreateSaslUser', '2019-09-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_sasl_user(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_sasl_user_with_options(request, runtime)

    def create_topic_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alikafka_20190916_models.CreateTopicResponse().from_map(
            self.do_rpcrequest('CreateTopic', '2019-09-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_topic(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_topic_with_options(request, runtime)

    def delete_acl_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alikafka_20190916_models.DeleteAclResponse().from_map(
            self.do_rpcrequest('DeleteAcl', '2019-09-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_acl(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_acl_with_options(request, runtime)

    def delete_consumer_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alikafka_20190916_models.DeleteConsumerGroupResponse().from_map(
            self.do_rpcrequest('DeleteConsumerGroup', '2019-09-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_consumer_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_consumer_group_with_options(request, runtime)

    def delete_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alikafka_20190916_models.DeleteInstanceResponse().from_map(
            self.do_rpcrequest('DeleteInstance', '2019-09-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_instance_with_options(request, runtime)

    def delete_sasl_user_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alikafka_20190916_models.DeleteSaslUserResponse().from_map(
            self.do_rpcrequest('DeleteSaslUser', '2019-09-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_sasl_user(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_sasl_user_with_options(request, runtime)

    def delete_topic_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alikafka_20190916_models.DeleteTopicResponse().from_map(
            self.do_rpcrequest('DeleteTopic', '2019-09-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_topic(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_topic_with_options(request, runtime)

    def describe_acls_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alikafka_20190916_models.DescribeAclsResponse().from_map(
            self.do_rpcrequest('DescribeAcls', '2019-09-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_acls(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_acls_with_options(request, runtime)

    def describe_node_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alikafka_20190916_models.DescribeNodeStatusResponse().from_map(
            self.do_rpcrequest('DescribeNodeStatus', '2019-09-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_node_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_node_status_with_options(request, runtime)

    def describe_sasl_users_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alikafka_20190916_models.DescribeSaslUsersResponse().from_map(
            self.do_rpcrequest('DescribeSaslUsers', '2019-09-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_sasl_users(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_sasl_users_with_options(request, runtime)

    def get_allowed_ip_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alikafka_20190916_models.GetAllowedIpListResponse().from_map(
            self.do_rpcrequest('GetAllowedIpList', '2019-09-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_allowed_ip_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_allowed_ip_list_with_options(request, runtime)

    def get_consumer_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alikafka_20190916_models.GetConsumerListResponse().from_map(
            self.do_rpcrequest('GetConsumerList', '2019-09-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_consumer_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_consumer_list_with_options(request, runtime)

    def get_consumer_progress_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alikafka_20190916_models.GetConsumerProgressResponse().from_map(
            self.do_rpcrequest('GetConsumerProgress', '2019-09-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_consumer_progress(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_consumer_progress_with_options(request, runtime)

    def get_instance_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alikafka_20190916_models.GetInstanceListResponse().from_map(
            self.do_rpcrequest('GetInstanceList', '2019-09-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_instance_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_instance_list_with_options(request, runtime)

    def get_meta_product_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alikafka_20190916_models.GetMetaProductListResponse().from_map(
            self.do_rpcrequest('GetMetaProductList', '2019-09-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_meta_product_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_meta_product_list_with_options(request, runtime)

    def get_topic_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alikafka_20190916_models.GetTopicListResponse().from_map(
            self.do_rpcrequest('GetTopicList', '2019-09-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_topic_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_topic_list_with_options(request, runtime)

    def get_topic_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alikafka_20190916_models.GetTopicStatusResponse().from_map(
            self.do_rpcrequest('GetTopicStatus', '2019-09-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_topic_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_topic_status_with_options(request, runtime)

    def list_tag_resources_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alikafka_20190916_models.ListTagResourcesResponse().from_map(
            self.do_rpcrequest('ListTagResources', '2019-09-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_tag_resources(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_tag_resources_with_options(request, runtime)

    def modify_instance_name_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alikafka_20190916_models.ModifyInstanceNameResponse().from_map(
            self.do_rpcrequest('ModifyInstanceName', '2019-09-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_instance_name(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_instance_name_with_options(request, runtime)

    def modify_partition_num_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alikafka_20190916_models.ModifyPartitionNumResponse().from_map(
            self.do_rpcrequest('ModifyPartitionNum', '2019-09-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_partition_num(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_partition_num_with_options(request, runtime)

    def modify_topic_remark_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alikafka_20190916_models.ModifyTopicRemarkResponse().from_map(
            self.do_rpcrequest('ModifyTopicRemark', '2019-09-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_topic_remark(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_topic_remark_with_options(request, runtime)

    def release_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alikafka_20190916_models.ReleaseInstanceResponse().from_map(
            self.do_rpcrequest('ReleaseInstance', '2019-09-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def release_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.release_instance_with_options(request, runtime)

    def start_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alikafka_20190916_models.StartInstanceResponse().from_map(
            self.do_rpcrequest('StartInstance', '2019-09-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def start_instance(self, request):
        runtime = util_models.RuntimeOptions()
        return self.start_instance_with_options(request, runtime)

    def tag_resources_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alikafka_20190916_models.TagResourcesResponse().from_map(
            self.do_rpcrequest('TagResources', '2019-09-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def tag_resources(self, request):
        runtime = util_models.RuntimeOptions()
        return self.tag_resources_with_options(request, runtime)

    def untag_resources_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alikafka_20190916_models.UntagResourcesResponse().from_map(
            self.do_rpcrequest('UntagResources', '2019-09-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def untag_resources(self, request):
        runtime = util_models.RuntimeOptions()
        return self.untag_resources_with_options(request, runtime)

    def update_allowed_ip_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alikafka_20190916_models.UpdateAllowedIpResponse().from_map(
            self.do_rpcrequest('UpdateAllowedIp', '2019-09-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_allowed_ip(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_allowed_ip_with_options(request, runtime)

    def update_instance_config_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alikafka_20190916_models.UpdateInstanceConfigResponse().from_map(
            self.do_rpcrequest('UpdateInstanceConfig', '2019-09-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_instance_config(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_instance_config_with_options(request, runtime)

    def upgrade_instance_version_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alikafka_20190916_models.UpgradeInstanceVersionResponse().from_map(
            self.do_rpcrequest('UpgradeInstanceVersion', '2019-09-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def upgrade_instance_version(self, request):
        runtime = util_models.RuntimeOptions()
        return self.upgrade_instance_version_with_options(request, runtime)

    def upgrade_post_pay_order_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alikafka_20190916_models.UpgradePostPayOrderResponse().from_map(
            self.do_rpcrequest('UpgradePostPayOrder', '2019-09-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def upgrade_post_pay_order(self, request):
        runtime = util_models.RuntimeOptions()
        return self.upgrade_post_pay_order_with_options(request, runtime)

    def upgrade_pre_pay_order_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return alikafka_20190916_models.UpgradePrePayOrderResponse().from_map(
            self.do_rpcrequest('UpgradePrePayOrder', '2019-09-16', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def upgrade_pre_pay_order(self, request):
        runtime = util_models.RuntimeOptions()
        return self.upgrade_pre_pay_order_with_options(request, runtime)
