# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class AcceptApproveCommandRequest(TeaModel):
    def __init__(self, command_id=None, instance_id=None, region_id=None):
        self.command_id = command_id  # type: str
        self.instance_id = instance_id  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AcceptApproveCommandRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.command_id is not None:
            result['CommandId'] = self.command_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CommandId') is not None:
            self.command_id = m.get('CommandId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class AcceptApproveCommandResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AcceptApproveCommandResponseBody, self).to_map()
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


class AcceptApproveCommandResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: AcceptApproveCommandResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AcceptApproveCommandResponse, self).to_map()
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
            temp_model = AcceptApproveCommandResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AcceptOperationTicketRequest(TeaModel):
    def __init__(self, effect_count=None, effect_end_time=None, effect_start_time=None, instance_id=None,
                 operation_ticket_id=None, region_id=None):
        # The maximum number of logons allowed. Valid values:
        # 
        # *   0: The number of logons is unlimited. The O\&M engineer can log on to the specified asset for an unlimited number of times during the validity period.
        # *   1: The O\&M engineer can log on to the specified asset only once during the validity period.
        # 
        # >  You can set this parameter only to 0 if you review an O\&M application on a database.
        self.effect_count = effect_count  # type: str
        # The end time of the validity period. The value is a UNIX timestamp. Unit: seconds.
        self.effect_end_time = effect_end_time  # type: str
        # The start time of the validity period. The value is a UNIX timestamp. Unit: seconds.
        self.effect_start_time = effect_start_time  # type: str
        # The ID of the bastion host.
        # 
        # > You can call the [DescribeInstances](~~153281~~) operation to query the ID of the bastion host.
        self.instance_id = instance_id  # type: str
        # The ID of the O\&M application that you want to approve. You can call the ListOperationTickets operation to query the IDs of all O\&M applications that require review.
        self.operation_ticket_id = operation_ticket_id  # type: str
        # The region ID of the bastion host.
        # 
        # >  For more information about the mapping between region IDs and region names, see [Regions and zones](~~40654~~).
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AcceptOperationTicketRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.effect_count is not None:
            result['EffectCount'] = self.effect_count
        if self.effect_end_time is not None:
            result['EffectEndTime'] = self.effect_end_time
        if self.effect_start_time is not None:
            result['EffectStartTime'] = self.effect_start_time
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.operation_ticket_id is not None:
            result['OperationTicketId'] = self.operation_ticket_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EffectCount') is not None:
            self.effect_count = m.get('EffectCount')
        if m.get('EffectEndTime') is not None:
            self.effect_end_time = m.get('EffectEndTime')
        if m.get('EffectStartTime') is not None:
            self.effect_start_time = m.get('EffectStartTime')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('OperationTicketId') is not None:
            self.operation_ticket_id = m.get('OperationTicketId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class AcceptOperationTicketResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The request ID.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AcceptOperationTicketResponseBody, self).to_map()
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


class AcceptOperationTicketResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: AcceptOperationTicketResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AcceptOperationTicketResponse, self).to_map()
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
            temp_model = AcceptOperationTicketResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddHostsToGroupRequest(TeaModel):
    def __init__(self, host_group_id=None, host_ids=None, instance_id=None, region_id=None):
        # The ID of the host group to which you want to add hosts.
        # 
        # > You can call the [ListHostGroups](~~201307~~) operation to query the ID of the host group.
        self.host_group_id = host_group_id  # type: str
        # The ID of the host that you want to add to the host group. The value is a JSON string. You can add up to 100 host IDs.
        # 
        # > You can call the [ListHosts](~~200665~~) operation to query the IDs of hosts.
        self.host_ids = host_ids  # type: str
        # The ID of the bastion host for which you want to add hosts to the host group.
        # 
        # > You can call the [DescribeInstances](~~153281~~) operation to query the ID of the bastion host.
        self.instance_id = instance_id  # type: str
        # The region ID of the bastion host for which you want to add hosts to the host group.
        # 
        # > For more information about the mapping between region IDs and region names, see [Regions and zones](~~40654~~).
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddHostsToGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.host_group_id is not None:
            result['HostGroupId'] = self.host_group_id
        if self.host_ids is not None:
            result['HostIds'] = self.host_ids
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('HostGroupId') is not None:
            self.host_group_id = m.get('HostGroupId')
        if m.get('HostIds') is not None:
            self.host_ids = m.get('HostIds')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class AddHostsToGroupResponseBodyResults(TeaModel):
    def __init__(self, code=None, host_group_id=None, host_id=None, message=None):
        # The return code that indicates whether the call was successful. Valid values:
        # 
        # *   **OK**: The call was successful.
        # 
        # *   **UNEXPECTED**: An unknown error occurred.
        # 
        # *   **INVALID_ARGUMENT**: A request parameter is invalid.
        # 
        #     **\
        # 
        #     **Note**Make sure that the request parameters are valid and call the operation again.
        # 
        # *   **OBJECT_NOT_FOUND**: The specified object on which you want to perform the operation does not exist.
        # 
        #     **\
        # 
        #     **Note**Check whether the specified ID of the bastion host exists, whether the specified hosts exist, and whether the specified host IDs are valid. Then, call the operation again.
        # 
        # *   **OBJECT_AlREADY_EXISTS**: The specified object on which you want to perform the operation already exists.
        self.code = code  # type: str
        # The ID of the host group.
        self.host_group_id = host_group_id  # type: str
        # The ID of the host.
        self.host_id = host_id  # type: str
        # This parameter is deprecated.
        self.message = message  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddHostsToGroupResponseBodyResults, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.host_group_id is not None:
            result['HostGroupId'] = self.host_group_id
        if self.host_id is not None:
            result['HostId'] = self.host_id
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('HostGroupId') is not None:
            self.host_group_id = m.get('HostGroupId')
        if m.get('HostId') is not None:
            self.host_id = m.get('HostId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class AddHostsToGroupResponseBody(TeaModel):
    def __init__(self, request_id=None, results=None):
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The result of the call.
        self.results = results  # type: list[AddHostsToGroupResponseBodyResults]

    def validate(self):
        if self.results:
            for k in self.results:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(AddHostsToGroupResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Results'] = []
        if self.results is not None:
            for k in self.results:
                result['Results'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.results = []
        if m.get('Results') is not None:
            for k in m.get('Results'):
                temp_model = AddHostsToGroupResponseBodyResults()
                self.results.append(temp_model.from_map(k))
        return self


class AddHostsToGroupResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: AddHostsToGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AddHostsToGroupResponse, self).to_map()
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
            temp_model = AddHostsToGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddUsersToGroupRequest(TeaModel):
    def __init__(self, instance_id=None, region_id=None, user_group_id=None, user_ids=None):
        # The ID of the user that you want to add to the user group. The value is a JSON string. You can add up to 100 user IDs. If you specify multiple IDs, separate the IDs with commas (,).
        # 
        # >  You can call the [ListUsers](~~204522~~) operation to query the IDs of users.
        self.instance_id = instance_id  # type: str
        # The ID of the user.
        self.region_id = region_id  # type: str
        # The return code that indicates whether the call was successful. Valid values:
        # 
        # *   **OK**: The call was successful.
        # 
        # *   **UNEXPECTED**: An unknown error occurred.
        # 
        # *   **INVALID_ARGUMENT**: A request parameter is invalid.
        # 
        # > Make sure that the request parameters are valid and call the operation again.
        # 
        # *   **OBJECT_NOT_FOUND**: The specified object on which you want to perform the operation does not exist.
        # 
        # > Check whether the specified ID of the bastion host exists, whether the specified hosts exist, and whether the specified host IDs are valid. Then, call the operation again.
        # 
        # *   **OBJECT_AlREADY_EXISTS**: The specified object on which you want to perform the operation already exists.
        self.user_group_id = user_group_id  # type: str
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.user_ids = user_ids  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddUsersToGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.user_group_id is not None:
            result['UserGroupId'] = self.user_group_id
        if self.user_ids is not None:
            result['UserIds'] = self.user_ids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('UserGroupId') is not None:
            self.user_group_id = m.get('UserGroupId')
        if m.get('UserIds') is not None:
            self.user_ids = m.get('UserIds')
        return self


class AddUsersToGroupResponseBodyResults(TeaModel):
    def __init__(self, code=None, message=None, user_group_id=None, user_id=None):
        # AddUsersToGroup
        self.code = code  # type: str
        # WB01014029
        self.message = message  # type: str
        # AddUsersToGroup
        self.user_group_id = user_group_id  # type: str
        self.user_id = user_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AddUsersToGroupResponseBodyResults, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.user_group_id is not None:
            result['UserGroupId'] = self.user_group_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('UserGroupId') is not None:
            self.user_group_id = m.get('UserGroupId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class AddUsersToGroupResponseBody(TeaModel):
    def __init__(self, request_id=None, results=None):
        # All Alibaba Cloud API operations must include common request parameters. For more information about common request parameters, see [Common parameters](~~315526~~).
        # 
        # For more information about sample requests, see the "Examples" section of this topic.
        self.request_id = request_id  # type: str
        # Adds one or more users to a user group.
        self.results = results  # type: list[AddUsersToGroupResponseBodyResults]

    def validate(self):
        if self.results:
            for k in self.results:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(AddUsersToGroupResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Results'] = []
        if self.results is not None:
            for k in self.results:
                result['Results'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.results = []
        if m.get('Results') is not None:
            for k in m.get('Results'):
                temp_model = AddUsersToGroupResponseBodyResults()
                self.results.append(temp_model.from_map(k))
        return self


class AddUsersToGroupResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: AddUsersToGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AddUsersToGroupResponse, self).to_map()
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
            temp_model = AddUsersToGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AttachHostAccountsToHostShareKeyRequest(TeaModel):
    def __init__(self, host_account_ids=None, host_share_key_id=None, instance_id=None, region_id=None):
        # The IDs of the host accounts.
        # 
        # > You must specify this parameter.
        self.host_account_ids = host_account_ids  # type: str
        # The ID of the shared key.
        # 
        # > You must specify this parameter.
        self.host_share_key_id = host_share_key_id  # type: str
        # The ID of the bastion host. You can call the [DescribeInstances](~~153281~~) operation to query the ID of the bastion host.
        self.instance_id = instance_id  # type: str
        # The region ID of the bastion host. For more information about the mapping between region IDs and region names, see [Regions and zones](~~40654~~).
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AttachHostAccountsToHostShareKeyRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.host_account_ids is not None:
            result['HostAccountIds'] = self.host_account_ids
        if self.host_share_key_id is not None:
            result['HostShareKeyId'] = self.host_share_key_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('HostAccountIds') is not None:
            self.host_account_ids = m.get('HostAccountIds')
        if m.get('HostShareKeyId') is not None:
            self.host_share_key_id = m.get('HostShareKeyId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class AttachHostAccountsToHostShareKeyResponseBodyResults(TeaModel):
    def __init__(self, code=None, host_account_id=None, host_share_key_id=None, message=None):
        # The error code returned. If **OK** is returned, the association was successful. If another error code is returned, the association failed.
        self.code = code  # type: str
        # The ID of the host account.
        self.host_account_id = host_account_id  # type: str
        # The ID of the shared key.
        self.host_share_key_id = host_share_key_id  # type: str
        # The error message returned.
        self.message = message  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AttachHostAccountsToHostShareKeyResponseBodyResults, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.host_account_id is not None:
            result['HostAccountId'] = self.host_account_id
        if self.host_share_key_id is not None:
            result['HostShareKeyId'] = self.host_share_key_id
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('HostAccountId') is not None:
            self.host_account_id = m.get('HostAccountId')
        if m.get('HostShareKeyId') is not None:
            self.host_share_key_id = m.get('HostShareKeyId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class AttachHostAccountsToHostShareKeyResponseBody(TeaModel):
    def __init__(self, request_id=None, results=None):
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id  # type: str
        # The result of the call.
        self.results = results  # type: list[AttachHostAccountsToHostShareKeyResponseBodyResults]

    def validate(self):
        if self.results:
            for k in self.results:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(AttachHostAccountsToHostShareKeyResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Results'] = []
        if self.results is not None:
            for k in self.results:
                result['Results'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.results = []
        if m.get('Results') is not None:
            for k in m.get('Results'):
                temp_model = AttachHostAccountsToHostShareKeyResponseBodyResults()
                self.results.append(temp_model.from_map(k))
        return self


class AttachHostAccountsToHostShareKeyResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: AttachHostAccountsToHostShareKeyResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AttachHostAccountsToHostShareKeyResponse, self).to_map()
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
            temp_model = AttachHostAccountsToHostShareKeyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AttachHostAccountsToUserRequest(TeaModel):
    def __init__(self, hosts=None, instance_id=None, region_id=None, user_id=None):
        # The IDs of the host and host account that you want to authorize the user to manage. You can specify up to 10 host IDs and up to 10 host account IDs for each host. You can specify only host IDs. In this case, the user is authorized to manage only the specified hosts. For more information about this parameter, see the "Description of the Hosts parameter" section of this topic.
        # 
        # >  You can call the [ListHosts](~~200665~~) operation to query the ID of the host and the [ListHostAccounts](~~204372~~) operation to query the ID of the host account.
        self.hosts = hosts  # type: str
        # The ID of the bastion host for which you want to authorize the user to manage the specified hosts and host accounts.
        # 
        # >  You can call the [DescribeInstances](~~153281~~) operation to query the ID of the bastion host.
        self.instance_id = instance_id  # type: str
        # The region ID of the bastion host for which you want to authorize the user to manage the specified hosts and host accounts.
        # 
        # >  For more information about the mapping between region IDs and region names, see [Regions and zones](~~40654~~).
        self.region_id = region_id  # type: str
        # The ID of the user that you want to authorize to manage the specified hosts and host accounts.
        # 
        # >  You can call the [ListUsers](~~204522~~) operation to query the ID of the user.
        self.user_id = user_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AttachHostAccountsToUserRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.hosts is not None:
            result['Hosts'] = self.hosts
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Hosts') is not None:
            self.hosts = m.get('Hosts')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class AttachHostAccountsToUserResponseBodyResultsHostAccounts(TeaModel):
    def __init__(self, code=None, host_account_id=None, message=None):
        # The return code that indicates whether the user was authorized to manage the specified host account. Valid values:
        # 
        # *   **OK**: The call was successful.
        # *   **UNEXPECTED**: An unknown error occurred.
        # *   **INVALID_ARGUMENT**: A request parameter is invalid.
        # *   **OBJECT_NOT_FOUND**: The specified object on which you want to perform the operation does not exist.
        # *   **OBJECT_AlREADY_EXISTS**: The specified object on which you want to perform the operation already exists.
        self.code = code  # type: str
        # The ID of the host account.
        self.host_account_id = host_account_id  # type: str
        # This parameter is deprecated.
        self.message = message  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AttachHostAccountsToUserResponseBodyResultsHostAccounts, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.host_account_id is not None:
            result['HostAccountId'] = self.host_account_id
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('HostAccountId') is not None:
            self.host_account_id = m.get('HostAccountId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class AttachHostAccountsToUserResponseBodyResults(TeaModel):
    def __init__(self, code=None, host_accounts=None, host_id=None, message=None, user_id=None):
        # The return code that indicates whether the call was successful. Valid values:
        # 
        # *   **OK**: The call was successful.
        # 
        # *   **UNEXPECTED**: An unknown error occurred.
        # 
        # *   **INVALID_ARGUMENT**: A request parameter is invalid.
        # 
        # > Make sure that the request parameters are valid and call the operation again.
        # 
        # *   **OBJECT_NOT_FOUND**: The specified object on which you want to perform the operation does not exist.
        # 
        # > Check whether the specified ID of the bastion host exists, whether the specified hosts exist, and whether the specified host IDs are valid. Then, call the operation again.
        # 
        # *   **OBJECT_AlREADY_EXISTS**: The specified object on which you want to perform the operation already exists.
        self.code = code  # type: str
        # The result of authorizing the specified user to manage the specified host accounts.
        self.host_accounts = host_accounts  # type: list[AttachHostAccountsToUserResponseBodyResultsHostAccounts]
        # The ID of the host.
        self.host_id = host_id  # type: str
        # This parameter is deprecated.
        self.message = message  # type: str
        # The ID of the user.
        self.user_id = user_id  # type: str

    def validate(self):
        if self.host_accounts:
            for k in self.host_accounts:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(AttachHostAccountsToUserResponseBodyResults, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['HostAccounts'] = []
        if self.host_accounts is not None:
            for k in self.host_accounts:
                result['HostAccounts'].append(k.to_map() if k else None)
        if self.host_id is not None:
            result['HostId'] = self.host_id
        if self.message is not None:
            result['Message'] = self.message
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.host_accounts = []
        if m.get('HostAccounts') is not None:
            for k in m.get('HostAccounts'):
                temp_model = AttachHostAccountsToUserResponseBodyResultsHostAccounts()
                self.host_accounts.append(temp_model.from_map(k))
        if m.get('HostId') is not None:
            self.host_id = m.get('HostId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class AttachHostAccountsToUserResponseBody(TeaModel):
    def __init__(self, request_id=None, results=None):
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The result of the call.
        self.results = results  # type: list[AttachHostAccountsToUserResponseBodyResults]

    def validate(self):
        if self.results:
            for k in self.results:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(AttachHostAccountsToUserResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Results'] = []
        if self.results is not None:
            for k in self.results:
                result['Results'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.results = []
        if m.get('Results') is not None:
            for k in m.get('Results'):
                temp_model = AttachHostAccountsToUserResponseBodyResults()
                self.results.append(temp_model.from_map(k))
        return self


class AttachHostAccountsToUserResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: AttachHostAccountsToUserResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AttachHostAccountsToUserResponse, self).to_map()
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
            temp_model = AttachHostAccountsToUserResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AttachHostAccountsToUserGroupRequest(TeaModel):
    def __init__(self, hosts=None, instance_id=None, region_id=None, user_group_id=None):
        # The IDs of the host and host account that you want to authorize the user group to manage. You can specify up to 10 host IDs and up to 10 host account IDs for each host. You can specify only host IDs. In this case, the user group is authorized to manage only the specified hosts. For more information about this parameter, see the "Description of the Hosts parameter" section of this topic.
        # 
        # > You can call the [ListHosts](~~200665~~) operation to query the ID of the host and the [ListHostAccounts](~~204372~~) operation to query the ID of the host account.
        self.hosts = hosts  # type: str
        # The ID of the bastion host in which you want to authorize the user group to manage the specified hosts and host accounts.
        # 
        # > You can call the [DescribeInstances](~~153281~~) operation to query the ID of the bastion host.
        self.instance_id = instance_id  # type: str
        # The region ID of the bastion host in which you want to authorize the user group to manage the specified hosts and host accounts.
        # 
        # > For more information about the mapping between region IDs and region names, see [Regions and zones](~~40654~~).
        self.region_id = region_id  # type: str
        # The ID of the user group that you want to authorize to manage the specified hosts and host accounts.
        # 
        # > You can call the [ListUserGroups](~~204509~~) operation to query the ID of the user group.
        self.user_group_id = user_group_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AttachHostAccountsToUserGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.hosts is not None:
            result['Hosts'] = self.hosts
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.user_group_id is not None:
            result['UserGroupId'] = self.user_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Hosts') is not None:
            self.hosts = m.get('Hosts')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('UserGroupId') is not None:
            self.user_group_id = m.get('UserGroupId')
        return self


class AttachHostAccountsToUserGroupResponseBodyResultsHostAccounts(TeaModel):
    def __init__(self, code=None, host_account_id=None, message=None):
        # The return code that indicates whether the user group was authorized to manage the specified host account. Valid values:
        # 
        # *   **OK**: The call was successful.
        # *   **UNEXPECTED**: An unknown error occurred.
        # *   **INVALID_ARGUMENT**: A request parameter is invalid.
        # *   **OBJECT_NOT_FOUND**: The specified object on which you want to perform the operation does not exist.
        # *   **OBJECT_AlREADY_EXISTS**: The specified object on which you want to perform the operation already exists.
        self.code = code  # type: str
        # The ID of the host account.
        self.host_account_id = host_account_id  # type: str
        # This parameter is deprecated.
        self.message = message  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AttachHostAccountsToUserGroupResponseBodyResultsHostAccounts, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.host_account_id is not None:
            result['HostAccountId'] = self.host_account_id
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('HostAccountId') is not None:
            self.host_account_id = m.get('HostAccountId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class AttachHostAccountsToUserGroupResponseBodyResults(TeaModel):
    def __init__(self, code=None, host_accounts=None, host_id=None, message=None, user_group_id=None):
        # The return code that indicates whether the call was successful. Valid values:
        # 
        # *   **OK**: The call was successful.
        # *   **UNEXPECTED**: An unknown error occurred.
        # *   **INVALID_ARGUMENT**: A request parameter is invalid.
        # *   **OBJECT_NOT_FOUND**: The specified object on which you want to perform the operation does not exist.
        # *   **OBJECT_AlREADY_EXISTS**: The specified object on which you want to perform the operation already exists.
        self.code = code  # type: str
        # The result of authorizing the specified user group to manage the specified host accounts.
        self.host_accounts = host_accounts  # type: list[AttachHostAccountsToUserGroupResponseBodyResultsHostAccounts]
        # The ID of the host.
        self.host_id = host_id  # type: str
        # This parameter is deprecated.
        self.message = message  # type: str
        # The ID of the user group.
        self.user_group_id = user_group_id  # type: str

    def validate(self):
        if self.host_accounts:
            for k in self.host_accounts:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(AttachHostAccountsToUserGroupResponseBodyResults, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['HostAccounts'] = []
        if self.host_accounts is not None:
            for k in self.host_accounts:
                result['HostAccounts'].append(k.to_map() if k else None)
        if self.host_id is not None:
            result['HostId'] = self.host_id
        if self.message is not None:
            result['Message'] = self.message
        if self.user_group_id is not None:
            result['UserGroupId'] = self.user_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.host_accounts = []
        if m.get('HostAccounts') is not None:
            for k in m.get('HostAccounts'):
                temp_model = AttachHostAccountsToUserGroupResponseBodyResultsHostAccounts()
                self.host_accounts.append(temp_model.from_map(k))
        if m.get('HostId') is not None:
            self.host_id = m.get('HostId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('UserGroupId') is not None:
            self.user_group_id = m.get('UserGroupId')
        return self


class AttachHostAccountsToUserGroupResponseBody(TeaModel):
    def __init__(self, request_id=None, results=None):
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The result of the call.
        self.results = results  # type: list[AttachHostAccountsToUserGroupResponseBodyResults]

    def validate(self):
        if self.results:
            for k in self.results:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(AttachHostAccountsToUserGroupResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Results'] = []
        if self.results is not None:
            for k in self.results:
                result['Results'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.results = []
        if m.get('Results') is not None:
            for k in m.get('Results'):
                temp_model = AttachHostAccountsToUserGroupResponseBodyResults()
                self.results.append(temp_model.from_map(k))
        return self


class AttachHostAccountsToUserGroupResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: AttachHostAccountsToUserGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AttachHostAccountsToUserGroupResponse, self).to_map()
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
            temp_model = AttachHostAccountsToUserGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AttachHostGroupAccountsToUserRequest(TeaModel):
    def __init__(self, host_groups=None, instance_id=None, region_id=None, user_id=None):
        # The ID of the host group and the name of the host account that you want to authorize the user to manage. You can specify up to 10 host group IDs and up to 10 host account names for each host group. You can specify only host group IDs. In this case, the user is authorized to manage only the specified host groups. For more information about this parameter, see the "Description of the HostGroups parameter" section of this topic.
        # 
        # >  You can call the [ListHostGroups](~~201307~~) operation to query the ID of the host group and the [ListHostAccounts](~~204372~~) operation to query the name of the host account.
        self.host_groups = host_groups  # type: str
        # The ID of the bastion host for which you want to authorize the user to manage the specified host groups and host accounts.
        # 
        # >  You can call the [DescribeInstances](~~153281~~) operation to query the ID of the bastion host.
        self.instance_id = instance_id  # type: str
        # The region ID of the bastion host for which you want to authorize the user to manage the specified host groups and host accounts.
        # 
        # >  For more information about the mapping between region IDs and region names, see [Regions and zones](~~40654~~).
        self.region_id = region_id  # type: str
        # The ID of the user that you want to authorize to manage the specified host groups and host accounts.
        # 
        # >  You can call the [ListUsers](~~204522~~) operation to query the ID of the user.
        self.user_id = user_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AttachHostGroupAccountsToUserRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.host_groups is not None:
            result['HostGroups'] = self.host_groups
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('HostGroups') is not None:
            self.host_groups = m.get('HostGroups')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class AttachHostGroupAccountsToUserResponseBodyResultsHostAccountNames(TeaModel):
    def __init__(self, code=None, host_account_name=None, message=None):
        # The return code that indicates whether the user was authorized to manage the specified host account. Valid values:
        # 
        # *   **OK**: The call was successful.
        # *   **UNEXPECTED**: An unknown error occurred.
        # *   **INVALID_ARGUMENT**: A request parameter is invalid.
        # *   **OBJECT_NOT_FOUND**: The specified object on which you want to perform the operation does not exist.
        # *   **OBJECT_AlREADY_EXISTS**: The specified object on which you want to perform the operation already exists.
        self.code = code  # type: str
        # The name of the host account.
        self.host_account_name = host_account_name  # type: str
        # This parameter is deprecated.
        self.message = message  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AttachHostGroupAccountsToUserResponseBodyResultsHostAccountNames, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.host_account_name is not None:
            result['HostAccountName'] = self.host_account_name
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('HostAccountName') is not None:
            self.host_account_name = m.get('HostAccountName')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class AttachHostGroupAccountsToUserResponseBodyResults(TeaModel):
    def __init__(self, code=None, host_account_names=None, host_group_id=None, message=None, user_id=None):
        # The return code that indicates whether the call was successful. Valid values:
        # 
        # *   **OK**: The call was successful.
        # *   **UNEXPECTED**: An unknown error occurred.
        # *   **INVALID_ARGUMENT**: A request parameter is invalid.
        # *   **OBJECT_NOT_FOUND**: The specified object on which you want to perform the operation does not exist.
        # *   **OBJECT_AlREADY_EXISTS**: The specified object on which you want to perform the operation already exists.
        self.code = code  # type: str
        # The result of authorizing the user to manage the specified host accounts.
        self.host_account_names = host_account_names  # type: list[AttachHostGroupAccountsToUserResponseBodyResultsHostAccountNames]
        # The ID of the host group.
        self.host_group_id = host_group_id  # type: str
        # This parameter is deprecated.
        self.message = message  # type: str
        # The ID of the user.
        self.user_id = user_id  # type: str

    def validate(self):
        if self.host_account_names:
            for k in self.host_account_names:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(AttachHostGroupAccountsToUserResponseBodyResults, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['HostAccountNames'] = []
        if self.host_account_names is not None:
            for k in self.host_account_names:
                result['HostAccountNames'].append(k.to_map() if k else None)
        if self.host_group_id is not None:
            result['HostGroupId'] = self.host_group_id
        if self.message is not None:
            result['Message'] = self.message
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.host_account_names = []
        if m.get('HostAccountNames') is not None:
            for k in m.get('HostAccountNames'):
                temp_model = AttachHostGroupAccountsToUserResponseBodyResultsHostAccountNames()
                self.host_account_names.append(temp_model.from_map(k))
        if m.get('HostGroupId') is not None:
            self.host_group_id = m.get('HostGroupId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class AttachHostGroupAccountsToUserResponseBody(TeaModel):
    def __init__(self, request_id=None, results=None):
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The result of the call.
        self.results = results  # type: list[AttachHostGroupAccountsToUserResponseBodyResults]

    def validate(self):
        if self.results:
            for k in self.results:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(AttachHostGroupAccountsToUserResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Results'] = []
        if self.results is not None:
            for k in self.results:
                result['Results'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.results = []
        if m.get('Results') is not None:
            for k in m.get('Results'):
                temp_model = AttachHostGroupAccountsToUserResponseBodyResults()
                self.results.append(temp_model.from_map(k))
        return self


class AttachHostGroupAccountsToUserResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: AttachHostGroupAccountsToUserResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AttachHostGroupAccountsToUserResponse, self).to_map()
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
            temp_model = AttachHostGroupAccountsToUserResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AttachHostGroupAccountsToUserGroupRequest(TeaModel):
    def __init__(self, host_groups=None, instance_id=None, region_id=None, user_group_id=None):
        # The ID of the host group and the name of the host account that you want to authorize the user group to manage. You can specify up to 10 host group IDs and up to 10 host account names for each host group. You can specify only host group IDs. In this case, the user group is authorized to manage only the specified host groups. For more information about this parameter, see the "Description of the HostGroups parameter" section of this topic.
        # 
        # >  You can call the [ListHostGroups](~~201307~~) operation to query the ID of the host group and the [ListHostAccounts](~~204372~~) operation to query the name of the host account.
        self.host_groups = host_groups  # type: str
        # The ID of the bastion host for which you want to authorize the user group to manage the specified host groups and host accounts.
        # 
        # >  You can call the [DescribeInstances](~~153281~~) operation to query the ID of the bastion host.
        self.instance_id = instance_id  # type: str
        # The region ID of the bastion host for which you want to authorize the user group to manage the specified host groups and host accounts.
        # 
        # >  For more information about the mapping between region IDs and region names, see [Regions and zones](~~40654~~).
        self.region_id = region_id  # type: str
        # The ID of the user group that you want to authorize to manage the specified host groups and host accounts.
        # 
        # >  You can call the [ListUserGroups](~~204509~~) operation to query the ID of the user group.
        self.user_group_id = user_group_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AttachHostGroupAccountsToUserGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.host_groups is not None:
            result['HostGroups'] = self.host_groups
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.user_group_id is not None:
            result['UserGroupId'] = self.user_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('HostGroups') is not None:
            self.host_groups = m.get('HostGroups')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('UserGroupId') is not None:
            self.user_group_id = m.get('UserGroupId')
        return self


class AttachHostGroupAccountsToUserGroupResponseBodyResultsHostAccountNames(TeaModel):
    def __init__(self, code=None, host_account_name=None, message=None):
        # The return code that indicates whether the user group was authorized to manage the specified host account. Valid values:
        # 
        # *   **OK**: The call was successful.
        # *   **UNEXPECTED**: An unknown error occurred.
        # *   **INVALID_ARGUMENT**: A request parameter is invalid.
        # *   **OBJECT_NOT_FOUND**: The specified object on which you want to perform the operation does not exist.
        # *   **OBJECT_AlREADY_EXISTS**: The specified object on which you want to perform the operation already exists.
        self.code = code  # type: str
        # The name of the host account.
        self.host_account_name = host_account_name  # type: str
        # This parameter is deprecated.
        self.message = message  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(AttachHostGroupAccountsToUserGroupResponseBodyResultsHostAccountNames, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.host_account_name is not None:
            result['HostAccountName'] = self.host_account_name
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('HostAccountName') is not None:
            self.host_account_name = m.get('HostAccountName')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class AttachHostGroupAccountsToUserGroupResponseBodyResults(TeaModel):
    def __init__(self, code=None, host_account_names=None, host_group_id=None, message=None, user_group_id=None):
        # The return code that indicates whether the call was successful. Valid values:
        # 
        # *   **OK**: The call was successful.
        # *   **UNEXPECTED**: An unknown error occurred.
        # *   **INVALID_ARGUMENT**: A request parameter is invalid.
        # *   **OBJECT_NOT_FOUND**: The specified object on which you want to perform the operation does not exist.
        # *   **OBJECT_AlREADY_EXISTS**: The specified object on which you want to perform the operation already exists.
        self.code = code  # type: str
        # The result of authorizing the user group to manage the specified host accounts.
        self.host_account_names = host_account_names  # type: list[AttachHostGroupAccountsToUserGroupResponseBodyResultsHostAccountNames]
        # The ID of the host group.
        self.host_group_id = host_group_id  # type: str
        # This parameter is deprecated.
        self.message = message  # type: str
        # The ID of the group.
        self.user_group_id = user_group_id  # type: str

    def validate(self):
        if self.host_account_names:
            for k in self.host_account_names:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(AttachHostGroupAccountsToUserGroupResponseBodyResults, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['HostAccountNames'] = []
        if self.host_account_names is not None:
            for k in self.host_account_names:
                result['HostAccountNames'].append(k.to_map() if k else None)
        if self.host_group_id is not None:
            result['HostGroupId'] = self.host_group_id
        if self.message is not None:
            result['Message'] = self.message
        if self.user_group_id is not None:
            result['UserGroupId'] = self.user_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.host_account_names = []
        if m.get('HostAccountNames') is not None:
            for k in m.get('HostAccountNames'):
                temp_model = AttachHostGroupAccountsToUserGroupResponseBodyResultsHostAccountNames()
                self.host_account_names.append(temp_model.from_map(k))
        if m.get('HostGroupId') is not None:
            self.host_group_id = m.get('HostGroupId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('UserGroupId') is not None:
            self.user_group_id = m.get('UserGroupId')
        return self


class AttachHostGroupAccountsToUserGroupResponseBody(TeaModel):
    def __init__(self, request_id=None, results=None):
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The result of the call.
        self.results = results  # type: list[AttachHostGroupAccountsToUserGroupResponseBodyResults]

    def validate(self):
        if self.results:
            for k in self.results:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(AttachHostGroupAccountsToUserGroupResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Results'] = []
        if self.results is not None:
            for k in self.results:
                result['Results'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.results = []
        if m.get('Results') is not None:
            for k in m.get('Results'):
                temp_model = AttachHostGroupAccountsToUserGroupResponseBodyResults()
                self.results.append(temp_model.from_map(k))
        return self


class AttachHostGroupAccountsToUserGroupResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: AttachHostGroupAccountsToUserGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(AttachHostGroupAccountsToUserGroupResponse, self).to_map()
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
            temp_model = AttachHostGroupAccountsToUserGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ConfigInstanceSecurityGroupsRequest(TeaModel):
    def __init__(self, authorized_security_groups=None, instance_id=None, lang=None, region_id=None):
        # An array that consists of the IDs of authorized security groups.
        self.authorized_security_groups = authorized_security_groups  # type: list[str]
        # The ID of the bastion host.
        # 
        # > You can call the [DescribeInstances](~~153281~~) operation to query the ID of the bastion host.
        self.instance_id = instance_id  # type: str
        # The language of the content within the request and response. Default value: **zh**. Valid values:
        # 
        # *   **zh**: Chinese
        # *   **en**: English
        self.lang = lang  # type: str
        # The region ID of the bastion host.
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ConfigInstanceSecurityGroupsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.authorized_security_groups is not None:
            result['AuthorizedSecurityGroups'] = self.authorized_security_groups
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AuthorizedSecurityGroups') is not None:
            self.authorized_security_groups = m.get('AuthorizedSecurityGroups')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ConfigInstanceSecurityGroupsResponseBody(TeaModel):
    def __init__(self, instance_id=None, request_id=None):
        # The ID of the bastion host for which security groups were configured.
        self.instance_id = instance_id  # type: str
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ConfigInstanceSecurityGroupsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ConfigInstanceSecurityGroupsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ConfigInstanceSecurityGroupsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ConfigInstanceSecurityGroupsResponse, self).to_map()
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
            temp_model = ConfigInstanceSecurityGroupsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ConfigInstanceWhiteListRequest(TeaModel):
    def __init__(self, instance_id=None, region_id=None, white_list=None):
        # The ID of the bastion host for which a whitelist of public IP addresses is configured.
        self.instance_id = instance_id  # type: str
        # Configures a whitelist of public IP addresses for a bastion host.
        self.region_id = region_id  # type: str
        # ConfigInstanceWhiteList
        self.white_list = white_list  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(ConfigInstanceWhiteListRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.white_list is not None:
            result['WhiteList'] = self.white_list
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('WhiteList') is not None:
            self.white_list = m.get('WhiteList')
        return self


class ConfigInstanceWhiteListResponseBody(TeaModel):
    def __init__(self, instance_id=None, request_id=None):
        self.instance_id = instance_id  # type: str
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ConfigInstanceWhiteListResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ConfigInstanceWhiteListResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ConfigInstanceWhiteListResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ConfigInstanceWhiteListResponse, self).to_map()
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
            temp_model = ConfigInstanceWhiteListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateHostRequest(TeaModel):
    def __init__(self, active_address_type=None, comment=None, host_name=None, host_private_address=None,
                 host_public_address=None, instance_id=None, instance_region_id=None, network_domain_id=None, ostype=None,
                 region_id=None, source=None, source_instance_id=None):
        # The endpoint type of the host that you want to create. Valid values:
        # 
        # *   **Public**: public endpoint
        # *   **Private**: internal endpoint
        self.active_address_type = active_address_type  # type: str
        # The description of the host that you want to create. The value can be up to 500 characters in length.
        self.comment = comment  # type: str
        # The name of the host that you want to create. The name can be up to 128 characters in length.
        self.host_name = host_name  # type: str
        # The internal endpoint of the host that you want to create. You can set this parameter to a domain name or an IP address.
        # 
        # > This parameter is required if the **ActiveAddressType** parameter is set to **Private**.
        self.host_private_address = host_private_address  # type: str
        # The public endpoint of the host that you want to create. You can set this parameter to a domain name or an IP address.
        # 
        # > This parameter is required if the **ActiveAddressType** parameter is set to **Public**.
        self.host_public_address = host_public_address  # type: str
        # The ID of the bastion host in which you want to create the host.
        # 
        # > You can call the [DescribeInstances](~~153281~~) operation to query the ID of the bastion host.
        self.instance_id = instance_id  # type: str
        # The ID of the region to which the ECS instance or the host in an ApsaraDB MyBase dedicated cluster belongs.
        # 
        # > This parameter is required if the **Source** parameter is set to **Ecs** or **Rds**.
        self.instance_region_id = instance_region_id  # type: str
        self.network_domain_id = network_domain_id  # type: str
        # The operating system of the host that you want to create. Valid values:
        # 
        # *   **Linux**\
        # *   **Windows**\
        self.ostype = ostype  # type: str
        # The region ID of the bastion host in which you want to create the host.
        # 
        # > For more information about the mapping between region IDs and region names, see [Regions and zones](~~40654~~).
        self.region_id = region_id  # type: str
        # The source of the host that you want to create. Valid values:
        # 
        # *   **Local**: a host in a data center
        # *   **Ecs**: an Elastic Compute Service (ECS) instance
        # *   **Rds**: a host in an ApsaraDB MyBase dedicated cluster
        self.source = source  # type: str
        # The ID of the ECS instance or the host in an ApsaraDB MyBase dedicated cluster.
        # 
        # > This parameter is required if the **Source** parameter is set to **Ecs** or **Rds**.
        self.source_instance_id = source_instance_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateHostRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.active_address_type is not None:
            result['ActiveAddressType'] = self.active_address_type
        if self.comment is not None:
            result['Comment'] = self.comment
        if self.host_name is not None:
            result['HostName'] = self.host_name
        if self.host_private_address is not None:
            result['HostPrivateAddress'] = self.host_private_address
        if self.host_public_address is not None:
            result['HostPublicAddress'] = self.host_public_address
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_region_id is not None:
            result['InstanceRegionId'] = self.instance_region_id
        if self.network_domain_id is not None:
            result['NetworkDomainId'] = self.network_domain_id
        if self.ostype is not None:
            result['OSType'] = self.ostype
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.source is not None:
            result['Source'] = self.source
        if self.source_instance_id is not None:
            result['SourceInstanceId'] = self.source_instance_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ActiveAddressType') is not None:
            self.active_address_type = m.get('ActiveAddressType')
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')
        if m.get('HostName') is not None:
            self.host_name = m.get('HostName')
        if m.get('HostPrivateAddress') is not None:
            self.host_private_address = m.get('HostPrivateAddress')
        if m.get('HostPublicAddress') is not None:
            self.host_public_address = m.get('HostPublicAddress')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceRegionId') is not None:
            self.instance_region_id = m.get('InstanceRegionId')
        if m.get('NetworkDomainId') is not None:
            self.network_domain_id = m.get('NetworkDomainId')
        if m.get('OSType') is not None:
            self.ostype = m.get('OSType')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('SourceInstanceId') is not None:
            self.source_instance_id = m.get('SourceInstanceId')
        return self


class CreateHostResponseBody(TeaModel):
    def __init__(self, host_id=None, request_id=None):
        # The ID of the host.
        self.host_id = host_id  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateHostResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.host_id is not None:
            result['HostId'] = self.host_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('HostId') is not None:
            self.host_id = m.get('HostId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateHostResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateHostResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateHostResponse, self).to_map()
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
            temp_model = CreateHostResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateHostAccountRequest(TeaModel):
    def __init__(self, host_account_name=None, host_id=None, host_share_key_id=None, instance_id=None,
                 pass_phrase=None, password=None, private_key=None, protocol_name=None, region_id=None):
        # The passphrase of the private key for the host account.
        # 
        # >  You can specify this parameter when the ProtocolName parameter is set to SSH. If the ProtocolName parameter is set to RDP, you do not need to specify this parameter.
        self.host_account_name = host_account_name  # type: str
        # The ID of the shared key.
        self.host_id = host_id  # type: str
        # The protocol of the host to which you want to add a host account.
        # 
        # Valid values:
        # 
        # *   SSH
        # *   RDP
        self.host_share_key_id = host_share_key_id  # type: str
        # master
        self.instance_id = instance_id  # type: str
        # The private key of the host account. The value is a Base64-encoded string.
        # 
        # >  This parameter takes effect only when the ProtocolName parameter is set to SSH. If the ProtocolName parameter is set to RDP, you do not need to specify this parameter. You can configure a password and a private key for the host account at the same time. If both a password and a private key are configured for the host account, Bastionhost preferentially uses the private key to log on to the host.
        self.pass_phrase = pass_phrase  # type: str
        # The region ID of the bastion host in which you want to add a host account to the host.
        # 
        # >  For more information about the mapping between region IDs and region names, see [Regions and zones](~~40654~~).
        self.password = password  # type: str
        # The ID of the host to which you want to add a host account.
        # 
        # >  You can call the [ListHosts](~~200665~~) operation to query the ID of the host.
        self.private_key = private_key  # type: str
        # The ID of the bastion host in which you want to add a host account to the host.
        # 
        # >  You can call the [DescribeInstances](~~153281~~) operation to query the ID of the bastion host.
        self.protocol_name = protocol_name  # type: str
        # The password of the host account.
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateHostAccountRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.host_account_name is not None:
            result['HostAccountName'] = self.host_account_name
        if self.host_id is not None:
            result['HostId'] = self.host_id
        if self.host_share_key_id is not None:
            result['HostShareKeyId'] = self.host_share_key_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.pass_phrase is not None:
            result['PassPhrase'] = self.pass_phrase
        if self.password is not None:
            result['Password'] = self.password
        if self.private_key is not None:
            result['PrivateKey'] = self.private_key
        if self.protocol_name is not None:
            result['ProtocolName'] = self.protocol_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('HostAccountName') is not None:
            self.host_account_name = m.get('HostAccountName')
        if m.get('HostId') is not None:
            self.host_id = m.get('HostId')
        if m.get('HostShareKeyId') is not None:
            self.host_share_key_id = m.get('HostShareKeyId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('PassPhrase') is not None:
            self.pass_phrase = m.get('PassPhrase')
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('PrivateKey') is not None:
            self.private_key = m.get('PrivateKey')
        if m.get('ProtocolName') is not None:
            self.protocol_name = m.get('ProtocolName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class CreateHostAccountResponseBody(TeaModel):
    def __init__(self, host_account_id=None, request_id=None):
        # The ID of the request.
        self.host_account_id = host_account_id  # type: str
        # The operation that you want to perform. Set the value to **CreateHostAccount**.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateHostAccountResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.host_account_id is not None:
            result['HostAccountId'] = self.host_account_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('HostAccountId') is not None:
            self.host_account_id = m.get('HostAccountId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateHostAccountResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateHostAccountResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateHostAccountResponse, self).to_map()
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
            temp_model = CreateHostAccountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateHostGroupRequest(TeaModel):
    def __init__(self, comment=None, host_group_name=None, instance_id=None, region_id=None):
        # The description of the host group. The description can be up to 500 characters in length.
        self.comment = comment  # type: str
        # The name of the host group. The name can be up to 128 characters in length.
        self.host_group_name = host_group_name  # type: str
        # The ID of the bastion host on which you want to create a host group.
        # 
        # > You can call the [DescribeInstances](~~153281~~) operation to query the ID of the bastion host.
        self.instance_id = instance_id  # type: str
        # The region ID of the bastion host on which you want to create a host group.
        # 
        # **\
        # 
        # **For more information about the mapping between region IDs and region names, see **Regions and zones[.](~~40654~~)
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateHostGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.comment is not None:
            result['Comment'] = self.comment
        if self.host_group_name is not None:
            result['HostGroupName'] = self.host_group_name
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')
        if m.get('HostGroupName') is not None:
            self.host_group_name = m.get('HostGroupName')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class CreateHostGroupResponseBody(TeaModel):
    def __init__(self, host_group_id=None, request_id=None):
        # The ID of the host group.
        self.host_group_id = host_group_id  # type: str
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateHostGroupResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.host_group_id is not None:
            result['HostGroupId'] = self.host_group_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('HostGroupId') is not None:
            self.host_group_id = m.get('HostGroupId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateHostGroupResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateHostGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateHostGroupResponse, self).to_map()
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
            temp_model = CreateHostGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateHostShareKeyRequest(TeaModel):
    def __init__(self, host_share_key_name=None, instance_id=None, pass_phrase=None, private_key=None,
                 region_id=None):
        # The name of the shared key that you want to create. The name can be a maximum of 128 characters in length.
        self.host_share_key_name = host_share_key_name  # type: str
        # The ID of the bastion host. You can call the [DescribeInstances](~~153281~~) operation to query the ID of the bastion host.
        self.instance_id = instance_id  # type: str
        # The password of the private key. The value is a Base64-encoded string.
        self.pass_phrase = pass_phrase  # type: str
        # The private key. The value is a Base64-encoded string.
        self.private_key = private_key  # type: str
        # The region ID of the bastion host. For more information about the mapping between region IDs and region names, see [Regions and zones](~~40654~~).
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateHostShareKeyRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.host_share_key_name is not None:
            result['HostShareKeyName'] = self.host_share_key_name
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.pass_phrase is not None:
            result['PassPhrase'] = self.pass_phrase
        if self.private_key is not None:
            result['PrivateKey'] = self.private_key
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('HostShareKeyName') is not None:
            self.host_share_key_name = m.get('HostShareKeyName')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('PassPhrase') is not None:
            self.pass_phrase = m.get('PassPhrase')
        if m.get('PrivateKey') is not None:
            self.private_key = m.get('PrivateKey')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class CreateHostShareKeyResponseBody(TeaModel):
    def __init__(self, host_share_key_id=None, request_id=None):
        # The ID of the shared key.
        self.host_share_key_id = host_share_key_id  # type: long
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateHostShareKeyResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.host_share_key_id is not None:
            result['HostShareKeyId'] = self.host_share_key_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('HostShareKeyId') is not None:
            self.host_share_key_id = m.get('HostShareKeyId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateHostShareKeyResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateHostShareKeyResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateHostShareKeyResponse, self).to_map()
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
            temp_model = CreateHostShareKeyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateUserRequest(TeaModel):
    def __init__(self, comment=None, display_name=None, effective_end_time=None, effective_start_time=None,
                 email=None, instance_id=None, mobile=None, mobile_country_code=None, need_reset_password=None,
                 password=None, region_id=None, source=None, source_user_id=None, two_factor_methods=None,
                 two_factor_status=None, user_name=None):
        # The remarks of the user that you want to add. The remarks can be up to 500 characters in length.
        self.comment = comment  # type: str
        # The display name of the user that you want to add. This display name can be up to 128 characters in length.
        self.display_name = display_name  # type: str
        # The end of the validity period of the user. The value is a UNIX timestamp. Unit: seconds.
        self.effective_end_time = effective_end_time  # type: long
        # The beginning of the validity period of the user. The value is a UNIX timestamp. Unit: seconds.
        self.effective_start_time = effective_start_time  # type: long
        # The email address of the user that you want to add.
        self.email = email  # type: str
        # The ID of the bastion host to which you want to add a user.
        # 
        # >  You can call the [DescribeInstances](~~153281~~) operation to query the ID of the bastion host.
        self.instance_id = instance_id  # type: str
        # The mobile phone number of the user that you want to add.
        self.mobile = mobile  # type: str
        # The country where the mobile number of the user is registered. Default value: **CN**. Valid values:
        # 
        # *   **CN**: the Chinese mainland, whose country calling code is +86
        # *   **HK**: Hong Kong (China), whose country calling code is +852
        # *   **MO**: Macau (China), whose country calling code is +853
        # *   **TW**: Taiwan (China), whose country calling code is +886
        # *   **RU**: Russia, whose country calling code is +7
        # *   **SG**: Singapore, whose country calling code is +65
        # *   **MY**: Malaysia, whose country calling code is +60
        # *   **ID**: Indonesia, whose country calling code is +62
        # *   **DE**: Germany, whose country calling code is +49
        # *   **AU**: Australia, whose country calling code is +61
        # *   **US**: US, whose country calling code is +1
        # *   **AE**: United Arab Emirates, whose country calling code is +971
        # *   **JP**: Japan, whose country calling code is +81
        # *   **GB**: UK, whose country calling code is +44
        # *   **IN**: India, whose country calling code is +91
        # *   **KR**: Republic of Korea, whose country calling code is +82
        # *   **PH**: Philippines, whose country calling code is +63
        # *   **CH**: Switzerland, whose country calling code is +41
        # *   **SE**: Sweden, whose country calling code is +46
        self.mobile_country_code = mobile_country_code  # type: str
        # Specifies whether password reset is required upon the next logon. Valid values:
        # 
        # - true: yes
        # 
        # - false: no
        self.need_reset_password = need_reset_password  # type: bool
        # The logon password of the user that you want to add. The logon password can be up to 128 characters in length.
        # 
        # >  This parameter is required if the **Source** parameter is set to **Local**.
        self.password = password  # type: str
        # The region ID of the bastion host to which you want to add a user.
        # 
        # >  For more information about the mapping between region IDs and region names, see [Regions and zones](~~40654~~).
        self.region_id = region_id  # type: str
        # The source of the user that you want to add. Valid values:
        # 
        # - **Local**: a local user
        # - **Ram**: a RAM user
        # - **AD** : an AD-authenticated user
        # - **LDAP** : an LDAP-authenticated user
        self.source = source  # type: str
        # The unique identifier of the user that you want to add.
        # 
        # >  This parameter uniquely identifies a RAM user of the bastion host. This parameter is required if the **Source** parameter is set to **Ram**. You can call the [ListUsers](~~28684~~) operation to obtain the unique identifier of the user from the **UserId** response parameter.
        self.source_user_id = source_user_id  # type: str
        # The two-factor authentication method. You can select only one method. Valid values:
        # 
        # *   **sms:** text message
        # *   **email:** email
        # *   **dingtalk:** DingTalk
        # *   **totp OTP:** time-based one-time password (TOTP) app
        # 
        # > *   When the TwoFactorStatus parameter is set to Enable, you must specify one of the preceding values.
        self.two_factor_methods = two_factor_methods  # type: str
        # The two-factor authentication status of the user. Valid values:
        # 
        # - Global: follows the global settings
        # - Disable: disables two-factor authentication
        # - Enable: enable two-factor authentication and follows settings of the single user
        self.two_factor_status = two_factor_status  # type: str
        # The logon name of the user that you want to add. The logon name can contain only letters, digits, and underscores (\_) and can be up to 128 characters in length.
        self.user_name = user_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateUserRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.comment is not None:
            result['Comment'] = self.comment
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.effective_end_time is not None:
            result['EffectiveEndTime'] = self.effective_end_time
        if self.effective_start_time is not None:
            result['EffectiveStartTime'] = self.effective_start_time
        if self.email is not None:
            result['Email'] = self.email
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.mobile is not None:
            result['Mobile'] = self.mobile
        if self.mobile_country_code is not None:
            result['MobileCountryCode'] = self.mobile_country_code
        if self.need_reset_password is not None:
            result['NeedResetPassword'] = self.need_reset_password
        if self.password is not None:
            result['Password'] = self.password
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.source is not None:
            result['Source'] = self.source
        if self.source_user_id is not None:
            result['SourceUserId'] = self.source_user_id
        if self.two_factor_methods is not None:
            result['TwoFactorMethods'] = self.two_factor_methods
        if self.two_factor_status is not None:
            result['TwoFactorStatus'] = self.two_factor_status
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('EffectiveEndTime') is not None:
            self.effective_end_time = m.get('EffectiveEndTime')
        if m.get('EffectiveStartTime') is not None:
            self.effective_start_time = m.get('EffectiveStartTime')
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Mobile') is not None:
            self.mobile = m.get('Mobile')
        if m.get('MobileCountryCode') is not None:
            self.mobile_country_code = m.get('MobileCountryCode')
        if m.get('NeedResetPassword') is not None:
            self.need_reset_password = m.get('NeedResetPassword')
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('SourceUserId') is not None:
            self.source_user_id = m.get('SourceUserId')
        if m.get('TwoFactorMethods') is not None:
            self.two_factor_methods = m.get('TwoFactorMethods')
        if m.get('TwoFactorStatus') is not None:
            self.two_factor_status = m.get('TwoFactorStatus')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class CreateUserResponseBody(TeaModel):
    def __init__(self, request_id=None, user_id=None):
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id  # type: str
        # The ID of the user.
        self.user_id = user_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateUserResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class CreateUserResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateUserResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateUserResponse, self).to_map()
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
            temp_model = CreateUserResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateUserGroupRequest(TeaModel):
    def __init__(self, comment=None, instance_id=None, region_id=None, user_group_name=None):
        # The description of the user group. The description can be up to 500 characters in length.
        self.comment = comment  # type: str
        # The ID of the bastion host for which you want to create a user group.
        # 
        # > You can call the [DescribeInstances](~~153281~~) operation to query the ID of the bastion host.
        self.instance_id = instance_id  # type: str
        # The region ID of the bastion host for which you want to create a user group.
        # 
        # > For more information about the mapping between region IDs and region names, see [Regions and zones](~~40654~~).
        self.region_id = region_id  # type: str
        # The name of the user group that you want to create. This name can be a up to 128 characters in length.
        self.user_group_name = user_group_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateUserGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.comment is not None:
            result['Comment'] = self.comment
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.user_group_name is not None:
            result['UserGroupName'] = self.user_group_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('UserGroupName') is not None:
            self.user_group_name = m.get('UserGroupName')
        return self


class CreateUserGroupResponseBody(TeaModel):
    def __init__(self, request_id=None, user_group_id=None):
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id  # type: str
        # The ID of the user group.
        self.user_group_id = user_group_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateUserGroupResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.user_group_id is not None:
            result['UserGroupId'] = self.user_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('UserGroupId') is not None:
            self.user_group_id = m.get('UserGroupId')
        return self


class CreateUserGroupResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateUserGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateUserGroupResponse, self).to_map()
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
            temp_model = CreateUserGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateUserPublicKeyRequest(TeaModel):
    def __init__(self, comment=None, instance_id=None, public_key=None, public_key_name=None, region_id=None,
                 user_id=None):
        # The description of the public key. The description can be up to 500 characters in length.
        self.comment = comment  # type: str
        # The ID of the bastion host on which you want to create a public key for the user.
        # 
        # > You can call the [listinstances](~~204522~~) operation to query the ID of the bastion host.
        self.instance_id = instance_id  # type: str
        # The public key. Encode the value by using the Base64 algorithm.
        self.public_key = public_key  # type: str
        # The name of the public key.
        self.public_key_name = public_key_name  # type: str
        # Specifies the region ID of the bastion host on which you want to create a public key for the user.
        # 
        # > For more information about the mapping between region IDs and region names, see [Regions and zones](~~40654~~).
        self.region_id = region_id  # type: str
        # Specifies the ID of the user for whom you want to create a public key.
        self.user_id = user_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateUserPublicKeyRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.comment is not None:
            result['Comment'] = self.comment
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.public_key is not None:
            result['PublicKey'] = self.public_key
        if self.public_key_name is not None:
            result['PublicKeyName'] = self.public_key_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('PublicKey') is not None:
            self.public_key = m.get('PublicKey')
        if m.get('PublicKeyName') is not None:
            self.public_key_name = m.get('PublicKeyName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class CreateUserPublicKeyResponseBody(TeaModel):
    def __init__(self, public_key_id=None, request_id=None):
        # The ID of the public key.
        self.public_key_id = public_key_id  # type: str
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(CreateUserPublicKeyResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.public_key_id is not None:
            result['PublicKeyId'] = self.public_key_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PublicKeyId') is not None:
            self.public_key_id = m.get('PublicKeyId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class CreateUserPublicKeyResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: CreateUserPublicKeyResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(CreateUserPublicKeyResponse, self).to_map()
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
            temp_model = CreateUserPublicKeyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteHostRequest(TeaModel):
    def __init__(self, host_id=None, instance_id=None, region_id=None):
        # The ID of the host that you want to delete.
        # 
        # > You can call the [ListHosts](~~200665~~) operation to query the ID of the host.
        self.host_id = host_id  # type: str
        # The ID of the bastion host on which you want to delete the host.
        # 
        # > You can call the [DescribeInstances](~~153281~~) operation to query the ID of the bastion host.
        self.instance_id = instance_id  # type: str
        # The region ID of the bastion host on which you want to delete the host.
        # 
        # > For more information about the mapping between region IDs and region names, see [Regions and zones](~~40654~~).
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteHostRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.host_id is not None:
            result['HostId'] = self.host_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('HostId') is not None:
            self.host_id = m.get('HostId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DeleteHostResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteHostResponseBody, self).to_map()
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


class DeleteHostResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteHostResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteHostResponse, self).to_map()
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
            temp_model = DeleteHostResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteHostAccountRequest(TeaModel):
    def __init__(self, host_account_id=None, instance_id=None, region_id=None):
        # DeleteHostAccount
        self.host_account_id = host_account_id  # type: str
        # DeleteHostAccount
        self.instance_id = instance_id  # type: str
        # WB01014029
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteHostAccountRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.host_account_id is not None:
            result['HostAccountId'] = self.host_account_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('HostAccountId') is not None:
            self.host_account_id = m.get('HostAccountId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DeleteHostAccountResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteHostAccountResponseBody, self).to_map()
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


class DeleteHostAccountResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteHostAccountResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteHostAccountResponse, self).to_map()
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
            temp_model = DeleteHostAccountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteHostGroupRequest(TeaModel):
    def __init__(self, host_group_id=None, instance_id=None, region_id=None):
        # The ID of the host group that you want to delete.
        # 
        # > You can call the [ListHostGroups](~~201307~~) operation to query the ID of the host group.
        self.host_group_id = host_group_id  # type: str
        # The ID of the bastion host from which you want to delete the host group.
        # 
        # > You can call the [DescribeInstances](~~153281~~) operation to query the ID of the bastion host.
        self.instance_id = instance_id  # type: str
        # The region ID of the bastion host from which you want to delete the host group.
        # 
        # > For more information about the mapping between region IDs and region names, see [Regions and zones](~~40654~~).
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteHostGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.host_group_id is not None:
            result['HostGroupId'] = self.host_group_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('HostGroupId') is not None:
            self.host_group_id = m.get('HostGroupId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DeleteHostGroupResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteHostGroupResponseBody, self).to_map()
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


class DeleteHostGroupResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteHostGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteHostGroupResponse, self).to_map()
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
            temp_model = DeleteHostGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteHostShareKeyRequest(TeaModel):
    def __init__(self, host_share_key_id=None, instance_id=None, region_id=None):
        # The ID of the shared key.
        # 
        # > You must specify this parameter.
        self.host_share_key_id = host_share_key_id  # type: str
        # The ID of the bastion host. You can call the [DescribeInstances](~~153281~~) operation to query the ID of the bastion host.
        self.instance_id = instance_id  # type: str
        # The region ID of the bastion host. For more information about the mapping between region IDs and region names, see [Regions and zones](~~40654~~).
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteHostShareKeyRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.host_share_key_id is not None:
            result['HostShareKeyId'] = self.host_share_key_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('HostShareKeyId') is not None:
            self.host_share_key_id = m.get('HostShareKeyId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DeleteHostShareKeyResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteHostShareKeyResponseBody, self).to_map()
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


class DeleteHostShareKeyResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteHostShareKeyResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteHostShareKeyResponse, self).to_map()
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
            temp_model = DeleteHostShareKeyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteUserRequest(TeaModel):
    def __init__(self, instance_id=None, region_id=None, user_id=None):
        # The ID of the bastion host to which the user to be deleted belongs.
        # 
        # > You can call the [DescribeInstances](~~153281~~) operation to query the ID of the bastion host.
        self.instance_id = instance_id  # type: str
        # The region ID of the bastion host to which the user to be deleted belongs.
        # 
        # > For more information about the mapping between region IDs and region names, see [Regions and zones](~~40654~~).
        self.region_id = region_id  # type: str
        # The ID of the user to be deleted.
        self.user_id = user_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteUserRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class DeleteUserResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteUserResponseBody, self).to_map()
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


class DeleteUserResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteUserResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteUserResponse, self).to_map()
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
            temp_model = DeleteUserResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteUserGroupRequest(TeaModel):
    def __init__(self, instance_id=None, region_id=None, user_group_id=None):
        # The ID of the bastion host on which you want to delete the user group.
        # 
        # > You can call the [DescribeInstances](~~153281~~) operation to query the ID of the bastion host.
        self.instance_id = instance_id  # type: str
        # The region ID of the bastion host on which you want to delete the user group.
        # 
        # > For more information about the mapping between region IDs and region names, see [Regions and zones](~~40654~~).
        self.region_id = region_id  # type: str
        # The ID of the user group that you want to delete.
        # 
        # > You can call the [ListUserGroups](~~204509~~) operation to query the ID of the user group.
        self.user_group_id = user_group_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteUserGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.user_group_id is not None:
            result['UserGroupId'] = self.user_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('UserGroupId') is not None:
            self.user_group_id = m.get('UserGroupId')
        return self


class DeleteUserGroupResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteUserGroupResponseBody, self).to_map()
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


class DeleteUserGroupResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteUserGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteUserGroupResponse, self).to_map()
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
            temp_model = DeleteUserGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteUserPublicKeyRequest(TeaModel):
    def __init__(self, instance_id=None, public_key_id=None, region_id=None):
        # The region ID of the bastion host on which you want to delete the public key from the user.
        # 
        # > You can call the [DescribeInstances](~~153281~~) operation to query the ID of the bastion host.
        self.instance_id = instance_id  # type: str
        # The ID of the public key.
        self.public_key_id = public_key_id  # type: str
        # The region ID of the bastion host. For more information about the mapping between region IDs and region names, see [Regions and zones](~~40654~~).
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteUserPublicKeyRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.public_key_id is not None:
            result['PublicKeyId'] = self.public_key_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('PublicKeyId') is not None:
            self.public_key_id = m.get('PublicKeyId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DeleteUserPublicKeyResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DeleteUserPublicKeyResponseBody, self).to_map()
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


class DeleteUserPublicKeyResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DeleteUserPublicKeyResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DeleteUserPublicKeyResponse, self).to_map()
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
            temp_model = DeleteUserPublicKeyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeInstanceAttributeRequest(TeaModel):
    def __init__(self, instance_id=None, region_id=None):
        self.instance_id = instance_id  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeInstanceAttributeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeInstanceAttributeResponseBodyInstanceAttributePorts(TeaModel):
    def __init__(self, custom_port=None, standard_port=None):
        # The custom port.
        # 
        # >  You can change only the SSH and RDP ports. If O\&M ports are not specified, the value of the StandardPort parameter is returned.
        self.custom_port = custom_port  # type: int
        # The standard port of the bastion host. Valid values:
        # 
        # *   **SSH**: 60022
        # *   **RDP**: 63389
        # *   **HTTPS**: 443
        self.standard_port = standard_port  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeInstanceAttributeResponseBodyInstanceAttributePorts, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.custom_port is not None:
            result['CustomPort'] = self.custom_port
        if self.standard_port is not None:
            result['StandardPort'] = self.standard_port
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CustomPort') is not None:
            self.custom_port = m.get('CustomPort')
        if m.get('StandardPort') is not None:
            self.standard_port = m.get('StandardPort')
        return self


class DescribeInstanceAttributeResponseBodyInstanceAttribute(TeaModel):
    def __init__(self, authorized_security_groups=None, bandwidth=None, bandwidth_package=None,
                 db_operation_module=None, description=None, eni_instance_id=None, expire_time=None, instance_id=None,
                 instance_status=None, internet_endpoint=None, intranet_endpoint=None, license_code=None,
                 modify_password_module=None, network_proxy_module=None, ports=None, private_export_ips=None, private_white_list=None,
                 public_export_ips=None, public_ips=None, public_network_access=None, public_white_list=None, region_id=None,
                 resource_group_id=None, security_group_ids=None, start_time=None, storage=None, vpc_id=None, vswitch_id=None,
                 web_terminal_module=None):
        self.authorized_security_groups = authorized_security_groups  # type: list[str]
        # The total bandwidth of the bastion host.
        self.bandwidth = bandwidth  # type: str
        # The extra bandwidth plan of the bastion host.
        self.bandwidth_package = bandwidth_package  # type: str
        self.db_operation_module = db_operation_module  # type: str
        self.description = description  # type: str
        self.eni_instance_id = eni_instance_id  # type: str
        self.expire_time = expire_time  # type: long
        self.instance_id = instance_id  # type: str
        self.instance_status = instance_status  # type: str
        self.internet_endpoint = internet_endpoint  # type: str
        self.intranet_endpoint = intranet_endpoint  # type: str
        self.license_code = license_code  # type: str
        self.modify_password_module = modify_password_module  # type: str
        self.network_proxy_module = network_proxy_module  # type: str
        self.ports = ports  # type: list[DescribeInstanceAttributeResponseBodyInstanceAttributePorts]
        self.private_export_ips = private_export_ips  # type: list[str]
        self.private_white_list = private_white_list  # type: list[str]
        self.public_export_ips = public_export_ips  # type: list[str]
        self.public_ips = public_ips  # type: list[str]
        self.public_network_access = public_network_access  # type: bool
        self.public_white_list = public_white_list  # type: list[str]
        self.region_id = region_id  # type: str
        self.resource_group_id = resource_group_id  # type: str
        self.security_group_ids = security_group_ids  # type: list[str]
        self.start_time = start_time  # type: long
        self.storage = storage  # type: long
        self.vpc_id = vpc_id  # type: str
        self.vswitch_id = vswitch_id  # type: str
        self.web_terminal_module = web_terminal_module  # type: str

    def validate(self):
        if self.ports:
            for k in self.ports:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeInstanceAttributeResponseBodyInstanceAttribute, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.authorized_security_groups is not None:
            result['AuthorizedSecurityGroups'] = self.authorized_security_groups
        if self.bandwidth is not None:
            result['Bandwidth'] = self.bandwidth
        if self.bandwidth_package is not None:
            result['BandwidthPackage'] = self.bandwidth_package
        if self.db_operation_module is not None:
            result['DbOperationModule'] = self.db_operation_module
        if self.description is not None:
            result['Description'] = self.description
        if self.eni_instance_id is not None:
            result['EniInstanceId'] = self.eni_instance_id
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_status is not None:
            result['InstanceStatus'] = self.instance_status
        if self.internet_endpoint is not None:
            result['InternetEndpoint'] = self.internet_endpoint
        if self.intranet_endpoint is not None:
            result['IntranetEndpoint'] = self.intranet_endpoint
        if self.license_code is not None:
            result['LicenseCode'] = self.license_code
        if self.modify_password_module is not None:
            result['ModifyPasswordModule'] = self.modify_password_module
        if self.network_proxy_module is not None:
            result['NetworkProxyModule'] = self.network_proxy_module
        result['Ports'] = []
        if self.ports is not None:
            for k in self.ports:
                result['Ports'].append(k.to_map() if k else None)
        if self.private_export_ips is not None:
            result['PrivateExportIps'] = self.private_export_ips
        if self.private_white_list is not None:
            result['PrivateWhiteList'] = self.private_white_list
        if self.public_export_ips is not None:
            result['PublicExportIps'] = self.public_export_ips
        if self.public_ips is not None:
            result['PublicIps'] = self.public_ips
        if self.public_network_access is not None:
            result['PublicNetworkAccess'] = self.public_network_access
        if self.public_white_list is not None:
            result['PublicWhiteList'] = self.public_white_list
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.security_group_ids is not None:
            result['SecurityGroupIds'] = self.security_group_ids
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.storage is not None:
            result['Storage'] = self.storage
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.vswitch_id is not None:
            result['VswitchId'] = self.vswitch_id
        if self.web_terminal_module is not None:
            result['WebTerminalModule'] = self.web_terminal_module
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AuthorizedSecurityGroups') is not None:
            self.authorized_security_groups = m.get('AuthorizedSecurityGroups')
        if m.get('Bandwidth') is not None:
            self.bandwidth = m.get('Bandwidth')
        if m.get('BandwidthPackage') is not None:
            self.bandwidth_package = m.get('BandwidthPackage')
        if m.get('DbOperationModule') is not None:
            self.db_operation_module = m.get('DbOperationModule')
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('EniInstanceId') is not None:
            self.eni_instance_id = m.get('EniInstanceId')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceStatus') is not None:
            self.instance_status = m.get('InstanceStatus')
        if m.get('InternetEndpoint') is not None:
            self.internet_endpoint = m.get('InternetEndpoint')
        if m.get('IntranetEndpoint') is not None:
            self.intranet_endpoint = m.get('IntranetEndpoint')
        if m.get('LicenseCode') is not None:
            self.license_code = m.get('LicenseCode')
        if m.get('ModifyPasswordModule') is not None:
            self.modify_password_module = m.get('ModifyPasswordModule')
        if m.get('NetworkProxyModule') is not None:
            self.network_proxy_module = m.get('NetworkProxyModule')
        self.ports = []
        if m.get('Ports') is not None:
            for k in m.get('Ports'):
                temp_model = DescribeInstanceAttributeResponseBodyInstanceAttributePorts()
                self.ports.append(temp_model.from_map(k))
        if m.get('PrivateExportIps') is not None:
            self.private_export_ips = m.get('PrivateExportIps')
        if m.get('PrivateWhiteList') is not None:
            self.private_white_list = m.get('PrivateWhiteList')
        if m.get('PublicExportIps') is not None:
            self.public_export_ips = m.get('PublicExportIps')
        if m.get('PublicIps') is not None:
            self.public_ips = m.get('PublicIps')
        if m.get('PublicNetworkAccess') is not None:
            self.public_network_access = m.get('PublicNetworkAccess')
        if m.get('PublicWhiteList') is not None:
            self.public_white_list = m.get('PublicWhiteList')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('SecurityGroupIds') is not None:
            self.security_group_ids = m.get('SecurityGroupIds')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('Storage') is not None:
            self.storage = m.get('Storage')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('VswitchId') is not None:
            self.vswitch_id = m.get('VswitchId')
        if m.get('WebTerminalModule') is not None:
            self.web_terminal_module = m.get('WebTerminalModule')
        return self


class DescribeInstanceAttributeResponseBody(TeaModel):
    def __init__(self, instance_attribute=None, request_id=None):
        # The attribute information about the bastion host.
        self.instance_attribute = instance_attribute  # type: DescribeInstanceAttributeResponseBodyInstanceAttribute
        self.request_id = request_id  # type: str

    def validate(self):
        if self.instance_attribute:
            self.instance_attribute.validate()

    def to_map(self):
        _map = super(DescribeInstanceAttributeResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_attribute is not None:
            result['InstanceAttribute'] = self.instance_attribute.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceAttribute') is not None:
            temp_model = DescribeInstanceAttributeResponseBodyInstanceAttribute()
            self.instance_attribute = temp_model.from_map(m['InstanceAttribute'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DescribeInstanceAttributeResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeInstanceAttributeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeInstanceAttributeResponse, self).to_map()
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
            temp_model = DescribeInstanceAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeInstancesRequestTag(TeaModel):
    def __init__(self, key=None, value=None):
        # The key of the tag.
        self.key = key  # type: str
        # The value of the tag.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeInstancesRequestTag, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class DescribeInstancesRequest(TeaModel):
    def __init__(self, instance_id=None, instance_status=None, page_number=None, page_size=None, region_id=None,
                 resource_group_id=None, tag=None):
        # An array that consists of the IDs of the bastion hosts.
        self.instance_id = instance_id  # type: list[str]
        # The status of the bastion host. Valid values:
        # 
        # *   **PENDING**: The bastion host is not initialized.
        # *   **CREATING**: The bastion host is being created.
        # *   **RUNNING**: The bastion host is running.
        # *   **EXPIRED**: The bastion host expired.
        # *   **CREATE_FAILED**: The bastion host fails to be created.
        # *   **UPGRADING**: The configurations of the bastion host are being changed.
        # *   **UPGRADE_FAILED**: The configurations of the bastion host fail to be changed.
        self.instance_status = instance_status  # type: str
        # The number of the page to return. Default value: **1**.
        self.page_number = page_number  # type: int
        # The number of entries to return on each page. Default value: **10**.
        self.page_size = page_size  # type: int
        # The region ID of the bastion host.
        self.region_id = region_id  # type: str
        # The ID of the resource group to which the bastion host belongs.
        self.resource_group_id = resource_group_id  # type: str
        # An array consisting of the tags that are added to the bastion hosts.
        self.tag = tag  # type: list[DescribeInstancesRequestTag]

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeInstancesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_status is not None:
            result['InstanceStatus'] = self.instance_status
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceStatus') is not None:
            self.instance_status = m.get('InstanceStatus')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = DescribeInstancesRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class DescribeInstancesResponseBodyInstances(TeaModel):
    def __init__(self, description=None, expire_time=None, image_version=None, instance_id=None,
                 instance_status=None, internet_endpoint=None, intranet_endpoint=None, legacy=None, license_code=None,
                 plan_code=None, public_network_access=None, region_id=None, resource_group_id=None, start_time=None,
                 vpc_id=None, vswitch_id=None):
        # The description of the bastion host.
        self.description = description  # type: str
        # The timestamp when the bastion host expires. Unit: milliseconds.
        self.expire_time = expire_time  # type: long
        # The image version of the bastion host.
        self.image_version = image_version  # type: str
        # The ID of the bastion host.
        self.instance_id = instance_id  # type: str
        # The status of the bastion host. Valid values:
        # 
        # *   **PENDING**: The bastion host is not initialized.
        # *   **CREATING**: The bastion host is being created.
        # *   **RUNNING**: The bastion host is running.
        # *   **EXPIRED**: The bastion host expired.
        # *   **CREATE_FAILED**: The bastion host fails to be created.
        # *   **UPGRADING**: The configurations of the bastion host are being changed.
        # *   **UPGRADE_FAILED**: The configurations of the bastion host fail to be changed.
        self.instance_status = instance_status  # type: str
        # The public O\&M address of the bastion host.
        self.internet_endpoint = internet_endpoint  # type: str
        # The private O\&M address of the bastion host.
        self.intranet_endpoint = intranet_endpoint  # type: str
        # Indicates whether the bastion host runs an earlier version. Valid values:
        # 
        # *   **true**: indicates that the bastion host runs V2 or V3.1.
        # *   **false**:indicates that the bastion host runs V3.2.
        self.legacy = legacy  # type: bool
        # The license code of the bastion host.
        self.license_code = license_code  # type: str
        # The edition of the bastion host. Valid values:
        # 
        # *   **cloudbastion**: Basic
        # *   **cloudbastion_ha**: Enterprise
        self.plan_code = plan_code  # type: str
        # Indicates whether the bastion host can be accessed from the Internet. Valid values:
        # 
        # *   **true**: The bastion host can be accessed from the Internet.
        # *   **false**: The bastion host cannot be accessed from the Internet.
        self.public_network_access = public_network_access  # type: bool
        # The region ID of the bastion host.
        self.region_id = region_id  # type: str
        # The ID of the resource group to which the bastion host belongs.
        self.resource_group_id = resource_group_id  # type: str
        # The timestamp when the bastion host is purchased or renewed. Unit: milliseconds.
        self.start_time = start_time  # type: long
        # The ID of the virtual private cloud (VPC) to which the bastion host belongs.
        self.vpc_id = vpc_id  # type: str
        # The ID of the vSwitch to which the bastion host belongs.
        self.vswitch_id = vswitch_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeInstancesResponseBodyInstances, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.expire_time is not None:
            result['ExpireTime'] = self.expire_time
        if self.image_version is not None:
            result['ImageVersion'] = self.image_version
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.instance_status is not None:
            result['InstanceStatus'] = self.instance_status
        if self.internet_endpoint is not None:
            result['InternetEndpoint'] = self.internet_endpoint
        if self.intranet_endpoint is not None:
            result['IntranetEndpoint'] = self.intranet_endpoint
        if self.legacy is not None:
            result['Legacy'] = self.legacy
        if self.license_code is not None:
            result['LicenseCode'] = self.license_code
        if self.plan_code is not None:
            result['PlanCode'] = self.plan_code
        if self.public_network_access is not None:
            result['PublicNetworkAccess'] = self.public_network_access
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.start_time is not None:
            result['StartTime'] = self.start_time
        if self.vpc_id is not None:
            result['VpcId'] = self.vpc_id
        if self.vswitch_id is not None:
            result['VswitchId'] = self.vswitch_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('ExpireTime') is not None:
            self.expire_time = m.get('ExpireTime')
        if m.get('ImageVersion') is not None:
            self.image_version = m.get('ImageVersion')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('InstanceStatus') is not None:
            self.instance_status = m.get('InstanceStatus')
        if m.get('InternetEndpoint') is not None:
            self.internet_endpoint = m.get('InternetEndpoint')
        if m.get('IntranetEndpoint') is not None:
            self.intranet_endpoint = m.get('IntranetEndpoint')
        if m.get('Legacy') is not None:
            self.legacy = m.get('Legacy')
        if m.get('LicenseCode') is not None:
            self.license_code = m.get('LicenseCode')
        if m.get('PlanCode') is not None:
            self.plan_code = m.get('PlanCode')
        if m.get('PublicNetworkAccess') is not None:
            self.public_network_access = m.get('PublicNetworkAccess')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('StartTime') is not None:
            self.start_time = m.get('StartTime')
        if m.get('VpcId') is not None:
            self.vpc_id = m.get('VpcId')
        if m.get('VswitchId') is not None:
            self.vswitch_id = m.get('VswitchId')
        return self


class DescribeInstancesResponseBody(TeaModel):
    def __init__(self, instances=None, request_id=None, total_count=None):
        # An array that consists of the queried bastion hosts.
        self.instances = instances  # type: list[DescribeInstancesResponseBodyInstances]
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id  # type: str
        # The total number of bastion hosts that are queried.
        self.total_count = total_count  # type: long

    def validate(self):
        if self.instances:
            for k in self.instances:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DescribeInstancesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Instances'] = []
        if self.instances is not None:
            for k in self.instances:
                result['Instances'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.instances = []
        if m.get('Instances') is not None:
            for k in m.get('Instances'):
                temp_model = DescribeInstancesResponseBodyInstances()
                self.instances.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class DescribeInstancesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DescribeInstancesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DescribeInstancesResponse, self).to_map()
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
            temp_model = DescribeInstancesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRegionsRequest(TeaModel):
    def __init__(self, accept_language=None, region_id=None):
        # The ID of the region.
        self.accept_language = accept_language  # type: str
        # The ID of request.
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DescribeRegionsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.accept_language is not None:
            result['AcceptLanguage'] = self.accept_language
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AcceptLanguage') is not None:
            self.accept_language = m.get('AcceptLanguage')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DescribeRegionsResponseBodyRegions(TeaModel):
    def __init__(self, local_name=None, region_endpoint=None, region_id=None):
        self.local_name = local_name  # type: str
        self.region_endpoint = region_endpoint  # type: str
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
        # DescribeRegions
        self.regions = regions  # type: list[DescribeRegionsResponseBodyRegions]
        # Queries available regions where you can create bastion hosts.
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


class DetachHostAccountsFromHostShareKeyRequest(TeaModel):
    def __init__(self, host_account_ids=None, host_share_key_id=None, instance_id=None, region_id=None):
        # The IDs of the host accounts.
        self.host_account_ids = host_account_ids  # type: str
        # The ID of the shared key.
        self.host_share_key_id = host_share_key_id  # type: str
        # The ID of the bastion host. You can call the [DescribeInstances](~~153281~~) operation to query the ID of the bastion host.
        self.instance_id = instance_id  # type: str
        # The region ID of the bastion host. For more information about the mapping between region IDs and region names, see [Regions and zones](~~40654~~).
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DetachHostAccountsFromHostShareKeyRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.host_account_ids is not None:
            result['HostAccountIds'] = self.host_account_ids
        if self.host_share_key_id is not None:
            result['HostShareKeyId'] = self.host_share_key_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('HostAccountIds') is not None:
            self.host_account_ids = m.get('HostAccountIds')
        if m.get('HostShareKeyId') is not None:
            self.host_share_key_id = m.get('HostShareKeyId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DetachHostAccountsFromHostShareKeyResponseBodyResults(TeaModel):
    def __init__(self, code=None, host_account_id=None, host_share_key_id=None, message=None):
        # The error code returned. If **OK** is returned, the disassociation was successful. If a different error code is returned, the disassociation failed.
        self.code = code  # type: str
        # The ID of the host account.
        self.host_account_id = host_account_id  # type: str
        # The ID of the shared key.
        self.host_share_key_id = host_share_key_id  # type: str
        # The error message returned.
        self.message = message  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DetachHostAccountsFromHostShareKeyResponseBodyResults, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.host_account_id is not None:
            result['HostAccountId'] = self.host_account_id
        if self.host_share_key_id is not None:
            result['HostShareKeyId'] = self.host_share_key_id
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('HostAccountId') is not None:
            self.host_account_id = m.get('HostAccountId')
        if m.get('HostShareKeyId') is not None:
            self.host_share_key_id = m.get('HostShareKeyId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class DetachHostAccountsFromHostShareKeyResponseBody(TeaModel):
    def __init__(self, request_id=None, results=None):
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id  # type: str
        # The result of the call.
        self.results = results  # type: list[DetachHostAccountsFromHostShareKeyResponseBodyResults]

    def validate(self):
        if self.results:
            for k in self.results:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DetachHostAccountsFromHostShareKeyResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Results'] = []
        if self.results is not None:
            for k in self.results:
                result['Results'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.results = []
        if m.get('Results') is not None:
            for k in m.get('Results'):
                temp_model = DetachHostAccountsFromHostShareKeyResponseBodyResults()
                self.results.append(temp_model.from_map(k))
        return self


class DetachHostAccountsFromHostShareKeyResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DetachHostAccountsFromHostShareKeyResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DetachHostAccountsFromHostShareKeyResponse, self).to_map()
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
            temp_model = DetachHostAccountsFromHostShareKeyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DetachHostAccountsFromUserRequest(TeaModel):
    def __init__(self, hosts=None, instance_id=None, region_id=None, user_id=None):
        # The IDs of the host and host account on which you want to revoke permissions from the user. You can specify up to 10 host IDs and up to 10 host account IDs for each host. You can specify only host IDs. In this case, the permissions on both the specified hosts and all host accounts of the hosts are revoked from the user. For more information about this parameter, see the "Description of the Hosts parameter" section of this topic.
        # 
        # >  You can call the [ListHosts](~~200665~~) operation to query the ID of the host and the [ListHostAccounts](~~204372~~) operation to query the ID of the host account.
        self.hosts = hosts  # type: str
        # The ID of the bastion host in which you want to revoke permissions on the specified hosts and host accounts from the user.
        # 
        # >  You can call the [DescribeInstances](~~153281~~) operation to query the ID of the bastion host.
        self.instance_id = instance_id  # type: str
        # The region ID of the bastion host in which you want to revoke permissions on the specified hosts and host accounts from the user.
        # 
        # >  For more information about the mapping between region IDs and region names, see [Regions and zones](~~40654~~).
        self.region_id = region_id  # type: str
        # The ID of the user from which you want to revoke permissions on the specified hosts and host accounts.
        # 
        # >  You can call the [ListUsers](~~204522~~) operation to query the ID of the user.
        self.user_id = user_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DetachHostAccountsFromUserRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.hosts is not None:
            result['Hosts'] = self.hosts
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Hosts') is not None:
            self.hosts = m.get('Hosts')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class DetachHostAccountsFromUserResponseBodyResultsHostAccounts(TeaModel):
    def __init__(self, code=None, host_account_id=None, message=None):
        # The return code that indicates whether permissions on the specified host account were revoked from the user. Valid values:
        # 
        # *   **OK**: The call was successful.
        # *   **UNEXPECTED**: An unknown error occurred.
        # *   **INVALID_ARGUMENT**: A request parameter is invalid.
        # *   **OBJECT_NOT_FOUND**: The specified object on which you want to perform the operation does not exist.
        # *   **OBJECT_AlREADY_EXISTS**: The specified object on which you want to perform the operation already exists.
        self.code = code  # type: str
        # The ID of the host account.
        self.host_account_id = host_account_id  # type: str
        # This parameter is deprecated.
        self.message = message  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DetachHostAccountsFromUserResponseBodyResultsHostAccounts, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.host_account_id is not None:
            result['HostAccountId'] = self.host_account_id
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('HostAccountId') is not None:
            self.host_account_id = m.get('HostAccountId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class DetachHostAccountsFromUserResponseBodyResults(TeaModel):
    def __init__(self, code=None, host_accounts=None, host_id=None, message=None, user_id=None):
        # The return code that indicates whether the call was successful. Valid values:
        # 
        # *   **OK**: The call was successful.
        # *   **UNEXPECTED**: An unknown error occurred.
        # *   **INVALID_ARGUMENT**: A request parameter is invalid.
        # *   **OBJECT_NOT_FOUND**: The specified object on which you want to perform the operation does not exist.
        # *   **OBJECT_AlREADY_EXISTS**: The specified object on which you want to perform the operation already exists.
        self.code = code  # type: str
        # The result of revoking permissions on the specified host accounts from the user.
        self.host_accounts = host_accounts  # type: list[DetachHostAccountsFromUserResponseBodyResultsHostAccounts]
        # The ID of the host.
        self.host_id = host_id  # type: str
        # This parameter is deprecated.
        self.message = message  # type: str
        # The ID of the user.
        self.user_id = user_id  # type: str

    def validate(self):
        if self.host_accounts:
            for k in self.host_accounts:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DetachHostAccountsFromUserResponseBodyResults, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['HostAccounts'] = []
        if self.host_accounts is not None:
            for k in self.host_accounts:
                result['HostAccounts'].append(k.to_map() if k else None)
        if self.host_id is not None:
            result['HostId'] = self.host_id
        if self.message is not None:
            result['Message'] = self.message
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.host_accounts = []
        if m.get('HostAccounts') is not None:
            for k in m.get('HostAccounts'):
                temp_model = DetachHostAccountsFromUserResponseBodyResultsHostAccounts()
                self.host_accounts.append(temp_model.from_map(k))
        if m.get('HostId') is not None:
            self.host_id = m.get('HostId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class DetachHostAccountsFromUserResponseBody(TeaModel):
    def __init__(self, request_id=None, results=None):
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The result of the call.
        self.results = results  # type: list[DetachHostAccountsFromUserResponseBodyResults]

    def validate(self):
        if self.results:
            for k in self.results:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DetachHostAccountsFromUserResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Results'] = []
        if self.results is not None:
            for k in self.results:
                result['Results'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.results = []
        if m.get('Results') is not None:
            for k in m.get('Results'):
                temp_model = DetachHostAccountsFromUserResponseBodyResults()
                self.results.append(temp_model.from_map(k))
        return self


class DetachHostAccountsFromUserResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DetachHostAccountsFromUserResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DetachHostAccountsFromUserResponse, self).to_map()
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
            temp_model = DetachHostAccountsFromUserResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DetachHostAccountsFromUserGroupRequest(TeaModel):
    def __init__(self, hosts=None, instance_id=None, region_id=None, user_group_id=None):
        # The IDs of the host and host account on which you want to revoke permissions from the user group.
        # 
        # You can specify up to 10 host IDs and up to 10 host account IDs for each host. You can specify only host IDs. In this case, the permissions on both the specified hosts and all host accounts of the hosts are revoked from the user group. For more information about this parameter, see the "Description of the Hosts parameter" section of this topic.
        # 
        # >  You can call the [ListHosts](~~200665~~) operation to query the ID of the host and the [ListHostAccounts](~~204372~~) operation to query the ID of the host account.
        self.hosts = hosts  # type: str
        # The ID of the bastion host in which you want to revoke permissions on the specified hosts and host accounts from the user group.
        # 
        # >  You can call the [DescribeInstances](~~153281~~) operation to query the ID of the bastion host.
        self.instance_id = instance_id  # type: str
        # The region ID of the bastion host in which you want to revoke permissions on the specified hosts and host accounts from the user group.
        # 
        # >  For more information about the mapping between region IDs and region names, see [Regions and zones](~~40654~~).
        self.region_id = region_id  # type: str
        # The ID of the user group from which you want to revoke permissions on the specified hosts and host accounts.
        # 
        # >  You can call the [ListUserGroups](~~204509~~) operation to query the ID of the user group.
        self.user_group_id = user_group_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DetachHostAccountsFromUserGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.hosts is not None:
            result['Hosts'] = self.hosts
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.user_group_id is not None:
            result['UserGroupId'] = self.user_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Hosts') is not None:
            self.hosts = m.get('Hosts')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('UserGroupId') is not None:
            self.user_group_id = m.get('UserGroupId')
        return self


class DetachHostAccountsFromUserGroupResponseBodyResultsHostAccounts(TeaModel):
    def __init__(self, code=None, host_account_id=None, message=None):
        # The return code that indicates whether permissions on the specified host account were revoked from the user group. Valid values:
        # 
        # *   **OK**: The call was successful.
        # *   **UNEXPECTED**: An unknown error occurred.
        # *   **INVALID_ARGUMENT**: A request parameter is invalid.
        # *   **OBJECT_NOT_FOUND**: The specified object on which you want to perform the operation does not exist.
        # *   **OBJECT_AlREADY_EXISTS**: The specified object on which you want to perform the operation already exists.
        self.code = code  # type: str
        # The ID of the host account.
        self.host_account_id = host_account_id  # type: str
        # This parameter is deprecated.
        self.message = message  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DetachHostAccountsFromUserGroupResponseBodyResultsHostAccounts, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.host_account_id is not None:
            result['HostAccountId'] = self.host_account_id
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('HostAccountId') is not None:
            self.host_account_id = m.get('HostAccountId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class DetachHostAccountsFromUserGroupResponseBodyResults(TeaModel):
    def __init__(self, code=None, host_accounts=None, host_id=None, message=None, user_group_id=None):
        # The return code that indicates whether the call was successful. Valid values:
        # 
        # *   **OK**: The call was successful.
        # *   **UNEXPECTED**: An unknown error occurred.
        # *   **INVALID_ARGUMENT**: A request parameter is invalid.
        # *   **OBJECT_NOT_FOUND**: The specified object on which you want to perform the operation does not exist.
        # *   **OBJECT_AlREADY_EXISTS**: The specified object on which you want to perform the operation already exists.
        self.code = code  # type: str
        # The result of revoking permissions on the specified host accounts from the user group.
        self.host_accounts = host_accounts  # type: list[DetachHostAccountsFromUserGroupResponseBodyResultsHostAccounts]
        # The ID of the host.
        self.host_id = host_id  # type: str
        # This parameter is deprecated.
        self.message = message  # type: str
        # The ID of the group.
        self.user_group_id = user_group_id  # type: str

    def validate(self):
        if self.host_accounts:
            for k in self.host_accounts:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DetachHostAccountsFromUserGroupResponseBodyResults, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['HostAccounts'] = []
        if self.host_accounts is not None:
            for k in self.host_accounts:
                result['HostAccounts'].append(k.to_map() if k else None)
        if self.host_id is not None:
            result['HostId'] = self.host_id
        if self.message is not None:
            result['Message'] = self.message
        if self.user_group_id is not None:
            result['UserGroupId'] = self.user_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.host_accounts = []
        if m.get('HostAccounts') is not None:
            for k in m.get('HostAccounts'):
                temp_model = DetachHostAccountsFromUserGroupResponseBodyResultsHostAccounts()
                self.host_accounts.append(temp_model.from_map(k))
        if m.get('HostId') is not None:
            self.host_id = m.get('HostId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('UserGroupId') is not None:
            self.user_group_id = m.get('UserGroupId')
        return self


class DetachHostAccountsFromUserGroupResponseBody(TeaModel):
    def __init__(self, request_id=None, results=None):
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The result of the call.
        self.results = results  # type: list[DetachHostAccountsFromUserGroupResponseBodyResults]

    def validate(self):
        if self.results:
            for k in self.results:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DetachHostAccountsFromUserGroupResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Results'] = []
        if self.results is not None:
            for k in self.results:
                result['Results'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.results = []
        if m.get('Results') is not None:
            for k in m.get('Results'):
                temp_model = DetachHostAccountsFromUserGroupResponseBodyResults()
                self.results.append(temp_model.from_map(k))
        return self


class DetachHostAccountsFromUserGroupResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DetachHostAccountsFromUserGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DetachHostAccountsFromUserGroupResponse, self).to_map()
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
            temp_model = DetachHostAccountsFromUserGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DetachHostGroupAccountsFromUserRequest(TeaModel):
    def __init__(self, host_groups=None, instance_id=None, region_id=None, user_id=None):
        # The ID of the host group and the name of the host account on which you want to revoke permissions from the user. You can specify up to 10 host group IDs and up to 10 host account names for each host group. You can specify only host group IDs. In this case, the permissions on the specified host groups and all host accounts in the host groups are revoked from the user. For more information about this parameter, see the "Description of the HostGroups parameter" section of this topic.
        # 
        # > You can call the [ListHostGroups](~~201307~~) operation to query the ID of the host group and the [ListHostAccounts](~~204372~~) operation to query the name of the host account.
        self.host_groups = host_groups  # type: str
        # The ID of the bastion host for which you want to revoke permissions on the specified host groups and host accounts from the user.
        # 
        # > You can call the [DescribeInstances](~~153281~~) operation to query the ID of the bastion host.
        self.instance_id = instance_id  # type: str
        # The region ID of the bastion host for which you want to revoke permissions on the specified host groups and host accounts from the user.
        # 
        # > For more information about the mapping between region IDs and region names, see [Regions and zones](~~40654~~).
        self.region_id = region_id  # type: str
        # The ID of the user from which you want to revoke permissions on the specified host groups and host accounts.
        # 
        # > You can call the [ListUsers](~~204522~~) operation to query the ID of the user.
        self.user_id = user_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DetachHostGroupAccountsFromUserRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.host_groups is not None:
            result['HostGroups'] = self.host_groups
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('HostGroups') is not None:
            self.host_groups = m.get('HostGroups')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class DetachHostGroupAccountsFromUserResponseBodyResultsHostAccountNames(TeaModel):
    def __init__(self, code=None, host_account_name=None, message=None):
        # The return code that indicates whether permissions on the specified host account were revoked from the user. Valid values:
        # 
        # *   **OK**: The call was successful.
        # *   **UNEXPECTED**: An unknown error occurred.
        # *   **INVALID_ARGUMENT**: A request parameter is invalid.
        # *   **OBJECT_NOT_FOUND**: The specified object on which you want to perform the operation does not exist.
        # *   **OBJECT_AlREADY_EXISTS**: The specified object on which you want to perform the operation already exists.
        self.code = code  # type: str
        # The name of the host account.
        self.host_account_name = host_account_name  # type: str
        # This parameter is deprecated.
        self.message = message  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DetachHostGroupAccountsFromUserResponseBodyResultsHostAccountNames, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.host_account_name is not None:
            result['HostAccountName'] = self.host_account_name
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('HostAccountName') is not None:
            self.host_account_name = m.get('HostAccountName')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class DetachHostGroupAccountsFromUserResponseBodyResults(TeaModel):
    def __init__(self, code=None, host_account_names=None, host_group_id=None, message=None, user_id=None):
        # The return code that indicates whether the call was successful. Valid values:
        # 
        # *   **OK**: The call was successful.
        # *   **UNEXPECTED**: An unknown error occurred.
        # *   **INVALID_ARGUMENT**: A request parameter is invalid.
        # *   **OBJECT_NOT_FOUND**: The specified object on which you want to perform the operation does not exist.
        # *   **OBJECT_AlREADY_EXISTS**: The specified object on which you want to perform the operation already exists.
        self.code = code  # type: str
        # The result of revoking permissions on the specified host accounts from the user.
        self.host_account_names = host_account_names  # type: list[DetachHostGroupAccountsFromUserResponseBodyResultsHostAccountNames]
        # The ID of the host group.
        self.host_group_id = host_group_id  # type: str
        # This parameter is deprecated.
        self.message = message  # type: str
        # The ID of the user.
        self.user_id = user_id  # type: str

    def validate(self):
        if self.host_account_names:
            for k in self.host_account_names:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DetachHostGroupAccountsFromUserResponseBodyResults, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['HostAccountNames'] = []
        if self.host_account_names is not None:
            for k in self.host_account_names:
                result['HostAccountNames'].append(k.to_map() if k else None)
        if self.host_group_id is not None:
            result['HostGroupId'] = self.host_group_id
        if self.message is not None:
            result['Message'] = self.message
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.host_account_names = []
        if m.get('HostAccountNames') is not None:
            for k in m.get('HostAccountNames'):
                temp_model = DetachHostGroupAccountsFromUserResponseBodyResultsHostAccountNames()
                self.host_account_names.append(temp_model.from_map(k))
        if m.get('HostGroupId') is not None:
            self.host_group_id = m.get('HostGroupId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class DetachHostGroupAccountsFromUserResponseBody(TeaModel):
    def __init__(self, request_id=None, results=None):
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The result of the call.
        self.results = results  # type: list[DetachHostGroupAccountsFromUserResponseBodyResults]

    def validate(self):
        if self.results:
            for k in self.results:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DetachHostGroupAccountsFromUserResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Results'] = []
        if self.results is not None:
            for k in self.results:
                result['Results'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.results = []
        if m.get('Results') is not None:
            for k in m.get('Results'):
                temp_model = DetachHostGroupAccountsFromUserResponseBodyResults()
                self.results.append(temp_model.from_map(k))
        return self


class DetachHostGroupAccountsFromUserResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DetachHostGroupAccountsFromUserResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DetachHostGroupAccountsFromUserResponse, self).to_map()
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
            temp_model = DetachHostGroupAccountsFromUserResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DetachHostGroupAccountsFromUserGroupRequest(TeaModel):
    def __init__(self, host_groups=None, instance_id=None, region_id=None, user_group_id=None):
        # The ID of the host group and the name of host account on which you want to revoke permissions from the user group. You can specify up to 10 host group IDs and up to 10 host account names for each host group. You can specify only host group IDs. In this case, the permissions on the specified host groups and all host accounts in the host groups are revoked from the user group. For more information about this parameter, see the "Description of the HostGroups parameter" section of this topic.
        # 
        # >  You can call the [ListHostGroups](~~201307~~) operation to query the ID of the host group and the [ListHostAccounts](~~204372~~) operation to query the name of the host account.
        self.host_groups = host_groups  # type: str
        # The ID of the bastion host for which you want to revoke permissions on the specified host groups and host accounts from the user group.
        # 
        # >  You can call the [DescribeInstances](~~153281~~) operation to query the ID of the bastion host.
        self.instance_id = instance_id  # type: str
        # The region ID of the bastion host for which you want to revoke permissions on the specified host groups and host accounts from the user group.
        # 
        # >  For more information about the mapping between region IDs and region names, see [Regions and zones](~~40654~~).
        self.region_id = region_id  # type: str
        # The ID of the user group from which you want to revoke permissions on the specified host groups and host accounts.
        # 
        # >  You can call the [ListUserGroups](~~204509~~) operation to query the ID of the user group.
        self.user_group_id = user_group_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DetachHostGroupAccountsFromUserGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.host_groups is not None:
            result['HostGroups'] = self.host_groups
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.user_group_id is not None:
            result['UserGroupId'] = self.user_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('HostGroups') is not None:
            self.host_groups = m.get('HostGroups')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('UserGroupId') is not None:
            self.user_group_id = m.get('UserGroupId')
        return self


class DetachHostGroupAccountsFromUserGroupResponseBodyResultsHostAccountNames(TeaModel):
    def __init__(self, code=None, host_account_name=None, message=None):
        # The return code that indicates whether permissions on the specified host account were revoked from the specified user group. Valid values:
        # 
        # *   **OK**: The call was successful.
        # *   **UNEXPECTED**: An unknown error occurred.
        # *   **INVALID_ARGUMENT**: A request parameter is invalid.
        # *   **OBJECT_NOT_FOUND**: The specified object on which you want to perform the operation does not exist.
        # *   **OBJECT_AlREADY_EXISTS**: The specified object on which you want to perform the operation already exists.
        self.code = code  # type: str
        # The name of the host account.
        self.host_account_name = host_account_name  # type: str
        # This parameter is deprecated.
        self.message = message  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DetachHostGroupAccountsFromUserGroupResponseBodyResultsHostAccountNames, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.host_account_name is not None:
            result['HostAccountName'] = self.host_account_name
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('HostAccountName') is not None:
            self.host_account_name = m.get('HostAccountName')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class DetachHostGroupAccountsFromUserGroupResponseBodyResults(TeaModel):
    def __init__(self, code=None, host_account_names=None, host_group_id=None, message=None, user_group_id=None):
        # The return code that indicates whether the call was successful. Valid values:
        # 
        # *   **OK**: The call was successful.
        # *   **UNEXPECTED**: An unknown error occurred.
        # *   **INVALID_ARGUMENT**: A request parameter is invalid.
        # *   **OBJECT_NOT_FOUND**: The specified object on which you want to perform the operation does not exist.
        # *   **OBJECT_AlREADY_EXISTS**: The specified object on which you want to perform the operation already exists.
        self.code = code  # type: str
        # The result of revoking permissions on the specified host accounts from the user group.
        self.host_account_names = host_account_names  # type: list[DetachHostGroupAccountsFromUserGroupResponseBodyResultsHostAccountNames]
        # The ID of the host group.
        self.host_group_id = host_group_id  # type: str
        # This parameter is deprecated.
        self.message = message  # type: str
        # The ID of the group.
        self.user_group_id = user_group_id  # type: str

    def validate(self):
        if self.host_account_names:
            for k in self.host_account_names:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DetachHostGroupAccountsFromUserGroupResponseBodyResults, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        result['HostAccountNames'] = []
        if self.host_account_names is not None:
            for k in self.host_account_names:
                result['HostAccountNames'].append(k.to_map() if k else None)
        if self.host_group_id is not None:
            result['HostGroupId'] = self.host_group_id
        if self.message is not None:
            result['Message'] = self.message
        if self.user_group_id is not None:
            result['UserGroupId'] = self.user_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        self.host_account_names = []
        if m.get('HostAccountNames') is not None:
            for k in m.get('HostAccountNames'):
                temp_model = DetachHostGroupAccountsFromUserGroupResponseBodyResultsHostAccountNames()
                self.host_account_names.append(temp_model.from_map(k))
        if m.get('HostGroupId') is not None:
            self.host_group_id = m.get('HostGroupId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('UserGroupId') is not None:
            self.user_group_id = m.get('UserGroupId')
        return self


class DetachHostGroupAccountsFromUserGroupResponseBody(TeaModel):
    def __init__(self, request_id=None, results=None):
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The result of the call.
        self.results = results  # type: list[DetachHostGroupAccountsFromUserGroupResponseBodyResults]

    def validate(self):
        if self.results:
            for k in self.results:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(DetachHostGroupAccountsFromUserGroupResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Results'] = []
        if self.results is not None:
            for k in self.results:
                result['Results'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.results = []
        if m.get('Results') is not None:
            for k in m.get('Results'):
                temp_model = DetachHostGroupAccountsFromUserGroupResponseBodyResults()
                self.results.append(temp_model.from_map(k))
        return self


class DetachHostGroupAccountsFromUserGroupResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DetachHostGroupAccountsFromUserGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DetachHostGroupAccountsFromUserGroupResponse, self).to_map()
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
            temp_model = DetachHostGroupAccountsFromUserGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DisableInstancePublicAccessRequest(TeaModel):
    def __init__(self, instance_id=None, region_id=None):
        # The ID of the bastion host whose Internet access you want to disable.
        # 
        # > You can call the [DescribeInstances](~~153281~~) operation to query the ID of the bastion host.
        self.instance_id = instance_id  # type: str
        # The region ID of the bastion host.
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DisableInstancePublicAccessRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class DisableInstancePublicAccessResponseBody(TeaModel):
    def __init__(self, instance_id=None, request_id=None):
        # The ID of the bastion host whose Internet access is disabled.
        self.instance_id = instance_id  # type: str
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(DisableInstancePublicAccessResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class DisableInstancePublicAccessResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: DisableInstancePublicAccessResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(DisableInstancePublicAccessResponse, self).to_map()
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
            temp_model = DisableInstancePublicAccessResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EnableInstancePublicAccessRequest(TeaModel):
    def __init__(self, instance_id=None, region_id=None):
        # The ID of the bastion host.
        # 
        # >  You can call the [DescribeInstances](~~153281~~) operation to query the ID of the bastion host.
        self.instance_id = instance_id  # type: str
        # The region ID of the bastion host.
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(EnableInstancePublicAccessRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class EnableInstancePublicAccessResponseBody(TeaModel):
    def __init__(self, instance_id=None, request_id=None):
        # The ID of the bastion host whose Internet access is enabled.
        self.instance_id = instance_id  # type: str
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(EnableInstancePublicAccessResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class EnableInstancePublicAccessResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: EnableInstancePublicAccessResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(EnableInstancePublicAccessResponse, self).to_map()
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
            temp_model = EnableInstancePublicAccessResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetHostRequest(TeaModel):
    def __init__(self, host_id=None, instance_id=None, region_id=None):
        # The protocol that is used to connect to the host. Valid values:
        # 
        # *   **SSH**\
        # *   **RDP**\
        self.host_id = host_id  # type: str
        # The ID of the host that you want to query. You can specify only one host ID.
        # 
        # >  You can call the [ListHosts](~~200665~~) operation to query the ID of the host.
        self.instance_id = instance_id  # type: str
        # The name of the host.
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetHostRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.host_id is not None:
            result['HostId'] = self.host_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('HostId') is not None:
            self.host_id = m.get('HostId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class GetHostResponseBodyHostProtocols(TeaModel):
    def __init__(self, host_finger_print=None, port=None, protocol_name=None):
        # WB662865
        self.host_finger_print = host_finger_print  # type: str
        # GetHost
        self.port = port  # type: int
        self.protocol_name = protocol_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetHostResponseBodyHostProtocols, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.host_finger_print is not None:
            result['HostFingerPrint'] = self.host_finger_print
        if self.port is not None:
            result['Port'] = self.port
        if self.protocol_name is not None:
            result['ProtocolName'] = self.protocol_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('HostFingerPrint') is not None:
            self.host_finger_print = m.get('HostFingerPrint')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('ProtocolName') is not None:
            self.protocol_name = m.get('ProtocolName')
        return self


class GetHostResponseBodyHost(TeaModel):
    def __init__(self, active_address_type=None, comment=None, host_id=None, host_name=None,
                 host_private_address=None, host_public_address=None, network_domain_id=None, ostype=None, protocols=None, source=None,
                 source_instance_id=None, source_instance_state=None):
        # The public endpoint of the host. You can set this parameter to a domain name or an IP address.
        self.active_address_type = active_address_type  # type: str
        # The ID of the ECS instance or dedicated cluster host that was queried.
        # 
        # >  No value is returned for this parameter if the **Source** parameter is set to **Local**.
        self.comment = comment  # type: str
        # The ID of the request.
        self.host_id = host_id  # type: str
        # The ID of the Bastionhost instance where you want to query the host.
        # 
        # >  You can call the [DescribeInstances](~~153281~~) operation to query the ID of the Bastionhost instance.
        self.host_name = host_name  # type: str
        # The description of the host.
        self.host_private_address = host_private_address  # type: str
        # The status of the host. Valid values:
        # 
        # - **Normal**: The host is normal.
        # 
        # - **Release**: The host is released.
        self.host_public_address = host_public_address  # type: str
        self.network_domain_id = network_domain_id  # type: str
        # The operating system of the host. Valid values:
        # 
        # *   **Linux**\
        # *   **Windows**\
        self.ostype = ostype  # type: str
        # GetHost
        self.protocols = protocols  # type: list[GetHostResponseBodyHostProtocols]
        # The protocol information of the host.
        self.source = source  # type: str
        # Queries the details of a specified host, such as the name, source, endpoint, protocol, and service port of the host.
        self.source_instance_id = source_instance_id  # type: str
        # All Alibaba Cloud API operations must include common request parameters. For more information about common request parameters, see [Common parameters](~~315526~~).
        # 
        # For more information about sample requests, see the "Examples" section of this topic.
        self.source_instance_state = source_instance_state  # type: str

    def validate(self):
        if self.protocols:
            for k in self.protocols:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetHostResponseBodyHost, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.active_address_type is not None:
            result['ActiveAddressType'] = self.active_address_type
        if self.comment is not None:
            result['Comment'] = self.comment
        if self.host_id is not None:
            result['HostId'] = self.host_id
        if self.host_name is not None:
            result['HostName'] = self.host_name
        if self.host_private_address is not None:
            result['HostPrivateAddress'] = self.host_private_address
        if self.host_public_address is not None:
            result['HostPublicAddress'] = self.host_public_address
        if self.network_domain_id is not None:
            result['NetworkDomainId'] = self.network_domain_id
        if self.ostype is not None:
            result['OSType'] = self.ostype
        result['Protocols'] = []
        if self.protocols is not None:
            for k in self.protocols:
                result['Protocols'].append(k.to_map() if k else None)
        if self.source is not None:
            result['Source'] = self.source
        if self.source_instance_id is not None:
            result['SourceInstanceId'] = self.source_instance_id
        if self.source_instance_state is not None:
            result['SourceInstanceState'] = self.source_instance_state
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ActiveAddressType') is not None:
            self.active_address_type = m.get('ActiveAddressType')
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')
        if m.get('HostId') is not None:
            self.host_id = m.get('HostId')
        if m.get('HostName') is not None:
            self.host_name = m.get('HostName')
        if m.get('HostPrivateAddress') is not None:
            self.host_private_address = m.get('HostPrivateAddress')
        if m.get('HostPublicAddress') is not None:
            self.host_public_address = m.get('HostPublicAddress')
        if m.get('NetworkDomainId') is not None:
            self.network_domain_id = m.get('NetworkDomainId')
        if m.get('OSType') is not None:
            self.ostype = m.get('OSType')
        self.protocols = []
        if m.get('Protocols') is not None:
            for k in m.get('Protocols'):
                temp_model = GetHostResponseBodyHostProtocols()
                self.protocols.append(temp_model.from_map(k))
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('SourceInstanceId') is not None:
            self.source_instance_id = m.get('SourceInstanceId')
        if m.get('SourceInstanceState') is not None:
            self.source_instance_state = m.get('SourceInstanceState')
        return self


class GetHostResponseBody(TeaModel):
    def __init__(self, host=None, request_id=None):
        # The fingerprint of the host. This parameter uniquely identifies a host.
        self.host = host  # type: GetHostResponseBodyHost
        # The endpoint type of the host. Valid values:
        # 
        # *   **Public**: a public endpoint
        # *   **Private**: an internal endpoint
        self.request_id = request_id  # type: str

    def validate(self):
        if self.host:
            self.host.validate()

    def to_map(self):
        _map = super(GetHostResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.host is not None:
            result['Host'] = self.host.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Host') is not None:
            temp_model = GetHostResponseBodyHost()
            self.host = temp_model.from_map(m['Host'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetHostResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetHostResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetHostResponse, self).to_map()
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
            temp_model = GetHostResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetHostAccountRequest(TeaModel):
    def __init__(self, host_account_id=None, instance_id=None, region_id=None):
        # The ID of the host account that you want to query.
        # 
        # > You can call the [ListHostAccounts](~~204372~~) operation to query the ID of the host account.
        self.host_account_id = host_account_id  # type: str
        # The ID of the bastion host in which you want to query the details of the host account.
        # 
        # > You can call the [DescribeInstances](~~153281~~) operation to query the ID of the bastion host.
        self.instance_id = instance_id  # type: str
        # The region ID of the bastion host in which you want to query the details of the host account.
        # 
        # > For more information about the mapping between region IDs and region names, see [Regions and zones](~~40654~~).
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetHostAccountRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.host_account_id is not None:
            result['HostAccountId'] = self.host_account_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('HostAccountId') is not None:
            self.host_account_id = m.get('HostAccountId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class GetHostAccountResponseBodyHostAccount(TeaModel):
    def __init__(self, has_password=None, host_account_id=None, host_account_name=None, host_id=None,
                 host_share_key_id=None, host_share_key_name=None, private_key_fingerprint=None, protocol_name=None):
        # Indicates whether a password is configured for the host account. Valid values:
        # 
        # *   **true**: yes
        # *   **false**: no
        self.has_password = has_password  # type: bool
        # The ID of the host account.
        self.host_account_id = host_account_id  # type: str
        # The name of the host account.
        self.host_account_name = host_account_name  # type: str
        # The ID of the host to which the host account belongs.
        self.host_id = host_id  # type: str
        # The ID of the shared key.
        self.host_share_key_id = host_share_key_id  # type: str
        # The name of the shared key.
        self.host_share_key_name = host_share_key_name  # type: str
        # The fingerprint of the private key.
        self.private_key_fingerprint = private_key_fingerprint  # type: str
        # The protocol that is used by the host. Valid values:
        # 
        # *   **SSH**\
        # *   **RDP**\
        self.protocol_name = protocol_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetHostAccountResponseBodyHostAccount, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.has_password is not None:
            result['HasPassword'] = self.has_password
        if self.host_account_id is not None:
            result['HostAccountId'] = self.host_account_id
        if self.host_account_name is not None:
            result['HostAccountName'] = self.host_account_name
        if self.host_id is not None:
            result['HostId'] = self.host_id
        if self.host_share_key_id is not None:
            result['HostShareKeyId'] = self.host_share_key_id
        if self.host_share_key_name is not None:
            result['HostShareKeyName'] = self.host_share_key_name
        if self.private_key_fingerprint is not None:
            result['PrivateKeyFingerprint'] = self.private_key_fingerprint
        if self.protocol_name is not None:
            result['ProtocolName'] = self.protocol_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('HasPassword') is not None:
            self.has_password = m.get('HasPassword')
        if m.get('HostAccountId') is not None:
            self.host_account_id = m.get('HostAccountId')
        if m.get('HostAccountName') is not None:
            self.host_account_name = m.get('HostAccountName')
        if m.get('HostId') is not None:
            self.host_id = m.get('HostId')
        if m.get('HostShareKeyId') is not None:
            self.host_share_key_id = m.get('HostShareKeyId')
        if m.get('HostShareKeyName') is not None:
            self.host_share_key_name = m.get('HostShareKeyName')
        if m.get('PrivateKeyFingerprint') is not None:
            self.private_key_fingerprint = m.get('PrivateKeyFingerprint')
        if m.get('ProtocolName') is not None:
            self.protocol_name = m.get('ProtocolName')
        return self


class GetHostAccountResponseBody(TeaModel):
    def __init__(self, host_account=None, request_id=None):
        # The details of the host account that was queried.
        self.host_account = host_account  # type: GetHostAccountResponseBodyHostAccount
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.host_account:
            self.host_account.validate()

    def to_map(self):
        _map = super(GetHostAccountResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.host_account is not None:
            result['HostAccount'] = self.host_account.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('HostAccount') is not None:
            temp_model = GetHostAccountResponseBodyHostAccount()
            self.host_account = temp_model.from_map(m['HostAccount'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetHostAccountResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetHostAccountResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetHostAccountResponse, self).to_map()
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
            temp_model = GetHostAccountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetHostGroupRequest(TeaModel):
    def __init__(self, host_group_id=None, instance_id=None, region_id=None):
        # The region ID of the Bastionhost instance where you want to query the host group.
        # 
        # >  For more information about the mapping between region IDs and region names, see [Regions and zones](~~40654~~).
        self.host_group_id = host_group_id  # type: str
        # MyHostGroup
        self.instance_id = instance_id  # type: str
        # The ID of the Bastionhost instance where you want to query the host group.
        # 
        # >  You can call the [DescribeInstances](~~153281~~) operation to query the ID of the Bastionhost instance.
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetHostGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.host_group_id is not None:
            result['HostGroupId'] = self.host_group_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('HostGroupId') is not None:
            self.host_group_id = m.get('HostGroupId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class GetHostGroupResponseBodyHostGroup(TeaModel):
    def __init__(self, comment=None, host_group_id=None, host_group_name=None):
        # The details of the host group returned.
        self.comment = comment  # type: str
        # The description of the host group.
        self.host_group_id = host_group_id  # type: str
        # The ID of the host group.
        self.host_group_name = host_group_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetHostGroupResponseBodyHostGroup, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.comment is not None:
            result['Comment'] = self.comment
        if self.host_group_id is not None:
            result['HostGroupId'] = self.host_group_id
        if self.host_group_name is not None:
            result['HostGroupName'] = self.host_group_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')
        if m.get('HostGroupId') is not None:
            self.host_group_id = m.get('HostGroupId')
        if m.get('HostGroupName') is not None:
            self.host_group_name = m.get('HostGroupName')
        return self


class GetHostGroupResponseBody(TeaModel):
    def __init__(self, host_group=None, request_id=None):
        # The ID of the host group that you want to query.
        # 
        # >  You can call the [ListHostGroups](~~201307~~) operation to query the ID of the host group.
        self.host_group = host_group  # type: GetHostGroupResponseBodyHostGroup
        # my host group.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.host_group:
            self.host_group.validate()

    def to_map(self):
        _map = super(GetHostGroupResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.host_group is not None:
            result['HostGroup'] = self.host_group.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('HostGroup') is not None:
            temp_model = GetHostGroupResponseBodyHostGroup()
            self.host_group = temp_model.from_map(m['HostGroup'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetHostGroupResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetHostGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetHostGroupResponse, self).to_map()
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
            temp_model = GetHostGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetHostShareKeyRequest(TeaModel):
    def __init__(self, host_share_key_id=None, instance_id=None, region_id=None):
        # The time when the information about the shared key was last modified.
        self.host_share_key_id = host_share_key_id  # type: str
        # The ID of the shared key whose details you want to query.
        self.instance_id = instance_id  # type: str
        # The name of the shared key.
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetHostShareKeyRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.host_share_key_id is not None:
            result['HostShareKeyId'] = self.host_share_key_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('HostShareKeyId') is not None:
            self.host_share_key_id = m.get('HostShareKeyId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class GetHostShareKeyResponseBodyHostShareKey(TeaModel):
    def __init__(self, host_share_key_id=None, host_share_key_name=None, last_modify_key_at=None,
                 private_key_finger_print=None):
        # The fingerprint of the private key.
        self.host_share_key_id = host_share_key_id  # type: str
        self.host_share_key_name = host_share_key_name  # type: str
        self.last_modify_key_at = last_modify_key_at  # type: long
        self.private_key_finger_print = private_key_finger_print  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetHostShareKeyResponseBodyHostShareKey, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.host_share_key_id is not None:
            result['HostShareKeyId'] = self.host_share_key_id
        if self.host_share_key_name is not None:
            result['HostShareKeyName'] = self.host_share_key_name
        if self.last_modify_key_at is not None:
            result['LastModifyKeyAt'] = self.last_modify_key_at
        if self.private_key_finger_print is not None:
            result['PrivateKeyFingerPrint'] = self.private_key_finger_print
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('HostShareKeyId') is not None:
            self.host_share_key_id = m.get('HostShareKeyId')
        if m.get('HostShareKeyName') is not None:
            self.host_share_key_name = m.get('HostShareKeyName')
        if m.get('LastModifyKeyAt') is not None:
            self.last_modify_key_at = m.get('LastModifyKeyAt')
        if m.get('PrivateKeyFingerPrint') is not None:
            self.private_key_finger_print = m.get('PrivateKeyFingerPrint')
        return self


class GetHostShareKeyResponseBody(TeaModel):
    def __init__(self, host_share_key=None, request_id=None):
        # The operation that you want to perform. Set the value to **GetHostShareKey**.
        self.host_share_key = host_share_key  # type: GetHostShareKeyResponseBodyHostShareKey
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.host_share_key:
            self.host_share_key.validate()

    def to_map(self):
        _map = super(GetHostShareKeyResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.host_share_key is not None:
            result['HostShareKey'] = self.host_share_key.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('HostShareKey') is not None:
            temp_model = GetHostShareKeyResponseBodyHostShareKey()
            self.host_share_key = temp_model.from_map(m['HostShareKey'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetHostShareKeyResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetHostShareKeyResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetHostShareKeyResponse, self).to_map()
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
            temp_model = GetHostShareKeyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetInstanceADAuthServerRequest(TeaModel):
    def __init__(self, instance_id=None, region_id=None):
        # The field that is used to indicate the email address of a user on the AD server.
        self.instance_id = instance_id  # type: str
        # Indicates whether passwords are required. Valid values:
        # 
        # *   **true**: required
        # *   **false**: not required
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetInstanceADAuthServerRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class GetInstanceADAuthServerResponseBodyAD(TeaModel):
    def __init__(self, account=None, base_dn=None, domain=None, email_mapping=None, filter=None, has_password=None,
                 is_ssl=None, mobile_mapping=None, name_mapping=None, port=None, server=None, standby_server=None):
        # The port that is used to access the AD server.
        self.account = account  # type: str
        # The ID of the bastion host to query.
        # 
        # You can call the [DescribeInstances](~~153281~~) operation to query the ID of the bastion host.
        self.base_dn = base_dn  # type: str
        # The settings of AD authentication.
        self.domain = domain  # type: str
        # The address of the secondary AD server.
        self.email_mapping = email_mapping  # type: str
        # The field that is used to indicate the mobile phone number of a user on the AD server.
        self.filter = filter  # type: str
        # The address of the AD server.
        self.has_password = has_password  # type: bool
        # The Base DN of the AD server.
        self.is_ssl = is_ssl  # type: bool
        # The field that is used to indicate the name of a user on the AD server.
        self.mobile_mapping = mobile_mapping  # type: str
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.name_mapping = name_mapping  # type: str
        # Queries the settings of Active Directory (AD) authentication on a bastion host.
        self.port = port  # type: long
        self.server = server  # type: str
        self.standby_server = standby_server  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetInstanceADAuthServerResponseBodyAD, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account is not None:
            result['Account'] = self.account
        if self.base_dn is not None:
            result['BaseDN'] = self.base_dn
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.email_mapping is not None:
            result['EmailMapping'] = self.email_mapping
        if self.filter is not None:
            result['Filter'] = self.filter
        if self.has_password is not None:
            result['HasPassword'] = self.has_password
        if self.is_ssl is not None:
            result['IsSSL'] = self.is_ssl
        if self.mobile_mapping is not None:
            result['MobileMapping'] = self.mobile_mapping
        if self.name_mapping is not None:
            result['NameMapping'] = self.name_mapping
        if self.port is not None:
            result['Port'] = self.port
        if self.server is not None:
            result['Server'] = self.server
        if self.standby_server is not None:
            result['StandbyServer'] = self.standby_server
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Account') is not None:
            self.account = m.get('Account')
        if m.get('BaseDN') is not None:
            self.base_dn = m.get('BaseDN')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('EmailMapping') is not None:
            self.email_mapping = m.get('EmailMapping')
        if m.get('Filter') is not None:
            self.filter = m.get('Filter')
        if m.get('HasPassword') is not None:
            self.has_password = m.get('HasPassword')
        if m.get('IsSSL') is not None:
            self.is_ssl = m.get('IsSSL')
        if m.get('MobileMapping') is not None:
            self.mobile_mapping = m.get('MobileMapping')
        if m.get('NameMapping') is not None:
            self.name_mapping = m.get('NameMapping')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('Server') is not None:
            self.server = m.get('Server')
        if m.get('StandbyServer') is not None:
            self.standby_server = m.get('StandbyServer')
        return self


class GetInstanceADAuthServerResponseBody(TeaModel):
    def __init__(self, ad=None, request_id=None):
        # The operation that you want to perform. Set the value to **GetInstanceADAuthServer**.
        self.ad = ad  # type: GetInstanceADAuthServerResponseBodyAD
        # Indicates whether SSL is supported. Valid values:
        # 
        # *   **true**: supported
        # *   **false**: not supported
        self.request_id = request_id  # type: str

    def validate(self):
        if self.ad:
            self.ad.validate()

    def to_map(self):
        _map = super(GetInstanceADAuthServerResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ad is not None:
            result['AD'] = self.ad.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AD') is not None:
            temp_model = GetInstanceADAuthServerResponseBodyAD()
            self.ad = temp_model.from_map(m['AD'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetInstanceADAuthServerResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetInstanceADAuthServerResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetInstanceADAuthServerResponse, self).to_map()
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
            temp_model = GetInstanceADAuthServerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetInstanceLDAPAuthServerRequest(TeaModel):
    def __init__(self, instance_id=None, region_id=None):
        # Indicates whether passwords are required. Valid values:
        # 
        # *   **true**: required
        # *   **false**: not required
        self.instance_id = instance_id  # type: str
        # The operation that you want to perform. Set the value to **GetInstanceLDAPAuthServer**.
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetInstanceLDAPAuthServerRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class GetInstanceLDAPAuthServerResponseBodyLDAP(TeaModel):
    def __init__(self, account=None, base_dn=None, email_mapping=None, filter=None, has_password=None, is_ssl=None,
                 login_name_mapping=None, mobile_mapping=None, name_mapping=None, port=None, server=None, standby_server=None):
        # The ID of the bastion host.
        # 
        # >  You can call the [DescribeInstances](~~153281~~) operation to query the ID of the bastion host.
        self.account = account  # type: str
        # The field that is used to indicate the logon name of a user on the LDAP server.
        self.base_dn = base_dn  # type: str
        # The address of the secondary LDAP server.
        self.email_mapping = email_mapping  # type: str
        # The Base distinguished name (DN).
        self.filter = filter  # type: str
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.has_password = has_password  # type: str
        # The condition that is used to filter users.
        self.is_ssl = is_ssl  # type: bool
        # The port that is used to access the LDAP server.
        self.login_name_mapping = login_name_mapping  # type: str
        # The field that is used to indicate the email address of a user on the LDAP server.
        self.mobile_mapping = mobile_mapping  # type: str
        # The field that is used to indicate the mobile phone number of a user on the LDAP server.
        self.name_mapping = name_mapping  # type: str
        self.port = port  # type: long
        self.server = server  # type: str
        self.standby_server = standby_server  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetInstanceLDAPAuthServerResponseBodyLDAP, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account is not None:
            result['Account'] = self.account
        if self.base_dn is not None:
            result['BaseDN'] = self.base_dn
        if self.email_mapping is not None:
            result['EmailMapping'] = self.email_mapping
        if self.filter is not None:
            result['Filter'] = self.filter
        if self.has_password is not None:
            result['HasPassword'] = self.has_password
        if self.is_ssl is not None:
            result['IsSSL'] = self.is_ssl
        if self.login_name_mapping is not None:
            result['LoginNameMapping'] = self.login_name_mapping
        if self.mobile_mapping is not None:
            result['MobileMapping'] = self.mobile_mapping
        if self.name_mapping is not None:
            result['NameMapping'] = self.name_mapping
        if self.port is not None:
            result['Port'] = self.port
        if self.server is not None:
            result['Server'] = self.server
        if self.standby_server is not None:
            result['StandbyServer'] = self.standby_server
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Account') is not None:
            self.account = m.get('Account')
        if m.get('BaseDN') is not None:
            self.base_dn = m.get('BaseDN')
        if m.get('EmailMapping') is not None:
            self.email_mapping = m.get('EmailMapping')
        if m.get('Filter') is not None:
            self.filter = m.get('Filter')
        if m.get('HasPassword') is not None:
            self.has_password = m.get('HasPassword')
        if m.get('IsSSL') is not None:
            self.is_ssl = m.get('IsSSL')
        if m.get('LoginNameMapping') is not None:
            self.login_name_mapping = m.get('LoginNameMapping')
        if m.get('MobileMapping') is not None:
            self.mobile_mapping = m.get('MobileMapping')
        if m.get('NameMapping') is not None:
            self.name_mapping = m.get('NameMapping')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('Server') is not None:
            self.server = m.get('Server')
        if m.get('StandbyServer') is not None:
            self.standby_server = m.get('StandbyServer')
        return self


class GetInstanceLDAPAuthServerResponseBody(TeaModel):
    def __init__(self, ldap=None, request_id=None):
        # Indicates whether SSL is supported. Valid values:
        # 
        # *   **true**: supported
        # *   **false**: not supported
        self.ldap = ldap  # type: GetInstanceLDAPAuthServerResponseBodyLDAP
        # The settings of LDAP authentication.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.ldap:
            self.ldap.validate()

    def to_map(self):
        _map = super(GetInstanceLDAPAuthServerResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ldap is not None:
            result['LDAP'] = self.ldap.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('LDAP') is not None:
            temp_model = GetInstanceLDAPAuthServerResponseBodyLDAP()
            self.ldap = temp_model.from_map(m['LDAP'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetInstanceLDAPAuthServerResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetInstanceLDAPAuthServerResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetInstanceLDAPAuthServerResponse, self).to_map()
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
            temp_model = GetInstanceLDAPAuthServerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetInstanceTwoFactorRequest(TeaModel):
    def __init__(self, instance_id=None, region_id=None):
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.instance_id = instance_id  # type: str
        # The operation that you want to perform. Set the value to **GetInstanceTwoFactor**.
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetInstanceTwoFactorRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class GetInstanceTwoFactorResponseBodyConfig(TeaModel):
    def __init__(self, enable_two_factor=None, skip_two_factor_time=None, two_factor_methods=None):
        # Queries the settings of two-factor authentication on a bastion host.
        self.enable_two_factor = enable_two_factor  # type: bool
        self.skip_two_factor_time = skip_two_factor_time  # type: long
        self.two_factor_methods = two_factor_methods  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetInstanceTwoFactorResponseBodyConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable_two_factor is not None:
            result['EnableTwoFactor'] = self.enable_two_factor
        if self.skip_two_factor_time is not None:
            result['SkipTwoFactorTime'] = self.skip_two_factor_time
        if self.two_factor_methods is not None:
            result['TwoFactorMethods'] = self.two_factor_methods
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EnableTwoFactor') is not None:
            self.enable_two_factor = m.get('EnableTwoFactor')
        if m.get('SkipTwoFactorTime') is not None:
            self.skip_two_factor_time = m.get('SkipTwoFactorTime')
        if m.get('TwoFactorMethods') is not None:
            self.two_factor_methods = m.get('TwoFactorMethods')
        return self


class GetInstanceTwoFactorResponseBody(TeaModel):
    def __init__(self, config=None, request_id=None):
        # The settings of two-factor authentication.
        self.config = config  # type: GetInstanceTwoFactorResponseBodyConfig
        # The duration within which two-factor authentication is not required after a local user passes two-factor authentication. Valid values: `0 to 168`. Unit: hours.
        # 
        # >  If 0 is returned, a local user must pass two-factor authentication every time the local user logs on to the bastion host.
        self.request_id = request_id  # type: str

    def validate(self):
        if self.config:
            self.config.validate()

    def to_map(self):
        _map = super(GetInstanceTwoFactorResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.config is not None:
            result['Config'] = self.config.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Config') is not None:
            temp_model = GetInstanceTwoFactorResponseBodyConfig()
            self.config = temp_model.from_map(m['Config'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetInstanceTwoFactorResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetInstanceTwoFactorResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetInstanceTwoFactorResponse, self).to_map()
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
            temp_model = GetInstanceTwoFactorResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetUserRequest(TeaModel):
    def __init__(self, instance_id=None, region_id=None, user_id=None):
        # The ID of the bastion host on which you want to query the user.
        # 
        # > You can call the [DescribeInstances](~~153281~~) operation to query the ID of the bastion host.
        self.instance_id = instance_id  # type: str
        # The region ID of the bastion host on which you want to query the user.
        # 
        # > For more information about the mapping between region IDs and region names, see [Regions and zones](~~40654~~).
        self.region_id = region_id  # type: str
        # The ID of the user.
        # 
        # > You can call the [ListUsers](~~204522~~) operation to query the ID of the user.
        self.user_id = user_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetUserRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class GetUserResponseBodyUser(TeaModel):
    def __init__(self, comment=None, display_name=None, effective_end_time=None, effective_start_time=None,
                 email=None, mobile=None, mobile_country_code=None, need_reset_password=None, source=None,
                 source_user_id=None, two_factor_methods=None, two_factor_status=None, user_id=None, user_name=None,
                 user_state=None):
        # The description of the user.
        self.comment = comment  # type: str
        # The display name of the user.
        self.display_name = display_name  # type: str
        # The end of the validity period of the user. The value is a UNIX timestamp. Unit: seconds.
        self.effective_end_time = effective_end_time  # type: long
        # The beginning of the validity period of the user. The value is a UNIX timestamp. Unit: seconds.
        self.effective_start_time = effective_start_time  # type: long
        # The email address of the user.
        self.email = email  # type: str
        # The mobile phone number of the user.
        self.mobile = mobile  # type: str
        # The location in which the mobile number of the user is registered. Valid values:
        # 
        # *   **CN**: the Chinese mainland, whose country calling code is +86
        # *   **HK**: Hong Kong (China), whose country calling code is +852
        # *   **MO**: Macao (China), whose country calling code is +853
        # *   **TW**: Taiwan (China), whose country calling code is +886
        # *   **RU**: Russia, whose country calling code is +7
        # *   **SG**: Singapore, whose country calling code is +65
        # *   **MY**: Malaysia, whose country calling code is +60
        # *   **ID**: Indonesia, whose country calling code is +62
        # *   **DE**: Germany, whose country calling code is +49
        # *   **AU**: Australia, whose country calling code is +61
        # *   **US**: US, whose country calling code is +1
        # *   **AE**: United Arab Emirates, whose country calling code is +971
        # *   **JP:** Japan, whose country calling code is +81
        # *   **GB**: UK, whose country calling code is +44
        # *   **IN**: India, whose country calling code is +91
        # *   **KR**: Republic of Korea, whose country calling code is +82
        # *   **PH**: Philippines, whose country calling code is +63
        # *   **CH**: Switzerland, whose country calling code is +41
        # *   **SE**: Sweden, whose country calling code is +46
        self.mobile_country_code = mobile_country_code  # type: str
        # Specifies whether password reset is required upon the next logon. Valid values:
        # 
        # *   **true**: yes
        # *   **false**: no
        self.need_reset_password = need_reset_password  # type: bool
        # The source of the user. Valid values:
        # 
        # *   **Local**: a local user
        # *   **Ram**: a RAM user
        self.source = source  # type: str
        # The unique ID of the user.
        # 
        # > This parameter uniquely identifies a RAM user of the bastion host. A value is returned for this parameter if the **Source** parameter is set to **Ram**. No value is returned for this parameter if the **Source** parameter is set to **Local**.
        self.source_user_id = source_user_id  # type: str
        # An array that consists of the details of the two-factor authentication method.
        self.two_factor_methods = two_factor_methods  # type: list[str]
        # The two-factor authentication status of the user. Valid values:
        # 
        # *   **Global**: The global settings are used.
        # *   **Disable**: The two-factor authentication is disabled.
        # *   **Enable**: The two-factor authentication is enabled and the user-specific setting is used.
        self.two_factor_status = two_factor_status  # type: str
        # The ID of the user.
        self.user_id = user_id  # type: str
        # The logon name of the user.
        self.user_name = user_name  # type: str
        # An array that consists of the details of the user status.
        self.user_state = user_state  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetUserResponseBodyUser, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.comment is not None:
            result['Comment'] = self.comment
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.effective_end_time is not None:
            result['EffectiveEndTime'] = self.effective_end_time
        if self.effective_start_time is not None:
            result['EffectiveStartTime'] = self.effective_start_time
        if self.email is not None:
            result['Email'] = self.email
        if self.mobile is not None:
            result['Mobile'] = self.mobile
        if self.mobile_country_code is not None:
            result['MobileCountryCode'] = self.mobile_country_code
        if self.need_reset_password is not None:
            result['NeedResetPassword'] = self.need_reset_password
        if self.source is not None:
            result['Source'] = self.source
        if self.source_user_id is not None:
            result['SourceUserId'] = self.source_user_id
        if self.two_factor_methods is not None:
            result['TwoFactorMethods'] = self.two_factor_methods
        if self.two_factor_status is not None:
            result['TwoFactorStatus'] = self.two_factor_status
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.user_name is not None:
            result['UserName'] = self.user_name
        if self.user_state is not None:
            result['UserState'] = self.user_state
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('EffectiveEndTime') is not None:
            self.effective_end_time = m.get('EffectiveEndTime')
        if m.get('EffectiveStartTime') is not None:
            self.effective_start_time = m.get('EffectiveStartTime')
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('Mobile') is not None:
            self.mobile = m.get('Mobile')
        if m.get('MobileCountryCode') is not None:
            self.mobile_country_code = m.get('MobileCountryCode')
        if m.get('NeedResetPassword') is not None:
            self.need_reset_password = m.get('NeedResetPassword')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('SourceUserId') is not None:
            self.source_user_id = m.get('SourceUserId')
        if m.get('TwoFactorMethods') is not None:
            self.two_factor_methods = m.get('TwoFactorMethods')
        if m.get('TwoFactorStatus') is not None:
            self.two_factor_status = m.get('TwoFactorStatus')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        if m.get('UserState') is not None:
            self.user_state = m.get('UserState')
        return self


class GetUserResponseBody(TeaModel):
    def __init__(self, request_id=None, user=None):
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The details of the user that was queried.
        self.user = user  # type: GetUserResponseBodyUser

    def validate(self):
        if self.user:
            self.user.validate()

    def to_map(self):
        _map = super(GetUserResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.user is not None:
            result['User'] = self.user.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('User') is not None:
            temp_model = GetUserResponseBodyUser()
            self.user = temp_model.from_map(m['User'])
        return self


class GetUserResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetUserResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetUserResponse, self).to_map()
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
            temp_model = GetUserResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetUserGroupRequest(TeaModel):
    def __init__(self, instance_id=None, region_id=None, user_group_id=None):
        # The ID of the request.
        self.instance_id = instance_id  # type: str
        # The name of the user group.
        self.region_id = region_id  # type: str
        # All Bastionhost API requests must include common request parameters. For more information about common request parameters, see [Common parameters](~~315526~~).
        # 
        # For more information about sample requests, see the "Examples" section of this topic.
        self.user_group_id = user_group_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetUserGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.user_group_id is not None:
            result['UserGroupId'] = self.user_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('UserGroupId') is not None:
            self.user_group_id = m.get('UserGroupId')
        return self


class GetUserGroupResponseBodyUserGroup(TeaModel):
    def __init__(self, comment=None, user_group_id=None, user_group_name=None):
        # GetUserGroup
        self.comment = comment  # type: str
        self.user_group_id = user_group_id  # type: str
        # WB662865
        self.user_group_name = user_group_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetUserGroupResponseBodyUserGroup, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.comment is not None:
            result['Comment'] = self.comment
        if self.user_group_id is not None:
            result['UserGroupId'] = self.user_group_id
        if self.user_group_name is not None:
            result['UserGroupName'] = self.user_group_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')
        if m.get('UserGroupId') is not None:
            self.user_group_id = m.get('UserGroupId')
        if m.get('UserGroupName') is not None:
            self.user_group_name = m.get('UserGroupName')
        return self


class GetUserGroupResponseBody(TeaModel):
    def __init__(self, request_id=None, user_group=None):
        # Queries the details of a specified user group in a specified Bastionhost instance.
        self.request_id = request_id  # type: str
        # GetUserGroup
        self.user_group = user_group  # type: GetUserGroupResponseBodyUserGroup

    def validate(self):
        if self.user_group:
            self.user_group.validate()

    def to_map(self):
        _map = super(GetUserGroupResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.user_group is not None:
            result['UserGroup'] = self.user_group.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('UserGroup') is not None:
            temp_model = GetUserGroupResponseBodyUserGroup()
            self.user_group = temp_model.from_map(m['UserGroup'])
        return self


class GetUserGroupResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: GetUserGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetUserGroupResponse, self).to_map()
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
            temp_model = GetUserGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListApproveCommandsRequest(TeaModel):
    def __init__(self, instance_id=None, page_number=None, page_size=None, region_id=None):
        self.instance_id = instance_id  # type: str
        self.page_number = page_number  # type: str
        self.page_size = page_size  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListApproveCommandsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListApproveCommandsResponseBodyApproveCommands(TeaModel):
    def __init__(self, approve_command_id=None, asset_account_name=None, asset_ip=None, asset_name=None,
                 client_ip=None, client_user=None, command=None, create_time=None, protocol_name=None, session_id=None,
                 state=None):
        self.approve_command_id = approve_command_id  # type: str
        self.asset_account_name = asset_account_name  # type: str
        self.asset_ip = asset_ip  # type: str
        self.asset_name = asset_name  # type: str
        self.client_ip = client_ip  # type: str
        self.client_user = client_user  # type: str
        self.command = command  # type: str
        self.create_time = create_time  # type: str
        self.protocol_name = protocol_name  # type: str
        self.session_id = session_id  # type: str
        self.state = state  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListApproveCommandsResponseBodyApproveCommands, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.approve_command_id is not None:
            result['ApproveCommandId'] = self.approve_command_id
        if self.asset_account_name is not None:
            result['AssetAccountName'] = self.asset_account_name
        if self.asset_ip is not None:
            result['AssetIp'] = self.asset_ip
        if self.asset_name is not None:
            result['AssetName'] = self.asset_name
        if self.client_ip is not None:
            result['ClientIp'] = self.client_ip
        if self.client_user is not None:
            result['ClientUser'] = self.client_user
        if self.command is not None:
            result['Command'] = self.command
        if self.create_time is not None:
            result['CreateTime'] = self.create_time
        if self.protocol_name is not None:
            result['ProtocolName'] = self.protocol_name
        if self.session_id is not None:
            result['SessionId'] = self.session_id
        if self.state is not None:
            result['State'] = self.state
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApproveCommandId') is not None:
            self.approve_command_id = m.get('ApproveCommandId')
        if m.get('AssetAccountName') is not None:
            self.asset_account_name = m.get('AssetAccountName')
        if m.get('AssetIp') is not None:
            self.asset_ip = m.get('AssetIp')
        if m.get('AssetName') is not None:
            self.asset_name = m.get('AssetName')
        if m.get('ClientIp') is not None:
            self.client_ip = m.get('ClientIp')
        if m.get('ClientUser') is not None:
            self.client_user = m.get('ClientUser')
        if m.get('Command') is not None:
            self.command = m.get('Command')
        if m.get('CreateTime') is not None:
            self.create_time = m.get('CreateTime')
        if m.get('ProtocolName') is not None:
            self.protocol_name = m.get('ProtocolName')
        if m.get('SessionId') is not None:
            self.session_id = m.get('SessionId')
        if m.get('State') is not None:
            self.state = m.get('State')
        return self


class ListApproveCommandsResponseBody(TeaModel):
    def __init__(self, approve_commands=None, request_id=None, total_count=None):
        self.approve_commands = approve_commands  # type: list[ListApproveCommandsResponseBodyApproveCommands]
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: long

    def validate(self):
        if self.approve_commands:
            for k in self.approve_commands:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListApproveCommandsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['ApproveCommands'] = []
        if self.approve_commands is not None:
            for k in self.approve_commands:
                result['ApproveCommands'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.approve_commands = []
        if m.get('ApproveCommands') is not None:
            for k in m.get('ApproveCommands'):
                temp_model = ListApproveCommandsResponseBodyApproveCommands()
                self.approve_commands.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListApproveCommandsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListApproveCommandsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListApproveCommandsResponse, self).to_map()
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
            temp_model = ListApproveCommandsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListHostAccountsRequest(TeaModel):
    def __init__(self, host_account_name=None, host_id=None, instance_id=None, page_number=None, page_size=None,
                 protocol_name=None, region_id=None):
        # Indicates whether a password is configured for the host account.
        # 
        # Valid values:
        # 
        # *   true: A password is configured for the host account.
        # *   false: No passwords are configured for the host account.
        self.host_account_name = host_account_name  # type: str
        # The protocol used by the host whose accounts you want to query.
        # 
        # Valid values:
        # 
        # *   SSH
        # *   RDP
        self.host_id = host_id  # type: str
        # The ID of the shared key.
        self.instance_id = instance_id  # type: str
        # The operation that you want to perform.
        # 
        # Set the value to **ListHostAccounts**.
        self.page_number = page_number  # type: str
        # The number of entries to return on each page.
        # 
        # Maximum value: 100. Default value: 20. If you leave this parameter empty, 20 entries are returned on each page.
        # 
        # >  We recommend that you do not leave this parameter empty.
        self.page_size = page_size  # type: str
        # The name of the host account that you want to query. The name can be up to 128 characters in length. Only exact match is supported.
        self.protocol_name = protocol_name  # type: str
        # The ID of the specified host whose accounts you want to query.
        # 
        # >  You can call the [ListHosts](~~200665~~) operation to query the ID of the host.
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListHostAccountsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.host_account_name is not None:
            result['HostAccountName'] = self.host_account_name
        if self.host_id is not None:
            result['HostId'] = self.host_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.protocol_name is not None:
            result['ProtocolName'] = self.protocol_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('HostAccountName') is not None:
            self.host_account_name = m.get('HostAccountName')
        if m.get('HostId') is not None:
            self.host_id = m.get('HostId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('ProtocolName') is not None:
            self.protocol_name = m.get('ProtocolName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListHostAccountsResponseBodyHostAccounts(TeaModel):
    def __init__(self, has_password=None, host_account_id=None, host_account_name=None, host_id=None,
                 host_share_key_id=None, host_share_key_name=None, private_key_fingerprint=None, protocol_name=None):
        # The fingerprint of the private key for the host account.
        self.has_password = has_password  # type: bool
        # The ID of the request.
        self.host_account_id = host_account_id  # type: str
        # The name of the shared key.
        self.host_account_name = host_account_name  # type: str
        self.host_id = host_id  # type: str
        self.host_share_key_id = host_share_key_id  # type: str
        self.host_share_key_name = host_share_key_name  # type: str
        # The protocol that is used by the host.
        # 
        # Valid values:
        # 
        # *   SSH
        # *   RDP
        self.private_key_fingerprint = private_key_fingerprint  # type: str
        # The number of the page to return. Default value: **1**.
        self.protocol_name = protocol_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListHostAccountsResponseBodyHostAccounts, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.has_password is not None:
            result['HasPassword'] = self.has_password
        if self.host_account_id is not None:
            result['HostAccountId'] = self.host_account_id
        if self.host_account_name is not None:
            result['HostAccountName'] = self.host_account_name
        if self.host_id is not None:
            result['HostId'] = self.host_id
        if self.host_share_key_id is not None:
            result['HostShareKeyId'] = self.host_share_key_id
        if self.host_share_key_name is not None:
            result['HostShareKeyName'] = self.host_share_key_name
        if self.private_key_fingerprint is not None:
            result['PrivateKeyFingerprint'] = self.private_key_fingerprint
        if self.protocol_name is not None:
            result['ProtocolName'] = self.protocol_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('HasPassword') is not None:
            self.has_password = m.get('HasPassword')
        if m.get('HostAccountId') is not None:
            self.host_account_id = m.get('HostAccountId')
        if m.get('HostAccountName') is not None:
            self.host_account_name = m.get('HostAccountName')
        if m.get('HostId') is not None:
            self.host_id = m.get('HostId')
        if m.get('HostShareKeyId') is not None:
            self.host_share_key_id = m.get('HostShareKeyId')
        if m.get('HostShareKeyName') is not None:
            self.host_share_key_name = m.get('HostShareKeyName')
        if m.get('PrivateKeyFingerprint') is not None:
            self.private_key_fingerprint = m.get('PrivateKeyFingerprint')
        if m.get('ProtocolName') is not None:
            self.protocol_name = m.get('ProtocolName')
        return self


class ListHostAccountsResponseBody(TeaModel):
    def __init__(self, host_accounts=None, request_id=None, total_count=None):
        # The ID of the host account.
        self.host_accounts = host_accounts  # type: list[ListHostAccountsResponseBodyHostAccounts]
        # An array that consists of the queried host accounts.
        self.request_id = request_id  # type: str
        # The ID of the bastion host in which you want to query accounts of the specified host.
        # 
        # >  You can call the DescribeInstances operation to query the ID of the bastion host.
        self.total_count = total_count  # type: int

    def validate(self):
        if self.host_accounts:
            for k in self.host_accounts:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListHostAccountsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['HostAccounts'] = []
        if self.host_accounts is not None:
            for k in self.host_accounts:
                result['HostAccounts'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.host_accounts = []
        if m.get('HostAccounts') is not None:
            for k in m.get('HostAccounts'):
                temp_model = ListHostAccountsResponseBodyHostAccounts()
                self.host_accounts.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListHostAccountsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListHostAccountsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListHostAccountsResponse, self).to_map()
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
            temp_model = ListHostAccountsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListHostAccountsForHostShareKeyRequest(TeaModel):
    def __init__(self, host_share_key_id=None, instance_id=None, page_number=None, page_size=None, region_id=None):
        # The ID of the shared key.
        self.host_share_key_id = host_share_key_id  # type: str
        # The ID of the bastion host. You can call the [DescribeInstances](~~153281~~) operation to query the ID of the bastion host.
        self.instance_id = instance_id  # type: str
        # The number of the page to return. Default value: **1**.
        self.page_number = page_number  # type: str
        # The number of entries to return on each page. Default value: **10**.
        self.page_size = page_size  # type: str
        # The region ID of the bastion host. For more information about the mapping between region IDs and region names, see [Regions and zones](~~40654~~).
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListHostAccountsForHostShareKeyRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.host_share_key_id is not None:
            result['HostShareKeyId'] = self.host_share_key_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('HostShareKeyId') is not None:
            self.host_share_key_id = m.get('HostShareKeyId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListHostAccountsForHostShareKeyResponseBodyHostAccounts(TeaModel):
    def __init__(self, host_account_name=None, host_id=None, hosts_account_id=None, protocol_name=None):
        # The name of the host account.
        self.host_account_name = host_account_name  # type: str
        # The ID of the host.
        self.host_id = host_id  # type: str
        # The ID of the host account.
        self.hosts_account_id = hosts_account_id  # type: str
        # The O\&M protocol.
        self.protocol_name = protocol_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListHostAccountsForHostShareKeyResponseBodyHostAccounts, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.host_account_name is not None:
            result['HostAccountName'] = self.host_account_name
        if self.host_id is not None:
            result['HostId'] = self.host_id
        if self.hosts_account_id is not None:
            result['HostsAccountId'] = self.hosts_account_id
        if self.protocol_name is not None:
            result['ProtocolName'] = self.protocol_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('HostAccountName') is not None:
            self.host_account_name = m.get('HostAccountName')
        if m.get('HostId') is not None:
            self.host_id = m.get('HostId')
        if m.get('HostsAccountId') is not None:
            self.hosts_account_id = m.get('HostsAccountId')
        if m.get('ProtocolName') is not None:
            self.protocol_name = m.get('ProtocolName')
        return self


class ListHostAccountsForHostShareKeyResponseBody(TeaModel):
    def __init__(self, host_accounts=None, request_id=None, total_count=None):
        # An array that consists of the host accounts that are associated with the shared key.
        self.host_accounts = host_accounts  # type: list[ListHostAccountsForHostShareKeyResponseBodyHostAccounts]
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id  # type: str
        # The total number of the host accounts that are associated with the shared key.
        self.total_count = total_count  # type: long

    def validate(self):
        if self.host_accounts:
            for k in self.host_accounts:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListHostAccountsForHostShareKeyResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['HostAccounts'] = []
        if self.host_accounts is not None:
            for k in self.host_accounts:
                result['HostAccounts'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.host_accounts = []
        if m.get('HostAccounts') is not None:
            for k in m.get('HostAccounts'):
                temp_model = ListHostAccountsForHostShareKeyResponseBodyHostAccounts()
                self.host_accounts.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListHostAccountsForHostShareKeyResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListHostAccountsForHostShareKeyResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListHostAccountsForHostShareKeyResponse, self).to_map()
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
            temp_model = ListHostAccountsForHostShareKeyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListHostAccountsForUserRequest(TeaModel):
    def __init__(self, host_account_name=None, host_id=None, instance_id=None, page_number=None, page_size=None,
                 region_id=None, user_id=None):
        # The number of the page to return. Default value: **1**.
        self.host_account_name = host_account_name  # type: str
        # The ID of the host for which the host accounts were queried.
        self.host_id = host_id  # type: str
        # The total number of host accounts returned.
        self.instance_id = instance_id  # type: str
        # The ID of the user for which you want to query authorized host accounts.
        # 
        # >  You can call the [ListUsers](~~204522~~) operation to query the ID of the user ID.
        self.page_number = page_number  # type: str
        # The name of the host account that you want to query. Exact match is supported.
        self.page_size = page_size  # type: str
        # The name of the host account.
        self.region_id = region_id  # type: str
        # The region ID of the Bastionhost instance where you want to query the host accounts that the user is authorized to manage on the host.
        # 
        # >  For more information about the mapping between region IDs and region names, see [Regions and zones](~~40654~~).
        self.user_id = user_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListHostAccountsForUserRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.host_account_name is not None:
            result['HostAccountName'] = self.host_account_name
        if self.host_id is not None:
            result['HostId'] = self.host_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('HostAccountName') is not None:
            self.host_account_name = m.get('HostAccountName')
        if m.get('HostId') is not None:
            self.host_id = m.get('HostId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class ListHostAccountsForUserResponseBodyHostAccounts(TeaModel):
    def __init__(self, host_account_id=None, host_account_name=None, host_id=None, is_authorized=None,
                 protocol_name=None):
        # The protocol that is used by the host account. Valid values:
        # 
        # *   **SSH**\
        # *   **RDP**\
        self.host_account_id = host_account_id  # type: str
        # The ID of the host account.
        self.host_account_name = host_account_name  # type: str
        # The ID of the request.
        self.host_id = host_id  # type: str
        # The ID of the host for which you want to query the host accounts that the user is authorized to manage.
        # 
        # >  You can call the [ListHosts](~~200665~~) operation to query the ID of the host.
        self.is_authorized = is_authorized  # type: bool
        # Indicates whether the user is authorized to manage the host account. Valid values:
        # 
        # *   **true**: The user is authorized to manage the host account.
        # *   **false**: The user is not authorized to manage the host account.
        self.protocol_name = protocol_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListHostAccountsForUserResponseBodyHostAccounts, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.host_account_id is not None:
            result['HostAccountId'] = self.host_account_id
        if self.host_account_name is not None:
            result['HostAccountName'] = self.host_account_name
        if self.host_id is not None:
            result['HostId'] = self.host_id
        if self.is_authorized is not None:
            result['IsAuthorized'] = self.is_authorized
        if self.protocol_name is not None:
            result['ProtocolName'] = self.protocol_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('HostAccountId') is not None:
            self.host_account_id = m.get('HostAccountId')
        if m.get('HostAccountName') is not None:
            self.host_account_name = m.get('HostAccountName')
        if m.get('HostId') is not None:
            self.host_id = m.get('HostId')
        if m.get('IsAuthorized') is not None:
            self.is_authorized = m.get('IsAuthorized')
        if m.get('ProtocolName') is not None:
            self.protocol_name = m.get('ProtocolName')
        return self


class ListHostAccountsForUserResponseBody(TeaModel):
    def __init__(self, host_accounts=None, request_id=None, total_count=None):
        # The host accounts returned.
        self.host_accounts = host_accounts  # type: list[ListHostAccountsForUserResponseBodyHostAccounts]
        # The ID of the Bastionhost instance where you want to query the host accounts that the user is authorized to manage on the host.
        # 
        # >  You can call the [DescribeInstances](~~153281~~) operation to query the ID of the Bastionhost instance.
        self.request_id = request_id  # type: str
        # The number of entries to return on each page.
        # 
        # The value of the PageSize parameter must not exceed 100. Default value: 20. If you leave the PageSize parameter empty, 20 entries are returned on each page.
        # 
        # >  We recommend that you do not leave the PageSize parameter empty.
        self.total_count = total_count  # type: int

    def validate(self):
        if self.host_accounts:
            for k in self.host_accounts:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListHostAccountsForUserResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['HostAccounts'] = []
        if self.host_accounts is not None:
            for k in self.host_accounts:
                result['HostAccounts'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.host_accounts = []
        if m.get('HostAccounts') is not None:
            for k in m.get('HostAccounts'):
                temp_model = ListHostAccountsForUserResponseBodyHostAccounts()
                self.host_accounts.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListHostAccountsForUserResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListHostAccountsForUserResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListHostAccountsForUserResponse, self).to_map()
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
            temp_model = ListHostAccountsForUserResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListHostAccountsForUserGroupRequest(TeaModel):
    def __init__(self, host_account_name=None, host_id=None, instance_id=None, page_number=None, page_size=None,
                 region_id=None, user_group_id=None):
        # The name of the host account that you want to query. Exact match is supported.
        self.host_account_name = host_account_name  # type: str
        # The ID of the host to query.
        # 
        # > You can call the [ListHosts](~~200665~~) operation to query the ID of the host.
        self.host_id = host_id  # type: str
        # The ID of the bastion host on which you want to query the host accounts to be managed by the specified user group on the specified host.
        # 
        # > You can call the [DescribeInstances](~~153281~~) operation to query the ID of the bastion host.
        self.instance_id = instance_id  # type: str
        # The number of the page to return. Default value: **1**.
        self.page_number = page_number  # type: str
        # The number of entries to return on each page.\
        # Maximum value: 100. Default value: 20. If you leave this parameter empty, 20 entries are returned on each page.
        # 
        # > We recommend that you do not leave this parameter empty.
        self.page_size = page_size  # type: str
        # The region ID of the bastion host on which you want to query the host accounts to be managed by the specified user group on the specified host.
        # 
        # > For more information about the mapping between region IDs and region names, see [Regions and zones](~~40654~~).
        self.region_id = region_id  # type: str
        # The ID of the user group for which you want to query authorized host accounts.
        # 
        # > You can call the [ListUserGroups](~~204509~~) operation to query the ID of the user group.
        self.user_group_id = user_group_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListHostAccountsForUserGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.host_account_name is not None:
            result['HostAccountName'] = self.host_account_name
        if self.host_id is not None:
            result['HostId'] = self.host_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.user_group_id is not None:
            result['UserGroupId'] = self.user_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('HostAccountName') is not None:
            self.host_account_name = m.get('HostAccountName')
        if m.get('HostId') is not None:
            self.host_id = m.get('HostId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('UserGroupId') is not None:
            self.user_group_id = m.get('UserGroupId')
        return self


class ListHostAccountsForUserGroupResponseBodyHostAccounts(TeaModel):
    def __init__(self, host_account_id=None, host_account_name=None, host_id=None, is_authorized=None,
                 protocol_name=None):
        # The ID of the host account.
        self.host_account_id = host_account_id  # type: str
        # The name of the host account.
        self.host_account_name = host_account_name  # type: str
        # The ID of the host for which the host accounts were queried.
        self.host_id = host_id  # type: str
        # Indicates whether the user group is authorized to manage the host account. Valid values:
        # 
        # *   **true**: yes
        # *   **false**: no
        self.is_authorized = is_authorized  # type: bool
        # The protocol that is used by the host. Valid values:
        # 
        # *   **SSH**\
        # *   **RDP**\
        self.protocol_name = protocol_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListHostAccountsForUserGroupResponseBodyHostAccounts, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.host_account_id is not None:
            result['HostAccountId'] = self.host_account_id
        if self.host_account_name is not None:
            result['HostAccountName'] = self.host_account_name
        if self.host_id is not None:
            result['HostId'] = self.host_id
        if self.is_authorized is not None:
            result['IsAuthorized'] = self.is_authorized
        if self.protocol_name is not None:
            result['ProtocolName'] = self.protocol_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('HostAccountId') is not None:
            self.host_account_id = m.get('HostAccountId')
        if m.get('HostAccountName') is not None:
            self.host_account_name = m.get('HostAccountName')
        if m.get('HostId') is not None:
            self.host_id = m.get('HostId')
        if m.get('IsAuthorized') is not None:
            self.is_authorized = m.get('IsAuthorized')
        if m.get('ProtocolName') is not None:
            self.protocol_name = m.get('ProtocolName')
        return self


class ListHostAccountsForUserGroupResponseBody(TeaModel):
    def __init__(self, host_accounts=None, request_id=None, total_count=None):
        # An array that consists of the queried host accounts.
        self.host_accounts = host_accounts  # type: list[ListHostAccountsForUserGroupResponseBodyHostAccounts]
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The total number of host accounts that were queried.
        self.total_count = total_count  # type: int

    def validate(self):
        if self.host_accounts:
            for k in self.host_accounts:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListHostAccountsForUserGroupResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['HostAccounts'] = []
        if self.host_accounts is not None:
            for k in self.host_accounts:
                result['HostAccounts'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.host_accounts = []
        if m.get('HostAccounts') is not None:
            for k in m.get('HostAccounts'):
                temp_model = ListHostAccountsForUserGroupResponseBodyHostAccounts()
                self.host_accounts.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListHostAccountsForUserGroupResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListHostAccountsForUserGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListHostAccountsForUserGroupResponse, self).to_map()
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
            temp_model = ListHostAccountsForUserGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListHostGroupAccountNamesForUserRequest(TeaModel):
    def __init__(self, host_group_id=None, instance_id=None, region_id=None, user_id=None):
        # The ID of the host group.
        # 
        # > You can call the [ListHostGroups](~~201307~~) operation to query the ID of the host group.
        self.host_group_id = host_group_id  # type: str
        # The ID of the bastion host to which the user belongs.
        # 
        # > You can call the [DescribeInstances](~~153281~~) operation to query the ID of the bastion host.
        self.instance_id = instance_id  # type: str
        # The region ID of the bastion host to which the user belongs.
        # 
        # > For more information about the mapping between region IDs and region names, see [Regions and zones](~~40654~~).
        self.region_id = region_id  # type: str
        # The ID of the user.
        # 
        # > You can call the [ListUsers](~~204522~~) operation to query the ID of the user.
        self.user_id = user_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListHostGroupAccountNamesForUserRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.host_group_id is not None:
            result['HostGroupId'] = self.host_group_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('HostGroupId') is not None:
            self.host_group_id = m.get('HostGroupId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class ListHostGroupAccountNamesForUserResponseBody(TeaModel):
    def __init__(self, host_account_names=None, request_id=None):
        # An array that consists of the names of host accounts.
        self.host_account_names = host_account_names  # type: list[str]
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListHostGroupAccountNamesForUserResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.host_account_names is not None:
            result['HostAccountNames'] = self.host_account_names
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('HostAccountNames') is not None:
            self.host_account_names = m.get('HostAccountNames')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListHostGroupAccountNamesForUserResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListHostGroupAccountNamesForUserResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListHostGroupAccountNamesForUserResponse, self).to_map()
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
            temp_model = ListHostGroupAccountNamesForUserResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListHostGroupAccountNamesForUserGroupRequest(TeaModel):
    def __init__(self, host_group_id=None, instance_id=None, region_id=None, user_group_id=None):
        # WB662865
        self.host_group_id = host_group_id  # type: str
        # All Bastionhost API requests must include common request parameters. For more information about common request parameters, see [Common parameters](~~148139~~).
        # 
        # For more information about sample requests, see the "Examples" section of this topic.
        self.instance_id = instance_id  # type: str
        # Queries the names of the host accounts that a specified user group is authorized to manage in a specified host group.
        self.region_id = region_id  # type: str
        # ListHostGroupAccountNamesForUserGroup
        self.user_group_id = user_group_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListHostGroupAccountNamesForUserGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.host_group_id is not None:
            result['HostGroupId'] = self.host_group_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.user_group_id is not None:
            result['UserGroupId'] = self.user_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('HostGroupId') is not None:
            self.host_group_id = m.get('HostGroupId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('UserGroupId') is not None:
            self.user_group_id = m.get('UserGroupId')
        return self


class ListHostGroupAccountNamesForUserGroupResponseBody(TeaModel):
    def __init__(self, host_account_names=None, request_id=None):
        self.host_account_names = host_account_names  # type: list[str]
        # ListHostGroupAccountNamesForUserGroup
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListHostGroupAccountNamesForUserGroupResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.host_account_names is not None:
            result['HostAccountNames'] = self.host_account_names
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('HostAccountNames') is not None:
            self.host_account_names = m.get('HostAccountNames')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class ListHostGroupAccountNamesForUserGroupResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListHostGroupAccountNamesForUserGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListHostGroupAccountNamesForUserGroupResponse, self).to_map()
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
            temp_model = ListHostGroupAccountNamesForUserGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListHostGroupsRequest(TeaModel):
    def __init__(self, host_group_name=None, instance_id=None, page_number=None, page_size=None, region_id=None):
        # The name of the host group that you want to query. Only exact match is supported.
        self.host_group_name = host_group_name  # type: str
        # The ID of the bastion host in which you want to query the host group.
        # 
        # > You can call the [DescribeInstances](~~153281~~) operation to query the ID of the bastion host.
        self.instance_id = instance_id  # type: str
        # The number of the page to return. Default value: **1**.
        self.page_number = page_number  # type: str
        # The number of entries to return on each page.\
        # Maximum value: 100. Default value: 20. If you leave this parameter empty, 20 entries are returned on each page.
        # 
        # > We recommend that you do not leave this parameter empty.
        self.page_size = page_size  # type: str
        # The region ID of the bastion host in which you want to query the host group.
        # 
        # > For more information about the mapping between region IDs and region names, see [Regions and zones](~~40654~~).
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListHostGroupsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.host_group_name is not None:
            result['HostGroupName'] = self.host_group_name
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('HostGroupName') is not None:
            self.host_group_name = m.get('HostGroupName')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListHostGroupsResponseBodyHostGroups(TeaModel):
    def __init__(self, comment=None, host_group_id=None, host_group_name=None, member_count=None):
        # The description of the host group.
        self.comment = comment  # type: str
        # The ID of the host group.
        self.host_group_id = host_group_id  # type: str
        # The name of the host group.
        self.host_group_name = host_group_name  # type: str
        # The number of hosts in the host group.
        self.member_count = member_count  # type: int

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListHostGroupsResponseBodyHostGroups, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.comment is not None:
            result['Comment'] = self.comment
        if self.host_group_id is not None:
            result['HostGroupId'] = self.host_group_id
        if self.host_group_name is not None:
            result['HostGroupName'] = self.host_group_name
        if self.member_count is not None:
            result['MemberCount'] = self.member_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')
        if m.get('HostGroupId') is not None:
            self.host_group_id = m.get('HostGroupId')
        if m.get('HostGroupName') is not None:
            self.host_group_name = m.get('HostGroupName')
        if m.get('MemberCount') is not None:
            self.member_count = m.get('MemberCount')
        return self


class ListHostGroupsResponseBody(TeaModel):
    def __init__(self, host_groups=None, request_id=None, total_count=None):
        # An array that consists of the host groups.
        self.host_groups = host_groups  # type: list[ListHostGroupsResponseBodyHostGroups]
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The total number of host groups returned.
        self.total_count = total_count  # type: int

    def validate(self):
        if self.host_groups:
            for k in self.host_groups:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListHostGroupsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['HostGroups'] = []
        if self.host_groups is not None:
            for k in self.host_groups:
                result['HostGroups'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.host_groups = []
        if m.get('HostGroups') is not None:
            for k in m.get('HostGroups'):
                temp_model = ListHostGroupsResponseBodyHostGroups()
                self.host_groups.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListHostGroupsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListHostGroupsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListHostGroupsResponse, self).to_map()
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
            temp_model = ListHostGroupsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListHostGroupsForUserRequest(TeaModel):
    def __init__(self, host_group_name=None, instance_id=None, mode=None, page_number=None, page_size=None,
                 region_id=None, user_id=None):
        # The ID of the request.
        self.host_group_name = host_group_name  # type: str
        # The host groups returned.
        self.instance_id = instance_id  # type: str
        # The number of entries to return on each page.
        # 
        # The value of the PageSize parameter must not exceed 100. Default value: 20. If you leave the PageSize parameter empty, 20 entries are returned on each page.
        # 
        # >  We recommend that you do not leave the PageSize parameter empty.
        self.mode = mode  # type: str
        # The ID of the host group.
        self.page_number = page_number  # type: str
        # The ID of the user.
        # 
        # >  You can call the [ListUsers](~~204522~~) operation to query the ID of the user.
        self.page_size = page_size  # type: str
        # The number of the page to return. Default value: **1**.
        self.region_id = region_id  # type: str
        # The ID of the Bastionhost instance where you want to query the host groups that the user is authorized or not authorized to manage.
        # 
        # >  You can call the [DescribeInstances](~~153281~~) operation to query the ID of the Bastionhost instance.
        self.user_id = user_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListHostGroupsForUserRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.host_group_name is not None:
            result['HostGroupName'] = self.host_group_name
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.mode is not None:
            result['Mode'] = self.mode
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('HostGroupName') is not None:
            self.host_group_name = m.get('HostGroupName')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Mode') is not None:
            self.mode = m.get('Mode')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class ListHostGroupsForUserResponseBodyHostGroups(TeaModel):
    def __init__(self, comment=None, host_group_id=None, host_group_name=None):
        # ListHostGroupsForUser
        self.comment = comment  # type: str
        # WB662865
        self.host_group_id = host_group_id  # type: str
        self.host_group_name = host_group_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListHostGroupsForUserResponseBodyHostGroups, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.comment is not None:
            result['Comment'] = self.comment
        if self.host_group_id is not None:
            result['HostGroupId'] = self.host_group_id
        if self.host_group_name is not None:
            result['HostGroupName'] = self.host_group_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')
        if m.get('HostGroupId') is not None:
            self.host_group_id = m.get('HostGroupId')
        if m.get('HostGroupName') is not None:
            self.host_group_name = m.get('HostGroupName')
        return self


class ListHostGroupsForUserResponseBody(TeaModel):
    def __init__(self, host_groups=None, request_id=None, total_count=None):
        # ListHostGroupsForUser
        self.host_groups = host_groups  # type: list[ListHostGroupsForUserResponseBodyHostGroups]
        # Queries the host groups that a specified user is authorized or not authorized to manage.
        self.request_id = request_id  # type: str
        # All Bastionhost API requests must include common request parameters. For more information about common request parameters, see [Common parameters](~~148139~~).
        # 
        # For more information about sample requests, see the "Examples" section of this topic.
        self.total_count = total_count  # type: int

    def validate(self):
        if self.host_groups:
            for k in self.host_groups:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListHostGroupsForUserResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['HostGroups'] = []
        if self.host_groups is not None:
            for k in self.host_groups:
                result['HostGroups'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.host_groups = []
        if m.get('HostGroups') is not None:
            for k in m.get('HostGroups'):
                temp_model = ListHostGroupsForUserResponseBodyHostGroups()
                self.host_groups.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListHostGroupsForUserResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListHostGroupsForUserResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListHostGroupsForUserResponse, self).to_map()
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
            temp_model = ListHostGroupsForUserResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListHostGroupsForUserGroupRequest(TeaModel):
    def __init__(self, host_group_name=None, instance_id=None, mode=None, page_number=None, page_size=None,
                 region_id=None, user_group_id=None):
        # The name of the host group that you want to query. Only exact match is supported.
        self.host_group_name = host_group_name  # type: str
        # The ID of the bastion host to which the user group belongs.
        # 
        # > You can call the [DescribeInstances](~~153281~~) operation to query the ID of the bastion host.
        self.instance_id = instance_id  # type: str
        # Specifies the category of the host group that you want to query. Valid values:
        # 
        # *   **Authorized**: queries the host groups that the user group is authorized to manage. This is the default value.
        # *   **Unauthorized**: queries the host groups that the user group is not authorized to manage.
        self.mode = mode  # type: str
        # The number of the page to return. Default value: **1**.
        self.page_number = page_number  # type: str
        # The number of entries to return on each page.\
        # Maximum value: 100. Default value: 20. If you leave this parameter empty, 20 entries are returned on each page.
        # 
        # > We recommend that you do not leave this parameter empty.
        self.page_size = page_size  # type: str
        # The region ID of the bastion host to which the user group belongs.
        # 
        # > For more information about the mapping between region IDs and region names, see [Regions and zones](~~40654~~).
        self.region_id = region_id  # type: str
        # The ID of the user group.
        # 
        # > You can call the [ListUserGroups](~~204509~~) operation to query the ID of the user group.
        self.user_group_id = user_group_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListHostGroupsForUserGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.host_group_name is not None:
            result['HostGroupName'] = self.host_group_name
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.mode is not None:
            result['Mode'] = self.mode
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.user_group_id is not None:
            result['UserGroupId'] = self.user_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('HostGroupName') is not None:
            self.host_group_name = m.get('HostGroupName')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Mode') is not None:
            self.mode = m.get('Mode')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('UserGroupId') is not None:
            self.user_group_id = m.get('UserGroupId')
        return self


class ListHostGroupsForUserGroupResponseBodyHostGroups(TeaModel):
    def __init__(self, comment=None, host_group_id=None, host_group_name=None):
        # The description of the host group.
        self.comment = comment  # type: str
        # The ID of the host group.
        self.host_group_id = host_group_id  # type: str
        # The name of the host group.
        self.host_group_name = host_group_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListHostGroupsForUserGroupResponseBodyHostGroups, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.comment is not None:
            result['Comment'] = self.comment
        if self.host_group_id is not None:
            result['HostGroupId'] = self.host_group_id
        if self.host_group_name is not None:
            result['HostGroupName'] = self.host_group_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')
        if m.get('HostGroupId') is not None:
            self.host_group_id = m.get('HostGroupId')
        if m.get('HostGroupName') is not None:
            self.host_group_name = m.get('HostGroupName')
        return self


class ListHostGroupsForUserGroupResponseBody(TeaModel):
    def __init__(self, host_groups=None, request_id=None, total_count=None):
        # The host groups returned.
        self.host_groups = host_groups  # type: list[ListHostGroupsForUserGroupResponseBodyHostGroups]
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The total number of host groups returned.
        self.total_count = total_count  # type: int

    def validate(self):
        if self.host_groups:
            for k in self.host_groups:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListHostGroupsForUserGroupResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['HostGroups'] = []
        if self.host_groups is not None:
            for k in self.host_groups:
                result['HostGroups'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.host_groups = []
        if m.get('HostGroups') is not None:
            for k in m.get('HostGroups'):
                temp_model = ListHostGroupsForUserGroupResponseBodyHostGroups()
                self.host_groups.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListHostGroupsForUserGroupResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListHostGroupsForUserGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListHostGroupsForUserGroupResponse, self).to_map()
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
            temp_model = ListHostGroupsForUserGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListHostShareKeysRequest(TeaModel):
    def __init__(self, instance_id=None, page_number=None, page_size=None, region_id=None):
        # The ID of the bastion host. You can call the [DescribeInstances](~~153281~~) operation to query the ID of the bastion host.
        self.instance_id = instance_id  # type: str
        # The number of the page to return. Default value: **1**.
        self.page_number = page_number  # type: str
        # The number of entries to return on each page. Default value: **20**.
        self.page_size = page_size  # type: str
        # The region ID of the bastion host. For more information about the mapping between region IDs and region names, see [Regions and zones](~~40654~~).
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListHostShareKeysRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListHostShareKeysResponseBodyHostShareKeys(TeaModel):
    def __init__(self, host_account_count=None, host_share_key_id=None, host_share_key_name=None,
                 last_modify_key_at=None, private_key_finger_print=None):
        # The number of the associated host accounts.
        self.host_account_count = host_account_count  # type: long
        # The ID of the host account.
        self.host_share_key_id = host_share_key_id  # type: str
        # The name of the shared key.
        self.host_share_key_name = host_share_key_name  # type: str
        # The time when the shared key was last modified.
        self.last_modify_key_at = last_modify_key_at  # type: long
        # The fingerprint of the private key.
        self.private_key_finger_print = private_key_finger_print  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListHostShareKeysResponseBodyHostShareKeys, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.host_account_count is not None:
            result['HostAccountCount'] = self.host_account_count
        if self.host_share_key_id is not None:
            result['HostShareKeyId'] = self.host_share_key_id
        if self.host_share_key_name is not None:
            result['HostShareKeyName'] = self.host_share_key_name
        if self.last_modify_key_at is not None:
            result['LastModifyKeyAt'] = self.last_modify_key_at
        if self.private_key_finger_print is not None:
            result['PrivateKeyFingerPrint'] = self.private_key_finger_print
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('HostAccountCount') is not None:
            self.host_account_count = m.get('HostAccountCount')
        if m.get('HostShareKeyId') is not None:
            self.host_share_key_id = m.get('HostShareKeyId')
        if m.get('HostShareKeyName') is not None:
            self.host_share_key_name = m.get('HostShareKeyName')
        if m.get('LastModifyKeyAt') is not None:
            self.last_modify_key_at = m.get('LastModifyKeyAt')
        if m.get('PrivateKeyFingerPrint') is not None:
            self.private_key_finger_print = m.get('PrivateKeyFingerPrint')
        return self


class ListHostShareKeysResponseBody(TeaModel):
    def __init__(self, host_share_keys=None, request_id=None, total_count=None):
        # An array that consists of the shared keys.
        self.host_share_keys = host_share_keys  # type: list[ListHostShareKeysResponseBodyHostShareKeys]
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id  # type: str
        # The total number of the shared keys.
        self.total_count = total_count  # type: long

    def validate(self):
        if self.host_share_keys:
            for k in self.host_share_keys:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListHostShareKeysResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['HostShareKeys'] = []
        if self.host_share_keys is not None:
            for k in self.host_share_keys:
                result['HostShareKeys'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.host_share_keys = []
        if m.get('HostShareKeys') is not None:
            for k in m.get('HostShareKeys'):
                temp_model = ListHostShareKeysResponseBodyHostShareKeys()
                self.host_share_keys.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListHostShareKeysResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListHostShareKeysResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListHostShareKeysResponse, self).to_map()
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
            temp_model = ListHostShareKeysResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListHostsRequest(TeaModel):
    def __init__(self, host_address=None, host_group_id=None, host_name=None, instance_id=None, ostype=None,
                 page_number=None, page_size=None, region_id=None, source=None, source_instance_id=None,
                 source_instance_state=None):
        # The address of the host that you want to query. You can set this parameter to a domain name or an IP address. Only exact match is supported.
        self.host_address = host_address  # type: str
        # The ID of the host group to which the host to be queried belongs.
        # 
        # > You can call the [ListHostGroups](~~201307~~) operation to query the ID of the host group.
        self.host_group_id = host_group_id  # type: str
        # The name of the host that you want to query. Only exact match is supported.
        self.host_name = host_name  # type: str
        # The ID of the bastion host on which you want to query hosts.
        # 
        # > You can call the [DescribeInstances](~~153281~~) operation to query the ID of the bastion host.
        self.instance_id = instance_id  # type: str
        # The operating system of the host that you want to query. Valid values:
        # 
        # *   **Linux**\
        # *   **Windows**\
        self.ostype = ostype  # type: str
        # The number of the page to return. Default value: **1**.
        self.page_number = page_number  # type: str
        # The number of entries to return on each page. Default value: **10**.
        # 
        # > We recommend that you do not leave this parameter empty.
        self.page_size = page_size  # type: str
        # The region ID of the bastion host on which you want to query hosts.
        # 
        # > For more information about the mapping between region IDs and region names, see [Regions and zones](~~40654~~).
        self.region_id = region_id  # type: str
        # The source of the host that you want to query. Valid values:
        # 
        # *   **Local**: a host in a data center
        # *   **Ecs**: an Elastic Compute Service (ECS) instance
        # *   **Rds**: a host in an ApsaraDB MyBase dedicated cluster
        self.source = source  # type: str
        # The ID of the ECS instance or the host in an ApsaraDB MyBase dedicated cluster that you want to query. Only exact match is supported.
        self.source_instance_id = source_instance_id  # type: str
        # The status of the host that you want to query. Valid values:
        # 
        # *   **Normal**: normal
        # *   **Release**: released
        self.source_instance_state = source_instance_state  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListHostsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.host_address is not None:
            result['HostAddress'] = self.host_address
        if self.host_group_id is not None:
            result['HostGroupId'] = self.host_group_id
        if self.host_name is not None:
            result['HostName'] = self.host_name
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.ostype is not None:
            result['OSType'] = self.ostype
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.source is not None:
            result['Source'] = self.source
        if self.source_instance_id is not None:
            result['SourceInstanceId'] = self.source_instance_id
        if self.source_instance_state is not None:
            result['SourceInstanceState'] = self.source_instance_state
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('HostAddress') is not None:
            self.host_address = m.get('HostAddress')
        if m.get('HostGroupId') is not None:
            self.host_group_id = m.get('HostGroupId')
        if m.get('HostName') is not None:
            self.host_name = m.get('HostName')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('OSType') is not None:
            self.ostype = m.get('OSType')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('SourceInstanceId') is not None:
            self.source_instance_id = m.get('SourceInstanceId')
        if m.get('SourceInstanceState') is not None:
            self.source_instance_state = m.get('SourceInstanceState')
        return self


class ListHostsResponseBodyHosts(TeaModel):
    def __init__(self, active_address_type=None, comment=None, host_account_count=None, host_id=None,
                 host_name=None, host_private_address=None, host_public_address=None, ostype=None, source=None,
                 source_instance_id=None, source_instance_state=None):
        # The address type of the host. Valid values:
        # 
        # *   **Public**: a public address
        # *   **Private**: a private address
        self.active_address_type = active_address_type  # type: str
        # The description of the host.
        self.comment = comment  # type: str
        # The number of host accounts.
        self.host_account_count = host_account_count  # type: int
        # The ID of the host.
        self.host_id = host_id  # type: str
        # The name of the host.
        self.host_name = host_name  # type: str
        # The private address of the host. The value is a domain name or an IP address.
        self.host_private_address = host_private_address  # type: str
        # The public address of the host. The value is a domain name or an IP address.
        self.host_public_address = host_public_address  # type: str
        # The operating system of the host. Valid values:
        # 
        # *   **Linux**\
        # *   **Windows**\
        self.ostype = ostype  # type: str
        # The source of the host. Valid values:
        # 
        # *   **Local**: a host in a data center
        # *   **Ecs**: an ECS instance
        # *   **Rds**: a host in an ApsaraDB MyBase dedicated cluster
        self.source = source  # type: str
        # The ID of the ECS instance or the host in an ApsaraDB MyBase dedicated cluster.
        # 
        # > No value is returned for this parameter if the **Source** parameter is set to **Local**.
        self.source_instance_id = source_instance_id  # type: str
        # The status of the host. Valid values:
        # 
        # *   **Normal**: normal
        # *   **Release**: released
        self.source_instance_state = source_instance_state  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListHostsResponseBodyHosts, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.active_address_type is not None:
            result['ActiveAddressType'] = self.active_address_type
        if self.comment is not None:
            result['Comment'] = self.comment
        if self.host_account_count is not None:
            result['HostAccountCount'] = self.host_account_count
        if self.host_id is not None:
            result['HostId'] = self.host_id
        if self.host_name is not None:
            result['HostName'] = self.host_name
        if self.host_private_address is not None:
            result['HostPrivateAddress'] = self.host_private_address
        if self.host_public_address is not None:
            result['HostPublicAddress'] = self.host_public_address
        if self.ostype is not None:
            result['OSType'] = self.ostype
        if self.source is not None:
            result['Source'] = self.source
        if self.source_instance_id is not None:
            result['SourceInstanceId'] = self.source_instance_id
        if self.source_instance_state is not None:
            result['SourceInstanceState'] = self.source_instance_state
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ActiveAddressType') is not None:
            self.active_address_type = m.get('ActiveAddressType')
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')
        if m.get('HostAccountCount') is not None:
            self.host_account_count = m.get('HostAccountCount')
        if m.get('HostId') is not None:
            self.host_id = m.get('HostId')
        if m.get('HostName') is not None:
            self.host_name = m.get('HostName')
        if m.get('HostPrivateAddress') is not None:
            self.host_private_address = m.get('HostPrivateAddress')
        if m.get('HostPublicAddress') is not None:
            self.host_public_address = m.get('HostPublicAddress')
        if m.get('OSType') is not None:
            self.ostype = m.get('OSType')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('SourceInstanceId') is not None:
            self.source_instance_id = m.get('SourceInstanceId')
        if m.get('SourceInstanceState') is not None:
            self.source_instance_state = m.get('SourceInstanceState')
        return self


class ListHostsResponseBody(TeaModel):
    def __init__(self, hosts=None, request_id=None, total_count=None):
        # An array that consists of the hosts returned.
        self.hosts = hosts  # type: list[ListHostsResponseBodyHosts]
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id  # type: str
        # The total number of hosts returned.
        self.total_count = total_count  # type: int

    def validate(self):
        if self.hosts:
            for k in self.hosts:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListHostsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Hosts'] = []
        if self.hosts is not None:
            for k in self.hosts:
                result['Hosts'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.hosts = []
        if m.get('Hosts') is not None:
            for k in m.get('Hosts'):
                temp_model = ListHostsResponseBodyHosts()
                self.hosts.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListHostsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListHostsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListHostsResponse, self).to_map()
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
            temp_model = ListHostsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListHostsForUserRequest(TeaModel):
    def __init__(self, host_address=None, host_name=None, instance_id=None, mode=None, ostype=None, page_number=None,
                 page_size=None, region_id=None, user_id=None):
        # The operating system of the host that you want to query. Valid values:
        # 
        # *   **Linux**\
        # *   **Windows**\
        self.host_address = host_address  # type: str
        # The ID of the Bastionhost instance where you want to query the hosts that the user is authorized or not authorized to manage.
        # 
        # >  You can call the [DescribeInstances](~~153281~~) operation to query the ID of the Bastionhost instance.
        self.host_name = host_name  # type: str
        # The category of the host that you want to query. Valid values:
        # 
        # *   **Authorized**: Query the hosts that the user is authorized to manage. This is the default value.
        # *   **Unauthorized**: Query the hosts that the user is not authorized to manage.
        self.instance_id = instance_id  # type: str
        # The operating system of the host. Valid values:
        # 
        # *   **Linux**\
        # *   **Windows**\
        self.mode = mode  # type: str
        # The internal endpoint of the host. The value is a domain name or an IP address.
        self.ostype = ostype  # type: str
        # The endpoint type of the host. Valid values:
        # 
        # *   **Public**: a public endpoint
        # *   **Private**: an internal endpoint
        self.page_number = page_number  # type: str
        # The number of entries to return on each page.
        # 
        # The value of the PageSize parameter must not exceed 100. Default value: 20. If you leave the PageSize parameter empty, 20 entries are returned on each page.
        # 
        # >  We recommend that you do not leave the PageSize parameter empty.
        self.page_size = page_size  # type: str
        # The endpoint of the host that you want to query. You can set this parameter to a domain name or an IP address. Only exact match is supported.
        self.region_id = region_id  # type: str
        # The number of the page to return. Default value: 1.
        self.user_id = user_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListHostsForUserRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.host_address is not None:
            result['HostAddress'] = self.host_address
        if self.host_name is not None:
            result['HostName'] = self.host_name
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.mode is not None:
            result['Mode'] = self.mode
        if self.ostype is not None:
            result['OSType'] = self.ostype
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('HostAddress') is not None:
            self.host_address = m.get('HostAddress')
        if m.get('HostName') is not None:
            self.host_name = m.get('HostName')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Mode') is not None:
            self.mode = m.get('Mode')
        if m.get('OSType') is not None:
            self.ostype = m.get('OSType')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class ListHostsForUserResponseBodyHosts(TeaModel):
    def __init__(self, active_address_type=None, comment=None, host_id=None, host_name=None,
                 host_private_address=None, host_public_address=None, ostype=None):
        # All Bastionhost API requests must include common request parameters. For more information about common request parameters, see [Common parameters](~~148139~~).
        # 
        # For more information about sample requests, see the "Examples" section of this topic.
        self.active_address_type = active_address_type  # type: str
        # The ID of the request.
        self.comment = comment  # type: str
        self.host_id = host_id  # type: str
        # ListHostsForUser
        self.host_name = host_name  # type: str
        # WB662865
        self.host_private_address = host_private_address  # type: str
        # Queries the hosts that a specified user is authorized or not authorized to manage.
        self.host_public_address = host_public_address  # type: str
        # ListHostsForUser
        self.ostype = ostype  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListHostsForUserResponseBodyHosts, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.active_address_type is not None:
            result['ActiveAddressType'] = self.active_address_type
        if self.comment is not None:
            result['Comment'] = self.comment
        if self.host_id is not None:
            result['HostId'] = self.host_id
        if self.host_name is not None:
            result['HostName'] = self.host_name
        if self.host_private_address is not None:
            result['HostPrivateAddress'] = self.host_private_address
        if self.host_public_address is not None:
            result['HostPublicAddress'] = self.host_public_address
        if self.ostype is not None:
            result['OSType'] = self.ostype
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ActiveAddressType') is not None:
            self.active_address_type = m.get('ActiveAddressType')
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')
        if m.get('HostId') is not None:
            self.host_id = m.get('HostId')
        if m.get('HostName') is not None:
            self.host_name = m.get('HostName')
        if m.get('HostPrivateAddress') is not None:
            self.host_private_address = m.get('HostPrivateAddress')
        if m.get('HostPublicAddress') is not None:
            self.host_public_address = m.get('HostPublicAddress')
        if m.get('OSType') is not None:
            self.ostype = m.get('OSType')
        return self


class ListHostsForUserResponseBody(TeaModel):
    def __init__(self, hosts=None, request_id=None, total_count=None):
        # The ID of the user.
        # 
        # >  You can call the [ListUsers](~~204522~~) operation to query the ID of the user ID.
        self.hosts = hosts  # type: list[ListHostsForUserResponseBodyHosts]
        # The hosts returned.
        self.request_id = request_id  # type: str
        # The public endpoint of the host. The value is a domain name or an IP address.
        self.total_count = total_count  # type: int

    def validate(self):
        if self.hosts:
            for k in self.hosts:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListHostsForUserResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Hosts'] = []
        if self.hosts is not None:
            for k in self.hosts:
                result['Hosts'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.hosts = []
        if m.get('Hosts') is not None:
            for k in m.get('Hosts'):
                temp_model = ListHostsForUserResponseBodyHosts()
                self.hosts.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListHostsForUserResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListHostsForUserResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListHostsForUserResponse, self).to_map()
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
            temp_model = ListHostsForUserResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListHostsForUserGroupRequest(TeaModel):
    def __init__(self, host_address=None, host_name=None, instance_id=None, mode=None, ostype=None, page_number=None,
                 page_size=None, region_id=None, user_group_id=None):
        # The operating system of the host that you want to query. Valid values:
        # 
        # *   **Linux**\
        # *   **Windows**\
        self.host_address = host_address  # type: str
        # The ID of the Bastionhost instance where you want to query the hosts that the user group is authorized or not authorized to manage.
        # 
        # >  You can call the [DescribeInstances](~~153281~~) operation to query the ID of the Bastionhost instance.
        self.host_name = host_name  # type: str
        # The category of the host that you want to query. Valid values:
        # 
        # *   **Authorized**: Query the hosts that the user group is authorized to manage. This is the default value.
        # *   **Unauthorized**: Query the hosts that the user group is not authorized to manage.
        self.instance_id = instance_id  # type: str
        # The operating system of the host. Valid values:
        # 
        # *   **Linux**\
        # *   **Windows**\
        self.mode = mode  # type: str
        # The internal endpoint of the host. The value is a domain name or an IP address.
        self.ostype = ostype  # type: str
        # The endpoint type of the host. Valid values:
        # 
        # *   **Public**: a public endpoint
        # *   **Private**: an internal endpoint
        self.page_number = page_number  # type: str
        # The number of entries to return on each page.
        # 
        # The value of the PageSize parameter must not exceed 100. Default value: 20. If you leave the PageSize parameter empty, 20 entries are returned on each page.
        # 
        # >  We recommend that you do not leave the PageSize parameter empty.
        self.page_size = page_size  # type: str
        # The endpoint of the host that you want to query. You can set this parameter to a domain name or an IP address. Only exact match is supported.
        self.region_id = region_id  # type: str
        # The number of the page to return. Default value: 1.
        self.user_group_id = user_group_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListHostsForUserGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.host_address is not None:
            result['HostAddress'] = self.host_address
        if self.host_name is not None:
            result['HostName'] = self.host_name
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.mode is not None:
            result['Mode'] = self.mode
        if self.ostype is not None:
            result['OSType'] = self.ostype
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.user_group_id is not None:
            result['UserGroupId'] = self.user_group_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('HostAddress') is not None:
            self.host_address = m.get('HostAddress')
        if m.get('HostName') is not None:
            self.host_name = m.get('HostName')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Mode') is not None:
            self.mode = m.get('Mode')
        if m.get('OSType') is not None:
            self.ostype = m.get('OSType')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('UserGroupId') is not None:
            self.user_group_id = m.get('UserGroupId')
        return self


class ListHostsForUserGroupResponseBodyHosts(TeaModel):
    def __init__(self, active_address_type=None, comment=None, host_id=None, host_name=None,
                 host_private_address=None, host_public_address=None, ostype=None):
        # All Bastionhost API requests must include common request parameters. For more information about common request parameters, see [Common parameters](~~148139~~).
        # 
        # For more information about sample requests, see the "Examples" section of this topic.
        self.active_address_type = active_address_type  # type: str
        # The ID of the request.
        self.comment = comment  # type: str
        self.host_id = host_id  # type: str
        # ListHostsForUserGroup
        self.host_name = host_name  # type: str
        # WB662865
        self.host_private_address = host_private_address  # type: str
        # Queries the hosts that a specified user group is authorized or not authorized to manage.
        self.host_public_address = host_public_address  # type: str
        # ListHostsForUserGroup
        self.ostype = ostype  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListHostsForUserGroupResponseBodyHosts, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.active_address_type is not None:
            result['ActiveAddressType'] = self.active_address_type
        if self.comment is not None:
            result['Comment'] = self.comment
        if self.host_id is not None:
            result['HostId'] = self.host_id
        if self.host_name is not None:
            result['HostName'] = self.host_name
        if self.host_private_address is not None:
            result['HostPrivateAddress'] = self.host_private_address
        if self.host_public_address is not None:
            result['HostPublicAddress'] = self.host_public_address
        if self.ostype is not None:
            result['OSType'] = self.ostype
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ActiveAddressType') is not None:
            self.active_address_type = m.get('ActiveAddressType')
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')
        if m.get('HostId') is not None:
            self.host_id = m.get('HostId')
        if m.get('HostName') is not None:
            self.host_name = m.get('HostName')
        if m.get('HostPrivateAddress') is not None:
            self.host_private_address = m.get('HostPrivateAddress')
        if m.get('HostPublicAddress') is not None:
            self.host_public_address = m.get('HostPublicAddress')
        if m.get('OSType') is not None:
            self.ostype = m.get('OSType')
        return self


class ListHostsForUserGroupResponseBody(TeaModel):
    def __init__(self, hosts=None, request_id=None, total_count=None):
        # The ID of the user group for which you want to query hosts.
        # 
        # >  You can call the [ListUserGroups](~~204509~~) operation to query the ID of the user group.
        self.hosts = hosts  # type: list[ListHostsForUserGroupResponseBodyHosts]
        # The hosts returned.
        self.request_id = request_id  # type: str
        # The public endpoint of the host. The value is a domain name or an IP address.
        self.total_count = total_count  # type: int

    def validate(self):
        if self.hosts:
            for k in self.hosts:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListHostsForUserGroupResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['Hosts'] = []
        if self.hosts is not None:
            for k in self.hosts:
                result['Hosts'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.hosts = []
        if m.get('Hosts') is not None:
            for k in m.get('Hosts'):
                temp_model = ListHostsForUserGroupResponseBodyHosts()
                self.hosts.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListHostsForUserGroupResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListHostsForUserGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListHostsForUserGroupResponse, self).to_map()
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
            temp_model = ListHostsForUserGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListOperationTicketsRequest(TeaModel):
    def __init__(self, asset_address=None, instance_id=None, page_number=None, page_size=None, region_id=None):
        self.asset_address = asset_address  # type: str
        self.instance_id = instance_id  # type: str
        self.page_number = page_number  # type: str
        self.page_size = page_size  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListOperationTicketsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.asset_address is not None:
            result['AssetAddress'] = self.asset_address
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AssetAddress') is not None:
            self.asset_address = m.get('AssetAddress')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ListOperationTicketsResponseBodyOperationTickets(TeaModel):
    def __init__(self, apply_user_id=None, apply_username=None, asset_account_id=None, asset_account_name=None,
                 asset_address=None, asset_id=None, asset_name=None, asset_network_domain_id=None, asset_os=None,
                 asset_source=None, asset_source_instance_id=None, created_time=None, operation_ticket_id=None,
                 protocol_name=None, state=None):
        self.apply_user_id = apply_user_id  # type: str
        self.apply_username = apply_username  # type: str
        self.asset_account_id = asset_account_id  # type: str
        self.asset_account_name = asset_account_name  # type: str
        self.asset_address = asset_address  # type: str
        self.asset_id = asset_id  # type: str
        self.asset_name = asset_name  # type: str
        self.asset_network_domain_id = asset_network_domain_id  # type: str
        self.asset_os = asset_os  # type: str
        self.asset_source = asset_source  # type: str
        self.asset_source_instance_id = asset_source_instance_id  # type: str
        self.created_time = created_time  # type: long
        self.operation_ticket_id = operation_ticket_id  # type: str
        self.protocol_name = protocol_name  # type: str
        self.state = state  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListOperationTicketsResponseBodyOperationTickets, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.apply_user_id is not None:
            result['ApplyUserId'] = self.apply_user_id
        if self.apply_username is not None:
            result['ApplyUsername'] = self.apply_username
        if self.asset_account_id is not None:
            result['AssetAccountId'] = self.asset_account_id
        if self.asset_account_name is not None:
            result['AssetAccountName'] = self.asset_account_name
        if self.asset_address is not None:
            result['AssetAddress'] = self.asset_address
        if self.asset_id is not None:
            result['AssetId'] = self.asset_id
        if self.asset_name is not None:
            result['AssetName'] = self.asset_name
        if self.asset_network_domain_id is not None:
            result['AssetNetworkDomainId'] = self.asset_network_domain_id
        if self.asset_os is not None:
            result['AssetOs'] = self.asset_os
        if self.asset_source is not None:
            result['AssetSource'] = self.asset_source
        if self.asset_source_instance_id is not None:
            result['AssetSourceInstanceId'] = self.asset_source_instance_id
        if self.created_time is not None:
            result['CreatedTime'] = self.created_time
        if self.operation_ticket_id is not None:
            result['OperationTicketId'] = self.operation_ticket_id
        if self.protocol_name is not None:
            result['ProtocolName'] = self.protocol_name
        if self.state is not None:
            result['State'] = self.state
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ApplyUserId') is not None:
            self.apply_user_id = m.get('ApplyUserId')
        if m.get('ApplyUsername') is not None:
            self.apply_username = m.get('ApplyUsername')
        if m.get('AssetAccountId') is not None:
            self.asset_account_id = m.get('AssetAccountId')
        if m.get('AssetAccountName') is not None:
            self.asset_account_name = m.get('AssetAccountName')
        if m.get('AssetAddress') is not None:
            self.asset_address = m.get('AssetAddress')
        if m.get('AssetId') is not None:
            self.asset_id = m.get('AssetId')
        if m.get('AssetName') is not None:
            self.asset_name = m.get('AssetName')
        if m.get('AssetNetworkDomainId') is not None:
            self.asset_network_domain_id = m.get('AssetNetworkDomainId')
        if m.get('AssetOs') is not None:
            self.asset_os = m.get('AssetOs')
        if m.get('AssetSource') is not None:
            self.asset_source = m.get('AssetSource')
        if m.get('AssetSourceInstanceId') is not None:
            self.asset_source_instance_id = m.get('AssetSourceInstanceId')
        if m.get('CreatedTime') is not None:
            self.created_time = m.get('CreatedTime')
        if m.get('OperationTicketId') is not None:
            self.operation_ticket_id = m.get('OperationTicketId')
        if m.get('ProtocolName') is not None:
            self.protocol_name = m.get('ProtocolName')
        if m.get('State') is not None:
            self.state = m.get('State')
        return self


class ListOperationTicketsResponseBody(TeaModel):
    def __init__(self, operation_tickets=None, request_id=None, total_count=None):
        self.operation_tickets = operation_tickets  # type: list[ListOperationTicketsResponseBodyOperationTickets]
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: long

    def validate(self):
        if self.operation_tickets:
            for k in self.operation_tickets:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListOperationTicketsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['OperationTickets'] = []
        if self.operation_tickets is not None:
            for k in self.operation_tickets:
                result['OperationTickets'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.operation_tickets = []
        if m.get('OperationTickets') is not None:
            for k in m.get('OperationTickets'):
                temp_model = ListOperationTicketsResponseBodyOperationTickets()
                self.operation_tickets.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListOperationTicketsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListOperationTicketsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListOperationTicketsResponse, self).to_map()
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
            temp_model = ListOperationTicketsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTagKeysRequest(TeaModel):
    def __init__(self, page_number=None, page_size=None, region_id=None, resource_type=None):
        # The number of the page to return.
        self.page_number = page_number  # type: int
        # The number of entries to return on each page.
        self.page_size = page_size  # type: int
        # The region ID of the bastion host.
        self.region_id = region_id  # type: str
        # The type of the resource.
        # 
        # Set the value to INSTANCE, which indicates that the resource is a bastion host.
        self.resource_type = resource_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListTagKeysRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        return self


class ListTagKeysResponseBodyTagKeys(TeaModel):
    def __init__(self, tag_count=None, tag_key=None):
        # The total number of tag keys.
        self.tag_count = tag_count  # type: int
        # The name of the tag key.
        self.tag_key = tag_key  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListTagKeysResponseBodyTagKeys, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.tag_count is not None:
            result['TagCount'] = self.tag_count
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('TagCount') is not None:
            self.tag_count = m.get('TagCount')
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        return self


class ListTagKeysResponseBody(TeaModel):
    def __init__(self, page_number=None, page_size=None, request_id=None, tag_keys=None, total_count=None):
        # The page number of the returned page.
        self.page_number = page_number  # type: int
        # The number of entries returned per page.
        self.page_size = page_size  # type: int
        # The ID of the request.
        self.request_id = request_id  # type: str
        # An array that consists of tags.
        self.tag_keys = tag_keys  # type: list[ListTagKeysResponseBodyTagKeys]
        # The total number of tags returned.
        self.total_count = total_count  # type: int

    def validate(self):
        if self.tag_keys:
            for k in self.tag_keys:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListTagKeysResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['TagKeys'] = []
        if self.tag_keys is not None:
            for k in self.tag_keys:
                result['TagKeys'].append(k.to_map() if k else None)
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.tag_keys = []
        if m.get('TagKeys') is not None:
            for k in m.get('TagKeys'):
                temp_model = ListTagKeysResponseBodyTagKeys()
                self.tag_keys.append(temp_model.from_map(k))
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListTagKeysResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListTagKeysResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListTagKeysResponse, self).to_map()
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
            temp_model = ListTagKeysResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTagResourcesRequestTag(TeaModel):
    def __init__(self, key=None, value=None):
        # The ID of the request.
        self.key = key  # type: str
        # The type of the resource.
        # 
        # The returned value is INSTANCE, which indicates that the resource is a Bastionhost instance.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListTagResourcesRequestTag, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class ListTagResourcesRequest(TeaModel):
    def __init__(self, next_token=None, region_id=None, resource_id=None, resource_type=None, tag=None):
        # The region ID of the Bastionhost instance.
        self.next_token = next_token  # type: str
        # The ID of the instance.
        self.region_id = region_id  # type: str
        # The value of the tag.
        self.resource_id = resource_id  # type: list[str]
        # The operation that you want to perform.
        # 
        # Set the value to **ListTagResources**.
        self.resource_type = resource_type  # type: str
        # The key of tag N.
        # 
        # Valid values of N: 1 to 20.
        self.tag = tag  # type: list[ListTagResourcesRequestTag]

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListTagResourcesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = ListTagResourcesRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class ListTagResourcesResponseBodyTagResources(TeaModel):
    def __init__(self, resource_id=None, resource_type=None, tag_key=None, tag_value=None):
        self.resource_id = resource_id  # type: str
        self.resource_type = resource_type  # type: str
        self.tag_key = tag_key  # type: str
        self.tag_value = tag_value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListTagResourcesResponseBodyTagResources, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        if self.tag_value is not None:
            result['TagValue'] = self.tag_value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        if m.get('TagValue') is not None:
            self.tag_value = m.get('TagValue')
        return self


class ListTagResourcesResponseBody(TeaModel):
    def __init__(self, next_token=None, request_id=None, tag_resources=None):
        # Queries the tags bound to one or more Bastionhost instances.
        self.next_token = next_token  # type: str
        # ListTagResources
        self.request_id = request_id  # type: str
        # 58928
        self.tag_resources = tag_resources  # type: list[ListTagResourcesResponseBodyTagResources]

    def validate(self):
        if self.tag_resources:
            for k in self.tag_resources:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListTagResourcesResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.next_token is not None:
            result['NextToken'] = self.next_token
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['TagResources'] = []
        if self.tag_resources is not None:
            for k in self.tag_resources:
                result['TagResources'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('NextToken') is not None:
            self.next_token = m.get('NextToken')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.tag_resources = []
        if m.get('TagResources') is not None:
            for k in m.get('TagResources'):
                temp_model = ListTagResourcesResponseBodyTagResources()
                self.tag_resources.append(temp_model.from_map(k))
        return self


class ListTagResourcesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListTagResourcesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListTagResourcesResponse, self).to_map()
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
            temp_model = ListTagResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListUserGroupsRequest(TeaModel):
    def __init__(self, instance_id=None, page_number=None, page_size=None, region_id=None, user_group_name=None):
        self.instance_id = instance_id  # type: str
        self.page_number = page_number  # type: str
        self.page_size = page_size  # type: str
        self.region_id = region_id  # type: str
        self.user_group_name = user_group_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListUserGroupsRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.user_group_name is not None:
            result['UserGroupName'] = self.user_group_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('UserGroupName') is not None:
            self.user_group_name = m.get('UserGroupName')
        return self


class ListUserGroupsResponseBodyUserGroups(TeaModel):
    def __init__(self, comment=None, member_count=None, user_group_id=None, user_group_name=None):
        self.comment = comment  # type: str
        self.member_count = member_count  # type: int
        self.user_group_id = user_group_id  # type: str
        self.user_group_name = user_group_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListUserGroupsResponseBodyUserGroups, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.comment is not None:
            result['Comment'] = self.comment
        if self.member_count is not None:
            result['MemberCount'] = self.member_count
        if self.user_group_id is not None:
            result['UserGroupId'] = self.user_group_id
        if self.user_group_name is not None:
            result['UserGroupName'] = self.user_group_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')
        if m.get('MemberCount') is not None:
            self.member_count = m.get('MemberCount')
        if m.get('UserGroupId') is not None:
            self.user_group_id = m.get('UserGroupId')
        if m.get('UserGroupName') is not None:
            self.user_group_name = m.get('UserGroupName')
        return self


class ListUserGroupsResponseBody(TeaModel):
    def __init__(self, request_id=None, total_count=None, user_groups=None):
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: int
        self.user_groups = user_groups  # type: list[ListUserGroupsResponseBodyUserGroups]

    def validate(self):
        if self.user_groups:
            for k in self.user_groups:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListUserGroupsResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        result['UserGroups'] = []
        if self.user_groups is not None:
            for k in self.user_groups:
                result['UserGroups'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        self.user_groups = []
        if m.get('UserGroups') is not None:
            for k in m.get('UserGroups'):
                temp_model = ListUserGroupsResponseBodyUserGroups()
                self.user_groups.append(temp_model.from_map(k))
        return self


class ListUserGroupsResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListUserGroupsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListUserGroupsResponse, self).to_map()
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
            temp_model = ListUserGroupsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListUserPublicKeysRequest(TeaModel):
    def __init__(self, instance_id=None, page_number=None, page_size=None, region_id=None, user_id=None):
        # The ID of the bastion host on which you want to query all public keys of the user.
        # 
        # > You can call the [DescribeInstances](~~153281~~) operation to query the ID of the bastion host.
        self.instance_id = instance_id  # type: str
        # The number of the page to return. Default value: 1.
        self.page_number = page_number  # type: str
        # The number of entries to return on each page.\
        # Maximum value: 100. Default value: 20. If you leave this parameter empty, 20 entries are returned on each page.
        # 
        # > We recommend that you do not leave this parameter empty.
        self.page_size = page_size  # type: str
        # The region ID of the bastion host on which you want to query all public keys of the user.
        # 
        # > For more information about the mapping between region IDs and region names, see [Regions and zones](~~40654~~).
        self.region_id = region_id  # type: str
        # The ID of the user whose public keys you want to query.
        self.user_id = user_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListUserPublicKeysRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class ListUserPublicKeysResponseBodyPublicKeys(TeaModel):
    def __init__(self, comment=None, finger_print=None, public_key_id=None, public_key_name=None, user_id=None):
        # The description of the public key.
        self.comment = comment  # type: str
        # The fingerprint of the public key.
        self.finger_print = finger_print  # type: str
        # The ID of the public key.
        self.public_key_id = public_key_id  # type: str
        # The name of the public key.
        self.public_key_name = public_key_name  # type: str
        # The ID of the user to which the public key belongs.
        self.user_id = user_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListUserPublicKeysResponseBodyPublicKeys, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.comment is not None:
            result['Comment'] = self.comment
        if self.finger_print is not None:
            result['FingerPrint'] = self.finger_print
        if self.public_key_id is not None:
            result['PublicKeyId'] = self.public_key_id
        if self.public_key_name is not None:
            result['PublicKeyName'] = self.public_key_name
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')
        if m.get('FingerPrint') is not None:
            self.finger_print = m.get('FingerPrint')
        if m.get('PublicKeyId') is not None:
            self.public_key_id = m.get('PublicKeyId')
        if m.get('PublicKeyName') is not None:
            self.public_key_name = m.get('PublicKeyName')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class ListUserPublicKeysResponseBody(TeaModel):
    def __init__(self, public_keys=None, request_id=None, total_count=None):
        # An array that consists of the public keys of the user.
        self.public_keys = public_keys  # type: list[ListUserPublicKeysResponseBodyPublicKeys]
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id  # type: str
        # The total number of public keys.
        self.total_count = total_count  # type: long

    def validate(self):
        if self.public_keys:
            for k in self.public_keys:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListUserPublicKeysResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        result['PublicKeys'] = []
        if self.public_keys is not None:
            for k in self.public_keys:
                result['PublicKeys'].append(k.to_map() if k else None)
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        return result

    def from_map(self, m=None):
        m = m or dict()
        self.public_keys = []
        if m.get('PublicKeys') is not None:
            for k in m.get('PublicKeys'):
                temp_model = ListUserPublicKeysResponseBodyPublicKeys()
                self.public_keys.append(temp_model.from_map(k))
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        return self


class ListUserPublicKeysResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListUserPublicKeysResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListUserPublicKeysResponse, self).to_map()
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
            temp_model = ListUserPublicKeysResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListUsersRequest(TeaModel):
    def __init__(self, display_name=None, instance_id=None, mobile=None, page_number=None, page_size=None,
                 region_id=None, source=None, source_user_id=None, user_group_id=None, user_name=None, user_state=None):
        # The display name of the user to be queried. Only exact match is supported.
        self.display_name = display_name  # type: str
        # The ID of the Bastionhost instance to which the users to be queried belong.
        # 
        # >  You can call the [DescribeInstances](~~153281~~) operation to query the ID of the Bastionhost instance.
        self.instance_id = instance_id  # type: str
        # The mobile number of the user to be queried. Only exact match is supported.
        self.mobile = mobile  # type: str
        # The number of the page to return. Default value: **1**.
        self.page_number = page_number  # type: str
        # The number of entries to return on each page.
        # 
        # The value of the PageSize parameter must not exceed 100. By default, the number of entries on each page is 20. If you do not set the PageSize parameter, 20 entries are returned per page by default.
        # 
        # >  We recommend that you do not leave this parameter empty.
        self.page_size = page_size  # type: str
        # The region ID of the Bastionhost instance to which the users to be queried belong.
        # 
        # >  For more information about the mapping between region IDs and region names, see [Regions and zones](~~40654~~).
        self.region_id = region_id  # type: str
        # The source of the user to be queried. Valid values:
        # 
        # *   **Local**: a local user
        # *   **Ram**: a RAM user
        self.source = source  # type: str
        # The unique ID of the user to be queried. Only exact match is supported.
        # 
        # >  This parameter uniquely identifies a RAM user of the Bastionhost instance. This parameter takes effect only when the **Source** parameter is set to **Ram**. You can call the [ListUsers](~~28684~~) operation to obtain the unique ID of the user from the **UserId** response parameter.
        self.source_user_id = source_user_id  # type: str
        # The ID of the user group to be queried.
        # 
        # >  You can call the [ListUserGroups](~~204509~~) operation to query the ID of the user group.
        self.user_group_id = user_group_id  # type: str
        # The logon name of the user to be queried. Only exact match is supported.
        self.user_name = user_name  # type: str
        # The status of the user to be queried. Valid values:
        # 
        # *   **Normal**: The user can access the Bastionhost instance.
        # *   **Frozen**: The user is locked and cannot access the Bastionhost instance.
        # *   **Expired**: The user has expired and cannot access the Bastionhost instance.
        self.user_state = user_state  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListUsersRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.mobile is not None:
            result['Mobile'] = self.mobile
        if self.page_number is not None:
            result['PageNumber'] = self.page_number
        if self.page_size is not None:
            result['PageSize'] = self.page_size
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.source is not None:
            result['Source'] = self.source
        if self.source_user_id is not None:
            result['SourceUserId'] = self.source_user_id
        if self.user_group_id is not None:
            result['UserGroupId'] = self.user_group_id
        if self.user_name is not None:
            result['UserName'] = self.user_name
        if self.user_state is not None:
            result['UserState'] = self.user_state
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Mobile') is not None:
            self.mobile = m.get('Mobile')
        if m.get('PageNumber') is not None:
            self.page_number = m.get('PageNumber')
        if m.get('PageSize') is not None:
            self.page_size = m.get('PageSize')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('SourceUserId') is not None:
            self.source_user_id = m.get('SourceUserId')
        if m.get('UserGroupId') is not None:
            self.user_group_id = m.get('UserGroupId')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        if m.get('UserState') is not None:
            self.user_state = m.get('UserState')
        return self


class ListUsersResponseBodyUsers(TeaModel):
    def __init__(self, comment=None, display_name=None, effective_end_time=None, effective_start_time=None,
                 email=None, mobile=None, mobile_country_code=None, need_reset_password=None, source=None,
                 source_user_id=None, two_factor_methods=None, two_factor_status=None, user_id=None, user_name=None,
                 user_state=None):
        # The description of the user.
        self.comment = comment  # type: str
        # The display name of the user.
        self.display_name = display_name  # type: str
        # The end of the validity period of the user. The value is a UNIX timestamp. Unit: seconds.
        self.effective_end_time = effective_end_time  # type: long
        # The beginning of the validity period of the user. The value is a UNIX timestamp. Unit: seconds.
        self.effective_start_time = effective_start_time  # type: long
        # The email address of the user.
        self.email = email  # type: str
        # The mobile number of the user.
        self.mobile = mobile  # type: str
        # The country where the mobile number of the user is registered. Valid values:
        # 
        # *   **CN**: the Chinese mainland, whose country calling code is +86
        # *   **HK**: Hong Kong (China), whose country calling code is +852
        # *   **MO**: Macau (China), whose country calling code is +853
        # *   **TW**: Taiwan (China), whose country calling code is +886
        # *   **RU**: Russia, whose country calling code is +7
        # *   **SG**: Singapore, whose country calling code is +65
        # *   **MY**: Malaysia, whose country calling code is +60
        # *   **ID**: Indonesia, whose country calling code is +62
        # *   **DE**: Germany, whose country calling code is +49
        # *   **AU**: Australia, whose country calling code is +61
        # *   **US**: United States, whose country calling code is +1
        # *   **AE**: United Arab Emirates, whose country calling code is +971
        # *   **JP**: Japan, whose country calling code is +81
        # *   **GB**: United Kingdom, whose country calling code is +44
        # *   **IN**: India, whose country calling code is +91
        # *   **KR**: South Korea, whose country calling code is +82
        # *   **PH**: Philippines, whose country calling code is +63
        # *   **CH**: Switzerland, whose country calling code is +41
        # *   **SE**: Sweden, whose country calling code is +46
        self.mobile_country_code = mobile_country_code  # type: str
        # Specifies whether password reset is required upon the next logon. Valid values:
        # 
        # - true: yes
        # - false: no
        self.need_reset_password = need_reset_password  # type: bool
        # The source of the user. Valid values:
        # 
        # *   **Local**: a local user
        # *   **Ram**: a RAM user
        self.source = source  # type: str
        # The unique ID of the user.
        # 
        # >  This parameter uniquely identifies a RAM user of the Bastionhost instance. A value is returned for this parameter if the **Source** parameter is set to **Ram**. No value is returned for this parameter if the **Source** parameter is set to **Local**.
        self.source_user_id = source_user_id  # type: str
        # The two-factor authentication method.
        self.two_factor_methods = two_factor_methods  # type: list[str]
        # The two-factor authentication status of the user. Valid values:
        # 
        # *   **Global:** follows the global settings
        # *   **Disable:** disables two-factor authentication
        # *   **Enable:** enable two-factor authentication and follows settings of the single user
        self.two_factor_status = two_factor_status  # type: str
        # The ID of the user.
        self.user_id = user_id  # type: str
        # The logon name of the user.
        self.user_name = user_name  # type: str
        # The statuses of the user.
        self.user_state = user_state  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(ListUsersResponseBodyUsers, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.comment is not None:
            result['Comment'] = self.comment
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.effective_end_time is not None:
            result['EffectiveEndTime'] = self.effective_end_time
        if self.effective_start_time is not None:
            result['EffectiveStartTime'] = self.effective_start_time
        if self.email is not None:
            result['Email'] = self.email
        if self.mobile is not None:
            result['Mobile'] = self.mobile
        if self.mobile_country_code is not None:
            result['MobileCountryCode'] = self.mobile_country_code
        if self.need_reset_password is not None:
            result['NeedResetPassword'] = self.need_reset_password
        if self.source is not None:
            result['Source'] = self.source
        if self.source_user_id is not None:
            result['SourceUserId'] = self.source_user_id
        if self.two_factor_methods is not None:
            result['TwoFactorMethods'] = self.two_factor_methods
        if self.two_factor_status is not None:
            result['TwoFactorStatus'] = self.two_factor_status
        if self.user_id is not None:
            result['UserId'] = self.user_id
        if self.user_name is not None:
            result['UserName'] = self.user_name
        if self.user_state is not None:
            result['UserState'] = self.user_state
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('EffectiveEndTime') is not None:
            self.effective_end_time = m.get('EffectiveEndTime')
        if m.get('EffectiveStartTime') is not None:
            self.effective_start_time = m.get('EffectiveStartTime')
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('Mobile') is not None:
            self.mobile = m.get('Mobile')
        if m.get('MobileCountryCode') is not None:
            self.mobile_country_code = m.get('MobileCountryCode')
        if m.get('NeedResetPassword') is not None:
            self.need_reset_password = m.get('NeedResetPassword')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('SourceUserId') is not None:
            self.source_user_id = m.get('SourceUserId')
        if m.get('TwoFactorMethods') is not None:
            self.two_factor_methods = m.get('TwoFactorMethods')
        if m.get('TwoFactorStatus') is not None:
            self.two_factor_status = m.get('TwoFactorStatus')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        if m.get('UserState') is not None:
            self.user_state = m.get('UserState')
        return self


class ListUsersResponseBody(TeaModel):
    def __init__(self, request_id=None, total_count=None, users=None):
        # The ID of the request.
        self.request_id = request_id  # type: str
        # The total number of users that were queried.
        self.total_count = total_count  # type: int
        # The list of users that were queried.
        self.users = users  # type: list[ListUsersResponseBodyUsers]

    def validate(self):
        if self.users:
            for k in self.users:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ListUsersResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        if self.total_count is not None:
            result['TotalCount'] = self.total_count
        result['Users'] = []
        if self.users is not None:
            for k in self.users:
                result['Users'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        if m.get('TotalCount') is not None:
            self.total_count = m.get('TotalCount')
        self.users = []
        if m.get('Users') is not None:
            for k in m.get('Users'):
                temp_model = ListUsersResponseBodyUsers()
                self.users.append(temp_model.from_map(k))
        return self


class ListUsersResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ListUsersResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ListUsersResponse, self).to_map()
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
            temp_model = ListUsersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class LockUsersRequest(TeaModel):
    def __init__(self, instance_id=None, region_id=None, user_ids=None):
        # The ID of the bastion host to which the users to be locked belong.
        # 
        # > You can call the [DescribeInstances](~~153281~~) operation to query the ID of the bastion host.
        self.instance_id = instance_id  # type: str
        # The region ID of the bastion host to which the users to be locked belong.
        # 
        # > For more information about the mapping between region IDs and region names, see [Regions and zones](~~40654~~).
        self.region_id = region_id  # type: str
        # The ID of the user to be locked. The value is a JSON string. You can add up to 100 user IDs. If you specify multiple IDs, separate the IDs with commas (,).
        # 
        # > You can call the [ListUsers](~~204522~~) operation to query the ID of the user.
        self.user_ids = user_ids  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(LockUsersRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.user_ids is not None:
            result['UserIds'] = self.user_ids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('UserIds') is not None:
            self.user_ids = m.get('UserIds')
        return self


class LockUsersResponseBodyResults(TeaModel):
    def __init__(self, code=None, message=None, user_id=None):
        # The return code that indicates whether the call was successful. Valid values:
        # 
        # *   **OK**: The call was successful.
        # 
        # *   **UNEXPECTED**: An unknown error occurred.
        # 
        # *   **INVALID_ARGUMENT**: A request parameter is invalid.
        # 
        #     **\
        # 
        #     **Note**Make sure that the request parameters are valid and call the operation again.
        # 
        # *   **OBJECT_NOT_FOUND**: The specified object on which you want to perform the operation does not exist.
        # 
        #     **\
        # 
        #     **Note**Check whether the specified ID of the bastion host exists, whether the specified hosts exist, and whether the specified host IDs are valid. Then, call the operation again.
        # 
        # *   **OBJECT_AlREADY_EXISTS**: The specified object on which you want to perform the operation already exists.
        self.code = code  # type: str
        # This parameter is deprecated.
        self.message = message  # type: str
        # The ID of the user.
        self.user_id = user_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(LockUsersResponseBodyResults, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class LockUsersResponseBody(TeaModel):
    def __init__(self, request_id=None, results=None):
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id  # type: str
        # The result of the call.
        self.results = results  # type: list[LockUsersResponseBodyResults]

    def validate(self):
        if self.results:
            for k in self.results:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(LockUsersResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Results'] = []
        if self.results is not None:
            for k in self.results:
                result['Results'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.results = []
        if m.get('Results') is not None:
            for k in m.get('Results'):
                temp_model = LockUsersResponseBodyResults()
                self.results.append(temp_model.from_map(k))
        return self


class LockUsersResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: LockUsersResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(LockUsersResponse, self).to_map()
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
            temp_model = LockUsersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyHostRequest(TeaModel):
    def __init__(self, comment=None, host_id=None, host_name=None, host_private_address=None,
                 host_public_address=None, instance_id=None, network_domain_id=None, ostype=None, region_id=None):
        # The new internal endpoint of the host. You can set this parameter to a domain name or an IP address.
        self.comment = comment  # type: str
        # The ID of the Bastionhost instance where you want to modify the information of the host.
        # 
        # >  You can call the [DescribeInstances](~~153281~~) operation to query the ID of the Bastionhost instance.
        self.host_id = host_id  # type: str
        # The new name of the host. The name can be up to 128 characters.
        self.host_name = host_name  # type: str
        # The new description of the host. The value can be up to 500 characters in length.
        self.host_private_address = host_private_address  # type: str
        # The region ID of the Bastionhost instance where you want to modify the information of the host.
        # 
        # >  For more information about the mapping between region IDs and region names, see [Regions and zones](~~40654~~).
        self.host_public_address = host_public_address  # type: str
        # You can call this operation to modify the basic information of an on-premises host, an Elastic Compute Service (ECS) instance, or a host in a dedicated cluster.
        # 
        # >  The basic information of ECS instances and hosts in dedicated clusters within your Alibaba Cloud account is synchronized to Bastionhost on a regular basis. After you modify the basic information of an ECS instance or a host in a dedicated cluster, the modification result may be overwritten by the synchronized information.
        self.instance_id = instance_id  # type: str
        self.network_domain_id = network_domain_id  # type: str
        # The ID of the host.
        # 
        # >  You can call the [ListHosts](~~200665~~) operation to query the ID of the host.
        self.ostype = ostype  # type: str
        # The new operating system of the host. Valid values:
        # 
        # *   **Linux**\
        # *   **Windows**\
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyHostRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.comment is not None:
            result['Comment'] = self.comment
        if self.host_id is not None:
            result['HostId'] = self.host_id
        if self.host_name is not None:
            result['HostName'] = self.host_name
        if self.host_private_address is not None:
            result['HostPrivateAddress'] = self.host_private_address
        if self.host_public_address is not None:
            result['HostPublicAddress'] = self.host_public_address
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.network_domain_id is not None:
            result['NetworkDomainId'] = self.network_domain_id
        if self.ostype is not None:
            result['OSType'] = self.ostype
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')
        if m.get('HostId') is not None:
            self.host_id = m.get('HostId')
        if m.get('HostName') is not None:
            self.host_name = m.get('HostName')
        if m.get('HostPrivateAddress') is not None:
            self.host_private_address = m.get('HostPrivateAddress')
        if m.get('HostPublicAddress') is not None:
            self.host_public_address = m.get('HostPublicAddress')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('NetworkDomainId') is not None:
            self.network_domain_id = m.get('NetworkDomainId')
        if m.get('OSType') is not None:
            self.ostype = m.get('OSType')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ModifyHostResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyHostResponseBody, self).to_map()
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


class ModifyHostResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ModifyHostResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyHostResponse, self).to_map()
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
            temp_model = ModifyHostResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyHostAccountRequest(TeaModel):
    def __init__(self, host_account_id=None, host_account_name=None, host_share_key_id=None, instance_id=None,
                 pass_phrase=None, password=None, private_key=None, region_id=None):
        # The ID of the host account whose information you want to modify.
        # 
        # > You can call the [ListHostAccounts](~~204372~~) operation to query the ID of the host account.
        self.host_account_id = host_account_id  # type: str
        # The new name of the host account. The name can be up to 128 characters in length.
        self.host_account_name = host_account_name  # type: str
        # The ID of the shared key.
        self.host_share_key_id = host_share_key_id  # type: str
        # The ID of the bastion host in which you want to modify the information about the host account.
        # 
        # > You can call the [DescribeInstances](~~153281~~) operation to query the ID of the bastion host.
        self.instance_id = instance_id  # type: str
        # The passphrase of the new private key for the host account.
        # 
        # > This parameter takes effect only when the protocol of the host is set to SSH. If the protocol of the host is set to RDP, this parameter is not required.
        self.pass_phrase = pass_phrase  # type: str
        # The new password of the host account.
        self.password = password  # type: str
        # The new private key of the host account. The value is a Base64-encoded string.
        # 
        # > This parameter takes effect only when the protocol of the host is set to SSH. If the protocol of the host is set to RDP, this parameter is not required. You can call the [GetHostAccount](~~204391~~) operation to query the protocol used by the host. You can configure a password and a private key for the host account at the same time. If both a password and a private key are configured for the host account, Bastionhost preferentially uses the private key for logon.
        self.private_key = private_key  # type: str
        # The region ID of the bastion host in which you want to query the details of the host account.
        # 
        # > For more information about the mapping between region IDs and region names, see [Regions and zones](~~40654~~).
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyHostAccountRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.host_account_id is not None:
            result['HostAccountId'] = self.host_account_id
        if self.host_account_name is not None:
            result['HostAccountName'] = self.host_account_name
        if self.host_share_key_id is not None:
            result['HostShareKeyId'] = self.host_share_key_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.pass_phrase is not None:
            result['PassPhrase'] = self.pass_phrase
        if self.password is not None:
            result['Password'] = self.password
        if self.private_key is not None:
            result['PrivateKey'] = self.private_key
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('HostAccountId') is not None:
            self.host_account_id = m.get('HostAccountId')
        if m.get('HostAccountName') is not None:
            self.host_account_name = m.get('HostAccountName')
        if m.get('HostShareKeyId') is not None:
            self.host_share_key_id = m.get('HostShareKeyId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('PassPhrase') is not None:
            self.pass_phrase = m.get('PassPhrase')
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('PrivateKey') is not None:
            self.private_key = m.get('PrivateKey')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ModifyHostAccountResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyHostAccountResponseBody, self).to_map()
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


class ModifyHostAccountResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ModifyHostAccountResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyHostAccountResponse, self).to_map()
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
            temp_model = ModifyHostAccountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyHostGroupRequest(TeaModel):
    def __init__(self, comment=None, host_group_id=None, host_group_name=None, instance_id=None, region_id=None):
        # The new name of the host group. The name can be up to 128 characters in length.
        self.comment = comment  # type: str
        # The region ID of the Bastionhost instance where you want to modify the information of the host group.
        # 
        # >  For more information about the mapping between region IDs and region names, see [Regions and zones](~~40654~~).
        self.host_group_id = host_group_id  # type: str
        # The ID of the host group that you want to modify.
        # 
        # >  You can call the [ListHostGroups](~~201307~~) operation to query the ID of the host group.
        self.host_group_name = host_group_name  # type: str
        # The ID of the request.
        self.instance_id = instance_id  # type: str
        # The ID of the Bastionhost instance where you want to modify the information of the host group.
        # 
        # >  You can call the [DescribeInstances](~~153281~~) operation to query the ID of the Bastionhost instance.
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyHostGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.comment is not None:
            result['Comment'] = self.comment
        if self.host_group_id is not None:
            result['HostGroupId'] = self.host_group_id
        if self.host_group_name is not None:
            result['HostGroupName'] = self.host_group_name
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')
        if m.get('HostGroupId') is not None:
            self.host_group_id = m.get('HostGroupId')
        if m.get('HostGroupName') is not None:
            self.host_group_name = m.get('HostGroupName')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ModifyHostGroupResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyHostGroupResponseBody, self).to_map()
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


class ModifyHostGroupResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ModifyHostGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyHostGroupResponse, self).to_map()
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
            temp_model = ModifyHostGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyHostShareKeyRequest(TeaModel):
    def __init__(self, host_share_key_id=None, host_share_key_name=None, instance_id=None, pass_phrase=None,
                 private_key=None, region_id=None):
        # The ID of the shared key whose information you want to modify.
        self.host_share_key_id = host_share_key_id  # type: str
        # The name of the shared key.
        self.host_share_key_name = host_share_key_name  # type: str
        # The ID of the bastion host. You can call the [DescribeInstances](~~153281~~) operation to query the ID of the bastion host.
        self.instance_id = instance_id  # type: str
        # The passphrase of the private key. The value is a Base64-encoded string.
        self.pass_phrase = pass_phrase  # type: str
        # The private key. The value is a Base64-encoded string.
        self.private_key = private_key  # type: str
        # The region ID of the bastion host. For more information about the mapping between region IDs and region names, see [Regions and zones](~~40654~~).
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyHostShareKeyRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.host_share_key_id is not None:
            result['HostShareKeyId'] = self.host_share_key_id
        if self.host_share_key_name is not None:
            result['HostShareKeyName'] = self.host_share_key_name
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.pass_phrase is not None:
            result['PassPhrase'] = self.pass_phrase
        if self.private_key is not None:
            result['PrivateKey'] = self.private_key
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('HostShareKeyId') is not None:
            self.host_share_key_id = m.get('HostShareKeyId')
        if m.get('HostShareKeyName') is not None:
            self.host_share_key_name = m.get('HostShareKeyName')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('PassPhrase') is not None:
            self.pass_phrase = m.get('PassPhrase')
        if m.get('PrivateKey') is not None:
            self.private_key = m.get('PrivateKey')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ModifyHostShareKeyResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyHostShareKeyResponseBody, self).to_map()
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


class ModifyHostShareKeyResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ModifyHostShareKeyResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyHostShareKeyResponse, self).to_map()
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
            temp_model = ModifyHostShareKeyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyHostsActiveAddressTypeRequest(TeaModel):
    def __init__(self, active_address_type=None, host_ids=None, instance_id=None, region_id=None):
        # The new portal type of the host. Valid values:
        # 
        # *   **Public**: public portal
        # *   **Private**: internal portal
        self.active_address_type = active_address_type  # type: str
        # The ID of the host for which you want to change the portal type. The value is a JSON string. You can add up to 100 host IDs.
        # 
        # >  You can call the [ListHosts](~~200665~~) operation to query the ID of the host.
        self.host_ids = host_ids  # type: str
        # The ID of the bastion host for which you want to change the portal type of the host.
        # 
        # >  You can call the [DescribeInstances](~~153281~~) operation to query the ID of the bastion host.
        self.instance_id = instance_id  # type: str
        # The region ID of the bastion host for which you want to change the portal type of the host.
        # 
        # >  For more information about the mapping between region IDs and region names, see [Regions and zones](~~40654~~).
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyHostsActiveAddressTypeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.active_address_type is not None:
            result['ActiveAddressType'] = self.active_address_type
        if self.host_ids is not None:
            result['HostIds'] = self.host_ids
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('ActiveAddressType') is not None:
            self.active_address_type = m.get('ActiveAddressType')
        if m.get('HostIds') is not None:
            self.host_ids = m.get('HostIds')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ModifyHostsActiveAddressTypeResponseBodyResults(TeaModel):
    def __init__(self, code=None, host_id=None, message=None):
        # The return code that indicates whether the call was successful. Valid values:
        # 
        # *   **OK**: The call was successful.
        # *   **UNEXPECTED**: An unknown error occurred.
        # *   **INVALID_ARGUMENT**: A request parameter is invalid.
        # *   **OBJECT_NOT_FOUND**: The specified object on which you want to perform the operation does not exist.
        # *   **OBJECT_AlREADY_EXISTS**: The specified object on which you want to perform the operation already exists.
        self.code = code  # type: str
        # The ID of the host.
        self.host_id = host_id  # type: str
        # This parameter is deprecated.
        self.message = message  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyHostsActiveAddressTypeResponseBodyResults, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.host_id is not None:
            result['HostId'] = self.host_id
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('HostId') is not None:
            self.host_id = m.get('HostId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class ModifyHostsActiveAddressTypeResponseBody(TeaModel):
    def __init__(self, request_id=None, results=None):
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id  # type: str
        # The result of the call.
        self.results = results  # type: list[ModifyHostsActiveAddressTypeResponseBodyResults]

    def validate(self):
        if self.results:
            for k in self.results:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ModifyHostsActiveAddressTypeResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Results'] = []
        if self.results is not None:
            for k in self.results:
                result['Results'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.results = []
        if m.get('Results') is not None:
            for k in m.get('Results'):
                temp_model = ModifyHostsActiveAddressTypeResponseBodyResults()
                self.results.append(temp_model.from_map(k))
        return self


class ModifyHostsActiveAddressTypeResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ModifyHostsActiveAddressTypeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyHostsActiveAddressTypeResponse, self).to_map()
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
            temp_model = ModifyHostsActiveAddressTypeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyHostsPortRequest(TeaModel):
    def __init__(self, host_ids=None, instance_id=None, port=None, protocol_name=None, region_id=None):
        # The ID of the host for which you want to change the port. The value is a JSON string. You can add up to 100 host IDs. If you specify multiple IDs, separate the IDs with commas (,).
        # 
        # >  You can call the [ListHosts](~~200665~~) operation to query the IDs of hosts.
        self.host_ids = host_ids  # type: str
        # The ID of the bastion host for which you want to change the port of the host.
        # 
        # >  You can call the [DescribeInstances](~~153281~~) operation to query the ID of the bastion host.
        self.instance_id = instance_id  # type: str
        # The new port of the host. The port number must be an integer. Valid values: 22 to 65535.
        self.port = port  # type: str
        # The protocol that is used to connect to the host. Valid values:
        # 
        # *   **SSH**\
        # *   **RDP**\
        self.protocol_name = protocol_name  # type: str
        # The region ID of the bastion host for which you want to change the port of the host.
        # 
        # >  For more information about the mapping between region IDs and region names, see [Regions and zones](~~40654~~).
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyHostsPortRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.host_ids is not None:
            result['HostIds'] = self.host_ids
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.port is not None:
            result['Port'] = self.port
        if self.protocol_name is not None:
            result['ProtocolName'] = self.protocol_name
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('HostIds') is not None:
            self.host_ids = m.get('HostIds')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('ProtocolName') is not None:
            self.protocol_name = m.get('ProtocolName')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ModifyHostsPortResponseBodyResults(TeaModel):
    def __init__(self, code=None, host_id=None, message=None):
        # The return code that indicates whether the call was successful. Valid values:
        # 
        # *   **OK**: The call was successful.
        # *   **UNEXPECTED**: An unknown error occurred.
        # *   **INVALID_ARGUMENT**: A request parameter is invalid.
        #     > Make sure that the request parameters are valid and call the operation again.
        # 
        # *   **OBJECT_NOT_FOUND**: The specified object on which you want to perform the operation does not exist.
        # 
        #     > Check whether the specified ID of the bastion host exists, whether the specified hosts exist, and whether the specified host IDs are valid. Then, call the operation again.
        # 
        # *   **OBJECT\_AlREADY\_EXISTS**: The specified object on which you want to perform the operation already exists.
        self.code = code  # type: str
        # The ID of the host.
        self.host_id = host_id  # type: str
        # This parameter is deprecated.
        self.message = message  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyHostsPortResponseBodyResults, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.host_id is not None:
            result['HostId'] = self.host_id
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('HostId') is not None:
            self.host_id = m.get('HostId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class ModifyHostsPortResponseBody(TeaModel):
    def __init__(self, request_id=None, results=None):
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id  # type: str
        # The result of the call.
        self.results = results  # type: list[ModifyHostsPortResponseBodyResults]

    def validate(self):
        if self.results:
            for k in self.results:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(ModifyHostsPortResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Results'] = []
        if self.results is not None:
            for k in self.results:
                result['Results'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.results = []
        if m.get('Results') is not None:
            for k in m.get('Results'):
                temp_model = ModifyHostsPortResponseBodyResults()
                self.results.append(temp_model.from_map(k))
        return self


class ModifyHostsPortResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ModifyHostsPortResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyHostsPortResponse, self).to_map()
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
            temp_model = ModifyHostsPortResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyInstanceADAuthServerRequest(TeaModel):
    def __init__(self, account=None, base_dn=None, domain=None, email_mapping=None, filter=None, instance_id=None,
                 is_ssl=None, mobile_mapping=None, name_mapping=None, password=None, port=None, region_id=None, server=None,
                 standby_server=None):
        # The username of the account that is used for the AD server.
        self.account = account  # type: str
        # The Base distinguished name (DN).
        self.base_dn = base_dn  # type: str
        # The domain on the AD server.
        self.domain = domain  # type: str
        # The field that is used to indicate the email address of a user on the AD server.
        self.email_mapping = email_mapping  # type: str
        # The condition that is used to filter users.
        self.filter = filter  # type: str
        # The ID of the bastion host. You can call the [DescribeInstances](~~153281~~) operation to query the ID of the bastion host.
        self.instance_id = instance_id  # type: str
        # Specifies whether to support SSL. Valid values:
        # 
        # *   **true**: yes
        # *   **false**: no
        self.is_ssl = is_ssl  # type: str
        # The field that is used to indicate the mobile phone number of a user on the AD server.
        self.mobile_mapping = mobile_mapping  # type: str
        # The field that is used to indicate the name of a user on the AD server.
        self.name_mapping = name_mapping  # type: str
        # The password of the account that is used for the AD server.
        self.password = password  # type: str
        # The port that is used to access the AD server.
        self.port = port  # type: str
        # The region ID of the bastion host. For more information about the mapping between region IDs and region names, see [Regions and zones](~~40654~~).
        self.region_id = region_id  # type: str
        # The address of the AD server.
        self.server = server  # type: str
        # The address of the secondary AD server.
        self.standby_server = standby_server  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyInstanceADAuthServerRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account is not None:
            result['Account'] = self.account
        if self.base_dn is not None:
            result['BaseDN'] = self.base_dn
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.email_mapping is not None:
            result['EmailMapping'] = self.email_mapping
        if self.filter is not None:
            result['Filter'] = self.filter
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.is_ssl is not None:
            result['IsSSL'] = self.is_ssl
        if self.mobile_mapping is not None:
            result['MobileMapping'] = self.mobile_mapping
        if self.name_mapping is not None:
            result['NameMapping'] = self.name_mapping
        if self.password is not None:
            result['Password'] = self.password
        if self.port is not None:
            result['Port'] = self.port
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.server is not None:
            result['Server'] = self.server
        if self.standby_server is not None:
            result['StandbyServer'] = self.standby_server
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Account') is not None:
            self.account = m.get('Account')
        if m.get('BaseDN') is not None:
            self.base_dn = m.get('BaseDN')
        if m.get('Domain') is not None:
            self.domain = m.get('Domain')
        if m.get('EmailMapping') is not None:
            self.email_mapping = m.get('EmailMapping')
        if m.get('Filter') is not None:
            self.filter = m.get('Filter')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('IsSSL') is not None:
            self.is_ssl = m.get('IsSSL')
        if m.get('MobileMapping') is not None:
            self.mobile_mapping = m.get('MobileMapping')
        if m.get('NameMapping') is not None:
            self.name_mapping = m.get('NameMapping')
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Server') is not None:
            self.server = m.get('Server')
        if m.get('StandbyServer') is not None:
            self.standby_server = m.get('StandbyServer')
        return self


class ModifyInstanceADAuthServerResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyInstanceADAuthServerResponseBody, self).to_map()
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


class ModifyInstanceADAuthServerResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ModifyInstanceADAuthServerResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyInstanceADAuthServerResponse, self).to_map()
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
            temp_model = ModifyInstanceADAuthServerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyInstanceAttributeRequest(TeaModel):
    def __init__(self, description=None, instance_id=None, region_id=None):
        # The description of the bastion host.
        # 
        # > The description can contain only letters, digits, underscores (\_), and hyphens (-). The description can be up to 30 characters in length.
        self.description = description  # type: str
        # The ID of the bastion host.
        # 
        # > You can call the [DescribeInstances](~~153281~~) operation to query the ID of the bastion host.
        self.instance_id = instance_id  # type: str
        # The region ID of the bastion host.
        # 
        # > For more information about the mapping between region IDs and region names, see [Regions and zones](~~40654~~).
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyInstanceAttributeRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.description is not None:
            result['Description'] = self.description
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Description') is not None:
            self.description = m.get('Description')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ModifyInstanceAttributeResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyInstanceAttributeResponseBody, self).to_map()
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


class ModifyInstanceAttributeResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ModifyInstanceAttributeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyInstanceAttributeResponse, self).to_map()
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
            temp_model = ModifyInstanceAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyInstanceLDAPAuthServerRequest(TeaModel):
    def __init__(self, account=None, base_dn=None, email_mapping=None, filter=None, instance_id=None, is_ssl=None,
                 login_name_mapping=None, mobile_mapping=None, name_mapping=None, password=None, port=None, region_id=None, server=None,
                 standby_server=None):
        # The username of the account that is used for the LDAP server.
        self.account = account  # type: str
        # The Base distinguished name (DN).
        self.base_dn = base_dn  # type: str
        # The field that is used to indicate the email address of a user on the LDAP server.
        self.email_mapping = email_mapping  # type: str
        # The condition that is used to filter users.
        self.filter = filter  # type: str
        # The ID of the bastion host. You can call the [DescribeInstances](~~153281~~) operation to query the ID of the bastion host.
        self.instance_id = instance_id  # type: str
        # Specifies whether to support SSL. Valid values:
        # 
        # *   **true**\
        # *   **false**\
        self.is_ssl = is_ssl  # type: str
        # The field that is used to indicate the logon name of a user on the LDAP server.
        self.login_name_mapping = login_name_mapping  # type: str
        # The field that is used to indicate the mobile phone number of a user on the LDAP server.
        self.mobile_mapping = mobile_mapping  # type: str
        # The field that is used to indicate the name of a user on the LDAP server.
        self.name_mapping = name_mapping  # type: str
        # The password of the account that is used for the LDAP server. You must configure a password when you configure LDAP authentication. If you leave this parameter empty when you modify the settings of LDAP authentication, the current password is used.
        self.password = password  # type: str
        # The port that is used to access the LDAP server.
        self.port = port  # type: str
        # The region ID of the bastion host. For more information about the mapping between region IDs and region names, see [Regions and zones](~~40654~~).
        self.region_id = region_id  # type: str
        # The address of the LDAP server.
        self.server = server  # type: str
        # The address of the secondary LDAP server.
        self.standby_server = standby_server  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyInstanceLDAPAuthServerRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account is not None:
            result['Account'] = self.account
        if self.base_dn is not None:
            result['BaseDN'] = self.base_dn
        if self.email_mapping is not None:
            result['EmailMapping'] = self.email_mapping
        if self.filter is not None:
            result['Filter'] = self.filter
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.is_ssl is not None:
            result['IsSSL'] = self.is_ssl
        if self.login_name_mapping is not None:
            result['LoginNameMapping'] = self.login_name_mapping
        if self.mobile_mapping is not None:
            result['MobileMapping'] = self.mobile_mapping
        if self.name_mapping is not None:
            result['NameMapping'] = self.name_mapping
        if self.password is not None:
            result['Password'] = self.password
        if self.port is not None:
            result['Port'] = self.port
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.server is not None:
            result['Server'] = self.server
        if self.standby_server is not None:
            result['StandbyServer'] = self.standby_server
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Account') is not None:
            self.account = m.get('Account')
        if m.get('BaseDN') is not None:
            self.base_dn = m.get('BaseDN')
        if m.get('EmailMapping') is not None:
            self.email_mapping = m.get('EmailMapping')
        if m.get('Filter') is not None:
            self.filter = m.get('Filter')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('IsSSL') is not None:
            self.is_ssl = m.get('IsSSL')
        if m.get('LoginNameMapping') is not None:
            self.login_name_mapping = m.get('LoginNameMapping')
        if m.get('MobileMapping') is not None:
            self.mobile_mapping = m.get('MobileMapping')
        if m.get('NameMapping') is not None:
            self.name_mapping = m.get('NameMapping')
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('Port') is not None:
            self.port = m.get('Port')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Server') is not None:
            self.server = m.get('Server')
        if m.get('StandbyServer') is not None:
            self.standby_server = m.get('StandbyServer')
        return self


class ModifyInstanceLDAPAuthServerResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyInstanceLDAPAuthServerResponseBody, self).to_map()
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


class ModifyInstanceLDAPAuthServerResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ModifyInstanceLDAPAuthServerResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyInstanceLDAPAuthServerResponse, self).to_map()
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
            temp_model = ModifyInstanceLDAPAuthServerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyInstanceTwoFactorRequest(TeaModel):
    def __init__(self, enable_two_factor=None, instance_id=None, region_id=None, skip_two_factor_time=None,
                 two_factor_methods=None):
        # Specifies whether to enable two-factor authentication. Valid values:
        # 
        # *   **true**: enables two-factor authentication.
        # *   **false**: disables two-factor authentication.
        self.enable_two_factor = enable_two_factor  # type: str
        # The ID of the bastion host.
        # 
        # >  You can call the [DescribeInstances](~~153281~~) operation to query the ID of the bastion host.
        self.instance_id = instance_id  # type: str
        # The region ID of the bastion host.
        # 
        # >  For more information about the mapping between region IDs and region names, see [Regions and zones](~~40654~~).
        self.region_id = region_id  # type: str
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.skip_two_factor_time = skip_two_factor_time  # type: str
        # One or more methods that are used to send a verification code if two-factor authentication is enabled. If you set the EnableTwoFactor parameter to true, you must specify at least one method. Valid values:
        # 
        # *   **sms**: text message
        # *   **email**: email
        # *   **dingtalk**: Notice in DingTalk
        self.two_factor_methods = two_factor_methods  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyInstanceTwoFactorRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.enable_two_factor is not None:
            result['EnableTwoFactor'] = self.enable_two_factor
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.skip_two_factor_time is not None:
            result['SkipTwoFactorTime'] = self.skip_two_factor_time
        if self.two_factor_methods is not None:
            result['TwoFactorMethods'] = self.two_factor_methods
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('EnableTwoFactor') is not None:
            self.enable_two_factor = m.get('EnableTwoFactor')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SkipTwoFactorTime') is not None:
            self.skip_two_factor_time = m.get('SkipTwoFactorTime')
        if m.get('TwoFactorMethods') is not None:
            self.two_factor_methods = m.get('TwoFactorMethods')
        return self


class ModifyInstanceTwoFactorResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The duration within which two-factor authentication is not required after a local user passes two-factor authentication. Valid values: 0 to 168. Unit: hours. If you set this parameter to 0, the local user must pass two-factor authentication every time the local user logs on to the bastion host.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyInstanceTwoFactorResponseBody, self).to_map()
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


class ModifyInstanceTwoFactorResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ModifyInstanceTwoFactorResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyInstanceTwoFactorResponse, self).to_map()
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
            temp_model = ModifyInstanceTwoFactorResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyUserRequest(TeaModel):
    def __init__(self, comment=None, display_name=None, effective_end_time=None, effective_start_time=None,
                 email=None, instance_id=None, mobile=None, mobile_country_code=None, need_reset_password=None,
                 password=None, region_id=None, two_factor_methods=None, two_factor_status=None, user_id=None):
        # The new description of the user. The description can be up to 500 characters in length.
        self.comment = comment  # type: str
        # The new display name of the user. This display name can be up to 128 characters in length.
        self.display_name = display_name  # type: str
        # The end of the validity period of the user. The value is a UNIX timestamp. Unit: seconds.
        self.effective_end_time = effective_end_time  # type: long
        # The beginning of the validity period of the user. The value is a UNIX timestamp. Unit: seconds.
        self.effective_start_time = effective_start_time  # type: long
        # The new email address of the user.
        # 
        # > This parameter is required when the TwoFactorStatus parameter is set to Enable and the TwoFactorMethods parameter is set to email.
        self.email = email  # type: str
        # The ID of the bastion host where you want to modify user information.
        # 
        # > You can call the [DescribeInstances](~~153281~~) operation to query the ID of the bastion host.
        self.instance_id = instance_id  # type: str
        # The new mobile number of the user.
        # 
        # > This parameter is required when the TwoFactorStatus parameter is set to Enable and the TwoFactorMethods parameter is set to sms or dingtalk.
        self.mobile = mobile  # type: str
        # The country where the new mobile number of the user is registered. Valid values:
        # 
        # *   **CN:** the Chinese mainland, whose country calling code is +86
        # *   **HK:** Hong Kong (China), whose country calling code is +852
        # *   **MO:** Macao (China), whose country calling code is +853
        # *   **TW:** Taiwan (China), whose country calling code is +886
        # *   **RU:** Russia, whose country calling code is +7
        # *   **SG:** Singapore, whose country calling code is +65
        # *   **MY:** Malaysia, whose country calling code is +60
        # *   **ID:** Indonesia, whose country calling code is +62
        # *   **DE:** Germany, whose country calling code is +49
        # *   **AU:** Australia, whose country calling code is +61
        # *   **US:** US, whose country calling code is +1
        # *   **AE:** United Arab Emirates, whose country calling code is +971
        # *   **JP:** Japan, whose country calling code is +81
        # *   **GB:** UK, whose country calling code is +44
        # *   **IN:** India, whose country calling code is +91
        # *   **KR:** Republic of Korea, whose country calling code is +82
        # *   **PH:** Philippines, whose country calling code is +63
        # *   **CH:** Switzerland, whose country calling code is +41
        # *   **SE:** Sweden, whose country calling code is +46
        # *   **SA:** Saudi Arabia, whose country calling code is +966
        self.mobile_country_code = mobile_country_code  # type: str
        # Specifies whether password reset is required upon the next logon. Valid values:
        # 
        # - true: yes
        # - false: no
        self.need_reset_password = need_reset_password  # type: bool
        # The new password of the user. The password must be 8 to 128 characters in length and must contain lowercase letters, uppercase letters, digits, and special characters.
        self.password = password  # type: str
        # The region ID of the bastion host where you want to modify user information.
        # 
        # > For more information about the mapping between region IDs and region names, see [Regions and zones](~~40654~~).
        self.region_id = region_id  # type: str
        # The two-factor authentication method. You can select only one method. Valid values:
        # 
        # *   **sms:** text message
        # *   **email:** email
        # *   **dingtalk:** DingTalk
        # *   **totp OTP:** time-based one-time password (TOTP) app
        # 
        # > *   When the TwoFactorStatus parameter is set to Enable, you must specify one of the preceding values.
        self.two_factor_methods = two_factor_methods  # type: str
        # The two-factor authentication status of the user. Valid values:
        # 
        # *   **Global:** follows the global settings
        # *   **Disable:** disables two-factor authentication
        # *   **Enable:** enable two-factor authentication and follows settings of the single user
        self.two_factor_status = two_factor_status  # type: str
        # The ID of the user whose information you want to modify.
        self.user_id = user_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyUserRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.comment is not None:
            result['Comment'] = self.comment
        if self.display_name is not None:
            result['DisplayName'] = self.display_name
        if self.effective_end_time is not None:
            result['EffectiveEndTime'] = self.effective_end_time
        if self.effective_start_time is not None:
            result['EffectiveStartTime'] = self.effective_start_time
        if self.email is not None:
            result['Email'] = self.email
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.mobile is not None:
            result['Mobile'] = self.mobile
        if self.mobile_country_code is not None:
            result['MobileCountryCode'] = self.mobile_country_code
        if self.need_reset_password is not None:
            result['NeedResetPassword'] = self.need_reset_password
        if self.password is not None:
            result['Password'] = self.password
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.two_factor_methods is not None:
            result['TwoFactorMethods'] = self.two_factor_methods
        if self.two_factor_status is not None:
            result['TwoFactorStatus'] = self.two_factor_status
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('EffectiveEndTime') is not None:
            self.effective_end_time = m.get('EffectiveEndTime')
        if m.get('EffectiveStartTime') is not None:
            self.effective_start_time = m.get('EffectiveStartTime')
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Mobile') is not None:
            self.mobile = m.get('Mobile')
        if m.get('MobileCountryCode') is not None:
            self.mobile_country_code = m.get('MobileCountryCode')
        if m.get('NeedResetPassword') is not None:
            self.need_reset_password = m.get('NeedResetPassword')
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('TwoFactorMethods') is not None:
            self.two_factor_methods = m.get('TwoFactorMethods')
        if m.get('TwoFactorStatus') is not None:
            self.two_factor_status = m.get('TwoFactorStatus')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class ModifyUserResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyUserResponseBody, self).to_map()
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


class ModifyUserResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ModifyUserResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyUserResponse, self).to_map()
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
            temp_model = ModifyUserResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyUserGroupRequest(TeaModel):
    def __init__(self, comment=None, instance_id=None, region_id=None, user_group_id=None, user_group_name=None):
        # The new description of the user group. The description can be up to 500 characters in length.
        self.comment = comment  # type: str
        # The ID of the bastion host in which you want to modify the information about the user group.
        # 
        # > You can call the [DescribeInstances](~~153281~~) operation to query the ID of the bastion host.
        self.instance_id = instance_id  # type: str
        # The region ID of the bastion host in which you want to modify the information about the user group.
        # 
        # > For more information about the mapping between region IDs and region names, see [Regions and zones](~~40654~~).
        self.region_id = region_id  # type: str
        # The ID of the user group that you want to modify.
        # 
        # > You can call the [ListUserGroups](~~204509~~) operation to query the ID of the user group.
        self.user_group_id = user_group_id  # type: str
        # The new name of the user group. This name can be up to 128 characters in length.
        self.user_group_name = user_group_name  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyUserGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.comment is not None:
            result['Comment'] = self.comment
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.user_group_id is not None:
            result['UserGroupId'] = self.user_group_id
        if self.user_group_name is not None:
            result['UserGroupName'] = self.user_group_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('UserGroupId') is not None:
            self.user_group_id = m.get('UserGroupId')
        if m.get('UserGroupName') is not None:
            self.user_group_name = m.get('UserGroupName')
        return self


class ModifyUserGroupResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyUserGroupResponseBody, self).to_map()
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


class ModifyUserGroupResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ModifyUserGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyUserGroupResponse, self).to_map()
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
            temp_model = ModifyUserGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class MoveResourceGroupRequest(TeaModel):
    def __init__(self, region_id=None, resource_group_id=None, resource_id=None, resource_type=None):
        # The region ID of the bastion host.
        self.region_id = region_id  # type: str
        # The ID of the resource group to which the bastion host is moved.
        # 
        # > You can call the [DescribeInstances](~~153281~~) operation to query the resource group ID of the bastion host.
        self.resource_group_id = resource_group_id  # type: str
        # The ID of the bastion host for which you want to change the resource group.
        # 
        # > You can call the [DescribeInstances](~~153281~~) operation to query the ID of the bastion host.
        self.resource_id = resource_id  # type: str
        # The type of the resource. Set the value to **INSTANCE**, which indicates that the resource is a bastion host.
        self.resource_type = resource_type  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(MoveResourceGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_group_id is not None:
            result['ResourceGroupId'] = self.resource_group_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceGroupId') is not None:
            self.resource_group_id = m.get('ResourceGroupId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        return self


class MoveResourceGroupResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(MoveResourceGroupResponseBody, self).to_map()
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


class MoveResourceGroupResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: MoveResourceGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(MoveResourceGroupResponse, self).to_map()
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
            temp_model = MoveResourceGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RejectApproveCommandRequest(TeaModel):
    def __init__(self, command_id=None, instance_id=None, region_id=None):
        self.command_id = command_id  # type: str
        self.instance_id = instance_id  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RejectApproveCommandRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.command_id is not None:
            result['CommandId'] = self.command_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CommandId') is not None:
            self.command_id = m.get('CommandId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class RejectApproveCommandResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RejectApproveCommandResponseBody, self).to_map()
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


class RejectApproveCommandResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RejectApproveCommandResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RejectApproveCommandResponse, self).to_map()
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
            temp_model = RejectApproveCommandResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RejectOperationTicketRequest(TeaModel):
    def __init__(self, instance_id=None, operation_ticket_id=None, region_id=None):
        self.instance_id = instance_id  # type: str
        self.operation_ticket_id = operation_ticket_id  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RejectOperationTicketRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.operation_ticket_id is not None:
            result['OperationTicketId'] = self.operation_ticket_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('OperationTicketId') is not None:
            self.operation_ticket_id = m.get('OperationTicketId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class RejectOperationTicketResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RejectOperationTicketResponseBody, self).to_map()
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


class RejectOperationTicketResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RejectOperationTicketResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RejectOperationTicketResponse, self).to_map()
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
            temp_model = RejectOperationTicketResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RemoveHostsFromGroupRequest(TeaModel):
    def __init__(self, host_group_id=None, host_ids=None, instance_id=None, region_id=None):
        # The return code that indicates whether the call was successful. Valid values:
        # 
        # *   **OK**: The call was successful.
        # *   **UNEXPECTED**: An unknown error occurred.
        # *   **INVALID_ARGUMENT**: A request parameter is invalid.
        # *   **OBJECT_NOT_FOUND**: The specified object on which you want to perform the operation does not exist.
        # *   **OBJECT_AlREADY_EXISTS**: The specified object on which you want to perform the operation already exists.
        self.host_group_id = host_group_id  # type: str
        # The ID of the request.
        self.host_ids = host_ids  # type: str
        # The ID of the host that you want to remove from the host group. The value is a JSON string. You can add up to 100 host IDs.
        # 
        # >  You can call the [ListHosts](~~200665~~) operation to query the IDs of hosts.
        self.instance_id = instance_id  # type: str
        # The ID of the host group.
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RemoveHostsFromGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.host_group_id is not None:
            result['HostGroupId'] = self.host_group_id
        if self.host_ids is not None:
            result['HostIds'] = self.host_ids
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('HostGroupId') is not None:
            self.host_group_id = m.get('HostGroupId')
        if m.get('HostIds') is not None:
            self.host_ids = m.get('HostIds')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class RemoveHostsFromGroupResponseBodyResults(TeaModel):
    def __init__(self, code=None, host_group_id=None, host_id=None, message=None):
        # RemoveHostsFromGroup
        self.code = code  # type: str
        # RemoveHostsFromGroup
        self.host_group_id = host_group_id  # type: str
        self.host_id = host_id  # type: str
        # WB662865
        self.message = message  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RemoveHostsFromGroupResponseBodyResults, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.host_group_id is not None:
            result['HostGroupId'] = self.host_group_id
        if self.host_id is not None:
            result['HostId'] = self.host_id
        if self.message is not None:
            result['Message'] = self.message
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('HostGroupId') is not None:
            self.host_group_id = m.get('HostGroupId')
        if m.get('HostId') is not None:
            self.host_id = m.get('HostId')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        return self


class RemoveHostsFromGroupResponseBody(TeaModel):
    def __init__(self, request_id=None, results=None):
        # All Alibaba Cloud API operations must include common request parameters. For more information about common request parameters, see [Common parameters](~~315526~~).
        # 
        # For more information about sample requests, see the "Examples" section of this topic.
        self.request_id = request_id  # type: str
        # Removes one or more hosts from a host group.
        self.results = results  # type: list[RemoveHostsFromGroupResponseBodyResults]

    def validate(self):
        if self.results:
            for k in self.results:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(RemoveHostsFromGroupResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Results'] = []
        if self.results is not None:
            for k in self.results:
                result['Results'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.results = []
        if m.get('Results') is not None:
            for k in m.get('Results'):
                temp_model = RemoveHostsFromGroupResponseBodyResults()
                self.results.append(temp_model.from_map(k))
        return self


class RemoveHostsFromGroupResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RemoveHostsFromGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RemoveHostsFromGroupResponse, self).to_map()
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
            temp_model = RemoveHostsFromGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RemoveUsersFromGroupRequest(TeaModel):
    def __init__(self, instance_id=None, region_id=None, user_group_id=None, user_ids=None):
        # The ID of the user who you want to remove. The value is a JSON string. You can add up to 100 user IDs. If you specify multiple IDs, separate the IDs with commas (,).
        # 
        # >  You can call the [ListUsers](~~204522~~) operation to query the IDs of users.
        self.instance_id = instance_id  # type: str
        # The ID of the user.
        self.region_id = region_id  # type: str
        # The return code that indicates whether the call was successful. Valid values:
        # 
        # *   **OK**: The call was successful.
        # 
        # *   **UNEXPECTED**: An unknown error occurred.
        # 
        # *   **INVALID_ARGUMENT**: A request parameter is invalid.
        # 
        # > Make sure that the request parameters are valid and call the operation again.
        # 
        # *   **OBJECT_NOT_FOUND**: The specified object on which you want to perform the operation does not exist.
        # 
        # > Check whether the specified ID of the bastion host exists, whether the specified hosts exist, and whether the specified host IDs are valid. Then, call the operation again.
        # 
        # *   **OBJECT_AlREADY_EXISTS**: The specified object on which you want to perform the operation already exists.
        self.user_group_id = user_group_id  # type: str
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.user_ids = user_ids  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RemoveUsersFromGroupRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.user_group_id is not None:
            result['UserGroupId'] = self.user_group_id
        if self.user_ids is not None:
            result['UserIds'] = self.user_ids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('UserGroupId') is not None:
            self.user_group_id = m.get('UserGroupId')
        if m.get('UserIds') is not None:
            self.user_ids = m.get('UserIds')
        return self


class RemoveUsersFromGroupResponseBodyResults(TeaModel):
    def __init__(self, code=None, message=None, user_group_id=None, user_id=None):
        # RemoveUsersFromGroup
        self.code = code  # type: str
        # WB01014029
        self.message = message  # type: str
        # RemoveUsersFromGroup
        self.user_group_id = user_group_id  # type: str
        self.user_id = user_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(RemoveUsersFromGroupResponseBodyResults, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.user_group_id is not None:
            result['UserGroupId'] = self.user_group_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('UserGroupId') is not None:
            self.user_group_id = m.get('UserGroupId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class RemoveUsersFromGroupResponseBody(TeaModel):
    def __init__(self, request_id=None, results=None):
        # All Alibaba Cloud API operations must include common request parameters. For more information about common request parameters, see [Common parameters](~~315526~~).
        # 
        # For more information about sample requests, see the "Examples" section of this topic.
        self.request_id = request_id  # type: str
        # Removes one or more users from a user group.
        self.results = results  # type: list[RemoveUsersFromGroupResponseBodyResults]

    def validate(self):
        if self.results:
            for k in self.results:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(RemoveUsersFromGroupResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Results'] = []
        if self.results is not None:
            for k in self.results:
                result['Results'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.results = []
        if m.get('Results') is not None:
            for k in m.get('Results'):
                temp_model = RemoveUsersFromGroupResponseBodyResults()
                self.results.append(temp_model.from_map(k))
        return self


class RemoveUsersFromGroupResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: RemoveUsersFromGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(RemoveUsersFromGroupResponse, self).to_map()
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
            temp_model = RemoveUsersFromGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ResetHostAccountCredentialRequest(TeaModel):
    def __init__(self, credential_type=None, host_account_id=None, instance_id=None, region_id=None):
        # ResetHostAccountCredential
        self.credential_type = credential_type  # type: str
        # WB662865
        self.host_account_id = host_account_id  # type: str
        # Deletes the logon credential of a specified host account of a specified Bastionhost instance. The logon credential can be the password or SSH private key.
        self.instance_id = instance_id  # type: str
        # ResetHostAccountCredential
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ResetHostAccountCredentialRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.credential_type is not None:
            result['CredentialType'] = self.credential_type
        if self.host_account_id is not None:
            result['HostAccountId'] = self.host_account_id
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CredentialType') is not None:
            self.credential_type = m.get('CredentialType')
        if m.get('HostAccountId') is not None:
            self.host_account_id = m.get('HostAccountId')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ResetHostAccountCredentialResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ResetHostAccountCredentialResponseBody, self).to_map()
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


class ResetHostAccountCredentialResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: ResetHostAccountCredentialResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ResetHostAccountCredentialResponse, self).to_map()
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
            temp_model = ResetHostAccountCredentialResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StartInstanceRequest(TeaModel):
    def __init__(self, instance_id=None, region_id=None, security_group_ids=None, vswitch_id=None):
        # The ID of the bastion host that you want to enable.
        # 
        # > You can call the [DescribeInstances](~~153281~~) operation to query the ID of the bastion host.
        self.instance_id = instance_id  # type: str
        # The region ID of the bastion host.
        self.region_id = region_id  # type: str
        # An array consisting of the IDs of security groups to which the bastion host is added.
        self.security_group_ids = security_group_ids  # type: list[str]
        # The ID of the vSwitch to which the bastion host belongs.
        self.vswitch_id = vswitch_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(StartInstanceRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.security_group_ids is not None:
            result['SecurityGroupIds'] = self.security_group_ids
        if self.vswitch_id is not None:
            result['VswitchId'] = self.vswitch_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SecurityGroupIds') is not None:
            self.security_group_ids = m.get('SecurityGroupIds')
        if m.get('VswitchId') is not None:
            self.vswitch_id = m.get('VswitchId')
        return self


class StartInstanceResponseBody(TeaModel):
    def __init__(self, instance_id=None, request_id=None):
        # The ID of the bastion host that you enable.
        self.instance_id = instance_id  # type: str
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(StartInstanceResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class StartInstanceResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: StartInstanceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(StartInstanceResponse, self).to_map()
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
            temp_model = StartInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TagResourcesRequestTag(TeaModel):
    def __init__(self, key=None, value=None):
        # The key of tag N. Valid values of N: 1 to 20.
        # 
        # > 
        # 
        # *   The value can be up to 128 characters in length but cannot be an empty string.
        # 
        # *   The value cannot start with **aliyun** or **acs:**. The value cannot contain **http://** or **https://**.
        self.key = key  # type: str
        # The value of tag N.\
        # Valid values of N: 1 to 20.
        # 
        # > 
        # 
        # *   The value can be up to 128 characters in length or an empty string.
        # 
        # *   The value cannot start with **aliyun** or **acs:**. The value cannot contain **http://** or **https://**.
        self.value = value  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(TagResourcesRequestTag, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.key is not None:
            result['Key'] = self.key
        if self.value is not None:
            result['Value'] = self.value
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Key') is not None:
            self.key = m.get('Key')
        if m.get('Value') is not None:
            self.value = m.get('Value')
        return self


class TagResourcesRequest(TeaModel):
    def __init__(self, region_id=None, resource_id=None, resource_type=None, tag=None):
        # The region ID of the bastion hosts to which you want to create and add tags.
        # 
        # > For more information about the mapping between region IDs and region names, see [Regions and zones](~~40654~~).
        self.region_id = region_id  # type: str
        # An array that consists of IDs of bastion hosts.
        # 
        # Valid values: 1 to 20.
        # 
        # > You can call the [DescribeInstances](~~153281~~) operation to query IDs of bastion hosts.
        self.resource_id = resource_id  # type: list[str]
        # The type of the resource.
        # 
        # Set the value to **INSTANCE**, which indicates that the resource is a bastion host.
        self.resource_type = resource_type  # type: str
        # An array that consists of tags.
        self.tag = tag  # type: list[TagResourcesRequestTag]

    def validate(self):
        if self.tag:
            for k in self.tag:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(TagResourcesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        result['Tag'] = []
        if self.tag is not None:
            for k in self.tag:
                result['Tag'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        self.tag = []
        if m.get('Tag') is not None:
            for k in m.get('Tag'):
                temp_model = TagResourcesRequestTag()
                self.tag.append(temp_model.from_map(k))
        return self


class TagResourcesResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(TagResourcesResponseBody, self).to_map()
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


class TagResourcesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: TagResourcesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(TagResourcesResponse, self).to_map()
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
            temp_model = TagResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UnlockUsersRequest(TeaModel):
    def __init__(self, instance_id=None, region_id=None, user_ids=None):
        # The ID of the bastion host to which the users to be unlocked belong.
        # 
        # > You can call the [DescribeInstances](~~153281~~) operation to query the ID of the bastion host.
        self.instance_id = instance_id  # type: str
        # The region ID of the bastion host to which the users to be unlocked belong.
        # 
        # > For more information about the mapping between region IDs and region names, see [Regions and zones](~~40654~~).
        self.region_id = region_id  # type: str
        # The ID of the user that you want to unlock. The value is a JSON string. You can add up to 100 user IDs. If you specify multiple IDs, separate the IDs with commas (,).
        # 
        # > You can call the [ListUsers](~~204522~~) operation to query the ID of the user.
        self.user_ids = user_ids  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UnlockUsersRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.user_ids is not None:
            result['UserIds'] = self.user_ids
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('UserIds') is not None:
            self.user_ids = m.get('UserIds')
        return self


class UnlockUsersResponseBodyResults(TeaModel):
    def __init__(self, code=None, message=None, user_id=None):
        # The result of the call. Valid values:
        # 
        # *   **OK**: The call was successful.
        # 
        # *   **UNEXPECTED**: An unknown error occurred.
        # 
        # *   **INVALID_ARGUMENT**: A request parameter is invalid.
        # 
        #     **\
        # 
        #     **Note**Make sure that the request parameters are valid and call the operation again.
        # 
        # *   **OBJECT_NOT_FOUND**: The specified object on which you want to perform the operation does not exist.
        # 
        #     **\
        # 
        #     **Note**Check whether the specified ID of the bastion host exists, whether the specified hosts exist, and whether the specified host IDs are valid. Then, call the operation again.
        # 
        # *   **OBJECT_AlREADY_EXISTS**: The specified object on which you want to perform the operation already exists.
        self.code = code  # type: str
        # This parameter is deprecated.
        self.message = message  # type: str
        # The ID of the user.
        self.user_id = user_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UnlockUsersResponseBodyResults, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.code is not None:
            result['Code'] = self.code
        if self.message is not None:
            result['Message'] = self.message
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Code') is not None:
            self.code = m.get('Code')
        if m.get('Message') is not None:
            self.message = m.get('Message')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class UnlockUsersResponseBody(TeaModel):
    def __init__(self, request_id=None, results=None):
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id  # type: str
        # An array that consists of information about the result of the call.
        self.results = results  # type: list[UnlockUsersResponseBodyResults]

    def validate(self):
        if self.results:
            for k in self.results:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(UnlockUsersResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        result['Results'] = []
        if self.results is not None:
            for k in self.results:
                result['Results'].append(k.to_map() if k else None)
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        self.results = []
        if m.get('Results') is not None:
            for k in m.get('Results'):
                temp_model = UnlockUsersResponseBodyResults()
                self.results.append(temp_model.from_map(k))
        return self


class UnlockUsersResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UnlockUsersResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UnlockUsersResponse, self).to_map()
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
            temp_model = UnlockUsersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UntagResourcesRequest(TeaModel):
    def __init__(self, all=None, region_id=None, resource_id=None, resource_type=None, tag_key=None):
        # Specifies whether to delete all tags that are added to the bastion host.
        # 
        # *   If you specify TagKey.N, the value of this parameter can only be **false**, which indicates that only a specified tag is deleted.
        # *   If you do not specify TagKey.N and the value of this parameter is **true**, all tags are deleted. If you do not specify TagKey.N and the value of this parameter is **false**, no tags are deleted.
        self.all = all  # type: bool
        # The region ID of the bastion host to query.
        # 
        # > For more information about the mapping between region IDs and region names, see [Regions and zones](~~40654~~).
        self.region_id = region_id  # type: str
        # An array that consists of IDs of bastion hosts.
        # 
        # Valid values: 1 to 20.
        # 
        # > You can call the [DescribeInstances](~~153281~~) operation to query the ID of the bastion host.
        self.resource_id = resource_id  # type: list[str]
        # The type of the resource.
        # 
        # Set the value to **INSTANCE**, which indicates that the resource is a bastion host.
        self.resource_type = resource_type  # type: str
        # The key of tag N.
        # 
        # Valid values of N: 1 to 20.
        self.tag_key = tag_key  # type: list[str]

    def validate(self):
        pass

    def to_map(self):
        _map = super(UntagResourcesRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.all is not None:
            result['All'] = self.all
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.resource_id is not None:
            result['ResourceId'] = self.resource_id
        if self.resource_type is not None:
            result['ResourceType'] = self.resource_type
        if self.tag_key is not None:
            result['TagKey'] = self.tag_key
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('All') is not None:
            self.all = m.get('All')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('ResourceId') is not None:
            self.resource_id = m.get('ResourceId')
        if m.get('ResourceType') is not None:
            self.resource_type = m.get('ResourceType')
        if m.get('TagKey') is not None:
            self.tag_key = m.get('TagKey')
        return self


class UntagResourcesResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # The ID of the request, which is used to locate and troubleshoot issues.
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UntagResourcesResponseBody, self).to_map()
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


class UntagResourcesResponse(TeaModel):
    def __init__(self, headers=None, status_code=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.status_code = status_code  # type: int
        self.body = body  # type: UntagResourcesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.status_code, 'status_code')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UntagResourcesResponse, self).to_map()
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
            temp_model = UntagResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


