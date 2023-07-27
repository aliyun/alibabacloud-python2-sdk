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
        """
        After an invited Alibaba Cloud account joins a resource directory, it becomes a member of the resource directory. By default, the name of the invited Alibaba Cloud account is used as the display name of the account in the resource directory.
        This topic provides an example on how to call the API operation to accept the invitation `h-Ih8IuPfvV0t0****` that is initiated to invite the Alibaba Cloud account `177242285274****` to join the resource directory `rd-3G****`.
        

        @param request: AcceptHandshakeRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: AcceptHandshakeResponse
        """
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
        """
        After an invited Alibaba Cloud account joins a resource directory, it becomes a member of the resource directory. By default, the name of the invited Alibaba Cloud account is used as the display name of the account in the resource directory.
        This topic provides an example on how to call the API operation to accept the invitation `h-Ih8IuPfvV0t0****` that is initiated to invite the Alibaba Cloud account `177242285274****` to join the resource directory `rd-3G****`.
        

        @param request: AcceptHandshakeRequest

        @return: AcceptHandshakeResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.accept_handshake_with_options(request, runtime)

    def attach_control_policy_with_options(self, request, runtime):
        """
        After you attach an access control policy, the operations performed on resources by using members are limited by the policy. Make sure that the attached policy meets your expectations. Otherwise, your business may be affected.
        By default, the system access control policy FullAliyunAccess is attached to each folder and member.
        The access control policy that is attached to a folder also applies to all its subfolders and all members in the subfolders.
        A maximum of 10 access control policies can be attached to a folder or member.
        This topic provides an example on how to call the API operation to attach the custom access control policy `cp-jExXAqIYkwHN****` to the folder `fd-ZDNPiT****`.
        

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
        """
        After you attach an access control policy, the operations performed on resources by using members are limited by the policy. Make sure that the attached policy meets your expectations. Otherwise, your business may be affected.
        By default, the system access control policy FullAliyunAccess is attached to each folder and member.
        The access control policy that is attached to a folder also applies to all its subfolders and all members in the subfolders.
        A maximum of 10 access control policies can be attached to a folder or member.
        This topic provides an example on how to call the API operation to attach the custom access control policy `cp-jExXAqIYkwHN****` to the folder `fd-ZDNPiT****`.
        

        @param request: AttachControlPolicyRequest

        @return: AttachControlPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.attach_control_policy_with_options(request, runtime)

    def attach_policy_with_options(self, request, runtime):
        """
        In this example, the policy `AdministratorAccess` is attached to the RAM user `alice@demo.onaliyun.com` and takes effect only for resources in the `rg-9gLOoK***` resource group.
        

        @param request: AttachPolicyRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: AttachPolicyResponse
        """
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
        """
        In this example, the policy `AdministratorAccess` is attached to the RAM user `alice@demo.onaliyun.com` and takes effect only for resources in the `rg-9gLOoK***` resource group.
        

        @param request: AttachPolicyRequest

        @return: AttachPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.attach_policy_with_options(request, runtime)

    def bind_secure_mobile_phone_with_options(self, request, runtime):
        """
        You can call this API operation only to bind a mobile phone number to a member of the resource account type. You cannot call this API operation to change the mobile phone number that is bound to a member of the resource account type.
        To ensure that the system can record the operators of management operations, you must use a RAM user or RAM role to which the AliyunResourceDirectoryFullAccess policy is attached within the management account of your resource directory to call this API operation.
        This topic provides an example on how to call the API operation to bind a mobile phone number to the member `138660628348****` for security purposes.
        

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
        """
        You can call this API operation only to bind a mobile phone number to a member of the resource account type. You cannot call this API operation to change the mobile phone number that is bound to a member of the resource account type.
        To ensure that the system can record the operators of management operations, you must use a RAM user or RAM role to which the AliyunResourceDirectoryFullAccess policy is attached within the management account of your resource directory to call this API operation.
        This topic provides an example on how to call the API operation to bind a mobile phone number to the member `138660628348****` for security purposes.
        

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
            resource_manager_20200331_models.CancelChangeAccountEmailResponse(),
            self.call_api(params, req, runtime)
        )

    def cancel_change_account_email(self, request):
        runtime = util_models.RuntimeOptions()
        return self.cancel_change_account_email_with_options(request, runtime)

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
        """
        This topic provides an example on how to call the API operation to cancel the invitation whose ID is `h-ycm4rp***`.
        

        @param request: CancelHandshakeRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CancelHandshakeResponse
        """
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
        """
        This topic provides an example on how to call the API operation to cancel the invitation whose ID is `h-ycm4rp***`.
        

        @param request: CancelHandshakeRequest

        @return: CancelHandshakeResponse
        """
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
            resource_manager_20200331_models.ChangeAccountEmailResponse(),
            self.call_api(params, req, runtime)
        )

    def change_account_email(self, request):
        runtime = util_models.RuntimeOptions()
        return self.change_account_email_with_options(request, runtime)

    def check_account_delete_with_options(self, request, runtime):
        """
        Before you delete a member, you must call this API operation to check whether the member can be deleted.
        This topic provides an example on how to call the API operation to perform a deletion check on the member whose ID is `179855839641****`.
        

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
            resource_manager_20200331_models.CheckAccountDeleteResponse(),
            self.call_api(params, req, runtime)
        )

    def check_account_delete(self, request):
        """
        Before you delete a member, you must call this API operation to check whether the member can be deleted.
        This topic provides an example on how to call the API operation to perform a deletion check on the member whose ID is `179855839641****`.
        

        @param request: CheckAccountDeleteRequest

        @return: CheckAccountDeleteResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.check_account_delete_with_options(request, runtime)

    def create_cloud_account_with_options(self, request, runtime):
        """
        A resource directory supports two types of member accounts: resource accounts and cloud accounts.
        *   Resource account (recommended): A resource account is only used as a resource container and fully depends on a resource directory. Such member accounts are secure and easy-to-create. For more information about how to create a resource account, see [CreateResourceAccount](~~159392~~).
        >  A resource account can be upgraded to a cloud account. For more information, see [PromoteResourceAccount](~~159395~~) .
        *   Cloud account: A cloud account has all the features of an Alibaba Cloud account, including root permissions.
        

        @param request: CreateCloudAccountRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateCloudAccountResponse
        """
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
        """
        A resource directory supports two types of member accounts: resource accounts and cloud accounts.
        *   Resource account (recommended): A resource account is only used as a resource container and fully depends on a resource directory. Such member accounts are secure and easy-to-create. For more information about how to create a resource account, see [CreateResourceAccount](~~159392~~).
        >  A resource account can be upgraded to a cloud account. For more information, see [PromoteResourceAccount](~~159395~~) .
        *   Cloud account: A cloud account has all the features of an Alibaba Cloud account, including root permissions.
        

        @param request: CreateCloudAccountRequest

        @return: CreateCloudAccountResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_cloud_account_with_options(request, runtime)

    def create_control_policy_with_options(self, request, runtime):
        """
        This topic provides an example on how to call the API operation to create a custom access control policy named `ExampleControlPolicy`. This access control policy is used to prohibit modifications to the ResourceDirectoryAccountAccessRole role and the permissions of the role.
        

        @param request: CreateControlPolicyRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateControlPolicyResponse
        """
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
        """
        This topic provides an example on how to call the API operation to create a custom access control policy named `ExampleControlPolicy`. This access control policy is used to prohibit modifications to the ResourceDirectoryAccountAccessRole role and the permissions of the role.
        

        @param request: CreateControlPolicyRequest

        @return: CreateControlPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_control_policy_with_options(request, runtime)

    def create_folder_with_options(self, request, runtime):
        """
        >  A maximum of five levels of folders can be created under the root folder.
        In this example, a folder named `rdFolder` is created under the root folder.
        

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
        """
        >  A maximum of five levels of folders can be created under the root folder.
        In this example, a folder named `rdFolder` is created under the root folder.
        

        @param request: CreateFolderRequest

        @return: CreateFolderResponse
        """
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
        """
        A member serves as a container for resources and is also an organizational unit in a resource directory. A member indicates a project or application. The resources of different members are isolated.
        This topic provides an example on how to call the API operation to create a member in the `fd-r23M55****` folder. The display name of the member is `Dev`, and the prefix for the Alibaba Cloud account name of the member is `alice`.
        

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
        """
        A member serves as a container for resources and is also an organizational unit in a resource directory. A member indicates a project or application. The resources of different members are isolated.
        This topic provides an example on how to call the API operation to create a member in the `fd-r23M55****` folder. The display name of the member is `Dev`, and the prefix for the Alibaba Cloud account name of the member is `alice`.
        

        @param request: CreateResourceAccountRequest

        @return: CreateResourceAccountResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_resource_account_with_options(request, runtime)

    def create_resource_group_with_options(self, request, runtime):
        """
        For more information about common request parameters, see [Common parameters](~~159973~~).
        

        @param request: CreateResourceGroupRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateResourceGroupResponse
        """
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
        """
        For more information about common request parameters, see [Common parameters](~~159973~~).
        

        @param request: CreateResourceGroupRequest

        @return: CreateResourceGroupResponse
        """
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

    def delete_account_with_options(self, tmp_req, runtime):
        """
        The ID of the member that you want to delete.
        

        @param tmp_req: DeleteAccountRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteAccountResponse
        """
        UtilClient.validate_model(tmp_req)
        request = resource_manager_20200331_models.DeleteAccountShrinkRequest()
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
            resource_manager_20200331_models.DeleteAccountResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_account(self, request):
        """
        The ID of the member that you want to delete.
        

        @param request: DeleteAccountRequest

        @return: DeleteAccountResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_account_with_options(request, runtime)

    def delete_control_policy_with_options(self, request, runtime):
        """
        If you want to delete a custom control policy that is attached to folders or member accounts, you must call the [DetachControlPolicy](~~208331~~) operation to detach the policy before you delete it.
        In this example, the custom control policy `cp-SImPt8GCEwiq****` is deleted.
        

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
        """
        If you want to delete a custom control policy that is attached to folders or member accounts, you must call the [DetachControlPolicy](~~208331~~) operation to detach the policy before you delete it.
        In this example, the custom control policy `cp-SImPt8GCEwiq****` is deleted.
        

        @param request: DeleteControlPolicyRequest

        @return: DeleteControlPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_control_policy_with_options(request, runtime)

    def delete_folder_with_options(self, request, runtime):
        """
        >  Before you delete a folder, make sure that the folder does not contain any member accounts or child folders.
        

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
        """
        >  Before you delete a folder, make sure that the folder does not contain any member accounts or child folders.
        

        @param request: DeleteFolderRequest

        @return: DeleteFolderResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_folder_with_options(request, runtime)

    def delete_policy_with_options(self, request, runtime):
        """
        >
        *   Before you delete a policy, you must delete all non-default versions of the policy. For more information about how to delete a policy version, see [DeletePolicyVersion](~~159041~~).
        *   Before you delete a policy, make sure that the policy is not referenced. This means that the policy is not attached to RAM users, RAM user groups, or RAM roles. For more information about how to detach a policy, see [DetachPolicy](~~159168~~).
        

        @param request: DeletePolicyRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeletePolicyResponse
        """
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
        """
        >
        *   Before you delete a policy, you must delete all non-default versions of the policy. For more information about how to delete a policy version, see [DeletePolicyVersion](~~159041~~).
        *   Before you delete a policy, make sure that the policy is not referenced. This means that the policy is not attached to RAM users, RAM user groups, or RAM roles. For more information about how to detach a policy, see [DetachPolicy](~~159168~~).
        

        @param request: DeletePolicyRequest

        @return: DeletePolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_policy_with_options(request, runtime)

    def delete_policy_version_with_options(self, request, runtime):
        """
        >  The default version of a permission policy cannot be deleted.
        

        @param request: DeletePolicyVersionRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeletePolicyVersionResponse
        """
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
        """
        >  The default version of a permission policy cannot be deleted.
        

        @param request: DeletePolicyVersionRequest

        @return: DeletePolicyVersionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_policy_version_with_options(request, runtime)

    def delete_resource_group_with_options(self, request, runtime):
        """
        >  Before you delete a resource group, you must delete all the resources in it.
        In this example, the resource group whose ID is `rg-9gLOoK****` is deleted.
        

        @param request: DeleteResourceGroupRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteResourceGroupResponse
        """
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
        """
        >  Before you delete a resource group, you must delete all the resources in it.
        In this example, the resource group whose ID is `rg-9gLOoK****` is deleted.
        

        @param request: DeleteResourceGroupRequest

        @return: DeleteResourceGroupResponse
        """
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
        """
        >  If the delegated administrator account that you want to remove has historical management tasks in the related trusted service, the trusted service may be affected after the delegated administrator account is removed. Therefore, proceed with caution.
        This topic provides an example on how to call the API operation to remove the delegated administrator account `181761095690****` for Cloud Firewall.
        

        @param request: DeregisterDelegatedAdministratorRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeregisterDelegatedAdministratorResponse
        """
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
        """
        >  If the delegated administrator account that you want to remove has historical management tasks in the related trusted service, the trusted service may be affected after the delegated administrator account is removed. Therefore, proceed with caution.
        This topic provides an example on how to call the API operation to remove the delegated administrator account `181761095690****` for Cloud Firewall.
        

        @param request: DeregisterDelegatedAdministratorRequest

        @return: DeregisterDelegatedAdministratorResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.deregister_delegated_administrator_with_options(request, runtime)

    def destroy_resource_directory_with_options(self, runtime):
        """
        Before you disable a resource directory, make sure that the following requirements are met:
        *   All member accounts must be removed from the resource directory. For more information about how to remove a member account, see [RemoveCloudAccount](~~159431~~).
        *   All folders except the root folder must be deleted from the resource directory. For more information about how to delete a folder, see [DeleteFolder](~~159432~~).
        

        @param request: DestroyResourceDirectoryRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DestroyResourceDirectoryResponse
        """
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
        """
        Before you disable a resource directory, make sure that the following requirements are met:
        *   All member accounts must be removed from the resource directory. For more information about how to remove a member account, see [RemoveCloudAccount](~~159431~~).
        *   All folders except the root folder must be deleted from the resource directory. For more information about how to delete a folder, see [DeleteFolder](~~159432~~).
        

        @return: DestroyResourceDirectoryResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.destroy_resource_directory_with_options(runtime)

    def detach_control_policy_with_options(self, request, runtime):
        """
        After you detach an access control policy, the operations performed on resources by using members are not limited by the policy. Make sure that the detached policy meets your expectations. Otherwise, your business may be affected.
        Both the system and custom access control policies can be detached. If an object has only one access control policy attached, the policy cannot be detached.
        This topic provides an example on how to call the API operation to detach the custom control policy `cp-jExXAqIYkwHN****` from the folder `fd-ZDNPiT****`.
        

        @param request: DetachControlPolicyRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DetachControlPolicyResponse
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
        """
        After you detach an access control policy, the operations performed on resources by using members are not limited by the policy. Make sure that the detached policy meets your expectations. Otherwise, your business may be affected.
        Both the system and custom access control policies can be detached. If an object has only one access control policy attached, the policy cannot be detached.
        This topic provides an example on how to call the API operation to detach the custom control policy `cp-jExXAqIYkwHN****` from the folder `fd-ZDNPiT****`.
        

        @param request: DetachControlPolicyRequest

        @return: DetachControlPolicyResponse
        """
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
        """
        After you disable the Control Policy feature, the system automatically detaches all control policies that are attached to folders and member accounts. The system does not delete these control policies, but you cannot attach them to folders or member accounts again.
        >  If you disable the Control Policy feature, the permissions of all folders and member accounts in a resource directory are affected. You must proceed with caution.
        

        @param request: DisableControlPolicyRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DisableControlPolicyResponse
        """
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
        """
        After you disable the Control Policy feature, the system automatically detaches all control policies that are attached to folders and member accounts. The system does not delete these control policies, but you cannot attach them to folders or member accounts again.
        >  If you disable the Control Policy feature, the permissions of all folders and member accounts in a resource directory are affected. You must proceed with caution.
        

        @return: DisableControlPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.disable_control_policy_with_options(runtime)

    def enable_control_policy_with_options(self, runtime):
        """
        The Control Policy feature allows you to manage the permission boundaries of the folders or member accounts in a resource directory in a centralized manner. This feature is implemented based on the resource directory. You can use this feature to develop common or dedicated rules for access control. The Control Policy feature does not grant permissions but only defines permission boundaries. A member account in a resource directory can be used to access resources only after it is granted the required permissions by using the Resource Access Management (RAM) service. For more information, see [Overview of the Control Policy feature](~~178671~~).
        

        @param request: EnableControlPolicyRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: EnableControlPolicyResponse
        """
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
        """
        The Control Policy feature allows you to manage the permission boundaries of the folders or member accounts in a resource directory in a centralized manner. This feature is implemented based on the resource directory. You can use this feature to develop common or dedicated rules for access control. The Control Policy feature does not grant permissions but only defines permission boundaries. A member account in a resource directory can be used to access resources only after it is granted the required permissions by using the Resource Access Management (RAM) service. For more information, see [Overview of the Control Policy feature](~~178671~~).
        

        @return: EnableControlPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.enable_control_policy_with_options(runtime)

    def enable_resource_directory_with_options(self, request, runtime):
        """
        You can use the current account or a newly created account to enable a resource directory. For more information, see [Enable a resource directory](~~111215~~).
        In this example, the current account is used to enable a resource directory.
        

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
        """
        You can use the current account or a newly created account to enable a resource directory. For more information, see [Enable a resource directory](~~111215~~).
        In this example, the current account is used to enable a resource directory.
        

        @param request: EnableResourceDirectoryRequest

        @return: EnableResourceDirectoryResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.enable_resource_directory_with_options(request, runtime)

    def get_account_with_options(self, request, runtime):
        """
        This topic provides an example on how to call the API operation to query the information of the member whose Alibaba Cloud account ID is `181761095690***`.
        

        @param request: GetAccountRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: GetAccountResponse
        """
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
        """
        This topic provides an example on how to call the API operation to query the information of the member whose Alibaba Cloud account ID is `181761095690***`.
        

        @param request: GetAccountRequest

        @return: GetAccountResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_account_with_options(request, runtime)

    def get_account_deletion_check_result_with_options(self, request, runtime):
        """
        After you call the [CheckAccountDelete](~~448542~~) operation to perform a member deletion check, you can call the GetAccountDeletionCheckResult operation to query the check result. If the check result shows that the member meets deletion requirements, you can delete the member. Otherwise, you need to first modify the items that do not meet requirements.
        This topic provides an example on how to call the API operation to query the result of the deletion check for the member whose ID is `179855839641****`. The response shows that the member does not meet deletion requirements.
        

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
            resource_manager_20200331_models.GetAccountDeletionCheckResultResponse(),
            self.call_api(params, req, runtime)
        )

    def get_account_deletion_check_result(self, request):
        """
        After you call the [CheckAccountDelete](~~448542~~) operation to perform a member deletion check, you can call the GetAccountDeletionCheckResult operation to query the check result. If the check result shows that the member meets deletion requirements, you can delete the member. Otherwise, you need to first modify the items that do not meet requirements.
        This topic provides an example on how to call the API operation to query the result of the deletion check for the member whose ID is `179855839641****`. The response shows that the member does not meet deletion requirements.
        

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
            resource_manager_20200331_models.GetAccountDeletionStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def get_account_deletion_status(self, request):
        runtime = util_models.RuntimeOptions()
        return self.get_account_deletion_status_with_options(request, runtime)

    def get_control_policy_with_options(self, request, runtime):
        """
        This topic provides an example on how to call the API operation to query the details of the access control policy whose ID is `cp-SImPt8GCEwiq***`.
        

        @param request: GetControlPolicyRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: GetControlPolicyResponse
        """
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
        """
        This topic provides an example on how to call the API operation to query the details of the access control policy whose ID is `cp-SImPt8GCEwiq***`.
        

        @param request: GetControlPolicyRequest

        @return: GetControlPolicyResponse
        """
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
        """
        In this example, the information of the folder `fd-Jyl5U7***` is queried.
        

        @param request: GetFolderRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: GetFolderResponse
        """
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
        """
        In this example, the information of the folder `fd-Jyl5U7***` is queried.
        

        @param request: GetFolderRequest

        @return: GetFolderResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_folder_with_options(request, runtime)

    def get_handshake_with_options(self, request, runtime):
        """
        In this example, the information of the invitation whose ID is `h-ycm4rp***` is queried.
        

        @param request: GetHandshakeRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: GetHandshakeResponse
        """
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
        """
        In this example, the information of the invitation whose ID is `h-ycm4rp***` is queried.
        

        @param request: GetHandshakeRequest

        @return: GetHandshakeResponse
        """
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
        """
        This topic provides an example on how to use a management account to call the API operation to query the information of the resource directory that is enabled by using the management account.
        

        @param request: GetResourceDirectoryRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: GetResourceDirectoryResponse
        """
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
        """
        This topic provides an example on how to use a management account to call the API operation to query the information of the resource directory that is enabled by using the management account.
        

        @return: GetResourceDirectoryResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_resource_directory_with_options(runtime)

    def get_resource_group_with_options(self, request, runtime):
        """
        For more information about common request parameters, see [Common parameters](~~159973~~).
        

        @param request: GetResourceGroupRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: GetResourceGroupResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.include_tags):
            query['IncludeTags'] = request.include_tags
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
        """
        For more information about common request parameters, see [Common parameters](~~159973~~).
        

        @param request: GetResourceGroupRequest

        @return: GetResourceGroupResponse
        """
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
        """
        >
        *   An account can be used to enable a resource directory only after it passes enterprise real-name verification. An account that only passed individual real-name verification cannot be used to enable a resource directory.
        *   We recommend that you only use the enterprise management account as the administrator of the resource directory. Do not use the enterprise management account to purchase cloud resources.
        

        @param request: InitResourceDirectoryRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: InitResourceDirectoryResponse
        """
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
        """
        >
        *   An account can be used to enable a resource directory only after it passes enterprise real-name verification. An account that only passed individual real-name verification cannot be used to enable a resource directory.
        *   We recommend that you only use the enterprise management account as the administrator of the resource directory. Do not use the enterprise management account to purchase cloud resources.
        

        @return: InitResourceDirectoryResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.init_resource_directory_with_options(runtime)

    def invite_account_to_resource_directory_with_options(self, request, runtime):
        """
        This topic provides an example on how to call the API operation to invite the account `someone@example.com` to join a resource directory.
        

        @param request: InviteAccountToResourceDirectoryRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: InviteAccountToResourceDirectoryResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.note):
            query['Note'] = request.note
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
        """
        This topic provides an example on how to call the API operation to invite the account `someone@example.com` to join a resource directory.
        

        @param request: InviteAccountToResourceDirectoryRequest

        @return: InviteAccountToResourceDirectoryResponse
        """
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
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
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
        """
        This topic provides an example on how to call the API operation to query the system access control policies within a resource directory. The response shows that the resource directory has only one system access control policy. The policy is named `FullAliyunAccess`.
        

        @param request: ListControlPoliciesRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListControlPoliciesResponse
        """
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
        """
        This topic provides an example on how to call the API operation to query the system access control policies within a resource directory. The response shows that the resource directory has only one system access control policy. The policy is named `FullAliyunAccess`.
        

        @param request: ListControlPoliciesRequest

        @return: ListControlPoliciesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_control_policies_with_options(request, runtime)

    def list_control_policy_attachments_for_target_with_options(self, request, runtime):
        """
        This topic provides an example on how to call the API operation to query the access control policies that are attached to the folder `fd-ZDNPiT***`.
        

        @param request: ListControlPolicyAttachmentsForTargetRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListControlPolicyAttachmentsForTargetResponse
        """
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
        """
        This topic provides an example on how to call the API operation to query the access control policies that are attached to the folder `fd-ZDNPiT***`.
        

        @param request: ListControlPolicyAttachmentsForTargetRequest

        @return: ListControlPolicyAttachmentsForTargetResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_control_policy_attachments_for_target_with_options(request, runtime)

    def list_delegated_administrators_with_options(self, request, runtime):
        """
        This topic provides an example on how to call the API operation to query all delegated administrator accounts in a resource directory. The response shows that two delegated administrator accounts for Cloud Firewall exist in the resource directory.
        

        @param request: ListDelegatedAdministratorsRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListDelegatedAdministratorsResponse
        """
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
        """
        This topic provides an example on how to call the API operation to query all delegated administrator accounts in a resource directory. The response shows that two delegated administrator accounts for Cloud Firewall exist in the resource directory.
        

        @param request: ListDelegatedAdministratorsRequest

        @return: ListDelegatedAdministratorsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_delegated_administrators_with_options(request, runtime)

    def list_delegated_services_for_account_with_options(self, request, runtime):
        """
        This topic provides an example on how to call the API operation to query the trusted services for which the member `138660628348***` is specified as a delegated administrator account. The response shows that the member is specified as a delegated administrator account of Cloud Firewall.
        

        @param request: ListDelegatedServicesForAccountRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListDelegatedServicesForAccountResponse
        """
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
        """
        This topic provides an example on how to call the API operation to query the trusted services for which the member `138660628348***` is specified as a delegated administrator account. The response shows that the member is specified as a delegated administrator account of Cloud Firewall.
        

        @param request: ListDelegatedServicesForAccountRequest

        @return: ListDelegatedServicesForAccountResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_delegated_services_for_account_with_options(request, runtime)

    def list_folders_for_parent_with_options(self, request, runtime):
        """
        >  You can view the information of only the first-level subfolders of a folder.
        

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
        """
        >  You can view the information of only the first-level subfolders of a folder.
        

        @param request: ListFoldersForParentRequest

        @return: ListFoldersForParentResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_folders_for_parent_with_options(request, runtime)

    def list_handshakes_for_account_with_options(self, request, runtime):
        """
        This topic provides an example on how to call the API operation to query the invitations that are associated with the management account `172841235500***`. The response shows that two invitations are associated with the management account.
        

        @param request: ListHandshakesForAccountRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListHandshakesForAccountResponse
        """
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
        """
        This topic provides an example on how to call the API operation to query the invitations that are associated with the management account `172841235500***`. The response shows that two invitations are associated with the management account.
        

        @param request: ListHandshakesForAccountRequest

        @return: ListHandshakesForAccountResponse
        """
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
        """
        You can view the following information:
        *   Policy attachment records under an Alibaba Cloud account or a resource group
        *   Policies attached to RAM users, RAM user groups, or RAM roles
        *   RAM users, RAM user groups, or RAM roles to which policies are attached under an Alibaba Cloud account or a resource group
        

        @param request: ListPolicyAttachmentsRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListPolicyAttachmentsResponse
        """
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
        """
        You can view the following information:
        *   Policy attachment records under an Alibaba Cloud account or a resource group
        *   Policies attached to RAM users, RAM user groups, or RAM roles
        *   RAM users, RAM user groups, or RAM roles to which policies are attached under an Alibaba Cloud account or a resource group
        

        @param request: ListPolicyAttachmentsRequest

        @return: ListPolicyAttachmentsResponse
        """
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
        """
        You can call this API operation to query all resource groups within the current account. You can also call this API operation to query a specific resource group based on the status, ID, identifier, or display name of the resource group.
        This topic provides an example on how to call the API operation to query the basic information about the resource groups `rg-1hSBH2****` and `rg-9gLOoK****` within the current account.
        

        @param request: ListResourceGroupsRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListResourceGroupsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.display_name):
            query['DisplayName'] = request.display_name
        if not UtilClient.is_unset(request.include_tags):
            query['IncludeTags'] = request.include_tags
        if not UtilClient.is_unset(request.name):
            query['Name'] = request.name
        if not UtilClient.is_unset(request.page_number):
            query['PageNumber'] = request.page_number
        if not UtilClient.is_unset(request.page_size):
            query['PageSize'] = request.page_size
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_group_ids):
            query['ResourceGroupIds'] = request.resource_group_ids
        if not UtilClient.is_unset(request.status):
            query['Status'] = request.status
        if not UtilClient.is_unset(request.tag):
            query['Tag'] = request.tag
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
        """
        You can call this API operation to query all resource groups within the current account. You can also call this API operation to query a specific resource group based on the status, ID, identifier, or display name of the resource group.
        This topic provides an example on how to call the API operation to query the basic information about the resource groups `rg-1hSBH2****` and `rg-9gLOoK****` within the current account.
        

        @param request: ListResourceGroupsRequest

        @return: ListResourceGroupsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_resource_groups_with_options(request, runtime)

    def list_resources_with_options(self, request, runtime):
        """
        >  You can use a RAM role that is not associated with a session policy to call this API operation.
        This topic provides an example on how to call the API operation to query the resources that can be accessed by the current account in resource groups. The response shows that the current account can access only the Elastic Compute Service (ECS) instance `i-23v38****` in the resource group `rg-uPJpP****`.
        

        @param request: ListResourcesRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListResourcesResponse
        """
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
        if not UtilClient.is_unset(request.resource_types):
            query['ResourceTypes'] = request.resource_types
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
        """
        >  You can use a RAM role that is not associated with a session policy to call this API operation.
        This topic provides an example on how to call the API operation to query the resources that can be accessed by the current account in resource groups. The response shows that the current account can access only the Elastic Compute Service (ECS) instance `i-23v38****` in the resource group `rg-uPJpP****`.
        

        @param request: ListResourcesRequest

        @return: ListResourcesResponse
        """
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

    def list_tag_keys_with_options(self, request, runtime):
        """
        This topic provides an example on how to call the API operation to query tag keys. The response shows that the custom tag key team exists.
        

        @param request: ListTagKeysRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListTagKeysResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.key_filter):
            query['KeyFilter'] = request.key_filter
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTagKeys',
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
            resource_manager_20200331_models.ListTagKeysResponse(),
            self.call_api(params, req, runtime)
        )

    def list_tag_keys(self, request):
        """
        This topic provides an example on how to call the API operation to query tag keys. The response shows that the custom tag key team exists.
        

        @param request: ListTagKeysRequest

        @return: ListTagKeysResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_tag_keys_with_options(request, runtime)

    def list_tag_resources_with_options(self, request, runtime):
        """
        This topic provides an example on how to call the API operation to query the tags that are added to the resource group with an ID of `rg-aekz6bre2uq***`. The response shows that only the `k1:v1` tag is added to the resource group.
        

        @param request: ListTagResourcesRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListTagResourcesResponse
        """
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
            resource_manager_20200331_models.ListTagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_tag_resources(self, request):
        """
        This topic provides an example on how to call the API operation to query the tags that are added to the resource group with an ID of `rg-aekz6bre2uq***`. The response shows that only the `k1:v1` tag is added to the resource group.
        

        @param request: ListTagResourcesRequest

        @return: ListTagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_tag_resources_with_options(request, runtime)

    def list_tag_values_with_options(self, request, runtime):
        """
        This topic provides an example on how to call the API operation to query the tag values of the tag key k1. The response shows that the tag value of the tag key k1 is v1.
        

        @param request: ListTagValuesRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListTagValuesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.tag_key):
            query['TagKey'] = request.tag_key
        if not UtilClient.is_unset(request.value_filter):
            query['ValueFilter'] = request.value_filter
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListTagValues',
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
            resource_manager_20200331_models.ListTagValuesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_tag_values(self, request):
        """
        This topic provides an example on how to call the API operation to query the tag values of the tag key k1. The response shows that the tag value of the tag key k1 is v1.
        

        @param request: ListTagValuesRequest

        @return: ListTagValuesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_tag_values_with_options(request, runtime)

    def list_target_attachments_for_control_policy_with_options(self, request, runtime):
        """
        In this example, the folders or member accounts to which the control policy `cp-jExXAqIYkwHN***` is attached are queried. The returned result shows that the control policy is attached to the folder `fd-ZDNPiT****`.
        

        @param request: ListTargetAttachmentsForControlPolicyRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListTargetAttachmentsForControlPolicyResponse
        """
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
        """
        In this example, the folders or member accounts to which the control policy `cp-jExXAqIYkwHN***` is attached are queried. The returned result shows that the control policy is attached to the folder `fd-ZDNPiT****`.
        

        @param request: ListTargetAttachmentsForControlPolicyRequest

        @return: ListTargetAttachmentsForControlPolicyResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_target_attachments_for_control_policy_with_options(request, runtime)

    def list_trusted_service_status_with_options(self, request, runtime):
        """
        >  Only an enterprise management account or delegated administrator account can be used to call this operation.
        In this example, the trusted services that are enabled within an enterprise management account are queried. The returned result shows that the trusted services Cloud Config and ActionTrail are enabled within the enterprise management account.
        

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
        """
        >  Only an enterprise management account or delegated administrator account can be used to call this operation.
        In this example, the trusted services that are enabled within an enterprise management account are queried. The returned result shows that the trusted services Cloud Config and ActionTrail are enabled within the enterprise management account.
        

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
        """
        For more information about Alibaba Cloud services whose resources can be moved between resource groups, see the *Supported by the API** column in [Alibaba Cloud services that support resource groups](~~94479~~).
        In this example, two virtual private clouds (VPCs) `vpc-bp1sig0mjktx5ewx1****` and `vpc-bp1visxm225pv49dz****` that reside in different regions and belong to different resource groups are moved to the resource group `rg-aekzmeobk5w****`.
        

        @param request: MoveResourcesRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: MoveResourcesResponse
        """
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
        """
        For more information about Alibaba Cloud services whose resources can be moved between resource groups, see the *Supported by the API** column in [Alibaba Cloud services that support resource groups](~~94479~~).
        In this example, two virtual private clouds (VPCs) `vpc-bp1sig0mjktx5ewx1****` and `vpc-bp1visxm225pv49dz****` that reside in different regions and belong to different resource groups are moved to the resource group `rg-aekzmeobk5w****`.
        

        @param request: MoveResourcesRequest

        @return: MoveResourcesResponse
        """
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
        """
        The delegated administrator account can be used to access the information of the resource directory and view the structure and members of the resource directory. The delegated administrator account can also be used to perform service-related management operations in the trusted service on behalf of the management account of the resource directory.
        When you call this operation, you must take note of the following limits:
        *   Only some trusted services support delegated administrator accounts. For more information, see [Supported trusted services](~~208133~~).
        *   Only the management account of a resource directory or an authorized RAM user or RAM role of the management account can be used to call this operation.
        *   The number of delegated administrator accounts that are allowed for a trusted service is defined by the trusted service.
        This topic provides an example on how to call the API operation to specify the member `181761095690****` as a delegated administrator account of Cloud Firewall.
        

        @param request: RegisterDelegatedAdministratorRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: RegisterDelegatedAdministratorResponse
        """
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
        """
        The delegated administrator account can be used to access the information of the resource directory and view the structure and members of the resource directory. The delegated administrator account can also be used to perform service-related management operations in the trusted service on behalf of the management account of the resource directory.
        When you call this operation, you must take note of the following limits:
        *   Only some trusted services support delegated administrator accounts. For more information, see [Supported trusted services](~~208133~~).
        *   Only the management account of a resource directory or an authorized RAM user or RAM role of the management account can be used to call this operation.
        *   The number of delegated administrator accounts that are allowed for a trusted service is defined by the trusted service.
        This topic provides an example on how to call the API operation to specify the member `181761095690****` as a delegated administrator account of Cloud Firewall.
        

        @param request: RegisterDelegatedAdministratorRequest

        @return: RegisterDelegatedAdministratorResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.register_delegated_administrator_with_options(request, runtime)

    def remove_cloud_account_with_options(self, request, runtime):
        """
        This topic provides an example on how to call the API operation to remove the member `177242285274***` from a resource directory.
        

        @param request: RemoveCloudAccountRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: RemoveCloudAccountResponse
        """
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
        """
        This topic provides an example on how to call the API operation to remove the member `177242285274***` from a resource directory.
        

        @param request: RemoveCloudAccountRequest

        @return: RemoveCloudAccountResponse
        """
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
            resource_manager_20200331_models.RetryChangeAccountEmailResponse(),
            self.call_api(params, req, runtime)
        )

    def retry_change_account_email(self, request):
        runtime = util_models.RuntimeOptions()
        return self.retry_change_account_email_with_options(request, runtime)

    def send_verification_code_for_bind_secure_mobile_phone_with_options(self, request, runtime):
        """
        To ensure that the system can record the operators of management operations, you must use a RAM user or RAM role to which the AliyunResourceDirectoryFullAccess policy is attached within the management account of your resource directory to call this operation.
        In this example, a verification code is sent to the mobile phone number that you want to bind to the resource account `138660628348****`.
        

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
        """
        To ensure that the system can record the operators of management operations, you must use a RAM user or RAM role to which the AliyunResourceDirectoryFullAccess policy is attached within the management account of your resource directory to call this operation.
        In this example, a verification code is sent to the mobile phone number that you want to bind to the resource account `138660628348****`.
        

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
        """
        Each Alibaba Cloud account can be used to send a maximum of 100 verification codes per day.
        

        @param request: SendVerificationCodeForEnableRDRequest

        @return: SendVerificationCodeForEnableRDResponse
        """
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
            resource_manager_20200331_models.SetMemberDeletionPermissionResponse(),
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
        """
        This topic provides an example on how to call the API operation to add the tag `k1:v1` to the resource group with an ID of `rg-aekz6bre2uq***`.
        

        @param request: TagResourcesRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: TagResourcesResponse
        """
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
            resource_manager_20200331_models.TagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    def tag_resources(self, request):
        """
        This topic provides an example on how to call the API operation to add the tag `k1:v1` to the resource group with an ID of `rg-aekz6bre2uq***`.
        

        @param request: TagResourcesRequest

        @return: TagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.tag_resources_with_options(request, runtime)

    def untag_resources_with_options(self, request, runtime):
        """
        This topic provides an example on how to call the API operation to remove the tag whose tag key is `k1` from the resource group whose ID is `rg-aek2dpwyrfr***`.
        

        @param request: UntagResourcesRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: UntagResourcesResponse
        """
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
            resource_manager_20200331_models.UntagResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    def untag_resources(self, request):
        """
        This topic provides an example on how to call the API operation to remove the tag whose tag key is `k1` from the resource group whose ID is `rg-aek2dpwyrfr***`.
        

        @param request: UntagResourcesRequest

        @return: UntagResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.untag_resources_with_options(request, runtime)

    def update_account_with_options(self, request, runtime):
        """
        To ensure that the system can record the operators of management operations, you must use a RAM user or RAM role to which the AliyunResourceDirectoryFullAccess policy is attached within the management account of your resource directory to call this operation.
        *   Before you switch the type of a member from resource account to cloud account, make sure that specific conditions are met. For more information about the conditions, see [Switch a resource account to a cloud account](~~111233~~).
        *   Before you switch the type of a member from cloud account to resource account, make sure that specific conditions are met. For more information about the conditions, see [Switch a cloud account to a resource account](~~209980~~).
        This example provides an example on how to call the API operation to change the display name of the member `12323344****` to `admin`.
        

        @param request: UpdateAccountRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: UpdateAccountResponse
        """
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
        """
        To ensure that the system can record the operators of management operations, you must use a RAM user or RAM role to which the AliyunResourceDirectoryFullAccess policy is attached within the management account of your resource directory to call this operation.
        *   Before you switch the type of a member from resource account to cloud account, make sure that specific conditions are met. For more information about the conditions, see [Switch a resource account to a cloud account](~~111233~~).
        *   Before you switch the type of a member from cloud account to resource account, make sure that specific conditions are met. For more information about the conditions, see [Switch a cloud account to a resource account](~~209980~~).
        This example provides an example on how to call the API operation to change the display name of the member `12323344****` to `admin`.
        

        @param request: UpdateAccountRequest

        @return: UpdateAccountResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_account_with_options(request, runtime)

    def update_control_policy_with_options(self, request, runtime):
        """
        In this example, the name of the access control policy whose ID is `cp-jExXAqIYkwHN***` is changed to `NewControlPolicy`.
        

        @param request: UpdateControlPolicyRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: UpdateControlPolicyResponse
        """
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
        """
        In this example, the name of the access control policy whose ID is `cp-jExXAqIYkwHN***` is changed to `NewControlPolicy`.
        

        @param request: UpdateControlPolicyRequest

        @return: UpdateControlPolicyResponse
        """
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
        """
        In this example, the display name of the resource group `rg-9gLOoK***` is changed to `project`.
        

        @param request: UpdateResourceGroupRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: UpdateResourceGroupResponse
        """
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
        """
        In this example, the display name of the resource group `rg-9gLOoK***` is changed to `project`.
        

        @param request: UpdateResourceGroupRequest

        @return: UpdateResourceGroupResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_resource_group_with_options(request, runtime)

    def update_role_with_options(self, request, runtime):
        """
        In this example, the description of the RAM role `ECSAdmin` is updated to `ECS administrator`.
        

        @param request: UpdateRoleRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: UpdateRoleResponse
        """
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
        """
        In this example, the description of the RAM role `ECSAdmin` is updated to `ECS administrator`.
        

        @param request: UpdateRoleRequest

        @return: UpdateRoleResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_role_with_options(request, runtime)
