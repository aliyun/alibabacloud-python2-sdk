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
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.AcceptHandshakeResponse(),
            self.do_rpcrequest('AcceptHandshake', '2020-03-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def accept_handshake(self, request):
        runtime = util_models.RuntimeOptions()
        return self.accept_handshake_with_options(request, runtime)

    def attach_control_policy_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.AttachControlPolicyResponse(),
            self.do_rpcrequest('AttachControlPolicy', '2020-03-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def attach_control_policy(self, request):
        runtime = util_models.RuntimeOptions()
        return self.attach_control_policy_with_options(request, runtime)

    def attach_policy_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.AttachPolicyResponse(),
            self.do_rpcrequest('AttachPolicy', '2020-03-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def attach_policy(self, request):
        runtime = util_models.RuntimeOptions()
        return self.attach_policy_with_options(request, runtime)

    def cancel_create_cloud_account_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.CancelCreateCloudAccountResponse(),
            self.do_rpcrequest('CancelCreateCloudAccount', '2020-03-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def cancel_create_cloud_account(self, request):
        runtime = util_models.RuntimeOptions()
        return self.cancel_create_cloud_account_with_options(request, runtime)

    def cancel_handshake_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.CancelHandshakeResponse(),
            self.do_rpcrequest('CancelHandshake', '2020-03-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def cancel_handshake(self, request):
        runtime = util_models.RuntimeOptions()
        return self.cancel_handshake_with_options(request, runtime)

    def cancel_promote_resource_account_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.CancelPromoteResourceAccountResponse(),
            self.do_rpcrequest('CancelPromoteResourceAccount', '2020-03-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def cancel_promote_resource_account(self, request):
        runtime = util_models.RuntimeOptions()
        return self.cancel_promote_resource_account_with_options(request, runtime)

    def create_cloud_account_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.CreateCloudAccountResponse(),
            self.do_rpcrequest('CreateCloudAccount', '2020-03-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_cloud_account(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_cloud_account_with_options(request, runtime)

    def create_control_policy_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.CreateControlPolicyResponse(),
            self.do_rpcrequest('CreateControlPolicy', '2020-03-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_control_policy(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_control_policy_with_options(request, runtime)

    def create_folder_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.CreateFolderResponse(),
            self.do_rpcrequest('CreateFolder', '2020-03-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_folder(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_folder_with_options(request, runtime)

    def create_policy_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.CreatePolicyResponse(),
            self.do_rpcrequest('CreatePolicy', '2020-03-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_policy(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_policy_with_options(request, runtime)

    def create_policy_version_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.CreatePolicyVersionResponse(),
            self.do_rpcrequest('CreatePolicyVersion', '2020-03-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_policy_version(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_policy_version_with_options(request, runtime)

    def create_resource_account_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.CreateResourceAccountResponse(),
            self.do_rpcrequest('CreateResourceAccount', '2020-03-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_resource_account(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_resource_account_with_options(request, runtime)

    def create_resource_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.CreateResourceGroupResponse(),
            self.do_rpcrequest('CreateResourceGroup', '2020-03-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_resource_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_resource_group_with_options(request, runtime)

    def create_role_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.CreateRoleResponse(),
            self.do_rpcrequest('CreateRole', '2020-03-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_role(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_role_with_options(request, runtime)

    def create_service_linked_role_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.CreateServiceLinkedRoleResponse(),
            self.do_rpcrequest('CreateServiceLinkedRole', '2020-03-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def create_service_linked_role(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_service_linked_role_with_options(request, runtime)

    def decline_handshake_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.DeclineHandshakeResponse(),
            self.do_rpcrequest('DeclineHandshake', '2020-03-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def decline_handshake(self, request):
        runtime = util_models.RuntimeOptions()
        return self.decline_handshake_with_options(request, runtime)

    def delete_control_policy_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.DeleteControlPolicyResponse(),
            self.do_rpcrequest('DeleteControlPolicy', '2020-03-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_control_policy(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_control_policy_with_options(request, runtime)

    def delete_folder_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.DeleteFolderResponse(),
            self.do_rpcrequest('DeleteFolder', '2020-03-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_folder(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_folder_with_options(request, runtime)

    def delete_policy_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.DeletePolicyResponse(),
            self.do_rpcrequest('DeletePolicy', '2020-03-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_policy(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_policy_with_options(request, runtime)

    def delete_policy_version_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.DeletePolicyVersionResponse(),
            self.do_rpcrequest('DeletePolicyVersion', '2020-03-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_policy_version(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_policy_version_with_options(request, runtime)

    def delete_resource_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.DeleteResourceGroupResponse(),
            self.do_rpcrequest('DeleteResourceGroup', '2020-03-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_resource_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_resource_group_with_options(request, runtime)

    def delete_role_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.DeleteRoleResponse(),
            self.do_rpcrequest('DeleteRole', '2020-03-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_role(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_role_with_options(request, runtime)

    def delete_service_linked_role_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.DeleteServiceLinkedRoleResponse(),
            self.do_rpcrequest('DeleteServiceLinkedRole', '2020-03-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def delete_service_linked_role(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_service_linked_role_with_options(request, runtime)

    def deregister_delegated_administrator_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.DeregisterDelegatedAdministratorResponse(),
            self.do_rpcrequest('DeregisterDelegatedAdministrator', '2020-03-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def deregister_delegated_administrator(self, request):
        runtime = util_models.RuntimeOptions()
        return self.deregister_delegated_administrator_with_options(request, runtime)

    def destroy_resource_directory_with_options(self, runtime):
        req = open_api_models.OpenApiRequest()
        return TeaCore.from_map(
            resource_manager_20200331_models.DestroyResourceDirectoryResponse(),
            self.do_rpcrequest('DestroyResourceDirectory', '2020-03-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def destroy_resource_directory(self):
        runtime = util_models.RuntimeOptions()
        return self.destroy_resource_directory_with_options(runtime)

    def detach_control_policy_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.DetachControlPolicyResponse(),
            self.do_rpcrequest('DetachControlPolicy', '2020-03-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def detach_control_policy(self, request):
        runtime = util_models.RuntimeOptions()
        return self.detach_control_policy_with_options(request, runtime)

    def detach_policy_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.DetachPolicyResponse(),
            self.do_rpcrequest('DetachPolicy', '2020-03-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def detach_policy(self, request):
        runtime = util_models.RuntimeOptions()
        return self.detach_policy_with_options(request, runtime)

    def disable_control_policy_with_options(self, runtime):
        req = open_api_models.OpenApiRequest()
        return TeaCore.from_map(
            resource_manager_20200331_models.DisableControlPolicyResponse(),
            self.do_rpcrequest('DisableControlPolicy', '2020-03-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def disable_control_policy(self):
        runtime = util_models.RuntimeOptions()
        return self.disable_control_policy_with_options(runtime)

    def enable_control_policy_with_options(self, runtime):
        req = open_api_models.OpenApiRequest()
        return TeaCore.from_map(
            resource_manager_20200331_models.EnableControlPolicyResponse(),
            self.do_rpcrequest('EnableControlPolicy', '2020-03-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def enable_control_policy(self):
        runtime = util_models.RuntimeOptions()
        return self.enable_control_policy_with_options(runtime)

    def get_account_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.GetAccountResponse(),
            self.do_rpcrequest('GetAccount', '2020-03-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_account(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_account_with_options(request, runtime)

    def get_control_policy_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.GetControlPolicyResponse(),
            self.do_rpcrequest('GetControlPolicy', '2020-03-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_control_policy(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_control_policy_with_options(request, runtime)

    def get_control_policy_enablement_status_with_options(self, runtime):
        req = open_api_models.OpenApiRequest()
        return TeaCore.from_map(
            resource_manager_20200331_models.GetControlPolicyEnablementStatusResponse(),
            self.do_rpcrequest('GetControlPolicyEnablementStatus', '2020-03-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_control_policy_enablement_status(self):
        runtime = util_models.RuntimeOptions()
        return self.get_control_policy_enablement_status_with_options(runtime)

    def get_folder_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.GetFolderResponse(),
            self.do_rpcrequest('GetFolder', '2020-03-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_folder(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_folder_with_options(request, runtime)

    def get_handshake_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.GetHandshakeResponse(),
            self.do_rpcrequest('GetHandshake', '2020-03-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_handshake(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_handshake_with_options(request, runtime)

    def get_payer_for_account_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.GetPayerForAccountResponse(),
            self.do_rpcrequest('GetPayerForAccount', '2020-03-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_payer_for_account(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_payer_for_account_with_options(request, runtime)

    def get_policy_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.GetPolicyResponse(),
            self.do_rpcrequest('GetPolicy', '2020-03-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_policy(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_policy_with_options(request, runtime)

    def get_policy_version_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.GetPolicyVersionResponse(),
            self.do_rpcrequest('GetPolicyVersion', '2020-03-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_policy_version(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_policy_version_with_options(request, runtime)

    def get_resource_directory_with_options(self, runtime):
        req = open_api_models.OpenApiRequest()
        return TeaCore.from_map(
            resource_manager_20200331_models.GetResourceDirectoryResponse(),
            self.do_rpcrequest('GetResourceDirectory', '2020-03-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_resource_directory(self):
        runtime = util_models.RuntimeOptions()
        return self.get_resource_directory_with_options(runtime)

    def get_resource_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.GetResourceGroupResponse(),
            self.do_rpcrequest('GetResourceGroup', '2020-03-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_resource_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_resource_group_with_options(request, runtime)

    def get_role_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.GetRoleResponse(),
            self.do_rpcrequest('GetRole', '2020-03-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_role(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_role_with_options(request, runtime)

    def get_service_linked_role_deletion_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.GetServiceLinkedRoleDeletionStatusResponse(),
            self.do_rpcrequest('GetServiceLinkedRoleDeletionStatus', '2020-03-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def get_service_linked_role_deletion_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_service_linked_role_deletion_status_with_options(request, runtime)

    def init_resource_directory_with_options(self, runtime):
        req = open_api_models.OpenApiRequest()
        return TeaCore.from_map(
            resource_manager_20200331_models.InitResourceDirectoryResponse(),
            self.do_rpcrequest('InitResourceDirectory', '2020-03-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def init_resource_directory(self):
        runtime = util_models.RuntimeOptions()
        return self.init_resource_directory_with_options(runtime)

    def invite_account_to_resource_directory_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.InviteAccountToResourceDirectoryResponse(),
            self.do_rpcrequest('InviteAccountToResourceDirectory', '2020-03-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def invite_account_to_resource_directory(self, request):
        runtime = util_models.RuntimeOptions()
        return self.invite_account_to_resource_directory_with_options(request, runtime)

    def list_accounts_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.ListAccountsResponse(),
            self.do_rpcrequest('ListAccounts', '2020-03-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_accounts(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_accounts_with_options(request, runtime)

    def list_accounts_for_parent_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.ListAccountsForParentResponse(),
            self.do_rpcrequest('ListAccountsForParent', '2020-03-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_accounts_for_parent(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_accounts_for_parent_with_options(request, runtime)

    def list_ancestors_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.ListAncestorsResponse(),
            self.do_rpcrequest('ListAncestors', '2020-03-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_ancestors(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_ancestors_with_options(request, runtime)

    def list_control_policies_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.ListControlPoliciesResponse(),
            self.do_rpcrequest('ListControlPolicies', '2020-03-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_control_policies(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_control_policies_with_options(request, runtime)

    def list_control_policy_attachments_for_target_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.ListControlPolicyAttachmentsForTargetResponse(),
            self.do_rpcrequest('ListControlPolicyAttachmentsForTarget', '2020-03-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_control_policy_attachments_for_target(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_control_policy_attachments_for_target_with_options(request, runtime)

    def list_delegated_administrators_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.ListDelegatedAdministratorsResponse(),
            self.do_rpcrequest('ListDelegatedAdministrators', '2020-03-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_delegated_administrators(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_delegated_administrators_with_options(request, runtime)

    def list_delegated_services_for_account_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.ListDelegatedServicesForAccountResponse(),
            self.do_rpcrequest('ListDelegatedServicesForAccount', '2020-03-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_delegated_services_for_account(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_delegated_services_for_account_with_options(request, runtime)

    def list_folders_for_parent_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.ListFoldersForParentResponse(),
            self.do_rpcrequest('ListFoldersForParent', '2020-03-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_folders_for_parent(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_folders_for_parent_with_options(request, runtime)

    def list_handshakes_for_account_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.ListHandshakesForAccountResponse(),
            self.do_rpcrequest('ListHandshakesForAccount', '2020-03-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_handshakes_for_account(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_handshakes_for_account_with_options(request, runtime)

    def list_handshakes_for_resource_directory_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.ListHandshakesForResourceDirectoryResponse(),
            self.do_rpcrequest('ListHandshakesForResourceDirectory', '2020-03-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_handshakes_for_resource_directory(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_handshakes_for_resource_directory_with_options(request, runtime)

    def list_policies_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.ListPoliciesResponse(),
            self.do_rpcrequest('ListPolicies', '2020-03-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_policies(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_policies_with_options(request, runtime)

    def list_policy_attachments_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.ListPolicyAttachmentsResponse(),
            self.do_rpcrequest('ListPolicyAttachments', '2020-03-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_policy_attachments(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_policy_attachments_with_options(request, runtime)

    def list_policy_versions_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.ListPolicyVersionsResponse(),
            self.do_rpcrequest('ListPolicyVersions', '2020-03-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_policy_versions(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_policy_versions_with_options(request, runtime)

    def list_resource_groups_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.ListResourceGroupsResponse(),
            self.do_rpcrequest('ListResourceGroups', '2020-03-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_resource_groups(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_resource_groups_with_options(request, runtime)

    def list_resources_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.ListResourcesResponse(),
            self.do_rpcrequest('ListResources', '2020-03-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_resources(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_resources_with_options(request, runtime)

    def list_roles_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.ListRolesResponse(),
            self.do_rpcrequest('ListRoles', '2020-03-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_roles(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_roles_with_options(request, runtime)

    def list_target_attachments_for_control_policy_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.ListTargetAttachmentsForControlPolicyResponse(),
            self.do_rpcrequest('ListTargetAttachmentsForControlPolicy', '2020-03-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_target_attachments_for_control_policy(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_target_attachments_for_control_policy_with_options(request, runtime)

    def list_trusted_service_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.ListTrustedServiceStatusResponse(),
            self.do_rpcrequest('ListTrustedServiceStatus', '2020-03-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def list_trusted_service_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_trusted_service_status_with_options(request, runtime)

    def move_account_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.MoveAccountResponse(),
            self.do_rpcrequest('MoveAccount', '2020-03-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def move_account(self, request):
        runtime = util_models.RuntimeOptions()
        return self.move_account_with_options(request, runtime)

    def promote_resource_account_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.PromoteResourceAccountResponse(),
            self.do_rpcrequest('PromoteResourceAccount', '2020-03-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def promote_resource_account(self, request):
        runtime = util_models.RuntimeOptions()
        return self.promote_resource_account_with_options(request, runtime)

    def register_delegated_administrator_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.RegisterDelegatedAdministratorResponse(),
            self.do_rpcrequest('RegisterDelegatedAdministrator', '2020-03-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def register_delegated_administrator(self, request):
        runtime = util_models.RuntimeOptions()
        return self.register_delegated_administrator_with_options(request, runtime)

    def remove_cloud_account_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.RemoveCloudAccountResponse(),
            self.do_rpcrequest('RemoveCloudAccount', '2020-03-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def remove_cloud_account(self, request):
        runtime = util_models.RuntimeOptions()
        return self.remove_cloud_account_with_options(request, runtime)

    def resend_create_cloud_account_email_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.ResendCreateCloudAccountEmailResponse(),
            self.do_rpcrequest('ResendCreateCloudAccountEmail', '2020-03-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def resend_create_cloud_account_email(self, request):
        runtime = util_models.RuntimeOptions()
        return self.resend_create_cloud_account_email_with_options(request, runtime)

    def resend_promote_resource_account_email_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.ResendPromoteResourceAccountEmailResponse(),
            self.do_rpcrequest('ResendPromoteResourceAccountEmail', '2020-03-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def resend_promote_resource_account_email(self, request):
        runtime = util_models.RuntimeOptions()
        return self.resend_promote_resource_account_email_with_options(request, runtime)

    def set_default_policy_version_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.SetDefaultPolicyVersionResponse(),
            self.do_rpcrequest('SetDefaultPolicyVersion', '2020-03-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def set_default_policy_version(self, request):
        runtime = util_models.RuntimeOptions()
        return self.set_default_policy_version_with_options(request, runtime)

    def update_account_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.UpdateAccountResponse(),
            self.do_rpcrequest('UpdateAccount', '2020-03-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_account(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_account_with_options(request, runtime)

    def update_control_policy_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.UpdateControlPolicyResponse(),
            self.do_rpcrequest('UpdateControlPolicy', '2020-03-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_control_policy(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_control_policy_with_options(request, runtime)

    def update_folder_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.UpdateFolderResponse(),
            self.do_rpcrequest('UpdateFolder', '2020-03-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_folder(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_folder_with_options(request, runtime)

    def update_resource_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.UpdateResourceGroupResponse(),
            self.do_rpcrequest('UpdateResourceGroup', '2020-03-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_resource_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_resource_group_with_options(request, runtime)

    def update_role_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        req = open_api_models.OpenApiRequest(
            body=UtilClient.to_map(request)
        )
        return TeaCore.from_map(
            resource_manager_20200331_models.UpdateRoleResponse(),
            self.do_rpcrequest('UpdateRole', '2020-03-31', 'HTTPS', 'POST', 'AK', 'json', req, runtime)
        )

    def update_role(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_role_with_options(request, runtime)
