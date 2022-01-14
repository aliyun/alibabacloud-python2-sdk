# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_resourcemanager20200331 import models as resource_manager_20200331_models
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
        self._endpoint = self.get_endpoint('resourcemanager', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def accept_handshake_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.handshake_id):
            query['HandshakeId'] = request.handshake_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AcceptHandshake',
            version='2020-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.AcceptHandshakeResponse(),
            self.call_api(params, req, runtime)
        )

    def accept_handshake(self, request):
        runtime = util_models.RuntimeOptions()
        return self.accept_handshake_with_options(request, runtime)

    def attach_control_policy_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.policy_id):
            query['PolicyId'] = request.policy_id
        if not UtilClient.is_unset(request.target_id):
            query['TargetId'] = request.target_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AttachControlPolicy',
            version='2020-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.AttachControlPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    def attach_control_policy(self, request):
        runtime = util_models.RuntimeOptions()
        return self.attach_control_policy_with_options(request, runtime)

    def attach_policy_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.policy_name):
            query['PolicyName'] = request.policy_name
        if not UtilClient.is_unset(request.policy_type):
            query['PolicyType'] = request.policy_type
        if not UtilClient.is_unset(request.principal_name):
            query['PrincipalName'] = request.principal_name
        if not UtilClient.is_unset(request.principal_type):
            query['PrincipalType'] = request.principal_type
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AttachPolicy',
            version='2020-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.AttachPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    def attach_policy(self, request):
        runtime = util_models.RuntimeOptions()
        return self.attach_policy_with_options(request, runtime)

    def bind_secure_mobile_phone_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.secure_mobile_phone):
            query['SecureMobilePhone'] = request.secure_mobile_phone
        if not UtilClient.is_unset(request.verification_code):
            query['VerificationCode'] = request.verification_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='BindSecureMobilePhone',
            version='2020-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.BindSecureMobilePhoneResponse(),
            self.call_api(params, req, runtime)
        )

    def bind_secure_mobile_phone(self, request):
        runtime = util_models.RuntimeOptions()
        return self.bind_secure_mobile_phone_with_options(request, runtime)

    def cancel_create_cloud_account_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.record_id):
            query['RecordId'] = request.record_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CancelCreateCloudAccount',
            version='2020-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.CancelCreateCloudAccountResponse(),
            self.call_api(params, req, runtime)
        )

    def cancel_create_cloud_account(self, request):
        runtime = util_models.RuntimeOptions()
        return self.cancel_create_cloud_account_with_options(request, runtime)

    def cancel_handshake_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.handshake_id):
            query['HandshakeId'] = request.handshake_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CancelHandshake',
            version='2020-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.CancelHandshakeResponse(),
            self.call_api(params, req, runtime)
        )

    def cancel_handshake(self, request):
        runtime = util_models.RuntimeOptions()
        return self.cancel_handshake_with_options(request, runtime)

    def cancel_promote_resource_account_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.record_id):
            query['RecordId'] = request.record_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CancelPromoteResourceAccount',
            version='2020-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.CancelPromoteResourceAccountResponse(),
            self.call_api(params, req, runtime)
        )

    def cancel_promote_resource_account(self, request):
        runtime = util_models.RuntimeOptions()
        return self.cancel_promote_resource_account_with_options(request, runtime)

    def create_cloud_account_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.display_name):
            query['DisplayName'] = request.display_name
        if not UtilClient.is_unset(request.email):
            query['Email'] = request.email
        if not UtilClient.is_unset(request.parent_folder_id):
            query['ParentFolderId'] = request.parent_folder_id
        if not UtilClient.is_unset(request.payer_account_id):
            query['PayerAccountId'] = request.payer_account_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateCloudAccount',
            version='2020-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.CreateCloudAccountResponse(),
            self.call_api(params, req, runtime)
        )

    def create_cloud_account(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_cloud_account_with_options(request, runtime)

    def create_control_policy_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.effect_scope):
            query['EffectScope'] = request.effect_scope
        if not UtilClient.is_unset(request.policy_document):
            query['PolicyDocument'] = request.policy_document
        if not UtilClient.is_unset(request.policy_name):
            query['PolicyName'] = request.policy_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateControlPolicy',
            version='2020-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.CreateControlPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    def create_control_policy(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_control_policy_with_options(request, runtime)

    def create_folder_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.folder_name):
            query['FolderName'] = request.folder_name
        if not UtilClient.is_unset(request.parent_folder_id):
            query['ParentFolderId'] = request.parent_folder_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateFolder',
            version='2020-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.CreateFolderResponse(),
            self.call_api(params, req, runtime)
        )

    def create_folder(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_folder_with_options(request, runtime)

    def create_policy_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.policy_document):
            query['PolicyDocument'] = request.policy_document
        if not UtilClient.is_unset(request.policy_name):
            query['PolicyName'] = request.policy_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreatePolicy',
            version='2020-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.CreatePolicyResponse(),
            self.call_api(params, req, runtime)
        )

    def create_policy(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_policy_with_options(request, runtime)

    def create_policy_version_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.policy_document):
            query['PolicyDocument'] = request.policy_document
        if not UtilClient.is_unset(request.policy_name):
            query['PolicyName'] = request.policy_name
        if not UtilClient.is_unset(request.set_as_default):
            query['SetAsDefault'] = request.set_as_default
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreatePolicyVersion',
            version='2020-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.CreatePolicyVersionResponse(),
            self.call_api(params, req, runtime)
        )

    def create_policy_version(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_policy_version_with_options(request, runtime)

    def create_resource_account_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_name_prefix):
            query['AccountNamePrefix'] = request.account_name_prefix
        if not UtilClient.is_unset(request.display_name):
            query['DisplayName'] = request.display_name
        if not UtilClient.is_unset(request.parent_folder_id):
            query['ParentFolderId'] = request.parent_folder_id
        if not UtilClient.is_unset(request.payer_account_id):
            query['PayerAccountId'] = request.payer_account_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateResourceAccount',
            version='2020-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.CreateResourceAccountResponse(),
            self.call_api(params, req, runtime)
        )

    def create_resource_account(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_resource_account_with_options(request, runtime)

    def create_resource_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.display_name):
            query['DisplayName'] = request.display_name
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateResourceGroup',
            version='2020-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.CreateResourceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def create_resource_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_resource_group_with_options(request, runtime)

    def create_role_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.assume_role_policy_document):
            query['AssumeRolePolicyDocument'] = request.assume_role_policy_document
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.max_session_duration):
            query['MaxSessionDuration'] = request.max_session_duration
        if not UtilClient.is_unset(request.role_name):
            query['RoleName'] = request.role_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateRole',
            version='2020-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.CreateRoleResponse(),
            self.call_api(params, req, runtime)
        )

    def create_role(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_role_with_options(request, runtime)

    def create_service_linked_role_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.custom_suffix):
            query['CustomSuffix'] = request.custom_suffix
        if not UtilClient.is_unset(request.description):
            query['Description'] = request.description
        if not UtilClient.is_unset(request.service_name):
            query['ServiceName'] = request.service_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateServiceLinkedRole',
            version='2020-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.CreateServiceLinkedRoleResponse(),
            self.call_api(params, req, runtime)
        )

    def create_service_linked_role(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_service_linked_role_with_options(request, runtime)

    def decline_handshake_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.handshake_id):
            query['HandshakeId'] = request.handshake_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeclineHandshake',
            version='2020-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.DeclineHandshakeResponse(),
            self.call_api(params, req, runtime)
        )

    def decline_handshake(self, request):
        runtime = util_models.RuntimeOptions()
        return self.decline_handshake_with_options(request, runtime)

    def delete_control_policy_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.policy_id):
            query['PolicyId'] = request.policy_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteControlPolicy',
            version='2020-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.DeleteControlPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_control_policy(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_control_policy_with_options(request, runtime)

    def delete_folder_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.folder_id):
            query['FolderId'] = request.folder_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteFolder',
            version='2020-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.DeleteFolderResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_folder(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_folder_with_options(request, runtime)

    def delete_policy_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.policy_name):
            query['PolicyName'] = request.policy_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeletePolicy',
            version='2020-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.DeletePolicyResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_policy(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_policy_with_options(request, runtime)

    def delete_policy_version_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.policy_name):
            query['PolicyName'] = request.policy_name
        if not UtilClient.is_unset(request.version_id):
            query['VersionId'] = request.version_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeletePolicyVersion',
            version='2020-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.DeletePolicyVersionResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_policy_version(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_policy_version_with_options(request, runtime)

    def delete_resource_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteResourceGroup',
            version='2020-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.DeleteResourceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_resource_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_resource_group_with_options(request, runtime)

    def delete_role_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.role_name):
            query['RoleName'] = request.role_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteRole',
            version='2020-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.DeleteRoleResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_role(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_role_with_options(request, runtime)

    def delete_service_linked_role_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.role_name):
            query['RoleName'] = request.role_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteServiceLinkedRole',
            version='2020-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.DeleteServiceLinkedRoleResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_service_linked_role(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_service_linked_role_with_options(request, runtime)

    def deregister_delegated_administrator_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.service_principal):
            query['ServicePrincipal'] = request.service_principal
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeregisterDelegatedAdministrator',
            version='2020-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.DeregisterDelegatedAdministratorResponse(),
            self.call_api(params, req, runtime)
        )

    def deregister_delegated_administrator(self, request):
        runtime = util_models.RuntimeOptions()
        return self.deregister_delegated_administrator_with_options(request, runtime)

    def destroy_resource_directory_with_options(self, runtime):
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DestroyResourceDirectory',
            version='2020-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.DestroyResourceDirectoryResponse(),
            self.call_api(params, req, runtime)
        )

    def destroy_resource_directory(self):
        runtime = util_models.RuntimeOptions()
        return self.destroy_resource_directory_with_options(runtime)

    def detach_control_policy_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.policy_id):
            query['PolicyId'] = request.policy_id
        if not UtilClient.is_unset(request.target_id):
            query['TargetId'] = request.target_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DetachControlPolicy',
            version='2020-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.DetachControlPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    def detach_control_policy(self, request):
        runtime = util_models.RuntimeOptions()
        return self.detach_control_policy_with_options(request, runtime)

    def detach_policy_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.policy_name):
            query['PolicyName'] = request.policy_name
        if not UtilClient.is_unset(request.policy_type):
            query['PolicyType'] = request.policy_type
        if not UtilClient.is_unset(request.principal_name):
            query['PrincipalName'] = request.principal_name
        if not UtilClient.is_unset(request.principal_type):
            query['PrincipalType'] = request.principal_type
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DetachPolicy',
            version='2020-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.DetachPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    def detach_policy(self, request):
        runtime = util_models.RuntimeOptions()
        return self.detach_policy_with_options(request, runtime)

    def disable_control_policy_with_options(self, runtime):
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DisableControlPolicy',
            version='2020-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.DisableControlPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    def disable_control_policy(self):
        runtime = util_models.RuntimeOptions()
        return self.disable_control_policy_with_options(runtime)

    def enable_control_policy_with_options(self, runtime):
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='EnableControlPolicy',
            version='2020-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.EnableControlPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    def enable_control_policy(self):
        runtime = util_models.RuntimeOptions()
        return self.enable_control_policy_with_options(runtime)

    def enable_resource_directory_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.enable_mode):
            query['EnableMode'] = request.enable_mode
        if not UtilClient.is_unset(request.maname):
            query['MAName'] = request.maname
        if not UtilClient.is_unset(request.masecure_mobile_phone):
            query['MASecureMobilePhone'] = request.masecure_mobile_phone
        if not UtilClient.is_unset(request.verification_code):
            query['VerificationCode'] = request.verification_code
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='EnableResourceDirectory',
            version='2020-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.EnableResourceDirectoryResponse(),
            self.call_api(params, req, runtime)
        )

    def enable_resource_directory(self, request):
        runtime = util_models.RuntimeOptions()
        return self.enable_resource_directory_with_options(request, runtime)

    def get_account_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAccount',
            version='2020-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.GetAccountResponse(),
            self.call_api(params, req, runtime)
        )

    def get_account(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_account_with_options(request, runtime)

    def get_control_policy_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.language):
            query['Language'] = request.language
        if not UtilClient.is_unset(request.policy_id):
            query['PolicyId'] = request.policy_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetControlPolicy',
            version='2020-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.GetControlPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    def get_control_policy(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_control_policy_with_options(request, runtime)

    def get_control_policy_enablement_status_with_options(self, runtime):
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='GetControlPolicyEnablementStatus',
            version='2020-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.GetControlPolicyEnablementStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def get_control_policy_enablement_status(self):
        runtime = util_models.RuntimeOptions()
        return self.get_control_policy_enablement_status_with_options(runtime)

    def get_folder_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.folder_id):
            query['FolderId'] = request.folder_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetFolder',
            version='2020-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.GetFolderResponse(),
            self.call_api(params, req, runtime)
        )

    def get_folder(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_folder_with_options(request, runtime)

    def get_handshake_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.handshake_id):
            query['HandshakeId'] = request.handshake_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetHandshake',
            version='2020-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.GetHandshakeResponse(),
            self.call_api(params, req, runtime)
        )

    def get_handshake(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_handshake_with_options(request, runtime)

    def get_payer_for_account_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetPayerForAccount',
            version='2020-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.GetPayerForAccountResponse(),
            self.call_api(params, req, runtime)
        )

    def get_payer_for_account(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_payer_for_account_with_options(request, runtime)

    def get_policy_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.language):
            query['Language'] = request.language
        if not UtilClient.is_unset(request.policy_name):
            query['PolicyName'] = request.policy_name
        if not UtilClient.is_unset(request.policy_type):
            query['PolicyType'] = request.policy_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetPolicy',
            version='2020-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.GetPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    def get_policy(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_policy_with_options(request, runtime)

    def get_policy_version_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.policy_name):
            query['PolicyName'] = request.policy_name
        if not UtilClient.is_unset(request.policy_type):
            query['PolicyType'] = request.policy_type
        if not UtilClient.is_unset(request.version_id):
            query['VersionId'] = request.version_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetPolicyVersion',
            version='2020-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.GetPolicyVersionResponse(),
            self.call_api(params, req, runtime)
        )

    def get_policy_version(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_policy_version_with_options(request, runtime)

    def get_resource_directory_with_options(self, runtime):
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='GetResourceDirectory',
            version='2020-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.GetResourceDirectoryResponse(),
            self.call_api(params, req, runtime)
        )

    def get_resource_directory(self):
        runtime = util_models.RuntimeOptions()
        return self.get_resource_directory_with_options(runtime)

    def get_resource_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetResourceGroup',
            version='2020-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.GetResourceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def get_resource_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_resource_group_with_options(request, runtime)

    def get_role_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.language):
            query['Language'] = request.language
        if not UtilClient.is_unset(request.role_name):
            query['RoleName'] = request.role_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetRole',
            version='2020-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.GetRoleResponse(),
            self.call_api(params, req, runtime)
        )

    def get_role(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_role_with_options(request, runtime)

    def get_service_linked_role_deletion_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.deletion_task_id):
            query['DeletionTaskId'] = request.deletion_task_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetServiceLinkedRoleDeletionStatus',
            version='2020-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.GetServiceLinkedRoleDeletionStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def get_service_linked_role_deletion_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_service_linked_role_deletion_status_with_options(request, runtime)

    def init_resource_directory_with_options(self, runtime):
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='InitResourceDirectory',
            version='2020-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.InitResourceDirectoryResponse(),
            self.call_api(params, req, runtime)
        )

    def init_resource_directory(self):
        runtime = util_models.RuntimeOptions()
        return self.init_resource_directory_with_options(runtime)

    def invite_account_to_resource_directory_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.note):
            query['Note'] = request.note
        if not UtilClient.is_unset(request.target_entity):
            query['TargetEntity'] = request.target_entity
        if not UtilClient.is_unset(request.target_type):
            query['TargetType'] = request.target_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='InviteAccountToResourceDirectory',
            version='2020-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.InviteAccountToResourceDirectoryResponse(),
            self.call_api(params, req, runtime)
        )

    def invite_account_to_resource_directory(self, request):
        runtime = util_models.RuntimeOptions()
        return self.invite_account_to_resource_directory_with_options(request, runtime)

    def list_accounts_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAccounts',
            version='2020-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.ListAccountsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_accounts(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_accounts_with_options(request, runtime)

    def list_accounts_for_parent_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.parent_folder_id):
            query['ParentFolderId'] = request.parent_folder_id
        if not UtilClient.is_unset(request.query_keyword):
            query['QueryKeyword'] = request.query_keyword
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAccountsForParent',
            version='2020-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.ListAccountsForParentResponse(),
            self.call_api(params, req, runtime)
        )

    def list_accounts_for_parent(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_accounts_for_parent_with_options(request, runtime)

    def list_ancestors_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.child_id):
            query['ChildId'] = request.child_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAncestors',
            version='2020-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.ListAncestorsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_ancestors(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_ancestors_with_options(request, runtime)

    def list_control_policies_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.language):
            query['Language'] = request.language
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.policy_type):
            query['PolicyType'] = request.policy_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListControlPolicies',
            version='2020-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.ListControlPoliciesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_control_policies(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_control_policies_with_options(request, runtime)

    def list_control_policy_attachments_for_target_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.language):
            query['Language'] = request.language
        if not UtilClient.is_unset(request.target_id):
            query['TargetId'] = request.target_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListControlPolicyAttachmentsForTarget',
            version='2020-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.ListControlPolicyAttachmentsForTargetResponse(),
            self.call_api(params, req, runtime)
        )

    def list_control_policy_attachments_for_target(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_control_policy_attachments_for_target_with_options(request, runtime)

    def list_delegated_administrators_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.service_principal):
            query['ServicePrincipal'] = request.service_principal
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDelegatedAdministrators',
            version='2020-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.ListDelegatedAdministratorsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_delegated_administrators(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_delegated_administrators_with_options(request, runtime)

    def list_delegated_services_for_account_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListDelegatedServicesForAccount',
            version='2020-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.ListDelegatedServicesForAccountResponse(),
            self.call_api(params, req, runtime)
        )

    def list_delegated_services_for_account(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_delegated_services_for_account_with_options(request, runtime)

    def list_folders_for_parent_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.parent_folder_id):
            query['ParentFolderId'] = request.parent_folder_id
        if not UtilClient.is_unset(request.query_keyword):
            query['QueryKeyword'] = request.query_keyword
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListFoldersForParent',
            version='2020-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.ListFoldersForParentResponse(),
            self.call_api(params, req, runtime)
        )

    def list_folders_for_parent(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_folders_for_parent_with_options(request, runtime)

    def list_handshakes_for_account_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListHandshakesForAccount',
            version='2020-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.ListHandshakesForAccountResponse(),
            self.call_api(params, req, runtime)
        )

    def list_handshakes_for_account(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_handshakes_for_account_with_options(request, runtime)

    def list_handshakes_for_resource_directory_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListHandshakesForResourceDirectory',
            version='2020-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.ListHandshakesForResourceDirectoryResponse(),
            self.call_api(params, req, runtime)
        )

    def list_handshakes_for_resource_directory(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_handshakes_for_resource_directory_with_options(request, runtime)

    def list_policies_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.language):
            query['Language'] = request.language
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.policy_type):
            query['PolicyType'] = request.policy_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPolicies',
            version='2020-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.ListPoliciesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_policies(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_policies_with_options(request, runtime)

    def list_policy_attachments_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.language):
            query['Language'] = request.language
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.policy_name):
            query['PolicyName'] = request.policy_name
        if not UtilClient.is_unset(request.policy_type):
            query['PolicyType'] = request.policy_type
        if not UtilClient.is_unset(request.principal_name):
            query['PrincipalName'] = request.principal_name
        if not UtilClient.is_unset(request.principal_type):
            query['PrincipalType'] = request.principal_type
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPolicyAttachments',
            version='2020-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.ListPolicyAttachmentsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_policy_attachments(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_policy_attachments_with_options(request, runtime)

    def list_policy_versions_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.policy_name):
            query['PolicyName'] = request.policy_name
        if not UtilClient.is_unset(request.policy_type):
            query['PolicyType'] = request.policy_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPolicyVersions',
            version='2020-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.ListPolicyVersionsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_policy_versions(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_policy_versions_with_options(request, runtime)

    def list_resource_groups_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.display_name):
            query['DisplayName'] = request.display_name
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListResourceGroups',
            version='2020-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.ListResourceGroupsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_resource_groups(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_resource_groups_with_options(request, runtime)

    def list_resources_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.region):
            query['Region'] = request.region
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.service):
            query['Service'] = request.service
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListResources',
            version='2020-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.ListResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_resources(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_resources_with_options(request, runtime)

    def list_roles_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.language):
            query['Language'] = request.language
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListRoles',
            version='2020-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.ListRolesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_roles(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_roles_with_options(request, runtime)

    def list_target_attachments_for_control_policy_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.policy_id):
            query['PolicyId'] = request.policy_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTargetAttachmentsForControlPolicy',
            version='2020-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.ListTargetAttachmentsForControlPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    def list_target_attachments_for_control_policy(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_target_attachments_for_control_policy_with_options(request, runtime)

    def list_trusted_service_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.admin_account_id):
            query['AdminAccountId'] = request.admin_account_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTrustedServiceStatus',
            version='2020-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.ListTrustedServiceStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def list_trusted_service_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_trusted_service_status_with_options(request, runtime)

    def move_account_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.destination_folder_id):
            query['DestinationFolderId'] = request.destination_folder_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='MoveAccount',
            version='2020-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.MoveAccountResponse(),
            self.call_api(params, req, runtime)
        )

    def move_account(self, request):
        runtime = util_models.RuntimeOptions()
        return self.move_account_with_options(request, runtime)

    def move_resources_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resources):
            query['Resources'] = request.resources
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='MoveResources',
            version='2020-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.MoveResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    def move_resources(self, request):
        runtime = util_models.RuntimeOptions()
        return self.move_resources_with_options(request, runtime)

    def promote_resource_account_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.email):
            query['Email'] = request.email
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='PromoteResourceAccount',
            version='2020-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.PromoteResourceAccountResponse(),
            self.call_api(params, req, runtime)
        )

    def promote_resource_account(self, request):
        runtime = util_models.RuntimeOptions()
        return self.promote_resource_account_with_options(request, runtime)

    def register_delegated_administrator_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.service_principal):
            query['ServicePrincipal'] = request.service_principal
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RegisterDelegatedAdministrator',
            version='2020-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.RegisterDelegatedAdministratorResponse(),
            self.call_api(params, req, runtime)
        )

    def register_delegated_administrator(self, request):
        runtime = util_models.RuntimeOptions()
        return self.register_delegated_administrator_with_options(request, runtime)

    def remove_cloud_account_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RemoveCloudAccount',
            version='2020-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.RemoveCloudAccountResponse(),
            self.call_api(params, req, runtime)
        )

    def remove_cloud_account(self, request):
        runtime = util_models.RuntimeOptions()
        return self.remove_cloud_account_with_options(request, runtime)

    def resend_create_cloud_account_email_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.record_id):
            query['RecordId'] = request.record_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ResendCreateCloudAccountEmail',
            version='2020-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.ResendCreateCloudAccountEmailResponse(),
            self.call_api(params, req, runtime)
        )

    def resend_create_cloud_account_email(self, request):
        runtime = util_models.RuntimeOptions()
        return self.resend_create_cloud_account_email_with_options(request, runtime)

    def resend_promote_resource_account_email_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.record_id):
            query['RecordId'] = request.record_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ResendPromoteResourceAccountEmail',
            version='2020-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.ResendPromoteResourceAccountEmailResponse(),
            self.call_api(params, req, runtime)
        )

    def resend_promote_resource_account_email(self, request):
        runtime = util_models.RuntimeOptions()
        return self.resend_promote_resource_account_email_with_options(request, runtime)

    def send_verification_code_for_bind_secure_mobile_phone_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.secure_mobile_phone):
            query['SecureMobilePhone'] = request.secure_mobile_phone
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SendVerificationCodeForBindSecureMobilePhone',
            version='2020-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.SendVerificationCodeForBindSecureMobilePhoneResponse(),
            self.call_api(params, req, runtime)
        )

    def send_verification_code_for_bind_secure_mobile_phone(self, request):
        runtime = util_models.RuntimeOptions()
        return self.send_verification_code_for_bind_secure_mobile_phone_with_options(request, runtime)

    def send_verification_code_for_enable_rdwith_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.secure_mobile_phone):
            query['SecureMobilePhone'] = request.secure_mobile_phone
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SendVerificationCodeForEnableRD',
            version='2020-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.SendVerificationCodeForEnableRDResponse(),
            self.call_api(params, req, runtime)
        )

    def send_verification_code_for_enable_rd(self, request):
        runtime = util_models.RuntimeOptions()
        return self.send_verification_code_for_enable_rdwith_options(request, runtime)

    def set_default_policy_version_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.policy_name):
            query['PolicyName'] = request.policy_name
        if not UtilClient.is_unset(request.version_id):
            query['VersionId'] = request.version_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetDefaultPolicyVersion',
            version='2020-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.SetDefaultPolicyVersionResponse(),
            self.call_api(params, req, runtime)
        )

    def set_default_policy_version(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_default_policy_version_with_options(request, runtime)

    def update_account_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.new_account_type):
            query['NewAccountType'] = request.new_account_type
        if not UtilClient.is_unset(request.new_display_name):
            query['NewDisplayName'] = request.new_display_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateAccount',
            version='2020-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.UpdateAccountResponse(),
            self.call_api(params, req, runtime)
        )

    def update_account(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_account_with_options(request, runtime)

    def update_control_policy_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.new_description):
            query['NewDescription'] = request.new_description
        if not UtilClient.is_unset(request.new_policy_document):
            query['NewPolicyDocument'] = request.new_policy_document
        if not UtilClient.is_unset(request.new_policy_name):
            query['NewPolicyName'] = request.new_policy_name
        if not UtilClient.is_unset(request.policy_id):
            query['PolicyId'] = request.policy_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateControlPolicy',
            version='2020-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.UpdateControlPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    def update_control_policy(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_control_policy_with_options(request, runtime)

    def update_folder_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.folder_id):
            query['FolderId'] = request.folder_id
        if not UtilClient.is_unset(request.new_folder_name):
            query['NewFolderName'] = request.new_folder_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateFolder',
            version='2020-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.UpdateFolderResponse(),
            self.call_api(params, req, runtime)
        )

    def update_folder(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_folder_with_options(request, runtime)

    def update_resource_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.new_display_name):
            query['NewDisplayName'] = request.new_display_name
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateResourceGroup',
            version='2020-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.UpdateResourceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def update_resource_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_resource_group_with_options(request, runtime)

    def update_role_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.new_assume_role_policy_document):
            query['NewAssumeRolePolicyDocument'] = request.new_assume_role_policy_document
        if not UtilClient.is_unset(request.new_description):
            query['NewDescription'] = request.new_description
        if not UtilClient.is_unset(request.new_max_session_duration):
            query['NewMaxSessionDuration'] = request.new_max_session_duration
        if not UtilClient.is_unset(request.role_name):
            query['RoleName'] = request.role_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateRole',
            version='2020-03-31',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.UpdateRoleResponse(),
            self.call_api(params, req, runtime)
        )

    def update_role(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_role_with_options(request, runtime)
