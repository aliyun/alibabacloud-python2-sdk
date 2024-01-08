# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from __future__ import unicode_literals

from Tea.core import TeaCore

from alibabacloud_tea_openapi.client import Client as OpenApiClient
from alibabacloud_tea_openapi import models as open_api_models
from alibabacloud_tea_util.client import Client as UtilClient
from alibabacloud_endpoint_util.client import Client as EndpointUtilClient
from alibabacloud_resourcesharing20200110 import models as resource_sharing_20200110_models
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
        self._endpoint = self.get_endpoint('resourcesharing', self._region_id, self._endpoint_rule, self._network, self._suffix, self._endpoint_map, self._endpoint)

    def get_endpoint(self, product_id, region_id, endpoint_rule, network, suffix, endpoint_map, endpoint):
        if not UtilClient.empty(endpoint):
            return endpoint
        if not UtilClient.is_unset(endpoint_map) and not UtilClient.empty(endpoint_map.get(region_id)):
            return endpoint_map.get(region_id)
        return EndpointUtilClient.get_endpoint_rules(product_id, region_id, endpoint_rule, network, suffix)

    def accept_resource_share_invitation_with_options(self, request, runtime):
        """
        ### [](#)
        *   A principal needs to accept or reject a resource sharing invitation only if the principal is not the management account or a member of a resource directory. If you share resources with an object in a resource directory, the system automatically accepts the resource sharing invitation for the object.
        *   A resource sharing invitation is valid for seven days. A principal must accept or reject the invitation within the validity period.
        This topic provides an example on how to call the API operation to accept the resource sharing invitation whose ID is `i-pMnItMX19fBJ****` in the `cn-hangzhou` region.
        

        @param request: AcceptResourceShareInvitationRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: AcceptResourceShareInvitationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.resource_share_invitation_id):
            query['ResourceShareInvitationId'] = request.resource_share_invitation_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AcceptResourceShareInvitation',
            version='2020-01-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_sharing_20200110_models.AcceptResourceShareInvitationResponse(),
            self.call_api(params, req, runtime)
        )

    def accept_resource_share_invitation(self, request):
        """
        ### [](#)
        *   A principal needs to accept or reject a resource sharing invitation only if the principal is not the management account or a member of a resource directory. If you share resources with an object in a resource directory, the system automatically accepts the resource sharing invitation for the object.
        *   A resource sharing invitation is valid for seven days. A principal must accept or reject the invitation within the validity period.
        This topic provides an example on how to call the API operation to accept the resource sharing invitation whose ID is `i-pMnItMX19fBJ****` in the `cn-hangzhou` region.
        

        @param request: AcceptResourceShareInvitationRequest

        @return: AcceptResourceShareInvitationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.accept_resource_share_invitation_with_options(request, runtime)

    def associate_resource_share_with_options(self, request, runtime):
        """
        This topic provides an example on how to call the API operation to associate the vSwitch `vsw-bp183p93qs667muql***` and the member `172050525300****` with the resource share `rs-6GRmdD3X****` in the `cn-hangzhou` region. After the association, the vSwitch is shared with the member.
        

        @param request: AssociateResourceShareRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: AssociateResourceShareResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.permission_names):
            query['PermissionNames'] = request.permission_names
        if not UtilClient.is_unset(request.resource_share_id):
            query['ResourceShareId'] = request.resource_share_id
        if not UtilClient.is_unset(request.resources):
            query['Resources'] = request.resources
        if not UtilClient.is_unset(request.targets):
            query['Targets'] = request.targets
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AssociateResourceShare',
            version='2020-01-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_sharing_20200110_models.AssociateResourceShareResponse(),
            self.call_api(params, req, runtime)
        )

    def associate_resource_share(self, request):
        """
        This topic provides an example on how to call the API operation to associate the vSwitch `vsw-bp183p93qs667muql***` and the member `172050525300****` with the resource share `rs-6GRmdD3X****` in the `cn-hangzhou` region. After the association, the vSwitch is shared with the member.
        

        @param request: AssociateResourceShareRequest

        @return: AssociateResourceShareResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.associate_resource_share_with_options(request, runtime)

    def associate_resource_share_permission_with_options(self, request, runtime):
        """
        This topic provides an example on how to call the API operation to associate the `AliyunRSDefaultPermissionVSwitch` permission with the `rs-6GRmdD3X***` resource share in the `cn-hangzhou` region.
        

        @param request: AssociateResourceSharePermissionRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: AssociateResourceSharePermissionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.permission_name):
            query['PermissionName'] = request.permission_name
        if not UtilClient.is_unset(request.replace):
            query['Replace'] = request.replace
        if not UtilClient.is_unset(request.resource_share_id):
            query['ResourceShareId'] = request.resource_share_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='AssociateResourceSharePermission',
            version='2020-01-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_sharing_20200110_models.AssociateResourceSharePermissionResponse(),
            self.call_api(params, req, runtime)
        )

    def associate_resource_share_permission(self, request):
        """
        This topic provides an example on how to call the API operation to associate the `AliyunRSDefaultPermissionVSwitch` permission with the `rs-6GRmdD3X***` resource share in the `cn-hangzhou` region.
        

        @param request: AssociateResourceSharePermissionRequest

        @return: AssociateResourceSharePermissionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.associate_resource_share_permission_with_options(request, runtime)

    def change_resource_group_with_options(self, request, runtime):
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.resource_group_id):
            query['ResourceGroupId'] = request.resource_group_id
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_region_id):
            query['ResourceRegionId'] = request.resource_region_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ChangeResourceGroup',
            version='2020-01-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_sharing_20200110_models.ChangeResourceGroupResponse(),
            self.call_api(params, req, runtime)
        )

    def change_resource_group(self, request):
        runtime = util_models.RuntimeOptions()
        return self.change_resource_group_with_options(request, runtime)

    def check_sharing_with_resource_directory_status_with_options(self, runtime):
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='CheckSharingWithResourceDirectoryStatus',
            version='2020-01-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_sharing_20200110_models.CheckSharingWithResourceDirectoryStatusResponse(),
            self.call_api(params, req, runtime)
        )

    def check_sharing_with_resource_directory_status(self):
        runtime = util_models.RuntimeOptions()
        return self.check_sharing_with_resource_directory_status_with_options(runtime)

    def create_resource_share_with_options(self, request, runtime):
        """
        Resource Sharing allows you to share your resources with one or more accounts and access the resources shared by other accounts. For more information, see [Resource Sharing overview](~~160622~~).
        This topic provides an example on how to call the API operation to create a resource share named `test` in the `cn-hangzhou` region to share the vSwitch `vsw-bp183p93qs667muql****` with the member `172050525300****`. In this example, the management account of a resource directory is used to call this API operation.
        

        @param request: CreateResourceShareRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: CreateResourceShareResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.allow_external_targets):
            query['AllowExternalTargets'] = request.allow_external_targets
        if not UtilClient.is_unset(request.permission_names):
            query['PermissionNames'] = request.permission_names
        if not UtilClient.is_unset(request.resource_share_name):
            query['ResourceShareName'] = request.resource_share_name
        if not UtilClient.is_unset(request.resources):
            query['Resources'] = request.resources
        if not UtilClient.is_unset(request.targets):
            query['Targets'] = request.targets
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='CreateResourceShare',
            version='2020-01-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_sharing_20200110_models.CreateResourceShareResponse(),
            self.call_api(params, req, runtime)
        )

    def create_resource_share(self, request):
        """
        Resource Sharing allows you to share your resources with one or more accounts and access the resources shared by other accounts. For more information, see [Resource Sharing overview](~~160622~~).
        This topic provides an example on how to call the API operation to create a resource share named `test` in the `cn-hangzhou` region to share the vSwitch `vsw-bp183p93qs667muql****` with the member `172050525300****`. In this example, the management account of a resource directory is used to call this API operation.
        

        @param request: CreateResourceShareRequest

        @return: CreateResourceShareResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.create_resource_share_with_options(request, runtime)

    def delete_resource_share_with_options(self, request, runtime):
        """
        After a resource share is deleted, all principals in the resource share can no longer access the resources in the resource share. However, the resources are not deleted with the resource share.
        A resource share that is deleted is in the `Deleted` state. The system deletes the record of the resource share within 48 hours to 96 hours.
        This topic provides an example on how to call the API operation to delete the resource share `rs-qSkW1HBY****` in the `cn-hangzhou` region.
        

        @param request: DeleteResourceShareRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DeleteResourceShareResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.resource_share_id):
            query['ResourceShareId'] = request.resource_share_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DeleteResourceShare',
            version='2020-01-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_sharing_20200110_models.DeleteResourceShareResponse(),
            self.call_api(params, req, runtime)
        )

    def delete_resource_share(self, request):
        """
        After a resource share is deleted, all principals in the resource share can no longer access the resources in the resource share. However, the resources are not deleted with the resource share.
        A resource share that is deleted is in the `Deleted` state. The system deletes the record of the resource share within 48 hours to 96 hours.
        This topic provides an example on how to call the API operation to delete the resource share `rs-qSkW1HBY****` in the `cn-hangzhou` region.
        

        @param request: DeleteResourceShareRequest

        @return: DeleteResourceShareResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.delete_resource_share_with_options(request, runtime)

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
            version='2020-01-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_sharing_20200110_models.DescribeRegionsResponse(),
            self.call_api(params, req, runtime)
        )

    def describe_regions(self, request):
        runtime = util_models.RuntimeOptions()
        return self.describe_regions_with_options(request, runtime)

    def disassociate_resource_share_with_options(self, request, runtime):
        """
        A resource owner can call this API operation to remove shared resources or principals from a resource share.
        *   If an Alibaba Cloud account that is not the management account or a member of a resource directory is added to a resource share as a principal, you can use the Alibaba Cloud account to call this API operation to exit the resource share. For more information, see [Exit a resource share](~~440614~~).
        This topic provides an example on how to use the management account of a resource directory to call the API operation to remove the member `172050525300****` from the resource share `rs-6GRmdD3X****` in the `cn-hangzhou` region. After the member is removed from the resource share, the member cannot share the resources in the resource share.
        

        @param request: DisassociateResourceShareRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DisassociateResourceShareResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.resource_owner):
            query['ResourceOwner'] = request.resource_owner
        if not UtilClient.is_unset(request.resource_share_id):
            query['ResourceShareId'] = request.resource_share_id
        if not UtilClient.is_unset(request.resources):
            query['Resources'] = request.resources
        if not UtilClient.is_unset(request.targets):
            query['Targets'] = request.targets
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DisassociateResourceShare',
            version='2020-01-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_sharing_20200110_models.DisassociateResourceShareResponse(),
            self.call_api(params, req, runtime)
        )

    def disassociate_resource_share(self, request):
        """
        A resource owner can call this API operation to remove shared resources or principals from a resource share.
        *   If an Alibaba Cloud account that is not the management account or a member of a resource directory is added to a resource share as a principal, you can use the Alibaba Cloud account to call this API operation to exit the resource share. For more information, see [Exit a resource share](~~440614~~).
        This topic provides an example on how to use the management account of a resource directory to call the API operation to remove the member `172050525300****` from the resource share `rs-6GRmdD3X****` in the `cn-hangzhou` region. After the member is removed from the resource share, the member cannot share the resources in the resource share.
        

        @param request: DisassociateResourceShareRequest

        @return: DisassociateResourceShareResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.disassociate_resource_share_with_options(request, runtime)

    def disassociate_resource_share_permission_with_options(self, request, runtime):
        """
        This topic provides an example on how to call the API operation to disassociate the `AliyunRSDefaultPermissionVSwitch` permission from the `rs-6GRmdD3X***` resource share in the `cn-hangzhou` region.
        

        @param request: DisassociateResourceSharePermissionRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: DisassociateResourceSharePermissionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.permission_name):
            query['PermissionName'] = request.permission_name
        if not UtilClient.is_unset(request.resource_share_id):
            query['ResourceShareId'] = request.resource_share_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='DisassociateResourceSharePermission',
            version='2020-01-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_sharing_20200110_models.DisassociateResourceSharePermissionResponse(),
            self.call_api(params, req, runtime)
        )

    def disassociate_resource_share_permission(self, request):
        """
        This topic provides an example on how to call the API operation to disassociate the `AliyunRSDefaultPermissionVSwitch` permission from the `rs-6GRmdD3X***` resource share in the `cn-hangzhou` region.
        

        @param request: DisassociateResourceSharePermissionRequest

        @return: DisassociateResourceSharePermissionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.disassociate_resource_share_permission_with_options(request, runtime)

    def enable_sharing_with_resource_directory_with_options(self, runtime):
        """
        You can share your resources with all members in your resource directory, all members in a specific folder in your resource directory, or a specific member in your resource directory as a resource owner only after you enable resource sharing for your resource directory.
        You can call this API operation only by using the management account of your resource directory or a RAM user or RAM role to which the required permissions are granted within the management account.
        

        @param request: EnableSharingWithResourceDirectoryRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: EnableSharingWithResourceDirectoryResponse
        """
        req = open_api_models.OpenApiRequest()
        params = open_api_models.Params(
            action='EnableSharingWithResourceDirectory',
            version='2020-01-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_sharing_20200110_models.EnableSharingWithResourceDirectoryResponse(),
            self.call_api(params, req, runtime)
        )

    def enable_sharing_with_resource_directory(self):
        """
        You can share your resources with all members in your resource directory, all members in a specific folder in your resource directory, or a specific member in your resource directory as a resource owner only after you enable resource sharing for your resource directory.
        You can call this API operation only by using the management account of your resource directory or a RAM user or RAM role to which the required permissions are granted within the management account.
        

        @return: EnableSharingWithResourceDirectoryResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.enable_sharing_with_resource_directory_with_options(runtime)

    def get_permission_with_options(self, request, runtime):
        """
        This topic provides an example on how to call the API operation to query the information about the `AliyunRSDefaultPermissionVSwitch` permission whose version is `v1` in the `cn-hangzhou` region.
        

        @param request: GetPermissionRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: GetPermissionResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.permission_name):
            query['PermissionName'] = request.permission_name
        if not UtilClient.is_unset(request.permission_version):
            query['PermissionVersion'] = request.permission_version
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='GetPermission',
            version='2020-01-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_sharing_20200110_models.GetPermissionResponse(),
            self.call_api(params, req, runtime)
        )

    def get_permission(self, request):
        """
        This topic provides an example on how to call the API operation to query the information about the `AliyunRSDefaultPermissionVSwitch` permission whose version is `v1` in the `cn-hangzhou` region.
        

        @param request: GetPermissionRequest

        @return: GetPermissionResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.get_permission_with_options(request, runtime)

    def list_permission_versions_with_options(self, request, runtime):
        """
        This topic provides an example on how to call the API operation to query the versions of the `AliyunRSDefaultPermissionVSwitch` permission in the `cn-hangzhou` region.
        

        @param request: ListPermissionVersionsRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListPermissionVersionsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.permission_name):
            query['PermissionName'] = request.permission_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListPermissionVersions',
            version='2020-01-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_sharing_20200110_models.ListPermissionVersionsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_permission_versions(self, request):
        """
        This topic provides an example on how to call the API operation to query the versions of the `AliyunRSDefaultPermissionVSwitch` permission in the `cn-hangzhou` region.
        

        @param request: ListPermissionVersionsRequest

        @return: ListPermissionVersionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_permission_versions_with_options(request, runtime)

    def list_permissions_with_options(self, request, runtime):
        """
        This topic provides an example on how to call the API operation to query the information about the default permission for the `VSwitch` resource type in the `cn-hangzhou` region.
        

        @param request: ListPermissionsRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListPermissionsResponse
        """
        UtilClient.validate_model(request)
        query = {}
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
            action='ListPermissions',
            version='2020-01-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_sharing_20200110_models.ListPermissionsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_permissions(self, request):
        """
        This topic provides an example on how to call the API operation to query the information about the default permission for the `VSwitch` resource type in the `cn-hangzhou` region.
        

        @param request: ListPermissionsRequest

        @return: ListPermissionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_permissions_with_options(request, runtime)

    def list_resource_share_associations_with_options(self, request, runtime):
        """
        This topic provides an example on how to call the API operation to query the association records of the resource shares that are created by using the current Alibaba Cloud account in the `cn-hangzhou` region. The response shows the following records:
        *   The resource `vsw-bp1upw03qyz8n7us9****` of the `VSwitch` type has been associated with the resource share `rs-6GRmdD3X****`. The resource is in the `Associated` state. This indicates that the resource is being shared.
        *   The resource `vsw-bp183p93qs667muql****` of the `VSwitch` type has been disassociated from the resource share `rs-6GRmdD3X****`. The resource is in the `Disassociated` state. This indicates that the sharing of the resource is stopped.
        

        @param request: ListResourceShareAssociationsRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListResourceShareAssociationsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.association_status):
            query['AssociationStatus'] = request.association_status
        if not UtilClient.is_unset(request.association_type):
            query['AssociationType'] = request.association_type
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_share_ids):
            query['ResourceShareIds'] = request.resource_share_ids
        if not UtilClient.is_unset(request.target):
            query['Target'] = request.target
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListResourceShareAssociations',
            version='2020-01-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_sharing_20200110_models.ListResourceShareAssociationsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_resource_share_associations(self, request):
        """
        This topic provides an example on how to call the API operation to query the association records of the resource shares that are created by using the current Alibaba Cloud account in the `cn-hangzhou` region. The response shows the following records:
        *   The resource `vsw-bp1upw03qyz8n7us9****` of the `VSwitch` type has been associated with the resource share `rs-6GRmdD3X****`. The resource is in the `Associated` state. This indicates that the resource is being shared.
        *   The resource `vsw-bp183p93qs667muql****` of the `VSwitch` type has been disassociated from the resource share `rs-6GRmdD3X****`. The resource is in the `Disassociated` state. This indicates that the sharing of the resource is stopped.
        

        @param request: ListResourceShareAssociationsRequest

        @return: ListResourceShareAssociationsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_resource_share_associations_with_options(request, runtime)

    def list_resource_share_invitations_with_options(self, request, runtime):
        """
        ### [](#)
        This topic provides an example on how to call the API operation to query the resource sharing invitations that are received by the current account in the `cn-hangzhou` region. The response shows that one invitation is received by the current account and is waiting for confirmation.
        

        @param request: ListResourceShareInvitationsRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListResourceShareInvitationsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.resource_share_ids):
            query['ResourceShareIds'] = request.resource_share_ids
        if not UtilClient.is_unset(request.resource_share_invitation_ids):
            query['ResourceShareInvitationIds'] = request.resource_share_invitation_ids
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListResourceShareInvitations',
            version='2020-01-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_sharing_20200110_models.ListResourceShareInvitationsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_resource_share_invitations(self, request):
        """
        ### [](#)
        This topic provides an example on how to call the API operation to query the resource sharing invitations that are received by the current account in the `cn-hangzhou` region. The response shows that one invitation is received by the current account and is waiting for confirmation.
        

        @param request: ListResourceShareInvitationsRequest

        @return: ListResourceShareInvitationsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_resource_share_invitations_with_options(request, runtime)

    def list_resource_share_permissions_with_options(self, request, runtime):
        """
        This topic provides an example on how to call the API operation to query the permissions that are associated with the resource share created by using the current Alibaba Cloud account in the `cn-hangzhou` region.
        

        @param request: ListResourceSharePermissionsRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListResourceSharePermissionsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.resource_owner):
            query['ResourceOwner'] = request.resource_owner
        if not UtilClient.is_unset(request.resource_share_id):
            query['ResourceShareId'] = request.resource_share_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListResourceSharePermissions',
            version='2020-01-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_sharing_20200110_models.ListResourceSharePermissionsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_resource_share_permissions(self, request):
        """
        This topic provides an example on how to call the API operation to query the permissions that are associated with the resource share created by using the current Alibaba Cloud account in the `cn-hangzhou` region.
        

        @param request: ListResourceSharePermissionsRequest

        @return: ListResourceSharePermissionsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_resource_share_permissions_with_options(request, runtime)

    def list_resource_shares_with_options(self, request, runtime):
        """
        This topic provides an example on how to call the API operation to query the resource shares that are created by using the current Alibaba Cloud account in the `cn-hangzhou` region. The response shows that the following resource shares are created by using the account whose ID is `151266687691***`:
        *   `rs-hX9wC5jO****`, which is in the `Deleted` state
        *   `rs-PqysnzIj****`, which is in the `Active` state
        

        @param request: ListResourceSharesRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListResourceSharesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.permission_name):
            query['PermissionName'] = request.permission_name
        if not UtilClient.is_unset(request.resource_owner):
            query['ResourceOwner'] = request.resource_owner
        if not UtilClient.is_unset(request.resource_share_ids):
            query['ResourceShareIds'] = request.resource_share_ids
        if not UtilClient.is_unset(request.resource_share_name):
            query['ResourceShareName'] = request.resource_share_name
        if not UtilClient.is_unset(request.resource_share_status):
            query['ResourceShareStatus'] = request.resource_share_status
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListResourceShares',
            version='2020-01-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_sharing_20200110_models.ListResourceSharesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_resource_shares(self, request):
        """
        This topic provides an example on how to call the API operation to query the resource shares that are created by using the current Alibaba Cloud account in the `cn-hangzhou` region. The response shows that the following resource shares are created by using the account whose ID is `151266687691***`:
        *   `rs-hX9wC5jO****`, which is in the `Deleted` state
        *   `rs-PqysnzIj****`, which is in the `Active` state
        

        @param request: ListResourceSharesRequest

        @return: ListResourceSharesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_resource_shares_with_options(request, runtime)

    def list_shared_resources_with_options(self, request, runtime):
        """
        This topic provides an example on how to call the API operation to query the resources that you share with other accounts in the `cn-hangzhou` region. The response shows that in the resource share `rs-6GRmdD3X***`, you share the `vsw-bp1upw03qyz8n7us9****` resource of the `VSwitch` type with other accounts.
        

        @param request: ListSharedResourcesRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListSharedResourcesResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.resource_ids):
            query['ResourceIds'] = request.resource_ids
        if not UtilClient.is_unset(request.resource_owner):
            query['ResourceOwner'] = request.resource_owner
        if not UtilClient.is_unset(request.resource_share_ids):
            query['ResourceShareIds'] = request.resource_share_ids
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.target):
            query['Target'] = request.target
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSharedResources',
            version='2020-01-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_sharing_20200110_models.ListSharedResourcesResponse(),
            self.call_api(params, req, runtime)
        )

    def list_shared_resources(self, request):
        """
        This topic provides an example on how to call the API operation to query the resources that you share with other accounts in the `cn-hangzhou` region. The response shows that in the resource share `rs-6GRmdD3X***`, you share the `vsw-bp1upw03qyz8n7us9****` resource of the `VSwitch` type with other accounts.
        

        @param request: ListSharedResourcesRequest

        @return: ListSharedResourcesResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_shared_resources_with_options(request, runtime)

    def list_shared_targets_with_options(self, request, runtime):
        """
        If you are a resource owner, you can query the principals with which you share your resources.
        If you are a principal, you can query the resources that are shared with you.
        This topic provides an example on how to call the API operation to query the principals with which you share your resources in the `cn-hangzhou` region. The response shows that you share your resources with the principals `114240524784****` and `172050525300****`.
        

        @param request: ListSharedTargetsRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: ListSharedTargetsResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.max_results):
            query['MaxResults'] = request.max_results
        if not UtilClient.is_unset(request.next_token):
            query['NextToken'] = request.next_token
        if not UtilClient.is_unset(request.resource_id):
            query['ResourceId'] = request.resource_id
        if not UtilClient.is_unset(request.resource_owner):
            query['ResourceOwner'] = request.resource_owner
        if not UtilClient.is_unset(request.resource_share_ids):
            query['ResourceShareIds'] = request.resource_share_ids
        if not UtilClient.is_unset(request.resource_type):
            query['ResourceType'] = request.resource_type
        if not UtilClient.is_unset(request.targets):
            query['Targets'] = request.targets
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='ListSharedTargets',
            version='2020-01-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_sharing_20200110_models.ListSharedTargetsResponse(),
            self.call_api(params, req, runtime)
        )

    def list_shared_targets(self, request):
        """
        If you are a resource owner, you can query the principals with which you share your resources.
        If you are a principal, you can query the resources that are shared with you.
        This topic provides an example on how to call the API operation to query the principals with which you share your resources in the `cn-hangzhou` region. The response shows that you share your resources with the principals `114240524784****` and `172050525300****`.
        

        @param request: ListSharedTargetsRequest

        @return: ListSharedTargetsResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.list_shared_targets_with_options(request, runtime)

    def reject_resource_share_invitation_with_options(self, request, runtime):
        """
        This topic provides an example on how to call the API operation to reject the resource sharing invitation `i-yyTWbkjHArYh***` in the `cn-hangzhou` region.
        

        @param request: RejectResourceShareInvitationRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: RejectResourceShareInvitationResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.resource_share_invitation_id):
            query['ResourceShareInvitationId'] = request.resource_share_invitation_id
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='RejectResourceShareInvitation',
            version='2020-01-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_sharing_20200110_models.RejectResourceShareInvitationResponse(),
            self.call_api(params, req, runtime)
        )

    def reject_resource_share_invitation(self, request):
        """
        This topic provides an example on how to call the API operation to reject the resource sharing invitation `i-yyTWbkjHArYh***` in the `cn-hangzhou` region.
        

        @param request: RejectResourceShareInvitationRequest

        @return: RejectResourceShareInvitationResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.reject_resource_share_invitation_with_options(request, runtime)

    def update_resource_share_with_options(self, request, runtime):
        """
        You can call this API operation to change the name or resource sharing scope of a resource share.
        This topic provides an example on how to call the API operation to change the name of the resource share `rs-qSkW1HBY****` in the `cn-hangzhou` region from `test` to `new`.
        

        @param request: UpdateResourceShareRequest

        @param runtime: runtime options for this request RuntimeOptions

        @return: UpdateResourceShareResponse
        """
        UtilClient.validate_model(request)
        query = {}
        if not UtilClient.is_unset(request.allow_external_targets):
            query['AllowExternalTargets'] = request.allow_external_targets
        if not UtilClient.is_unset(request.resource_share_id):
            query['ResourceShareId'] = request.resource_share_id
        if not UtilClient.is_unset(request.resource_share_name):
            query['ResourceShareName'] = request.resource_share_name
        req = open_api_models.OpenApiRequest(
            query=OpenApiUtilClient.query(query)
        )
        params = open_api_models.Params(
            action='UpdateResourceShare',
            version='2020-01-10',
            protocol='HTTPS',
            pathname='/',
            method='POST',
            auth_type='AK',
            style='RPC',
            req_body_type='formData',
            body_type='json'
        )
        return TeaCore.from_map(
            resource_sharing_20200110_models.UpdateResourceShareResponse(),
            self.call_api(params, req, runtime)
        )

    def update_resource_share(self, request):
        """
        You can call this API operation to change the name or resource sharing scope of a resource share.
        This topic provides an example on how to call the API operation to change the name of the resource share `rs-qSkW1HBY****` in the `cn-hangzhou` region from `test` to `new`.
        

        @param request: UpdateResourceShareRequest

        @return: UpdateResourceShareResponse
        """
        runtime = util_models.RuntimeOptions()
        return self.update_resource_share_with_options(request, runtime)
