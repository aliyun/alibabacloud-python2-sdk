# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_slb20140515 import models as slb_20140515_models
from alibabacloud_tea_util import models as util_models


class Client(OpenApiClient):
    """
    *\
    """
    def __init__(self, config):
        super(Client, self).__init__(config)
        self._endpoint_rule = 'regional'
        self._endpoint_map = {
            'cn-qingdao': 'slb.aliyuncs.com',
            'cn-beijing': 'slb.aliyuncs.com',
            'cn-hangzhou': 'slb.aliyuncs.com',
            'cn-shanghai': 'slb.aliyuncs.com',
            'cn-shenzhen': 'slb.aliyuncs.com',
            'cn-hongkong': 'slb.aliyuncs.com',
            'ap-southeast-1': 'slb.aliyuncs.com',
            'us-west-1': 'slb.aliyuncs.com',
            'us-east-1': 'slb.aliyuncs.com',
            'cn-shanghai-finance-1': 'slb.aliyuncs.com',
            'cn-shenzhen-finance-1': 'slb.aliyuncs.com',
            'cn-north-2-gov-1': 'slb.aliyuncs.com',
            'ap-northeast-2-pop': 'slb.aliyuncs.com',
            'cn-beijing-finance-1': 'slb.aliyuncs.com',
            'cn-beijing-finance-pop': 'slb.aliyuncs.com',
            'cn-beijing-gov-1': 'slb.aliyuncs.com',
            'cn-beijing-nu16-b01': 'slb.aliyuncs.com',
            'cn-edge-1': 'slb.aliyuncs.com',
            'cn-fujian': 'slb.aliyuncs.com',
            'cn-haidian-cm12-c01': 'slb.aliyuncs.com',
            'cn-hangzhou-bj-b01': 'slb.aliyuncs.com',
            'cn-hangzhou-finance': 'slb.aliyuncs.com',
            'cn-hangzhou-internal-prod-1': 'slb.aliyuncs.com',
            'cn-hangzhou-internal-test-1': 'slb.aliyuncs.com',
            'cn-hangzhou-internal-test-2': 'slb.aliyuncs.com',
            'cn-hangzhou-internal-test-3': 'slb.aliyuncs.com',
            'cn-hangzhou-test-306': 'slb.aliyuncs.com',
            'cn-hongkong-finance-pop': 'slb.aliyuncs.com',
            'cn-huhehaote-nebula-1': 'slb-api.cn-qingdao-nebula.aliyuncs.com',
            'cn-shanghai-et15-b01': 'slb.aliyuncs.com',
            'cn-shanghai-et2-b01': 'slb.aliyuncs.com',
            'cn-shanghai-inner': 'slb.aliyuncs.com',
            'cn-shanghai-internal-test-1': 'slb.aliyuncs.com',
            'cn-shenzhen-inner': 'slb.aliyuncs.com',
            'cn-shenzhen-st4-d01': 'slb.aliyuncs.com',
            'cn-shenzhen-su18-b01': 'slb.aliyuncs.com',
            'cn-wuhan': 'slb.aliyuncs.com',
            'cn-yushanfang': 'slb.aliyuncs.com',
            'cn-zhangbei-na61-b01': 'slb.aliyuncs.com',
            'cn-zhangjiakou-na62-a01': 'slb.aliyuncs.com',
            'cn-zhengzhou-nebula-1': 'slb.aliyuncs.com',
            'eu-west-1-oxs': 'slb.aliyuncs.com',
            'rus-west-1-pop': 'slb.aliyuncs.com'
        }
        self.check_config(config)
        self._endpoint = self.get_endpoint('slb', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def add_access_control_list_entry_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            slb_20140515_models.AddAccessControlListEntryResponse(),
            self.do_rpcrequest('AddAccessControlListEntry', '2014-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def add_access_control_list_entry(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_access_control_list_entry_with_options(request, runtime)

    def add_backend_servers_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            slb_20140515_models.AddBackendServersResponse(),
            self.do_rpcrequest('AddBackendServers', '2014-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def add_backend_servers(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_backend_servers_with_options(request, runtime)

    def add_listener_white_list_item_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            slb_20140515_models.AddListenerWhiteListItemResponse(),
            self.do_rpcrequest('AddListenerWhiteListItem', '2014-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def add_listener_white_list_item(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_listener_white_list_item_with_options(request, runtime)

    def add_tags_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            slb_20140515_models.AddTagsResponse(),
            self.do_rpcrequest('AddTags', '2014-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def add_tags(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_tags_with_options(request, runtime)

    def add_vserver_group_backend_servers_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            slb_20140515_models.AddVServerGroupBackendServersResponse(),
            self.do_rpcrequest('AddVServerGroupBackendServers', '2014-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def add_vserver_group_backend_servers(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_vserver_group_backend_servers_with_options(request, runtime)

    def create_access_control_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            slb_20140515_models.CreateAccessControlListResponse(),
            self.do_rpcrequest('CreateAccessControlList', '2014-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_access_control_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_access_control_list_with_options(request, runtime)

    def create_domain_extension_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            slb_20140515_models.CreateDomainExtensionResponse(),
            self.do_rpcrequest('CreateDomainExtension', '2014-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_domain_extension(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_domain_extension_with_options(request, runtime)

    def create_load_balancer_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            slb_20140515_models.CreateLoadBalancerResponse(),
            self.do_rpcrequest('CreateLoadBalancer', '2014-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_load_balancer(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_load_balancer_with_options(request, runtime)

    def create_load_balancer_httplistener_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            slb_20140515_models.CreateLoadBalancerHTTPListenerResponse(),
            self.do_rpcrequest('CreateLoadBalancerHTTPListener', '2014-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_load_balancer_httplistener(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_load_balancer_httplistener_with_options(request, runtime)

    def create_load_balancer_httpslistener_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            slb_20140515_models.CreateLoadBalancerHTTPSListenerResponse(),
            self.do_rpcrequest('CreateLoadBalancerHTTPSListener', '2014-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_load_balancer_httpslistener(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_load_balancer_httpslistener_with_options(request, runtime)

    def create_load_balancer_tcplistener_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            slb_20140515_models.CreateLoadBalancerTCPListenerResponse(),
            self.do_rpcrequest('CreateLoadBalancerTCPListener', '2014-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_load_balancer_tcplistener(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_load_balancer_tcplistener_with_options(request, runtime)

    def create_load_balancer_udplistener_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            slb_20140515_models.CreateLoadBalancerUDPListenerResponse(),
            self.do_rpcrequest('CreateLoadBalancerUDPListener', '2014-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_load_balancer_udplistener(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_load_balancer_udplistener_with_options(request, runtime)

    def create_master_slave_server_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            slb_20140515_models.CreateMasterSlaveServerGroupResponse(),
            self.do_rpcrequest('CreateMasterSlaveServerGroup', '2014-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_master_slave_server_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_master_slave_server_group_with_options(request, runtime)

    def create_rules_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            slb_20140515_models.CreateRulesResponse(),
            self.do_rpcrequest('CreateRules', '2014-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_rules(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_rules_with_options(request, runtime)

    def create_tlscipher_policy_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            slb_20140515_models.CreateTLSCipherPolicyResponse(),
            self.do_rpcrequest('CreateTLSCipherPolicy', '2014-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_tlscipher_policy(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_tlscipher_policy_with_options(request, runtime)

    def create_vserver_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            slb_20140515_models.CreateVServerGroupResponse(),
            self.do_rpcrequest('CreateVServerGroup', '2014-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_vserver_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_vserver_group_with_options(request, runtime)

    def delete_access_control_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            slb_20140515_models.DeleteAccessControlListResponse(),
            self.do_rpcrequest('DeleteAccessControlList', '2014-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_access_control_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_access_control_list_with_options(request, runtime)

    def delete_cacertificate_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            slb_20140515_models.DeleteCACertificateResponse(),
            self.do_rpcrequest('DeleteCACertificate', '2014-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_cacertificate(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_cacertificate_with_options(request, runtime)

    def delete_domain_extension_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            slb_20140515_models.DeleteDomainExtensionResponse(),
            self.do_rpcrequest('DeleteDomainExtension', '2014-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_domain_extension(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_domain_extension_with_options(request, runtime)

    def delete_load_balancer_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            slb_20140515_models.DeleteLoadBalancerResponse(),
            self.do_rpcrequest('DeleteLoadBalancer', '2014-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_load_balancer(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_load_balancer_with_options(request, runtime)

    def delete_load_balancer_listener_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            slb_20140515_models.DeleteLoadBalancerListenerResponse(),
            self.do_rpcrequest('DeleteLoadBalancerListener', '2014-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_load_balancer_listener(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_load_balancer_listener_with_options(request, runtime)

    def delete_master_slave_server_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            slb_20140515_models.DeleteMasterSlaveServerGroupResponse(),
            self.do_rpcrequest('DeleteMasterSlaveServerGroup', '2014-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_master_slave_server_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_master_slave_server_group_with_options(request, runtime)

    def delete_rules_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            slb_20140515_models.DeleteRulesResponse(),
            self.do_rpcrequest('DeleteRules', '2014-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_rules(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_rules_with_options(request, runtime)

    def delete_server_certificate_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            slb_20140515_models.DeleteServerCertificateResponse(),
            self.do_rpcrequest('DeleteServerCertificate', '2014-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_server_certificate(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_server_certificate_with_options(request, runtime)

    def delete_tlscipher_policy_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            slb_20140515_models.DeleteTLSCipherPolicyResponse(),
            self.do_rpcrequest('DeleteTLSCipherPolicy', '2014-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_tlscipher_policy(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_tlscipher_policy_with_options(request, runtime)

    def delete_vserver_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            slb_20140515_models.DeleteVServerGroupResponse(),
            self.do_rpcrequest('DeleteVServerGroup', '2014-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_vserver_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_vserver_group_with_options(request, runtime)

    def describe_access_control_list_attribute_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            slb_20140515_models.DescribeAccessControlListAttributeResponse(),
            self.do_rpcrequest('DescribeAccessControlListAttribute', '2014-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_access_control_list_attribute(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_access_control_list_attribute_with_options(request, runtime)

    def describe_access_control_lists_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            slb_20140515_models.DescribeAccessControlListsResponse(),
            self.do_rpcrequest('DescribeAccessControlLists', '2014-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_access_control_lists(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_access_control_lists_with_options(request, runtime)

    def describe_available_resource_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            slb_20140515_models.DescribeAvailableResourceResponse(),
            self.do_rpcrequest('DescribeAvailableResource', '2014-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_available_resource(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_available_resource_with_options(request, runtime)

    def describe_cacertificates_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            slb_20140515_models.DescribeCACertificatesResponse(),
            self.do_rpcrequest('DescribeCACertificates', '2014-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_cacertificates(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_cacertificates_with_options(request, runtime)

    def describe_domain_extension_attribute_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            slb_20140515_models.DescribeDomainExtensionAttributeResponse(),
            self.do_rpcrequest('DescribeDomainExtensionAttribute', '2014-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_domain_extension_attribute(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_extension_attribute_with_options(request, runtime)

    def describe_domain_extensions_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            slb_20140515_models.DescribeDomainExtensionsResponse(),
            self.do_rpcrequest('DescribeDomainExtensions', '2014-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_domain_extensions(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_extensions_with_options(request, runtime)

    def describe_health_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            slb_20140515_models.DescribeHealthStatusResponse(),
            self.do_rpcrequest('DescribeHealthStatus', '2014-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_health_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_health_status_with_options(request, runtime)

    def describe_listener_access_control_attribute_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            slb_20140515_models.DescribeListenerAccessControlAttributeResponse(),
            self.do_rpcrequest('DescribeListenerAccessControlAttribute', '2014-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_listener_access_control_attribute(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_listener_access_control_attribute_with_options(request, runtime)

    def describe_load_balancer_attribute_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            slb_20140515_models.DescribeLoadBalancerAttributeResponse(),
            self.do_rpcrequest('DescribeLoadBalancerAttribute', '2014-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_load_balancer_attribute(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_load_balancer_attribute_with_options(request, runtime)

    def describe_load_balancer_httplistener_attribute_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            slb_20140515_models.DescribeLoadBalancerHTTPListenerAttributeResponse(),
            self.do_rpcrequest('DescribeLoadBalancerHTTPListenerAttribute', '2014-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_load_balancer_httplistener_attribute(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_load_balancer_httplistener_attribute_with_options(request, runtime)

    def describe_load_balancer_httpslistener_attribute_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            slb_20140515_models.DescribeLoadBalancerHTTPSListenerAttributeResponse(),
            self.do_rpcrequest('DescribeLoadBalancerHTTPSListenerAttribute', '2014-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_load_balancer_httpslistener_attribute(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_load_balancer_httpslistener_attribute_with_options(request, runtime)

    def describe_load_balancer_listeners_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            slb_20140515_models.DescribeLoadBalancerListenersResponse(),
            self.do_rpcrequest('DescribeLoadBalancerListeners', '2014-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_load_balancer_listeners(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_load_balancer_listeners_with_options(request, runtime)

    def describe_load_balancers_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            slb_20140515_models.DescribeLoadBalancersResponse(),
            self.do_rpcrequest('DescribeLoadBalancers', '2014-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_load_balancers(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_load_balancers_with_options(request, runtime)

    def describe_load_balancer_tcplistener_attribute_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            slb_20140515_models.DescribeLoadBalancerTCPListenerAttributeResponse(),
            self.do_rpcrequest('DescribeLoadBalancerTCPListenerAttribute', '2014-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_load_balancer_tcplistener_attribute(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_load_balancer_tcplistener_attribute_with_options(request, runtime)

    def describe_load_balancer_udplistener_attribute_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            slb_20140515_models.DescribeLoadBalancerUDPListenerAttributeResponse(),
            self.do_rpcrequest('DescribeLoadBalancerUDPListenerAttribute', '2014-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_load_balancer_udplistener_attribute(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_load_balancer_udplistener_attribute_with_options(request, runtime)

    def describe_master_slave_server_group_attribute_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            slb_20140515_models.DescribeMasterSlaveServerGroupAttributeResponse(),
            self.do_rpcrequest('DescribeMasterSlaveServerGroupAttribute', '2014-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_master_slave_server_group_attribute(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_master_slave_server_group_attribute_with_options(request, runtime)

    def describe_master_slave_server_groups_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            slb_20140515_models.DescribeMasterSlaveServerGroupsResponse(),
            self.do_rpcrequest('DescribeMasterSlaveServerGroups', '2014-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_master_slave_server_groups(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_master_slave_server_groups_with_options(request, runtime)

    def describe_regions_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            slb_20140515_models.DescribeRegionsResponse(),
            self.do_rpcrequest('DescribeRegions', '2014-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_regions(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_regions_with_options(request, runtime)

    def describe_rule_attribute_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            slb_20140515_models.DescribeRuleAttributeResponse(),
            self.do_rpcrequest('DescribeRuleAttribute', '2014-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_rule_attribute(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_rule_attribute_with_options(request, runtime)

    def describe_rules_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            slb_20140515_models.DescribeRulesResponse(),
            self.do_rpcrequest('DescribeRules', '2014-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_rules(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_rules_with_options(request, runtime)

    def describe_server_certificates_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            slb_20140515_models.DescribeServerCertificatesResponse(),
            self.do_rpcrequest('DescribeServerCertificates', '2014-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_server_certificates(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_server_certificates_with_options(request, runtime)

    def describe_tags_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            slb_20140515_models.DescribeTagsResponse(),
            self.do_rpcrequest('DescribeTags', '2014-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_tags(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_tags_with_options(request, runtime)

    def describe_vserver_group_attribute_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            slb_20140515_models.DescribeVServerGroupAttributeResponse(),
            self.do_rpcrequest('DescribeVServerGroupAttribute', '2014-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_vserver_group_attribute(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_vserver_group_attribute_with_options(request, runtime)

    def describe_vserver_groups_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            slb_20140515_models.DescribeVServerGroupsResponse(),
            self.do_rpcrequest('DescribeVServerGroups', '2014-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_vserver_groups(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_vserver_groups_with_options(request, runtime)

    def describe_zones_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            slb_20140515_models.DescribeZonesResponse(),
            self.do_rpcrequest('DescribeZones', '2014-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def describe_zones(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_zones_with_options(request, runtime)

    def list_tag_resources_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            slb_20140515_models.ListTagResourcesResponse(),
            self.do_rpcrequest('ListTagResources', '2014-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_tag_resources(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_tag_resources_with_options(request, runtime)

    def list_tlscipher_policies_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            slb_20140515_models.ListTLSCipherPoliciesResponse(),
            self.do_rpcrequest('ListTLSCipherPolicies', '2014-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_tlscipher_policies(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_tlscipher_policies_with_options(request, runtime)

    def modify_load_balancer_instance_spec_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            slb_20140515_models.ModifyLoadBalancerInstanceSpecResponse(),
            self.do_rpcrequest('ModifyLoadBalancerInstanceSpec', '2014-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_load_balancer_instance_spec(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_load_balancer_instance_spec_with_options(request, runtime)

    def modify_load_balancer_internet_spec_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            slb_20140515_models.ModifyLoadBalancerInternetSpecResponse(),
            self.do_rpcrequest('ModifyLoadBalancerInternetSpec', '2014-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_load_balancer_internet_spec(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_load_balancer_internet_spec_with_options(request, runtime)

    def modify_load_balancer_pay_type_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            slb_20140515_models.ModifyLoadBalancerPayTypeResponse(),
            self.do_rpcrequest('ModifyLoadBalancerPayType', '2014-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_load_balancer_pay_type(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_load_balancer_pay_type_with_options(request, runtime)

    def modify_vserver_group_backend_servers_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            slb_20140515_models.ModifyVServerGroupBackendServersResponse(),
            self.do_rpcrequest('ModifyVServerGroupBackendServers', '2014-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def modify_vserver_group_backend_servers(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_vserver_group_backend_servers_with_options(request, runtime)

    def remove_access_control_list_entry_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            slb_20140515_models.RemoveAccessControlListEntryResponse(),
            self.do_rpcrequest('RemoveAccessControlListEntry', '2014-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def remove_access_control_list_entry(self, request):
        runtime = util_models.RuntimeOptions()
        return self.remove_access_control_list_entry_with_options(request, runtime)

    def remove_backend_servers_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            slb_20140515_models.RemoveBackendServersResponse(),
            self.do_rpcrequest('RemoveBackendServers', '2014-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def remove_backend_servers(self, request):
        runtime = util_models.RuntimeOptions()
        return self.remove_backend_servers_with_options(request, runtime)

    def remove_listener_white_list_item_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            slb_20140515_models.RemoveListenerWhiteListItemResponse(),
            self.do_rpcrequest('RemoveListenerWhiteListItem', '2014-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def remove_listener_white_list_item(self, request):
        runtime = util_models.RuntimeOptions()
        return self.remove_listener_white_list_item_with_options(request, runtime)

    def remove_tags_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            slb_20140515_models.RemoveTagsResponse(),
            self.do_rpcrequest('RemoveTags', '2014-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def remove_tags(self, request):
        runtime = util_models.RuntimeOptions()
        return self.remove_tags_with_options(request, runtime)

    def remove_vserver_group_backend_servers_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            slb_20140515_models.RemoveVServerGroupBackendServersResponse(),
            self.do_rpcrequest('RemoveVServerGroupBackendServers', '2014-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def remove_vserver_group_backend_servers(self, request):
        runtime = util_models.RuntimeOptions()
        return self.remove_vserver_group_backend_servers_with_options(request, runtime)

    def set_access_control_list_attribute_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            slb_20140515_models.SetAccessControlListAttributeResponse(),
            self.do_rpcrequest('SetAccessControlListAttribute', '2014-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def set_access_control_list_attribute(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_access_control_list_attribute_with_options(request, runtime)

    def set_backend_servers_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            slb_20140515_models.SetBackendServersResponse(),
            self.do_rpcrequest('SetBackendServers', '2014-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def set_backend_servers(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_backend_servers_with_options(request, runtime)

    def set_cacertificate_name_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            slb_20140515_models.SetCACertificateNameResponse(),
            self.do_rpcrequest('SetCACertificateName', '2014-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def set_cacertificate_name(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_cacertificate_name_with_options(request, runtime)

    def set_domain_extension_attribute_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            slb_20140515_models.SetDomainExtensionAttributeResponse(),
            self.do_rpcrequest('SetDomainExtensionAttribute', '2014-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def set_domain_extension_attribute(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_domain_extension_attribute_with_options(request, runtime)

    def set_listener_access_control_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            slb_20140515_models.SetListenerAccessControlStatusResponse(),
            self.do_rpcrequest('SetListenerAccessControlStatus', '2014-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def set_listener_access_control_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_listener_access_control_status_with_options(request, runtime)

    def set_load_balancer_delete_protection_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            slb_20140515_models.SetLoadBalancerDeleteProtectionResponse(),
            self.do_rpcrequest('SetLoadBalancerDeleteProtection', '2014-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def set_load_balancer_delete_protection(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_load_balancer_delete_protection_with_options(request, runtime)

    def set_load_balancer_httplistener_attribute_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            slb_20140515_models.SetLoadBalancerHTTPListenerAttributeResponse(),
            self.do_rpcrequest('SetLoadBalancerHTTPListenerAttribute', '2014-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def set_load_balancer_httplistener_attribute(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_load_balancer_httplistener_attribute_with_options(request, runtime)

    def set_load_balancer_httpslistener_attribute_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            slb_20140515_models.SetLoadBalancerHTTPSListenerAttributeResponse(),
            self.do_rpcrequest('SetLoadBalancerHTTPSListenerAttribute', '2014-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def set_load_balancer_httpslistener_attribute(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_load_balancer_httpslistener_attribute_with_options(request, runtime)

    def set_load_balancer_modification_protection_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            slb_20140515_models.SetLoadBalancerModificationProtectionResponse(),
            self.do_rpcrequest('SetLoadBalancerModificationProtection', '2014-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def set_load_balancer_modification_protection(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_load_balancer_modification_protection_with_options(request, runtime)

    def set_load_balancer_name_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            slb_20140515_models.SetLoadBalancerNameResponse(),
            self.do_rpcrequest('SetLoadBalancerName', '2014-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def set_load_balancer_name(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_load_balancer_name_with_options(request, runtime)

    def set_load_balancer_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            slb_20140515_models.SetLoadBalancerStatusResponse(),
            self.do_rpcrequest('SetLoadBalancerStatus', '2014-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def set_load_balancer_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_load_balancer_status_with_options(request, runtime)

    def set_load_balancer_tcplistener_attribute_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            slb_20140515_models.SetLoadBalancerTCPListenerAttributeResponse(),
            self.do_rpcrequest('SetLoadBalancerTCPListenerAttribute', '2014-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def set_load_balancer_tcplistener_attribute(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_load_balancer_tcplistener_attribute_with_options(request, runtime)

    def set_load_balancer_udplistener_attribute_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            slb_20140515_models.SetLoadBalancerUDPListenerAttributeResponse(),
            self.do_rpcrequest('SetLoadBalancerUDPListenerAttribute', '2014-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def set_load_balancer_udplistener_attribute(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_load_balancer_udplistener_attribute_with_options(request, runtime)

    def set_rule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            slb_20140515_models.SetRuleResponse(),
            self.do_rpcrequest('SetRule', '2014-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def set_rule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_rule_with_options(request, runtime)

    def set_server_certificate_name_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            slb_20140515_models.SetServerCertificateNameResponse(),
            self.do_rpcrequest('SetServerCertificateName', '2014-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def set_server_certificate_name(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_server_certificate_name_with_options(request, runtime)

    def set_tlscipher_policy_attribute_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            slb_20140515_models.SetTLSCipherPolicyAttributeResponse(),
            self.do_rpcrequest('SetTLSCipherPolicyAttribute', '2014-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def set_tlscipher_policy_attribute(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_tlscipher_policy_attribute_with_options(request, runtime)

    def set_vserver_group_attribute_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            slb_20140515_models.SetVServerGroupAttributeResponse(),
            self.do_rpcrequest('SetVServerGroupAttribute', '2014-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def set_vserver_group_attribute(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_vserver_group_attribute_with_options(request, runtime)

    def start_load_balancer_listener_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            slb_20140515_models.StartLoadBalancerListenerResponse(),
            self.do_rpcrequest('StartLoadBalancerListener', '2014-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def start_load_balancer_listener(self, request):
        runtime = util_models.RuntimeOptions()
        return self.start_load_balancer_listener_with_options(request, runtime)

    def stop_load_balancer_listener_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            slb_20140515_models.StopLoadBalancerListenerResponse(),
            self.do_rpcrequest('StopLoadBalancerListener', '2014-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def stop_load_balancer_listener(self, request):
        runtime = util_models.RuntimeOptions()
        return self.stop_load_balancer_listener_with_options(request, runtime)

    def tag_resources_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            slb_20140515_models.TagResourcesResponse(),
            self.do_rpcrequest('TagResources', '2014-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def tag_resources(self, request):
        runtime = util_models.RuntimeOptions()
        return self.tag_resources_with_options(request, runtime)

    def untag_resources_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            slb_20140515_models.UntagResourcesResponse(),
            self.do_rpcrequest('UntagResources', '2014-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def untag_resources(self, request):
        runtime = util_models.RuntimeOptions()
        return self.untag_resources_with_options(request, runtime)

    def upload_cacertificate_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            slb_20140515_models.UploadCACertificateResponse(),
            self.do_rpcrequest('UploadCACertificate', '2014-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def upload_cacertificate(self, request):
        runtime = util_models.RuntimeOptions()
        return self.upload_cacertificate_with_options(request, runtime)

    def upload_server_certificate_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            slb_20140515_models.UploadServerCertificateResponse(),
            self.do_rpcrequest('UploadServerCertificate', '2014-05-15', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def upload_server_certificate(self, request):
        runtime = util_models.RuntimeOptions()
        return self.upload_server_certificate_with_options(request, runtime)
