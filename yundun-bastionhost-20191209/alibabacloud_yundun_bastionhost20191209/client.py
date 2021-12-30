# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_yundun_bastionhost20191209 import models as yundun_bastionhost_20191209_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_openapi_util.client import Client as OpenApiUtilClient


class Client(OpenApiClient):
    """
    *\
    """
    def __init__(self, config):
        super(Client, self).__init__(config)
        self._endpoint_rule = ''
        self.check_config(config)
        self._endpoint = self.get_endpoint('yundun-bastionhost', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def add_hosts_to_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.host_group_id):
            query['HostGroupId'] = request.host_group_id
        if not UtilClient.is_unset(request.host_ids):
            query['HostIds'] = request.host_ids
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddHostsToGroup',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.AddHostsToGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def add_hosts_to_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_hosts_to_group_with_options(request, runtime)

    def add_users_to_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.user_group_id):
            query['UserGroupId'] = request.user_group_id
        if not UtilClient.is_unset(request.user_ids):
            query['UserIds'] = request.user_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddUsersToGroup',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.AddUsersToGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def add_users_to_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_users_to_group_with_options(request, runtime)

    def attach_host_accounts_to_host_share_key_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.host_account_ids):
            query['HostAccountIds'] = request.host_account_ids
        if not UtilClient.is_unset(request.host_share_key_id):
            query['HostShareKeyId'] = request.host_share_key_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AttachHostAccountsToHostShareKey',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.AttachHostAccountsToHostShareKeyResponse(),
            self.call_api(params, req, runtime)
        )

    def attach_host_accounts_to_host_share_key(self, request):
        runtime = util_models.RuntimeOptions()
        return self.attach_host_accounts_to_host_share_key_with_options(request, runtime)

    def attach_host_accounts_to_user_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.hosts):
            query['Hosts'] = request.hosts
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AttachHostAccountsToUser',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.AttachHostAccountsToUserResponse(),
            self.call_api(params, req, runtime)
        )

    def attach_host_accounts_to_user(self, request):
        runtime = util_models.RuntimeOptions()
        return self.attach_host_accounts_to_user_with_options(request, runtime)

    def attach_host_accounts_to_user_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.hosts):
            query['Hosts'] = request.hosts
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.user_group_id):
            query['UserGroupId'] = request.user_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AttachHostAccountsToUserGroup',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.AttachHostAccountsToUserGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def attach_host_accounts_to_user_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.attach_host_accounts_to_user_group_with_options(request, runtime)

    def attach_host_group_accounts_to_user_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.host_groups):
            query['HostGroups'] = request.host_groups
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AttachHostGroupAccountsToUser',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.AttachHostGroupAccountsToUserResponse(),
            self.call_api(params, req, runtime)
        )

    def attach_host_group_accounts_to_user(self, request):
        runtime = util_models.RuntimeOptions()
        return self.attach_host_group_accounts_to_user_with_options(request, runtime)

    def attach_host_group_accounts_to_user_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.host_groups):
            query['HostGroups'] = request.host_groups
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.user_group_id):
            query['UserGroupId'] = request.user_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AttachHostGroupAccountsToUserGroup',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.AttachHostGroupAccountsToUserGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def attach_host_group_accounts_to_user_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.attach_host_group_accounts_to_user_group_with_options(request, runtime)

    def config_instance_security_groups_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.authorized_security_groups):
            query['AuthorizedSecurityGroups'] = request.authorized_security_groups
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ConfigInstanceSecurityGroups',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.ConfigInstanceSecurityGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    def config_instance_security_groups(self, request):
        runtime = util_models.RuntimeOptions()
        return self.config_instance_security_groups_with_options(request, runtime)

    def config_instance_white_list_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.white_list):
            query['WhiteList'] = request.white_list
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ConfigInstanceWhiteList',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.ConfigInstanceWhiteListResponse(),
            self.call_api(params, req, runtime)
        )

    def config_instance_white_list(self, request):
        runtime = util_models.RuntimeOptions()
        return self.config_instance_white_list_with_options(request, runtime)

    def create_host_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.active_address_type):
            query['ActiveAddressType'] = request.active_address_type
        if not UtilClient.is_unset(request.comment):
            query['Comment'] = request.comment
        if not UtilClient.is_unset(request.host_name):
            query['HostName'] = request.host_name
        if not UtilClient.is_unset(request.host_private_address):
            query['HostPrivateAddress'] = request.host_private_address
        if not UtilClient.is_unset(request.host_public_address):
            query['HostPublicAddress'] = request.host_public_address
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_region_id):
            query['InstanceRegionId'] = request.instance_region_id
        if not UtilClient.is_unset(request.ostype):
            query['OSType'] = request.ostype
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        if not UtilClient.is_unset(request.source_instance_id):
            query['SourceInstanceId'] = request.source_instance_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateHost',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.CreateHostResponse(),
            self.call_api(params, req, runtime)
        )

    def create_host(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_host_with_options(request, runtime)

    def create_host_account_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.host_account_name):
            query['HostAccountName'] = request.host_account_name
        if not UtilClient.is_unset(request.host_id):
            query['HostId'] = request.host_id
        if not UtilClient.is_unset(request.host_share_key_id):
            query['HostShareKeyId'] = request.host_share_key_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.pass_phrase):
            query['PassPhrase'] = request.pass_phrase
        if not UtilClient.is_unset(request.password):
            query['Password'] = request.password
        if not UtilClient.is_unset(request.private_key):
            query['PrivateKey'] = request.private_key
        if not UtilClient.is_unset(request.protocol_name):
            query['ProtocolName'] = request.protocol_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateHostAccount',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.CreateHostAccountResponse(),
            self.call_api(params, req, runtime)
        )

    def create_host_account(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_host_account_with_options(request, runtime)

    def create_host_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.comment):
            query['Comment'] = request.comment
        if not UtilClient.is_unset(request.host_group_name):
            query['HostGroupName'] = request.host_group_name
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateHostGroup',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.CreateHostGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def create_host_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_host_group_with_options(request, runtime)

    def create_host_share_key_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.host_share_key_name):
            query['HostShareKeyName'] = request.host_share_key_name
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.pass_phrase):
            query['PassPhrase'] = request.pass_phrase
        if not UtilClient.is_unset(request.private_key):
            query['PrivateKey'] = request.private_key
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateHostShareKey',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.CreateHostShareKeyResponse(),
            self.call_api(params, req, runtime)
        )

    def create_host_share_key(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_host_share_key_with_options(request, runtime)

    def create_user_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.comment):
            query['Comment'] = request.comment
        if not UtilClient.is_unset(request.display_name):
            query['DisplayName'] = request.display_name
        if not UtilClient.is_unset(request.email):
            query['Email'] = request.email
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.mobile):
            query['Mobile'] = request.mobile
        if not UtilClient.is_unset(request.mobile_country_code):
            query['MobileCountryCode'] = request.mobile_country_code
        if not UtilClient.is_unset(request.password):
            query['Password'] = request.password
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        if not UtilClient.is_unset(request.source_user_id):
            query['SourceUserId'] = request.source_user_id
        if not UtilClient.is_unset(request.user_name):
            query['UserName'] = request.user_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateUser',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.CreateUserResponse(),
            self.call_api(params, req, runtime)
        )

    def create_user(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_user_with_options(request, runtime)

    def create_user_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.comment):
            query['Comment'] = request.comment
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.user_group_name):
            query['UserGroupName'] = request.user_group_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateUserGroup',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.CreateUserGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def create_user_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_user_group_with_options(request, runtime)

    def delete_host_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.host_id):
            query['HostId'] = request.host_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteHost',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.DeleteHostResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_host(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_host_with_options(request, runtime)

    def delete_host_account_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.host_account_id):
            query['HostAccountId'] = request.host_account_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteHostAccount',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.DeleteHostAccountResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_host_account(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_host_account_with_options(request, runtime)

    def delete_host_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.host_group_id):
            query['HostGroupId'] = request.host_group_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteHostGroup',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.DeleteHostGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_host_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_host_group_with_options(request, runtime)

    def delete_host_share_key_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.host_share_key_id):
            query['HostShareKeyId'] = request.host_share_key_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteHostShareKey',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.DeleteHostShareKeyResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_host_share_key(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_host_share_key_with_options(request, runtime)

    def delete_user_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteUser',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.DeleteUserResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_user(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_user_with_options(request, runtime)

    def delete_user_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.user_group_id):
            query['UserGroupId'] = request.user_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteUserGroup',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.DeleteUserGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_user_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_user_group_with_options(request, runtime)

    def describe_instance_attribute_with_options(self, request, runtime):
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
            action='DescribeInstanceAttribute',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.DescribeInstanceAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_instance_attribute(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_instance_attribute_with_options(request, runtime)

    def describe_instances_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.instance_status):
            query['InstanceStatus'] = request.instance_status
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeInstances',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.DescribeInstancesResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_instances(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_instances_with_options(request, runtime)

    def describe_regions_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.accept_language):
            query['AcceptLanguage'] = request.accept_language
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeRegions',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.DescribeRegionsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_regions(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_regions_with_options(request, runtime)

    def detach_host_accounts_from_host_share_key_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.host_account_ids):
            query['HostAccountIds'] = request.host_account_ids
        if not UtilClient.is_unset(request.host_share_key_id):
            query['HostShareKeyId'] = request.host_share_key_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DetachHostAccountsFromHostShareKey',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.DetachHostAccountsFromHostShareKeyResponse(),
            self.call_api(params, req, runtime)
        )

    def detach_host_accounts_from_host_share_key(self, request):
        runtime = util_models.RuntimeOptions()
        return self.detach_host_accounts_from_host_share_key_with_options(request, runtime)

    def detach_host_accounts_from_user_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.hosts):
            query['Hosts'] = request.hosts
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DetachHostAccountsFromUser',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.DetachHostAccountsFromUserResponse(),
            self.call_api(params, req, runtime)
        )

    def detach_host_accounts_from_user(self, request):
        runtime = util_models.RuntimeOptions()
        return self.detach_host_accounts_from_user_with_options(request, runtime)

    def detach_host_accounts_from_user_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.hosts):
            query['Hosts'] = request.hosts
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.user_group_id):
            query['UserGroupId'] = request.user_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DetachHostAccountsFromUserGroup',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.DetachHostAccountsFromUserGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def detach_host_accounts_from_user_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.detach_host_accounts_from_user_group_with_options(request, runtime)

    def detach_host_group_accounts_from_user_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.host_groups):
            query['HostGroups'] = request.host_groups
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DetachHostGroupAccountsFromUser',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.DetachHostGroupAccountsFromUserResponse(),
            self.call_api(params, req, runtime)
        )

    def detach_host_group_accounts_from_user(self, request):
        runtime = util_models.RuntimeOptions()
        return self.detach_host_group_accounts_from_user_with_options(request, runtime)

    def detach_host_group_accounts_from_user_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.host_groups):
            query['HostGroups'] = request.host_groups
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.user_group_id):
            query['UserGroupId'] = request.user_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DetachHostGroupAccountsFromUserGroup',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.DetachHostGroupAccountsFromUserGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def detach_host_group_accounts_from_user_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.detach_host_group_accounts_from_user_group_with_options(request, runtime)

    def disable_instance_public_access_with_options(self, request, runtime):
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
            action='DisableInstancePublicAccess',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.DisableInstancePublicAccessResponse(),
            self.call_api(params, req, runtime)
        )

    def disable_instance_public_access(self, request):
        runtime = util_models.RuntimeOptions()
        return self.disable_instance_public_access_with_options(request, runtime)

    def enable_instance_public_access_with_options(self, request, runtime):
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
            action='EnableInstancePublicAccess',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.EnableInstancePublicAccessResponse(),
            self.call_api(params, req, runtime)
        )

    def enable_instance_public_access(self, request):
        runtime = util_models.RuntimeOptions()
        return self.enable_instance_public_access_with_options(request, runtime)

    def get_host_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.host_id):
            query['HostId'] = request.host_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetHost',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.GetHostResponse(),
            self.call_api(params, req, runtime)
        )

    def get_host(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_host_with_options(request, runtime)

    def get_host_account_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.host_account_id):
            query['HostAccountId'] = request.host_account_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetHostAccount',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.GetHostAccountResponse(),
            self.call_api(params, req, runtime)
        )

    def get_host_account(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_host_account_with_options(request, runtime)

    def get_host_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.host_group_id):
            query['HostGroupId'] = request.host_group_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetHostGroup',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.GetHostGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def get_host_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_host_group_with_options(request, runtime)

    def get_host_share_key_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.host_share_key_id):
            query['HostShareKeyId'] = request.host_share_key_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetHostShareKey',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.GetHostShareKeyResponse(),
            self.call_api(params, req, runtime)
        )

    def get_host_share_key(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_host_share_key_with_options(request, runtime)

    def get_instance_adauth_server_with_options(self, request, runtime):
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
            action='GetInstanceADAuthServer',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.GetInstanceADAuthServerResponse(),
            self.call_api(params, req, runtime)
        )

    def get_instance_adauth_server(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_instance_adauth_server_with_options(request, runtime)

    def get_instance_ldapauth_server_with_options(self, request, runtime):
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
            action='GetInstanceLDAPAuthServer',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.GetInstanceLDAPAuthServerResponse(),
            self.call_api(params, req, runtime)
        )

    def get_instance_ldapauth_server(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_instance_ldapauth_server_with_options(request, runtime)

    def get_instance_two_factor_with_options(self, request, runtime):
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
            action='GetInstanceTwoFactor',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.GetInstanceTwoFactorResponse(),
            self.call_api(params, req, runtime)
        )

    def get_instance_two_factor(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_instance_two_factor_with_options(request, runtime)

    def get_instance_upgrade_info_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetInstanceUpgradeInfo',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.GetInstanceUpgradeInfoResponse(),
            self.call_api(params, req, runtime)
        )

    def get_instance_upgrade_info(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_instance_upgrade_info_with_options(request, runtime)

    def get_user_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetUser',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.GetUserResponse(),
            self.call_api(params, req, runtime)
        )

    def get_user(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_user_with_options(request, runtime)

    def get_user_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.user_group_id):
            query['UserGroupId'] = request.user_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetUserGroup',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.GetUserGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def get_user_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_user_group_with_options(request, runtime)

    def list_host_accounts_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.host_account_name):
            query['HostAccountName'] = request.host_account_name
        if not UtilClient.is_unset(request.host_id):
            query['HostId'] = request.host_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.protocol_name):
            query['ProtocolName'] = request.protocol_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListHostAccounts',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.ListHostAccountsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_host_accounts(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_host_accounts_with_options(request, runtime)

    def list_host_accounts_for_host_share_key_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.host_share_key_id):
            query['HostShareKeyId'] = request.host_share_key_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListHostAccountsForHostShareKey',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.ListHostAccountsForHostShareKeyResponse(),
            self.call_api(params, req, runtime)
        )

    def list_host_accounts_for_host_share_key(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_host_accounts_for_host_share_key_with_options(request, runtime)

    def list_host_accounts_for_user_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.host_account_name):
            query['HostAccountName'] = request.host_account_name
        if not UtilClient.is_unset(request.host_id):
            query['HostId'] = request.host_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListHostAccountsForUser',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.ListHostAccountsForUserResponse(),
            self.call_api(params, req, runtime)
        )

    def list_host_accounts_for_user(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_host_accounts_for_user_with_options(request, runtime)

    def list_host_accounts_for_user_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.host_account_name):
            query['HostAccountName'] = request.host_account_name
        if not UtilClient.is_unset(request.host_id):
            query['HostId'] = request.host_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.user_group_id):
            query['UserGroupId'] = request.user_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListHostAccountsForUserGroup',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.ListHostAccountsForUserGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def list_host_accounts_for_user_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_host_accounts_for_user_group_with_options(request, runtime)

    def list_host_group_account_names_for_user_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.host_group_id):
            query['HostGroupId'] = request.host_group_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListHostGroupAccountNamesForUser',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.ListHostGroupAccountNamesForUserResponse(),
            self.call_api(params, req, runtime)
        )

    def list_host_group_account_names_for_user(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_host_group_account_names_for_user_with_options(request, runtime)

    def list_host_group_account_names_for_user_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.host_group_id):
            query['HostGroupId'] = request.host_group_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.user_group_id):
            query['UserGroupId'] = request.user_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListHostGroupAccountNamesForUserGroup',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.ListHostGroupAccountNamesForUserGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def list_host_group_account_names_for_user_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_host_group_account_names_for_user_group_with_options(request, runtime)

    def list_host_groups_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.host_group_name):
            query['HostGroupName'] = request.host_group_name
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListHostGroups',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.ListHostGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_host_groups(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_host_groups_with_options(request, runtime)

    def list_host_groups_for_user_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.host_group_name):
            query['HostGroupName'] = request.host_group_name
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.mode):
            query['Mode'] = request.mode
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListHostGroupsForUser',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.ListHostGroupsForUserResponse(),
            self.call_api(params, req, runtime)
        )

    def list_host_groups_for_user(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_host_groups_for_user_with_options(request, runtime)

    def list_host_groups_for_user_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.host_group_name):
            query['HostGroupName'] = request.host_group_name
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.mode):
            query['Mode'] = request.mode
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.user_group_id):
            query['UserGroupId'] = request.user_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListHostGroupsForUserGroup',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.ListHostGroupsForUserGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def list_host_groups_for_user_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_host_groups_for_user_group_with_options(request, runtime)

    def list_host_share_keys_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListHostShareKeys',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.ListHostShareKeysResponse(),
            self.call_api(params, req, runtime)
        )

    def list_host_share_keys(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_host_share_keys_with_options(request, runtime)

    def list_hosts_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.host_address):
            query['HostAddress'] = request.host_address
        if not UtilClient.is_unset(request.host_group_id):
            query['HostGroupId'] = request.host_group_id
        if not UtilClient.is_unset(request.host_name):
            query['HostName'] = request.host_name
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.ostype):
            query['OSType'] = request.ostype
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        if not UtilClient.is_unset(request.source_instance_id):
            query['SourceInstanceId'] = request.source_instance_id
        if not UtilClient.is_unset(request.source_instance_state):
            query['SourceInstanceState'] = request.source_instance_state
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListHosts',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.ListHostsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_hosts(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_hosts_with_options(request, runtime)

    def list_hosts_for_user_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.host_address):
            query['HostAddress'] = request.host_address
        if not UtilClient.is_unset(request.host_name):
            query['HostName'] = request.host_name
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.mode):
            query['Mode'] = request.mode
        if not UtilClient.is_unset(request.ostype):
            query['OSType'] = request.ostype
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListHostsForUser',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.ListHostsForUserResponse(),
            self.call_api(params, req, runtime)
        )

    def list_hosts_for_user(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_hosts_for_user_with_options(request, runtime)

    def list_hosts_for_user_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.host_address):
            query['HostAddress'] = request.host_address
        if not UtilClient.is_unset(request.host_name):
            query['HostName'] = request.host_name
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.mode):
            query['Mode'] = request.mode
        if not UtilClient.is_unset(request.ostype):
            query['OSType'] = request.ostype
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.user_group_id):
            query['UserGroupId'] = request.user_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListHostsForUserGroup',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.ListHostsForUserGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def list_hosts_for_user_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_hosts_for_user_group_with_options(request, runtime)

    def list_tag_keys_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTagKeys',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.ListTagKeysResponse(),
            self.call_api(params, req, runtime)
        )

    def list_tag_keys(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_tag_keys_with_options(request, runtime)

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
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.ListTagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_tag_resources(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_tag_resources_with_options(request, runtime)

    def list_user_groups_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.user_group_name):
            query['UserGroupName'] = request.user_group_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListUserGroups',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.ListUserGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_user_groups(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_user_groups_with_options(request, runtime)

    def list_users_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.display_name):
            query['DisplayName'] = request.display_name
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.mobile):
            query['Mobile'] = request.mobile
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.source):
            query['Source'] = request.source
        if not UtilClient.is_unset(request.source_user_id):
            query['SourceUserId'] = request.source_user_id
        if not UtilClient.is_unset(request.user_group_id):
            query['UserGroupId'] = request.user_group_id
        if not UtilClient.is_unset(request.user_name):
            query['UserName'] = request.user_name
        if not UtilClient.is_unset(request.user_state):
            query['UserState'] = request.user_state
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListUsers',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.ListUsersResponse(),
            self.call_api(params, req, runtime)
        )

    def list_users(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_users_with_options(request, runtime)

    def lock_users_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.user_ids):
            query['UserIds'] = request.user_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='LockUsers',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.LockUsersResponse(),
            self.call_api(params, req, runtime)
        )

    def lock_users(self, request):
        runtime = util_models.RuntimeOptions()
        return self.lock_users_with_options(request, runtime)

    def modify_host_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.comment):
            query['Comment'] = request.comment
        if not UtilClient.is_unset(request.host_id):
            query['HostId'] = request.host_id
        if not UtilClient.is_unset(request.host_name):
            query['HostName'] = request.host_name
        if not UtilClient.is_unset(request.host_private_address):
            query['HostPrivateAddress'] = request.host_private_address
        if not UtilClient.is_unset(request.host_public_address):
            query['HostPublicAddress'] = request.host_public_address
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.ostype):
            query['OSType'] = request.ostype
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyHost',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.ModifyHostResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_host(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_host_with_options(request, runtime)

    def modify_host_account_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.host_account_id):
            query['HostAccountId'] = request.host_account_id
        if not UtilClient.is_unset(request.host_account_name):
            query['HostAccountName'] = request.host_account_name
        if not UtilClient.is_unset(request.host_share_key_id):
            query['HostShareKeyId'] = request.host_share_key_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.pass_phrase):
            query['PassPhrase'] = request.pass_phrase
        if not UtilClient.is_unset(request.password):
            query['Password'] = request.password
        if not UtilClient.is_unset(request.private_key):
            query['PrivateKey'] = request.private_key
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyHostAccount',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.ModifyHostAccountResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_host_account(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_host_account_with_options(request, runtime)

    def modify_host_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.comment):
            query['Comment'] = request.comment
        if not UtilClient.is_unset(request.host_group_id):
            query['HostGroupId'] = request.host_group_id
        if not UtilClient.is_unset(request.host_group_name):
            query['HostGroupName'] = request.host_group_name
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyHostGroup',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.ModifyHostGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_host_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_host_group_with_options(request, runtime)

    def modify_host_share_key_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.host_share_key_id):
            query['HostShareKeyId'] = request.host_share_key_id
        if not UtilClient.is_unset(request.host_share_key_name):
            query['HostShareKeyName'] = request.host_share_key_name
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.pass_phrase):
            query['PassPhrase'] = request.pass_phrase
        if not UtilClient.is_unset(request.private_key):
            query['PrivateKey'] = request.private_key
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyHostShareKey',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.ModifyHostShareKeyResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_host_share_key(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_host_share_key_with_options(request, runtime)

    def modify_hosts_active_address_type_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.active_address_type):
            query['ActiveAddressType'] = request.active_address_type
        if not UtilClient.is_unset(request.host_ids):
            query['HostIds'] = request.host_ids
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyHostsActiveAddressType',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.ModifyHostsActiveAddressTypeResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_hosts_active_address_type(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_hosts_active_address_type_with_options(request, runtime)

    def modify_hosts_port_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.host_ids):
            query['HostIds'] = request.host_ids
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.port):
            query['Port'] = request.port
        if not UtilClient.is_unset(request.protocol_name):
            query['ProtocolName'] = request.protocol_name
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyHostsPort',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.ModifyHostsPortResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_hosts_port(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_hosts_port_with_options(request, runtime)

    def modify_instance_adauth_server_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account):
            query['Account'] = request.account
        if not UtilClient.is_unset(request.base_dn):
            query['BaseDN'] = request.base_dn
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.email_mapping):
            query['EmailMapping'] = request.email_mapping
        if not UtilClient.is_unset(request.filter):
            query['Filter'] = request.filter
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.is_ssl):
            query['IsSSL'] = request.is_ssl
        if not UtilClient.is_unset(request.mobile_mapping):
            query['MobileMapping'] = request.mobile_mapping
        if not UtilClient.is_unset(request.name_mapping):
            query['NameMapping'] = request.name_mapping
        if not UtilClient.is_unset(request.password):
            query['Password'] = request.password
        if not UtilClient.is_unset(request.port):
            query['Port'] = request.port
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.server):
            query['Server'] = request.server
        if not UtilClient.is_unset(request.standby_server):
            query['StandbyServer'] = request.standby_server
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyInstanceADAuthServer',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.ModifyInstanceADAuthServerResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_instance_adauth_server(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_instance_adauth_server_with_options(request, runtime)

    def modify_instance_attribute_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyInstanceAttribute',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.ModifyInstanceAttributeResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_instance_attribute(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_instance_attribute_with_options(request, runtime)

    def modify_instance_ldapauth_server_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account):
            query['Account'] = request.account
        if not UtilClient.is_unset(request.base_dn):
            query['BaseDN'] = request.base_dn
        if not UtilClient.is_unset(request.email_mapping):
            query['EmailMapping'] = request.email_mapping
        if not UtilClient.is_unset(request.filter):
            query['Filter'] = request.filter
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.is_ssl):
            query['IsSSL'] = request.is_ssl
        if not UtilClient.is_unset(request.login_name_mapping):
            query['LoginNameMapping'] = request.login_name_mapping
        if not UtilClient.is_unset(request.mobile_mapping):
            query['MobileMapping'] = request.mobile_mapping
        if not UtilClient.is_unset(request.name_mapping):
            query['NameMapping'] = request.name_mapping
        if not UtilClient.is_unset(request.password):
            query['Password'] = request.password
        if not UtilClient.is_unset(request.port):
            query['Port'] = request.port
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.server):
            query['Server'] = request.server
        if not UtilClient.is_unset(request.standby_server):
            query['StandbyServer'] = request.standby_server
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyInstanceLDAPAuthServer',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.ModifyInstanceLDAPAuthServerResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_instance_ldapauth_server(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_instance_ldapauth_server_with_options(request, runtime)

    def modify_instance_two_factor_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ding_talk_config):
            query['DingTalkConfig'] = request.ding_talk_config
        if not UtilClient.is_unset(request.enable_two_factor):
            query['EnableTwoFactor'] = request.enable_two_factor
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.message_language):
            query['MessageLanguage'] = request.message_language
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.skip_two_factor_time):
            query['SkipTwoFactorTime'] = request.skip_two_factor_time
        if not UtilClient.is_unset(request.two_factor_methods):
            query['TwoFactorMethods'] = request.two_factor_methods
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyInstanceTwoFactor',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.ModifyInstanceTwoFactorResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_instance_two_factor(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_instance_two_factor_with_options(request, runtime)

    def modify_instance_upgrade_period_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.upgrade_mode):
            query['UpgradeMode'] = request.upgrade_mode
        if not UtilClient.is_unset(request.upgrade_start_time):
            query['UpgradeStartTime'] = request.upgrade_start_time
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyInstanceUpgradePeriod',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.ModifyInstanceUpgradePeriodResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_instance_upgrade_period(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_instance_upgrade_period_with_options(request, runtime)

    def modify_user_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.comment):
            query['Comment'] = request.comment
        if not UtilClient.is_unset(request.display_name):
            query['DisplayName'] = request.display_name
        if not UtilClient.is_unset(request.email):
            query['Email'] = request.email
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.mobile):
            query['Mobile'] = request.mobile
        if not UtilClient.is_unset(request.mobile_country_code):
            query['MobileCountryCode'] = request.mobile_country_code
        if not UtilClient.is_unset(request.password):
            query['Password'] = request.password
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.user_id):
            query['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyUser',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.ModifyUserResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_user(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_user_with_options(request, runtime)

    def modify_user_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.comment):
            query['Comment'] = request.comment
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.user_group_id):
            query['UserGroupId'] = request.user_group_id
        if not UtilClient.is_unset(request.user_group_name):
            query['UserGroupName'] = request.user_group_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyUserGroup',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.ModifyUserGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_user_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_user_group_with_options(request, runtime)

    def move_resource_group_with_options(self, request, runtime):
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
            action='MoveResourceGroup',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.MoveResourceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def move_resource_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.move_resource_group_with_options(request, runtime)

    def remove_hosts_from_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.host_group_id):
            query['HostGroupId'] = request.host_group_id
        if not UtilClient.is_unset(request.host_ids):
            query['HostIds'] = request.host_ids
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemoveHostsFromGroup',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.RemoveHostsFromGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def remove_hosts_from_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.remove_hosts_from_group_with_options(request, runtime)

    def remove_users_from_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.user_group_id):
            query['UserGroupId'] = request.user_group_id
        if not UtilClient.is_unset(request.user_ids):
            query['UserIds'] = request.user_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemoveUsersFromGroup',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.RemoveUsersFromGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def remove_users_from_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.remove_users_from_group_with_options(request, runtime)

    def reset_host_account_credential_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.credential_type):
            query['CredentialType'] = request.credential_type
        if not UtilClient.is_unset(request.host_account_id):
            query['HostAccountId'] = request.host_account_id
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ResetHostAccountCredential',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.ResetHostAccountCredentialResponse(),
            self.call_api(params, req, runtime)
        )

    def reset_host_account_credential(self, request):
        runtime = util_models.RuntimeOptions()
        return self.reset_host_account_credential_with_options(request, runtime)

    def start_instance_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.security_group_ids):
            query['SecurityGroupIds'] = request.security_group_ids
        if not UtilClient.is_unset(request.vswitch_id):
            query['VswitchId'] = request.vswitch_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='StartInstance',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.StartInstanceResponse(),
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
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.TagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    def tag_resources(self, request):
        runtime = util_models.RuntimeOptions()
        return self.tag_resources_with_options(request, runtime)

    def unlock_users_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.user_ids):
            query['UserIds'] = request.user_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UnlockUsers',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.UnlockUsersResponse(),
            self.call_api(params, req, runtime)
        )

    def unlock_users(self, request):
        runtime = util_models.RuntimeOptions()
        return self.unlock_users_with_options(request, runtime)

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
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.UntagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    def untag_resources(self, request):
        runtime = util_models.RuntimeOptions()
        return self.untag_resources_with_options(request, runtime)

    def upgrade_instance_image_version_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.lang):
            query['Lang'] = request.lang
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpgradeInstanceImageVersion',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.UpgradeInstanceImageVersionResponse(),
            self.call_api(params, req, runtime)
        )

    def upgrade_instance_image_version(self, request):
        runtime = util_models.RuntimeOptions()
        return self.upgrade_instance_image_version_with_options(request, runtime)

    def verify_instance_adauth_server_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account):
            query['Account'] = request.account
        if not UtilClient.is_unset(request.base_dn):
            query['BaseDN'] = request.base_dn
        if not UtilClient.is_unset(request.domain):
            query['Domain'] = request.domain
        if not UtilClient.is_unset(request.filter):
            query['Filter'] = request.filter
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.is_ssl):
            query['IsSSL'] = request.is_ssl
        if not UtilClient.is_unset(request.password):
            query['Password'] = request.password
        if not UtilClient.is_unset(request.port):
            query['Port'] = request.port
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.server):
            query['Server'] = request.server
        if not UtilClient.is_unset(request.standby_server):
            query['StandbyServer'] = request.standby_server
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='VerifyInstanceADAuthServer',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.VerifyInstanceADAuthServerResponse(),
            self.call_api(params, req, runtime)
        )

    def verify_instance_adauth_server(self, request):
        runtime = util_models.RuntimeOptions()
        return self.verify_instance_adauth_server_with_options(request, runtime)

    def verify_instance_ldapauth_server_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account):
            query['Account'] = request.account
        if not UtilClient.is_unset(request.base_dn):
            query['BaseDN'] = request.base_dn
        if not UtilClient.is_unset(request.filter):
            query['Filter'] = request.filter
        if not UtilClient.is_unset(request.instance_id):
            query['InstanceId'] = request.instance_id
        if not UtilClient.is_unset(request.is_ssl):
            query['IsSSL'] = request.is_ssl
        if not UtilClient.is_unset(request.password):
            query['Password'] = request.password
        if not UtilClient.is_unset(request.port):
            query['Port'] = request.port
        if not UtilClient.is_unset(request.region_id):
            query['RegionId'] = request.region_id
        if not UtilClient.is_unset(request.server):
            query['Server'] = request.server
        if not UtilClient.is_unset(request.standby_server):
            query['StandbyServer'] = request.standby_server
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='VerifyInstanceLDAPAuthServer',
            version='2019-12-09',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            yundun_bastionhost_20191209_models.VerifyInstanceLDAPAuthServerResponse(),
            self.call_api(params, req, runtime)
        )

    def verify_instance_ldapauth_server(self, request):
        runtime = util_models.RuntimeOptions()
        return self.verify_instance_ldapauth_server_with_options(request, runtime)
