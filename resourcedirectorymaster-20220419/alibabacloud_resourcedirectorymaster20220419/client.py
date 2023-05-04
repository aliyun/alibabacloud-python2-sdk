# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_resourcedirectorymaster20220419 import models as resource_directory_master_20220419_models
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
        self._endpoint = self.get_endpoint('resourcedirectorymaster', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

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
            version='2022-04-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_directory_master_20220419_models.AcceptHandshakeResponse(),
            self.call_api(params, req, runtime)
        )

    def accept_handshake(self, request):
        runtime = util_models.RuntimeOptions()
        return self.accept_handshake_with_options(request, runtime)

    def add_message_contact_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.email_address):
            query['EmailAddress'] = request.email_address
        if not UtilClient.is_unset(request.message_types):
            query['MessageTypes'] = request.message_types
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.phone_number):
            query['PhoneNumber'] = request.phone_number
        if not UtilClient.is_unset(request.title):
            query['Title'] = request.title
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AddMessageContact',
            version='2022-04-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_directory_master_20220419_models.AddMessageContactResponse(),
            self.call_api(params, req, runtime)
        )

    def add_message_contact(self, request):
        runtime = util_models.RuntimeOptions()
        return self.add_message_contact_with_options(request, runtime)

    def associate_members_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.contact_id):
            query['ContactId'] = request.contact_id
        if not UtilClient.is_unset(request.members):
            query['Members'] = request.members
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AssociateMembers',
            version='2022-04-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_directory_master_20220419_models.AssociateMembersResponse(),
            self.call_api(params, req, runtime)
        )

    def associate_members(self, request):
        runtime = util_models.RuntimeOptions()
        return self.associate_members_with_options(request, runtime)

    def attach_control_policy_with_options(self, request, runtime):
        """
        The ID of the request.
        

        @param request: AttachControlPolicyRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: AttachControlPolicyResponse
        """
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
            version='2022-04-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_directory_master_20220419_models.AttachControlPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    def attach_control_policy(self, request):
        """
        The ID of the request.
        

        @param request: AttachControlPolicyRequest

        @return: AttachControlPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.attach_control_policy_with_options(request, runtime)

    def bind_secure_mobile_phone_with_options(self, request, runtime):
        """
        The ID of the request.
        

        @param request: BindSecureMobilePhoneRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: BindSecureMobilePhoneResponse
        """
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
            version='2022-04-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_directory_master_20220419_models.BindSecureMobilePhoneResponse(),
            self.call_api(params, req, runtime)
        )

    def bind_secure_mobile_phone(self, request):
        """
        The ID of the request.
        

        @param request: BindSecureMobilePhoneRequest

        @return: BindSecureMobilePhoneResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.bind_secure_mobile_phone_with_options(request, runtime)

    def cancel_change_account_email_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CancelChangeAccountEmail',
            version='2022-04-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_directory_master_20220419_models.CancelChangeAccountEmailResponse(),
            self.call_api(params, req, runtime)
        )

    def cancel_change_account_email(self, request):
        runtime = util_models.RuntimeOptions()
        return self.cancel_change_account_email_with_options(request, runtime)

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
            version='2022-04-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_directory_master_20220419_models.CancelHandshakeResponse(),
            self.call_api(params, req, runtime)
        )

    def cancel_handshake(self, request):
        runtime = util_models.RuntimeOptions()
        return self.cancel_handshake_with_options(request, runtime)

    def cancel_message_contact_update_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.contact_id):
            query['ContactId'] = request.contact_id
        if not UtilClient.is_unset(request.email_address):
            query['EmailAddress'] = request.email_address
        if not UtilClient.is_unset(request.phone_number):
            query['PhoneNumber'] = request.phone_number
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CancelMessageContactUpdate',
            version='2022-04-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_directory_master_20220419_models.CancelMessageContactUpdateResponse(),
            self.call_api(params, req, runtime)
        )

    def cancel_message_contact_update(self, request):
        runtime = util_models.RuntimeOptions()
        return self.cancel_message_contact_update_with_options(request, runtime)

    def change_account_email_with_options(self, request, runtime):
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
            action='ChangeAccountEmail',
            version='2022-04-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_directory_master_20220419_models.ChangeAccountEmailResponse(),
            self.call_api(params, req, runtime)
        )

    def change_account_email(self, request):
        runtime = util_models.RuntimeOptions()
        return self.change_account_email_with_options(request, runtime)

    def check_account_delete_with_options(self, request, runtime):
        """
        The returned result.
        

        @param request: CheckAccountDeleteRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CheckAccountDeleteResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CheckAccountDelete',
            version='2022-04-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_directory_master_20220419_models.CheckAccountDeleteResponse(),
            self.call_api(params, req, runtime)
        )

    def check_account_delete(self, request):
        """
        The returned result.
        

        @param request: CheckAccountDeleteRequest

        @return: CheckAccountDeleteResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.check_account_delete_with_options(request, runtime)

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
            version='2022-04-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_directory_master_20220419_models.CreateControlPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    def create_control_policy(self, request):
        runtime = util_models.RuntimeOptions()
        return self.create_control_policy_with_options(request, runtime)

    def create_folder_with_options(self, request, runtime):
        """
        The name of the folder.
        

        @param request: CreateFolderRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateFolderResponse
        """
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
            version='2022-04-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_directory_master_20220419_models.CreateFolderResponse(),
            self.call_api(params, req, runtime)
        )

    def create_folder(self, request):
        """
        The name of the folder.
        

        @param request: CreateFolderRequest

        @return: CreateFolderResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_folder_with_options(request, runtime)

    def create_resource_account_with_options(self, request, runtime):
        """
        The Alibaba Cloud account name of the member.
        

        @param request: CreateResourceAccountRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateResourceAccountResponse
        """
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
        if not UtilClient.is_unset(request.resell_account_type):
            query['ResellAccountType'] = request.resell_account_type
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateResourceAccount',
            version='2022-04-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_directory_master_20220419_models.CreateResourceAccountResponse(),
            self.call_api(params, req, runtime)
        )

    def create_resource_account(self, request):
        """
        The Alibaba Cloud account name of the member.
        

        @param request: CreateResourceAccountRequest

        @return: CreateResourceAccountResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_resource_account_with_options(request, runtime)

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
            version='2022-04-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_directory_master_20220419_models.DeclineHandshakeResponse(),
            self.call_api(params, req, runtime)
        )

    def decline_handshake(self, request):
        runtime = util_models.RuntimeOptions()
        return self.decline_handshake_with_options(request, runtime)

    def delete_account_with_options(self, tmp_req, runtime):
        UtilClient.validate_model(tmp_req)
        request = resource_directory_master_20220419_models.DeleteAccountShrinkRequest()
        OpenApiUtilClient.convert(tmp_req, request)
        if not UtilClient.is_unset(tmp_req.abandonable_check_id):
            request.abandonable_check_id_shrink = OpenApiUtilClient.array_to_string_with_specified_style(tmp_req.abandonable_check_id, 'AbandonableCheckId', 'json')
        query = {}
        if not UtilClient.is_unset(request.abandonable_check_id_shrink):
            query['AbandonableCheckId'] = request.abandonable_check_id_shrink
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteAccount',
            version='2022-04-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_directory_master_20220419_models.DeleteAccountResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_account(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_account_with_options(request, runtime)

    def delete_control_policy_with_options(self, request, runtime):
        """
        The ID of the request.
        

        @param request: DeleteControlPolicyRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteControlPolicyResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.policy_id):
            query['PolicyId'] = request.policy_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteControlPolicy',
            version='2022-04-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_directory_master_20220419_models.DeleteControlPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_control_policy(self, request):
        """
        The ID of the request.
        

        @param request: DeleteControlPolicyRequest

        @return: DeleteControlPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_control_policy_with_options(request, runtime)

    def delete_folder_with_options(self, request, runtime):
        """
        The ID of the request.
        

        @param request: DeleteFolderRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteFolderResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.folder_id):
            query['FolderId'] = request.folder_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteFolder',
            version='2022-04-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_directory_master_20220419_models.DeleteFolderResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_folder(self, request):
        """
        The ID of the request.
        

        @param request: DeleteFolderRequest

        @return: DeleteFolderResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_folder_with_options(request, runtime)

    def delete_message_contact_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.contact_id):
            query['ContactId'] = request.contact_id
        if not UtilClient.is_unset(request.retain_contact_in_members):
            query['RetainContactInMembers'] = request.retain_contact_in_members
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteMessageContact',
            version='2022-04-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_directory_master_20220419_models.DeleteMessageContactResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_message_contact(self, request):
        runtime = util_models.RuntimeOptions()
        return self.delete_message_contact_with_options(request, runtime)

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
            version='2022-04-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_directory_master_20220419_models.DeregisterDelegatedAdministratorResponse(),
            self.call_api(params, req, runtime)
        )

    def deregister_delegated_administrator(self, request):
        runtime = util_models.RuntimeOptions()
        return self.deregister_delegated_administrator_with_options(request, runtime)

    def destroy_resource_directory_with_options(self, runtime):
        """
        The ID of the request.
        

        @param request: DestroyResourceDirectoryRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DestroyResourceDirectoryResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DestroyResourceDirectory',
            version='2022-04-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_directory_master_20220419_models.DestroyResourceDirectoryResponse(),
            self.call_api(params, req, runtime)
        )

    def destroy_resource_directory(self):
        """
        The ID of the request.
        

        @return: DestroyResourceDirectoryResponse
        """
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
            version='2022-04-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_directory_master_20220419_models.DetachControlPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    def detach_control_policy(self, request):
        runtime = util_models.RuntimeOptions()
        return self.detach_control_policy_with_options(request, runtime)

    def disable_control_policy_with_options(self, runtime):
        """
        The ID of the request.
        

        @param request: DisableControlPolicyRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DisableControlPolicyResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='DisableControlPolicy',
            version='2022-04-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_directory_master_20220419_models.DisableControlPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    def disable_control_policy(self):
        """
        The ID of the request.
        

        @return: DisableControlPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.disable_control_policy_with_options(runtime)

    def disassociate_members_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.contact_id):
            query['ContactId'] = request.contact_id
        if not UtilClient.is_unset(request.members):
            query['Members'] = request.members
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DisassociateMembers',
            version='2022-04-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_directory_master_20220419_models.DisassociateMembersResponse(),
            self.call_api(params, req, runtime)
        )

    def disassociate_members(self, request):
        runtime = util_models.RuntimeOptions()
        return self.disassociate_members_with_options(request, runtime)

    def enable_control_policy_with_options(self, runtime):
        """
        The ID of the request.
        

        @param request: EnableControlPolicyRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: EnableControlPolicyResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='EnableControlPolicy',
            version='2022-04-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_directory_master_20220419_models.EnableControlPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    def enable_control_policy(self):
        """
        The ID of the request.
        

        @return: EnableControlPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.enable_control_policy_with_options(runtime)

    def enable_resource_directory_with_options(self, request, runtime):
        """
        The ID of the request.
        

        @param request: EnableResourceDirectoryRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: EnableResourceDirectoryResponse
        """
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
            version='2022-04-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_directory_master_20220419_models.EnableResourceDirectoryResponse(),
            self.call_api(params, req, runtime)
        )

    def enable_resource_directory(self, request):
        """
        The ID of the request.
        

        @param request: EnableResourceDirectoryRequest

        @return: EnableResourceDirectoryResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.enable_resource_directory_with_options(request, runtime)

    def get_account_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        if not UtilClient.is_unset(request.include_tags):
            query['IncludeTags'] = request.include_tags
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAccount',
            version='2022-04-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_directory_master_20220419_models.GetAccountResponse(),
            self.call_api(params, req, runtime)
        )

    def get_account(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_account_with_options(request, runtime)

    def get_account_deletion_check_result_with_options(self, request, runtime):
        """
        Container Service for Kubernetes
        

        @param request: GetAccountDeletionCheckResultRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: GetAccountDeletionCheckResultResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAccountDeletionCheckResult',
            version='2022-04-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_directory_master_20220419_models.GetAccountDeletionCheckResultResponse(),
            self.call_api(params, req, runtime)
        )

    def get_account_deletion_check_result(self, request):
        """
        Container Service for Kubernetes
        

        @param request: GetAccountDeletionCheckResultRequest

        @return: GetAccountDeletionCheckResultResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_account_deletion_check_result_with_options(request, runtime)

    def get_account_deletion_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetAccountDeletionStatus',
            version='2022-04-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_directory_master_20220419_models.GetAccountDeletionStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def get_account_deletion_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_account_deletion_status_with_options(request, runtime)

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
            version='2022-04-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_directory_master_20220419_models.GetControlPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    def get_control_policy(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_control_policy_with_options(request, runtime)

    def get_control_policy_enablement_status_with_options(self, runtime):
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='GetControlPolicyEnablementStatus',
            version='2022-04-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_directory_master_20220419_models.GetControlPolicyEnablementStatusResponse(),
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
            version='2022-04-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_directory_master_20220419_models.GetFolderResponse(),
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
            version='2022-04-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_directory_master_20220419_models.GetHandshakeResponse(),
            self.call_api(params, req, runtime)
        )

    def get_handshake(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_handshake_with_options(request, runtime)

    def get_message_contact_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.contact_id):
            query['ContactId'] = request.contact_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetMessageContact',
            version='2022-04-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_directory_master_20220419_models.GetMessageContactResponse(),
            self.call_api(params, req, runtime)
        )

    def get_message_contact(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_message_contact_with_options(request, runtime)

    def get_message_contact_deletion_status_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.contact_id):
            query['ContactId'] = request.contact_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetMessageContactDeletionStatus',
            version='2022-04-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_directory_master_20220419_models.GetMessageContactDeletionStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def get_message_contact_deletion_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_message_contact_deletion_status_with_options(request, runtime)

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
            version='2022-04-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_directory_master_20220419_models.GetPayerForAccountResponse(),
            self.call_api(params, req, runtime)
        )

    def get_payer_for_account(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_payer_for_account_with_options(request, runtime)

    def get_resource_directory_with_options(self, runtime):
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='GetResourceDirectory',
            version='2022-04-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_directory_master_20220419_models.GetResourceDirectoryResponse(),
            self.call_api(params, req, runtime)
        )

    def get_resource_directory(self):
        runtime = util_models.RuntimeOptions()
        return self.get_resource_directory_with_options(runtime)

    def invite_account_to_resource_directory_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.note):
            query['Note'] = request.note
        if not UtilClient.is_unset(request.parent_folder_id):
            query['ParentFolderId'] = request.parent_folder_id
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        if not UtilClient.is_unset(request.target_entity):
            query['TargetEntity'] = request.target_entity
        if not UtilClient.is_unset(request.target_type):
            query['TargetType'] = request.target_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='InviteAccountToResourceDirectory',
            version='2022-04-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_directory_master_20220419_models.InviteAccountToResourceDirectoryResponse(),
            self.call_api(params, req, runtime)
        )

    def invite_account_to_resource_directory(self, request):
        runtime = util_models.RuntimeOptions()
        return self.invite_account_to_resource_directory_with_options(request, runtime)

    def list_accounts_with_options(self, request, runtime):
        """
        You can use only the management account of a resource directory or a delegated administrator account of a trusted service to call this operation.
        

        @param request: ListAccountsRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListAccountsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.include_tags):
            query['IncludeTags'] = request.include_tags
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.query_keyword):
            query['QueryKeyword'] = request.query_keyword
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAccounts',
            version='2022-04-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_directory_master_20220419_models.ListAccountsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_accounts(self, request):
        """
        You can use only the management account of a resource directory or a delegated administrator account of a trusted service to call this operation.
        

        @param request: ListAccountsRequest

        @return: ListAccountsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_accounts_with_options(request, runtime)

    def list_accounts_for_parent_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.include_tags):
            query['IncludeTags'] = request.include_tags
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.parent_folder_id):
            query['ParentFolderId'] = request.parent_folder_id
        if not UtilClient.is_unset(request.query_keyword):
            query['QueryKeyword'] = request.query_keyword
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListAccountsForParent',
            version='2022-04-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_directory_master_20220419_models.ListAccountsForParentResponse(),
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
            version='2022-04-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_directory_master_20220419_models.ListAncestorsResponse(),
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
            version='2022-04-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_directory_master_20220419_models.ListControlPoliciesResponse(),
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
            version='2022-04-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_directory_master_20220419_models.ListControlPolicyAttachmentsForTargetResponse(),
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
            version='2022-04-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_directory_master_20220419_models.ListDelegatedAdministratorsResponse(),
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
            version='2022-04-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_directory_master_20220419_models.ListDelegatedServicesForAccountResponse(),
            self.call_api(params, req, runtime)
        )

    def list_delegated_services_for_account(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_delegated_services_for_account_with_options(request, runtime)

    def list_folders_for_parent_with_options(self, request, runtime):
        """
        You can call this API operation to view the information of only the first-level subfolders of a folder.
        

        @param request: ListFoldersForParentRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListFoldersForParentResponse
        """
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
            version='2022-04-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_directory_master_20220419_models.ListFoldersForParentResponse(),
            self.call_api(params, req, runtime)
        )

    def list_folders_for_parent(self, request):
        """
        You can call this API operation to view the information of only the first-level subfolders of a folder.
        

        @param request: ListFoldersForParentRequest

        @return: ListFoldersForParentResponse
        """
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
            version='2022-04-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_directory_master_20220419_models.ListHandshakesForAccountResponse(),
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
            version='2022-04-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_directory_master_20220419_models.ListHandshakesForResourceDirectoryResponse(),
            self.call_api(params, req, runtime)
        )

    def list_handshakes_for_resource_directory(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_handshakes_for_resource_directory_with_options(request, runtime)

    def list_message_contact_verifications_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.contact_id):
            query['ContactId'] = request.contact_id
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListMessageContactVerifications',
            version='2022-04-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_directory_master_20220419_models.ListMessageContactVerificationsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_message_contact_verifications(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_message_contact_verifications_with_options(request, runtime)

    def list_message_contacts_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.contact_id):
            query['ContactId'] = request.contact_id
        if not UtilClient.is_unset(request.member):
            query['Member'] = request.member
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListMessageContacts',
            version='2022-04-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_directory_master_20220419_models.ListMessageContactsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_message_contacts(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_message_contacts_with_options(request, runtime)

    def list_tag_resources_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
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
            version='2022-04-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_directory_master_20220419_models.ListTagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_tag_resources(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_tag_resources_with_options(request, runtime)

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
            version='2022-04-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_directory_master_20220419_models.ListTargetAttachmentsForControlPolicyResponse(),
            self.call_api(params, req, runtime)
        )

    def list_target_attachments_for_control_policy(self, request):
        runtime = util_models.RuntimeOptions()
        return self.list_target_attachments_for_control_policy_with_options(request, runtime)

    def list_trusted_service_status_with_options(self, request, runtime):
        """
        The time when the trusted service was enabled.
        

        @param request: ListTrustedServiceStatusRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListTrustedServiceStatusResponse
        """
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
            version='2022-04-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_directory_master_20220419_models.ListTrustedServiceStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def list_trusted_service_status(self, request):
        """
        The time when the trusted service was enabled.
        

        @param request: ListTrustedServiceStatusRequest

        @return: ListTrustedServiceStatusResponse
        """
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
            version='2022-04-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_directory_master_20220419_models.MoveAccountResponse(),
            self.call_api(params, req, runtime)
        )

    def move_account(self, request):
        runtime = util_models.RuntimeOptions()
        return self.move_account_with_options(request, runtime)

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
            version='2022-04-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_directory_master_20220419_models.RegisterDelegatedAdministratorResponse(),
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
            version='2022-04-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_directory_master_20220419_models.RemoveCloudAccountResponse(),
            self.call_api(params, req, runtime)
        )

    def remove_cloud_account(self, request):
        runtime = util_models.RuntimeOptions()
        return self.remove_cloud_account_with_options(request, runtime)

    def retry_change_account_email_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.account_id):
            query['AccountId'] = request.account_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RetryChangeAccountEmail',
            version='2022-04-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_directory_master_20220419_models.RetryChangeAccountEmailResponse(),
            self.call_api(params, req, runtime)
        )

    def retry_change_account_email(self, request):
        runtime = util_models.RuntimeOptions()
        return self.retry_change_account_email_with_options(request, runtime)

    def send_email_verification_for_message_contact_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.contact_id):
            query['ContactId'] = request.contact_id
        if not UtilClient.is_unset(request.email_address):
            query['EmailAddress'] = request.email_address
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SendEmailVerificationForMessageContact',
            version='2022-04-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_directory_master_20220419_models.SendEmailVerificationForMessageContactResponse(),
            self.call_api(params, req, runtime)
        )

    def send_email_verification_for_message_contact(self, request):
        runtime = util_models.RuntimeOptions()
        return self.send_email_verification_for_message_contact_with_options(request, runtime)

    def send_phone_verification_for_message_contact_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.contact_id):
            query['ContactId'] = request.contact_id
        if not UtilClient.is_unset(request.phone_number):
            query['PhoneNumber'] = request.phone_number
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SendPhoneVerificationForMessageContact',
            version='2022-04-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_directory_master_20220419_models.SendPhoneVerificationForMessageContactResponse(),
            self.call_api(params, req, runtime)
        )

    def send_phone_verification_for_message_contact(self, request):
        runtime = util_models.RuntimeOptions()
        return self.send_phone_verification_for_message_contact_with_options(request, runtime)

    def send_verification_code_for_bind_secure_mobile_phone_with_options(self, request, runtime):
        """
        To ensure that the system can record the operators of management operations, you must use a RAM user or RAM role to which the AliyunResourceDirectoryFullAccess policy is attached within the management account of your resource directory to call this API operation.
        

        @param request: SendVerificationCodeForBindSecureMobilePhoneRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: SendVerificationCodeForBindSecureMobilePhoneResponse
        """
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
            version='2022-04-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_directory_master_20220419_models.SendVerificationCodeForBindSecureMobilePhoneResponse(),
            self.call_api(params, req, runtime)
        )

    def send_verification_code_for_bind_secure_mobile_phone(self, request):
        """
        To ensure that the system can record the operators of management operations, you must use a RAM user or RAM role to which the AliyunResourceDirectoryFullAccess policy is attached within the management account of your resource directory to call this API operation.
        

        @param request: SendVerificationCodeForBindSecureMobilePhoneRequest

        @return: SendVerificationCodeForBindSecureMobilePhoneResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.send_verification_code_for_bind_secure_mobile_phone_with_options(request, runtime)

    def send_verification_code_for_enable_rdwith_options(self, request, runtime):
        """
        Each Alibaba Cloud account can be used to send a maximum of 100 verification codes per day.
        

        @param request: SendVerificationCodeForEnableRDRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: SendVerificationCodeForEnableRDResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.secure_mobile_phone):
            query['SecureMobilePhone'] = request.secure_mobile_phone
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SendVerificationCodeForEnableRD',
            version='2022-04-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_directory_master_20220419_models.SendVerificationCodeForEnableRDResponse(),
            self.call_api(params, req, runtime)
        )

    def send_verification_code_for_enable_rd(self, request):
        """
        Each Alibaba Cloud account can be used to send a maximum of 100 verification codes per day.
        

        @param request: SendVerificationCodeForEnableRDRequest

        @return: SendVerificationCodeForEnableRDResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.send_verification_code_for_enable_rdwith_options(request, runtime)

    def set_member_deletion_permission_with_options(self, request, runtime):
        """
        Members of the resource account type can be deleted only after the member deletion feature is enabled.
        

        @param request: SetMemberDeletionPermissionRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: SetMemberDeletionPermissionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='SetMemberDeletionPermission',
            version='2022-04-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_directory_master_20220419_models.SetMemberDeletionPermissionResponse(),
            self.call_api(params, req, runtime)
        )

    def set_member_deletion_permission(self, request):
        """
        Members of the resource account type can be deleted only after the member deletion feature is enabled.
        

        @param request: SetMemberDeletionPermissionRequest

        @return: SetMemberDeletionPermissionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.set_member_deletion_permission_with_options(request, runtime)

    def tag_resources_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
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
            version='2022-04-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_directory_master_20220419_models.TagResourcesResponse(),
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
            version='2022-04-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_directory_master_20220419_models.UntagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    def untag_resources(self, request):
        runtime = util_models.RuntimeOptions()
        return self.untag_resources_with_options(request, runtime)

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
            version='2022-04-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_directory_master_20220419_models.UpdateAccountResponse(),
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
            version='2022-04-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_directory_master_20220419_models.UpdateControlPolicyResponse(),
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
            version='2022-04-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_directory_master_20220419_models.UpdateFolderResponse(),
            self.call_api(params, req, runtime)
        )

    def update_folder(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_folder_with_options(request, runtime)

    def update_message_contact_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.contact_id):
            query['ContactId'] = request.contact_id
        if not UtilClient.is_unset(request.email_address):
            query['EmailAddress'] = request.email_address
        if not UtilClient.is_unset(request.message_types):
            query['MessageTypes'] = request.message_types
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.phone_number):
            query['PhoneNumber'] = request.phone_number
        if not UtilClient.is_unset(request.title):
            query['Title'] = request.title
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateMessageContact',
            version='2022-04-19',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_directory_master_20220419_models.UpdateMessageContactResponse(),
            self.call_api(params, req, runtime)
        )

    def update_message_contact(self, request):
        runtime = util_models.RuntimeOptions()
        return self.update_message_contact_with_options(request, runtime)
