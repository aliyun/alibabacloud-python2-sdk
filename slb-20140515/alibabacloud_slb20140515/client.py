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
from alibabacloud_openapi_util.client import Client as OpenApiUtilClient


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
            'us-east-1': 'slb.aliyuncs.com',
            'us-west-1': 'slb.aliyuncs.com',
            'cn-shanghai-finance-1': 'slb.aliyuncs.com',
            'cn-shenzhen-finance-1': 'slb.aliyuncs.com',
            'cn-north-2-gov-1': 'slb.aliyuncs.com',
            'ap-northeast-2-pop': 'slb.aliyuncs.com',
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
            'cn-zhangbei': 'slb.aliyuncs.com',
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
        """
        Each network ACL can contain one or more IP addresses or CIDR blocks. Take note of the following limits on network ACLs:
        *   The number of IP entries that can be added to a network ACL with each Alibaba Cloud account at a time: 50
        *   The maximum number of IP entries that each network ACL can contain: 300
        

        @param request: AddAccessControlListEntryRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: AddAccessControlListEntryResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.acl_entrys):
            query['AclEntrys'] = request.acl_entrys
        if not UtilClient.is_unset(request.acl_id):
            query['AclId'] = request.acl_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddAccessControlListEntry',
            version='2014-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            slb_20140515_models.AddAccessControlListEntryResponse(),
            self.call_api(params, req, runtime)
        )

    def add_access_control_list_entry(self, request):
        """
        Each network ACL can contain one or more IP addresses or CIDR blocks. Take note of the following limits on network ACLs:
        *   The number of IP entries that can be added to a network ACL with each Alibaba Cloud account at a time: 50
        *   The maximum number of IP entries that each network ACL can contain: 300
        

        @param request: AddAccessControlListEntryRequest

        @return: AddAccessControlListEntryResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.add_access_control_list_entry_with_options(request, runtime)

    def add_backend_servers_with_options(self, request, runtime):
        """
        >  If multiple identical Elastic Compute Service (ECS) instances are specified in a request, only the first ECS instance is added. The other ECS instances are ignored. If the backend server that you add is the same as one of the existing backend servers that are already associated with the listener, an error message is returned.
        

        @param request: AddBackendServersRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: AddBackendServersResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backend_servers):
            query['BackendServers'] = request.backend_servers
        if not UtilClient.is_unset(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddBackendServers',
            version='2014-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            slb_20140515_models.AddBackendServersResponse(),
            self.call_api(params, req, runtime)
        )

    def add_backend_servers(self, request):
        """
        >  If multiple identical Elastic Compute Service (ECS) instances are specified in a request, only the first ECS instance is added. The other ECS instances are ignored. If the backend server that you add is the same as one of the existing backend servers that are already associated with the listener, an error message is returned.
        

        @param request: AddBackendServersRequest

        @return: AddBackendServersResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.add_backend_servers_with_options(request, runtime)

    def add_listener_white_list_item_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.listener_port):
            query['ListenerPort'] = request.listener_port
        if not UtilClient.is_unset(request.listener_protocol):
            query['ListenerProtocol'] = request.listener_protocol
        if not UtilClient.is_unset(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.source_items):
            query['SourceItems'] = request.source_items
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddListenerWhiteListItem',
            version='2014-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            slb_20140515_models.AddListenerWhiteListItemResponse(),
            self.call_api(params, req, runtime)
        )

    def add_listener_white_list_item(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_listener_white_list_item_with_options(request, runtime)

    def add_tags_with_options(self, request, runtime):
        """
        # Limits
        Before you call this API, note the following limits:
        *   You can add up to 10 tags to each SLB instance.
        *   You can add up to five pairs of tags at a time.
        *   All the tags and keys added to an SLB instance must be unique.
        *   If you add a tag of which the key is the same as that of an existing tag, but the value is different, the new tag overwrites the existing one.
        

        @param request: AddTagsRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: AddTagsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddTags',
            version='2014-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            slb_20140515_models.AddTagsResponse(),
            self.call_api(params, req, runtime)
        )

    def add_tags(self, request):
        """
        # Limits
        Before you call this API, note the following limits:
        *   You can add up to 10 tags to each SLB instance.
        *   You can add up to five pairs of tags at a time.
        *   All the tags and keys added to an SLB instance must be unique.
        *   If you add a tag of which the key is the same as that of an existing tag, but the value is different, the new tag overwrites the existing one.
        

        @param request: AddTagsRequest

        @return: AddTagsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.add_tags_with_options(request, runtime)

    def add_vserver_group_backend_servers_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backend_servers):
            query['BackendServers'] = request.backend_servers
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.vserver_group_id):
            query['VServerGroupId'] = request.vserver_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddVServerGroupBackendServers',
            version='2014-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            slb_20140515_models.AddVServerGroupBackendServersResponse(),
            self.call_api(params, req, runtime)
        )

    def add_vserver_group_backend_servers(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_vserver_group_backend_servers_with_options(request, runtime)

    def create_access_control_list_with_options(self, request, runtime):
        """
        You can create multiple ACLs. Each ACL can contain one or more IP addresses or CIDR blocks. Before you create an ACL, take note of the following limits:
        *   An account can have a maximum of 50 ACLs in each region.
        *   You can add a maximum of 50 IP addresses or CIDR blocks at a time within an account.
        *   Each ACL can contain a maximum of 300 IP addresses or CIDR blocks.
        

        @param request: CreateAccessControlListRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateAccessControlListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.acl_name):
            query['AclName'] = request.acl_name
        if not UtilClient.is_unset(request.address_ipversion):
            query['AddressIPVersion'] = request.address_ipversion
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateAccessControlList',
            version='2014-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            slb_20140515_models.CreateAccessControlListResponse(),
            self.call_api(params, req, runtime)
        )

    def create_access_control_list(self, request):
        """
        You can create multiple ACLs. Each ACL can contain one or more IP addresses or CIDR blocks. Before you create an ACL, take note of the following limits:
        *   An account can have a maximum of 50 ACLs in each region.
        *   You can add a maximum of 50 IP addresses or CIDR blocks at a time within an account.
        *   Each ACL can contain a maximum of 300 IP addresses or CIDR blocks.
        

        @param request: CreateAccessControlListRequest

        @return: CreateAccessControlListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_access_control_list_with_options(request, runtime)

    def create_domain_extension_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.listener_port):
            query['ListenerPort'] = request.listener_port
        if not UtilClient.is_unset(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.server_certificate_id):
            query['ServerCertificateId'] = request.server_certificate_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateDomainExtension',
            version='2014-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            slb_20140515_models.CreateDomainExtensionResponse(),
            self.call_api(params, req, runtime)
        )

    def create_domain_extension(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_domain_extension_with_options(request, runtime)

    def create_load_balancer_with_options(self, request, runtime):
        """
        Before you create a CLB instance, call the [DescribeAvailableResource](~~DescribeAvailableResource~~) operation to query the resources available for purchase in the region where you want to create the CLB instance.
        *   After a CLB instance is created, you are charged for using the CLB instance.
        *   The pay-as-you-go billing method supports the pay-by-specification and pay-by-LCU metering methods.
        

        @param request: CreateLoadBalancerRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateLoadBalancerResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.address):
            query['Address'] = request.address
        if not UtilClient.is_unset(request.address_ipversion):
            query['AddressIPVersion'] = request.address_ipversion
        if not UtilClient.is_unset(request.address_type):
            query['AddressType'] = request.address_type
        if not UtilClient.is_unset(request.auto_pay):
            query['AutoPay'] = request.auto_pay
        if not UtilClient.is_unset(request.bandwidth):
            query['Bandwidth'] = request.bandwidth
        if not UtilClient.is_unset(request.client_token):
            query['ClientToken'] = request.client_token
        if not UtilClient.is_unset(request.delete_protection):
            query['DeleteProtection'] = request.delete_protection
        if not UtilClient.is_unset(request.duration):
            query['Duration'] = request.duration
        if not UtilClient.is_unset(request.instance_charge_type):
            query['InstanceChargeType'] = request.instance_charge_type
        if not UtilClient.is_unset(request.internet_charge_type):
            query['InternetChargeType'] = request.internet_charge_type
        if not UtilClient.is_unset(request.load_balancer_name):
            query['LoadBalancerName'] = request.load_balancer_name
        if not UtilClient.is_unset(request.load_balancer_spec):
            query['LoadBalancerSpec'] = request.load_balancer_spec
        if not UtilClient.is_unset(request.master_zone_id):
            query['MasterZoneId'] = request.master_zone_id
        if not UtilClient.is_unset(request.modification_protection_reason):
            query['ModificationProtectionReason'] = request.modification_protection_reason
        if not UtilClient.is_unset(request.modification_protection_status):
            query['ModificationProtectionStatus'] = request.modification_protection_status
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.pay_type):
            query['PayType'] = request.pay_type
        if not UtilClient.is_unset(request.pricing_cycle):
            query['PricingCycle'] = request.pricing_cycle
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.slave_zone_id):
            query['SlaveZoneId'] = request.slave_zone_id
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.v_switch_id):
            query['VSwitchId'] = request.v_switch_id
        if not UtilClient.is_unset(request.vpc_id):
            query['VpcId'] = request.vpc_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateLoadBalancer',
            version='2014-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            slb_20140515_models.CreateLoadBalancerResponse(),
            self.call_api(params, req, runtime)
        )

    def create_load_balancer(self, request):
        """
        Before you create a CLB instance, call the [DescribeAvailableResource](~~DescribeAvailableResource~~) operation to query the resources available for purchase in the region where you want to create the CLB instance.
        *   After a CLB instance is created, you are charged for using the CLB instance.
        *   The pay-as-you-go billing method supports the pay-by-specification and pay-by-LCU metering methods.
        

        @param request: CreateLoadBalancerRequest

        @return: CreateLoadBalancerResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_load_balancer_with_options(request, runtime)

    def create_load_balancer_httplistener_with_options(self, request, runtime):
        """
        A newly created listener is in the *stopped** state. After a listener is created, you can call the [StartLoadBalancerListener](~~StartLoadBalancerListener~~) operation to start the listener. After the listener is started, the listener can forward traffic to backend servers.
        ## Prerequisites
        A Classic Load Balancer (CLB) instance is created. For more information, see [CreateLoadBalancer](~~StartLoadBalancerListener~~).
        

        @param request: CreateLoadBalancerHTTPListenerRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateLoadBalancerHTTPListenerResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.acl_id):
            query['AclId'] = request.acl_id
        if not UtilClient.is_unset(request.acl_status):
            query['AclStatus'] = request.acl_status
        if not UtilClient.is_unset(request.acl_type):
            query['AclType'] = request.acl_type
        if not UtilClient.is_unset(request.backend_server_port):
            query['BackendServerPort'] = request.backend_server_port
        if not UtilClient.is_unset(request.bandwidth):
            query['Bandwidth'] = request.bandwidth
        if not UtilClient.is_unset(request.cookie):
            query['Cookie'] = request.cookie
        if not UtilClient.is_unset(request.cookie_timeout):
            query['CookieTimeout'] = request.cookie_timeout
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.forward_port):
            query['ForwardPort'] = request.forward_port
        if not UtilClient.is_unset(request.gzip):
            query['Gzip'] = request.gzip
        if not UtilClient.is_unset(request.health_check):
            query['HealthCheck'] = request.health_check
        if not UtilClient.is_unset(request.health_check_connect_port):
            query['HealthCheckConnectPort'] = request.health_check_connect_port
        if not UtilClient.is_unset(request.health_check_domain):
            query['HealthCheckDomain'] = request.health_check_domain
        if not UtilClient.is_unset(request.health_check_http_code):
            query['HealthCheckHttpCode'] = request.health_check_http_code
        if not UtilClient.is_unset(request.health_check_interval):
            query['HealthCheckInterval'] = request.health_check_interval
        if not UtilClient.is_unset(request.health_check_method):
            query['HealthCheckMethod'] = request.health_check_method
        if not UtilClient.is_unset(request.health_check_timeout):
            query['HealthCheckTimeout'] = request.health_check_timeout
        if not UtilClient.is_unset(request.health_check_uri):
            query['HealthCheckURI'] = request.health_check_uri
        if not UtilClient.is_unset(request.healthy_threshold):
            query['HealthyThreshold'] = request.healthy_threshold
        if not UtilClient.is_unset(request.idle_timeout):
            query['IdleTimeout'] = request.idle_timeout
        if not UtilClient.is_unset(request.listener_forward):
            query['ListenerForward'] = request.listener_forward
        if not UtilClient.is_unset(request.listener_port):
            query['ListenerPort'] = request.listener_port
        if not UtilClient.is_unset(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.request_timeout):
            query['RequestTimeout'] = request.request_timeout
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.scheduler):
            query['Scheduler'] = request.scheduler
        if not UtilClient.is_unset(request.sticky_session):
            query['StickySession'] = request.sticky_session
        if not UtilClient.is_unset(request.sticky_session_type):
            query['StickySessionType'] = request.sticky_session_type
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.unhealthy_threshold):
            query['UnhealthyThreshold'] = request.unhealthy_threshold
        if not UtilClient.is_unset(request.vserver_group_id):
            query['VServerGroupId'] = request.vserver_group_id
        if not UtilClient.is_unset(request.xforwarded_for):
            query['XForwardedFor'] = request.xforwarded_for
        if not UtilClient.is_unset(request.xforwarded_for__client_src_port):
            query['XForwardedFor_ClientSrcPort'] = request.xforwarded_for__client_src_port
        if not UtilClient.is_unset(request.xforwarded_for__slbid):
            query['XForwardedFor_SLBID'] = request.xforwarded_for__slbid
        if not UtilClient.is_unset(request.xforwarded_for__slbip):
            query['XForwardedFor_SLBIP'] = request.xforwarded_for__slbip
        if not UtilClient.is_unset(request.xforwarded_for__slbport):
            query['XForwardedFor_SLBPORT'] = request.xforwarded_for__slbport
        if not UtilClient.is_unset(request.xforwarded_for_proto):
            query['XForwardedFor_proto'] = request.xforwarded_for_proto
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateLoadBalancerHTTPListener',
            version='2014-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            slb_20140515_models.CreateLoadBalancerHTTPListenerResponse(),
            self.call_api(params, req, runtime)
        )

    def create_load_balancer_httplistener(self, request):
        """
        A newly created listener is in the *stopped** state. After a listener is created, you can call the [StartLoadBalancerListener](~~StartLoadBalancerListener~~) operation to start the listener. After the listener is started, the listener can forward traffic to backend servers.
        ## Prerequisites
        A Classic Load Balancer (CLB) instance is created. For more information, see [CreateLoadBalancer](~~StartLoadBalancerListener~~).
        

        @param request: CreateLoadBalancerHTTPListenerRequest

        @return: CreateLoadBalancerHTTPListenerResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_load_balancer_httplistener_with_options(request, runtime)

    def create_load_balancer_httpslistener_with_options(self, request, runtime):
        """
        A newly created listener is in the *stopped** state. After a listener is created, you can call the [StartLoadBalancerListener](~~27597~~) operation to start the listener. After the listener is started, the listener can forward traffic to backend servers.
        ## Prerequisites
        A Classic Load Balancer (CLB) instance is created. For more information, see [CreateLoadBalancer](https://www.alibabacloud.com/help/en/server-load-balancer/latest/createloadbalancer-2).
        

        @param request: CreateLoadBalancerHTTPSListenerRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateLoadBalancerHTTPSListenerResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.acl_id):
            query['AclId'] = request.acl_id
        if not UtilClient.is_unset(request.acl_status):
            query['AclStatus'] = request.acl_status
        if not UtilClient.is_unset(request.acl_type):
            query['AclType'] = request.acl_type
        if not UtilClient.is_unset(request.backend_server_port):
            query['BackendServerPort'] = request.backend_server_port
        if not UtilClient.is_unset(request.bandwidth):
            query['Bandwidth'] = request.bandwidth
        if not UtilClient.is_unset(request.cacertificate_id):
            query['CACertificateId'] = request.cacertificate_id
        if not UtilClient.is_unset(request.cookie):
            query['Cookie'] = request.cookie
        if not UtilClient.is_unset(request.cookie_timeout):
            query['CookieTimeout'] = request.cookie_timeout
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.enable_http_2):
            query['EnableHttp2'] = request.enable_http_2
        if not UtilClient.is_unset(request.gzip):
            query['Gzip'] = request.gzip
        if not UtilClient.is_unset(request.health_check):
            query['HealthCheck'] = request.health_check
        if not UtilClient.is_unset(request.health_check_connect_port):
            query['HealthCheckConnectPort'] = request.health_check_connect_port
        if not UtilClient.is_unset(request.health_check_domain):
            query['HealthCheckDomain'] = request.health_check_domain
        if not UtilClient.is_unset(request.health_check_http_code):
            query['HealthCheckHttpCode'] = request.health_check_http_code
        if not UtilClient.is_unset(request.health_check_interval):
            query['HealthCheckInterval'] = request.health_check_interval
        if not UtilClient.is_unset(request.health_check_method):
            query['HealthCheckMethod'] = request.health_check_method
        if not UtilClient.is_unset(request.health_check_timeout):
            query['HealthCheckTimeout'] = request.health_check_timeout
        if not UtilClient.is_unset(request.health_check_uri):
            query['HealthCheckURI'] = request.health_check_uri
        if not UtilClient.is_unset(request.healthy_threshold):
            query['HealthyThreshold'] = request.healthy_threshold
        if not UtilClient.is_unset(request.idle_timeout):
            query['IdleTimeout'] = request.idle_timeout
        if not UtilClient.is_unset(request.listener_port):
            query['ListenerPort'] = request.listener_port
        if not UtilClient.is_unset(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.request_timeout):
            query['RequestTimeout'] = request.request_timeout
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.scheduler):
            query['Scheduler'] = request.scheduler
        if not UtilClient.is_unset(request.server_certificate_id):
            query['ServerCertificateId'] = request.server_certificate_id
        if not UtilClient.is_unset(request.sticky_session):
            query['StickySession'] = request.sticky_session
        if not UtilClient.is_unset(request.sticky_session_type):
            query['StickySessionType'] = request.sticky_session_type
        if not UtilClient.is_unset(request.tlscipher_policy):
            query['TLSCipherPolicy'] = request.tlscipher_policy
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.unhealthy_threshold):
            query['UnhealthyThreshold'] = request.unhealthy_threshold
        if not UtilClient.is_unset(request.vserver_group_id):
            query['VServerGroupId'] = request.vserver_group_id
        if not UtilClient.is_unset(request.xforwarded_for):
            query['XForwardedFor'] = request.xforwarded_for
        if not UtilClient.is_unset(request.xforwarded_for__client_src_port):
            query['XForwardedFor_ClientSrcPort'] = request.xforwarded_for__client_src_port
        if not UtilClient.is_unset(request.xforwarded_for__slbid):
            query['XForwardedFor_SLBID'] = request.xforwarded_for__slbid
        if not UtilClient.is_unset(request.xforwarded_for__slbip):
            query['XForwardedFor_SLBIP'] = request.xforwarded_for__slbip
        if not UtilClient.is_unset(request.xforwarded_for__slbport):
            query['XForwardedFor_SLBPORT'] = request.xforwarded_for__slbport
        if not UtilClient.is_unset(request.xforwarded_for_proto):
            query['XForwardedFor_proto'] = request.xforwarded_for_proto
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateLoadBalancerHTTPSListener',
            version='2014-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            slb_20140515_models.CreateLoadBalancerHTTPSListenerResponse(),
            self.call_api(params, req, runtime)
        )

    def create_load_balancer_httpslistener(self, request):
        """
        A newly created listener is in the *stopped** state. After a listener is created, you can call the [StartLoadBalancerListener](~~27597~~) operation to start the listener. After the listener is started, the listener can forward traffic to backend servers.
        ## Prerequisites
        A Classic Load Balancer (CLB) instance is created. For more information, see [CreateLoadBalancer](https://www.alibabacloud.com/help/en/server-load-balancer/latest/createloadbalancer-2).
        

        @param request: CreateLoadBalancerHTTPSListenerRequest

        @return: CreateLoadBalancerHTTPSListenerResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_load_balancer_httpslistener_with_options(request, runtime)

    def create_load_balancer_tcplistener_with_options(self, request, runtime):
        """
        >  A newly created listener is in the *stopped** state. After a listener is created, you can call the [StartLoadBalancerListener](~~27597~~) operation to enable the listener to forward traffic to backend servers.
        

        @param request: CreateLoadBalancerTCPListenerRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateLoadBalancerTCPListenerResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.acl_id):
            query['AclId'] = request.acl_id
        if not UtilClient.is_unset(request.acl_status):
            query['AclStatus'] = request.acl_status
        if not UtilClient.is_unset(request.acl_type):
            query['AclType'] = request.acl_type
        if not UtilClient.is_unset(request.backend_server_port):
            query['BackendServerPort'] = request.backend_server_port
        if not UtilClient.is_unset(request.bandwidth):
            query['Bandwidth'] = request.bandwidth
        if not UtilClient.is_unset(request.connection_drain):
            query['ConnectionDrain'] = request.connection_drain
        if not UtilClient.is_unset(request.connection_drain_timeout):
            query['ConnectionDrainTimeout'] = request.connection_drain_timeout
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.established_timeout):
            query['EstablishedTimeout'] = request.established_timeout
        if not UtilClient.is_unset(request.health_check_connect_port):
            query['HealthCheckConnectPort'] = request.health_check_connect_port
        if not UtilClient.is_unset(request.health_check_connect_timeout):
            query['HealthCheckConnectTimeout'] = request.health_check_connect_timeout
        if not UtilClient.is_unset(request.health_check_domain):
            query['HealthCheckDomain'] = request.health_check_domain
        if not UtilClient.is_unset(request.health_check_http_code):
            query['HealthCheckHttpCode'] = request.health_check_http_code
        if not UtilClient.is_unset(request.health_check_switch):
            query['HealthCheckSwitch'] = request.health_check_switch
        if not UtilClient.is_unset(request.health_check_type):
            query['HealthCheckType'] = request.health_check_type
        if not UtilClient.is_unset(request.health_check_uri):
            query['HealthCheckURI'] = request.health_check_uri
        if not UtilClient.is_unset(request.healthy_threshold):
            query['HealthyThreshold'] = request.healthy_threshold
        if not UtilClient.is_unset(request.listener_port):
            query['ListenerPort'] = request.listener_port
        if not UtilClient.is_unset(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        if not UtilClient.is_unset(request.master_slave_server_group_id):
            query['MasterSlaveServerGroupId'] = request.master_slave_server_group_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.persistence_timeout):
            query['PersistenceTimeout'] = request.persistence_timeout
        if not UtilClient.is_unset(request.proxy_protocol_v2enabled):
            query['ProxyProtocolV2Enabled'] = request.proxy_protocol_v2enabled
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.scheduler):
            query['Scheduler'] = request.scheduler
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.unhealthy_threshold):
            query['UnhealthyThreshold'] = request.unhealthy_threshold
        if not UtilClient.is_unset(request.vserver_group_id):
            query['VServerGroupId'] = request.vserver_group_id
        if not UtilClient.is_unset(request.health_check_interval):
            query['healthCheckInterval'] = request.health_check_interval
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateLoadBalancerTCPListener',
            version='2014-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            slb_20140515_models.CreateLoadBalancerTCPListenerResponse(),
            self.call_api(params, req, runtime)
        )

    def create_load_balancer_tcplistener(self, request):
        """
        >  A newly created listener is in the *stopped** state. After a listener is created, you can call the [StartLoadBalancerListener](~~27597~~) operation to enable the listener to forward traffic to backend servers.
        

        @param request: CreateLoadBalancerTCPListenerRequest

        @return: CreateLoadBalancerTCPListenerResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_load_balancer_tcplistener_with_options(request, runtime)

    def create_load_balancer_udplistener_with_options(self, request, runtime):
        """
        UDP listeners of Classic Load Balancer (CLB) instances in a classic network cannot pass client IP addresses to backend servers.
        >  A newly created listener is in the **stopped** state. After a listener is created, you can call the [StartLoadBalancerListener](~~27597~~) operation to enable the listener to forward traffic to backend servers.
        

        @param request: CreateLoadBalancerUDPListenerRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateLoadBalancerUDPListenerResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.acl_id):
            query['AclId'] = request.acl_id
        if not UtilClient.is_unset(request.acl_status):
            query['AclStatus'] = request.acl_status
        if not UtilClient.is_unset(request.acl_type):
            query['AclType'] = request.acl_type
        if not UtilClient.is_unset(request.backend_server_port):
            query['BackendServerPort'] = request.backend_server_port
        if not UtilClient.is_unset(request.bandwidth):
            query['Bandwidth'] = request.bandwidth
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.health_check_connect_port):
            query['HealthCheckConnectPort'] = request.health_check_connect_port
        if not UtilClient.is_unset(request.health_check_connect_timeout):
            query['HealthCheckConnectTimeout'] = request.health_check_connect_timeout
        if not UtilClient.is_unset(request.health_check_switch):
            query['HealthCheckSwitch'] = request.health_check_switch
        if not UtilClient.is_unset(request.healthy_threshold):
            query['HealthyThreshold'] = request.healthy_threshold
        if not UtilClient.is_unset(request.listener_port):
            query['ListenerPort'] = request.listener_port
        if not UtilClient.is_unset(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        if not UtilClient.is_unset(request.master_slave_server_group_id):
            query['MasterSlaveServerGroupId'] = request.master_slave_server_group_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.proxy_protocol_v2enabled):
            query['ProxyProtocolV2Enabled'] = request.proxy_protocol_v2enabled
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.scheduler):
            query['Scheduler'] = request.scheduler
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.unhealthy_threshold):
            query['UnhealthyThreshold'] = request.unhealthy_threshold
        if not UtilClient.is_unset(request.vserver_group_id):
            query['VServerGroupId'] = request.vserver_group_id
        if not UtilClient.is_unset(request.health_check_exp):
            query['healthCheckExp'] = request.health_check_exp
        if not UtilClient.is_unset(request.health_check_interval):
            query['healthCheckInterval'] = request.health_check_interval
        if not UtilClient.is_unset(request.health_check_req):
            query['healthCheckReq'] = request.health_check_req
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateLoadBalancerUDPListener',
            version='2014-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            slb_20140515_models.CreateLoadBalancerUDPListenerResponse(),
            self.call_api(params, req, runtime)
        )

    def create_load_balancer_udplistener(self, request):
        """
        UDP listeners of Classic Load Balancer (CLB) instances in a classic network cannot pass client IP addresses to backend servers.
        >  A newly created listener is in the **stopped** state. After a listener is created, you can call the [StartLoadBalancerListener](~~27597~~) operation to enable the listener to forward traffic to backend servers.
        

        @param request: CreateLoadBalancerUDPListenerRequest

        @return: CreateLoadBalancerUDPListenerResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_load_balancer_udplistener_with_options(request, runtime)

    def create_master_slave_server_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        if not UtilClient.is_unset(request.master_slave_backend_servers):
            query['MasterSlaveBackendServers'] = request.master_slave_backend_servers
        if not UtilClient.is_unset(request.master_slave_server_group_name):
            query['MasterSlaveServerGroupName'] = request.master_slave_server_group_name
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateMasterSlaveServerGroup',
            version='2014-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            slb_20140515_models.CreateMasterSlaveServerGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def create_master_slave_server_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_master_slave_server_group_with_options(request, runtime)

    def create_rules_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.listener_port):
            query['ListenerPort'] = request.listener_port
        if not UtilClient.is_unset(request.listener_protocol):
            query['ListenerProtocol'] = request.listener_protocol
        if not UtilClient.is_unset(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.rule_list):
            query['RuleList'] = request.rule_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateRules',
            version='2014-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            slb_20140515_models.CreateRulesResponse(),
            self.call_api(params, req, runtime)
        )

    def create_rules(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_rules_with_options(request, runtime)

    def create_tlscipher_policy_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ciphers):
            query['Ciphers'] = request.ciphers
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.tlsversions):
            query['TLSVersions'] = request.tlsversions
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateTLSCipherPolicy',
            version='2014-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            slb_20140515_models.CreateTLSCipherPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    def create_tlscipher_policy(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_tlscipher_policy_with_options(request, runtime)

    def create_vserver_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backend_servers):
            query['BackendServers'] = request.backend_servers
        if not UtilClient.is_unset(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.vserver_group_name):
            query['VServerGroupName'] = request.vserver_group_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateVServerGroup',
            version='2014-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            slb_20140515_models.CreateVServerGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def create_vserver_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_vserver_group_with_options(request, runtime)

    def delete_access_control_list_with_options(self, request, runtime):
        """
        You can delete an ACL only if it is not associated with a listener.
        

        @param request: DeleteAccessControlListRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteAccessControlListResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.acl_id):
            query['AclId'] = request.acl_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteAccessControlList',
            version='2014-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            slb_20140515_models.DeleteAccessControlListResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_access_control_list(self, request):
        """
        You can delete an ACL only if it is not associated with a listener.
        

        @param request: DeleteAccessControlListRequest

        @return: DeleteAccessControlListResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_access_control_list_with_options(request, runtime)

    def delete_access_logs_download_attribute_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        if not UtilClient.is_unset(request.logs_download_attributes):
            query['LogsDownloadAttributes'] = request.logs_download_attributes
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteAccessLogsDownloadAttribute',
            version='2014-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            slb_20140515_models.DeleteAccessLogsDownloadAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_access_logs_download_attribute(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_access_logs_download_attribute_with_options(request, runtime)

    def delete_cacertificate_with_options(self, request, runtime):
        """
        You cannot delete a CA certificate that is in use.
        

        @param request: DeleteCACertificateRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteCACertificateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cacertificate_id):
            query['CACertificateId'] = request.cacertificate_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteCACertificate',
            version='2014-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            slb_20140515_models.DeleteCACertificateResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_cacertificate(self, request):
        """
        You cannot delete a CA certificate that is in use.
        

        @param request: DeleteCACertificateRequest

        @return: DeleteCACertificateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_cacertificate_with_options(request, runtime)

    def delete_domain_extension_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_extension_id):
            query['DomainExtensionId'] = request.domain_extension_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteDomainExtension',
            version='2014-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            slb_20140515_models.DeleteDomainExtensionResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_domain_extension(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_domain_extension_with_options(request, runtime)

    def delete_load_balancer_with_options(self, request, runtime):
        """
        > The listeners and tags of the SLB instance are deleted along with the SLB instance.
        

        @param request: DeleteLoadBalancerRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteLoadBalancerResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteLoadBalancer',
            version='2014-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            slb_20140515_models.DeleteLoadBalancerResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_load_balancer(self, request):
        """
        > The listeners and tags of the SLB instance are deleted along with the SLB instance.
        

        @param request: DeleteLoadBalancerRequest

        @return: DeleteLoadBalancerResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_load_balancer_with_options(request, runtime)

    def delete_load_balancer_listener_with_options(self, request, runtime):
        """
        >  You can delete only listeners that are in the *stopped** or **running** state.
        

        @param request: DeleteLoadBalancerListenerRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteLoadBalancerListenerResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.listener_port):
            query['ListenerPort'] = request.listener_port
        if not UtilClient.is_unset(request.listener_protocol):
            query['ListenerProtocol'] = request.listener_protocol
        if not UtilClient.is_unset(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteLoadBalancerListener',
            version='2014-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            slb_20140515_models.DeleteLoadBalancerListenerResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_load_balancer_listener(self, request):
        """
        >  You can delete only listeners that are in the *stopped** or **running** state.
        

        @param request: DeleteLoadBalancerListenerRequest

        @return: DeleteLoadBalancerListenerResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_load_balancer_listener_with_options(request, runtime)

    def delete_master_slave_server_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.master_slave_server_group_id):
            query['MasterSlaveServerGroupId'] = request.master_slave_server_group_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteMasterSlaveServerGroup',
            version='2014-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            slb_20140515_models.DeleteMasterSlaveServerGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_master_slave_server_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_master_slave_server_group_with_options(request, runtime)

    def delete_rules_with_options(self, request, runtime):
        """
        ## Limits
        The RuleIds parameter is required. You can specify up to 10 forwarding rules in each request.
        

        @param request: DeleteRulesRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteRulesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.rule_ids):
            query['RuleIds'] = request.rule_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteRules',
            version='2014-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            slb_20140515_models.DeleteRulesResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_rules(self, request):
        """
        ## Limits
        The RuleIds parameter is required. You can specify up to 10 forwarding rules in each request.
        

        @param request: DeleteRulesRequest

        @return: DeleteRulesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_rules_with_options(request, runtime)

    def delete_server_certificate_with_options(self, request, runtime):
        """
        >  You cannot delete server certificates that are in use.
        

        @param request: DeleteServerCertificateRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteServerCertificateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.server_certificate_id):
            query['ServerCertificateId'] = request.server_certificate_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteServerCertificate',
            version='2014-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            slb_20140515_models.DeleteServerCertificateResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_server_certificate(self, request):
        """
        >  You cannot delete server certificates that are in use.
        

        @param request: DeleteServerCertificateRequest

        @return: DeleteServerCertificateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_server_certificate_with_options(request, runtime)

    def delete_tlscipher_policy_with_options(self, request, runtime):
        """
        ## Debugging
        [OpenAPI Explorer automatically calculates the signature value. For your convenience, we recommend that you call this operation in OpenAPI Explorer. OpenAPI Explorer dynamically generates the sample code of the operation for different SDKs.](https://api.aliyun.com/#product=Slb\\&api=DeleteTLSCipherPolicy\\&type=RPC\\&version=2014-05-15)
        

        @param request: DeleteTLSCipherPolicyRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteTLSCipherPolicyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.tlscipher_policy_id):
            query['TLSCipherPolicyId'] = request.tlscipher_policy_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteTLSCipherPolicy',
            version='2014-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            slb_20140515_models.DeleteTLSCipherPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_tlscipher_policy(self, request):
        """
        ## Debugging
        [OpenAPI Explorer automatically calculates the signature value. For your convenience, we recommend that you call this operation in OpenAPI Explorer. OpenAPI Explorer dynamically generates the sample code of the operation for different SDKs.](https://api.aliyun.com/#product=Slb\\&api=DeleteTLSCipherPolicy\\&type=RPC\\&version=2014-05-15)
        

        @param request: DeleteTLSCipherPolicyRequest

        @return: DeleteTLSCipherPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_tlscipher_policy_with_options(request, runtime)

    def delete_vserver_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.vserver_group_id):
            query['VServerGroupId'] = request.vserver_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteVServerGroup',
            version='2014-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            slb_20140515_models.DeleteVServerGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_vserver_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_vserver_group_with_options(request, runtime)

    def describe_access_control_list_attribute_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.acl_entry_comment):
            query['AclEntryComment'] = request.acl_entry_comment
        if not UtilClient.is_unset(request.acl_id):
            query['AclId'] = request.acl_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page):
            query['Page'] = request.page
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAccessControlListAttribute',
            version='2014-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            slb_20140515_models.DescribeAccessControlListAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_access_control_list_attribute(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_access_control_list_attribute_with_options(request, runtime)

    def describe_access_control_lists_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.acl_name):
            query['AclName'] = request.acl_name
        if not UtilClient.is_unset(request.address_ipversion):
            query['AddressIPVersion'] = request.address_ipversion
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAccessControlLists',
            version='2014-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            slb_20140515_models.DescribeAccessControlListsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_access_control_lists(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_access_control_lists_with_options(request, runtime)

    def describe_access_logs_download_attribute_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        if not UtilClient.is_unset(request.log_type):
            query['LogType'] = request.log_type
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAccessLogsDownloadAttribute',
            version='2014-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            slb_20140515_models.DescribeAccessLogsDownloadAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_access_logs_download_attribute(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_access_logs_download_attribute_with_options(request, runtime)

    def describe_available_resource_with_options(self, request, runtime):
        """
        > Only the available resources and zones are returned.
        

        @param request: DescribeAvailableResourceRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeAvailableResourceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.address_ipversion):
            query['AddressIPVersion'] = request.address_ipversion
        if not UtilClient.is_unset(request.address_type):
            query['AddressType'] = request.address_type
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeAvailableResource',
            version='2014-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            slb_20140515_models.DescribeAvailableResourceResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_available_resource(self, request):
        """
        > Only the available resources and zones are returned.
        

        @param request: DescribeAvailableResourceRequest

        @return: DescribeAvailableResourceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_available_resource_with_options(request, runtime)

    def describe_cacertificates_with_options(self, request, runtime):
        """
        > To ensure data confidentiality, only the certificate fingerprint and name are returned. The certificate content is not returned.
        

        @param request: DescribeCACertificatesRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeCACertificatesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cacertificate_id):
            query['CACertificateId'] = request.cacertificate_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeCACertificates',
            version='2014-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            slb_20140515_models.DescribeCACertificatesResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_cacertificates(self, request):
        """
        > To ensure data confidentiality, only the certificate fingerprint and name are returned. The certificate content is not returned.
        

        @param request: DescribeCACertificatesRequest

        @return: DescribeCACertificatesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_cacertificates_with_options(request, runtime)

    def describe_domain_extension_attribute_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_extension_id):
            query['DomainExtensionId'] = request.domain_extension_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDomainExtensionAttribute',
            version='2014-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            slb_20140515_models.DescribeDomainExtensionAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_domain_extension_attribute(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_extension_attribute_with_options(request, runtime)

    def describe_domain_extensions_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_extension_id):
            query['DomainExtensionId'] = request.domain_extension_id
        if not UtilClient.is_unset(request.listener_port):
            query['ListenerPort'] = request.listener_port
        if not UtilClient.is_unset(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeDomainExtensions',
            version='2014-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            slb_20140515_models.DescribeDomainExtensionsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_domain_extensions(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_domain_extensions_with_options(request, runtime)

    def describe_health_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.listener_port):
            query['ListenerPort'] = request.listener_port
        if not UtilClient.is_unset(request.listener_protocol):
            query['ListenerProtocol'] = request.listener_protocol
        if not UtilClient.is_unset(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeHealthStatus',
            version='2014-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            slb_20140515_models.DescribeHealthStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_health_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_health_status_with_options(request, runtime)

    def describe_high_defination_monitor_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeHighDefinationMonitor',
            version='2014-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            slb_20140515_models.DescribeHighDefinationMonitorResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_high_defination_monitor(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_high_defination_monitor_with_options(request, runtime)

    def describe_listener_access_control_attribute_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.listener_port):
            query['ListenerPort'] = request.listener_port
        if not UtilClient.is_unset(request.listener_protocol):
            query['ListenerProtocol'] = request.listener_protocol
        if not UtilClient.is_unset(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeListenerAccessControlAttribute',
            version='2014-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            slb_20140515_models.DescribeListenerAccessControlAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_listener_access_control_attribute(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_listener_access_control_attribute_with_options(request, runtime)

    def describe_load_balancer_attribute_with_options(self, request, runtime):
        """
        >  If backend servers are deployed in a vServer group, you can call the [DescribeVServerGroupAttribute](~~35224~~) operation to query the backend servers.
        

        @param request: DescribeLoadBalancerAttributeRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeLoadBalancerAttributeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLoadBalancerAttribute',
            version='2014-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            slb_20140515_models.DescribeLoadBalancerAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_load_balancer_attribute(self, request):
        """
        >  If backend servers are deployed in a vServer group, you can call the [DescribeVServerGroupAttribute](~~35224~~) operation to query the backend servers.
        

        @param request: DescribeLoadBalancerAttributeRequest

        @return: DescribeLoadBalancerAttributeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_load_balancer_attribute_with_options(request, runtime)

    def describe_load_balancer_httplistener_attribute_with_options(self, request, runtime):
        """
        A Classic Load Balancer (CLB) instance is created. For more information, see [CreateLoadBalancer](~~27577~~).
        *   An HTTP listener is created. For more information about how to create an HTTP listener, see [CreateLoadBalancerHTTPListener](~~27592~~).
        

        @param request: DescribeLoadBalancerHTTPListenerAttributeRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeLoadBalancerHTTPListenerAttributeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.listener_port):
            query['ListenerPort'] = request.listener_port
        if not UtilClient.is_unset(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLoadBalancerHTTPListenerAttribute',
            version='2014-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            slb_20140515_models.DescribeLoadBalancerHTTPListenerAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_load_balancer_httplistener_attribute(self, request):
        """
        A Classic Load Balancer (CLB) instance is created. For more information, see [CreateLoadBalancer](~~27577~~).
        *   An HTTP listener is created. For more information about how to create an HTTP listener, see [CreateLoadBalancerHTTPListener](~~27592~~).
        

        @param request: DescribeLoadBalancerHTTPListenerAttributeRequest

        @return: DescribeLoadBalancerHTTPListenerAttributeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_load_balancer_httplistener_attribute_with_options(request, runtime)

    def describe_load_balancer_httpslistener_attribute_with_options(self, request, runtime):
        """
        A Classic Load Balancer (CLB) instance is created. For more information, see [CreateLoadBalancer](~~27577~~).
        *   An HTTPS listener is created. For more information about how to create an HTTPS listener, see [CreateLoadBalancerHTTPSListener](~~27593~~).
        

        @param request: DescribeLoadBalancerHTTPSListenerAttributeRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeLoadBalancerHTTPSListenerAttributeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.listener_port):
            query['ListenerPort'] = request.listener_port
        if not UtilClient.is_unset(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLoadBalancerHTTPSListenerAttribute',
            version='2014-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            slb_20140515_models.DescribeLoadBalancerHTTPSListenerAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_load_balancer_httpslistener_attribute(self, request):
        """
        A Classic Load Balancer (CLB) instance is created. For more information, see [CreateLoadBalancer](~~27577~~).
        *   An HTTPS listener is created. For more information about how to create an HTTPS listener, see [CreateLoadBalancerHTTPSListener](~~27593~~).
        

        @param request: DescribeLoadBalancerHTTPSListenerAttributeRequest

        @return: DescribeLoadBalancerHTTPSListenerAttributeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_load_balancer_httpslistener_attribute_with_options(request, runtime)

    def describe_load_balancer_listeners_with_options(self, request, runtime):
        """
        A CLB instance is created. For more information, see [CreateLoadBalancer](~~2401685~~).
        *   One or more listeners are added to the CLB instance. For more information, see the following topics:
        *   [CreateLoadBalancerUDPListener](~~CreateLoadBalancerUDPListener~~)
        *   [CreateLoadBalancerTCPListener](~~CreateLoadBalancerTCPListener~~)
        *   [CreateLoadBalancerHTTPListener](~~CreateLoadBalancerHTTPListener~~)
        *   [CreateLoadBalancerHTTPSListener](~~CreateLoadBalancerHTTPSListener~~)
        

        @param request: DescribeLoadBalancerListenersRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeLoadBalancerListenersResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.listener_port):
            query['ListenerPort'] = request.listener_port
        if not UtilClient.is_unset(request.listener_protocol):
            query['ListenerProtocol'] = request.listener_protocol
        if not UtilClient.is_unset(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLoadBalancerListeners',
            version='2014-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            slb_20140515_models.DescribeLoadBalancerListenersResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_load_balancer_listeners(self, request):
        """
        A CLB instance is created. For more information, see [CreateLoadBalancer](~~2401685~~).
        *   One or more listeners are added to the CLB instance. For more information, see the following topics:
        *   [CreateLoadBalancerUDPListener](~~CreateLoadBalancerUDPListener~~)
        *   [CreateLoadBalancerTCPListener](~~CreateLoadBalancerTCPListener~~)
        *   [CreateLoadBalancerHTTPListener](~~CreateLoadBalancerHTTPListener~~)
        *   [CreateLoadBalancerHTTPSListener](~~CreateLoadBalancerHTTPSListener~~)
        

        @param request: DescribeLoadBalancerListenersRequest

        @return: DescribeLoadBalancerListenersResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_load_balancer_listeners_with_options(request, runtime)

    def describe_load_balancer_tcplistener_attribute_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.listener_port):
            query['ListenerPort'] = request.listener_port
        if not UtilClient.is_unset(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLoadBalancerTCPListenerAttribute',
            version='2014-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            slb_20140515_models.DescribeLoadBalancerTCPListenerAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_load_balancer_tcplistener_attribute(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_load_balancer_tcplistener_attribute_with_options(request, runtime)

    def describe_load_balancer_udplistener_attribute_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.listener_port):
            query['ListenerPort'] = request.listener_port
        if not UtilClient.is_unset(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeLoadBalancerUDPListenerAttribute',
            version='2014-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            slb_20140515_models.DescribeLoadBalancerUDPListenerAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_load_balancer_udplistener_attribute(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_load_balancer_udplistener_attribute_with_options(request, runtime)

    def describe_load_balancers_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.address):
            query['Address'] = request.address
        if not UtilClient.is_unset(request.address_ipversion):
            query['AddressIPVersion'] = request.address_ipversion
        if not UtilClient.is_unset(request.address_type):
            query['AddressType'] = request.address_type
        if not UtilClient.is_unset(request.internet_charge_type):
            query['InternetChargeType'] = request.internet_charge_type
        if not UtilClient.is_unset(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        if not UtilClient.is_unset(request.load_balancer_name):
            query['LoadBalancerName'] = request.load_balancer_name
        if not UtilClient.is_unset(request.load_balancer_status):
            query['LoadBalancerStatus'] = request.load_balancer_status
        if not UtilClient.is_unset(request.master_zone_id):
            query['MasterZoneId'] = request.master_zone_id
        if not UtilClient.is_unset(request.network_type):
            query['NetworkType'] = request.network_type
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.pay_type):
            query['PayType'] = request.pay_type
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.server_id):
            query['ServerId'] = request.server_id
        if not UtilClient.is_unset(request.server_intranet_address):
            query['ServerIntranetAddress'] = request.server_intranet_address
        if not UtilClient.is_unset(request.slave_zone_id):
            query['SlaveZoneId'] = request.slave_zone_id
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
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
            action='DescribeLoadBalancers',
            version='2014-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            slb_20140515_models.DescribeLoadBalancersResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_load_balancers(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_load_balancers_with_options(request, runtime)

    def describe_master_slave_server_group_attribute_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.master_slave_server_group_id):
            query['MasterSlaveServerGroupId'] = request.master_slave_server_group_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeMasterSlaveServerGroupAttribute',
            version='2014-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            slb_20140515_models.DescribeMasterSlaveServerGroupAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_master_slave_server_group_attribute(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_master_slave_server_group_attribute_with_options(request, runtime)

    def describe_master_slave_server_groups_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.include_listener):
            query['IncludeListener'] = request.include_listener
        if not UtilClient.is_unset(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeMasterSlaveServerGroups',
            version='2014-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            slb_20140515_models.DescribeMasterSlaveServerGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_master_slave_server_groups(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_master_slave_server_groups_with_options(request, runtime)

    def describe_regions_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRegions',
            version='2014-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            slb_20140515_models.DescribeRegionsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_regions(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_regions_with_options(request, runtime)

    def describe_rule_attribute_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.rule_id):
            query['RuleId'] = request.rule_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRuleAttribute',
            version='2014-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            slb_20140515_models.DescribeRuleAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_rule_attribute(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_rule_attribute_with_options(request, runtime)

    def describe_rules_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.listener_port):
            query['ListenerPort'] = request.listener_port
        if not UtilClient.is_unset(request.listener_protocol):
            query['ListenerProtocol'] = request.listener_protocol
        if not UtilClient.is_unset(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRules',
            version='2014-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            slb_20140515_models.DescribeRulesResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_rules(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_rules_with_options(request, runtime)

    def describe_server_certificates_with_options(self, request, runtime):
        """
        >  For security reasons, only fingerprints and names of the server certificates are returned. The content of the server certificates and private keys is not returned.
        

        @param request: DescribeServerCertificatesRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeServerCertificatesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.server_certificate_id):
            query['ServerCertificateId'] = request.server_certificate_id
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeServerCertificates',
            version='2014-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            slb_20140515_models.DescribeServerCertificatesResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_server_certificates(self, request):
        """
        >  For security reasons, only fingerprints and names of the server certificates are returned. The content of the server certificates and private keys is not returned.
        

        @param request: DescribeServerCertificatesRequest

        @return: DescribeServerCertificatesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_server_certificates_with_options(request, runtime)

    def describe_tags_with_options(self, request, runtime):
        """
        When you call this operation, take note of the following items:
        *   You can query tags by instance ID, tag key, and tag value. If the operation is successful, the system returns all tags that match the specified conditions.
        *   The logical relationship among the specified conditions is AND. Only tags that match all the specified conditions are returned.
        *   If the Tagkey parameter is set and the Tagvalue parameter is not set, all tags that contain the specified tag key are returned.
        *   If you set the Tagvalue parameter in a request, you must also set the Tagkey parameter in the request.
        *   If you set both the Tagkey and Tagvalue parameters, only tags that contain the specified keys and values are returned.
        

        @param request: DescribeTagsRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DescribeTagsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.distinct_key):
            query['DistinctKey'] = request.distinct_key
        if not UtilClient.is_unset(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeTags',
            version='2014-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            slb_20140515_models.DescribeTagsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_tags(self, request):
        """
        When you call this operation, take note of the following items:
        *   You can query tags by instance ID, tag key, and tag value. If the operation is successful, the system returns all tags that match the specified conditions.
        *   The logical relationship among the specified conditions is AND. Only tags that match all the specified conditions are returned.
        *   If the Tagkey parameter is set and the Tagvalue parameter is not set, all tags that contain the specified tag key are returned.
        *   If you set the Tagvalue parameter in a request, you must also set the Tagkey parameter in the request.
        *   If you set both the Tagkey and Tagvalue parameters, only tags that contain the specified keys and values are returned.
        

        @param request: DescribeTagsRequest

        @return: DescribeTagsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.describe_tags_with_options(request, runtime)

    def describe_vserver_group_attribute_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.vserver_group_id):
            query['VServerGroupId'] = request.vserver_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeVServerGroupAttribute',
            version='2014-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            slb_20140515_models.DescribeVServerGroupAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_vserver_group_attribute(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_vserver_group_attribute_with_options(request, runtime)

    def describe_vserver_groups_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.include_listener):
            query['IncludeListener'] = request.include_listener
        if not UtilClient.is_unset(request.include_rule):
            query['IncludeRule'] = request.include_rule
        if not UtilClient.is_unset(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeVServerGroups',
            version='2014-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            slb_20140515_models.DescribeVServerGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_vserver_groups(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_vserver_groups_with_options(request, runtime)

    def describe_zones_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeZones',
            version='2014-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            slb_20140515_models.DescribeZonesResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_zones(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_zones_with_options(request, runtime)

    def enable_high_defination_monitor_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.log_project):
            query['LogProject'] = request.log_project
        if not UtilClient.is_unset(request.log_store):
            query['LogStore'] = request.log_store
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnableHighDefinationMonitor',
            version='2014-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            slb_20140515_models.EnableHighDefinationMonitorResponse(),
            self.call_api(params, req, runtime)
        )

    def enable_high_defination_monitor(self, request):
        runtime = util_models.RuntimeOptions()
        return self.enable_high_defination_monitor_with_options(request, runtime)

    def list_tlscipher_policies_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.include_listener):
            query['IncludeListener'] = request.include_listener
        if not UtilClient.is_unset(request.max_items):
            query['MaxItems'] = request.max_items
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.tlscipher_policy_id):
            query['TLSCipherPolicyId'] = request.tlscipher_policy_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTLSCipherPolicies',
            version='2014-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            slb_20140515_models.ListTLSCipherPoliciesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_tlscipher_policies(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_tlscipher_policies_with_options(request, runtime)

    def list_tag_resources_with_options(self, request, runtime):
        """
        Set **ResourceId.N** or **Tag.N** that consists of **Tag.N.Key** and **Tag.N.Value** in the request to specify the object to be queried.
        *   **Tag.N** is a resource tag that consists of a key-value pair. If you set only **Tag.N.Key**, all tag values that are associated with the specified tag key are returned. If you set only **Tag.N.Value**, an error message is returned.
        *   If you set **Tag.N** and **ResourceId.N** to filter tags, **ResourceId.N** must match all specified key-value pairs.
        *   If you specify multiple key-value pairs, resources that contain these key-value pairs are returned.
        

        @param request: ListTagResourcesRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListTagResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTagResources',
            version='2014-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            slb_20140515_models.ListTagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_tag_resources(self, request):
        """
        Set **ResourceId.N** or **Tag.N** that consists of **Tag.N.Key** and **Tag.N.Value** in the request to specify the object to be queried.
        *   **Tag.N** is a resource tag that consists of a key-value pair. If you set only **Tag.N.Key**, all tag values that are associated with the specified tag key are returned. If you set only **Tag.N.Value**, an error message is returned.
        *   If you set **Tag.N** and **ResourceId.N** to filter tags, **ResourceId.N** must match all specified key-value pairs.
        *   If you specify multiple key-value pairs, resources that contain these key-value pairs are returned.
        

        @param request: ListTagResourcesRequest

        @return: ListTagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_tag_resources_with_options(request, runtime)

    def modify_high_defination_monitor_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.log_project):
            query['LogProject'] = request.log_project
        if not UtilClient.is_unset(request.log_store):
            query['LogStore'] = request.log_store
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyHighDefinationMonitor',
            version='2014-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            slb_20140515_models.ModifyHighDefinationMonitorResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_high_defination_monitor(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_high_defination_monitor_with_options(request, runtime)

    def modify_load_balancer_instance_charge_type_with_options(self, request, runtime):
        """
        >    For pay-as-you-go CLB instances, you can only change the metering method from pay-by-specification to pay-by-LCU. You cannot change the metering method from pay-by-LCU to pay-by-specification.
        >*   This operation can change the metering method of only one instance at a time.
        

        @param request: ModifyLoadBalancerInstanceChargeTypeRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ModifyLoadBalancerInstanceChargeTypeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.bandwidth):
            query['Bandwidth'] = request.bandwidth
        if not UtilClient.is_unset(request.instance_charge_type):
            query['InstanceChargeType'] = request.instance_charge_type
        if not UtilClient.is_unset(request.internet_charge_type):
            query['InternetChargeType'] = request.internet_charge_type
        if not UtilClient.is_unset(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        if not UtilClient.is_unset(request.load_balancer_spec):
            query['LoadBalancerSpec'] = request.load_balancer_spec
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyLoadBalancerInstanceChargeType',
            version='2014-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            slb_20140515_models.ModifyLoadBalancerInstanceChargeTypeResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_load_balancer_instance_charge_type(self, request):
        """
        >    For pay-as-you-go CLB instances, you can only change the metering method from pay-by-specification to pay-by-LCU. You cannot change the metering method from pay-by-LCU to pay-by-specification.
        >*   This operation can change the metering method of only one instance at a time.
        

        @param request: ModifyLoadBalancerInstanceChargeTypeRequest

        @return: ModifyLoadBalancerInstanceChargeTypeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_load_balancer_instance_charge_type_with_options(request, runtime)

    def modify_load_balancer_instance_spec_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_pay):
            query['AutoPay'] = request.auto_pay
        if not UtilClient.is_unset(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        if not UtilClient.is_unset(request.load_balancer_spec):
            query['LoadBalancerSpec'] = request.load_balancer_spec
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyLoadBalancerInstanceSpec',
            version='2014-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            slb_20140515_models.ModifyLoadBalancerInstanceSpecResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_load_balancer_instance_spec(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_load_balancer_instance_spec_with_options(request, runtime)

    def modify_load_balancer_internet_spec_with_options(self, request, runtime):
        """
        ## Description
        *   If you modify only the maximum bandwidth of a pay-by-bandwidth CLB instance, the new bandwidth immediately takes effect.
        *   If you modify the metering method (for example, switch from pay-by-bandwidth to pay-by-data-transfer), the new metering method and the other changes specified in the operation take effect at 00:00:00 the next day.
        

        @param request: ModifyLoadBalancerInternetSpecRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ModifyLoadBalancerInternetSpecResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_pay):
            query['AutoPay'] = request.auto_pay
        if not UtilClient.is_unset(request.bandwidth):
            query['Bandwidth'] = request.bandwidth
        if not UtilClient.is_unset(request.internet_charge_type):
            query['InternetChargeType'] = request.internet_charge_type
        if not UtilClient.is_unset(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyLoadBalancerInternetSpec',
            version='2014-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            slb_20140515_models.ModifyLoadBalancerInternetSpecResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_load_balancer_internet_spec(self, request):
        """
        ## Description
        *   If you modify only the maximum bandwidth of a pay-by-bandwidth CLB instance, the new bandwidth immediately takes effect.
        *   If you modify the metering method (for example, switch from pay-by-bandwidth to pay-by-data-transfer), the new metering method and the other changes specified in the operation take effect at 00:00:00 the next day.
        

        @param request: ModifyLoadBalancerInternetSpecRequest

        @return: ModifyLoadBalancerInternetSpecResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_load_balancer_internet_spec_with_options(request, runtime)

    def modify_load_balancer_pay_type_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_pay):
            query['AutoPay'] = request.auto_pay
        if not UtilClient.is_unset(request.duration):
            query['Duration'] = request.duration
        if not UtilClient.is_unset(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.pay_type):
            query['PayType'] = request.pay_type
        if not UtilClient.is_unset(request.pricing_cycle):
            query['PricingCycle'] = request.pricing_cycle
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyLoadBalancerPayType',
            version='2014-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            slb_20140515_models.ModifyLoadBalancerPayTypeResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_load_balancer_pay_type(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_load_balancer_pay_type_with_options(request, runtime)

    def modify_vserver_group_backend_servers_with_options(self, request, runtime):
        """
        You can call this operation to replace the backend servers in a specified vServer group. To modify the configurations of the backend servers, such as their weights, you can call the [SetVServerGroupAttribute](~~35217~~) operation.
        

        @param request: ModifyVServerGroupBackendServersRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ModifyVServerGroupBackendServersResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.new_backend_servers):
            query['NewBackendServers'] = request.new_backend_servers
        if not UtilClient.is_unset(request.old_backend_servers):
            query['OldBackendServers'] = request.old_backend_servers
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.vserver_group_id):
            query['VServerGroupId'] = request.vserver_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyVServerGroupBackendServers',
            version='2014-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            slb_20140515_models.ModifyVServerGroupBackendServersResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_vserver_group_backend_servers(self, request):
        """
        You can call this operation to replace the backend servers in a specified vServer group. To modify the configurations of the backend servers, such as their weights, you can call the [SetVServerGroupAttribute](~~35217~~) operation.
        

        @param request: ModifyVServerGroupBackendServersRequest

        @return: ModifyVServerGroupBackendServersResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.modify_vserver_group_backend_servers_with_options(request, runtime)

    def move_resource_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.new_resource_group_id):
            query['NewResourceGroupId'] = request.new_resource_group_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.access_key_id):
            query['access_key_id'] = request.access_key_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='MoveResourceGroup',
            version='2014-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            slb_20140515_models.MoveResourceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def move_resource_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.move_resource_group_with_options(request, runtime)

    def remove_access_control_list_entry_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.acl_entrys):
            query['AclEntrys'] = request.acl_entrys
        if not UtilClient.is_unset(request.acl_id):
            query['AclId'] = request.acl_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemoveAccessControlListEntry',
            version='2014-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            slb_20140515_models.RemoveAccessControlListEntryResponse(),
            self.call_api(params, req, runtime)
        )

    def remove_access_control_list_entry(self, request):
        runtime = util_models.RuntimeOptions()
        return self.remove_access_control_list_entry_with_options(request, runtime)

    def remove_backend_servers_with_options(self, request, runtime):
        """
        >  If the backend servers that you want to remove are not in the server list of the Classic Load Balancer (CLB) instance, the request fails. However, the system does not report an error.
        

        @param request: RemoveBackendServersRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: RemoveBackendServersResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backend_servers):
            query['BackendServers'] = request.backend_servers
        if not UtilClient.is_unset(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemoveBackendServers',
            version='2014-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            slb_20140515_models.RemoveBackendServersResponse(),
            self.call_api(params, req, runtime)
        )

    def remove_backend_servers(self, request):
        """
        >  If the backend servers that you want to remove are not in the server list of the Classic Load Balancer (CLB) instance, the request fails. However, the system does not report an error.
        

        @param request: RemoveBackendServersRequest

        @return: RemoveBackendServersResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.remove_backend_servers_with_options(request, runtime)

    def remove_listener_white_list_item_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.listener_port):
            query['ListenerPort'] = request.listener_port
        if not UtilClient.is_unset(request.listener_protocol):
            query['ListenerProtocol'] = request.listener_protocol
        if not UtilClient.is_unset(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.source_items):
            query['SourceItems'] = request.source_items
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemoveListenerWhiteListItem',
            version='2014-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            slb_20140515_models.RemoveListenerWhiteListItemResponse(),
            self.call_api(params, req, runtime)
        )

    def remove_listener_white_list_item(self, request):
        runtime = util_models.RuntimeOptions()
        return self.remove_listener_white_list_item_with_options(request, runtime)

    def remove_tags_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemoveTags',
            version='2014-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            slb_20140515_models.RemoveTagsResponse(),
            self.call_api(params, req, runtime)
        )

    def remove_tags(self, request):
        runtime = util_models.RuntimeOptions()
        return self.remove_tags_with_options(request, runtime)

    def remove_vserver_group_backend_servers_with_options(self, request, runtime):
        """
        >  If one or more backend servers specified by the *BackendServers** parameter do not exist in the specified vServer group, these backend servers are ignored and no error message is returned.
        

        @param request: RemoveVServerGroupBackendServersRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: RemoveVServerGroupBackendServersResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backend_servers):
            query['BackendServers'] = request.backend_servers
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.vserver_group_id):
            query['VServerGroupId'] = request.vserver_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemoveVServerGroupBackendServers',
            version='2014-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            slb_20140515_models.RemoveVServerGroupBackendServersResponse(),
            self.call_api(params, req, runtime)
        )

    def remove_vserver_group_backend_servers(self, request):
        """
        >  If one or more backend servers specified by the *BackendServers** parameter do not exist in the specified vServer group, these backend servers are ignored and no error message is returned.
        

        @param request: RemoveVServerGroupBackendServersRequest

        @return: RemoveVServerGroupBackendServersResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.remove_vserver_group_backend_servers_with_options(request, runtime)

    def set_access_control_list_attribute_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.acl_id):
            query['AclId'] = request.acl_id
        if not UtilClient.is_unset(request.acl_name):
            query['AclName'] = request.acl_name
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetAccessControlListAttribute',
            version='2014-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            slb_20140515_models.SetAccessControlListAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    def set_access_control_list_attribute(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_access_control_list_attribute_with_options(request, runtime)

    def set_access_logs_download_attribute_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        if not UtilClient.is_unset(request.logs_download_attributes):
            query['LogsDownloadAttributes'] = request.logs_download_attributes
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.tags):
            query['Tags'] = request.tags
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetAccessLogsDownloadAttribute',
            version='2014-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            slb_20140515_models.SetAccessLogsDownloadAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    def set_access_logs_download_attribute(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_access_logs_download_attribute_with_options(request, runtime)

    def set_backend_servers_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backend_servers):
            query['BackendServers'] = request.backend_servers
        if not UtilClient.is_unset(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetBackendServers',
            version='2014-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            slb_20140515_models.SetBackendServersResponse(),
            self.call_api(params, req, runtime)
        )

    def set_backend_servers(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_backend_servers_with_options(request, runtime)

    def set_cacertificate_name_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cacertificate_id):
            query['CACertificateId'] = request.cacertificate_id
        if not UtilClient.is_unset(request.cacertificate_name):
            query['CACertificateName'] = request.cacertificate_name
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetCACertificateName',
            version='2014-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            slb_20140515_models.SetCACertificateNameResponse(),
            self.call_api(params, req, runtime)
        )

    def set_cacertificate_name(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_cacertificate_name_with_options(request, runtime)

    def set_domain_extension_attribute_with_options(self, request, runtime):
        """
        >  You cannot replace an additional certificate for a listener that is added to a shared-resource Server Load Balancer (SLB) instance.
        

        @param request: SetDomainExtensionAttributeRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: SetDomainExtensionAttributeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.domain_extension_id):
            query['DomainExtensionId'] = request.domain_extension_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.server_certificate_id):
            query['ServerCertificateId'] = request.server_certificate_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetDomainExtensionAttribute',
            version='2014-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            slb_20140515_models.SetDomainExtensionAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    def set_domain_extension_attribute(self, request):
        """
        >  You cannot replace an additional certificate for a listener that is added to a shared-resource Server Load Balancer (SLB) instance.
        

        @param request: SetDomainExtensionAttributeRequest

        @return: SetDomainExtensionAttributeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.set_domain_extension_attribute_with_options(request, runtime)

    def set_listener_access_control_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.access_control_status):
            query['AccessControlStatus'] = request.access_control_status
        if not UtilClient.is_unset(request.listener_port):
            query['ListenerPort'] = request.listener_port
        if not UtilClient.is_unset(request.listener_protocol):
            query['ListenerProtocol'] = request.listener_protocol
        if not UtilClient.is_unset(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetListenerAccessControlStatus',
            version='2014-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            slb_20140515_models.SetListenerAccessControlStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def set_listener_access_control_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_listener_access_control_status_with_options(request, runtime)

    def set_load_balancer_delete_protection_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.delete_protection):
            query['DeleteProtection'] = request.delete_protection
        if not UtilClient.is_unset(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetLoadBalancerDeleteProtection',
            version='2014-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            slb_20140515_models.SetLoadBalancerDeleteProtectionResponse(),
            self.call_api(params, req, runtime)
        )

    def set_load_balancer_delete_protection(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_load_balancer_delete_protection_with_options(request, runtime)

    def set_load_balancer_httplistener_attribute_with_options(self, request, runtime):
        """
        ### Prerequisites
        *   A Classic Load Balancer (CLB) instance is created. For more information, see [CreateLoadBalancer](~~27577~~).
        *   An HTTP listener is created. For more information about how to create an HTTP listener, see [CreateLoadBalancerHTTPListener](~~27592~~).
        

        @param request: SetLoadBalancerHTTPListenerAttributeRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: SetLoadBalancerHTTPListenerAttributeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.acl_id):
            query['AclId'] = request.acl_id
        if not UtilClient.is_unset(request.acl_status):
            query['AclStatus'] = request.acl_status
        if not UtilClient.is_unset(request.acl_type):
            query['AclType'] = request.acl_type
        if not UtilClient.is_unset(request.bandwidth):
            query['Bandwidth'] = request.bandwidth
        if not UtilClient.is_unset(request.cookie):
            query['Cookie'] = request.cookie
        if not UtilClient.is_unset(request.cookie_timeout):
            query['CookieTimeout'] = request.cookie_timeout
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.gzip):
            query['Gzip'] = request.gzip
        if not UtilClient.is_unset(request.health_check):
            query['HealthCheck'] = request.health_check
        if not UtilClient.is_unset(request.health_check_connect_port):
            query['HealthCheckConnectPort'] = request.health_check_connect_port
        if not UtilClient.is_unset(request.health_check_domain):
            query['HealthCheckDomain'] = request.health_check_domain
        if not UtilClient.is_unset(request.health_check_http_code):
            query['HealthCheckHttpCode'] = request.health_check_http_code
        if not UtilClient.is_unset(request.health_check_interval):
            query['HealthCheckInterval'] = request.health_check_interval
        if not UtilClient.is_unset(request.health_check_method):
            query['HealthCheckMethod'] = request.health_check_method
        if not UtilClient.is_unset(request.health_check_timeout):
            query['HealthCheckTimeout'] = request.health_check_timeout
        if not UtilClient.is_unset(request.health_check_uri):
            query['HealthCheckURI'] = request.health_check_uri
        if not UtilClient.is_unset(request.healthy_threshold):
            query['HealthyThreshold'] = request.healthy_threshold
        if not UtilClient.is_unset(request.idle_timeout):
            query['IdleTimeout'] = request.idle_timeout
        if not UtilClient.is_unset(request.listener_port):
            query['ListenerPort'] = request.listener_port
        if not UtilClient.is_unset(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.request_timeout):
            query['RequestTimeout'] = request.request_timeout
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.scheduler):
            query['Scheduler'] = request.scheduler
        if not UtilClient.is_unset(request.sticky_session):
            query['StickySession'] = request.sticky_session
        if not UtilClient.is_unset(request.sticky_session_type):
            query['StickySessionType'] = request.sticky_session_type
        if not UtilClient.is_unset(request.unhealthy_threshold):
            query['UnhealthyThreshold'] = request.unhealthy_threshold
        if not UtilClient.is_unset(request.vserver_group):
            query['VServerGroup'] = request.vserver_group
        if not UtilClient.is_unset(request.vserver_group_id):
            query['VServerGroupId'] = request.vserver_group_id
        if not UtilClient.is_unset(request.xforwarded_for):
            query['XForwardedFor'] = request.xforwarded_for
        if not UtilClient.is_unset(request.xforwarded_for__client_src_port):
            query['XForwardedFor_ClientSrcPort'] = request.xforwarded_for__client_src_port
        if not UtilClient.is_unset(request.xforwarded_for__slbid):
            query['XForwardedFor_SLBID'] = request.xforwarded_for__slbid
        if not UtilClient.is_unset(request.xforwarded_for__slbip):
            query['XForwardedFor_SLBIP'] = request.xforwarded_for__slbip
        if not UtilClient.is_unset(request.xforwarded_for__slbport):
            query['XForwardedFor_SLBPORT'] = request.xforwarded_for__slbport
        if not UtilClient.is_unset(request.xforwarded_for_proto):
            query['XForwardedFor_proto'] = request.xforwarded_for_proto
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetLoadBalancerHTTPListenerAttribute',
            version='2014-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            slb_20140515_models.SetLoadBalancerHTTPListenerAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    def set_load_balancer_httplistener_attribute(self, request):
        """
        ### Prerequisites
        *   A Classic Load Balancer (CLB) instance is created. For more information, see [CreateLoadBalancer](~~27577~~).
        *   An HTTP listener is created. For more information about how to create an HTTP listener, see [CreateLoadBalancerHTTPListener](~~27592~~).
        

        @param request: SetLoadBalancerHTTPListenerAttributeRequest

        @return: SetLoadBalancerHTTPListenerAttributeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.set_load_balancer_httplistener_attribute_with_options(request, runtime)

    def set_load_balancer_httpslistener_attribute_with_options(self, request, runtime):
        """
        A Classic Load Balancer (CLB) instance is created. For more information, see [CreateLoadBalancer](~~27577~~).
        *   An HTTPS listener is created. For more information about how to create an HTTPS listener, see [CreateLoadBalancerHTTPSListener](~~27593~~).
        

        @param request: SetLoadBalancerHTTPSListenerAttributeRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: SetLoadBalancerHTTPSListenerAttributeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.acl_id):
            query['AclId'] = request.acl_id
        if not UtilClient.is_unset(request.acl_status):
            query['AclStatus'] = request.acl_status
        if not UtilClient.is_unset(request.acl_type):
            query['AclType'] = request.acl_type
        if not UtilClient.is_unset(request.bandwidth):
            query['Bandwidth'] = request.bandwidth
        if not UtilClient.is_unset(request.cacertificate_id):
            query['CACertificateId'] = request.cacertificate_id
        if not UtilClient.is_unset(request.cookie):
            query['Cookie'] = request.cookie
        if not UtilClient.is_unset(request.cookie_timeout):
            query['CookieTimeout'] = request.cookie_timeout
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.enable_http_2):
            query['EnableHttp2'] = request.enable_http_2
        if not UtilClient.is_unset(request.gzip):
            query['Gzip'] = request.gzip
        if not UtilClient.is_unset(request.health_check):
            query['HealthCheck'] = request.health_check
        if not UtilClient.is_unset(request.health_check_connect_port):
            query['HealthCheckConnectPort'] = request.health_check_connect_port
        if not UtilClient.is_unset(request.health_check_domain):
            query['HealthCheckDomain'] = request.health_check_domain
        if not UtilClient.is_unset(request.health_check_http_code):
            query['HealthCheckHttpCode'] = request.health_check_http_code
        if not UtilClient.is_unset(request.health_check_interval):
            query['HealthCheckInterval'] = request.health_check_interval
        if not UtilClient.is_unset(request.health_check_method):
            query['HealthCheckMethod'] = request.health_check_method
        if not UtilClient.is_unset(request.health_check_timeout):
            query['HealthCheckTimeout'] = request.health_check_timeout
        if not UtilClient.is_unset(request.health_check_uri):
            query['HealthCheckURI'] = request.health_check_uri
        if not UtilClient.is_unset(request.healthy_threshold):
            query['HealthyThreshold'] = request.healthy_threshold
        if not UtilClient.is_unset(request.idle_timeout):
            query['IdleTimeout'] = request.idle_timeout
        if not UtilClient.is_unset(request.listener_port):
            query['ListenerPort'] = request.listener_port
        if not UtilClient.is_unset(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.request_timeout):
            query['RequestTimeout'] = request.request_timeout
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.scheduler):
            query['Scheduler'] = request.scheduler
        if not UtilClient.is_unset(request.server_certificate_id):
            query['ServerCertificateId'] = request.server_certificate_id
        if not UtilClient.is_unset(request.sticky_session):
            query['StickySession'] = request.sticky_session
        if not UtilClient.is_unset(request.sticky_session_type):
            query['StickySessionType'] = request.sticky_session_type
        if not UtilClient.is_unset(request.tlscipher_policy):
            query['TLSCipherPolicy'] = request.tlscipher_policy
        if not UtilClient.is_unset(request.unhealthy_threshold):
            query['UnhealthyThreshold'] = request.unhealthy_threshold
        if not UtilClient.is_unset(request.vserver_group):
            query['VServerGroup'] = request.vserver_group
        if not UtilClient.is_unset(request.vserver_group_id):
            query['VServerGroupId'] = request.vserver_group_id
        if not UtilClient.is_unset(request.xforwarded_for):
            query['XForwardedFor'] = request.xforwarded_for
        if not UtilClient.is_unset(request.xforwarded_for__client_src_port):
            query['XForwardedFor_ClientSrcPort'] = request.xforwarded_for__client_src_port
        if not UtilClient.is_unset(request.xforwarded_for__slbid):
            query['XForwardedFor_SLBID'] = request.xforwarded_for__slbid
        if not UtilClient.is_unset(request.xforwarded_for__slbip):
            query['XForwardedFor_SLBIP'] = request.xforwarded_for__slbip
        if not UtilClient.is_unset(request.xforwarded_for__slbport):
            query['XForwardedFor_SLBPORT'] = request.xforwarded_for__slbport
        if not UtilClient.is_unset(request.xforwarded_for_proto):
            query['XForwardedFor_proto'] = request.xforwarded_for_proto
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetLoadBalancerHTTPSListenerAttribute',
            version='2014-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            slb_20140515_models.SetLoadBalancerHTTPSListenerAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    def set_load_balancer_httpslistener_attribute(self, request):
        """
        A Classic Load Balancer (CLB) instance is created. For more information, see [CreateLoadBalancer](~~27577~~).
        *   An HTTPS listener is created. For more information about how to create an HTTPS listener, see [CreateLoadBalancerHTTPSListener](~~27593~~).
        

        @param request: SetLoadBalancerHTTPSListenerAttributeRequest

        @return: SetLoadBalancerHTTPSListenerAttributeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.set_load_balancer_httpslistener_attribute_with_options(request, runtime)

    def set_load_balancer_modification_protection_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        if not UtilClient.is_unset(request.modification_protection_reason):
            query['ModificationProtectionReason'] = request.modification_protection_reason
        if not UtilClient.is_unset(request.modification_protection_status):
            query['ModificationProtectionStatus'] = request.modification_protection_status
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetLoadBalancerModificationProtection',
            version='2014-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            slb_20140515_models.SetLoadBalancerModificationProtectionResponse(),
            self.call_api(params, req, runtime)
        )

    def set_load_balancer_modification_protection(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_load_balancer_modification_protection_with_options(request, runtime)

    def set_load_balancer_name_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        if not UtilClient.is_unset(request.load_balancer_name):
            query['LoadBalancerName'] = request.load_balancer_name
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetLoadBalancerName',
            version='2014-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            slb_20140515_models.SetLoadBalancerNameResponse(),
            self.call_api(params, req, runtime)
        )

    def set_load_balancer_name(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_load_balancer_name_with_options(request, runtime)

    def set_load_balancer_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        if not UtilClient.is_unset(request.load_balancer_status):
            query['LoadBalancerStatus'] = request.load_balancer_status
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetLoadBalancerStatus',
            version='2014-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            slb_20140515_models.SetLoadBalancerStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def set_load_balancer_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_load_balancer_status_with_options(request, runtime)

    def set_load_balancer_tcplistener_attribute_with_options(self, request, runtime):
        """
        A CLB instance is created. For more information, see [CreateLoadBalancer](~~2401685~~).
        *   A TCP listener is created. For more information, see [CreateLoadBalancerTCPListener](~~CreateLoadBalancerTCPListener~~).
        

        @param request: SetLoadBalancerTCPListenerAttributeRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: SetLoadBalancerTCPListenerAttributeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.acl_id):
            query['AclId'] = request.acl_id
        if not UtilClient.is_unset(request.acl_status):
            query['AclStatus'] = request.acl_status
        if not UtilClient.is_unset(request.acl_type):
            query['AclType'] = request.acl_type
        if not UtilClient.is_unset(request.bandwidth):
            query['Bandwidth'] = request.bandwidth
        if not UtilClient.is_unset(request.connection_drain):
            query['ConnectionDrain'] = request.connection_drain
        if not UtilClient.is_unset(request.connection_drain_timeout):
            query['ConnectionDrainTimeout'] = request.connection_drain_timeout
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.established_timeout):
            query['EstablishedTimeout'] = request.established_timeout
        if not UtilClient.is_unset(request.health_check_connect_port):
            query['HealthCheckConnectPort'] = request.health_check_connect_port
        if not UtilClient.is_unset(request.health_check_connect_timeout):
            query['HealthCheckConnectTimeout'] = request.health_check_connect_timeout
        if not UtilClient.is_unset(request.health_check_domain):
            query['HealthCheckDomain'] = request.health_check_domain
        if not UtilClient.is_unset(request.health_check_http_code):
            query['HealthCheckHttpCode'] = request.health_check_http_code
        if not UtilClient.is_unset(request.health_check_interval):
            query['HealthCheckInterval'] = request.health_check_interval
        if not UtilClient.is_unset(request.health_check_switch):
            query['HealthCheckSwitch'] = request.health_check_switch
        if not UtilClient.is_unset(request.health_check_type):
            query['HealthCheckType'] = request.health_check_type
        if not UtilClient.is_unset(request.health_check_uri):
            query['HealthCheckURI'] = request.health_check_uri
        if not UtilClient.is_unset(request.healthy_threshold):
            query['HealthyThreshold'] = request.healthy_threshold
        if not UtilClient.is_unset(request.listener_port):
            query['ListenerPort'] = request.listener_port
        if not UtilClient.is_unset(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        if not UtilClient.is_unset(request.master_slave_server_group):
            query['MasterSlaveServerGroup'] = request.master_slave_server_group
        if not UtilClient.is_unset(request.master_slave_server_group_id):
            query['MasterSlaveServerGroupId'] = request.master_slave_server_group_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.persistence_timeout):
            query['PersistenceTimeout'] = request.persistence_timeout
        if not UtilClient.is_unset(request.proxy_protocol_v2enabled):
            query['ProxyProtocolV2Enabled'] = request.proxy_protocol_v2enabled
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.scheduler):
            query['Scheduler'] = request.scheduler
        if not UtilClient.is_unset(request.syn_proxy):
            query['SynProxy'] = request.syn_proxy
        if not UtilClient.is_unset(request.unhealthy_threshold):
            query['UnhealthyThreshold'] = request.unhealthy_threshold
        if not UtilClient.is_unset(request.vserver_group):
            query['VServerGroup'] = request.vserver_group
        if not UtilClient.is_unset(request.vserver_group_id):
            query['VServerGroupId'] = request.vserver_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetLoadBalancerTCPListenerAttribute',
            version='2014-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            slb_20140515_models.SetLoadBalancerTCPListenerAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    def set_load_balancer_tcplistener_attribute(self, request):
        """
        A CLB instance is created. For more information, see [CreateLoadBalancer](~~2401685~~).
        *   A TCP listener is created. For more information, see [CreateLoadBalancerTCPListener](~~CreateLoadBalancerTCPListener~~).
        

        @param request: SetLoadBalancerTCPListenerAttributeRequest

        @return: SetLoadBalancerTCPListenerAttributeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.set_load_balancer_tcplistener_attribute_with_options(request, runtime)

    def set_load_balancer_udplistener_attribute_with_options(self, request, runtime):
        """
        A Classic Load Balancer (CLB) instance is created. For more information, see [CreateLoadBalancer](~~27577~~).
        *   A UDP listener is created. For more information, see [CreateLoadBalancerUDPListener](~~27595~~).
        

        @param request: SetLoadBalancerUDPListenerAttributeRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: SetLoadBalancerUDPListenerAttributeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.acl_id):
            query['AclId'] = request.acl_id
        if not UtilClient.is_unset(request.acl_status):
            query['AclStatus'] = request.acl_status
        if not UtilClient.is_unset(request.acl_type):
            query['AclType'] = request.acl_type
        if not UtilClient.is_unset(request.bandwidth):
            query['Bandwidth'] = request.bandwidth
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.health_check_connect_port):
            query['HealthCheckConnectPort'] = request.health_check_connect_port
        if not UtilClient.is_unset(request.health_check_connect_timeout):
            query['HealthCheckConnectTimeout'] = request.health_check_connect_timeout
        if not UtilClient.is_unset(request.health_check_interval):
            query['HealthCheckInterval'] = request.health_check_interval
        if not UtilClient.is_unset(request.health_check_switch):
            query['HealthCheckSwitch'] = request.health_check_switch
        if not UtilClient.is_unset(request.healthy_threshold):
            query['HealthyThreshold'] = request.healthy_threshold
        if not UtilClient.is_unset(request.listener_port):
            query['ListenerPort'] = request.listener_port
        if not UtilClient.is_unset(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        if not UtilClient.is_unset(request.master_slave_server_group):
            query['MasterSlaveServerGroup'] = request.master_slave_server_group
        if not UtilClient.is_unset(request.master_slave_server_group_id):
            query['MasterSlaveServerGroupId'] = request.master_slave_server_group_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.proxy_protocol_v2enabled):
            query['ProxyProtocolV2Enabled'] = request.proxy_protocol_v2enabled
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.scheduler):
            query['Scheduler'] = request.scheduler
        if not UtilClient.is_unset(request.unhealthy_threshold):
            query['UnhealthyThreshold'] = request.unhealthy_threshold
        if not UtilClient.is_unset(request.vserver_group):
            query['VServerGroup'] = request.vserver_group
        if not UtilClient.is_unset(request.vserver_group_id):
            query['VServerGroupId'] = request.vserver_group_id
        if not UtilClient.is_unset(request.health_check_exp):
            query['healthCheckExp'] = request.health_check_exp
        if not UtilClient.is_unset(request.health_check_req):
            query['healthCheckReq'] = request.health_check_req
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetLoadBalancerUDPListenerAttribute',
            version='2014-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            slb_20140515_models.SetLoadBalancerUDPListenerAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    def set_load_balancer_udplistener_attribute(self, request):
        """
        A Classic Load Balancer (CLB) instance is created. For more information, see [CreateLoadBalancer](~~27577~~).
        *   A UDP listener is created. For more information, see [CreateLoadBalancerUDPListener](~~27595~~).
        

        @param request: SetLoadBalancerUDPListenerAttributeRequest

        @return: SetLoadBalancerUDPListenerAttributeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.set_load_balancer_udplistener_attribute_with_options(request, runtime)

    def set_rule_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cookie):
            query['Cookie'] = request.cookie
        if not UtilClient.is_unset(request.cookie_timeout):
            query['CookieTimeout'] = request.cookie_timeout
        if not UtilClient.is_unset(request.health_check):
            query['HealthCheck'] = request.health_check
        if not UtilClient.is_unset(request.health_check_connect_port):
            query['HealthCheckConnectPort'] = request.health_check_connect_port
        if not UtilClient.is_unset(request.health_check_domain):
            query['HealthCheckDomain'] = request.health_check_domain
        if not UtilClient.is_unset(request.health_check_http_code):
            query['HealthCheckHttpCode'] = request.health_check_http_code
        if not UtilClient.is_unset(request.health_check_interval):
            query['HealthCheckInterval'] = request.health_check_interval
        if not UtilClient.is_unset(request.health_check_timeout):
            query['HealthCheckTimeout'] = request.health_check_timeout
        if not UtilClient.is_unset(request.health_check_uri):
            query['HealthCheckURI'] = request.health_check_uri
        if not UtilClient.is_unset(request.healthy_threshold):
            query['HealthyThreshold'] = request.healthy_threshold
        if not UtilClient.is_unset(request.listener_sync):
            query['ListenerSync'] = request.listener_sync
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.rule_id):
            query['RuleId'] = request.rule_id
        if not UtilClient.is_unset(request.rule_name):
            query['RuleName'] = request.rule_name
        if not UtilClient.is_unset(request.scheduler):
            query['Scheduler'] = request.scheduler
        if not UtilClient.is_unset(request.sticky_session):
            query['StickySession'] = request.sticky_session
        if not UtilClient.is_unset(request.sticky_session_type):
            query['StickySessionType'] = request.sticky_session_type
        if not UtilClient.is_unset(request.unhealthy_threshold):
            query['UnhealthyThreshold'] = request.unhealthy_threshold
        if not UtilClient.is_unset(request.vserver_group_id):
            query['VServerGroupId'] = request.vserver_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetRule',
            version='2014-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            slb_20140515_models.SetRuleResponse(),
            self.call_api(params, req, runtime)
        )

    def set_rule(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_rule_with_options(request, runtime)

    def set_server_certificate_name_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.server_certificate_id):
            query['ServerCertificateId'] = request.server_certificate_id
        if not UtilClient.is_unset(request.server_certificate_name):
            query['ServerCertificateName'] = request.server_certificate_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetServerCertificateName',
            version='2014-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            slb_20140515_models.SetServerCertificateNameResponse(),
            self.call_api(params, req, runtime)
        )

    def set_server_certificate_name(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_server_certificate_name_with_options(request, runtime)

    def set_tlscipher_policy_attribute_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ciphers):
            query['Ciphers'] = request.ciphers
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.tlscipher_policy_id):
            query['TLSCipherPolicyId'] = request.tlscipher_policy_id
        if not UtilClient.is_unset(request.tlsversions):
            query['TLSVersions'] = request.tlsversions
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetTLSCipherPolicyAttribute',
            version='2014-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            slb_20140515_models.SetTLSCipherPolicyAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    def set_tlscipher_policy_attribute(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_tlscipher_policy_attribute_with_options(request, runtime)

    def set_vserver_group_attribute_with_options(self, request, runtime):
        """
        This operation allows you to modify only the name of a vServer group and the weights of the backend servers in the vServer group.
        *   If you want to modify backend servers in a specified vServer group, call the [ModifyVServerGroupBackendServers](~~35220~~) operation.
        *   If you want to add backend servers to a specified vServer group, call the [AddVServerGroupBackendServers](~~35218~~) operation.
        

        @param request: SetVServerGroupAttributeRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: SetVServerGroupAttributeResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.backend_servers):
            query['BackendServers'] = request.backend_servers
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.vserver_group_id):
            query['VServerGroupId'] = request.vserver_group_id
        if not UtilClient.is_unset(request.vserver_group_name):
            query['VServerGroupName'] = request.vserver_group_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetVServerGroupAttribute',
            version='2014-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            slb_20140515_models.SetVServerGroupAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    def set_vserver_group_attribute(self, request):
        """
        This operation allows you to modify only the name of a vServer group and the weights of the backend servers in the vServer group.
        *   If you want to modify backend servers in a specified vServer group, call the [ModifyVServerGroupBackendServers](~~35220~~) operation.
        *   If you want to add backend servers to a specified vServer group, call the [AddVServerGroupBackendServers](~~35218~~) operation.
        

        @param request: SetVServerGroupAttributeRequest

        @return: SetVServerGroupAttributeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.set_vserver_group_attribute_with_options(request, runtime)

    def start_load_balancer_listener_with_options(self, request, runtime):
        """
        When you call this operation, note the following items:
        *   You can call the operation only when the listener is in the Stopped state.
        *   After the operation is called, the status of the listener changes to Starting.
        *   You cannot call this operation when the SLB instance to which the listener is bound is in the Locked state.
        

        @param request: StartLoadBalancerListenerRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: StartLoadBalancerListenerResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.listener_port):
            query['ListenerPort'] = request.listener_port
        if not UtilClient.is_unset(request.listener_protocol):
            query['ListenerProtocol'] = request.listener_protocol
        if not UtilClient.is_unset(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartLoadBalancerListener',
            version='2014-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            slb_20140515_models.StartLoadBalancerListenerResponse(),
            self.call_api(params, req, runtime)
        )

    def start_load_balancer_listener(self, request):
        """
        When you call this operation, note the following items:
        *   You can call the operation only when the listener is in the Stopped state.
        *   After the operation is called, the status of the listener changes to Starting.
        *   You cannot call this operation when the SLB instance to which the listener is bound is in the Locked state.
        

        @param request: StartLoadBalancerListenerRequest

        @return: StartLoadBalancerListenerResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.start_load_balancer_listener_with_options(request, runtime)

    def stop_load_balancer_listener_with_options(self, request, runtime):
        """
        Before you make this API call, note the following:
        *   After the API call is successfully made, the listener enters the stopped state.
        *   If the Server Load Balancer (SLB) instance to which the listener to be stopped belongs is in the locked state, this API call cannot be made.
        >  If you stop the listener, your services will be disrupted. Exercise caution when you perform this action.
        

        @param request: StopLoadBalancerListenerRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: StopLoadBalancerListenerResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.listener_port):
            query['ListenerPort'] = request.listener_port
        if not UtilClient.is_unset(request.listener_protocol):
            query['ListenerProtocol'] = request.listener_protocol
        if not UtilClient.is_unset(request.load_balancer_id):
            query['LoadBalancerId'] = request.load_balancer_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StopLoadBalancerListener',
            version='2014-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            slb_20140515_models.StopLoadBalancerListenerResponse(),
            self.call_api(params, req, runtime)
        )

    def stop_load_balancer_listener(self, request):
        """
        Before you make this API call, note the following:
        *   After the API call is successfully made, the listener enters the stopped state.
        *   If the Server Load Balancer (SLB) instance to which the listener to be stopped belongs is in the locked state, this API call cannot be made.
        >  If you stop the listener, your services will be disrupted. Exercise caution when you perform this action.
        

        @param request: StopLoadBalancerListenerRequest

        @return: StopLoadBalancerListenerResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.stop_load_balancer_listener_with_options(request, runtime)

    def tag_resources_with_options(self, request, runtime):
        """
        >  You can add at most 20 tags to each instance. Before you add tags to a resource, Alibaba Cloud checks the number of existing tags of the resource. If the maximum number is reached, an error message is returned.
        

        @param request: TagResourcesRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: TagResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='TagResources',
            version='2014-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            slb_20140515_models.TagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    def tag_resources(self, request):
        """
        >  You can add at most 20 tags to each instance. Before you add tags to a resource, Alibaba Cloud checks the number of existing tags of the resource. If the maximum number is reached, an error message is returned.
        

        @param request: TagResourcesRequest

        @return: TagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.tag_resources_with_options(request, runtime)

    def untag_resources_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.all):
            query['All'] = request.all
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag_key):
            query['TagKey'] = request.tag_key
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UntagResources',
            version='2014-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            slb_20140515_models.UntagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    def untag_resources(self, request):
        runtime = util_models.RuntimeOptions()
        return self.untag_resources_with_options(request, runtime)

    def upload_cacertificate_with_options(self, request, runtime):
        """
        You can upload only one CA certificate at a time. After a CA certificate is uploaded, the certificate ID, name, and fingerprint are returned.
        

        @param request: UploadCACertificateRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: UploadCACertificateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.cacertificate):
            query['CACertificate'] = request.cacertificate
        if not UtilClient.is_unset(request.cacertificate_name):
            query['CACertificateName'] = request.cacertificate_name
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UploadCACertificate',
            version='2014-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            slb_20140515_models.UploadCACertificateResponse(),
            self.call_api(params, req, runtime)
        )

    def upload_cacertificate(self, request):
        """
        You can upload only one CA certificate at a time. After a CA certificate is uploaded, the certificate ID, name, and fingerprint are returned.
        

        @param request: UploadCACertificateRequest

        @return: UploadCACertificateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.upload_cacertificate_with_options(request, runtime)

    def upload_server_certificate_with_options(self, request, runtime):
        """
        You can upload only one server certificate and its private key in each call.
        *   After a server certificate and its private key are uploaded, the fingerprints of all server certificates that belong to your Alibaba Cloud account are returned.
        

        @param request: UploadServerCertificateRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: UploadServerCertificateResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ali_cloud_certificate_id):
            query['AliCloudCertificateId'] = request.ali_cloud_certificate_id
        if not UtilClient.is_unset(request.ali_cloud_certificate_name):
            query['AliCloudCertificateName'] = request.ali_cloud_certificate_name
        if not UtilClient.is_unset(request.ali_cloud_certificate_region_id):
            query['AliCloudCertificateRegionId'] = request.ali_cloud_certificate_region_id
        if not UtilClient.is_unset(request.owner_account):
            query['OwnerAccount'] = request.owner_account
        if not UtilClient.is_unset(request.owner_id):
            query['OwnerId'] = request.owner_id
        if not UtilClient.is_unset(request.private_key):
            query['PrivateKey'] = request.private_key
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_owner_account):
            query['ResourceOwnerAccount'] = request.resource_owner_account
        if not UtilClient.is_unset(request.resource_owner_id):
            query['ResourceOwnerId'] = request.resource_owner_id
        if not UtilClient.is_unset(request.server_certificate):
            query['ServerCertificate'] = request.server_certificate
        if not UtilClient.is_unset(request.server_certificate_name):
            query['ServerCertificateName'] = request.server_certificate_name
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UploadServerCertificate',
            version='2014-05-15',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            slb_20140515_models.UploadServerCertificateResponse(),
            self.call_api(params, req, runtime)
        )

    def upload_server_certificate(self, request):
        """
        You can upload only one server certificate and its private key in each call.
        *   After a server certificate and its private key are uploaded, the fingerprints of all server certificates that belong to your Alibaba Cloud account are returned.
        

        @param request: UploadServerCertificateRequest

        @return: UploadServerCertificateResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.upload_server_certificate_with_options(request, runtime)
