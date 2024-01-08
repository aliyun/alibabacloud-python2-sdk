# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class AcceptResourceShareInvitationRequest(TeaModel):
    def __init__(self, resource_share_invitation_id=None):
        # The ID of the resource sharing invitation.
        # 
        # You can call the [ListResourceShareInvitations](~~450564~~) operation to obtain the ID.
        self.resource_share_invitation_id = resource_share_invitation_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AcceptResourceShareInvitationRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_share_invitation_id is not None:
            result['ResourceShareInvitationId'] = self.resource_share_invitation_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ResourceShareInvitationId') is not None:
            self.resource_share_invitation_id = m.get('ResourceShareInvitationId')
        return self


class AcceptResourceShareInvitationResponseBodyResourceShareInvitationAcceptInvitationFailedDetails(TeaModel):
    def __init__(self, associate_type=None, resource_id=None, resource_type=None, status=None, status_message=None):
        # The type of the sharing operation. Valid values:
        # 
        # *   Associate
        self.associate_type = associate_type  # type: str
        # The ID of the shared resource.
        self.resource_id = resource_id  # type: str
        # The type of the shared resource.
        # 
        # For more information about the types of resources that can be shared, see [Services that work with Resource Sharing](~~450526~~).
        self.resource_type = resource_type  # type: str
        # The failure status. Valid values:
        # 
        # *   Unavailable: The resource cannot be shared.
        # *   LimitExceeded: The number of shared resources within the Alibaba Cloud account exceeds the upper limit.
        # *   ZonalResourceInaccessible: The resource is unavailable in this region.
        # *   InternalError: An internal error occurred during the check.
        self.status = status  # type: str
        # The failure cause.
        self.status_message = status_message  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AcceptResourceShareInvitationResponseBodyResourceShareInvitationAcceptInvitationFailedDetails, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.associate_type is not None:
            result['AssociateType'] = self.associate_type
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.status is not None:
            result['Status'] = self.status
        if self.status_message is not None:
            result['StatusMessage'] = self.status_message
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AssociateType') is not None:
            self.associate_type = m.get('AssociateType')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('StatusMessage') is not None:
            self.status_message = m.get('StatusMessage')
        return self


class AcceptResourceShareInvitationResponseBodyResourceShareInvitation(TeaModel):
    def __init__(self, accept_invitation_failed_details=None, create_time=None, receiver_account_id=None,
                 resource_share_id=None, resource_share_invitation_id=None, resource_share_name=None, sender_account_id=None,
                 status=None):
        # The information about the failure.
        self.accept_invitation_failed_details = accept_invitation_failed_details  # type: list[AcceptResourceShareInvitationResponseBodyResourceShareInvitationAcceptInvitationFailedDetails]
        # The time when the invitation was created. The time is displayed in UTC.
        self.create_time = create_time  # type: str
        # The Alibaba Cloud account ID of the invitee.
        self.receiver_account_id = receiver_account_id  # type: str
        # The ID of the resource share.
        self.resource_share_id = resource_share_id  # type: str
        # The ID of the resource sharing invitation.
        self.resource_share_invitation_id = resource_share_invitation_id  # type: str
        # The name of the resource share.
        self.resource_share_name = resource_share_name  # type: str
        # The Alibaba Cloud account ID of the inviter.
        self.sender_account_id = sender_account_id  # type: str
        # The status of the invitation. Valid values:
        # 
        # *   Pending
        # *   Accepted
        # *   Cancelled
        # *   Rejected
        # *   Expired
        # *   AcceptFailed
        self.status = status  # type: str

    def validate(self):
        if self.accept_invitation_failed_details:
            for k in self.accept_invitation_failed_details:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(AcceptResourceShareInvitationResponseBodyResourceShareInvitation, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AcceptInvitationFailedDetails'] = []
        if self.accept_invitation_failed_details is not None:
            for k in self.accept_invitation_failed_details:
                result['AcceptInvitationFailedDetails'].append(k.to_map() if k else None)
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.receiver_account_id is not None:
            result['ReceiverAccountId'] = self.receiver_account_id
        if self.resource_share_id is not None:
            result['ResourceShareId'] = self.resource_share_id
        if self.resource_share_invitation_id is not None:
            result['ResourceShareInvitationId'] = self.resource_share_invitation_id
        if self.resource_share_name is not None:
            result['ResourceShareName'] = self.resource_share_name
        if self.sender_account_id is not None:
            result['SenderAccountId'] = self.sender_account_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.accept_invitation_failed_details = []
        if m.get('AcceptInvitationFailedDetails') is not None:
            for k in m.get('AcceptInvitationFailedDetails'):
                temp_model = AcceptResourceShareInvitationResponseBodyResourceShareInvitationAcceptInvitationFailedDetails()
                self.accept_invitation_failed_details.append(temp_model.from_map(k))
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ReceiverAccountId') is not None:
            self.receiver_account_id = m.get('ReceiverAccountId')
        if m.get('ResourceShareId') is not None:
            self.resource_share_id = m.get('ResourceShareId')
        if m.get('ResourceShareInvitationId') is not None:
            self.resource_share_invitation_id = m.get('ResourceShareInvitationId')
        if m.get('ResourceShareName') is not None:
            self.resource_share_name = m.get('ResourceShareName')
        if m.get('SenderAccountId') is not None:
            self.sender_account_id = m.get('SenderAccountId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class AcceptResourceShareInvitationResponseBody(TeaModel):
    def __init__(self, request_id=None, resource_share_invitation=None):
        # The request ID.
        self.request_id = request_id  # type: str
        # The information about the resource sharing invitation.
        self.resource_share_invitation = resource_share_invitation  # type: AcceptResourceShareInvitationResponseBodyResourceShareInvitation

    def validate(self):
        if self.resource_share_invitation:
            self.resource_share_invitation.validate()

    def to_map(self):
        _map = super(AcceptResourceShareInvitationResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.resource_share_invitation is not None:
            result['ResourceShareInvitation'] = self.resource_share_invitation.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResourceShareInvitation') is not None:
            temp_model = AcceptResourceShareInvitationResponseBodyResourceShareInvitation()
            self.resource_share_invitation = temp_model.from_map(m['ResourceShareInvitation'])
        return self


class AcceptResourceShareInvitationResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: AcceptResourceShareInvitationResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AcceptResourceShareInvitationResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = AcceptResourceShareInvitationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AssociateResourceShareRequestResources(TeaModel):
    def __init__(self, resource_id=None, resource_type=None):
        # The ID of a shared resource.
        # 
        # Valid values of N: 1 to 5. This indicates that a maximum of five shared resources can be specified at a time.
        # 
        # >  Resources.N.ResourceId and Resources.N.ResourceType must be used in pairs.
        self.resource_id = resource_id  # type: str
        # The type of a shared resource.
        # 
        # Valid values of N: 1 to 5. This indicates that a maximum of five shared resources can be specified at a time.
        # 
        # For more information about the types of resources that can be shared, see [Services that work with Resource Sharing](~~450526~~).
        # 
        # >  `Resources.N.ResourceId` and `Resources.N.ResourceType` must be used in pairs.
        self.resource_type = resource_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AssociateResourceShareRequestResources, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        return self


class AssociateResourceShareRequest(TeaModel):
    def __init__(self, permission_names=None, resource_share_id=None, resources=None, targets=None):
        # The information about the permissions. If you do not configure this parameter, the system automatically associates the default permission for the specified resource type with the resource share. For more information, see [Permission library](~~465474~~).
        self.permission_names = permission_names  # type: list[str]
        # The ID of the resource share.
        self.resource_share_id = resource_share_id  # type: str
        # The information about the resources.
        self.resources = resources  # type: list[AssociateResourceShareRequestResources]
        # The information about the principals.
        self.targets = targets  # type: list[str]

    def validate(self):
        if self.resources:
            for k in self.resources:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(AssociateResourceShareRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.permission_names is not None:
            result['PermissionNames'] = self.permission_names
        if self.resource_share_id is not None:
            result['ResourceShareId'] = self.resource_share_id
        result['Resources'] = []
        if self.resources is not None:
            for k in self.resources:
                result['Resources'].append(k.to_map() if k else None)
        if self.targets is not None:
            result['Targets'] = self.targets
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PermissionNames') is not None:
            self.permission_names = m.get('PermissionNames')
        if m.get('ResourceShareId') is not None:
            self.resource_share_id = m.get('ResourceShareId')
        self.resources = []
        if m.get('Resources') is not None:
            for k in m.get('Resources'):
                temp_model = AssociateResourceShareRequestResources()
                self.resources.append(temp_model.from_map(k))
        if m.get('Targets') is not None:
            self.targets = m.get('Targets')
        return self


class AssociateResourceShareResponseBodyResourceShareAssociations(TeaModel):
    def __init__(self, association_status=None, association_status_message=None, association_type=None,
                 create_time=None, entity_id=None, entity_type=None, resource_share_id=None, resource_share_name=None,
                 target_property=None, update_time=None):
        # The association status. Valid values:
        # 
        # *   Associating: The entity is being associated.
        # *   Associated: The entity is associated.
        # *   Failed: The entity fails to be associated.
        # *   Disassociating: The entity is being disassociated.
        # *   Disassociated: The entity is disassociated.
        # 
        # >  The system deletes the records of entities in the `Failed` or `Disassociated` state within 48 hours to 96 hours.
        self.association_status = association_status  # type: str
        # The cause of the association failure.
        self.association_status_message = association_status_message  # type: str
        # The association type. Valid values:
        # 
        # *   Resource
        # *   Target
        self.association_type = association_type  # type: str
        # The time when the association of the entity was created. The value of this parameter depends on the value of the AssociationType parameter:
        # 
        # *   If the value of `AssociationType` is `Resource`, the value of this parameter is the time when the shared resource was associated with the resource share.
        # *   If the value of `AssociationType` is `Target`, the value of this parameter is the time when the principal was associated with the resource share.
        self.create_time = create_time  # type: str
        # The ID of the entity. The value of this parameter depends on the value of the AssociationType parameter:
        # 
        # *   If the value of `AssociationType` is `Resource`, the value of this parameter is the ID of the shared resource.
        # *   If the value of `AssociationType` is `Target`, the value of this parameter is the ID of the principal.
        self.entity_id = entity_id  # type: str
        # The type of the entity. The value of this parameter depends on the value of the AssociationType parameter:
        # 
        # *   If the value of AssociationType is Resource, the value of this parameter is the type of the shared resource. For more information about the types of resources that can be shared, see [Services that work with Resource Sharing](~~450526~~).
        # *   If the value of AssociationType is Target, the value of this parameter is `Account`.
        self.entity_type = entity_type  # type: str
        # The ID of the resource share.
        self.resource_share_id = resource_share_id  # type: str
        # The name of the resource share.
        self.resource_share_name = resource_share_name  # type: str
        self.target_property = target_property  # type: str
        # The time when the association of the entity was updated. The value of this parameter depends on the value of the AssociationType parameter:
        # 
        # *   If the value of `AssociationType` is `Resource`, the value of this parameter is the time when the association of the shared resource was updated.
        # *   If the value of `AssociationType` is `Target`, the value of this parameter is the time when the association of the principal was updated.
        self.update_time = update_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AssociateResourceShareResponseBodyResourceShareAssociations, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.association_status is not None:
            result['AssociationStatus'] = self.association_status
        if self.association_status_message is not None:
            result['AssociationStatusMessage'] = self.association_status_message
        if self.association_type is not None:
            result['AssociationType'] = self.association_type
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.entity_id is not None:
            result['EntityId'] = self.entity_id
        if self.entity_type is not None:
            result['EntityType'] = self.entity_type
        if self.resource_share_id is not None:
            result['ResourceShareId'] = self.resource_share_id
        if self.resource_share_name is not None:
            result['ResourceShareName'] = self.resource_share_name
        if self.target_property is not None:
            result['TargetProperty'] = self.target_property
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AssociationStatus') is not None:
            self.association_status = m.get('AssociationStatus')
        if m.get('AssociationStatusMessage') is not None:
            self.association_status_message = m.get('AssociationStatusMessage')
        if m.get('AssociationType') is not None:
            self.association_type = m.get('AssociationType')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('EntityId') is not None:
            self.entity_id = m.get('EntityId')
        if m.get('EntityType') is not None:
            self.entity_type = m.get('EntityType')
        if m.get('ResourceShareId') is not None:
            self.resource_share_id = m.get('ResourceShareId')
        if m.get('ResourceShareName') is not None:
            self.resource_share_name = m.get('ResourceShareName')
        if m.get('TargetProperty') is not None:
            self.target_property = m.get('TargetProperty')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class AssociateResourceShareResponseBody(TeaModel):
    def __init__(self, request_id=None, resource_share_associations=None):
        # The request ID.
        self.request_id = request_id  # type: str
        # The information about the entities that are associated with the resource share.
        self.resource_share_associations = resource_share_associations  # type: list[AssociateResourceShareResponseBodyResourceShareAssociations]

    def validate(self):
        if self.resource_share_associations:
            for k in self.resource_share_associations:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(AssociateResourceShareResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['ResourceShareAssociations'] = []
        if self.resource_share_associations is not None:
            for k in self.resource_share_associations:
                result['ResourceShareAssociations'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.resource_share_associations = []
        if m.get('ResourceShareAssociations') is not None:
            for k in m.get('ResourceShareAssociations'):
                temp_model = AssociateResourceShareResponseBodyResourceShareAssociations()
                self.resource_share_associations.append(temp_model.from_map(k))
        return self


class AssociateResourceShareResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: AssociateResourceShareResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AssociateResourceShareResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = AssociateResourceShareResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AssociateResourceSharePermissionRequest(TeaModel):
    def __init__(self, permission_name=None, replace=None, resource_share_id=None):
        # The name of the permission.
        self.permission_name = permission_name  # type: str
        # Specifies whether to use the specified permission to replace an existing permission. Valid values:
        # 
        # *   false: does not use the specified permission to replace an existing permission. This is the default value. If you set the value to false for a resource share that does not have associated permissions, the system associates the specified permission with the resource share. In a resource share, one resource type can have only one permission. If you set the value to false for a resource share that already has a permission for the resource type indicated by the specified permission, the system reports an error. This prevents you from replacing the existing permission by mistake.
        # *   true: uses the specified permission to replace an existing permission of the same resource type.
        self.replace = replace  # type: bool
        # The ID of the resource share.
        self.resource_share_id = resource_share_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AssociateResourceSharePermissionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.permission_name is not None:
            result['PermissionName'] = self.permission_name
        if self.replace is not None:
            result['Replace'] = self.replace
        if self.resource_share_id is not None:
            result['ResourceShareId'] = self.resource_share_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PermissionName') is not None:
            self.permission_name = m.get('PermissionName')
        if m.get('Replace') is not None:
            self.replace = m.get('Replace')
        if m.get('ResourceShareId') is not None:
            self.resource_share_id = m.get('ResourceShareId')
        return self


class AssociateResourceSharePermissionResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AssociateResourceSharePermissionResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class AssociateResourceSharePermissionResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: AssociateResourceSharePermissionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AssociateResourceSharePermissionResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = AssociateResourceSharePermissionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ChangeResourceGroupRequest(TeaModel):
    def __init__(self, resource_group_id=None, resource_id=None, resource_region_id=None):
        # The ID of the destination resource group.
        self.resource_group_id = resource_group_id  # type: str
        # The ID of the resource share.
        self.resource_id = resource_id  # type: str
        # The region ID of the resource share.
        self.resource_region_id = resource_region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ChangeResourceGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_region_id is not None:
            result['ResourceRegionId'] = self.resource_region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceRegionId') is not None:
            self.resource_region_id = m.get('ResourceRegionId')
        return self


class ChangeResourceGroupResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ChangeResourceGroupResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ChangeResourceGroupResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ChangeResourceGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ChangeResourceGroupResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ChangeResourceGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CheckSharingWithResourceDirectoryStatusResponseBody(TeaModel):
    def __init__(self, enable_sharing_with_rd=None, request_id=None):
        # Indicates whether resource sharing within a resource directory is enabled. Valid values:
        # 
        # *   false
        # *   true
        self.enable_sharing_with_rd = enable_sharing_with_rd  # type: bool
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CheckSharingWithResourceDirectoryStatusResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable_sharing_with_rd is not None:
            result['EnableSharingWithRd'] = self.enable_sharing_with_rd
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EnableSharingWithRd') is not None:
            self.enable_sharing_with_rd = m.get('EnableSharingWithRd')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CheckSharingWithResourceDirectoryStatusResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CheckSharingWithResourceDirectoryStatusResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CheckSharingWithResourceDirectoryStatusResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CheckSharingWithResourceDirectoryStatusResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateResourceShareRequestResources(TeaModel):
    def __init__(self, resource_id=None, resource_type=None):
        # The ID of a shared resource.
        # 
        # Valid values of N: 1 to 5. This indicates that a maximum of five shared resources can be specified at a time.
        # 
        # >  `Resources.N.ResourceId` and `Resources.N.ResourceType` must be used in pairs.
        self.resource_id = resource_id  # type: str
        # The type of a shared resource.
        # 
        # Valid values of N: 1 to 5. This indicates that a maximum of five shared resources can be specified at a time.
        # 
        # For more information about the types of resources that can be shared, see [Services that work with Resource Sharing](~~450526~~).
        # 
        # >  `Resources.N.ResourceId` and `Resources.N.ResourceType` must be used in pairs.
        self.resource_type = resource_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateResourceShareRequestResources, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        return self


class CreateResourceShareRequest(TeaModel):
    def __init__(self, allow_external_targets=None, permission_names=None, resource_share_name=None,
                 resources=None, targets=None):
        # Specifies whether resources in the resource share can be shared with accounts outside the resource directory. Valid values:
        # 
        # *   false (default): Resources in the resource share can be shared only with accounts in the resource directory.
        # *   true: Resources in the resource share can be shared with both accounts in the resource directory and accounts outside the resource directory.
        self.allow_external_targets = allow_external_targets  # type: bool
        # The information about the permissions. If you do not configure this parameter, the system automatically associates the default permission for the specified resource type with the resource share. For more information, see [Permission library](~~465474~~).
        self.permission_names = permission_names  # type: list[str]
        # The name of the resource share.
        # 
        # The name must be 1 to 50 characters in length.
        # 
        # The name can contain letters, digits, periods (.), underscores (\_), and hyphens (-).
        self.resource_share_name = resource_share_name  # type: str
        # The information about the shared resources.
        self.resources = resources  # type: list[CreateResourceShareRequestResources]
        # The information about the principals.
        self.targets = targets  # type: list[str]

    def validate(self):
        if self.resources:
            for k in self.resources:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(CreateResourceShareRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.allow_external_targets is not None:
            result['AllowExternalTargets'] = self.allow_external_targets
        if self.permission_names is not None:
            result['PermissionNames'] = self.permission_names
        if self.resource_share_name is not None:
            result['ResourceShareName'] = self.resource_share_name
        result['Resources'] = []
        if self.resources is not None:
            for k in self.resources:
                result['Resources'].append(k.to_map() if k else None)
        if self.targets is not None:
            result['Targets'] = self.targets
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AllowExternalTargets') is not None:
            self.allow_external_targets = m.get('AllowExternalTargets')
        if m.get('PermissionNames') is not None:
            self.permission_names = m.get('PermissionNames')
        if m.get('ResourceShareName') is not None:
            self.resource_share_name = m.get('ResourceShareName')
        self.resources = []
        if m.get('Resources') is not None:
            for k in m.get('Resources'):
                temp_model = CreateResourceShareRequestResources()
                self.resources.append(temp_model.from_map(k))
        if m.get('Targets') is not None:
            self.targets = m.get('Targets')
        return self


class CreateResourceShareResponseBodyResourceShare(TeaModel):
    def __init__(self, allow_external_targets=None, create_time=None, resource_share_id=None,
                 resource_share_name=None, resource_share_owner=None, resource_share_status=None, update_time=None):
        # Indicates whether resources in the resource share can be shared with accounts outside the resource directory. Valid values:
        # 
        # *   false: Resources in the resource share can be shared only with accounts in the resource directory.
        # *   true: Resources in the resource share can be shared with both accounts in the resource directory and accounts outside the resource directory.
        self.allow_external_targets = allow_external_targets  # type: bool
        # The time when the resource share was created.
        self.create_time = create_time  # type: str
        # The ID of the resource share.
        self.resource_share_id = resource_share_id  # type: str
        # The name of the resource share.
        self.resource_share_name = resource_share_name  # type: str
        # The owner of the resource share.
        self.resource_share_owner = resource_share_owner  # type: str
        # The status of the resource share. Valid values:
        # 
        # *   Active: The resource share is enabled.
        # *   Pending: The resource share is associated with one or more resource sharing invitations that are waiting for confirmation.
        # *   Deleting: The resource share is being deleted.
        # *   Deleted: The resource share is deleted.
        # 
        # >  The system automatically deletes the records of resource shares in the Deleted state within 48 hours to 96 hours after you delete the resource shares.
        self.resource_share_status = resource_share_status  # type: str
        # The time when the resource share was updated.
        self.update_time = update_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateResourceShareResponseBodyResourceShare, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.allow_external_targets is not None:
            result['AllowExternalTargets'] = self.allow_external_targets
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.resource_share_id is not None:
            result['ResourceShareId'] = self.resource_share_id
        if self.resource_share_name is not None:
            result['ResourceShareName'] = self.resource_share_name
        if self.resource_share_owner is not None:
            result['ResourceShareOwner'] = self.resource_share_owner
        if self.resource_share_status is not None:
            result['ResourceShareStatus'] = self.resource_share_status
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AllowExternalTargets') is not None:
            self.allow_external_targets = m.get('AllowExternalTargets')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ResourceShareId') is not None:
            self.resource_share_id = m.get('ResourceShareId')
        if m.get('ResourceShareName') is not None:
            self.resource_share_name = m.get('ResourceShareName')
        if m.get('ResourceShareOwner') is not None:
            self.resource_share_owner = m.get('ResourceShareOwner')
        if m.get('ResourceShareStatus') is not None:
            self.resource_share_status = m.get('ResourceShareStatus')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class CreateResourceShareResponseBody(TeaModel):
    def __init__(self, request_id=None, resource_share=None):
        # The request ID.
        self.request_id = request_id  # type: str
        # The information about the resource share.
        self.resource_share = resource_share  # type: CreateResourceShareResponseBodyResourceShare

    def validate(self):
        if self.resource_share:
            self.resource_share.validate()

    def to_map(self):
        _map = super(CreateResourceShareResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.resource_share is not None:
            result['ResourceShare'] = self.resource_share.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResourceShare') is not None:
            temp_model = CreateResourceShareResponseBodyResourceShare()
            self.resource_share = temp_model.from_map(m['ResourceShare'])
        return self


class CreateResourceShareResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateResourceShareResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateResourceShareResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = CreateResourceShareResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteResourceShareRequest(TeaModel):
    def __init__(self, resource_share_id=None):
        # The ID of the resource share.
        self.resource_share_id = resource_share_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteResourceShareRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_share_id is not None:
            result['ResourceShareId'] = self.resource_share_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ResourceShareId') is not None:
            self.resource_share_id = m.get('ResourceShareId')
        return self


class DeleteResourceShareResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteResourceShareResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DeleteResourceShareResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteResourceShareResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteResourceShareResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DeleteResourceShareResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRegionsRequest(TeaModel):
    def __init__(self, accept_language=None):
        # The supported natural language. Valid values:
        # 
        # *   zh-CN: Chinese
        # *   en-US: English
        self.accept_language = accept_language  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeRegionsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        return self


class DescribeRegionsResponseBodyRegions(TeaModel):
    def __init__(self, local_name=None, region_endpoint=None, region_id=None):
        # The name of the region.
        self.local_name = local_name  # type: str
        # The endpoint of the Resource Sharing service in the region.
        self.region_endpoint = region_endpoint  # type: str
        # The ID of the region.
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeRegionsResponseBodyRegions, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.local_name is not None:
            result['LocalName'] = self.local_name
        if self.region_endpoint is not None:
            result['RegionEndpoint'] = self.region_endpoint
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('LocalName') is not None:
            self.local_name = m.get('LocalName')
        if m.get('RegionEndpoint') is not None:
            self.region_endpoint = m.get('RegionEndpoint')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeRegionsResponseBody(TeaModel):
    def __init__(self, regions=None, request_id=None):
        # The information of the regions.
        self.regions = regions  # type: list[DescribeRegionsResponseBodyRegions]
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.regions:
            for k in self.regions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeRegionsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Regions'] = []
        if self.regions is not None:
            for k in self.regions:
                result['Regions'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.regions = []
        if m.get('Regions') is not None:
            for k in m.get('Regions'):
                temp_model = DescribeRegionsResponseBodyRegions()
                self.regions.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeRegionsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeRegionsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeRegionsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DescribeRegionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DisassociateResourceShareRequestResources(TeaModel):
    def __init__(self, resource_id=None, resource_type=None):
        # The ID of a shared resource.
        # 
        # Valid values of N: 1 to 5. This indicates that a maximum of five shared resources can be specified at a time.
        # 
        # >  Resources.N.ResourceId and Resources.N.ResourceType must be used in pairs.
        self.resource_id = resource_id  # type: str
        # The type of a shared resource.
        # 
        # Valid values of N: 1 to 5. This indicates that a maximum of five shared resources can be specified at a time.
        # 
        # For more information about the types of resources that can be shared, see [Services that work with Resource Sharing](~~450526~~).
        # 
        # >  Resources.N.ResourceId and Resources.N.ResourceType must be used in pairs.
        self.resource_type = resource_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DisassociateResourceShareRequestResources, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        return self


class DisassociateResourceShareRequest(TeaModel):
    def __init__(self, resource_owner=None, resource_share_id=None, resources=None, targets=None):
        # The owner of the resource share. Valid values:
        # 
        # *   Self: The resource share belongs to the current account. This is the default value. If you are the management account or a member of a resource directory and you want to remove resources or principals from a resource share, set this parameter to Self.
        # *   OtherAccounts: The resource share belongs to another account. If you are not the management account or a member of a resource directory and you want to exit a resource share, set this parameter to OtherAccounts.
        self.resource_owner = resource_owner  # type: str
        # The ID of the resource share.
        self.resource_share_id = resource_share_id  # type: str
        # The shared resource.
        self.resources = resources  # type: list[DisassociateResourceShareRequestResources]
        # The ID of a principal.
        self.targets = targets  # type: list[str]

    def validate(self):
        if self.resources:
            for k in self.resources:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DisassociateResourceShareRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_owner is not None:
            result['ResourceOwner'] = self.resource_owner
        if self.resource_share_id is not None:
            result['ResourceShareId'] = self.resource_share_id
        result['Resources'] = []
        if self.resources is not None:
            for k in self.resources:
                result['Resources'].append(k.to_map() if k else None)
        if self.targets is not None:
            result['Targets'] = self.targets
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ResourceOwner') is not None:
            self.resource_owner = m.get('ResourceOwner')
        if m.get('ResourceShareId') is not None:
            self.resource_share_id = m.get('ResourceShareId')
        self.resources = []
        if m.get('Resources') is not None:
            for k in m.get('Resources'):
                temp_model = DisassociateResourceShareRequestResources()
                self.resources.append(temp_model.from_map(k))
        if m.get('Targets') is not None:
            self.targets = m.get('Targets')
        return self


class DisassociateResourceShareResponseBodyResourceShareAssociations(TeaModel):
    def __init__(self, association_status=None, association_status_message=None, association_type=None,
                 create_time=None, entity_id=None, entity_type=None, resource_share_id=None, resource_share_name=None,
                 target_property=None, update_time=None):
        # The association status. Valid values:
        # 
        # *   Associating: The entity is being associated.
        # *   Associated: The entity is associated.
        # *   Failed: The entity fails to be associated.
        # *   Disassociating: The entity is being disassociated.
        # *   Disassociated: The entity is disassociated.
        # 
        # >  The system deletes the records of entities in the `Failed` or `Disassociated` state within 48 hours to 96 hours.
        self.association_status = association_status  # type: str
        # The cause of the disassociation failure.
        self.association_status_message = association_status_message  # type: str
        # The association type. Valid values:
        # 
        # *   Resource
        # *   Target
        self.association_type = association_type  # type: str
        # The time when the disassociation of the entity was performed. The value of this parameter depends on the value of the AssociationType parameter:
        # 
        # *   If the value of `AssociationType` is `Resource`, the value of this parameter is the time when the resource was disassociated from the resource share.
        # *   If the value of `AssociationType` is `Target`, the value of this parameter is the time when the principal was disassociated from the resource share.
        self.create_time = create_time  # type: str
        # The ID of the entity. The value of this parameter depends on the value of the AssociationType parameter:
        # 
        # *   If the value of `AssociationType` is `Resource`, the value of this parameter is the ID of the resource.
        # *   If the value of `AssociationType` is `Target`, the value of this parameter is the ID of the resource directory, folder, or member.
        self.entity_id = entity_id  # type: str
        # The type of the entity. The value of this parameter depends on the value of the AssociationType parameter:
        # 
        # *   If the value of AssociationType is Resource, the value of this parameter is the type of the resource. For more information about the types of resources that can be shared, see [Services that work with Resource Sharing](~~450526~~).
        # *   If the value of AssociationType is Target, the value of this parameter is Account.
        self.entity_type = entity_type  # type: str
        # The ID of the resource share.
        self.resource_share_id = resource_share_id  # type: str
        # The name of the resource share.
        self.resource_share_name = resource_share_name  # type: str
        self.target_property = target_property  # type: str
        # The time when the disassociation of the entity was updated. The value of this parameter depends on the value of the AssociationType parameter:
        # 
        # *   If the value of `AssociationType` is `Resource`, the value of this parameter is the time when the disassociation of the resource was updated.
        # *   If the value of `AssociationType` is `Target`, the value of this parameter is the time when the disassociation of the principal was updated.
        self.update_time = update_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DisassociateResourceShareResponseBodyResourceShareAssociations, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.association_status is not None:
            result['AssociationStatus'] = self.association_status
        if self.association_status_message is not None:
            result['AssociationStatusMessage'] = self.association_status_message
        if self.association_type is not None:
            result['AssociationType'] = self.association_type
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.entity_id is not None:
            result['EntityId'] = self.entity_id
        if self.entity_type is not None:
            result['EntityType'] = self.entity_type
        if self.resource_share_id is not None:
            result['ResourceShareId'] = self.resource_share_id
        if self.resource_share_name is not None:
            result['ResourceShareName'] = self.resource_share_name
        if self.target_property is not None:
            result['TargetProperty'] = self.target_property
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AssociationStatus') is not None:
            self.association_status = m.get('AssociationStatus')
        if m.get('AssociationStatusMessage') is not None:
            self.association_status_message = m.get('AssociationStatusMessage')
        if m.get('AssociationType') is not None:
            self.association_type = m.get('AssociationType')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('EntityId') is not None:
            self.entity_id = m.get('EntityId')
        if m.get('EntityType') is not None:
            self.entity_type = m.get('EntityType')
        if m.get('ResourceShareId') is not None:
            self.resource_share_id = m.get('ResourceShareId')
        if m.get('ResourceShareName') is not None:
            self.resource_share_name = m.get('ResourceShareName')
        if m.get('TargetProperty') is not None:
            self.target_property = m.get('TargetProperty')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class DisassociateResourceShareResponseBody(TeaModel):
    def __init__(self, request_id=None, resource_share_associations=None):
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The information of the entities that are associated with the resource share.
        self.resource_share_associations = resource_share_associations  # type: list[DisassociateResourceShareResponseBodyResourceShareAssociations]

    def validate(self):
        if self.resource_share_associations:
            for k in self.resource_share_associations:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DisassociateResourceShareResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['ResourceShareAssociations'] = []
        if self.resource_share_associations is not None:
            for k in self.resource_share_associations:
                result['ResourceShareAssociations'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.resource_share_associations = []
        if m.get('ResourceShareAssociations') is not None:
            for k in m.get('ResourceShareAssociations'):
                temp_model = DisassociateResourceShareResponseBodyResourceShareAssociations()
                self.resource_share_associations.append(temp_model.from_map(k))
        return self


class DisassociateResourceShareResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DisassociateResourceShareResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DisassociateResourceShareResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DisassociateResourceShareResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DisassociateResourceSharePermissionRequest(TeaModel):
    def __init__(self, permission_name=None, resource_share_id=None):
        # The name of the permission. For more information, see [Permission library](~~465474~~).
        self.permission_name = permission_name  # type: str
        # The ID of the resource share.
        self.resource_share_id = resource_share_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DisassociateResourceSharePermissionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.permission_name is not None:
            result['PermissionName'] = self.permission_name
        if self.resource_share_id is not None:
            result['ResourceShareId'] = self.resource_share_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PermissionName') is not None:
            self.permission_name = m.get('PermissionName')
        if m.get('ResourceShareId') is not None:
            self.resource_share_id = m.get('ResourceShareId')
        return self


class DisassociateResourceSharePermissionResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DisassociateResourceSharePermissionResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DisassociateResourceSharePermissionResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DisassociateResourceSharePermissionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DisassociateResourceSharePermissionResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = DisassociateResourceSharePermissionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EnableSharingWithResourceDirectoryResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(EnableSharingWithResourceDirectoryResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class EnableSharingWithResourceDirectoryResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: EnableSharingWithResourceDirectoryResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(EnableSharingWithResourceDirectoryResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = EnableSharingWithResourceDirectoryResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetPermissionRequest(TeaModel):
    def __init__(self, permission_name=None, permission_version=None):
        # The name of the permission.
        self.permission_name = permission_name  # type: str
        # The version of the permission.
        self.permission_version = permission_version  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetPermissionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.permission_name is not None:
            result['PermissionName'] = self.permission_name
        if self.permission_version is not None:
            result['PermissionVersion'] = self.permission_version
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PermissionName') is not None:
            self.permission_name = m.get('PermissionName')
        if m.get('PermissionVersion') is not None:
            self.permission_version = m.get('PermissionVersion')
        return self


class GetPermissionResponseBodyPermission(TeaModel):
    def __init__(self, create_time=None, default_permission=None, default_version=None, permission=None,
                 permission_name=None, permission_version=None, resource_type=None, update_time=None):
        # The creation time.
        self.create_time = create_time  # type: str
        # Indicates whether the permission is the default permission. Valid values:
        # 
        # *   false: The permission is not the default permission.
        # *   true: The permission is the default permission.
        self.default_permission = default_permission  # type: bool
        # Indicates whether the version is the default version. Valid values:
        # 
        # *   false: The version is not the default version.
        # *   true: The version is the default version.
        self.default_version = default_version  # type: bool
        # The document of the policy related to the permission.
        self.permission = permission  # type: str
        # The name of the permission.
        self.permission_name = permission_name  # type: str
        # The version of the permission.
        self.permission_version = permission_version  # type: str
        # The type of the shared resources.
        # 
        # For more information about the types of resources that can be shared, see [Services that work with Resource Sharing](~~450526~~).
        self.resource_type = resource_type  # type: str
        # The update time.
        self.update_time = update_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetPermissionResponseBodyPermission, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.default_permission is not None:
            result['DefaultPermission'] = self.default_permission
        if self.default_version is not None:
            result['DefaultVersion'] = self.default_version
        if self.permission is not None:
            result['Permission'] = self.permission
        if self.permission_name is not None:
            result['PermissionName'] = self.permission_name
        if self.permission_version is not None:
            result['PermissionVersion'] = self.permission_version
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DefaultPermission') is not None:
            self.default_permission = m.get('DefaultPermission')
        if m.get('DefaultVersion') is not None:
            self.default_version = m.get('DefaultVersion')
        if m.get('Permission') is not None:
            self.permission = m.get('Permission')
        if m.get('PermissionName') is not None:
            self.permission_name = m.get('PermissionName')
        if m.get('PermissionVersion') is not None:
            self.permission_version = m.get('PermissionVersion')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class GetPermissionResponseBody(TeaModel):
    def __init__(self, permission=None, request_id=None):
        # The information about the permission.
        self.permission = permission  # type: GetPermissionResponseBodyPermission
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.permission:
            self.permission.validate()

    def to_map(self):
        _map = super(GetPermissionResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.permission is not None:
            result['Permission'] = self.permission.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Permission') is not None:
            temp_model = GetPermissionResponseBodyPermission()
            self.permission = temp_model.from_map(m['Permission'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetPermissionResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetPermissionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetPermissionResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = GetPermissionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListPermissionVersionsRequest(TeaModel):
    def __init__(self, max_results=None, next_token=None, permission_name=None):
        # The maximum number of entries to return for a single request.
        # 
        # Valid values: 1 to 100. Default value: 20.
        self.max_results = max_results  # type: int
        # The `token` that is used to initiate the next request. If the response of the current request is truncated, you can use the token to initiate another request and obtain the remaining records.
        self.next_token = next_token  # type: str
        # The name of the permission.
        self.permission_name = permission_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListPermissionVersionsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.permission_name is not None:
            result['PermissionName'] = self.permission_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('PermissionName') is not None:
            self.permission_name = m.get('PermissionName')
        return self


class ListPermissionVersionsResponseBodyPermissions(TeaModel):
    def __init__(self, create_time=None, default_permission=None, default_version=None, permission_name=None,
                 permission_version=None, resource_type=None, update_time=None):
        # The creation time.
        self.create_time = create_time  # type: str
        # Indicates whether the permission is the default permission. Valid values:
        # 
        # *   false: The permission is not the default permission.
        # *   true: The permission is the default permission.
        self.default_permission = default_permission  # type: bool
        # Indicates whether the version is the default version. Valid values:
        # 
        # *   false: The version is not the default version.
        # *   true: The version is the default version.
        self.default_version = default_version  # type: bool
        # The name of the permission.
        self.permission_name = permission_name  # type: str
        # The version of the permission.
        self.permission_version = permission_version  # type: str
        # The type of the shared resources.
        # 
        # For more information about the types of resources that can be shared, see [Services that work with Resource Sharing](~~450526~~).
        self.resource_type = resource_type  # type: str
        # The update time.
        self.update_time = update_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListPermissionVersionsResponseBodyPermissions, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.default_permission is not None:
            result['DefaultPermission'] = self.default_permission
        if self.default_version is not None:
            result['DefaultVersion'] = self.default_version
        if self.permission_name is not None:
            result['PermissionName'] = self.permission_name
        if self.permission_version is not None:
            result['PermissionVersion'] = self.permission_version
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DefaultPermission') is not None:
            self.default_permission = m.get('DefaultPermission')
        if m.get('DefaultVersion') is not None:
            self.default_version = m.get('DefaultVersion')
        if m.get('PermissionName') is not None:
            self.permission_name = m.get('PermissionName')
        if m.get('PermissionVersion') is not None:
            self.permission_version = m.get('PermissionVersion')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class ListPermissionVersionsResponseBody(TeaModel):
    def __init__(self, next_token=None, permissions=None, request_id=None):
        # The token that is used to initiate the next request. If the response of the current request is truncated, you can use the token to initiate another request and obtain the remaining records.
        self.next_token = next_token  # type: str
        # The information about the permission.
        self.permissions = permissions  # type: list[ListPermissionVersionsResponseBodyPermissions]
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.permissions:
            for k in self.permissions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListPermissionVersionsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        result['Permissions'] = []
        if self.permissions is not None:
            for k in self.permissions:
                result['Permissions'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        self.permissions = []
        if m.get('Permissions') is not None:
            for k in m.get('Permissions'):
                temp_model = ListPermissionVersionsResponseBodyPermissions()
                self.permissions.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListPermissionVersionsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListPermissionVersionsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListPermissionVersionsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListPermissionVersionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListPermissionsRequest(TeaModel):
    def __init__(self, max_results=None, next_token=None, resource_type=None):
        # The maximum number of entries to return for a single request.
        # 
        # Valid values: 1 to 100. Default value: 20.
        self.max_results = max_results  # type: int
        # The `token` that is used to initiate the next request. If the response of the current request is truncated, you can use the token to initiate another request and obtain the remaining records.
        self.next_token = next_token  # type: str
        # The type of the shared resources.
        # 
        # For more information about the types of resources that can be shared, see [Services that work with Resource Sharing](~~450526~~).
        self.resource_type = resource_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListPermissionsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        return self


class ListPermissionsResponseBodyPermissions(TeaModel):
    def __init__(self, create_time=None, default_permission=None, default_version=None, permission_name=None,
                 permission_version=None, resource_type=None, update_time=None):
        # The creation time.
        self.create_time = create_time  # type: str
        # Indicates whether the permission is the default permission. Valid values:
        # 
        # *   false: The permission is not the default permission.
        # *   true: The permission is the default permission.
        self.default_permission = default_permission  # type: bool
        # Indicates whether the version is the default version. Valid values:
        # 
        # *   false: The version is not the default version.
        # *   true: The version is the default version.
        self.default_version = default_version  # type: bool
        # The name of the permission.
        self.permission_name = permission_name  # type: str
        # The version of the permission.
        self.permission_version = permission_version  # type: str
        # The type of the shared resources.
        # 
        # For more information about the types of resources that can be shared, see [Services that work with Resource Sharing](~~450526~~).
        self.resource_type = resource_type  # type: str
        # The update time.
        self.update_time = update_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListPermissionsResponseBodyPermissions, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.default_permission is not None:
            result['DefaultPermission'] = self.default_permission
        if self.default_version is not None:
            result['DefaultVersion'] = self.default_version
        if self.permission_name is not None:
            result['PermissionName'] = self.permission_name
        if self.permission_version is not None:
            result['PermissionVersion'] = self.permission_version
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DefaultPermission') is not None:
            self.default_permission = m.get('DefaultPermission')
        if m.get('DefaultVersion') is not None:
            self.default_version = m.get('DefaultVersion')
        if m.get('PermissionName') is not None:
            self.permission_name = m.get('PermissionName')
        if m.get('PermissionVersion') is not None:
            self.permission_version = m.get('PermissionVersion')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class ListPermissionsResponseBody(TeaModel):
    def __init__(self, next_token=None, permissions=None, request_id=None):
        # The token that is used to initiate the next request. If the response of the current request is truncated, you can use the token to initiate another request and obtain the remaining records.
        self.next_token = next_token  # type: str
        # The information about the permission.
        self.permissions = permissions  # type: list[ListPermissionsResponseBodyPermissions]
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.permissions:
            for k in self.permissions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListPermissionsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        result['Permissions'] = []
        if self.permissions is not None:
            for k in self.permissions:
                result['Permissions'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        self.permissions = []
        if m.get('Permissions') is not None:
            for k in m.get('Permissions'):
                temp_model = ListPermissionsResponseBodyPermissions()
                self.permissions.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListPermissionsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListPermissionsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListPermissionsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListPermissionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListResourceShareAssociationsRequest(TeaModel):
    def __init__(self, association_status=None, association_type=None, max_results=None, next_token=None,
                 resource_id=None, resource_share_ids=None, target=None):
        # The association status. Valid values:
        # 
        # *   Associating: The entity is being associated.
        # *   Associated: The entity is associated.
        # *   Failed: The entity fails to be associated.
        # *   Disassociating: The entity is being disassociated.
        # *   Disassociated: The entity is disassociated.
        # 
        # >  The system deletes the records of entities in the `Failed` or `Disassociated` state within 48 hours to 96 hours.
        self.association_status = association_status  # type: str
        # The association type. Valid values:
        # 
        # *   Resource
        # *   Target
        self.association_type = association_type  # type: str
        # The maximum number of entries to return for a single request.
        # 
        # Valid values: 1 to 100. Default value: 20.
        self.max_results = max_results  # type: int
        # The `token` that is used to initiate the next request. If the response of the current request is truncated, you can use the token to initiate another request and obtain the remaining records.
        self.next_token = next_token  # type: str
        # The ID of the resource.
        # 
        # >  This parameter is unavailable if you set the `AssociationType` parameter to `Target`.
        self.resource_id = resource_id  # type: str
        # The IDs of the resource shares.
        self.resource_share_ids = resource_share_ids  # type: list[str]
        # The ID of the principal.
        # 
        # >  This parameter is unavailable if you set the `AssociationType` parameter to `Resource`.
        self.target = target  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListResourceShareAssociationsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.association_status is not None:
            result['AssociationStatus'] = self.association_status
        if self.association_type is not None:
            result['AssociationType'] = self.association_type
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_share_ids is not None:
            result['ResourceShareIds'] = self.resource_share_ids
        if self.target is not None:
            result['Target'] = self.target
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AssociationStatus') is not None:
            self.association_status = m.get('AssociationStatus')
        if m.get('AssociationType') is not None:
            self.association_type = m.get('AssociationType')
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceShareIds') is not None:
            self.resource_share_ids = m.get('ResourceShareIds')
        if m.get('Target') is not None:
            self.target = m.get('Target')
        return self


class ListResourceShareAssociationsResponseBodyResourceShareAssociationsAssociationFailedDetails(TeaModel):
    def __init__(self, associate_type=None, entity_id=None, entity_type=None, status=None, status_message=None):
        self.associate_type = associate_type  # type: str
        self.entity_id = entity_id  # type: str
        self.entity_type = entity_type  # type: str
        self.status = status  # type: str
        self.status_message = status_message  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListResourceShareAssociationsResponseBodyResourceShareAssociationsAssociationFailedDetails, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.associate_type is not None:
            result['AssociateType'] = self.associate_type
        if self.entity_id is not None:
            result['EntityId'] = self.entity_id
        if self.entity_type is not None:
            result['EntityType'] = self.entity_type
        if self.status is not None:
            result['Status'] = self.status
        if self.status_message is not None:
            result['StatusMessage'] = self.status_message
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AssociateType') is not None:
            self.associate_type = m.get('AssociateType')
        if m.get('EntityId') is not None:
            self.entity_id = m.get('EntityId')
        if m.get('EntityType') is not None:
            self.entity_type = m.get('EntityType')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('StatusMessage') is not None:
            self.status_message = m.get('StatusMessage')
        return self


class ListResourceShareAssociationsResponseBodyResourceShareAssociations(TeaModel):
    def __init__(self, association_failed_details=None, association_status=None, association_status_message=None,
                 association_type=None, create_time=None, entity_id=None, entity_type=None, external=None, resource_share_id=None,
                 resource_share_name=None, target_property=None, update_time=None):
        self.association_failed_details = association_failed_details  # type: list[ListResourceShareAssociationsResponseBodyResourceShareAssociationsAssociationFailedDetails]
        # The association status. Valid values:
        # 
        # *   Associating: The entity is being associated.
        # *   Associated: The entity is associated.
        # *   Failed: The entity fails to be associated.
        # *   Disassociating: The entity is being disassociated.
        # *   Disassociated: The entity is disassociated.
        # 
        # >  The system deletes the records of entities in the `Failed` or `Disassociated` state within 48 hours to 96 hours.
        self.association_status = association_status  # type: str
        # The cause of the association failure.
        self.association_status_message = association_status_message  # type: str
        # The association type. Valid values:
        # 
        # *   Resource
        # *   Target
        self.association_type = association_type  # type: str
        # The time when the association of the entity was created. The value of this parameter depends on the value of the AssociationType parameter:
        # 
        # *   If the value of `AssociationType` is `Resource`, the value of this parameter is the time when the shared resource was associated with or disassociated from the resource share.
        # *   If the value of `AssociationType` is `Target`, the value of this parameter is the time when the principal was associated with or disassociated from the resource share.
        self.create_time = create_time  # type: str
        # The ID of the entity. The value of this parameter depends on the value of the AssociationType parameter:
        # 
        # *   If the value of `AssociationType` is `Resource`, the value of this parameter is the ID of the shared resource.
        # *   If the value of `AssociationType` is `Target`, the value of this parameter is the ID of the principal.
        self.entity_id = entity_id  # type: str
        # The type of the entity. The value of this parameter depends on the value of the AssociationType parameter:
        # 
        # *   If the value of AssociationType is Resource, the value of this parameter is the type of the resource. For more information about the types of resources that can be shared, see [Services that work with Resource Sharing](~~450526~~).
        # *   If the value of AssociationType is Target, the value of this parameter is `Account`.
        self.entity_type = entity_type  # type: str
        # Indicates whether the principal is outside the resource directory. Valid values:
        # 
        # *   true: The principal is outside the resource directory.
        # *   false: The principal is in the resource directory.
        self.external = external  # type: bool
        # The ID of the resource share.
        self.resource_share_id = resource_share_id  # type: str
        # The name of the resource share.
        self.resource_share_name = resource_share_name  # type: str
        self.target_property = target_property  # type: str
        # The time when the association of the entity was updated. The value of this parameter depends on the value of the AssociationType parameter:
        # 
        # *   If the value of `AssociationType` is `Resource`, the value of this parameter is the time when the association of the shared resource was updated.
        # *   If the value of `AssociationType` is `Target`, the value of this parameter is the time when the association of the principal was updated.
        self.update_time = update_time  # type: str

    def validate(self):
        if self.association_failed_details:
            for k in self.association_failed_details:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListResourceShareAssociationsResponseBodyResourceShareAssociations, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['AssociationFailedDetails'] = []
        if self.association_failed_details is not None:
            for k in self.association_failed_details:
                result['AssociationFailedDetails'].append(k.to_map() if k else None)
        if self.association_status is not None:
            result['AssociationStatus'] = self.association_status
        if self.association_status_message is not None:
            result['AssociationStatusMessage'] = self.association_status_message
        if self.association_type is not None:
            result['AssociationType'] = self.association_type
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.entity_id is not None:
            result['EntityId'] = self.entity_id
        if self.entity_type is not None:
            result['EntityType'] = self.entity_type
        if self.external is not None:
            result['External'] = self.external
        if self.resource_share_id is not None:
            result['ResourceShareId'] = self.resource_share_id
        if self.resource_share_name is not None:
            result['ResourceShareName'] = self.resource_share_name
        if self.target_property is not None:
            result['TargetProperty'] = self.target_property
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.association_failed_details = []
        if m.get('AssociationFailedDetails') is not None:
            for k in m.get('AssociationFailedDetails'):
                temp_model = ListResourceShareAssociationsResponseBodyResourceShareAssociationsAssociationFailedDetails()
                self.association_failed_details.append(temp_model.from_map(k))
        if m.get('AssociationStatus') is not None:
            self.association_status = m.get('AssociationStatus')
        if m.get('AssociationStatusMessage') is not None:
            self.association_status_message = m.get('AssociationStatusMessage')
        if m.get('AssociationType') is not None:
            self.association_type = m.get('AssociationType')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('EntityId') is not None:
            self.entity_id = m.get('EntityId')
        if m.get('EntityType') is not None:
            self.entity_type = m.get('EntityType')
        if m.get('External') is not None:
            self.external = m.get('External')
        if m.get('ResourceShareId') is not None:
            self.resource_share_id = m.get('ResourceShareId')
        if m.get('ResourceShareName') is not None:
            self.resource_share_name = m.get('ResourceShareName')
        if m.get('TargetProperty') is not None:
            self.target_property = m.get('TargetProperty')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class ListResourceShareAssociationsResponseBody(TeaModel):
    def __init__(self, next_token=None, request_id=None, resource_share_associations=None):
        # The `token` that is used to initiate the next request. If the response of the current request is truncated, you can use the token to initiate another request and obtain the remaining records.
        self.next_token = next_token  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The information of the entities.
        self.resource_share_associations = resource_share_associations  # type: list[ListResourceShareAssociationsResponseBodyResourceShareAssociations]

    def validate(self):
        if self.resource_share_associations:
            for k in self.resource_share_associations:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListResourceShareAssociationsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['ResourceShareAssociations'] = []
        if self.resource_share_associations is not None:
            for k in self.resource_share_associations:
                result['ResourceShareAssociations'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.resource_share_associations = []
        if m.get('ResourceShareAssociations') is not None:
            for k in m.get('ResourceShareAssociations'):
                temp_model = ListResourceShareAssociationsResponseBodyResourceShareAssociations()
                self.resource_share_associations.append(temp_model.from_map(k))
        return self


class ListResourceShareAssociationsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListResourceShareAssociationsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListResourceShareAssociationsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListResourceShareAssociationsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListResourceShareInvitationsRequest(TeaModel):
    def __init__(self, max_results=None, next_token=None, resource_share_ids=None,
                 resource_share_invitation_ids=None):
        # The maximum number of entries to return for a single request.
        # 
        # Valid values: 1 to 100. Default value: 20.
        self.max_results = max_results  # type: int
        # The pagination token that is used in the next request to retrieve a new page of results. You do not need to specify this parameter for the first request. You must specify the token that is obtained from the previous query as the value of `NextToken`.
        self.next_token = next_token  # type: str
        # The IDs of the resource shares.
        self.resource_share_ids = resource_share_ids  # type: list[str]
        # The IDs of the resource sharing invitations.
        self.resource_share_invitation_ids = resource_share_invitation_ids  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListResourceShareInvitationsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.resource_share_ids is not None:
            result['ResourceShareIds'] = self.resource_share_ids
        if self.resource_share_invitation_ids is not None:
            result['ResourceShareInvitationIds'] = self.resource_share_invitation_ids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('ResourceShareIds') is not None:
            self.resource_share_ids = m.get('ResourceShareIds')
        if m.get('ResourceShareInvitationIds') is not None:
            self.resource_share_invitation_ids = m.get('ResourceShareInvitationIds')
        return self


class ListResourceShareInvitationsResponseBodyResourceShareInvitationsInvitationFailedDetails(TeaModel):
    def __init__(self, associate_type=None, resource_id=None, resource_type=None, status=None, status_message=None):
        # The type of the sharing operation. Valid values:
        # 
        # *   Associate
        # *   Disassociate
        self.associate_type = associate_type  # type: str
        # The ID of the shared resource.
        self.resource_id = resource_id  # type: str
        # The type of the shared resource.
        # 
        # For more information about the types of resources that can be shared, see [Services that work with Resource Sharing](~~450526~~).
        self.resource_type = resource_type  # type: str
        # The failure status. Valid values:
        # 
        # *   Unavailable: The resource cannot be shared.
        # *   LimitExceeded: The number of shared resources within the Alibaba Cloud account exceeds the upper limit.
        # *   ZonalResourceInaccessible: The resource is unavailable in this region.
        # *   UnsupportedOperation: The operation is not allowed because another association exists.
        # *   InternalError: An internal error occurred during the check.
        self.status = status  # type: str
        # The failure cause.
        self.status_message = status_message  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListResourceShareInvitationsResponseBodyResourceShareInvitationsInvitationFailedDetails, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.associate_type is not None:
            result['AssociateType'] = self.associate_type
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.status is not None:
            result['Status'] = self.status
        if self.status_message is not None:
            result['StatusMessage'] = self.status_message
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AssociateType') is not None:
            self.associate_type = m.get('AssociateType')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        if m.get('StatusMessage') is not None:
            self.status_message = m.get('StatusMessage')
        return self


class ListResourceShareInvitationsResponseBodyResourceShareInvitations(TeaModel):
    def __init__(self, create_time=None, invitation_failed_details=None, receiver_account_id=None,
                 resource_share_id=None, resource_share_invitation_id=None, resource_share_name=None, sender_account_id=None,
                 status=None):
        # The time when the invitation was created. The time is displayed in UTC.
        self.create_time = create_time  # type: str
        # The information about the failure.
        self.invitation_failed_details = invitation_failed_details  # type: list[ListResourceShareInvitationsResponseBodyResourceShareInvitationsInvitationFailedDetails]
        # The Alibaba Cloud account ID of the invitee.
        self.receiver_account_id = receiver_account_id  # type: str
        # The ID of the resource share.
        self.resource_share_id = resource_share_id  # type: str
        # The ID of the invitation.
        self.resource_share_invitation_id = resource_share_invitation_id  # type: str
        # The name of the resource share.
        self.resource_share_name = resource_share_name  # type: str
        # The Alibaba Cloud account ID of the inviter.
        self.sender_account_id = sender_account_id  # type: str
        # The status of the invitation. Valid values:
        # 
        # *   Pending
        # *   Accepted
        # *   Cancelled
        # *   Rejected
        # *   Expired
        # *   AcceptFailed
        self.status = status  # type: str

    def validate(self):
        if self.invitation_failed_details:
            for k in self.invitation_failed_details:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListResourceShareInvitationsResponseBodyResourceShareInvitations, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        result['InvitationFailedDetails'] = []
        if self.invitation_failed_details is not None:
            for k in self.invitation_failed_details:
                result['InvitationFailedDetails'].append(k.to_map() if k else None)
        if self.receiver_account_id is not None:
            result['ReceiverAccountId'] = self.receiver_account_id
        if self.resource_share_id is not None:
            result['ResourceShareId'] = self.resource_share_id
        if self.resource_share_invitation_id is not None:
            result['ResourceShareInvitationId'] = self.resource_share_invitation_id
        if self.resource_share_name is not None:
            result['ResourceShareName'] = self.resource_share_name
        if self.sender_account_id is not None:
            result['SenderAccountId'] = self.sender_account_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        self.invitation_failed_details = []
        if m.get('InvitationFailedDetails') is not None:
            for k in m.get('InvitationFailedDetails'):
                temp_model = ListResourceShareInvitationsResponseBodyResourceShareInvitationsInvitationFailedDetails()
                self.invitation_failed_details.append(temp_model.from_map(k))
        if m.get('ReceiverAccountId') is not None:
            self.receiver_account_id = m.get('ReceiverAccountId')
        if m.get('ResourceShareId') is not None:
            self.resource_share_id = m.get('ResourceShareId')
        if m.get('ResourceShareInvitationId') is not None:
            self.resource_share_invitation_id = m.get('ResourceShareInvitationId')
        if m.get('ResourceShareName') is not None:
            self.resource_share_name = m.get('ResourceShareName')
        if m.get('SenderAccountId') is not None:
            self.sender_account_id = m.get('SenderAccountId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class ListResourceShareInvitationsResponseBody(TeaModel):
    def __init__(self, next_token=None, request_id=None, resource_share_invitations=None):
        # The pagination token that is used in the next request to retrieve a new page of results. You do not need to specify this parameter for the first request. You must specify the token that is obtained from the previous query as the value of `NextToken`.
        self.next_token = next_token  # type: str
        # The request ID.
        self.request_id = request_id  # type: str
        # The information about the resource sharing invitations.
        self.resource_share_invitations = resource_share_invitations  # type: list[ListResourceShareInvitationsResponseBodyResourceShareInvitations]

    def validate(self):
        if self.resource_share_invitations:
            for k in self.resource_share_invitations:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListResourceShareInvitationsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['ResourceShareInvitations'] = []
        if self.resource_share_invitations is not None:
            for k in self.resource_share_invitations:
                result['ResourceShareInvitations'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.resource_share_invitations = []
        if m.get('ResourceShareInvitations') is not None:
            for k in m.get('ResourceShareInvitations'):
                temp_model = ListResourceShareInvitationsResponseBodyResourceShareInvitations()
                self.resource_share_invitations.append(temp_model.from_map(k))
        return self


class ListResourceShareInvitationsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListResourceShareInvitationsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListResourceShareInvitationsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListResourceShareInvitationsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListResourceSharePermissionsRequest(TeaModel):
    def __init__(self, max_results=None, next_token=None, resource_owner=None, resource_share_id=None):
        # The maximum number of entries to return for a single request.
        # 
        # Valid values: 1 to 100. Default value: 20.
        self.max_results = max_results  # type: int
        # The `token` that is used to initiate the next request. If the response of the current request is truncated, you can use the token to initiate another request and obtain the remaining records.
        self.next_token = next_token  # type: str
        # The owner of the resource share. Valid values:
        # 
        # *   Self: the current account
        # *   OtherAccounts: an account other than the current account
        self.resource_owner = resource_owner  # type: str
        # The ID of the resource share.
        self.resource_share_id = resource_share_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListResourceSharePermissionsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.resource_owner is not None:
            result['ResourceOwner'] = self.resource_owner
        if self.resource_share_id is not None:
            result['ResourceShareId'] = self.resource_share_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('ResourceOwner') is not None:
            self.resource_owner = m.get('ResourceOwner')
        if m.get('ResourceShareId') is not None:
            self.resource_share_id = m.get('ResourceShareId')
        return self


class ListResourceSharePermissionsResponseBodyPermissions(TeaModel):
    def __init__(self, create_time=None, default_permission=None, default_version=None, permission_name=None,
                 permission_version=None, resource_type=None, update_time=None):
        # The creation time.
        self.create_time = create_time  # type: str
        # Indicates whether the permission is the default permission. Valid values:
        # 
        # *   false: The permission is not the default permission.
        # *   true: The permission is the default permission.
        self.default_permission = default_permission  # type: bool
        # Indicates whether the version is the default version. Valid values:
        # 
        # *   false: The version is not the default version.
        # *   true: The version is the default version.
        self.default_version = default_version  # type: bool
        # The name of the permission.
        self.permission_name = permission_name  # type: str
        # The version of the permission.
        self.permission_version = permission_version  # type: str
        # The type of the shared resources.
        # 
        # For more information about the types of resources that can be shared, see [Services that work with Resource Sharing](~~450526~~).
        self.resource_type = resource_type  # type: str
        # The update time.
        self.update_time = update_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListResourceSharePermissionsResponseBodyPermissions, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.default_permission is not None:
            result['DefaultPermission'] = self.default_permission
        if self.default_version is not None:
            result['DefaultVersion'] = self.default_version
        if self.permission_name is not None:
            result['PermissionName'] = self.permission_name
        if self.permission_version is not None:
            result['PermissionVersion'] = self.permission_version
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('DefaultPermission') is not None:
            self.default_permission = m.get('DefaultPermission')
        if m.get('DefaultVersion') is not None:
            self.default_version = m.get('DefaultVersion')
        if m.get('PermissionName') is not None:
            self.permission_name = m.get('PermissionName')
        if m.get('PermissionVersion') is not None:
            self.permission_version = m.get('PermissionVersion')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class ListResourceSharePermissionsResponseBody(TeaModel):
    def __init__(self, next_token=None, permissions=None, request_id=None):
        # The `token` that is used to initiate the next request. If the response of the current request is truncated, you can use the token to initiate another request and obtain the remaining records.
        self.next_token = next_token  # type: str
        # The information about the permissions.
        self.permissions = permissions  # type: list[ListResourceSharePermissionsResponseBodyPermissions]
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.permissions:
            for k in self.permissions:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListResourceSharePermissionsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        result['Permissions'] = []
        if self.permissions is not None:
            for k in self.permissions:
                result['Permissions'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        self.permissions = []
        if m.get('Permissions') is not None:
            for k in m.get('Permissions'):
                temp_model = ListResourceSharePermissionsResponseBodyPermissions()
                self.permissions.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListResourceSharePermissionsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListResourceSharePermissionsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListResourceSharePermissionsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListResourceSharePermissionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListResourceSharesRequest(TeaModel):
    def __init__(self, max_results=None, next_token=None, permission_name=None, resource_owner=None,
                 resource_share_ids=None, resource_share_name=None, resource_share_status=None):
        # The maximum number of entries to return for a single request.
        # 
        # Valid values: 1 to 100. Default value: 20.
        self.max_results = max_results  # type: int
        # The `token` that is used to initiate the next request. If the response of the current request is truncated, you can use the token to initiate another request and obtain the remaining records.
        self.next_token = next_token  # type: str
        # The name of the permission. For more information, see [Permission library](~~465474~~).
        self.permission_name = permission_name  # type: str
        # The owner of the resource shares. Valid values:
        # 
        # *   Self: the current account
        # *   OtherAccounts: an account other than the current account
        self.resource_owner = resource_owner  # type: str
        # The ID of a resource share.
        self.resource_share_ids = resource_share_ids  # type: list[str]
        # The name of the resource share.
        self.resource_share_name = resource_share_name  # type: str
        # The status of the resource share. Valid values:
        # 
        # *   Active: The resource share is enabled.
        # *   Pending: The resource share is associated with one or more resource sharing invitations that are waiting for confirmation.
        # *   Deleting: The resource share is being deleted.
        # *   Deleted: The resource share is deleted.
        # 
        # >  The system deletes the records of resource shares in the Deleted state within 48 hours to 96 hours after you delete the resource shares.
        self.resource_share_status = resource_share_status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListResourceSharesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.permission_name is not None:
            result['PermissionName'] = self.permission_name
        if self.resource_owner is not None:
            result['ResourceOwner'] = self.resource_owner
        if self.resource_share_ids is not None:
            result['ResourceShareIds'] = self.resource_share_ids
        if self.resource_share_name is not None:
            result['ResourceShareName'] = self.resource_share_name
        if self.resource_share_status is not None:
            result['ResourceShareStatus'] = self.resource_share_status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('PermissionName') is not None:
            self.permission_name = m.get('PermissionName')
        if m.get('ResourceOwner') is not None:
            self.resource_owner = m.get('ResourceOwner')
        if m.get('ResourceShareIds') is not None:
            self.resource_share_ids = m.get('ResourceShareIds')
        if m.get('ResourceShareName') is not None:
            self.resource_share_name = m.get('ResourceShareName')
        if m.get('ResourceShareStatus') is not None:
            self.resource_share_status = m.get('ResourceShareStatus')
        return self


class ListResourceSharesResponseBodyResourceShares(TeaModel):
    def __init__(self, allow_external_targets=None, create_time=None, resource_share_id=None,
                 resource_share_name=None, resource_share_owner=None, resource_share_status=None, update_time=None):
        # Indicates whether resources in the resource share can be shared with accounts outside the resource directory. Valid values:
        # 
        # *   false: Resources in the resource share can be shared only with accounts in the resource directory.
        # *   true: Resources in the resource share can be shared with both accounts in the resource directory and accounts outside the resource directory.
        self.allow_external_targets = allow_external_targets  # type: bool
        # The time when the resource share was created.
        self.create_time = create_time  # type: str
        # The ID of the resource share.
        self.resource_share_id = resource_share_id  # type: str
        # The name of the resource share.
        self.resource_share_name = resource_share_name  # type: str
        # The owner of the resource share.
        self.resource_share_owner = resource_share_owner  # type: str
        # The status of the resource share. Valid values:
        # 
        # *   Active: The resource share is enabled.
        # *   Pending: The resource share is associated with one or more resource sharing invitations that are waiting for confirmation.
        # *   Deleting: The resource share is being deleted.
        # *   Deleted: The resource share is deleted.
        # 
        # >  The system deletes the records of resource shares in the Deleted state within 48 hours to 96 hours after you delete the resource shares.
        self.resource_share_status = resource_share_status  # type: str
        # The time when the resource share was updated.
        self.update_time = update_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListResourceSharesResponseBodyResourceShares, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.allow_external_targets is not None:
            result['AllowExternalTargets'] = self.allow_external_targets
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.resource_share_id is not None:
            result['ResourceShareId'] = self.resource_share_id
        if self.resource_share_name is not None:
            result['ResourceShareName'] = self.resource_share_name
        if self.resource_share_owner is not None:
            result['ResourceShareOwner'] = self.resource_share_owner
        if self.resource_share_status is not None:
            result['ResourceShareStatus'] = self.resource_share_status
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AllowExternalTargets') is not None:
            self.allow_external_targets = m.get('AllowExternalTargets')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ResourceShareId') is not None:
            self.resource_share_id = m.get('ResourceShareId')
        if m.get('ResourceShareName') is not None:
            self.resource_share_name = m.get('ResourceShareName')
        if m.get('ResourceShareOwner') is not None:
            self.resource_share_owner = m.get('ResourceShareOwner')
        if m.get('ResourceShareStatus') is not None:
            self.resource_share_status = m.get('ResourceShareStatus')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class ListResourceSharesResponseBody(TeaModel):
    def __init__(self, next_token=None, request_id=None, resource_shares=None):
        # The `token` that is used to initiate the next request. If the response of the current request is truncated, you can use the token to initiate another request and obtain the remaining records.
        self.next_token = next_token  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The information of the resource shares.
        self.resource_shares = resource_shares  # type: list[ListResourceSharesResponseBodyResourceShares]

    def validate(self):
        if self.resource_shares:
            for k in self.resource_shares:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListResourceSharesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['ResourceShares'] = []
        if self.resource_shares is not None:
            for k in self.resource_shares:
                result['ResourceShares'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.resource_shares = []
        if m.get('ResourceShares') is not None:
            for k in m.get('ResourceShares'):
                temp_model = ListResourceSharesResponseBodyResourceShares()
                self.resource_shares.append(temp_model.from_map(k))
        return self


class ListResourceSharesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListResourceSharesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListResourceSharesResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListResourceSharesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListSharedResourcesRequest(TeaModel):
    def __init__(self, max_results=None, next_token=None, resource_ids=None, resource_owner=None,
                 resource_share_ids=None, resource_type=None, target=None):
        # The maximum number of entries to return for a single request.
        # 
        # Valid values: 1 to 100. Default value: 20.
        self.max_results = max_results  # type: int
        # The `token` that is used to initiate the next request. If the response of the current request is truncated, you can use the token to initiate another request and obtain the remaining records.
        self.next_token = next_token  # type: str
        # The ID of a shared resource.
        self.resource_ids = resource_ids  # type: list[str]
        # The owner of the resource shares. Valid values:
        # 
        # *   Self: your account. If you set the value to Self, the resources you share with other accounts are queried.
        # *   OtherAccounts: another account. If you set the value to OtherAccounts, the resources other accounts share with you are queried.
        self.resource_owner = resource_owner  # type: str
        # The ID of a resource share.
        self.resource_share_ids = resource_share_ids  # type: list[str]
        # The type of the shared resources.
        # 
        # For more information about the types of resources that can be shared, see [Services that work with Resource Sharing](~~450526~~).
        self.resource_type = resource_type  # type: str
        # The ID of the principal or resource owner.
        # 
        # *   If the value of `ResourceOwner` is `Self`, set this parameter to the ID of a principal.
        # *   If the value of `ResourceOwner` is `OtherAccounts`, set this parameter to the ID of a resource owner.
        self.target = target  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListSharedResourcesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.resource_ids is not None:
            result['ResourceIds'] = self.resource_ids
        if self.resource_owner is not None:
            result['ResourceOwner'] = self.resource_owner
        if self.resource_share_ids is not None:
            result['ResourceShareIds'] = self.resource_share_ids
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.target is not None:
            result['Target'] = self.target
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('ResourceIds') is not None:
            self.resource_ids = m.get('ResourceIds')
        if m.get('ResourceOwner') is not None:
            self.resource_owner = m.get('ResourceOwner')
        if m.get('ResourceShareIds') is not None:
            self.resource_share_ids = m.get('ResourceShareIds')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('Target') is not None:
            self.target = m.get('Target')
        return self


class ListSharedResourcesResponseBodySharedResources(TeaModel):
    def __init__(self, create_time=None, resource_id=None, resource_share_id=None, resource_status=None,
                 resource_status_message=None, resource_type=None, update_time=None):
        # The time when the shared resource was associated with the resource share.
        self.create_time = create_time  # type: str
        # The ID of the shared resource.
        self.resource_id = resource_id  # type: str
        # The ID of the resource share.
        self.resource_share_id = resource_share_id  # type: str
        # The status of the shared resource. This parameter is returned only when you query the resources that other accounts share with you.
        # 
        # Valid values:
        # 
        # *   Available: The resource is available.
        # *   ZonalResourceInaccessible: The resource is unavailable in the current zone.
        # *   LimitExceeded: The resource is unavailable because the maximum number of resources that other accounts can share with you exceeds the upper limit.
        # *   Unavailable: The resource is unavailable.
        self.resource_status = resource_status  # type: str
        # The cause of the association failure.
        self.resource_status_message = resource_status_message  # type: str
        # The type of the shared resource.
        # 
        # For more information about the types of resources that can be shared, see [Services that work with Resource Sharing](~~450526~~).
        self.resource_type = resource_type  # type: str
        # The time when the association of the shared resource was updated.
        self.update_time = update_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListSharedResourcesResponseBodySharedResources, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_share_id is not None:
            result['ResourceShareId'] = self.resource_share_id
        if self.resource_status is not None:
            result['ResourceStatus'] = self.resource_status
        if self.resource_status_message is not None:
            result['ResourceStatusMessage'] = self.resource_status_message
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceShareId') is not None:
            self.resource_share_id = m.get('ResourceShareId')
        if m.get('ResourceStatus') is not None:
            self.resource_status = m.get('ResourceStatus')
        if m.get('ResourceStatusMessage') is not None:
            self.resource_status_message = m.get('ResourceStatusMessage')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class ListSharedResourcesResponseBody(TeaModel):
    def __init__(self, next_token=None, request_id=None, shared_resources=None):
        # The token that is used to initiate the next request. If the response of the current request is truncated, you can use the token to initiate another request and obtain the remaining records.
        self.next_token = next_token  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The information of the shared resources.
        self.shared_resources = shared_resources  # type: list[ListSharedResourcesResponseBodySharedResources]

    def validate(self):
        if self.shared_resources:
            for k in self.shared_resources:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListSharedResourcesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['SharedResources'] = []
        if self.shared_resources is not None:
            for k in self.shared_resources:
                result['SharedResources'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.shared_resources = []
        if m.get('SharedResources') is not None:
            for k in m.get('SharedResources'):
                temp_model = ListSharedResourcesResponseBodySharedResources()
                self.shared_resources.append(temp_model.from_map(k))
        return self


class ListSharedResourcesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListSharedResourcesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListSharedResourcesResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListSharedResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListSharedTargetsRequest(TeaModel):
    def __init__(self, max_results=None, next_token=None, resource_id=None, resource_owner=None,
                 resource_share_ids=None, resource_type=None, targets=None):
        # The maximum number of entries to return for a single request.
        # 
        # Valid values: 1 to 100. Default value: 20.
        self.max_results = max_results  # type: int
        # The `token` that is used to initiate the next request. If the response of the current request is truncated, you can use the token to initiate another request and obtain the remaining records.
        self.next_token = next_token  # type: str
        # The ID of the shared resource.
        self.resource_id = resource_id  # type: str
        # The owner of the resource share.
        # 
        # *   Self: your account. If you set the value to Self, the principals that are associated with your resource shares are queried.
        # *   OtherAccounts: another account. If you set the value to OtherAccounts, the resource shares with which your account is associated and the owners of the resource shares are queried.
        self.resource_owner = resource_owner  # type: str
        # The ID of a resource share.
        self.resource_share_ids = resource_share_ids  # type: list[str]
        # The type of the shared resources.
        # 
        # For more information about the types of resources that can be shared, see [Services that work with Resource Sharing](~~450526~~).
        self.resource_type = resource_type  # type: str
        # The ID of a principal.
        self.targets = targets  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListSharedTargetsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.max_results is not None:
            result['MaxResults'] = self.max_results
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_owner is not None:
            result['ResourceOwner'] = self.resource_owner
        if self.resource_share_ids is not None:
            result['ResourceShareIds'] = self.resource_share_ids
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.targets is not None:
            result['Targets'] = self.targets
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('MaxResults') is not None:
            self.max_results = m.get('MaxResults')
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceOwner') is not None:
            self.resource_owner = m.get('ResourceOwner')
        if m.get('ResourceShareIds') is not None:
            self.resource_share_ids = m.get('ResourceShareIds')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('Targets') is not None:
            self.targets = m.get('Targets')
        return self


class ListSharedTargetsResponseBodySharedTargets(TeaModel):
    def __init__(self, create_time=None, external=None, resource_share_id=None, target_id=None,
                 target_property=None, update_time=None):
        # The time when the principal was associated with the resource share.
        self.create_time = create_time  # type: str
        # Indicates whether the principal is outside the resource directory. Valid values:
        # 
        # *   true: The principal is outside the resource directory.
        # *   false: The principal is in the resource directory.
        self.external = external  # type: bool
        # The ID of the resource share.
        self.resource_share_id = resource_share_id  # type: str
        # The ID of the principal or resource owner.
        # 
        # *   If the value of `ResourceOwner` is `Self`, the value of this parameter is the ID of a principal.
        # *   If the value of `ResourceOwner` is `OtherAccounts`, the value of this parameter is the ID of a resource owner.
        self.target_id = target_id  # type: str
        self.target_property = target_property  # type: str
        # The time when the association of the principal was updated.
        self.update_time = update_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListSharedTargetsResponseBodySharedTargets, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.external is not None:
            result['External'] = self.external
        if self.resource_share_id is not None:
            result['ResourceShareId'] = self.resource_share_id
        if self.target_id is not None:
            result['TargetId'] = self.target_id
        if self.target_property is not None:
            result['TargetProperty'] = self.target_property
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('External') is not None:
            self.external = m.get('External')
        if m.get('ResourceShareId') is not None:
            self.resource_share_id = m.get('ResourceShareId')
        if m.get('TargetId') is not None:
            self.target_id = m.get('TargetId')
        if m.get('TargetProperty') is not None:
            self.target_property = m.get('TargetProperty')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class ListSharedTargetsResponseBody(TeaModel):
    def __init__(self, next_token=None, request_id=None, shared_targets=None):
        # The `token` that is used to initiate the next request. If the response of the current request is truncated, you can use the token to initiate another request and obtain the remaining records.
        self.next_token = next_token  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The information of the principals.
        self.shared_targets = shared_targets  # type: list[ListSharedTargetsResponseBodySharedTargets]

    def validate(self):
        if self.shared_targets:
            for k in self.shared_targets:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListSharedTargetsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['SharedTargets'] = []
        if self.shared_targets is not None:
            for k in self.shared_targets:
                result['SharedTargets'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.shared_targets = []
        if m.get('SharedTargets') is not None:
            for k in m.get('SharedTargets'):
                temp_model = ListSharedTargetsResponseBodySharedTargets()
                self.shared_targets.append(temp_model.from_map(k))
        return self


class ListSharedTargetsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListSharedTargetsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListSharedTargetsResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = ListSharedTargetsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RejectResourceShareInvitationRequest(TeaModel):
    def __init__(self, resource_share_invitation_id=None):
        # The ID of the resource sharing invitation.
        # 
        # You can call the [ListResourceShareInvitations](~~450564~~) operation to obtain the ID of a resource sharing invitation.
        self.resource_share_invitation_id = resource_share_invitation_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RejectResourceShareInvitationRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_share_invitation_id is not None:
            result['ResourceShareInvitationId'] = self.resource_share_invitation_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ResourceShareInvitationId') is not None:
            self.resource_share_invitation_id = m.get('ResourceShareInvitationId')
        return self


class RejectResourceShareInvitationResponseBodyResourceShareInvitation(TeaModel):
    def __init__(self, create_time=None, receiver_account_id=None, resource_share_id=None,
                 resource_share_invitation_id=None, resource_share_name=None, sender_account_id=None, status=None):
        # The time when the invitation was created. The time is displayed in UTC.
        self.create_time = create_time  # type: str
        # The Alibaba Cloud account ID of the invitee.
        self.receiver_account_id = receiver_account_id  # type: str
        # The ID of the resource share.
        self.resource_share_id = resource_share_id  # type: str
        # The ID of the invitation.
        self.resource_share_invitation_id = resource_share_invitation_id  # type: str
        # The name of the resource share.
        self.resource_share_name = resource_share_name  # type: str
        # The Alibaba Cloud account ID of the inviter.
        self.sender_account_id = sender_account_id  # type: str
        # The status of the invitation. Valid values:
        # 
        # *   Pending: The invitation is waiting for confirmation.
        # *   Accepted: The invitation is accepted.
        # *   Cancelled: The invitation is canceled.
        # *   Rejected: The invitation is rejected.
        # *   Expired: The invitation has expired.
        self.status = status  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RejectResourceShareInvitationResponseBodyResourceShareInvitation, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.receiver_account_id is not None:
            result['ReceiverAccountId'] = self.receiver_account_id
        if self.resource_share_id is not None:
            result['ResourceShareId'] = self.resource_share_id
        if self.resource_share_invitation_id is not None:
            result['ResourceShareInvitationId'] = self.resource_share_invitation_id
        if self.resource_share_name is not None:
            result['ResourceShareName'] = self.resource_share_name
        if self.sender_account_id is not None:
            result['SenderAccountId'] = self.sender_account_id
        if self.status is not None:
            result['Status'] = self.status
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ReceiverAccountId') is not None:
            self.receiver_account_id = m.get('ReceiverAccountId')
        if m.get('ResourceShareId') is not None:
            self.resource_share_id = m.get('ResourceShareId')
        if m.get('ResourceShareInvitationId') is not None:
            self.resource_share_invitation_id = m.get('ResourceShareInvitationId')
        if m.get('ResourceShareName') is not None:
            self.resource_share_name = m.get('ResourceShareName')
        if m.get('SenderAccountId') is not None:
            self.sender_account_id = m.get('SenderAccountId')
        if m.get('Status') is not None:
            self.status = m.get('Status')
        return self


class RejectResourceShareInvitationResponseBody(TeaModel):
    def __init__(self, request_id=None, resource_share_invitation=None):
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The information of the resource sharing invitation.
        self.resource_share_invitation = resource_share_invitation  # type: RejectResourceShareInvitationResponseBodyResourceShareInvitation

    def validate(self):
        if self.resource_share_invitation:
            self.resource_share_invitation.validate()

    def to_map(self):
        _map = super(RejectResourceShareInvitationResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.resource_share_invitation is not None:
            result['ResourceShareInvitation'] = self.resource_share_invitation.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResourceShareInvitation') is not None:
            temp_model = RejectResourceShareInvitationResponseBodyResourceShareInvitation()
            self.resource_share_invitation = temp_model.from_map(m['ResourceShareInvitation'])
        return self


class RejectResourceShareInvitationResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RejectResourceShareInvitationResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RejectResourceShareInvitationResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = RejectResourceShareInvitationResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpdateResourceShareRequest(TeaModel):
    def __init__(self, allow_external_targets=None, resource_share_id=None, resource_share_name=None):
        # Specifies whether resources in the resource share can be shared with accounts outside the resource directory. Valid values:
        # 
        # *   false: Resources in the resource share can be shared only with accounts in the resource directory.
        # *   true: Resources in the resource share can be shared with both accounts in the resource directory and accounts outside the resource directory.
        self.allow_external_targets = allow_external_targets  # type: bool
        # The ID of the resource share.
        self.resource_share_id = resource_share_id  # type: str
        # The new name of the resource share.
        # 
        # The name must be 1 to 50 characters in length.
        # 
        # The name can contain letters, digits, periods (.), underscores (\_), and hyphens (-).
        self.resource_share_name = resource_share_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateResourceShareRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.allow_external_targets is not None:
            result['AllowExternalTargets'] = self.allow_external_targets
        if self.resource_share_id is not None:
            result['ResourceShareId'] = self.resource_share_id
        if self.resource_share_name is not None:
            result['ResourceShareName'] = self.resource_share_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AllowExternalTargets') is not None:
            self.allow_external_targets = m.get('AllowExternalTargets')
        if m.get('ResourceShareId') is not None:
            self.resource_share_id = m.get('ResourceShareId')
        if m.get('ResourceShareName') is not None:
            self.resource_share_name = m.get('ResourceShareName')
        return self


class UpdateResourceShareResponseBodyResourceShare(TeaModel):
    def __init__(self, allow_external_targets=None, create_time=None, resource_share_id=None,
                 resource_share_name=None, resource_share_owner=None, resource_share_status=None, update_time=None):
        # Indicates whether resources in the resource share can be shared with accounts outside the resource directory. Valid values:
        # 
        # *   false: Resources in the resource share can be shared only with accounts in the resource directory.
        # *   true: Resources in the resource share can be shared with both accounts in the resource directory and accounts outside the resource directory.
        self.allow_external_targets = allow_external_targets  # type: bool
        # The time when the resource share was created.
        self.create_time = create_time  # type: str
        # The ID of the resource share.
        self.resource_share_id = resource_share_id  # type: str
        # The name of the resource share.
        self.resource_share_name = resource_share_name  # type: str
        # The owner of the resource share.
        self.resource_share_owner = resource_share_owner  # type: str
        # The status of the resource share. Valid values:
        # 
        # *   Active: The resource share is enabled.
        # *   Pending: The resource share is associated with one or more resource sharing invitations that are waiting for confirmation.
        # *   Deleting: The resource share is being deleted.
        # *   Deleted: The resource share is deleted.
        # 
        # >  The system deletes the records of resource shares in the Deleted state within 48 hours to 96 hours after you delete the resource shares.
        self.resource_share_status = resource_share_status  # type: str
        # The time when the resource share was updated.
        self.update_time = update_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpdateResourceShareResponseBodyResourceShare, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.allow_external_targets is not None:
            result['AllowExternalTargets'] = self.allow_external_targets
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.resource_share_id is not None:
            result['ResourceShareId'] = self.resource_share_id
        if self.resource_share_name is not None:
            result['ResourceShareName'] = self.resource_share_name
        if self.resource_share_owner is not None:
            result['ResourceShareOwner'] = self.resource_share_owner
        if self.resource_share_status is not None:
            result['ResourceShareStatus'] = self.resource_share_status
        if self.update_time is not None:
            result['UpdateTime'] = self.update_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AllowExternalTargets') is not None:
            self.allow_external_targets = m.get('AllowExternalTargets')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ResourceShareId') is not None:
            self.resource_share_id = m.get('ResourceShareId')
        if m.get('ResourceShareName') is not None:
            self.resource_share_name = m.get('ResourceShareName')
        if m.get('ResourceShareOwner') is not None:
            self.resource_share_owner = m.get('ResourceShareOwner')
        if m.get('ResourceShareStatus') is not None:
            self.resource_share_status = m.get('ResourceShareStatus')
        if m.get('UpdateTime') is not None:
            self.update_time = m.get('UpdateTime')
        return self


class UpdateResourceShareResponseBody(TeaModel):
    def __init__(self, request_id=None, resource_share=None):
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The information of the resource share.
        self.resource_share = resource_share  # type: UpdateResourceShareResponseBodyResourceShare

    def validate(self):
        if self.resource_share:
            self.resource_share.validate()

    def to_map(self):
        _map = super(UpdateResourceShareResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.resource_share is not None:
            result['ResourceShare'] = self.resource_share.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('ResourceShare') is not None:
            temp_model = UpdateResourceShareResponseBodyResourceShare()
            self.resource_share = temp_model.from_map(m['ResourceShare'])
        return self


class UpdateResourceShareResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UpdateResourceShareResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpdateResourceShareResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.status_code is not None:
            result['statusCode'] = self.status_code
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('statusCode') is not None:
            self.status_code = m.get('statusCode')
        if m.get('body') is not None:
            temp_model = UpdateResourceShareResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


