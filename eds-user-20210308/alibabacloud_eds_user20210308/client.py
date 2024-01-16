# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_eds_user20210308 import models as eds_user_20210308_models
from alibabacloud_tea_util import models as util_models
from alibabacloud_openapi_util.client import Client as OpenApiUtilClient


class Client(OpenApiClient):
    """
    *\
    """
    def __init__(self, config):
        super(Client, self).__init__(config)
        self._endpoint_rule = 'regional'
        self.check_config(config)
        self._endpoint = self.get_endpoint('eds-user', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def check_used_property_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.property_id):
            query['PropertyId'] = request.property_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CheckUsedProperty',
            version='2021-03-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eds_user_20210308_models.CheckUsedPropertyResponse(),
            self.call_api(params, req, runtime)
        )

    def check_used_property(self, request):
        runtime = util_models.RuntimeOptions()
        return self.check_used_property_with_options(request, runtime)

    def check_used_property_value_with_options(self, request, runtime):
        """
        Before you call the operation, you can call the [ListProperty](~~410890~~) operation to query the existing user properties and their IDs (PropertyId) and values (PropertyValueId).
        

        @param request: CheckUsedPropertyValueRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CheckUsedPropertyValueResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.property_id):
            query['PropertyId'] = request.property_id
        if not UtilClient.is_unset(request.property_value_id):
            query['PropertyValueId'] = request.property_value_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CheckUsedPropertyValue',
            version='2021-03-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eds_user_20210308_models.CheckUsedPropertyValueResponse(),
            self.call_api(params, req, runtime)
        )

    def check_used_property_value(self, request):
        """
        Before you call the operation, you can call the [ListProperty](~~410890~~) operation to query the existing user properties and their IDs (PropertyId) and values (PropertyValueId).
        

        @param request: CheckUsedPropertyValueRequest

        @return: CheckUsedPropertyValueResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.check_used_property_value_with_options(request, runtime)

    def create_property_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.property_key):
            body['PropertyKey'] = request.property_key
        if not UtilClient.is_unset(request.property_values):
            body['PropertyValues'] = request.property_values
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateProperty',
            version='2021-03-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eds_user_20210308_models.CreatePropertyResponse(),
            self.call_api(params, req, runtime)
        )

    def create_property(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_property_with_options(request, runtime)

    def create_users_with_options(self, request, runtime):
        """
        Convenience users are dedicated Elastic Desktop Service (EDS) user accounts and are suitable for scenarios in which you do not need to connect to enterprise Active Directory (AD) systems. The information about a convenience user includes the username, email address, and mobile number. You must specify the username or email address.
        

        @param request: CreateUsersRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateUsersResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_lock_time):
            query['AutoLockTime'] = request.auto_lock_time
        body = {}
        if not UtilClient.is_unset(request.password):
            body['Password'] = request.password
        if not UtilClient.is_unset(request.users):
            body['Users'] = request.users
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='CreateUsers',
            version='2021-03-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eds_user_20210308_models.CreateUsersResponse(),
            self.call_api(params, req, runtime)
        )

    def create_users(self, request):
        """
        Convenience users are dedicated Elastic Desktop Service (EDS) user accounts and are suitable for scenarios in which you do not need to connect to enterprise Active Directory (AD) systems. The information about a convenience user includes the username, email address, and mobile number. You must specify the username or email address.
        

        @param request: CreateUsersRequest

        @return: CreateUsersResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_users_with_options(request, runtime)

    def delete_user_property_value_with_options(self, request, runtime):
        """
        The operation that you want to perform. Set the value to *DeleteUserPropertyValue**.
        

        @param request: DeleteUserPropertyValueRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteUserPropertyValueResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.property_id):
            body['PropertyId'] = request.property_id
        if not UtilClient.is_unset(request.property_value_id):
            body['PropertyValueId'] = request.property_value_id
        if not UtilClient.is_unset(request.user_id):
            body['UserId'] = request.user_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DeleteUserPropertyValue',
            version='2021-03-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eds_user_20210308_models.DeleteUserPropertyValueResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_user_property_value(self, request):
        """
        The operation that you want to perform. Set the value to *DeleteUserPropertyValue**.
        

        @param request: DeleteUserPropertyValueRequest

        @return: DeleteUserPropertyValueResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_user_property_value_with_options(request, runtime)

    def describe_mfa_devices_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ad_domain):
            query['AdDomain'] = request.ad_domain
        if not UtilClient.is_unset(request.end_user_ids):
            query['EndUserIds'] = request.end_user_ids
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.serial_numbers):
            query['SerialNumbers'] = request.serial_numbers
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DescribeMfaDevices',
            version='2021-03-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eds_user_20210308_models.DescribeMfaDevicesResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_mfa_devices(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_mfa_devices_with_options(request, runtime)

    def describe_users_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.filter):
            query['Filter'] = request.filter
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        body = {}
        if not UtilClient.is_unset(request.biz_type):
            body['BizType'] = request.biz_type
        if not UtilClient.is_unset(request.end_user_ids):
            body['EndUserIds'] = request.end_user_ids
        if not UtilClient.is_unset(request.exclude_end_user_ids):
            body['ExcludeEndUserIds'] = request.exclude_end_user_ids
        if not UtilClient.is_unset(request.group_id):
            body['GroupId'] = request.group_id
        if not UtilClient.is_unset(request.org_id):
            body['OrgId'] = request.org_id
        if not UtilClient.is_unset(request.solution_id):
            body['SolutionId'] = request.solution_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='DescribeUsers',
            version='2021-03-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eds_user_20210308_models.DescribeUsersResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_users(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_users_with_options(request, runtime)

    def filter_users_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = eds_user_20210308_models.FilterUsersShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.order_param):
            request.order_param_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.order_param, 'OrderParam', 'json')
        query = {}
        if not UtilClient.is_unset(request.exclude_end_user_ids):
            query['ExcludeEndUserIds'] = request.exclude_end_user_ids
        if not UtilClient.is_unset(request.filter):
            query['Filter'] = request.filter
        if not UtilClient.is_unset(request.include_desktop_count):
            query['IncludeDesktopCount'] = request.include_desktop_count
        if not UtilClient.is_unset(request.include_desktop_group_count):
            query['IncludeDesktopGroupCount'] = request.include_desktop_group_count
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.order_param_shrink):
            query['OrderParam'] = request.order_param_shrink
        if not UtilClient.is_unset(request.org_id):
            query['OrgId'] = request.org_id
        if not UtilClient.is_unset(request.owner_type):
            query['OwnerType'] = request.owner_type
        if not UtilClient.is_unset(request.property_filter_param):
            query['PropertyFilterParam'] = request.property_filter_param
        if not UtilClient.is_unset(request.property_key_value_filter_param):
            query['PropertyKeyValueFilterParam'] = request.property_key_value_filter_param
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='FilterUsers',
            version='2021-03-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eds_user_20210308_models.FilterUsersResponse(),
            self.call_api(params, req, runtime)
        )

    def filter_users(self, request):
        runtime = util_models.RuntimeOptions()
        return self.filter_users_with_options(request, runtime)

    def get_manager_info_by_auth_code_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auth_code):
            query['AuthCode'] = request.auth_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetManagerInfoByAuthCode',
            version='2021-03-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eds_user_20210308_models.GetManagerInfoByAuthCodeResponse(),
            self.call_api(params, req, runtime)
        )

    def get_manager_info_by_auth_code(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_manager_info_by_auth_code_with_options(request, runtime)

    def list_property_with_options(self, runtime):
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='ListProperty',
            version='2021-03-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eds_user_20210308_models.ListPropertyResponse(),
            self.call_api(params, req, runtime)
        )

    def list_property(self):
        runtime = util_models.RuntimeOptions()
        return self.list_property_with_options(runtime)

    def list_property_value_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.property_id):
            query['PropertyId'] = request.property_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPropertyValue',
            version='2021-03-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eds_user_20210308_models.ListPropertyValueResponse(),
            self.call_api(params, req, runtime)
        )

    def list_property_value(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_property_value_with_options(request, runtime)

    def lock_mfa_device_with_options(self, request, runtime):
        """
        ## Description
        After a virtual MFA device is locked, the status of the virtual MFA device changes to LOCKED. The convenience user to which the MFA device is bound cannot log on to the cloud desktop that resides in the workspace with the MFA feature enabled because the convenience user will fail authentication based on the virtual MFA device. You can call the UnlockMfaDevice operation to unlock the virtual MFA device.
        

        @param request: LockMfaDeviceRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: LockMfaDeviceResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ad_domain):
            query['AdDomain'] = request.ad_domain
        if not UtilClient.is_unset(request.serial_number):
            query['SerialNumber'] = request.serial_number
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='LockMfaDevice',
            version='2021-03-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eds_user_20210308_models.LockMfaDeviceResponse(),
            self.call_api(params, req, runtime)
        )

    def lock_mfa_device(self, request):
        """
        ## Description
        After a virtual MFA device is locked, the status of the virtual MFA device changes to LOCKED. The convenience user to which the MFA device is bound cannot log on to the cloud desktop that resides in the workspace with the MFA feature enabled because the convenience user will fail authentication based on the virtual MFA device. You can call the UnlockMfaDevice operation to unlock the virtual MFA device.
        

        @param request: LockMfaDeviceRequest

        @return: LockMfaDeviceResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.lock_mfa_device_with_options(request, runtime)

    def lock_users_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.users):
            body['Users'] = request.users
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='LockUsers',
            version='2021-03-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eds_user_20210308_models.LockUsersResponse(),
            self.call_api(params, req, runtime)
        )

    def lock_users(self, request):
        runtime = util_models.RuntimeOptions()
        return self.lock_users_with_options(request, runtime)

    def modify_user_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.email):
            query['Email'] = request.email
        if not UtilClient.is_unset(request.end_user_id):
            query['EndUserId'] = request.end_user_id
        if not UtilClient.is_unset(request.phone):
            query['Phone'] = request.phone
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ModifyUser',
            version='2021-03-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eds_user_20210308_models.ModifyUserResponse(),
            self.call_api(params, req, runtime)
        )

    def modify_user(self, request):
        runtime = util_models.RuntimeOptions()
        return self.modify_user_with_options(request, runtime)

    def query_sync_status_by_ali_uid_with_options(self, runtime):
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='QuerySyncStatusByAliUid',
            version='2021-03-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eds_user_20210308_models.QuerySyncStatusByAliUidResponse(),
            self.call_api(params, req, runtime)
        )

    def query_sync_status_by_ali_uid(self):
        runtime = util_models.RuntimeOptions()
        return self.query_sync_status_by_ali_uid_with_options(runtime)

    def remove_mfa_device_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ad_domain):
            query['AdDomain'] = request.ad_domain
        if not UtilClient.is_unset(request.serial_number):
            query['SerialNumber'] = request.serial_number
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemoveMfaDevice',
            version='2021-03-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eds_user_20210308_models.RemoveMfaDeviceResponse(),
            self.call_api(params, req, runtime)
        )

    def remove_mfa_device(self, request):
        runtime = util_models.RuntimeOptions()
        return self.remove_mfa_device_with_options(request, runtime)

    def remove_property_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.property_id):
            body['PropertyId'] = request.property_id
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RemoveProperty',
            version='2021-03-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eds_user_20210308_models.RemovePropertyResponse(),
            self.call_api(params, req, runtime)
        )

    def remove_property(self, request):
        runtime = util_models.RuntimeOptions()
        return self.remove_property_with_options(request, runtime)

    def remove_users_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.users):
            body['Users'] = request.users
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='RemoveUsers',
            version='2021-03-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eds_user_20210308_models.RemoveUsersResponse(),
            self.call_api(params, req, runtime)
        )

    def remove_users(self, request):
        runtime = util_models.RuntimeOptions()
        return self.remove_users_with_options(request, runtime)

    def reset_user_password_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.notify_type):
            body['NotifyType'] = request.notify_type
        if not UtilClient.is_unset(request.users):
            body['Users'] = request.users
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='ResetUserPassword',
            version='2021-03-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eds_user_20210308_models.ResetUserPasswordResponse(),
            self.call_api(params, req, runtime)
        )

    def reset_user_password(self, request):
        runtime = util_models.RuntimeOptions()
        return self.reset_user_password_with_options(request, runtime)

    def set_user_property_value_with_options(self, request, runtime):
        """
        The ID of the request.
        

        @param request: SetUserPropertyValueRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: SetUserPropertyValueResponse
        """
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.property_id):
            body['PropertyId'] = request.property_id
        if not UtilClient.is_unset(request.property_value_id):
            body['PropertyValueId'] = request.property_value_id
        if not UtilClient.is_unset(request.user_id):
            body['UserId'] = request.user_id
        if not UtilClient.is_unset(request.user_name):
            body['UserName'] = request.user_name
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='SetUserPropertyValue',
            version='2021-03-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eds_user_20210308_models.SetUserPropertyValueResponse(),
            self.call_api(params, req, runtime)
        )

    def set_user_property_value(self, request):
        """
        The ID of the request.
        

        @param request: SetUserPropertyValueRequest

        @return: SetUserPropertyValueResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.set_user_property_value_with_options(request, runtime)

    def sync_all_edu_info_with_options(self, runtime):
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='SyncAllEduInfo',
            version='2021-03-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eds_user_20210308_models.SyncAllEduInfoResponse(),
            self.call_api(params, req, runtime)
        )

    def sync_all_edu_info(self):
        runtime = util_models.RuntimeOptions()
        return self.sync_all_edu_info_with_options(runtime)

    def unlock_mfa_device_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.ad_domain):
            query['AdDomain'] = request.ad_domain
        if not UtilClient.is_unset(request.serial_number):
            query['SerialNumber'] = request.serial_number
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UnlockMfaDevice',
            version='2021-03-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eds_user_20210308_models.UnlockMfaDeviceResponse(),
            self.call_api(params, req, runtime)
        )

    def unlock_mfa_device(self, request):
        runtime = util_models.RuntimeOptions()
        return self.unlock_mfa_device_with_options(request, runtime)

    def unlock_users_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.auto_lock_time):
            query['AutoLockTime'] = request.auto_lock_time
        body = {}
        if not UtilClient.is_unset(request.users):
            body['Users'] = request.users
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query),
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UnlockUsers',
            version='2021-03-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eds_user_20210308_models.UnlockUsersResponse(),
            self.call_api(params, req, runtime)
        )

    def unlock_users(self, request):
        runtime = util_models.RuntimeOptions()
        return self.unlock_users_with_options(request, runtime)

    def update_property_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        body = {}
        if not UtilClient.is_unset(request.property_id):
            body['PropertyId'] = request.property_id
        if not UtilClient.is_unset(request.property_key):
            body['PropertyKey'] = request.property_key
        if not UtilClient.is_unset(request.property_values):
            body['PropertyValues'] = request.property_values
        req = open_api_models.OpenApiRequest(
            body=OpenApiUtilClient.parse_to_map(body)
        )
        params = open_api_models.Params(
            action='UpdateProperty',
            version='2021-03-08',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            eds_user_20210308_models.UpdatePropertyResponse(),
            self.call_api(params, req, runtime)
        )

    def update_property(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_property_with_options(request, runtime)
