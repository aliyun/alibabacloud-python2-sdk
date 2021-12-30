# -*- coding: utf-8 -*-
# This file is auto-generated, don't edit it. Thanks.
from Tea.model import TeaModel


class AddHostsToGroupRequest(TeaModel):
    def __init__(self, host_group_id=None, host_ids=None, instance_id=None, region_id=None):
        self.host_group_id = host_group_id  # type: str
        self.host_ids = host_ids  # type: str
        self.instance_id = instance_id  # type: str
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
        self.code = code  # type: str
        self.host_group_id = host_group_id  # type: str
        self.host_id = host_id  # type: str
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
        self.request_id = request_id  # type: str
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: AddHostsToGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = AddHostsToGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AddUsersToGroupRequest(TeaModel):
    def __init__(self, instance_id=None, region_id=None, user_group_id=None, user_ids=None):
        self.instance_id = instance_id  # type: str
        self.region_id = region_id  # type: str
        self.user_group_id = user_group_id  # type: str
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
        self.code = code  # type: str
        self.message = message  # type: str
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
        self.request_id = request_id  # type: str
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: AddUsersToGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = AddUsersToGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AttachHostAccountsToHostShareKeyRequest(TeaModel):
    def __init__(self, host_account_ids=None, host_share_key_id=None, instance_id=None, region_id=None):
        self.host_account_ids = host_account_ids  # type: str
        self.host_share_key_id = host_share_key_id  # type: str
        self.instance_id = instance_id  # type: str
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
        self.code = code  # type: str
        self.host_account_id = host_account_id  # type: str
        self.host_share_key_id = host_share_key_id  # type: str
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
        # Id of the request
        self.request_id = request_id  # type: str
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: AttachHostAccountsToHostShareKeyResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = AttachHostAccountsToHostShareKeyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AttachHostAccountsToUserRequest(TeaModel):
    def __init__(self, hosts=None, instance_id=None, region_id=None, user_id=None):
        self.hosts = hosts  # type: str
        self.instance_id = instance_id  # type: str
        self.region_id = region_id  # type: str
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
        self.code = code  # type: str
        self.host_account_id = host_account_id  # type: str
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
        self.code = code  # type: str
        self.host_accounts = host_accounts  # type: list[AttachHostAccountsToUserResponseBodyResultsHostAccounts]
        self.host_id = host_id  # type: str
        self.message = message  # type: str
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
        self.request_id = request_id  # type: str
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: AttachHostAccountsToUserResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = AttachHostAccountsToUserResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AttachHostAccountsToUserGroupRequest(TeaModel):
    def __init__(self, hosts=None, instance_id=None, region_id=None, user_group_id=None):
        self.hosts = hosts  # type: str
        self.instance_id = instance_id  # type: str
        self.region_id = region_id  # type: str
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
        self.code = code  # type: str
        self.host_account_id = host_account_id  # type: str
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
        self.code = code  # type: str
        self.host_accounts = host_accounts  # type: list[AttachHostAccountsToUserGroupResponseBodyResultsHostAccounts]
        self.host_id = host_id  # type: str
        self.message = message  # type: str
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
        self.request_id = request_id  # type: str
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: AttachHostAccountsToUserGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = AttachHostAccountsToUserGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AttachHostGroupAccountsToUserRequest(TeaModel):
    def __init__(self, host_groups=None, instance_id=None, region_id=None, user_id=None):
        self.host_groups = host_groups  # type: str
        self.instance_id = instance_id  # type: str
        self.region_id = region_id  # type: str
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
        self.code = code  # type: str
        self.host_account_name = host_account_name  # type: str
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
        self.code = code  # type: str
        self.host_account_names = host_account_names  # type: list[AttachHostGroupAccountsToUserResponseBodyResultsHostAccountNames]
        self.host_group_id = host_group_id  # type: str
        self.message = message  # type: str
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
        self.request_id = request_id  # type: str
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: AttachHostGroupAccountsToUserResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = AttachHostGroupAccountsToUserResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class AttachHostGroupAccountsToUserGroupRequest(TeaModel):
    def __init__(self, host_groups=None, instance_id=None, region_id=None, user_group_id=None):
        self.host_groups = host_groups  # type: str
        self.instance_id = instance_id  # type: str
        self.region_id = region_id  # type: str
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
        self.code = code  # type: str
        self.host_account_name = host_account_name  # type: str
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
        self.code = code  # type: str
        self.host_account_names = host_account_names  # type: list[AttachHostGroupAccountsToUserGroupResponseBodyResultsHostAccountNames]
        self.host_group_id = host_group_id  # type: str
        self.message = message  # type: str
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
        self.request_id = request_id  # type: str
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: AttachHostGroupAccountsToUserGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = AttachHostGroupAccountsToUserGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ConfigInstanceSecurityGroupsRequest(TeaModel):
    def __init__(self, authorized_security_groups=None, instance_id=None, lang=None, region_id=None):
        self.authorized_security_groups = authorized_security_groups  # type: list[str]
        self.instance_id = instance_id  # type: str
        self.lang = lang  # type: str
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
        self.instance_id = instance_id  # type: str
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ConfigInstanceSecurityGroupsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ConfigInstanceSecurityGroupsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ConfigInstanceWhiteListRequest(TeaModel):
    def __init__(self, instance_id=None, region_id=None, white_list=None):
        self.instance_id = instance_id  # type: str
        self.region_id = region_id  # type: str
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ConfigInstanceWhiteListResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ConfigInstanceWhiteListResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateHostRequest(TeaModel):
    def __init__(self, active_address_type=None, comment=None, host_name=None, host_private_address=None,
                 host_public_address=None, instance_id=None, instance_region_id=None, ostype=None, region_id=None, source=None,
                 source_instance_id=None):
        self.active_address_type = active_address_type  # type: str
        self.comment = comment  # type: str
        self.host_name = host_name  # type: str
        self.host_private_address = host_private_address  # type: str
        self.host_public_address = host_public_address  # type: str
        self.instance_id = instance_id  # type: str
        self.instance_region_id = instance_region_id  # type: str
        self.ostype = ostype  # type: str
        self.region_id = region_id  # type: str
        self.source = source  # type: str
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
        self.host_id = host_id  # type: str
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateHostResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateHostResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateHostAccountRequest(TeaModel):
    def __init__(self, host_account_name=None, host_id=None, host_share_key_id=None, instance_id=None,
                 pass_phrase=None, password=None, private_key=None, protocol_name=None, region_id=None):
        self.host_account_name = host_account_name  # type: str
        self.host_id = host_id  # type: str
        self.host_share_key_id = host_share_key_id  # type: str
        self.instance_id = instance_id  # type: str
        self.pass_phrase = pass_phrase  # type: str
        self.password = password  # type: str
        self.private_key = private_key  # type: str
        self.protocol_name = protocol_name  # type: str
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
        self.host_account_id = host_account_id  # type: str
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateHostAccountResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateHostAccountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateHostGroupRequest(TeaModel):
    def __init__(self, comment=None, host_group_name=None, instance_id=None, region_id=None):
        self.comment = comment  # type: str
        self.host_group_name = host_group_name  # type: str
        self.instance_id = instance_id  # type: str
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
        self.host_group_id = host_group_id  # type: str
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateHostGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateHostGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateHostShareKeyRequest(TeaModel):
    def __init__(self, host_share_key_name=None, instance_id=None, pass_phrase=None, private_key=None,
                 region_id=None):
        self.host_share_key_name = host_share_key_name  # type: str
        self.instance_id = instance_id  # type: str
        self.pass_phrase = pass_phrase  # type: str
        self.private_key = private_key  # type: str
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
        self.host_share_key_id = host_share_key_id  # type: long
        # Id of the request
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateHostShareKeyResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateHostShareKeyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateUserRequest(TeaModel):
    def __init__(self, comment=None, display_name=None, email=None, instance_id=None, mobile=None,
                 mobile_country_code=None, password=None, region_id=None, source=None, source_user_id=None, user_name=None):
        self.comment = comment  # type: str
        self.display_name = display_name  # type: str
        self.email = email  # type: str
        self.instance_id = instance_id  # type: str
        self.mobile = mobile  # type: str
        self.mobile_country_code = mobile_country_code  # type: str
        self.password = password  # type: str
        self.region_id = region_id  # type: str
        self.source = source  # type: str
        self.source_user_id = source_user_id  # type: str
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
        if self.email is not None:
            result['Email'] = self.email
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.mobile is not None:
            result['Mobile'] = self.mobile
        if self.mobile_country_code is not None:
            result['MobileCountryCode'] = self.mobile_country_code
        if self.password is not None:
            result['Password'] = self.password
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.source is not None:
            result['Source'] = self.source
        if self.source_user_id is not None:
            result['SourceUserId'] = self.source_user_id
        if self.user_name is not None:
            result['UserName'] = self.user_name
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Mobile') is not None:
            self.mobile = m.get('Mobile')
        if m.get('MobileCountryCode') is not None:
            self.mobile_country_code = m.get('MobileCountryCode')
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('SourceUserId') is not None:
            self.source_user_id = m.get('SourceUserId')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        return self


class CreateUserResponseBody(TeaModel):
    def __init__(self, request_id=None, user_id=None):
        self.request_id = request_id  # type: str
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateUserResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateUserResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class CreateUserGroupRequest(TeaModel):
    def __init__(self, comment=None, instance_id=None, region_id=None, user_group_name=None):
        self.comment = comment  # type: str
        self.instance_id = instance_id  # type: str
        self.region_id = region_id  # type: str
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
        self.request_id = request_id  # type: str
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: CreateUserGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = CreateUserGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteHostRequest(TeaModel):
    def __init__(self, host_id=None, instance_id=None, region_id=None):
        self.host_id = host_id  # type: str
        self.instance_id = instance_id  # type: str
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteHostResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteHostResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteHostAccountRequest(TeaModel):
    def __init__(self, host_account_id=None, instance_id=None, region_id=None):
        self.host_account_id = host_account_id  # type: str
        self.instance_id = instance_id  # type: str
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteHostAccountResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteHostAccountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteHostGroupRequest(TeaModel):
    def __init__(self, host_group_id=None, instance_id=None, region_id=None):
        self.host_group_id = host_group_id  # type: str
        self.instance_id = instance_id  # type: str
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteHostGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteHostGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteHostShareKeyRequest(TeaModel):
    def __init__(self, host_share_key_id=None, instance_id=None, region_id=None):
        self.host_share_key_id = host_share_key_id  # type: str
        self.instance_id = instance_id  # type: str
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
        # Id of the request
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteHostShareKeyResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteHostShareKeyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteUserRequest(TeaModel):
    def __init__(self, instance_id=None, region_id=None, user_id=None):
        self.instance_id = instance_id  # type: str
        self.region_id = region_id  # type: str
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteUserResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteUserResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DeleteUserGroupRequest(TeaModel):
    def __init__(self, instance_id=None, region_id=None, user_group_id=None):
        self.instance_id = instance_id  # type: str
        self.region_id = region_id  # type: str
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DeleteUserGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DeleteUserGroupResponseBody()
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
        self.custom_port = custom_port  # type: int
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
    def __init__(self, authorized_security_groups=None, description=None, eni_instance_id=None, expire_time=None,
                 instance_id=None, instance_status=None, internet_endpoint=None, intranet_endpoint=None, license_code=None,
                 modify_password_module=None, network_proxy_module=None, ports=None, private_export_ips=None, private_white_list=None,
                 public_export_ips=None, public_ips=None, public_network_access=None, public_white_list=None, region_id=None,
                 resource_group_id=None, security_group_ids=None, start_time=None, storage=None, vpc_id=None, vswitch_id=None,
                 web_terminal_module=None):
        self.authorized_security_groups = authorized_security_groups  # type: list[str]
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeInstanceAttributeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeInstanceAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeInstancesRequestTag(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = key  # type: str
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
        self.instance_id = instance_id  # type: list[str]
        self.instance_status = instance_status  # type: str
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.region_id = region_id  # type: str
        self.resource_group_id = resource_group_id  # type: str
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
        self.description = description  # type: str
        self.expire_time = expire_time  # type: long
        self.image_version = image_version  # type: str
        self.instance_id = instance_id  # type: str
        self.instance_status = instance_status  # type: str
        self.internet_endpoint = internet_endpoint  # type: str
        self.intranet_endpoint = intranet_endpoint  # type: str
        self.legacy = legacy  # type: bool
        self.license_code = license_code  # type: str
        self.plan_code = plan_code  # type: str
        self.public_network_access = public_network_access  # type: bool
        self.region_id = region_id  # type: str
        self.resource_group_id = resource_group_id  # type: str
        self.start_time = start_time  # type: long
        self.vpc_id = vpc_id  # type: str
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
        self.instances = instances  # type: list[DescribeInstancesResponseBodyInstances]
        self.request_id = request_id  # type: str
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeInstancesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeInstancesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DescribeRegionsRequest(TeaModel):
    def __init__(self, accept_language=None):
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
        self.regions = regions  # type: list[DescribeRegionsResponseBodyRegions]
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DescribeRegionsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DescribeRegionsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DetachHostAccountsFromHostShareKeyRequest(TeaModel):
    def __init__(self, host_account_ids=None, host_share_key_id=None, instance_id=None, region_id=None):
        self.host_account_ids = host_account_ids  # type: str
        self.host_share_key_id = host_share_key_id  # type: str
        self.instance_id = instance_id  # type: str
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
        self.code = code  # type: str
        self.host_account_id = host_account_id  # type: str
        self.host_share_key_id = host_share_key_id  # type: str
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
        # Id of the request
        self.request_id = request_id  # type: str
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DetachHostAccountsFromHostShareKeyResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DetachHostAccountsFromHostShareKeyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DetachHostAccountsFromUserRequest(TeaModel):
    def __init__(self, hosts=None, instance_id=None, region_id=None, user_id=None):
        self.hosts = hosts  # type: str
        self.instance_id = instance_id  # type: str
        self.region_id = region_id  # type: str
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
        self.code = code  # type: str
        self.host_account_id = host_account_id  # type: str
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
        self.code = code  # type: str
        self.host_accounts = host_accounts  # type: list[DetachHostAccountsFromUserResponseBodyResultsHostAccounts]
        self.host_id = host_id  # type: str
        self.message = message  # type: str
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
        self.request_id = request_id  # type: str
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DetachHostAccountsFromUserResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DetachHostAccountsFromUserResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DetachHostAccountsFromUserGroupRequest(TeaModel):
    def __init__(self, hosts=None, instance_id=None, region_id=None, user_group_id=None):
        self.hosts = hosts  # type: str
        self.instance_id = instance_id  # type: str
        self.region_id = region_id  # type: str
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
        self.code = code  # type: str
        self.host_account_id = host_account_id  # type: str
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
        self.code = code  # type: str
        self.host_accounts = host_accounts  # type: list[DetachHostAccountsFromUserGroupResponseBodyResultsHostAccounts]
        self.host_id = host_id  # type: str
        self.message = message  # type: str
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
        self.request_id = request_id  # type: str
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DetachHostAccountsFromUserGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DetachHostAccountsFromUserGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DetachHostGroupAccountsFromUserRequest(TeaModel):
    def __init__(self, host_groups=None, instance_id=None, region_id=None, user_id=None):
        self.host_groups = host_groups  # type: str
        self.instance_id = instance_id  # type: str
        self.region_id = region_id  # type: str
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
        self.code = code  # type: str
        self.host_account_name = host_account_name  # type: str
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
        self.code = code  # type: str
        self.host_account_names = host_account_names  # type: list[DetachHostGroupAccountsFromUserResponseBodyResultsHostAccountNames]
        self.host_group_id = host_group_id  # type: str
        self.message = message  # type: str
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
        self.request_id = request_id  # type: str
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DetachHostGroupAccountsFromUserResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DetachHostGroupAccountsFromUserResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DetachHostGroupAccountsFromUserGroupRequest(TeaModel):
    def __init__(self, host_groups=None, instance_id=None, region_id=None, user_group_id=None):
        self.host_groups = host_groups  # type: str
        self.instance_id = instance_id  # type: str
        self.region_id = region_id  # type: str
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
        self.code = code  # type: str
        self.host_account_name = host_account_name  # type: str
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
        self.code = code  # type: str
        self.host_account_names = host_account_names  # type: list[DetachHostGroupAccountsFromUserGroupResponseBodyResultsHostAccountNames]
        self.host_group_id = host_group_id  # type: str
        self.message = message  # type: str
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
        self.request_id = request_id  # type: str
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DetachHostGroupAccountsFromUserGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DetachHostGroupAccountsFromUserGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class DisableInstancePublicAccessRequest(TeaModel):
    def __init__(self, instance_id=None, region_id=None):
        self.instance_id = instance_id  # type: str
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
        self.instance_id = instance_id  # type: str
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: DisableInstancePublicAccessResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = DisableInstancePublicAccessResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class EnableInstancePublicAccessRequest(TeaModel):
    def __init__(self, instance_id=None, region_id=None):
        self.instance_id = instance_id  # type: str
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
        self.instance_id = instance_id  # type: str
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: EnableInstancePublicAccessResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = EnableInstancePublicAccessResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetHostRequest(TeaModel):
    def __init__(self, host_id=None, instance_id=None, region_id=None):
        self.host_id = host_id  # type: str
        self.instance_id = instance_id  # type: str
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
        self.host_finger_print = host_finger_print  # type: str
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
                 host_private_address=None, host_public_address=None, ostype=None, protocols=None, source=None, source_instance_id=None,
                 source_instance_state=None):
        self.active_address_type = active_address_type  # type: str
        self.comment = comment  # type: str
        self.host_id = host_id  # type: str
        self.host_name = host_name  # type: str
        self.host_private_address = host_private_address  # type: str
        self.host_public_address = host_public_address  # type: str
        self.ostype = ostype  # type: str
        self.protocols = protocols  # type: list[GetHostResponseBodyHostProtocols]
        self.source = source  # type: str
        self.source_instance_id = source_instance_id  # type: str
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
        self.host = host  # type: GetHostResponseBodyHost
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetHostResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetHostResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetHostAccountRequest(TeaModel):
    def __init__(self, host_account_id=None, instance_id=None, region_id=None):
        self.host_account_id = host_account_id  # type: str
        self.instance_id = instance_id  # type: str
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
        self.has_password = has_password  # type: bool
        self.host_account_id = host_account_id  # type: str
        self.host_account_name = host_account_name  # type: str
        self.host_id = host_id  # type: str
        self.host_share_key_id = host_share_key_id  # type: str
        self.host_share_key_name = host_share_key_name  # type: str
        self.private_key_fingerprint = private_key_fingerprint  # type: str
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
        self.host_account = host_account  # type: GetHostAccountResponseBodyHostAccount
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetHostAccountResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetHostAccountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetHostGroupRequest(TeaModel):
    def __init__(self, host_group_id=None, instance_id=None, region_id=None):
        self.host_group_id = host_group_id  # type: str
        self.instance_id = instance_id  # type: str
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
        self.comment = comment  # type: str
        self.host_group_id = host_group_id  # type: str
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
        self.host_group = host_group  # type: GetHostGroupResponseBodyHostGroup
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetHostGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetHostGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetHostShareKeyRequest(TeaModel):
    def __init__(self, host_share_key_id=None, instance_id=None, region_id=None):
        self.host_share_key_id = host_share_key_id  # type: str
        self.instance_id = instance_id  # type: str
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
        self.host_share_key = host_share_key  # type: GetHostShareKeyResponseBodyHostShareKey
        # Id of the request
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetHostShareKeyResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetHostShareKeyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetInstanceADAuthServerRequest(TeaModel):
    def __init__(self, instance_id=None, region_id=None):
        self.instance_id = instance_id  # type: str
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
        self.account = account  # type: str
        self.base_dn = base_dn  # type: str
        self.domain = domain  # type: str
        self.email_mapping = email_mapping  # type: str
        self.filter = filter  # type: str
        self.has_password = has_password  # type: bool
        self.is_ssl = is_ssl  # type: bool
        self.mobile_mapping = mobile_mapping  # type: str
        self.name_mapping = name_mapping  # type: str
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
        self.ad = ad  # type: GetInstanceADAuthServerResponseBodyAD
        # Id of the request
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetInstanceADAuthServerResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetInstanceADAuthServerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetInstanceLDAPAuthServerRequest(TeaModel):
    def __init__(self, instance_id=None, region_id=None):
        self.instance_id = instance_id  # type: str
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
        self.account = account  # type: str
        self.base_dn = base_dn  # type: str
        self.email_mapping = email_mapping  # type: str
        self.filter = filter  # type: str
        self.has_password = has_password  # type: str
        self.is_ssl = is_ssl  # type: bool
        self.login_name_mapping = login_name_mapping  # type: str
        self.mobile_mapping = mobile_mapping  # type: str
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
        self.ldap = ldap  # type: GetInstanceLDAPAuthServerResponseBodyLDAP
        # Id of the request
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetInstanceLDAPAuthServerResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetInstanceLDAPAuthServerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetInstanceTwoFactorRequest(TeaModel):
    def __init__(self, instance_id=None, region_id=None):
        self.instance_id = instance_id  # type: str
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


class GetInstanceTwoFactorResponseBodyConfigDingTalkConfig(TeaModel):
    def __init__(self, agent_id=None, app_key=None, has_app_secret=None):
        self.agent_id = agent_id  # type: str
        self.app_key = app_key  # type: str
        self.has_app_secret = has_app_secret  # type: bool

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetInstanceTwoFactorResponseBodyConfigDingTalkConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.agent_id is not None:
            result['AgentId'] = self.agent_id
        if self.app_key is not None:
            result['AppKey'] = self.app_key
        if self.has_app_secret is not None:
            result['HasAppSecret'] = self.has_app_secret
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AgentId') is not None:
            self.agent_id = m.get('AgentId')
        if m.get('AppKey') is not None:
            self.app_key = m.get('AppKey')
        if m.get('HasAppSecret') is not None:
            self.has_app_secret = m.get('HasAppSecret')
        return self


class GetInstanceTwoFactorResponseBodyConfig(TeaModel):
    def __init__(self, ding_talk_config=None, enable_two_factor=None, message_language=None,
                 skip_two_factor_time=None, two_factor_methods=None):
        self.ding_talk_config = ding_talk_config  # type: GetInstanceTwoFactorResponseBodyConfigDingTalkConfig
        self.enable_two_factor = enable_two_factor  # type: bool
        self.message_language = message_language  # type: str
        self.skip_two_factor_time = skip_two_factor_time  # type: long
        self.two_factor_methods = two_factor_methods  # type: list[str]

    def validate(self):
        if self.ding_talk_config:
            self.ding_talk_config.validate()

    def to_map(self):
        _map = super(GetInstanceTwoFactorResponseBodyConfig, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ding_talk_config is not None:
            result['DingTalkConfig'] = self.ding_talk_config.to_map()
        if self.enable_two_factor is not None:
            result['EnableTwoFactor'] = self.enable_two_factor
        if self.message_language is not None:
            result['MessageLanguage'] = self.message_language
        if self.skip_two_factor_time is not None:
            result['SkipTwoFactorTime'] = self.skip_two_factor_time
        if self.two_factor_methods is not None:
            result['TwoFactorMethods'] = self.two_factor_methods
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DingTalkConfig') is not None:
            temp_model = GetInstanceTwoFactorResponseBodyConfigDingTalkConfig()
            self.ding_talk_config = temp_model.from_map(m['DingTalkConfig'])
        if m.get('EnableTwoFactor') is not None:
            self.enable_two_factor = m.get('EnableTwoFactor')
        if m.get('MessageLanguage') is not None:
            self.message_language = m.get('MessageLanguage')
        if m.get('SkipTwoFactorTime') is not None:
            self.skip_two_factor_time = m.get('SkipTwoFactorTime')
        if m.get('TwoFactorMethods') is not None:
            self.two_factor_methods = m.get('TwoFactorMethods')
        return self


class GetInstanceTwoFactorResponseBody(TeaModel):
    def __init__(self, config=None, request_id=None):
        self.config = config  # type: GetInstanceTwoFactorResponseBodyConfig
        # Id of the request
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetInstanceTwoFactorResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetInstanceTwoFactorResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetInstanceUpgradeInfoRequest(TeaModel):
    def __init__(self, instance_id=None, lang=None, region_id=None):
        self.instance_id = instance_id  # type: str
        self.lang = lang  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetInstanceUpgradeInfoRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class GetInstanceUpgradeInfoResponseBodyInstanceUpgradeInfoCandidatePeriodList(TeaModel):
    def __init__(self, candidate_end_time=None, candidate_start_time=None):
        self.candidate_end_time = candidate_end_time  # type: long
        self.candidate_start_time = candidate_start_time  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetInstanceUpgradeInfoResponseBodyInstanceUpgradeInfoCandidatePeriodList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.candidate_end_time is not None:
            result['CandidateEndTime'] = self.candidate_end_time
        if self.candidate_start_time is not None:
            result['CandidateStartTime'] = self.candidate_start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('CandidateEndTime') is not None:
            self.candidate_end_time = m.get('CandidateEndTime')
        if m.get('CandidateStartTime') is not None:
            self.candidate_start_time = m.get('CandidateStartTime')
        return self


class GetInstanceUpgradeInfoResponseBodyInstanceUpgradeInfoInvalidPeriodList(TeaModel):
    def __init__(self, invalid_end_time=None, invalid_start_time=None):
        self.invalid_end_time = invalid_end_time  # type: long
        self.invalid_start_time = invalid_start_time  # type: long

    def validate(self):
        pass

    def to_map(self):
        _map = super(GetInstanceUpgradeInfoResponseBodyInstanceUpgradeInfoInvalidPeriodList, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.invalid_end_time is not None:
            result['InvalidEndTime'] = self.invalid_end_time
        if self.invalid_start_time is not None:
            result['InvalidStartTime'] = self.invalid_start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InvalidEndTime') is not None:
            self.invalid_end_time = m.get('InvalidEndTime')
        if m.get('InvalidStartTime') is not None:
            self.invalid_start_time = m.get('InvalidStartTime')
        return self


class GetInstanceUpgradeInfoResponseBodyInstanceUpgradeInfo(TeaModel):
    def __init__(self, ali_uid=None, candidate_period_list=None, image_version=None, instance_id=None,
                 invalid_period_list=None, latest_start_time=None, operable=None, period_interval=None, upgrade_end_time=None,
                 upgrade_mode=None, upgrade_start_time=None):
        self.ali_uid = ali_uid  # type: long
        self.candidate_period_list = candidate_period_list  # type: list[GetInstanceUpgradeInfoResponseBodyInstanceUpgradeInfoCandidatePeriodList]
        self.image_version = image_version  # type: str
        self.instance_id = instance_id  # type: str
        self.invalid_period_list = invalid_period_list  # type: list[GetInstanceUpgradeInfoResponseBodyInstanceUpgradeInfoInvalidPeriodList]
        self.latest_start_time = latest_start_time  # type: long
        self.operable = operable  # type: bool
        self.period_interval = period_interval  # type: int
        self.upgrade_end_time = upgrade_end_time  # type: long
        self.upgrade_mode = upgrade_mode  # type: str
        self.upgrade_start_time = upgrade_start_time  # type: long

    def validate(self):
        if self.candidate_period_list:
            for k in self.candidate_period_list:
                if k:
                    k.validate()
        if self.invalid_period_list:
            for k in self.invalid_period_list:
                if k:
                    k.validate()

    def to_map(self):
        _map = super(GetInstanceUpgradeInfoResponseBodyInstanceUpgradeInfo, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ali_uid is not None:
            result['AliUid'] = self.ali_uid
        result['CandidatePeriodList'] = []
        if self.candidate_period_list is not None:
            for k in self.candidate_period_list:
                result['CandidatePeriodList'].append(k.to_map() if k else None)
        if self.image_version is not None:
            result['ImageVersion'] = self.image_version
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        result['InvalidPeriodList'] = []
        if self.invalid_period_list is not None:
            for k in self.invalid_period_list:
                result['InvalidPeriodList'].append(k.to_map() if k else None)
        if self.latest_start_time is not None:
            result['LatestStartTime'] = self.latest_start_time
        if self.operable is not None:
            result['Operable'] = self.operable
        if self.period_interval is not None:
            result['PeriodInterval'] = self.period_interval
        if self.upgrade_end_time is not None:
            result['UpgradeEndTime'] = self.upgrade_end_time
        if self.upgrade_mode is not None:
            result['UpgradeMode'] = self.upgrade_mode
        if self.upgrade_start_time is not None:
            result['UpgradeStartTime'] = self.upgrade_start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('AliUid') is not None:
            self.ali_uid = m.get('AliUid')
        self.candidate_period_list = []
        if m.get('CandidatePeriodList') is not None:
            for k in m.get('CandidatePeriodList'):
                temp_model = GetInstanceUpgradeInfoResponseBodyInstanceUpgradeInfoCandidatePeriodList()
                self.candidate_period_list.append(temp_model.from_map(k))
        if m.get('ImageVersion') is not None:
            self.image_version = m.get('ImageVersion')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        self.invalid_period_list = []
        if m.get('InvalidPeriodList') is not None:
            for k in m.get('InvalidPeriodList'):
                temp_model = GetInstanceUpgradeInfoResponseBodyInstanceUpgradeInfoInvalidPeriodList()
                self.invalid_period_list.append(temp_model.from_map(k))
        if m.get('LatestStartTime') is not None:
            self.latest_start_time = m.get('LatestStartTime')
        if m.get('Operable') is not None:
            self.operable = m.get('Operable')
        if m.get('PeriodInterval') is not None:
            self.period_interval = m.get('PeriodInterval')
        if m.get('UpgradeEndTime') is not None:
            self.upgrade_end_time = m.get('UpgradeEndTime')
        if m.get('UpgradeMode') is not None:
            self.upgrade_mode = m.get('UpgradeMode')
        if m.get('UpgradeStartTime') is not None:
            self.upgrade_start_time = m.get('UpgradeStartTime')
        return self


class GetInstanceUpgradeInfoResponseBody(TeaModel):
    def __init__(self, instance_upgrade_info=None, request_id=None):
        self.instance_upgrade_info = instance_upgrade_info  # type: GetInstanceUpgradeInfoResponseBodyInstanceUpgradeInfo
        self.request_id = request_id  # type: str

    def validate(self):
        if self.instance_upgrade_info:
            self.instance_upgrade_info.validate()

    def to_map(self):
        _map = super(GetInstanceUpgradeInfoResponseBody, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_upgrade_info is not None:
            result['InstanceUpgradeInfo'] = self.instance_upgrade_info.to_map()
        if self.request_id is not None:
            result['RequestId'] = self.request_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceUpgradeInfo') is not None:
            temp_model = GetInstanceUpgradeInfoResponseBodyInstanceUpgradeInfo()
            self.instance_upgrade_info = temp_model.from_map(m['InstanceUpgradeInfo'])
        if m.get('RequestId') is not None:
            self.request_id = m.get('RequestId')
        return self


class GetInstanceUpgradeInfoResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetInstanceUpgradeInfoResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(GetInstanceUpgradeInfoResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetInstanceUpgradeInfoResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetUserRequest(TeaModel):
    def __init__(self, instance_id=None, region_id=None, user_id=None):
        self.instance_id = instance_id  # type: str
        self.region_id = region_id  # type: str
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
    def __init__(self, comment=None, display_name=None, email=None, mobile=None, mobile_country_code=None,
                 source=None, source_user_id=None, user_id=None, user_name=None, user_state=None):
        self.comment = comment  # type: str
        self.display_name = display_name  # type: str
        self.email = email  # type: str
        self.mobile = mobile  # type: str
        self.mobile_country_code = mobile_country_code  # type: str
        self.source = source  # type: str
        self.source_user_id = source_user_id  # type: str
        self.user_id = user_id  # type: str
        self.user_name = user_name  # type: str
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
        if self.email is not None:
            result['Email'] = self.email
        if self.mobile is not None:
            result['Mobile'] = self.mobile
        if self.mobile_country_code is not None:
            result['MobileCountryCode'] = self.mobile_country_code
        if self.source is not None:
            result['Source'] = self.source
        if self.source_user_id is not None:
            result['SourceUserId'] = self.source_user_id
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
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('Mobile') is not None:
            self.mobile = m.get('Mobile')
        if m.get('MobileCountryCode') is not None:
            self.mobile_country_code = m.get('MobileCountryCode')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('SourceUserId') is not None:
            self.source_user_id = m.get('SourceUserId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        if m.get('UserState') is not None:
            self.user_state = m.get('UserState')
        return self


class GetUserResponseBody(TeaModel):
    def __init__(self, request_id=None, user=None):
        self.request_id = request_id  # type: str
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetUserResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetUserResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class GetUserGroupRequest(TeaModel):
    def __init__(self, instance_id=None, region_id=None, user_group_id=None):
        self.instance_id = instance_id  # type: str
        self.region_id = region_id  # type: str
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
        self.comment = comment  # type: str
        self.user_group_id = user_group_id  # type: str
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
        self.request_id = request_id  # type: str
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: GetUserGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = GetUserGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListHostAccountsRequest(TeaModel):
    def __init__(self, host_account_name=None, host_id=None, instance_id=None, page_number=None, page_size=None,
                 protocol_name=None, region_id=None):
        self.host_account_name = host_account_name  # type: str
        self.host_id = host_id  # type: str
        self.instance_id = instance_id  # type: str
        self.page_number = page_number  # type: str
        self.page_size = page_size  # type: str
        self.protocol_name = protocol_name  # type: str
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
        self.has_password = has_password  # type: bool
        self.host_account_id = host_account_id  # type: str
        self.host_account_name = host_account_name  # type: str
        self.host_id = host_id  # type: str
        self.host_share_key_id = host_share_key_id  # type: str
        self.host_share_key_name = host_share_key_name  # type: str
        self.private_key_fingerprint = private_key_fingerprint  # type: str
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
        self.host_accounts = host_accounts  # type: list[ListHostAccountsResponseBodyHostAccounts]
        self.request_id = request_id  # type: str
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListHostAccountsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListHostAccountsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListHostAccountsForHostShareKeyRequest(TeaModel):
    def __init__(self, host_share_key_id=None, instance_id=None, page_number=None, page_size=None, region_id=None):
        self.host_share_key_id = host_share_key_id  # type: str
        self.instance_id = instance_id  # type: str
        self.page_number = page_number  # type: str
        self.page_size = page_size  # type: str
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
        self.host_account_name = host_account_name  # type: str
        self.host_id = host_id  # type: str
        self.hosts_account_id = hosts_account_id  # type: str
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
        self.host_accounts = host_accounts  # type: list[ListHostAccountsForHostShareKeyResponseBodyHostAccounts]
        # Id of the request
        self.request_id = request_id  # type: str
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListHostAccountsForHostShareKeyResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListHostAccountsForHostShareKeyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListHostAccountsForUserRequest(TeaModel):
    def __init__(self, host_account_name=None, host_id=None, instance_id=None, page_number=None, page_size=None,
                 region_id=None, user_id=None):
        self.host_account_name = host_account_name  # type: str
        self.host_id = host_id  # type: str
        self.instance_id = instance_id  # type: str
        self.page_number = page_number  # type: str
        self.page_size = page_size  # type: str
        self.region_id = region_id  # type: str
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
        self.host_account_id = host_account_id  # type: str
        self.host_account_name = host_account_name  # type: str
        self.host_id = host_id  # type: str
        self.is_authorized = is_authorized  # type: bool
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
        self.host_accounts = host_accounts  # type: list[ListHostAccountsForUserResponseBodyHostAccounts]
        self.request_id = request_id  # type: str
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListHostAccountsForUserResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListHostAccountsForUserResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListHostAccountsForUserGroupRequest(TeaModel):
    def __init__(self, host_account_name=None, host_id=None, instance_id=None, page_number=None, page_size=None,
                 region_id=None, user_group_id=None):
        self.host_account_name = host_account_name  # type: str
        self.host_id = host_id  # type: str
        self.instance_id = instance_id  # type: str
        self.page_number = page_number  # type: str
        self.page_size = page_size  # type: str
        self.region_id = region_id  # type: str
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
        self.host_account_id = host_account_id  # type: str
        self.host_account_name = host_account_name  # type: str
        self.host_id = host_id  # type: str
        self.is_authorized = is_authorized  # type: bool
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
        self.host_accounts = host_accounts  # type: list[ListHostAccountsForUserGroupResponseBodyHostAccounts]
        self.request_id = request_id  # type: str
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListHostAccountsForUserGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListHostAccountsForUserGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListHostGroupAccountNamesForUserRequest(TeaModel):
    def __init__(self, host_group_id=None, instance_id=None, region_id=None, user_id=None):
        self.host_group_id = host_group_id  # type: str
        self.instance_id = instance_id  # type: str
        self.region_id = region_id  # type: str
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
        self.host_account_names = host_account_names  # type: list[str]
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListHostGroupAccountNamesForUserResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListHostGroupAccountNamesForUserResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListHostGroupAccountNamesForUserGroupRequest(TeaModel):
    def __init__(self, host_group_id=None, instance_id=None, region_id=None, user_group_id=None):
        self.host_group_id = host_group_id  # type: str
        self.instance_id = instance_id  # type: str
        self.region_id = region_id  # type: str
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListHostGroupAccountNamesForUserGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListHostGroupAccountNamesForUserGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListHostGroupsRequest(TeaModel):
    def __init__(self, host_group_name=None, instance_id=None, page_number=None, page_size=None, region_id=None):
        self.host_group_name = host_group_name  # type: str
        self.instance_id = instance_id  # type: str
        self.page_number = page_number  # type: str
        self.page_size = page_size  # type: str
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
        self.comment = comment  # type: str
        self.host_group_id = host_group_id  # type: str
        self.host_group_name = host_group_name  # type: str
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
        self.host_groups = host_groups  # type: list[ListHostGroupsResponseBodyHostGroups]
        self.request_id = request_id  # type: str
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListHostGroupsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListHostGroupsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListHostGroupsForUserRequest(TeaModel):
    def __init__(self, host_group_name=None, instance_id=None, mode=None, page_number=None, page_size=None,
                 region_id=None, user_id=None):
        self.host_group_name = host_group_name  # type: str
        self.instance_id = instance_id  # type: str
        self.mode = mode  # type: str
        self.page_number = page_number  # type: str
        self.page_size = page_size  # type: str
        self.region_id = region_id  # type: str
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
        self.comment = comment  # type: str
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
        self.host_groups = host_groups  # type: list[ListHostGroupsForUserResponseBodyHostGroups]
        self.request_id = request_id  # type: str
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListHostGroupsForUserResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListHostGroupsForUserResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListHostGroupsForUserGroupRequest(TeaModel):
    def __init__(self, host_group_name=None, instance_id=None, mode=None, page_number=None, page_size=None,
                 region_id=None, user_group_id=None):
        self.host_group_name = host_group_name  # type: str
        self.instance_id = instance_id  # type: str
        self.mode = mode  # type: str
        self.page_number = page_number  # type: str
        self.page_size = page_size  # type: str
        self.region_id = region_id  # type: str
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
        self.comment = comment  # type: str
        self.host_group_id = host_group_id  # type: str
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
        self.host_groups = host_groups  # type: list[ListHostGroupsForUserGroupResponseBodyHostGroups]
        self.request_id = request_id  # type: str
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListHostGroupsForUserGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListHostGroupsForUserGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListHostShareKeysRequest(TeaModel):
    def __init__(self, instance_id=None, page_number=None, page_size=None, region_id=None):
        self.instance_id = instance_id  # type: str
        self.page_number = page_number  # type: str
        self.page_size = page_size  # type: str
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
        self.host_account_count = host_account_count  # type: long
        self.host_share_key_id = host_share_key_id  # type: str
        self.host_share_key_name = host_share_key_name  # type: str
        self.last_modify_key_at = last_modify_key_at  # type: long
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
        self.host_share_keys = host_share_keys  # type: list[ListHostShareKeysResponseBodyHostShareKeys]
        # Id of the request
        self.request_id = request_id  # type: str
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListHostShareKeysResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListHostShareKeysResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListHostsRequest(TeaModel):
    def __init__(self, host_address=None, host_group_id=None, host_name=None, instance_id=None, ostype=None,
                 page_number=None, page_size=None, region_id=None, source=None, source_instance_id=None,
                 source_instance_state=None):
        self.host_address = host_address  # type: str
        self.host_group_id = host_group_id  # type: str
        self.host_name = host_name  # type: str
        self.instance_id = instance_id  # type: str
        self.ostype = ostype  # type: str
        self.page_number = page_number  # type: str
        self.page_size = page_size  # type: str
        self.region_id = region_id  # type: str
        self.source = source  # type: str
        self.source_instance_id = source_instance_id  # type: str
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
        self.active_address_type = active_address_type  # type: str
        self.comment = comment  # type: str
        self.host_account_count = host_account_count  # type: int
        self.host_id = host_id  # type: str
        self.host_name = host_name  # type: str
        self.host_private_address = host_private_address  # type: str
        self.host_public_address = host_public_address  # type: str
        self.ostype = ostype  # type: str
        self.source = source  # type: str
        self.source_instance_id = source_instance_id  # type: str
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
        self.hosts = hosts  # type: list[ListHostsResponseBodyHosts]
        self.request_id = request_id  # type: str
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListHostsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListHostsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListHostsForUserRequest(TeaModel):
    def __init__(self, host_address=None, host_name=None, instance_id=None, mode=None, ostype=None, page_number=None,
                 page_size=None, region_id=None, user_id=None):
        self.host_address = host_address  # type: str
        self.host_name = host_name  # type: str
        self.instance_id = instance_id  # type: str
        self.mode = mode  # type: str
        self.ostype = ostype  # type: str
        self.page_number = page_number  # type: str
        self.page_size = page_size  # type: str
        self.region_id = region_id  # type: str
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
        self.active_address_type = active_address_type  # type: str
        self.comment = comment  # type: str
        self.host_id = host_id  # type: str
        self.host_name = host_name  # type: str
        self.host_private_address = host_private_address  # type: str
        self.host_public_address = host_public_address  # type: str
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
        self.hosts = hosts  # type: list[ListHostsForUserResponseBodyHosts]
        self.request_id = request_id  # type: str
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListHostsForUserResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListHostsForUserResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListHostsForUserGroupRequest(TeaModel):
    def __init__(self, host_address=None, host_name=None, instance_id=None, mode=None, ostype=None, page_number=None,
                 page_size=None, region_id=None, user_group_id=None):
        self.host_address = host_address  # type: str
        self.host_name = host_name  # type: str
        self.instance_id = instance_id  # type: str
        self.mode = mode  # type: str
        self.ostype = ostype  # type: str
        self.page_number = page_number  # type: str
        self.page_size = page_size  # type: str
        self.region_id = region_id  # type: str
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
        self.active_address_type = active_address_type  # type: str
        self.comment = comment  # type: str
        self.host_id = host_id  # type: str
        self.host_name = host_name  # type: str
        self.host_private_address = host_private_address  # type: str
        self.host_public_address = host_public_address  # type: str
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
        self.hosts = hosts  # type: list[ListHostsForUserGroupResponseBodyHosts]
        self.request_id = request_id  # type: str
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListHostsForUserGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListHostsForUserGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTagKeysRequest(TeaModel):
    def __init__(self, page_number=None, page_size=None, region_id=None, resource_type=None):
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.region_id = region_id  # type: str
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
        self.tag_count = tag_count  # type: int
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
        self.page_number = page_number  # type: int
        self.page_size = page_size  # type: int
        self.request_id = request_id  # type: str
        self.tag_keys = tag_keys  # type: list[ListTagKeysResponseBodyTagKeys]
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListTagKeysResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListTagKeysResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListTagResourcesRequestTag(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = key  # type: str
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
        self.next_token = next_token  # type: str
        self.region_id = region_id  # type: str
        self.resource_id = resource_id  # type: list[str]
        self.resource_type = resource_type  # type: str
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
        self.next_token = next_token  # type: str
        self.request_id = request_id  # type: str
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListTagResourcesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListUserGroupsResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListUserGroupsResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ListUsersRequest(TeaModel):
    def __init__(self, display_name=None, instance_id=None, mobile=None, page_number=None, page_size=None,
                 region_id=None, source=None, source_user_id=None, user_group_id=None, user_name=None, user_state=None):
        self.display_name = display_name  # type: str
        self.instance_id = instance_id  # type: str
        self.mobile = mobile  # type: str
        self.page_number = page_number  # type: str
        self.page_size = page_size  # type: str
        self.region_id = region_id  # type: str
        self.source = source  # type: str
        self.source_user_id = source_user_id  # type: str
        self.user_group_id = user_group_id  # type: str
        self.user_name = user_name  # type: str
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
    def __init__(self, comment=None, display_name=None, email=None, mobile=None, mobile_country_code=None,
                 source=None, source_user_id=None, user_id=None, user_name=None, user_state=None):
        self.comment = comment  # type: str
        self.display_name = display_name  # type: str
        self.email = email  # type: str
        self.mobile = mobile  # type: str
        self.mobile_country_code = mobile_country_code  # type: str
        self.source = source  # type: str
        self.source_user_id = source_user_id  # type: str
        self.user_id = user_id  # type: str
        self.user_name = user_name  # type: str
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
        if self.email is not None:
            result['Email'] = self.email
        if self.mobile is not None:
            result['Mobile'] = self.mobile
        if self.mobile_country_code is not None:
            result['MobileCountryCode'] = self.mobile_country_code
        if self.source is not None:
            result['Source'] = self.source
        if self.source_user_id is not None:
            result['SourceUserId'] = self.source_user_id
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
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('Mobile') is not None:
            self.mobile = m.get('Mobile')
        if m.get('MobileCountryCode') is not None:
            self.mobile_country_code = m.get('MobileCountryCode')
        if m.get('Source') is not None:
            self.source = m.get('Source')
        if m.get('SourceUserId') is not None:
            self.source_user_id = m.get('SourceUserId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        if m.get('UserName') is not None:
            self.user_name = m.get('UserName')
        if m.get('UserState') is not None:
            self.user_state = m.get('UserState')
        return self


class ListUsersResponseBody(TeaModel):
    def __init__(self, request_id=None, total_count=None, users=None):
        self.request_id = request_id  # type: str
        self.total_count = total_count  # type: int
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ListUsersResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ListUsersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class LockUsersRequest(TeaModel):
    def __init__(self, instance_id=None, region_id=None, user_ids=None):
        self.instance_id = instance_id  # type: str
        self.region_id = region_id  # type: str
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
        self.code = code  # type: str
        self.message = message  # type: str
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
        self.request_id = request_id  # type: str
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: LockUsersResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = LockUsersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyHostRequest(TeaModel):
    def __init__(self, comment=None, host_id=None, host_name=None, host_private_address=None,
                 host_public_address=None, instance_id=None, ostype=None, region_id=None):
        self.comment = comment  # type: str
        self.host_id = host_id  # type: str
        self.host_name = host_name  # type: str
        self.host_private_address = host_private_address  # type: str
        self.host_public_address = host_public_address  # type: str
        self.instance_id = instance_id  # type: str
        self.ostype = ostype  # type: str
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
        if m.get('OSType') is not None:
            self.ostype = m.get('OSType')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class ModifyHostResponseBody(TeaModel):
    def __init__(self, request_id=None):
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ModifyHostResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyHostResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyHostAccountRequest(TeaModel):
    def __init__(self, host_account_id=None, host_account_name=None, host_share_key_id=None, instance_id=None,
                 pass_phrase=None, password=None, private_key=None, region_id=None):
        self.host_account_id = host_account_id  # type: str
        self.host_account_name = host_account_name  # type: str
        self.host_share_key_id = host_share_key_id  # type: str
        self.instance_id = instance_id  # type: str
        self.pass_phrase = pass_phrase  # type: str
        self.password = password  # type: str
        self.private_key = private_key  # type: str
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ModifyHostAccountResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyHostAccountResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyHostGroupRequest(TeaModel):
    def __init__(self, comment=None, host_group_id=None, host_group_name=None, instance_id=None, region_id=None):
        self.comment = comment  # type: str
        self.host_group_id = host_group_id  # type: str
        self.host_group_name = host_group_name  # type: str
        self.instance_id = instance_id  # type: str
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ModifyHostGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyHostGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyHostShareKeyRequest(TeaModel):
    def __init__(self, host_share_key_id=None, host_share_key_name=None, instance_id=None, pass_phrase=None,
                 private_key=None, region_id=None):
        self.host_share_key_id = host_share_key_id  # type: str
        self.host_share_key_name = host_share_key_name  # type: str
        self.instance_id = instance_id  # type: str
        self.pass_phrase = pass_phrase  # type: str
        self.private_key = private_key  # type: str
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
        # Id of the request
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ModifyHostShareKeyResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyHostShareKeyResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyHostsActiveAddressTypeRequest(TeaModel):
    def __init__(self, active_address_type=None, host_ids=None, instance_id=None, region_id=None):
        self.active_address_type = active_address_type  # type: str
        self.host_ids = host_ids  # type: str
        self.instance_id = instance_id  # type: str
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
        self.code = code  # type: str
        self.host_id = host_id  # type: str
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
        self.request_id = request_id  # type: str
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ModifyHostsActiveAddressTypeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyHostsActiveAddressTypeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyHostsPortRequest(TeaModel):
    def __init__(self, host_ids=None, instance_id=None, port=None, protocol_name=None, region_id=None):
        self.host_ids = host_ids  # type: str
        self.instance_id = instance_id  # type: str
        self.port = port  # type: str
        self.protocol_name = protocol_name  # type: str
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
        self.code = code  # type: str
        self.host_id = host_id  # type: str
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
        self.request_id = request_id  # type: str
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ModifyHostsPortResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyHostsPortResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyInstanceADAuthServerRequest(TeaModel):
    def __init__(self, account=None, base_dn=None, domain=None, email_mapping=None, filter=None, instance_id=None,
                 is_ssl=None, mobile_mapping=None, name_mapping=None, password=None, port=None, region_id=None, server=None,
                 standby_server=None):
        self.account = account  # type: str
        self.base_dn = base_dn  # type: str
        self.domain = domain  # type: str
        self.email_mapping = email_mapping  # type: str
        self.filter = filter  # type: str
        self.instance_id = instance_id  # type: str
        self.is_ssl = is_ssl  # type: str
        self.mobile_mapping = mobile_mapping  # type: str
        self.name_mapping = name_mapping  # type: str
        self.password = password  # type: str
        self.port = port  # type: str
        self.region_id = region_id  # type: str
        self.server = server  # type: str
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
        # Id of the request
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ModifyInstanceADAuthServerResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyInstanceADAuthServerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyInstanceAttributeRequest(TeaModel):
    def __init__(self, description=None, instance_id=None, region_id=None):
        self.description = description  # type: str
        self.instance_id = instance_id  # type: str
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ModifyInstanceAttributeResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyInstanceAttributeResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyInstanceLDAPAuthServerRequest(TeaModel):
    def __init__(self, account=None, base_dn=None, email_mapping=None, filter=None, instance_id=None, is_ssl=None,
                 login_name_mapping=None, mobile_mapping=None, name_mapping=None, password=None, port=None, region_id=None, server=None,
                 standby_server=None):
        self.account = account  # type: str
        self.base_dn = base_dn  # type: str
        self.email_mapping = email_mapping  # type: str
        self.filter = filter  # type: str
        self.instance_id = instance_id  # type: str
        self.is_ssl = is_ssl  # type: str
        self.login_name_mapping = login_name_mapping  # type: str
        self.mobile_mapping = mobile_mapping  # type: str
        self.name_mapping = name_mapping  # type: str
        self.password = password  # type: str
        self.port = port  # type: str
        self.region_id = region_id  # type: str
        self.server = server  # type: str
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
        # Id of the request
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ModifyInstanceLDAPAuthServerResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyInstanceLDAPAuthServerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyInstanceTwoFactorRequest(TeaModel):
    def __init__(self, ding_talk_config=None, enable_two_factor=None, instance_id=None, message_language=None,
                 region_id=None, skip_two_factor_time=None, two_factor_methods=None):
        self.ding_talk_config = ding_talk_config  # type: str
        self.enable_two_factor = enable_two_factor  # type: str
        self.instance_id = instance_id  # type: str
        self.message_language = message_language  # type: str
        self.region_id = region_id  # type: str
        self.skip_two_factor_time = skip_two_factor_time  # type: str
        self.two_factor_methods = two_factor_methods  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyInstanceTwoFactorRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.ding_talk_config is not None:
            result['DingTalkConfig'] = self.ding_talk_config
        if self.enable_two_factor is not None:
            result['EnableTwoFactor'] = self.enable_two_factor
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.message_language is not None:
            result['MessageLanguage'] = self.message_language
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.skip_two_factor_time is not None:
            result['SkipTwoFactorTime'] = self.skip_two_factor_time
        if self.two_factor_methods is not None:
            result['TwoFactorMethods'] = self.two_factor_methods
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('DingTalkConfig') is not None:
            self.ding_talk_config = m.get('DingTalkConfig')
        if m.get('EnableTwoFactor') is not None:
            self.enable_two_factor = m.get('EnableTwoFactor')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('MessageLanguage') is not None:
            self.message_language = m.get('MessageLanguage')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('SkipTwoFactorTime') is not None:
            self.skip_two_factor_time = m.get('SkipTwoFactorTime')
        if m.get('TwoFactorMethods') is not None:
            self.two_factor_methods = m.get('TwoFactorMethods')
        return self


class ModifyInstanceTwoFactorResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # Id of the request
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ModifyInstanceTwoFactorResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyInstanceTwoFactorResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyInstanceUpgradePeriodRequest(TeaModel):
    def __init__(self, instance_id=None, lang=None, region_id=None, upgrade_mode=None, upgrade_start_time=None):
        self.instance_id = instance_id  # type: str
        self.lang = lang  # type: str
        self.region_id = region_id  # type: str
        self.upgrade_mode = upgrade_mode  # type: str
        self.upgrade_start_time = upgrade_start_time  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyInstanceUpgradePeriodRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.upgrade_mode is not None:
            result['UpgradeMode'] = self.upgrade_mode
        if self.upgrade_start_time is not None:
            result['UpgradeStartTime'] = self.upgrade_start_time
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('UpgradeMode') is not None:
            self.upgrade_mode = m.get('UpgradeMode')
        if m.get('UpgradeStartTime') is not None:
            self.upgrade_start_time = m.get('UpgradeStartTime')
        return self


class ModifyInstanceUpgradePeriodResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(ModifyInstanceUpgradePeriodResponseBody, self).to_map()
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


class ModifyInstanceUpgradePeriodResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ModifyInstanceUpgradePeriodResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(ModifyInstanceUpgradePeriodResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyInstanceUpgradePeriodResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyUserRequest(TeaModel):
    def __init__(self, comment=None, display_name=None, email=None, instance_id=None, mobile=None,
                 mobile_country_code=None, password=None, region_id=None, user_id=None):
        self.comment = comment  # type: str
        self.display_name = display_name  # type: str
        self.email = email  # type: str
        self.instance_id = instance_id  # type: str
        self.mobile = mobile  # type: str
        self.mobile_country_code = mobile_country_code  # type: str
        self.password = password  # type: str
        self.region_id = region_id  # type: str
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
        if self.email is not None:
            result['Email'] = self.email
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.mobile is not None:
            result['Mobile'] = self.mobile
        if self.mobile_country_code is not None:
            result['MobileCountryCode'] = self.mobile_country_code
        if self.password is not None:
            result['Password'] = self.password
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        if self.user_id is not None:
            result['UserId'] = self.user_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('Comment') is not None:
            self.comment = m.get('Comment')
        if m.get('DisplayName') is not None:
            self.display_name = m.get('DisplayName')
        if m.get('Email') is not None:
            self.email = m.get('Email')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Mobile') is not None:
            self.mobile = m.get('Mobile')
        if m.get('MobileCountryCode') is not None:
            self.mobile_country_code = m.get('MobileCountryCode')
        if m.get('Password') is not None:
            self.password = m.get('Password')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        if m.get('UserId') is not None:
            self.user_id = m.get('UserId')
        return self


class ModifyUserResponseBody(TeaModel):
    def __init__(self, request_id=None):
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ModifyUserResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyUserResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ModifyUserGroupRequest(TeaModel):
    def __init__(self, comment=None, instance_id=None, region_id=None, user_group_id=None, user_group_name=None):
        self.comment = comment  # type: str
        self.instance_id = instance_id  # type: str
        self.region_id = region_id  # type: str
        self.user_group_id = user_group_id  # type: str
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ModifyUserGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ModifyUserGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class MoveResourceGroupRequest(TeaModel):
    def __init__(self, region_id=None, resource_group_id=None, resource_id=None, resource_type=None):
        self.region_id = region_id  # type: str
        self.resource_group_id = resource_group_id  # type: str
        self.resource_id = resource_id  # type: str
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: MoveResourceGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = MoveResourceGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RemoveHostsFromGroupRequest(TeaModel):
    def __init__(self, host_group_id=None, host_ids=None, instance_id=None, region_id=None):
        self.host_group_id = host_group_id  # type: str
        self.host_ids = host_ids  # type: str
        self.instance_id = instance_id  # type: str
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
        self.code = code  # type: str
        self.host_group_id = host_group_id  # type: str
        self.host_id = host_id  # type: str
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
        self.request_id = request_id  # type: str
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: RemoveHostsFromGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = RemoveHostsFromGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class RemoveUsersFromGroupRequest(TeaModel):
    def __init__(self, instance_id=None, region_id=None, user_group_id=None, user_ids=None):
        self.instance_id = instance_id  # type: str
        self.region_id = region_id  # type: str
        self.user_group_id = user_group_id  # type: str
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
        self.code = code  # type: str
        self.message = message  # type: str
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
        self.request_id = request_id  # type: str
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: RemoveUsersFromGroupResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = RemoveUsersFromGroupResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class ResetHostAccountCredentialRequest(TeaModel):
    def __init__(self, credential_type=None, host_account_id=None, instance_id=None, region_id=None):
        self.credential_type = credential_type  # type: str
        self.host_account_id = host_account_id  # type: str
        self.instance_id = instance_id  # type: str
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: ResetHostAccountCredentialResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = ResetHostAccountCredentialResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class StartInstanceRequest(TeaModel):
    def __init__(self, instance_id=None, region_id=None, security_group_ids=None, vswitch_id=None):
        self.instance_id = instance_id  # type: str
        self.region_id = region_id  # type: str
        self.security_group_ids = security_group_ids  # type: list[str]
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
        self.instance_id = instance_id  # type: str
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: StartInstanceResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = StartInstanceResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class TagResourcesRequestTag(TeaModel):
    def __init__(self, key=None, value=None):
        self.key = key  # type: str
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
        self.region_id = region_id  # type: str
        self.resource_id = resource_id  # type: list[str]
        self.resource_type = resource_type  # type: str
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: TagResourcesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = TagResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UnlockUsersRequest(TeaModel):
    def __init__(self, instance_id=None, region_id=None, user_ids=None):
        self.instance_id = instance_id  # type: str
        self.region_id = region_id  # type: str
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
        self.code = code  # type: str
        self.message = message  # type: str
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
        self.request_id = request_id  # type: str
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UnlockUsersResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UnlockUsersResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UntagResourcesRequest(TeaModel):
    def __init__(self, all=None, region_id=None, resource_id=None, resource_type=None, tag_key=None):
        self.all = all  # type: bool
        self.region_id = region_id  # type: str
        self.resource_id = resource_id  # type: list[str]
        self.resource_type = resource_type  # type: str
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
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UntagResourcesResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
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
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UntagResourcesResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class UpgradeInstanceImageVersionRequest(TeaModel):
    def __init__(self, instance_id=None, lang=None, region_id=None):
        self.instance_id = instance_id  # type: str
        self.lang = lang  # type: str
        self.region_id = region_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpgradeInstanceImageVersionRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.lang is not None:
            result['Lang'] = self.lang
        if self.region_id is not None:
            result['RegionId'] = self.region_id
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('Lang') is not None:
            self.lang = m.get('Lang')
        if m.get('RegionId') is not None:
            self.region_id = m.get('RegionId')
        return self


class UpgradeInstanceImageVersionResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(UpgradeInstanceImageVersionResponseBody, self).to_map()
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


class UpgradeInstanceImageVersionResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: UpgradeInstanceImageVersionResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(UpgradeInstanceImageVersionResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = UpgradeInstanceImageVersionResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class VerifyInstanceADAuthServerRequest(TeaModel):
    def __init__(self, account=None, base_dn=None, domain=None, filter=None, instance_id=None, is_ssl=None,
                 password=None, port=None, region_id=None, server=None, standby_server=None):
        self.account = account  # type: str
        self.base_dn = base_dn  # type: str
        self.domain = domain  # type: str
        self.filter = filter  # type: str
        self.instance_id = instance_id  # type: str
        self.is_ssl = is_ssl  # type: str
        self.password = password  # type: str
        self.port = port  # type: str
        self.region_id = region_id  # type: str
        self.server = server  # type: str
        self.standby_server = standby_server  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(VerifyInstanceADAuthServerRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account is not None:
            result['Account'] = self.account
        if self.base_dn is not None:
            result['BaseDN'] = self.base_dn
        if self.domain is not None:
            result['Domain'] = self.domain
        if self.filter is not None:
            result['Filter'] = self.filter
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.is_ssl is not None:
            result['IsSSL'] = self.is_ssl
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
        if m.get('Filter') is not None:
            self.filter = m.get('Filter')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('IsSSL') is not None:
            self.is_ssl = m.get('IsSSL')
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


class VerifyInstanceADAuthServerResponseBody(TeaModel):
    def __init__(self, request_id=None):
        # Id of the request
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(VerifyInstanceADAuthServerResponseBody, self).to_map()
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


class VerifyInstanceADAuthServerResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: VerifyInstanceADAuthServerResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(VerifyInstanceADAuthServerResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = VerifyInstanceADAuthServerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


class VerifyInstanceLDAPAuthServerRequest(TeaModel):
    def __init__(self, account=None, base_dn=None, filter=None, instance_id=None, is_ssl=None, password=None,
                 port=None, region_id=None, server=None, standby_server=None):
        self.account = account  # type: str
        self.base_dn = base_dn  # type: str
        self.filter = filter  # type: str
        self.instance_id = instance_id  # type: str
        self.is_ssl = is_ssl  # type: str
        self.password = password  # type: str
        self.port = port  # type: str
        self.region_id = region_id  # type: str
        self.server = server  # type: str
        self.standby_server = standby_server  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(VerifyInstanceLDAPAuthServerRequest, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.account is not None:
            result['Account'] = self.account
        if self.base_dn is not None:
            result['BaseDN'] = self.base_dn
        if self.filter is not None:
            result['Filter'] = self.filter
        if self.instance_id is not None:
            result['InstanceId'] = self.instance_id
        if self.is_ssl is not None:
            result['IsSSL'] = self.is_ssl
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
        if m.get('Filter') is not None:
            self.filter = m.get('Filter')
        if m.get('InstanceId') is not None:
            self.instance_id = m.get('InstanceId')
        if m.get('IsSSL') is not None:
            self.is_ssl = m.get('IsSSL')
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


class VerifyInstanceLDAPAuthServerResponseBody(TeaModel):
    def __init__(self, request_id=None):
        self.request_id = request_id  # type: str

    def validate(self):
        pass

    def to_map(self):
        _map = super(VerifyInstanceLDAPAuthServerResponseBody, self).to_map()
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


class VerifyInstanceLDAPAuthServerResponse(TeaModel):
    def __init__(self, headers=None, body=None):
        self.headers = headers  # type: dict[str, str]
        self.body = body  # type: VerifyInstanceLDAPAuthServerResponseBody

    def validate(self):
        self.validate_required(self.headers, 'headers')
        self.validate_required(self.body, 'body')
        if self.body:
            self.body.validate()

    def to_map(self):
        _map = super(VerifyInstanceLDAPAuthServerResponse, self).to_map()
        if _map is not None:
            return _map

        result = dict()
        if self.headers is not None:
            result['headers'] = self.headers
        if self.body is not None:
            result['body'] = self.body.to_map()
        return result

    def from_map(self, m=None):
        m = m or dict()
        if m.get('headers') is not None:
            self.headers = m.get('headers')
        if m.get('body') is not None:
            temp_model = VerifyInstanceLDAPAuthServerResponseBody()
            self.body = temp_model.from_map(m['body'])
        return self


